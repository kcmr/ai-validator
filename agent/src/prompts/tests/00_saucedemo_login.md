---
test: saucedemo_login
url: https://www.saucedemo.com/
title: Casos de Prueba para la Funcionalidad de Login en SauceDemo
---

# Autenticación de Usuarios

## 1 Login Exitoso
- **Objetivo**: Verificar que los usuarios pueden iniciar sesión correctamente
- **Precondiciones**: Usuario en la página de login
- **Pasos**:
  1. Ingresar nombre de usuario válido (ej: standard_user)
  2. Ingresar contraseña válida (ej: secret_sauce)
  3. Hacer clic en el botón "Login"
- **Resultado Esperado**: El usuario es redirigido a la página de inventario
- **Criterios de Aceptación**:
  - URL cambia a `/inventory.html`
  - Se muestra el menú de navegación
  - Se visualiza la lista de productos

## 2 Login con Credenciales Inválidas
- **Objetivo**: Verificar que el sistema rechaza credenciales incorrectas
- **Precondiciones**: Usuario en la página de login (previamente logout)
- **Pasos**:
  1. Ingresar nombre de usuario incorrecto o contraseña incorrecta
  2. Hacer clic en el botón "Login"
- **Resultado Esperado**: Se muestra un mensaje de error
- **Criterios de Aceptación**:
  - Permanece en la página de login
  - Se muestra un mensaje de error visible  
