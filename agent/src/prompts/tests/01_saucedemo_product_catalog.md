---
test: saucedemo_product_catalog
url: https://www.saucedemo.com/
title: Casos de Prueba para la Funcionalidad de Catálogo de Productos en SauceDemo
---

# Catálogo de Productos

## 1 Visualización de Productos
- **Objetivo**: Verificar que se muestra correctamente el catálogo de productos
- **Precondiciones**: Usuario autenticado (user: standard_user, password: secret_sauce)
- **Resultado Esperado**:
  - Se muestran todos los productos disponibles
  - Cada producto muestra: nombre, descripción, precio, imagen y botón "Add to cart"
  - Los productos se cargan correctamente
- **Criterios de Aceptación**:
  - Mínimo 6 productos visibles
  - Las imágenes se cargan sin errores

## 2 Ordenamiento de Productos
- **Objetivo**: Verificar que el sistema ordena los productos correctamente
- **Precondiciones**: Usuario autenticado en la página de inventario (user: standard_user, password: secret_sauce)
- **Opciones de Ordenamiento a Probar**:
  1. Name (A to Z)
  2. Name (Z to A)
  3. Price (low to high)
  4. Price (high to low)
- **Resultado Esperado**: Los productos se reordenan según la opción seleccionada
- **Criterios de Aceptación**:
  - El orden es correcto para cada opción
  - El cambio es inmediato

## 3 Información de Productos
- **Objetivo**: Verificar que la información de cada producto es correcta
- **Precondiciones**: Usuario autenticado en la página de producto (user: standard_user, password: secret_sauce)
- **Criterios de Aceptación**:
  - Nombre del producto visible
  - Descripción completa del producto
  - Precio correcto (ej: $29.99, $9.99, etc.)
  - Imagen del producto cargada correctamente