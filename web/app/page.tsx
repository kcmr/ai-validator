"use client";

import { useState } from "react";

export default function Home() {
  const [status, setStatus] = useState<string>("");

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const form = new FormData(event.currentTarget);
    const username = form.get("username");
    const password = form.get("password");

    if (!username || !password) {
      setStatus("Debes completar usuario y contraseña.");
      return;
    }

    setStatus(
      `Credenciales recibidas para ${username}. (Este formulario no realiza autenticación real.)`
    );
  };

  return (
    <main className="container">
      <section className="card" aria-label="Formulario de acceso de demostración">
        <h1>Validador de Pruebas</h1>
        <p>
          Introduce un usuario y contraseña ficticios para que el agente de validación
          pueda ejecutar sus pruebas end-to-end.
        </p>

        <form className="form" onSubmit={handleSubmit}>
          <label htmlFor="username">Usuario</label>
          <input id="username" name="username" placeholder="ej. ana.tester" />

          <label htmlFor="password">Contraseña</label>
          <input
            id="password"
            name="password"
            type="password"
            placeholder="Contraseña ficticia"
          />

          <button type="submit">Iniciar sesión</button>
        </form>

        {status && (
          <div role="status" className="status">
            {status}
          </div>
        )}
      </section>
    </main>
  );
}
