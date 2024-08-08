**Documentación del funcionamiento y desarrollo de la App Web**

En esta documentación, se detalla el proceso de creación y funcionamiento de una aplicación web utilizando Flask , SQLAlchemy y demás dependencias.
Se incluyen capturas de pantalla de cada paso importante.
1. Estructura del Proyecto
Descripción:

La estructura del proyecto incluye los siguientes archivos y directorios:
- ARCHIVOS
– db.py
– main.py
– models.py
– index.html
– editar.html
– main.css
– requirements.txt –
– DIRECTORIOS
– GestordeTareas
– Database
– Static
– Template

Explicación del Archivo main.py 

1. Importaciones
 
  os: Módulo que proporciona una forma de usar funcionalidades del sistema operativo.
Flask: Importa la clase principal y funciones necesarias para crear la aplicación web.
db: Importa el módulo db que contiene la configuración y las funciones relacionadas con la base de datos.
Tarea: Importa el modelo Tarea definido en el módulo models. datetime: Importa la clase datetime para manejar fechas y horas.

2. Inicialización de la Aplicación Flask
app: Crea una instancia de la clase Flask.
secret_key: Configura una clave secreta para manejar sesiones y mensajes flash.

3. Ruta Principal (/)
  @app.route('/'): Define la ruta principal de la aplicación. home(): Función que maneja las solicitudes a la ruta principal.
● session=db.SessionLocal():Creaunasesiónconlabasededatos. ● todas_las_tareas=session.query(Tarea).all():Consultatodaslas
tareas en la base de datos.
● session.close():Cierralasesióndelabasededatos.
● returnrender_template("index.html",
lista_de_tareas=todas_las_tareas): Renderiza la plantilla index.html y pasa la lista de tareas a la plantilla.

 4. Ruta para Crear Nuevas Tareas (/crear-tarea)
 ● @app.route('/crear-tarea',methods=['POST']):Definelarutapara manejar la creación de nuevas tareas mediante el método POST.
● crear():Funciónquemanejalacreacióndenuevastareas.
○ session=db.SessionLocal():Creaunasesiónconlabasede
datos.
○ tarea:CreaunanuevainstanciadelmodeloTareaconlosdatos
del formulario.
○ session.add(tarea):Añadelanuevatareaalasesióndelabase
de datos.
○ session.commit():Confirmalatransacciónparaguardarlatarea
en la base de datos.
○ session.close():Cierralasesióndelabasededatos.
○ returnredirect(url_for('home')):Redirigealapáginaprincipal.

Descripción Detallada del Archivo

El archivo main.py es el núcleo de la aplicación Flask. Aquí se configuran las rutas y las interacciones principales con la base de datos.

1. Configuración y Secret Key: La aplicación Flask se configura y se define una clave secreta para manejar las sesiones de manera segura.

2. Ruta Principal: En la ruta principal (/), se abre una sesión con la base de datos para consultar todas las tareas existentes y se renderiza la plantilla index.html con la lista de tareas.

3. Crear Nuevas Tareas: La ruta /crear-tarea permite agregar nuevas tareas a la base de datos. Los datos del formulario se utilizan para crear una nueva tarea, que luego se guarda en la base de datos.

Ejemplo de Uso

Para agregar una nueva tarea, el usuario completará un formulario en la interfaz web. Los datos del formulario se enviarán a la ruta /crear-tarea mediante una solicitud POST. La función crear() procesará estos datos, creará una nueva tarea y la guardará en la base de datos. Finalmente, el usuario será redirigido a la página principal, donde verá la lista actualizada de tareas.

Archivo db.py

El contenido del archivo db.py es el siguiente, según la captura de pantalla:

Importaciones

Configuración de la URL de la Base de Datos

Descripción: Definimos la URL de la base de datos, en este caso, utilizando SQLite. La base de datos se guardará en un archivo llamado tareas.db en el directorio actual.

Creación del Motor de la Base de Datos

Descripción: Creamos el motor de la base de datos utilizando la URL configurada. El motor es responsable de gestionar las conexiones a la base de datos.

Configuración de la Sesión de la Base de Datos

Descripción: Configuramos la sesión de la base de datos con sessionmaker. 
Esta configuración incluye desactivar el autocommit y el autoflush para que los cambios en la base de datos sean gestionados manualmente.

Definición del Modelo Base

Descripción: Definimos un modelo base utilizando declarative_base. 
Todas las clases de modelos en nuestra aplicación heredarán de este modelo base, facilitando la gestión y creación de tablas.
   
Descripción detallada del archivo models.py

Descripción: El archivo models.py define el modelo de datos para nuestra aplicación de gestión de tareas. 

Utiliza SQLAlchemy para mapear esta clase a una tabla en la base de datos.

1. Importaciones Necesarias: Importamos las clases y funciones necesarias de SQLAlchemy.

2. Definición de la Clase Tarea: Creamos una clase Tarea que define la estructura de la tabla tarea en la base de datos.

3. Inicialización del Modelo: El método __init__ se encarga de inicializar las propiedades de una nueva instancia de Tarea.

4. Métodos de Representación: Definimos los métodos __repr__ y __str__ para proporcionar representaciones significativas de las instancias de Tarea.

Documentación: Archivo index.html

Descripción detallada del archivo índex.html

Descripción: El archivo index.html define la estructura y el contenido de la página principal de la aplicación de gestión de tareas. 
Utiliza Jinja2 para renderizar contenido dinámico y Bootstrap para el diseño responsivo. 
Además,incluye un pequeño script en JavaScript para manejar los mensajes flash.

1. Estructura HTML Básica: Define la estructura del documento,
incluyendo la inclusión de la hoja de estilos.

2. Contenido Principal: Contiene el contenedor principal y las filas y
columnas para el diseño.

3. Lista de Tareas: Utiliza un bucle for para mostrar cada tarea en una
lista ordenada.

4. Formulario de Creación de Nuevas Tareas: Proporciona campos de
entrada para el contenido de la tarea, la categoría y la fecha límite.

5. Código JavaScript: Maneja los mensajes flash para proporcionar
retroalimentación visual al usuario.
 
 
Descripción detallada del archivo editar.html
Descripción: El archivo editar.html define la estructura y el contenido de la página de edición de tareas. 
Utiliza Jinja2 para renderizar contenido dinámico y Bootstrap para el diseño responsivo.

1. Estructura HTML Básica: Define la estructura del documento, incluyendo la inclusión de hojas de estilo.

2. Contenedor Principal: Contiene el contenedor principal y las filas y columnas para el diseño responsivo.

3. Formulario de Edición de Tareas: Proporciona campos de entrada para el contenido de la tarea, la categoría y la fecha límite, con valores pre-rellenados para la tarea actual.

Descripción detallada del archivo main.css
Descripción: El archivo main.css contiene las reglas de estilo CSS que definen la apariencia de la aplicación web. 
Utiliza degradados para el fondo, fuentes personalizadas para los títulos y estilos específicos para indicar tareas completadas.

1. Estilo del Cuerpo (body): Aplica un degradado de fondo que va de #f2fcfe a #1c92d2.

2. Estilo del Título (.titulo): Utiliza la fuente 'Permanent Marker' de Google Fonts.

3. Estilo para Tareas Hechas (.tarea_hecha): Aplica una línea que atraviesa el texto y cambia el color a gris claro para indicar que la tarea está completada.


 
Descripción detallada del archivo requirements.txt
Descripción: El archivo requirements.txt contiene las dependencias necesarias para ejecutar la aplicación de gestión de tareas. 

Cada dependencia está especificada junto con su versión para asegurar la compatibilidad y estabilidad del proyecto.

1. SQLAlchemy: Una biblioteca ORM que facilita la interacción con bases de datos relacionales.

2. Flask: Un microframework de Python utilizado para desarrollar aplicaciones web.

Imágenes del funcionamiento de la aplicación:
  

Consulta a la base de datos desde terminal :

Consulta de base de datos desde DB Browser:

Conclusión
Completar esta tarea ha sido un gran paso en mi desarrollo como programador. 
A lo largo de este proyecto, he aprendido a manejar diferentes componentes cruciales en la construcción de una aplicación web robusta y funcional. 
Estos son algunos de los aspectos más destacados y aprendizajes clave de esta experiencia:

1. Desarrollo con Flask

● Configuración y Estructura: Aprendera estructurar una aplicación
 Flask, configurar rutas, manejar formularios y renderizar plantillas con

● Jinja2.

● Manejo de Sesiones y Mensajes Flash:Implementación de sesiones y mensajes flash para mejorar la experiencia del usuario.

2. Gestión de Bases de Datos con SQLAlchemy

● Modelado de Datos: Definición de modelos de datos utilizando SQLAlchemy y comprensión de cómo se mapean a tablas en la base de datos.

● Operaciones CRUD: Implementación de operaciones de creación, lectura, actualización y eliminación (CRUD) sobre los datos almacenados.

3. Diseño de Interfaces Web

● Uso de Bootstrap:Aplicación de Bootstrap para crear interfaces web atractivas y responsivas.

● CSS Personalizado:Personalización de estilos con CSS para mejora la presentación visual de la aplicación.

4. Gestión de Dependencias
● Archivo requirements.txt:
Creación y manejo del archivo requirements.txt para asegurar que todas las dependencias del proyecto estén correctamente especificadas y gestionadas.
