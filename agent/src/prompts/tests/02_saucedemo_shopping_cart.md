---
test: saucedemo_product_catalog
url: https://www.saucedemo.com/
title: Casos de Prueba para la Funcionalidad de Carrito de Compras en SauceDemo
---

# Carrito de Compras

## 1 Agregar Productos al Carrito
- **Objetivo**: Verificar que los productos se agregan correctamente al carrito
- **Precondiciones**: Usuario autenticado en la página de inventario (user: standard_user, password: secret_sauce)
- **Pasos**:
  1. Hacer clic en "Add to cart" para uno o más productos
  2. Navegar al carrito
- **Resultado Esperado**: Los productos agregados aparecen en el carrito
- **Criterios de Aceptación**:
  - El contador del carrito se actualiza
  - Los productos aparecen en `/cart.html`
  - Se muestra la cantidad y descripción correctos

## 2 Cantidades en el Carrito
- **Objetivo**: Verificar que se muestra la cantidad correcta de cada producto
- **Precondiciones**: Usuario autenticado en la página de inventario (user: standard_user, password: secret_sauce)
- **Resultado Esperado**:
  - Se muestra la columna QTY con la cantidad
  - La cantidad es correcta para productos agregados múltiples veces
- **Criterios de Aceptación**:
  - QTY column visible y correcta
  - Total de precios calculado correctamente

## 3 Continuar Comprando
- **Objetivo**: Verificar que el usuario puede volver al catálogo desde el carrito
- **Precondiciones**:
  - Usuario autenticado en la página de inventario (user: standard_user, password: secret_sauce)
  - Usuario con productos en el carrito
- **Pasos**:
  1. Hacer clic en "Continue Shopping"
- **Resultado Esperado**: Regresa a la página de inventario, carrito mantiene los productos
- **Criterios de Aceptación**:
  - URL es `/inventory.html`
  - Los productos permanecen en el carrito