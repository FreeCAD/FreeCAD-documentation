# FreeCAD Scripting Basics/es
{{TOCright}}

## Guionización Python en FreeCAD 

FreeCAD está construido desde cero para ser totalmente controlado por guiónes de Python. Casi todas las partes de FreeCAD, como la interfaz, el contenido de la escena, e incluso la representación de este contenido en las vistas 3D, son accesibles desde el intérprete de Python incorporado o desde tus propios guiónes. Como resultado, FreeCAD es probablemente una de las aplicaciones de ingeniería más profundamente personalizables disponibles hoy en día.

Si no estás familiarizado con Python, te recomendamos que busques tutoriales en Internet y eches un vistazo rápido a su estructura. Python es un lenguaje muy fácil de aprender, especialmente porque puede ser ejecutado dentro de un intérprete, donde comandos simples, hasta programas completos, pueden ser ejecutados sobre la marcha sin necesidad de compilar nada. FreeCAD tiene un intérprete de Python incorporado. Si no ves la ventana etiquetada como **Consola de Python** como se muestra a continuación, puedes activarla en el **Ver → Paneles → Consola Python**.

### El intérprete 

Desde el intérprete, puedes acceder a todos los módulos de Python instalados en el sistema, así como a los módulos incorporados de FreeCAD, y a todos los módulos adicionales de FreeCAD que hayas instalado posteriormente. La captura de pantalla de abajo muestra el intérprete de Python:

![The FreeCAD Python interpreter](images/screenshot_pythoninterpreter.jpg )

Desde el intérprete, puedes ejecutar código Python y navegar a través de las clases y funciones disponibles. FreeCAD proporciona un navegador de clases muy práctico para explorar el mundo de FreeCAD: Cuando escribes el nombre de una clase conocida seguido de un punto (lo que significa que quieres añadir algo de esa clase), se abre una ventana del navegador de clases, donde puedes navegar entre las subclases y métodos disponibles. Cuando seleccionas algo, se muestra un texto de ayuda asociado (si existe):

![The FreeCAD class browser](images/screenshot_classbrowser.jpg )

Por lo tanto, comience aquí escribiendo `App.` o `Gui.` y vea lo que sucede. Otra forma más genérica de Python para explorar el contenido de los módulos y clases es utilizar el comando `print(dir())`. Por ejemplo, escribiendo `print(dir())` listará todos los módulos cargados actualmente en FreeCAD. `print(dir(App))` te mostrará todo lo que hay dentro del módulo App, etc.

Otra característica útil del intérprete es la posibilidad de retroceder en el historial de comandos y recuperar una línea de código que ya hayas escrito anteriormente. Para navegar por el historial de comandos, basta con utilizar **Flecha arriba** o **Flecha abajo**.

Al hacer clic derecho en la ventana del intérprete también tienes otras opciones, tales como copiar todo el historial (útil para experimentar con algo, y luego hacer un archivo de guión con todo ello), o insertar el nombre de un archivo con su ruta completa.

[inicio](#top.md)

### Ayuda de Python 

En el menú de FreeCAD **Ayuda**, encontrarás una entrada etiquetada como **Documentación automática de los módulos de Python**, que abrirá una ventana del navegador que contiene una documentación completa, generada en tiempo real, de todos los módulos de Python disponibles para el intérprete de FreeCAD, incluyendo los módulos incorporados de Python y FreeCAD, los módulos instalados en el sistema y los módulos adicionales de FreeCAD. La documentación disponible allí depende del esfuerzo que cada desarrollador de módulos ponga en documentar su código, pero los módulos de Python tienen la reputación de estar bastante bien documentados. Tu ventana de FreeCAD debe permanecer abierta para que este sistema de documentación funcione. La entrada **Documentación Guionización en Python** te dará un enlace rápido a la sección wiki [Centro usuarios avanzados](Power_users_hub/es.md).

[inicio](#top.md)

## Módulos incorporados 

Dado que FreeCAD está diseñado para que también pueda ejecutarse sin una interfaz gráfica de usuario (GUI), casi toda su funcionalidad está separada en dos grupos: La funcionalidad del núcleo, llamada `App`, y la funcionalidad de la GUI, llamada `Gui`. A estos dos módulos también se puede acceder desde scripts fuera del intérprete, con los nombres `FreeCAD` y `FreeCADGui` respectivamente.

-   En el módulo `App` encontrarás todo lo relacionado con la propia aplicación, como los métodos para abrir o cerrar archivos, y con los documentos, como establecer el documento activo o listar su contenido.

-   En el módulo `Gui`, encontrarás herramientas para acceder y gestionar los elementos de la Gui, como los ambientes de trabajo y sus barras de herramientas, y, lo que es más interesante, la representación gráfica de todo el contenido de FreeCAD.

Listar el contenido de estos módulos no es muy útil porque crecen bastante rápido a medida que FreeCAD se desarrolla. Pero las dos herramientas de navegación proporcionadas (el navegador de clases y la ayuda de Python) deberían darte una documentación completa y actualizada en cualquier momento.

[inicio](#top.md)

### Los objetos App y Gui 

Como ya se ha mencionado, en FreeCAD todo está separado en núcleo y representación. Esto incluye los objetos 3D. Puedes acceder a las propiedades que definen los objetos (llamados características en FreeCAD) a través del módulo `App`, y cambiar la forma en que se representan en la pantalla a través del módulo `Gui`. Por ejemplo, un cubo tiene propiedades que lo definen (como anchura, longitud, altura) que se almacenan en un objeto `App`, y propiedades de representación (como color de las caras, modo de dibujo) que se almacenan en un objeto `Gui` correspondiente.

Esta forma de hacer las cosas permite una amplia gama de usos, como los algoritmos que sólo funcionan en la parte definitoria de características, sin la necesidad de ocuparse de ningun aspecto visual, o incluso redirigir el contenido del documento con la aplicación no-gráfica, como listas, hojas de cálculo o análisis de elementos.

Para cada objeto `App` en su documento, existe un objeto `Gui` correspondiente. De hecho, el propio documento tiene tanto un objeto `App` como un objeto `Gui`. Esto, por supuesto, sólo se aplica cuando se ejecuta FreeCAD con su interfaz completa. En la versión de línea de comandos no existe la interfaz gráfica, por lo que sólo están disponibles los objetos `App`. Ten en cuenta que la parte `Gui` de los objetos se vuelve a generar cada vez que un objeto `App` se marca como \'a recalcular\' (por ejemplo cuando uno de sus parámetros cambia), por lo que cualquier cambio realizado directamente en el objeto `Gui` puede perderse.

Para acceder a la parte `App` de algo, se teclea:


```python
myObject = App.ActiveDocument.getObject("ObjectName")
```

donde `"ObjectName"` es el nombre de su objeto. También puede teclea:


```python
myObject = App.ActiveDocument.ObjectName
```

Para acceder a la parte `Gui` del mismo objeto, se teclea:


```python
myViewObject = Gui.ActiveDocument.getObject("ObjectName")
```

donde `"ObjectName"` es el nombre de su objeto. También puede teclea:


```python
myViewObject = App.ActiveDocument.ObjectName.ViewObject
```

Si está en modo de línea de comandos y no tiene GUI, la última línea devolverá `None`.

[inicio](#top.md)

### Los objetos Documento 

En FreeCAD todo tu trabajo reside dentro de los documentos. Un documento contiene tu geometría y puede ser guardado en un archivo. Se pueden abrir varios documentos al mismo tiempo. El documento, al igual que la geometría que contiene, tiene objetos `App` y `Gui`. El objeto `App` contiene las definiciones reales de la geometría, mientras que el objeto `Gui` contiene las diferentes vistas del documento. Puedes abrir varias ventanas, cada una de ellas viendo tu trabajo con un factor de zoom diferente o desde una dirección diferente. Todas estas vistas forman parte del objeto `Gui` de tu documento.

Para acceder a la parte `App` del documento actualmente abierto (activo), se escribe:


```python
myDocument = App.ActiveDocument
```

Para crear un nuevo documento, teclea:


```python
myDocument = App.newDocument("Document Name")
```

Para acceder a la parte `Gui` del documento abierto actualmente (active), teclea:


```python
myGuiDocument = Gui.ActiveDocument
```

Para acceder a la vista actual, teclea:


```python
myView = Gui.ActiveDocument.ActiveView
```

[inicio](#top.md)

## Utilizando módulos adicionales 

Los módulos `FreeCAD` y `FreeCADGui` sólo se encargan de crear y gestionar objetos en el documento de FreeCAD. En realidad no hacen nada más como crear o modificar la geometría. Esto se debe a que la geometría puede ser de varios tipos, y por lo tanto requiere módulos adicionales, cada uno responsable de la gestión de un determinado tipo de geometría. Por ejemplo, el [Part Workbench](Part_Workbench.md), usando el kernel de OpenCascade, es capaz de crear y manipular geometría del tipo [BRep](http://en.wikipedia.org/wiki/Boundary_representation). Mientras que el [Mesh Workbench](Mesh_Workbench.md) es capaz de construir y modificar objetos de malla. De esta manera FreeCAD es capaz de manejar una amplia variedad de tipos de objetos, que pueden coexistir en el mismo documento, y nuevos tipos pueden ser fácilmente añadidos en el futuro.

[inicio](#top.md)

### Creación objetos 

Cada módulo tiene su propia manera de tratar la geometría, pero una cosa que normalmente todos pueden hacer es crear objetos en el documento. Pero el documento de FreeCAD también es consciente de los tipos de objetos disponibles proporcionados por los módulos:


```python
FreeCAD.ActiveDocument.supportedTypes()
```

listará todos los objetos posibles que puedes crear. Por ejemplo, vamos a crear una malla (manejada por el módulo `Mesh`) y una pieza (manejada por el módulo `Part`):


```python
myMesh = FreeCAD.ActiveDocument.addObject("Mesh::Feature", "myMeshName")
myPart = FreeCAD.ActiveDocument.addObject("Part::Feature", "myPartName")
```

El primer argumento es el tipo de objeto, el segundo el nombre del objeto. Nuestros dos objetos parecen casi iguales: no contienen ninguna geometría todavía, y la mayoría de sus propiedades son las mismas cuando los inspeccionas con `dir(myMesh)` y `dir(myPart)`. Excepto por una cosa, `myMesh` tiene una propiedad `Mesh` y `myPart` tiene una propiedad `Shape`. Ahí es donde se almacenan los datos de la Malla y de la Pieza. Por ejemplo, vamos a crear un cubo `Part` y almacenarlo en nuestro objeto `myPart`:


```python
import Part
cube = Part.makeBox(2, 2, 2)
myPart.Shape = cube
```

Podrías intentar almacenar el cubo dentro de la propiedad `Mesh` del objeto `myMesh`, pero devolverá un error. Esto se debe a que cada propiedad está hecha para almacenar sólo un tipo determinado. En una propiedad `Mesh`, sólo puedes guardar cosas creadas con el módulo `Mesh`. Tenga en cuenta que la mayoría de los módulos también tienen un acceso directo para añadir su geometría al documento:


```python
import Part
cube = Part.makeBox(2, 2, 2)
Part.show(cube)
```

[inicio](#top.md)

### Modificando objetos 

Modificación de un objeto se hace de la misma manera:


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

[inicio](#top.md)

### Consultar objetos 

Siempre se puede mirar el tipo de un objeto así:


```python
myObj = FreeCAD.ActiveDocument.getObject("myObjectName")
print(myObj.TypeId)
```

o comprobar si un objeto deriva de uno de los básicos (Característica Pieza, Característica Malla, etc):


```python
print(myObj.isDerivedFrom("Part::Feature"))
```

¡Ahora puedes empezar a jugar de verdad con FreeCAD! Para una lista completa de los módulos disponibles y sus herramientas, visite la sección [Categoría:API](:Category:API/es.md).

[inicio](#top.md)


{{Powerdocnavi

}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)

---
[documentation index](../README.md) > [Developer Documentation](Category:Developer Documentation.md) > FreeCAD Scripting Basics/es
