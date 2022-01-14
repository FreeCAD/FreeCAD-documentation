# Python scripting tutorial/es
{{TOCright}}

## Introducción

[Python](http://es.wikipedia.org/wiki/Python) es un lenguaje de programación relativamente fácil de aprender y comprender. Es de código abierto y multiplataforma, y puede utilizarse para muchos fines: desde simples scripts de shell hasta programas muy complejos. Pero su uso más extendido es como lenguaje de scripting incrustado en otras aplicaciones. Así es como se utiliza dentro de FreeCAD. Desde la [Consola de Python](Python_console/es.md), o desde scripts personalizados, puedes controlar FreeCAD y hacer que realice operaciones muy complejas.

Por ejemplo, desde un archivo de guión de Python, puedes:

-   Crear nuevos objetos.
-   Modificar los objetos existentes.
-   Modificar la representación 3D de dichos objetos
-   Modificar la interfaz de FreeCAD

También existen diversas formas de utilizar Python en FreeCAD:

-   Desde el [Interprete de Python de FreeCAD](FreeCAD_Scripting_Basics/es.md), donde puedes dictar comandos como en una interfaz del tipo de línea de comandos
-   Desde [Macros](macros/es.md), que son una forma conveniente de añadir una herramienta que no exista a la interfaz de FreeCAD
-   Desde archivos de guión externos, que pueden utilizarse para programar cosas mucho más complejas. Como [Ambientes de trabajo](Workbenches/es.md) completos.

En este tutorial, trabajaremos en varios ejemplos básicos para que puedas iniciarte, pero existe mucha más documentación sobre los [documentación sobre guionización en Python](Power_users_hub/es.md) disponible en esta wiki. Si eres totalmente nuevo en Python y quieres comprender cómo funciona, también tenemos una básica [Introducción a Python](introduction_to_Python/es.md).

Antes de proceder con la escritura en Python, vaya a **Editar → Preferencias → General → Ventana de salida** y marque dos casillas:

-    **Redirigir salida Python interna a la vista de informe**.

-    **Redirigir errores Python internos a la vista de informe**.

Luego vaya a **Vista → Paneles** y compruebe:

-    **Vista de informe**.

## Escribiendo código en Python 

Existen dos modos sencillos de escribir código de Python en FreeCAD: Desde la consola de Python (disponible en el menú Vista -\> Vistas -\> Consola de Python) o desde el editor de macros (Herramientas -\> Macros). En la consola, escribes comandos de Python uno a uno, que son ejecutados al presionar Enter, mientras que las macros pueden contener archivos de guión más completos formados por varias líneas, que se ejecutan sólo cuando la macro es ejecutada.

![](images/Screenshot_pythoninterpreter.jpg ) 
*La consola FreeCAD Python*

En este tutorial se pueden utilizar ambos métodos. Puede copiar-pegar cada línea en la consola Python y luego presionar **Enter**, o copiar-pegar todo el código en una nueva ventana de Macro. {{Top}}

## Explorando FreeCAD 

Vamos a empezar creando un nuevo documento vacío:


```python
doc = FreeCAD.newDocument()
```


<div class="mw-translate-fuzzy">

Si escribe esto en la consola de FreeCAD Python, notará que en cuanto teclee `FreeCAD.` aparece una ventana que le permite autocompletar rápidamente el resto de su línea. Mejor aún, cada entrada de la lista de autocompletar tiene un tooltip que explica lo que hace. Esto facilita la exploración de la funcionalidad disponible. Antes de elegir `newDocument`, eche un vistazo a las otras opciones.


</div>

![](images/Screenshot_classbrowser.jpg ) 
*El mecanismo de autocompletar de la consola Python de FreeCAD*

Ahora nuestro nuevo documento se creará. Esto es similar a presionar el botón \"Nuevo documento\" en la barra de herramientas. En realidad, la mayoría de botones en FreeCAD no hacen nada más que ejecutar una línea o dos de código en Python. Aún mejor, puedes establecer una opción en Editar -\> Preferencias -\> General -\> Macro para \"mostrar los comandos de los archivos de guión en la consola de Python\". Esto mostrará en la consola todo el código de Python ejecutado cuando presionas los botones. Muy útil para aprender como reproducir acciones en Python.

Ahora volvamos a nuestro documento y veamos qué podemos hacer con él:


```python
doc.
```

Explore las opciones disponibles. Normalmente los nombres que empiezan con mayúscula son atributos, contienen un valor, mientras que los nombres que empiezan con minúscula son funciones (también llamadas métodos), \"hacen algo\". Los nombres que comienzan con un guión bajo suelen estar ahí para el funcionamiento interno del módulo, y no deberías preocuparte por ellos. Vamos a utilizar uno de los métodos para añadir un nuevo objeto a nuestro documento:


```python
box = doc.addObject("Part::Box", "myBox")
```


<div class="mw-translate-fuzzy">

No pasa nada. ¿Por qué? Porque FreeCAD está hecho para la gran imagen. Un día, trabajará con cientos de objetos complejos, todos dependiendo unos de otros. Hacer un pequeño cambio en algún lugar puede tener un gran impacto, puede necesitar recalcular todo el documento, lo que puede llevar mucho tiempo. Por esa razón casi ningún comando actualiza la escena automáticamente. Debes hacerlo manualmente:


</div>


```python
doc.recompute()
```


<div class="mw-translate-fuzzy">

Ahora nuestra caja apareció. Muchos de los botones que añaden objetos en FreeCAD en realidad hacen dos cosas: añadir el objeto, y volver a calcular. Si activaste la opción **Mostrar comandos de script en la consola de python** de arriba, intenta añadir una esfera con el botón de la GUI, verás las dos líneas de código Python ejecutándose una tras otra.


</div>

Ahora vamos a explorar el contenido de nuestro cubo:


```python
box.
```

Verás automáticamente varias cosas interesantes como:


```python
box.Height
```

Esto mostrará la altura actual de nuestro cubo. Ahora vamos a intentar cambiarla:


```python
box.Height = 5
```


<div class="mw-translate-fuzzy">

Si seleccionas tu caja con el ratón, verás que en el [Editor de propiedades](Property_editor/es.md), en la pestaña **Datos**, aparece nuestra propiedad **Altura**. Todas las propiedades de un objeto de FreeCAD que aparecen ahí (y también en la pestaña **Vista**, más adelante), son directamente accesibles por Python también, por sus nombres, como hicimos con la propiedad **Altura**. Prueba a cambiar las otras dimensiones de la caja.

Traducción realizada con la versión gratuita del traductor www.DeepL.com/Translator


</div>


{{Top}}

## Vectores y ubicaciones 

Los [vectores](http://es.wikipedia.org/wiki/Vector) son un concepto muy fundamental en cualquier aplicación 3D. Son una lista de 3 números (X, Y y Z), describiendo un punto o posición en el espacio 3D. Un montón de cosas se pueden hacer con los vectores, como sumas, restas, proyecciones y [mucho más](http://es.wikipedia.org/wiki/Espacio_vectorial). En FreeCAD los vectores funcionan así:


```python
myvec = FreeCAD.Vector(2, 0, 0)
myvec.x
myvec.y
othervec = FreeCAD.Vector(0, 3, 0)
sumvec = myvec.add(othervec)
```

Otra característica común de los objetos de FreeCAD es su [Ubicación](Placement/es.md). Cada objeto tiene una propiedad **Ubicación**, que contiene la **Base** (posición) y **Rotación** (orientación) del objeto. Es fácil de manipular, por ejemplo para mover nuestro objeto:


```python
box.Placement
box.Placement.Base
box.Placement.Base = sumvec
 
otherpla = FreeCAD.Placement()
box.Placement = otherpla
```

Ahora deberías comprender varios conceptos importantes antes de continuar avanzando. {{Top}}

## App y Gui 

FreeCAD ha sido diseñado para que también pueda ser utilizado sin su interfaz de usuario, como una aplicación de línea de comandos. Por lo tanto, casi todos los objetos de FreeCAD constan de dos partes: un `Object`, su componente de \"geometría\", y un `ViewObject`, su componente \"visual\". Cuando trabajas en modo línea de comandos, la parte de geometría está presente, pero la parte visual está desactivada.

Para ilustrar el concepto, veamos nuestro objeto cubo. Las propiedades geométricas del cubo, como sus dimensiones, posición, etc. se almacenan en el `Objeto`. Mientras que sus propiedades visuales, como su color, grosor de línea, etc. se almacenan en el `VistaObjeto`. Esto se corresponde con las pestañas **Datos** y **Vista**\' del [Editor de propiedades](Property_editor/es.md). El objeto vista de un objeto se accede así:


```python
vo = box.ViewObject
```

Ahora también puedes cambiar las propiedades en la pestaña **Vista**\':


```python
vo.Transparency = 80
vo.hide()
vo.show()
```

Cuando se inicia FreeCAD, la consola de Python ya carga dos módulos base: `FreeCAD` y `FreeCADGui` (a los que también se puede acceder por sus accesos directos `App` y `Gui`). Contienen todo tipo de funcionalidades genéricas para trabajar con documentos y sus objetos. Para ilustrar nuestro concepto, veamos que tanto `FreeCAD` como `FreeCADGui` contienen un atributo `ActiveDocument`, que es el documento actualmente abierto. `FreeCAD.ActiveDocument` y `FreeCADGui.ActiveDocument` no son el mismo objeto. Son los dos componentes de un documento de FreeCAD, y contienen diferentes atributos y métodos. Por ejemplo, `FreeCADGui.ActiveDocument` contiene `ActiveView`, que es la [Vista 3D](3D_view/es.md) actualmente abierta. {{Top}}

## Módulos

El verdadero poder de FreeCAD reside en sus fieles módulos, con sus respectivos bancos de trabajo. La aplicación base de FreeCAD es más o menos un contenedor vacío. Sin sus módulos no puede hacer mucho más que crear nuevos documentos vacíos. Cada módulo no sólo añade nuevos ambientes de trabajo a la interfaz, sino también nuevos comandos de Python y nuevos tipos de objetos. Como resultado, varios tipos de objetos diferentes, e incluso totalmente incompatibles, pueden coexistir en el mismo documento. Los módulos más importantes de FreeCAD que veremos en este tutorial son:[Piezas](Part_Workbench/es.md), [Mallas](Mesh_Workbench/es.md), [Croquizador](Sketcher_Workbench/es.md) o [Borrador](Draft_Workbench/es.md).

[Croquizador](Sketcher_Workbench/es.md) y [Borrador](Draft_Workbench/es.md) ambos utilizan el módulo [Piezas](Part_Workbench/es.md) para crear y manejar sus geometrías. Mientras que [Malla](Mesh_Workbench.md) es totalmente independiente, y maneja sus propios objetos. Más sobre esto a continuación.

Puedes comprobar todos los tipos de objeto base disponibles para el documento actual así:


```python
doc.supportedTypes()
```

Los diferentes módulos de FreeCAD no se cargan automáticamente en la consola de Python. Esto es para evitar tener un arranque muy lento. Los módulos se cargan sólo cuando los necesitas. Así, por ejemplo, para explorar lo que hay dentro del módulo Pieza:


```python
import Part
Part.
```

Pero ya hablaremos más adelante del módulo de Piezas. {{Top}}


<div class="mw-translate-fuzzy">

## Malla


</div>

Las [Mallas](https://en.wikipedia.org/wiki/Polygon_mesh) son un tipo de objeto 3D muy simple, utilizado por ejemplo por [Sketchup](https://en.wikipedia.org/wiki/SketchUp), [Blender](https://en.wikipedia.org/wiki/Blender_(software)) y [3D Studio Max](https://en.wikipedia.org/wiki/Autodesk_3ds_Max). Están compuestos por 3 elementos: puntos (también llamados vértices), líneas (también llamadas aristas) y caras. En muchas aplicaciones, incluido FreeCAD, las caras sólo pueden tener 3 vértices. Por supuesto, nada te impide tener una cara más grande formada por varios triángulos coplanares.

Las mallas son simples, pero como son simples puedes tener fácilmente millones de ellas en un solo documento. Sin embargo, en FreeCAD tienen menos uso y están principalmente ahí para que puedas importar objetos en formatos de malla ({{FileName|.stl}}, {{FileName|.obj}}) desde otras aplicaciones. El módulo de malla también se utilizó ampliamente como el principal módulo de prueba en el primer mes de vida de FreeCAD.

Los objetos de malla y los objetos de FreeCAD son cosas diferentes. Puedes ver el objeto FreeCAD como un contenedor para un objeto Malla (y como veremos más adelante, para los objetos Pieza también). Así que para añadir un objeto malla a FreeCAD, primero debemos crear un objeto FreeCAD y un objeto Malla, y luego añadir el objeto Malla al objeto FreeCAD:


```python
import Mesh
mymesh = Mesh.createSphere()
mymesh.Facets
mymesh.Points
 
meshobj = doc.addObject("Mesh::Feature", "MyMesh")
meshobj.Mesh = mymesh
doc.recompute()
```

Este es un ejemplo estándar que utiliza el método `createSphere()` para crear una esfera, pero también puedes crear mallas personalizadas desde cero definiendo sus vértices y caras.

[Leer más sobre guionización de malla\...](Mesh_Scripting/es.md) {{Top}}


<div class="mw-translate-fuzzy">

## Piezas


</div>

El [Pieza](Part_Workbench/es.md) módulo es el módulo más potente de todo FreeCAD. Te permite crear y manipular objetos [BREP](http://en.wikipedia.org/wiki/Boundary_representation). BREP significa \"Representación de Límites\". Un objeto BREP está definido por superficies que encierran y definen un volumen interior. A diferencia de las mallas, los objetos BREP pueden tener una gran variedad de componentes, desde caras planas hasta superficies NURBS muy complejas.

El módulo de Piezas está basado en la potente librería [OpenCasCade](https://en.wikipedia.org/wiki/Open_CASCADE_Technology), que permite realizar una amplia gama de operaciones complejas sobre estos objetos, como operaciones booleanas, fileteado, lofts, etc.

El módulo de Piezas funciona del mismo modo que el módulo de mallas: Se crea un objeto de FreeCAD, un objeto de Pieza, luego añadir el objeto de pieza al objeto de FreeCAD:


```python
import Part
myshape = Part.makeSphere(10)
myshape.Volume
myshape.Area

shapeobj = doc.addObject("Part::Feature", "MyShape")
shapeobj.Shape = myshape
doc.recompute()
```

El módulo Pieza (como el módulo de Mallas) también tiene un atajo que automáticamente crea un objeto de FreeCAD y le añade una forma, por lo que puede acortar las tres últimas líneas a:


```python
Part.show(myshape)
```

Al explorar el contenido de myshape, notarás muchos subcomponentes interesantes como `Faces`, `Edges`, `Vertexes`, `Solids` y `Shells`, y una amplia gama de operaciones de geometría como `cut` (sustracción), `common` (intersección) o `fuse` (unión). En la página [Guionización de topología de datos](Topological_data_scripting/es.md) se explica todo esto en detalle.

[ Leer más sobre guionización pieza\...](Topological_data_scripting/es.md) {{Top}}


<div class="mw-translate-fuzzy">

## Borrador


</div>

FreeCAD proporciona varios módulos, como el [Croquizador](Sketcher_Workbench/es.md) o [Borrador](Draft_Workbench/es.md), que también crean objetos de piezas, pero le añade parámetros, o incluso un nuevo modo de manejar la geometría de las piezas. Nuestro cubo de ejemplo de arriba, es un perfecto ejemplo de objeto paramétrico. Todo lo que necesitas, para definir el cubo, es especificar un conjunto de parámetros, como las altura, ancho y longitud. Basados en los cuales, el objeto calculará automáticamente su forma de Pieza. FreeCAD te permite [crear dichos objetos en Python](Scripted_objects/es.md).

El [Borrador](Draft_Workbench/es.md) Módulo añade tipos de objetos paramétricos 2D (que son todos objetos Pieza) como líneas y círculos, y también proporciona algunas funciones genéricas que no sólo funcionan con objetos Borrador, sino con cualquier objeto Pieza. Para explorar lo que está disponible, simplemente haga:


```python
import Draft
rec = Draft.makeRectangle(5, 2)
mvec = FreeCAD.Vector(4, 4, 0)
Draft.move(rec, mvec)
Draft.move(box, mvec)
```


{{Top}}

## Interfaz

La interfaz de usuario de FreeCAD está creada con [Qt](http://es.wikipedia.org/wiki/Qt_(biblioteca)), un poderoso sistema de interfaces gráficas, responsable de dibujar y manejar todos los controles, menús, barras de herramientas y botones en toda la vista 3D. Qt proporciona un módulo, denominado PyQt, que permite a Python acceder y modificar interfaces Qt, como la de FreeCAD. Vamos a tratar de lidiar con la interfaz de Qt y producir un letrero de diálogo simple:


```python
from PySide import QtGui
QtGui.QMessageBox.information(None, "Apollo program", "Houston, we have a problem")
```

Observa que el diálogo que aparece tiene el icono de FreeCAD en su barra de herramientas, lo que significa que Qt sabe que la orden ha sido emitida desde dentro de la aplicación FreeCAD. Es posible manipular cualquier parte de la interfaz de FreeCAD.

Qt es un sistema de interfaz muy potente que permite hacer cosas muy complejas. También tiene algunas herramientas fáciles de usar como el Qt Designer con el que puedes diseñar diálogos gráficamente y luego añadirlos a la interfaz de FreeCAD con unas pocas líneas de código Python.

[Lee más sobre PySide aquí\...](PySide/es.md) {{Top}}

## Macros

Ahora que tienes una buena comprensión de los conceptos básicos, a dónde vamos para mantener nuestros archivos de guión en Python, y cómo vamos a ejecutarlos fácilmente desde FreeCAD? Existe un sencillo mecanismo para ello, denominado [Macros](Macros/es.md). Una macro es simplemente un archivo de guión en Python, que puede ser añadida a una barra de herramientas y lanzada desde un simple clic de ratón. FreeCAD proporciona un simple editor de textos (Macro -\> Macros -\> Crear) donde puedes escribir o pegar archivos de guión. Una vez esté terminado, Herramientas -\> Personalizar -\> Macros te permite definir un botón para ella, que se puede añadir a las barras de herramientas.

Ahora estás listo para profundizar en guionización FreeCAD. Así que dirígete al [Centro usuarios avanzados](Power_users_hub/es.md)! {{Top}}





{{Powerdocnavi

}}

[<img src="images/Property.png" style="width:16px"> Developer Documentation](Category_Developer_Documentation.md) [<img src="images/Property.png" style="width:16px"> Python Code](Category_Python_Code.md)

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Python scripting tutorial/es
