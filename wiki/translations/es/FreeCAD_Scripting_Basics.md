


{{TOCright}}


<div class="mw-translate-fuzzy">

## Archivos de guión de Python en FreeCAD {#archivos_de_guión_de_python_en_freecad}

FreeCAD está construido desde cero para que sea totalmente controlado por archivos de guión (scripts) de Python. Casi todas las partes de FreeCAD como la interfaz, el contenido de la escena, e incluso la representación de ese contenido en las vistas 3D, son accesibles desde el intérprete de Python incorporado, o desde sus propios archivos de guión. Como resultado, FreeCAD es, probablemente, una de las aplicaciones de diseño para ingeniería más personalizables de las disponibles en la actualidad.


</div>

FreeCAD is built from scratch to be totally controlled by Python scripts. Almost all parts of FreeCAD, such as the interface, the scene contents, and even the representation of this content in the 3D views, are accessible from the built-in Python interpreter or from your own scripts. As a result, FreeCAD is probably one of the most deeply customizable engineering applications available today.


<div class="mw-translate-fuzzy">

Si no estás familiarizado con Python, te recomendamos buscar tutoriales en Internet, y echar un rápido vistazo a su estructura. Python es un lenguaje muy fácil de aprender, sobre todo porque se puede ejecutar dentro de un intérprete, donde tanto comandos simples como programas completos pueden ejecutarse sobre la marcha, sin necesidad de compilar nada. FreeCAD ha incorporado un intérprete de Python. Si no ves la ventana denominada \'Consola de Python\' como se muestra más abajo, puedes activarla en el menú Vista -\> Vistas -\> Consola de Python para mostrar el interprete.


</div>


<div class="mw-translate-fuzzy">

### El intérprete {#el_intérprete}

Desde el intérprete puedes acceder a todos los módulos de Python instalados en el sistema, así como a los módulos de FreeCAD incorporados, y a todos los módulos adicionales de FreeCAD que puedas instalar más tarde. La imagen siguiente muestra el intérprete de Python:


</div>

From the interpreter, you can access all your system-installed Python modules, as well as the built-in FreeCAD modules, and all additional FreeCAD modules you installed later. The screenshot below shows the Python interpreter:

![The FreeCAD Python interpreter](images/screenshot_pythoninterpreter.jpg )


<div class="mw-translate-fuzzy">

También, puedes ejecutar código Python y navegar a través de las clases y funciones disponibles. FreeCAD proporciona un navegador de clases muy útil para la exploración de su nuevo mundo FreeCAD. Cuando se escribe el nombre de una clase conocida seguido de un punto (.) (significando que quieres añadir algo de esa clase), se abre una ventana del navegador de clases, donde se puede navegar entre las subclases y métodos disponibles. Cuando se selecciona algo, se mostrará un texto de ayuda asociado (si existe):


</div>

![The FreeCAD class browser](images/screenshot_classbrowser.jpg )


<div class="mw-translate-fuzzy">

Así que, comienza por esto escribiendo \'\'\'App. \'\'\' o \'\'\'Gui. \'\'\' y verás qué pasa. Otra forma más genérica de exploración del contenido de los módulos y las clases de Python es usar el comando print dir(). Por ejemplo, escribiendo **print dir()** listará todos los módulos cargados en FreeCAD. **print Dir(App)** te mostrará todo el interior del módulo App, etc.


</div>


<div class="mw-translate-fuzzy">

Otra característica útil del intérprete es la posibilidad de volver atrás en el historial de comandos y recuperar una línea de código que ya has escrito antes. Para navegar en el historial de comandos, sólo tienes que utilizar CTRL + flecha arriba o CTRL + flecha abajo.


</div>

Al hacer clic derecho en la ventana del intérprete también tienes otras opciones, tales como copiar todo el historial (útil para experimentar con algo, y luego hacer un archivo de guión con todo ello), o insertar el nombre de un archivo con su ruta completa.

[top](#top.md)


<div class="mw-translate-fuzzy">

### Ayuda de Python {#ayuda_de_python}

En el menú *Ayuda* de FreeCAD, encontrarás una entrada llamada \"Módulos de Python\", que abrirá una ventana que contiene una documentación completa, generada en tiempo real, de todos los módulos de Python a disposición del intérprete de FreeCAD, incluyendo Python y los módulos propios de FreeCAD, los módulos instalados por el sistema, y los módulos de FreeCAD adicionales. La documentación disponible depende del esfuerzo que cada desarrollador de los módulos puso en documentar su código pero, en general, los módulos de Python tienen la reputación de estar bastante bien documentados. Tu ventana de FreeCAD debe permanecer abierta para que este sistema de documentación funcione.


</div>

In the FreeCAD {{MenuCommand|Help}} menu, you\'ll find an entry labeled {{MenuCommand|Automatic python modules documentation}}, which will open a browser window containing a complete, realtime-generated documentation of all Python modules available to the FreeCAD interpreter, including Python and FreeCAD built-in modules, system-installed modules, and FreeCAD additional modules. The documentation available there depends on how much effort each module developer put into documenting his code, but Python modules have a reputation for being fairly well documented. Your FreeCAD window must stay open for this documentation system to work. The entry {{MenuCommand|Python scripting documentation}} will give you a quick link to the [Power users hub](Power_users_hub.md) wiki section.

[top](#top.md)


<div class="mw-translate-fuzzy">

## Módulos incorporados (Built-in) {#módulos_incorporados_built_in}

Como FreeCAD está diseñado para poder ser ejecutado sin interfaz gráfica de usuario, casi toda su funcionalidad se separa en dos grupos: las funciones principales, llamado App, y la funcionalidad de la interfaz gráfica de usuario, llamado Gui. Así, nuestros dos principales módulos incorporados en FreeCAD se llaman App y Gui. Estos dos módulos también son accesibles desde fuera de los archivos de guiones de comandos del intérprete, con los nombres respectivos de FreeCAD y FreeCADGui.


</div>

Since FreeCAD is designed so that it can also be run without a Graphical User Interface (GUI), almost all its functionality is separated into two groups: Core functionality, named `App`, and GUI functionality, named `Gui`. These two modules can also be accessed from scripts outside of the interpreter, by the names `FreeCAD` and `FreeCADGui` respectively.


<div class="mw-translate-fuzzy">

-   En el módulo **App**, encontrarás todo lo relacionado con la aplicación en sí, como los métodos para abrir o cerrar archivos, y lo relacionado con los documentos, como los ajustes del documento activo o listar su contenido.


</div>


<div class="mw-translate-fuzzy">

-   En el módulo **Gui**, encontrarás herramientas para la gestión de la interfaz gráfica de usuario y el acceso a sus elementos, como los entornos (workbench) y sus barras de herramientas y, más interesante, la representación gráfica de todo el contenido de FreeCAD.


</div>


<div class="mw-translate-fuzzy">

Listar los contenidos de todos esos módulos es una tarea poco \"productiva\" ya que crecen muy rápido a lo largo del desarrollo de FreeCAD. Pero las dos herramientas de navegación (el navegador de clases y la ayuda de Python) te debería dar, en cualquier momento, una documentación actualizada y completa de estos módulos.


</div>

[top](#top.md)


<div class="mw-translate-fuzzy">

### Los objetos App y los objetos GUI {#los_objetos_app_y_los_objetos_gui}

Como hemos dicho, en FreeCAD, todo esta repartido entre el núcleo y la representación. Esto incluye también los objetos en 3D. Puedes acceder a la definición de propiedades de los objetos (llamadas características de FreeCAD) a través del módulo de la aplicación, y cambiar la forma en que están representados en la pantalla a través del módulo GUI. Por ejemplo, un cubo tiene propiedades que lo definen, como anchura, longitud, altura, que se almacenan en un *objeto App*, y las propiedades de la representación, como el color de las caras, modo de dibujo, que se almacenan en su correspondiente *objeto GUI*.


</div>

As already mentioned, in FreeCAD everything is separated into core and representation. This includes the 3D objects. You can access defining properties of objects (called features in FreeCAD) via the `App` module, and change the way they are represented on screen via the `Gui` module. For example, a cube has properties that define it (like width, length, height) that are stored in an `App` object, and representation properties (like faces color, drawing mode) that are stored in a corresponding `Gui` object.

Esta forma de hacer las cosas permite una amplia gama de usos, como los algoritmos que sólo funcionan en la parte definitoria de características, sin la necesidad de ocuparse de ningun aspecto visual, o incluso redirigir el contenido del documento con la aplicación no-gráfica, como listas, hojas de cálculo o análisis de elementos.


<div class="mw-translate-fuzzy">

Por cada objeto App de tu documento, existe su correspondiente objeto GUI. El documento en sí mismo, en realidad, también tiene objetos App y GUI. Esto, por supuesto, sólo es válido cuando se ejecuta FreeCAD con su interfaz completo. En la versión de línea de comandos, no existe interfaz gráfica de usuario, por lo que sólo habrá objetos App. Ten en cuenta que la parte de interfaz gráfica de usuario de los objetos se genera nuevamente cada vez que un objeto App se marca como \"que se vuelven a calcular\" (por ejemplo, cuando uno de sus parámetros ha cambiado), por lo que los cambios que podría haber hecho al objeto Gui directamente podrían perderse.


</div>


<div class="mw-translate-fuzzy">

para acceder a la parte App de algo, escribe:


</div>


```python
myObject = App.ActiveDocument.getObject("ObjectName")
```


<div class="mw-translate-fuzzy">

donde \"ObjectName\" es el nombre de tu objeto. Tambien puedes poner:


</div>


```python
myObject = App.ActiveDocument.ObjectName
```


<div class="mw-translate-fuzzy">

para acceder la la parte GUI del mismo objeto, escribe:


</div>


```python
myViewObject = Gui.ActiveDocument.getObject("ObjectName")
```


<div class="mw-translate-fuzzy">

donde \"ObjectName\" es el nombre de tu objeto. También puedes escribir:


</div>


```python
myViewObject = App.ActiveDocument.ObjectName.ViewObject
```


<div class="mw-translate-fuzzy">

Si no tenemos GUI (por ejemplo en el modo de línea de comandos), la última línea no devolverá nada.


</div>

[top](#top.md)


<div class="mw-translate-fuzzy">

### Los objetos de documento {#los_objetos_de_documento}

En FreeCAD todo tu trabajo reside en el interior de los documentos. Un documento contiene la geometría y se pueden guardar en un archivo. Varios documentos se pueden abrir al mismo tiempo. El documento, al igual que la geometría contenidos en el interior, tiene objetos App y Gui. El objeto App contiene las definiciones de geometría real, mientras que el objeto Gui contiene los puntos de vista diferentes de tu documento. Puedes abrir varias ventanas, cada una mostrando tu trabajo con un factor de zoom diferente o un determinado punto de vista. Estas vistas forman parte del objeto Gui de tu documento.


</div>

In FreeCAD all your work resides inside documents. A document contains your geometry and can be saved to a file. Several documents can be opened at the same time. The document, like the geometry contained inside, has `App` and `Gui` objects. The `App` object contains your actual geometry definitions, while the `Gui` object contains the different views of your document. You can open several windows, each one viewing your work with a different zoom factor or from a different direction. These views are all part of your document\'s `Gui` object.


<div class="mw-translate-fuzzy">

Para acceder a la parte App del documento abierto actualmente (activo), teclea:


</div>


```python
myDocument = App.ActiveDocument
```

Para crear un nuevo documento, teclea:


```python
myDocument = App.newDocument("Document Name")
```


<div class="mw-translate-fuzzy">

Para acceder a la parte GUI del documento abierto actualmente (active), teclea:


</div>


```python
myGuiDocument = Gui.ActiveDocument
```

Para acceder a la vista actual, teclea:


```python
myView = Gui.ActiveDocument.ActiveView
```

[top](#top.md)


<div class="mw-translate-fuzzy">

## Utilizando módulos adicionales {#utilizando_módulos_adicionales}

Los módulos FreeCAD y FreeCADGui son exclusivamente responsables de la creación y mantenimiento de objetos en el documento de FreeCAD. Normalmente no hacen nada como crear o modificar geometría. Eso es porque esa geometría puede ser de diversos tipos, y así es manejada por módulos adicionales, cada uno responsable de manejar ciertos tipos de geometría. Por ejemplo, el [Módulo de pieza](Part_Workbench/es.md) utiliza el kernel de OpenCascade, y por tanto es capaz de crear y manipular geometría de tipo [B-rep](http://en.wikipedia.org/wiki/Boundary_representation), la cual es para la que se ha construido OpenCascade. El [Módulo de malla](Mesh_Workbench/es.md) es capaz de construir y modificar objetos de malla. De ese modo, FreeCAD es capaz de manejar un amplio rango de tipos de objetos, que pueden coexistir todos en el mismo documento, y nuevos tipos se podrían añadir fácilmente en el futuro.


</div>

The `FreeCAD` and `FreeCADGui` modules are only responsible for creating and managing objects in the FreeCAD document. They don\'t actually do anything more such as creating or modifying geometry. This is because that geometry can be of several types, and therefore requires additional modules, each responsible for managing a certain geometry type. For example, the [Part Workbench](Part_Workbench.md), using the OpenCascade kernel, is able to create and manipulate [BRep](http://en.wikipedia.org/wiki/Boundary_representation) type geometry. Whereas the [Mesh Workbench](Mesh_Workbench.md) is able to build and modify mesh objects. In this manner FreeCAD is able to handle a wide variety of object types, that can all coexist in the same document, and new types can easily be added in the future.

[top](#top.md)


<div class="mw-translate-fuzzy">

### Creación de objetos {#creación_de_objetos}

Cada módulo tiene su propio modo de tratar sus geometrías, pero algo que todos ellos normalmente pueden hacer es crear objetos en el documento. Pero el documento de FreeCAD es consciente de los tipos de objetos disponibles proporcionados por los módulos:


</div>

Each module has its own way of dealing with geometry, but one thing they usually all can do is create objects in the document. But the FreeCAD document is also aware of the available object types provided by the modules:


```python
FreeCAD.ActiveDocument.supportedTypes()
```


<div class="mw-translate-fuzzy">

listará todos los objetos que puedes crear. Por ejemplo, vamos a crear una malla (tratada por el módulo de malla) y una pieza (tratada por el módulo de pieza):


</div>


```python
myMesh = FreeCAD.ActiveDocument.addObject("Mesh::Feature", "myMeshName")
myPart = FreeCAD.ActiveDocument.addObject("Part::Feature", "myPartName")
```


<div class="mw-translate-fuzzy">

El primer argumento es el tipo de objeto, el segundo el nombre del objeto. Nuestros dos objetos parecen casi lo mismo: Aún no contienen geometría, y la mayoría de sus propiedades son iguales cuando los inspeccionas con dir(myMesh) y dir(myPart). Excepto por una cosa, myMesh tiene una propiedad \"Mesh\" y \"Part\" tiene una propiedad \"Shape\". Eso es donde la malla y la pieza son almacenadas. Por ejemplo, vamos a crear una pieza de cubo y almacenarla en nuestro objeto myPart:


</div>


```python
import Part
cube = Part.makeBox(2, 2, 2)
myPart.Shape = cube
```


<div class="mw-translate-fuzzy">

Podrías probar almacenando el cubo dentro de la propiedad Mesh del objeto myMesh, devolverá un error quejándose de un tipo erróneo. Eso es porque dichas propiedades están creadas para almacenar sólo un cierto tipo. En la propiedad Mesh de myMesh, sólo puedes almacenar algo creado con el módulo de malla. Observa que la mayoría de módulos también tienen un atajo para añadir su geometría al documento:


</div>


```python
import Part
cube = Part.makeBox(2, 2, 2)
Part.show(cube)
```

[top](#top.md)


<div class="mw-translate-fuzzy">

### Modificando objetos {#modificando_objetos}

La modificación de un objeto se hace del mismo modo:


</div>

Modifying an object is done in the same way:


```python
import Part
cube = Part.makeBox(2, 2, 2)
myPart.Shape = cube
```

Ahora vamos a cambiar la forma por una mayor:


```python
biggercube = Part.makeBox(5, 5, 5)
myPart.Shape = biggercube
```

[top](#top.md)


<div class="mw-translate-fuzzy">

### Preguntando a los objetos {#preguntando_a_los_objetos}

Siempre puedes mirar el tipo de un objeto así:


</div>

You can always look at the type of an object like this:


```python
myObj = FreeCAD.ActiveDocument.getObject("myObjectName")
print(myObj.TypeId)
```


<div class="mw-translate-fuzzy">

o saber si un objeto es derivado de uno de los básicos (característica de Pieza, característica de malla, etc):


</div>


```python
print(myObj.isDerivedFrom("Part::Feature"))
```


<div class="mw-translate-fuzzy">

Ahora puedes empezar a jugar con FreeCAD de verdad! Para ver lo que puedes hacer con el [Módulo de pieza](Part_Workbench/es.md), lee la página [Archivos de guión de Piezas](Topological_data_scripting/es.md), o la página [Archivos de guión de mallas](Mesh_Scripting/es.md) para trabajar con el [Módulo de malla](Mesh_Workbench/es.md). Observa que, aunque los módulos de Pieza y Malla son los más completos y ampliamente utilizados, otros módulos como el [Módulo de Boceto](Draft_Workbench/es.md) también tienen [archivos de guión](Draft_API/es.md) APIs que pueden ser útiles para ti. Para ver una lista completa de cada módulo y sus herramientas disponibles, visita la sección [:Category:API/es](:Category:API/es.md).


</div>

[top](#top.md)


{{Powerdocnavi

}} 

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Python Code{{\#translation:}}](Category:Python_Code.md)
