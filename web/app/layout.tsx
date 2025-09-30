import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "AI Validator Demo",
  description: "Formulario ficticio para pruebas automatizadas"
};

export default function RootLayout({
  children
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="es">
      <body>{children}</body>
    </html>
  );
}
