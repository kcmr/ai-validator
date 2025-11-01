# Test Plan - Swag Labs (saucedemo.com)

## Descripción General
Swag Labs es una aplicación de e-commerce de demostración diseñada para practicar pruebas automatizadas. La aplicación permite a los usuarios iniciar sesión, navegar por un catálogo de productos, agregar artículos al carrito, y completar un proceso de compra.

---

## Funcionalidades Principales

### 1. Autenticación de Usuarios

#### 1.1 Login Exitoso
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

#### 1.2 Login con Credenciales Inválidas
- **Objetivo**: Verificar que el sistema rechaza credenciales incorrectas
- **Precondiciones**: Usuario en la página de login
- **Pasos**:
  1. Ingresar nombre de usuario incorrecto o contraseña incorrecta
  2. Hacer clic en el botón "Login"
- **Resultado Esperado**: Se muestra un mensaje de error
- **Criterios de Aceptación**:
  - Permanece en la página de login
  - Se muestra un mensaje de error visible

#### 1.3 Usuarios Especiales
- **Objetivo**: Probar diferentes tipos de usuarios para validar comportamientos específicos
- **Usuarios a Probar**:
  - `standard_user`: Usuario normal
  - `locked_out_user`: Usuario bloqueado (no puede acceder)
  - `problem_user`: Usuario que genera problemas en la aplicación
  - `performance_glitch_user`: Usuario que causa glitches de rendimiento
  - `error_user`: Usuario que genera errores
  - `visual_user`: Usuario que causa problemas visuales

---

### 2. Catálogo de Productos

#### 2.1 Visualización de Productos
- **Objetivo**: Verificar que se muestra correctamente el catálogo de productos
- **Precondiciones**: Usuario autenticado (user: standard_user, password: secret_sauce)
- **Resultado Esperado**:
  - Se muestran todos los productos disponibles
  - Cada producto muestra: nombre, descripción, precio, imagen y botón "Add to cart"
  - Los productos se cargan correctamente
- **Criterios de Aceptación**:
  - Mínimo 6 productos visibles
  - Las imágenes se cargan sin errores

#### 2.2 Ordenamiento de Productos
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

#### 2.3 Información de Productos
- **Objetivo**: Verificar que la información de cada producto es correcta
- **Precondiciones**: Usuario autenticado en la página de producto (user: standard_user, password: secret_sauce)
- **Criterios de Aceptación**:
  - Nombre del producto visible
  - Descripción completa del producto
  - Precio correcto (ej: $29.99, $9.99, etc.)
  - Imagen del producto cargada correctamente

---

### 3. Carrito de Compras

#### 3.1 Agregar Productos al Carrito
- **Objetivo**: Verificar que los productos se agregan correctamente al carrito
- **Precondiciones**: Usuario en la página de inventario
- **Pasos**:
  1. Hacer clic en "Add to cart" para uno o más productos
  2. Navegar al carrito
- **Resultado Esperado**: Los productos agregados aparecen en el carrito
- **Criterios de Aceptación**:
  - El contador del carrito se actualiza
  - Los productos aparecen en `/cart.html`
  - Se muestra la cantidad y descripción correctos

#### 3.2 Cantidades en el Carrito
- **Objetivo**: Verificar que se muestra la cantidad correcta de cada producto
- **Resultado Esperado**:
  - Se muestra la columna QTY con la cantidad
  - La cantidad es correcta para productos agregados múltiples veces
- **Criterios de Aceptación**:
  - QTY column visible y correcta
  - Total de precios calculado correctamente

#### 3.3 Continuar Comprando
- **Objetivo**: Verificar que el usuario puede volver al catálogo desde el carrito
- **Precondiciones**: Usuario con productos en el carrito
- **Pasos**:
  1. Hacer clic en "Continue Shopping"
- **Resultado Esperado**: Regresa a la página de inventario, carrito mantiene los productos
- **Criterios de Aceptación**:
  - URL es `/inventory.html`
  - Los productos permanecen en el carrito

---

### 4. Proceso de Checkout

#### 4.1 Step 1 - Información Personal
- **Objetivo**: Verificar que el formulario de información personal funciona correctamente
- **Precondiciones**: Usuario con productos en carrito
- **Pasos**:
  1. Hacer clic en "Checkout"
  2. Llenar formulario con datos válidos (First Name, Last Name, Zip/Postal Code)
  3. Hacer clic en "Continue"
- **Resultado Esperado**: Acceso al paso 2 del checkout
- **Criterios de Aceptación**:
  - URL es `/checkout-step-one.html`
  - Todos los campos son requeridos
  - Validación de campos (si aplica)
  - Navegación exitosa a Step 2

#### 4.2 Step 2 - Revisión del Pedido
- **Objetivo**: Verificar que se muestra la información del pedido correctamente
- **Precondiciones**: Usuario completó Step 1
- **Resultado Esperado**:
  - Se muestra el resumen de productos
  - Se muestra información de pago
  - Se muestra información de envío
  - Se muestra el total (Item total, Tax, Total)
- **Criterios de Aceptación**:
  - URL es `/checkout-step-two.html`
  - Información de pago visible: "SauceCard #31337"
  - Información de envío visible: "Free Pony Express Delivery!"
  - Cálculo de totales correcto

#### 4.3 Finalización de Compra
- **Objetivo**: Verificar que el proceso de compra se completa exitosamente
- **Precondiciones**: Usuario en Step 2 del checkout
- **Pasos**:
  1. Hacer clic en "Finish"
- **Resultado Esperado**: Compra completada exitosamente
- **Criterios de Aceptación**:
  - URL es `/checkout-complete.html`
  - Mensaje "Checkout: Complete!" visible
  - Mensaje "Thank you for your order!" visible
  - Imagen de confirmación (Pony Express) visible
  - Botón "Back Home" disponible

#### 4.4 Cancelar Checkout
- **Objetivo**: Verificar que el usuario puede cancelar el checkout en cualquier paso
- **Precondiciones**: Usuario en cualquier paso del checkout
- **Pasos**:
  1. Hacer clic en "Cancel"
- **Resultado Esperado**: Regresa al carrito
- **Criterios de Aceptación**:
  - URL regresa a `/cart.html`
  - Los productos permanecen en el carrito

---

### 5. Navegación y UI

#### 5.1 Menú de Navegación
- **Objetivo**: Verificar que el menú de navegación funciona correctamente
- **Elementos del Menú**:
  - All Items
  - About
  - Logout
  - Reset App State
- **Criterios de Aceptación**:
  - Menú se abre y cierra correctamente
  - Todos los enlaces funcionan
  - "Logout" cierra la sesión
  - "Reset App State" reinicia la aplicación

#### 5.2 Footer
- **Objetivo**: Verificar que el footer contiene los enlaces correctos
- **Enlaces Esperados**:
  - Twitter
  - Facebook
  - LinkedIn
  - Copyright notice
- **Criterios de Aceptación**:
  - Todos los enlaces son clickeables
  - Los enlaces abren en pestaña nueva (si aplica)
  - URLs son correctas

#### 5.3 Responsive Design
- **Objetivo**: Verificar que la aplicación funciona en diferentes tamaños de pantalla
- **Tamaños a Probar**:
  - Desktop (1920x1080, 1366x768)
  - Tablet (768x1024)
  - Mobile (375x667, 414x896)
- **Criterios de Aceptación**:
  - Elementos se ajustan correctamente
  - No hay desbordamientos de contenido
  - Menú es accesible en todos los tamaños

---

### 6. Búsqueda y Filtrado

#### 6.1 Búsqueda de Productos
- **Objetivo**: Verificar que el usuario puede encontrar productos específicos
- **Nota**: Si existe funcionalidad de búsqueda
- **Criterios de Aceptación**:
  - Los resultados de búsqueda son relevantes
  - Se filtran productos correctamente

---

## Casos de Prueba de Regresión

### 7.1 Flujo Completo de Compra
- **Objetivo**: Realizar una compra completa del inicio al fin
- **Pasos**:
  1. Login con credenciales válidas
  2. Seleccionar múltiples productos (al menos 3)
  3. Ordenar productos (probar diferentes opciones)
  4. Ir al carrito
  5. Completar checkout con información válida
  6. Confirmar compra exitosa
- **Resultado Esperado**: Compra completada sin errores
- **Criterios de Aceptación**:
  - Página de confirmación muestra "Thank you for your order!"
  - Todos los pasos se completan sin errores

### 7.2 Validación de Campos
- **Objetivo**: Verificar que los campos requeridos son validados
- **Campos a Validar**:
  - First Name (requerido)
  - Last Name (requerido)
  - Zip/Postal Code (requerido)
  - Username (requerido)
  - Password (requerido)
- **Criterios de Aceptación**:
  - No se puede proceder sin llenar campos requeridos
  - Se muestra mensaje de error descriptivo

---

## Casos de Prueba de Manejo de Errores

### 8.1 Manejo de Errores de Red
- **Objetivo**: Verificar que la aplicación maneja errores de red gracefully
- **Criterios de Aceptación**:
  - No se bloquea la aplicación
  - Se muestra mensaje de error comprensible
  - Usuario puede reintentar

### 8.2 Validación de Datos Inválidos
- **Objetivo**: Verificar que el sistema valida datos de entrada
- **Casos a Probar**:
  - Caracteres especiales en nombres
  - Códigos postales inválidos
  - Campos vacíos
- **Criterios de Aceptación**:
  - Se rechazan datos inválidos
  - Se muestra mensaje de error claro

---

## Criterios de Aceptación Global

- ✅ No hay errores en la consola (excepto los esperados)
- ✅ Todos los enlaces funcionan correctamente
- ✅ Las imágenes cargan correctamente
- ✅ La aplicación es responsive
- ✅ La navegación es intuitiva
- ✅ Los mensajes de error son claros
- ✅ No hay retrasos significativos en la carga

---

## Prioridad de Pruebas

### Alta Prioridad
1. Autenticación (Login/Logout)
2. Catálogo de Productos
3. Agregar productos al carrito
4. Proceso de Checkout completo
5. Finalización de compra

### Prioridad Media
1. Ordenamiento de productos
2. Navegación
3. Validación de formularios
4. Usuarios especiales

### Baja Prioridad
1. Footer y enlaces
2. Responsive design
3. Manejo de errores
4. Performance

---

## Ambiente de Prueba

- **URL**: https://www.saucedemo.com/
- **Navegadores**: Chrome, Firefox, Safari, Edge
- **Contraseña General**: secret_sauce
- **Usuarios Disponibles**: standard_user, locked_out_user, problem_user, performance_glitch_user, error_user, visual_user

---

## Notas Adicionales

- La aplicación es una herramienta de aprendizaje, por lo que ciertos "usuarios especiales" tienen comportamientos anómalos intencionales para practicar pruebas en diferentes escenarios
- El carrito persiste durante la sesión
- No hay costo real en las transacciones
- La dirección de envío es solo de demostración
