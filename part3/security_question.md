# Solución

Lo que haría para que mi sistema sea seguro teniendo en cuenta el Top 10 de OWASP, seria implementar las siguientes acciones:

## Implementaciones generales

- Realizar un modelado de amenazas y análisis de riesgos para identificar los requisitos de seguridad necesarios para el diseño de la aplicación.
- Utilizar patrones y principios de diseño seguros y arquitecturas de referencia.
- Incluir la seguridad en todas las etapas del ciclo de vida del desarrollo de software.
- Verificar que las aplicaciones cuenten con actualizaciones y parches, incluyendo las librerías de código.
- Configurar los controles de seguridad a valores seguros.
- Deshabilitar características innecesarias como puertos, servicios, páginas, cuentas, etc.
- Realizar un proceso de fortalecimiento para un entorno asegurado.
- Mantener actualizaciones y parches, incluyendo las librerías de código.
- Verificar que los registros se generen en un formato fácil de procesar por las herramientas de gestión de registros.
- Asegurarse de que los datos de registros son correctamente codificados para prevenir inyecciones o ataques en el sistema de monitoreo o registros.

Nota: Riesgos que se logran mitigar:

- A04:2021 - Diseño Inseguro
- A05:2021 - Configuración de Seguridad Incorrecta
- A06:2021 - Componentes Vulnerables y Desactualizados
- A08:2021 - Fallas en el Software y en la Integridad de los Datos
- A09:2021 - Fallas en el Registro y Monitoreo

## Implementaciones en aplicaciones móviles

- Cada usuario debe usar un método de autenticación y autorización, esto con el fin
  de que solo usuarios registrados, puedan entrar al sistema y acceder unicamente a
  los recursos que se le han asignado.
- Implementar autenticación multifactor para aumentar la seguridad.

Nota: Riesgo que se logra mitigar:

- A01:2021 - Pérdida de Control de Acceso

## Implementaciones en el servicio Backend

- El backend debe realizar criptografía ya que es donde se almacenan y procesan los datos sensibles.
- Validar todas las entradas de usuario y evitar la exposición de identificadores de sesión en la URL.
- Utilizar listas blancas de URL y puertos permitidos para limitar las solicitudes permitidas.

Nota: Riesgos que se logran mitigar:

- A02:2021 - Fallas Criptográficas
- A10:2021 - Falsificación de Solicitudes del Lado del Servidor

## Implementaciones en la base de datos

- Cada usuario debe usar un método de autenticación y autorización, esto con el fin
  de que solo usuarios registrados, puedan entrar al sistema y acceder unicamente a
  los recursos que se le han asignado.
- Limitar los privilegios de la cuenta de la base de datos utilizada por la aplicación.
- Utilizar contraseñas seguras y complejas, y evitar el almacenamiento de contraseñas en texto plano.
- Utilizar parámetros preparados y consultas parametrizadas en lugar de concatenar cadenas de consulta SQL.

Nota: Riesgos que se logran mitigar:

- A01:2021 - Pérdida de Control de Acceso
- A07:2021 - Fallas de Identificación y Autenticación
- A03:2021 - Inyección

## Implementaciones en el servicio Frontend

- Validar todas las entradas de usuario, incluyendo formularios web, cookies y parámetros de URL.
- Utilizar bibliotecas de validación de entrada y salida de datos.
- Utilizar contraseñas seguras y complejas, y evitar el almacenamiento de contraseñas en texto plano.
- Utilizar tokens de sesión seguros y configurar tiempos de expiración adecuados.
- Validar todas las entradas de usuario y evitar la exposición de identificadores de sesión en la URL.
- Realizar pruebas de seguridad y verificaciones manuales para identificar posibles debilidades en la identificación y autenticación.

Nota: Riesgos que se logran mitigar:

- A03:2021 - Inyección
- A07:2021 - Fallas de Identificación y Autenticación
