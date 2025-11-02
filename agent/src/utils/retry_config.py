"""HTTP retry configuration with exponential backoff and Retry-After header support."""

import logging
from typing import Any

from httpx import AsyncClient, AsyncHTTPTransport, HTTPStatusError
from pydantic_ai.retries import AsyncTenacityTransport, RetryConfig, wait_retry_after
from tenacity import (
    RetryCallState,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

logger = logging.getLogger(__name__)


def log_retry_attempt(retry_state: RetryCallState) -> None:
    """Log retry attempts with error details and wait time."""
    if retry_state.attempt_number > 1:
        exc = retry_state.outcome.exception() if retry_state.outcome else None
        next_wait = retry_state.next_action.sleep if retry_state.next_action else 0

        logger.warning(
            f"Retry #{retry_state.attempt_number} | "
            f"Error: {type(exc).__name__} | "
            f"Wait: {next_wait:.1f}s"
        )


def create_retrying_client(mode: str = "standard") -> AsyncClient:
    """
    Create an HTTP client with automatic retry for rate limit handling.

    Optimized for 10 RPM (requests per minute) rate limits.

    Args:
        mode: Configuration mode:
            - "standard": 10 attempts, max 5 minutes (RECOMMENDED)
            - "aggressive": 15 attempts, max 10 minutes (for persistent 429s)
            - "conservative": 5 attempts, max 1 minute (for strict timeouts)

    Returns:
        AsyncClient: Configured with automatic retry on transport layer
    """

    modes = {
        "standard": {
            "wait_multiplier": 1,
            "wait_max": 60,
            "max_wait": 300,
            "stop_attempts": 10,
        },
        "aggressive": {
            "wait_multiplier": 2,
            "wait_max": 120,
            "max_wait": 600,
            "stop_attempts": 15,
        },
        "conservative": {
            "wait_multiplier": 1,
            "wait_max": 10,
            "max_wait": 60,
            "stop_attempts": 5,
        },
    }

    if mode not in modes:
        raise ValueError(f"Mode must be one of: {list(modes.keys())}")

    cfg = modes[mode]

    def validate_response(response: Any) -> None:
        """Raise HTTPStatusError for retriable HTTP status codes."""
        if response.status_code in (429, 502, 503, 504):
            response.raise_for_status()

    retry_config: RetryConfig = {
        "retry": retry_if_exception_type((HTTPStatusError, ConnectionError)),
        "wait": wait_retry_after(
            fallback_strategy=wait_exponential(
                multiplier=cfg["wait_multiplier"], max=cfg["wait_max"]
            ),
            max_wait=cfg["max_wait"],
        ),
        "stop": stop_after_attempt(cfg["stop_attempts"]),
        "reraise": True,
        "before_sleep": log_retry_attempt,
    }

    transport = AsyncTenacityTransport(
        config=retry_config,
        wrapped=AsyncHTTPTransport(),
        validate_response=validate_response,
    )

    logger.info(
        f"HTTP client with retry configured ({mode}): "
        f"max_attempts={cfg['stop_attempts']}, max_wait={cfg['max_wait']}s"
    )

    return AsyncClient(transport=transport)
