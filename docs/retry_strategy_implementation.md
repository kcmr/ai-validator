# Retry Strategy Implementation

**Version:** 1.0  
**Date:** November 2, 2025  
**Objective:** To prevent `HTTP 429 (Too Many Requests)` errors by intelligently handling API rate limits.

---

## 1. Problem Statement

When consuming third-party APIs, especially those with free or tiered plans, it is common to encounter rate limits. Our system, which relies on an LLM with a limit of 10 requests per minute (RPM), was experiencing execution failures due to `HTTP 429` errors.

**Previous State:**
- **Limit:** 10 RPM.
- **Error:** `HTTP 429 (Too Many Requests)` when the limit was exceeded.
- **Impact:** The agent would fail immediately upon receiving a 429 error, without any attempt to recover. The server often provides a `Retry-After` header indicating when it's safe to try again, but this was being ignored.

This lack of a retry mechanism made the system unreliable, especially under moderate load.

---

## 2. The Implemented Solution

A two-layer, intelligent retry architecture was implemented to provide resilience and reliability. This solution handles rate-limiting errors gracefully at the HTTP transport layer, making it transparent to the agent's core logic.

### Two-Layer Defense Architecture

```
+-----------------------------------------+
|         Layer 2: Agent Retry            |
|      (Second line of defense)           |
+------------------┬----------------------+
                   |
+------------------▼----------------------+
|   Layer 1: Smart HTTP Transport Retry   |
|      (First line of defense)            |
|  - Respects 'Retry-After' headers       |
|  - Implements exponential backoff       |
|  - Configured for up to 10 attempts     |
+-----------------------------------------+
```

#### Key Advantages of this Architecture:

-   **Respects `Retry-After` Headers:** The system automatically parses the `Retry-After` header from 429 responses and waits for the specified duration. This is the most efficient way to handle rate limits.
-   **Exponential Backoff:** If a `Retry-After` header is not present, the system falls back to an exponential backoff strategy (e.g., waiting 1s, 2s, 4s, 8s...).
-   **Configurable Limits:** The retry mechanism is configured with a maximum number of attempts and a total maximum wait time to prevent indefinite hangs.
-   **Transparency:** The logic is contained within the HTTP client, so the agent's code does not need to be aware of the retry mechanism.
-   **Efficiency:** Retries are handled at the lowest possible level (HTTP transport), preventing unnecessary re-execution of higher-level logic.

---

## 3. Technical Components

The solution is built upon the `tenacity` library and integrated via `pydantic-ai`'s extensible transport layer.

### `RetryConfig`

This is a configuration dictionary that defines the behavior of the retry mechanism. The key parameters are:

-   `stop`: Defines when to stop retrying. The primary strategy is `stop_after_attempt(10)`.
-   `wait`: Defines the waiting strategy between retries. We use `wait_retry_after`, a smart strategy that prioritizes the `Retry-After` header and uses exponential backoff as a fallback.
-   `retry`: Specifies the conditions for a retry, primarily `HTTPStatusError` for codes like 429, 502, 503, and 504.
-   `reraise`: A boolean (`True`) that ensures the original exception is re-thrown if all retry attempts fail, allowing for clean error handling upstream.
-   `before_sleep`: An optional callback used for logging each retry attempt, which is invaluable for monitoring and debugging.

### `AsyncTenacityTransport`

This is a custom HTTP transport that wraps the standard `AsyncHTTPTransport`. It intercepts outgoing requests and incoming responses, applying the logic defined in the `RetryConfig`. It is the core component that enables the retry functionality.

### `wait_retry_after`

A specialized wait strategy that intelligently handles rate-limiting scenarios:
1.  It first attempts to parse the `Retry-After` header from the HTTP response. It supports both seconds and HTTP-date formats.
2.  If the header is absent, it reverts to a configurable `fallback_strategy`, which is set to exponential backoff.
3.  It respects a `max_wait` parameter to cap the total time spent waiting.

---

## 4. Implementation Overview

The integration was achieved in three high-level steps:

1.  **Dependency Update:** The `tenacity` library was added as a project dependency.

2.  **Retry Configuration Module:** A dedicated module was created to define the `RetryConfig` and a factory function (`create_retrying_client`) that returns an `httpx.AsyncClient` pre-configured with the `AsyncTenacityTransport`. This centralizes the retry logic.

    The standard configuration is optimized for a 10 RPM limit:
    -   **Attempts:** 10
    -   **Backoff:** Starts at 1 second and doubles, capped at 60 seconds.
    -   **Max Wait:** 5 minutes.

3.  **Integration with LLM Providers:** The pre-configured HTTP client is injected into the LLM providers (e.g., `GoogleProvider`, `OpenAIProvider`) during their initialization. This ensures that any API call made by these providers automatically benefits from the retry logic.

---

## 5. Behavior and Alternative Configurations

The default configuration provides a robust defense against transient errors and standard rate limits.

**Expected Behavior (Exponential Backoff Fallback):**
-   **Attempt 1:** Immediate
-   **Attempt 2:** ~1s wait
-   **Attempt 3:** ~2s wait
-   **Attempt 4:** ~4s wait
-   ...and so on, up to a maximum wait time per attempt.

To accommodate different API limits or application requirements, alternative configurations are also available:

-   **Aggressive:** Uses more attempts and longer wait times, suitable for very restrictive rate limits.
-   **Conservative:** Uses fewer attempts and shorter wait times, suitable for applications with strict time constraints where failing fast is preferable to long waits.

---

## 6. Monitoring and Best Practices

### Monitoring
Logging is crucial for visibility into the retry mechanism. By setting up a logger for the retry module and using the `before_sleep` callback, we can log every retry attempt, the error that caused it, and the duration of the wait.

**Example Log Output:**
```
2025-11-02 10:15:45 - [RetryModule] - WARNING - Retry #2 after error: HTTPStatusError - 429 Client Error: Too Many Requests
```

### Best Practices
-   **Always use `wait_retry_after`:** It provides the most respectful and efficient handling of server-indicated rate limits.
-   **Combine HTTP and Agent Retries:** The two-layer approach provides comprehensive fault tolerance. The HTTP retry handles transient network/API issues, while the agent-level retry can handle broader logical failures.
-   **Enable `reraise=True`:** This simplifies error handling by propagating the original, specific exception rather than a generic `RetryError`.
-   **Test Configurations:** Simulate rate limits in a development environment to validate that the chosen retry configuration behaves as expected.
