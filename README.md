## PROGRAMACION AVANZADA ##

# Proyecto Final #

***Descripción del Proyecto***
- En este proyecto, crearás una aplicación de escritorio en Python que permita gestionar empleados y libros utilizando una base de datos. La aplicación constará de un sistema de login que permitirá el acceso a dos tipos de usuarios: Administrador y Empleado. Dependiendo del tipo de usuario, tendrán diferentes permisos y funcionalidades disponibles.

***Requisitos Funcionales***
1. Login de Usuarios
- La aplicación debe tener una pantalla de login donde el usuario debe ingresar su nombre de usuario y contraseña.
- Existen dos tipos de usuarios:
- - Administrador: Tiene acceso completo al sistema, permitiéndole gestionar empleados (CRUD de empleados).
- - Empleado: Puede gestionar los libros, pero no tiene acceso a la gestión de empleados. Los empleados pueden realizar un CRUD de libros y filtrar por algún dato.
- Si las credenciales son correctas, el usuario será dirigido a la vista correspondiente según su rol.
2. Gestión de Empleados (Solo para Administradores)
- El administrador podrá crear, leer, actualizar y eliminar registros de empleados en la base de datos. 
3. Gestión de Libros (Solo para Empleados)
- Los empleados podrán crear, leer, actualizar y eliminar registros de libros en la base de datos.
- Cada libro debe tener información como: ID, título, autor, editorial, año de publicación, y precio.
- Además, los empleados podrán filtrar libros por algún dato para mostrar únicamente los libros de una editorial específica.

***Estructura de la Base de Datos***
Para almacenar la información, usarás una base de datos. La base de datos tendrá al menos dos tablas principales:
1. Tabla de Libros
- id (***INT***, ***PRIMARY KEY***, ***AUTOINCREMENT***)
- titulo (***TEXT***)
- autor (***TEXT***)
- editorial (***TEXT***)
- año_publicacion (***DATE***)
- precio (***REAL***)
2. Tabla de Usuarios
- id (***INT***, ***PRIMARY KEY***, ***AUTOINCREMENT***)
- Nombre (***TEXT***)
- Apellido (***TEXT***)
- usuario (***TEXT***, único)
- contraseña (***TEXT***)
- rol (***TEXT***: "administrador" o "empleado")

