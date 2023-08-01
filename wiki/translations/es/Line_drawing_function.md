# Line drawing function/es
## Introduction


<div class="mw-translate-fuzzy">

Esta página muestra cómo se puede crear funcionalidades avanzadas con Python. En este ejercicio, construiremos una nueva herramienta que dibuja una línea. Esta herramienta puede ser vinculada a un comando de FreeCAD, y ese comando se puede llamar desde cualquier elemento de la interfaz, tal como un elemento de menú o un botón de una barra de herramientas.


</div>


<div class="mw-translate-fuzzy">

## El archivo de guión principal 

En primer lugar vamos a escribir un archivo de guión que contenga toda nuestra funcionalidad. Después, vamos a guardar esto en un archivo, e importarlo en FreeCAD, así todas las clases y funciones que escribas estarán disponibles para FreeCAD. De modo que inicia tu editor de texto favorito y escribe las siguientes líneas:


</div>

First we will write a script containing all our functionality. Then we will save this in a file and import it in FreeCAD to make all its classes and functions available. Launch your favorite code editor and type the following lines:


```python
import FreeCADGui, Part
from pivy.coin import *

class line:

    """This class will create a line after the user clicked 2 points on the screen"""

    def __init__(self):
        self.view = FreeCADGui.ActiveDocument.ActiveView
        self.stack = []
        self.callback = self.view.addEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.getpoint)

    def getpoint(self, event_cb):
        event = event_cb.getEvent()
        if event.getState() == SoMouseButtonEvent.DOWN:
            pos = event.getPosition()
            point = self.view.getPoint(pos[0], pos[1])
            self.stack.append(point)
            if len(self.stack) == 2:
                l = Part.LineSegment(self.stack[0], self.stack[1])
                shape = l.toShape()
                Part.show(shape)
                self.view.removeEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.callback)
```


{{Top}}

## Explicación detallada 


```python
import Part, FreeCADGui
from pivy.coin import *
```


<div class="mw-translate-fuzzy">

En Python, cuando desees utilizar las funciones de otro módulo, tienes que importarlo. En nuestro caso, vamos a necesitar las funciones del [Módulo de Pieza](Part_Workbench/es.md), para la creación de la línea, y del módulo GUI (FreeCADGui), para acceder a la vista 3D. También necesitamos el contenido completo de la biblioteca de Coin, para que podamos utilizar directamente todos los objetos Coin, como SoMouseButtonEvent, etc ..


</div>


```python
class line:
```

Aquí definimos nuestra clase principal. ¿Por qué utilizar una clase y no una función? La razón es que necesitamos que nuestra herramienta se mantenga \"viva\" mientras esperamos a que el usuario haga clic en la pantalla. Una función termina cuando su tarea se ha hecho, pero un objeto (una clase se define como un objeto) se mantiene vivo hasta que se destruye.


```python
"""This class will create a line after the user clicked 2 points on the screen"""
```


<div class="mw-translate-fuzzy">

En Python, cada clase o función puede tener una cadena de descripción. Esto es particularmente útil en FreeCAD, porque cuando vas a llamar a esa clase en el intérprete, la cadena de descripción se mostrará como una nota.


</div>


```python
def __init__(self):
```


<div class="mw-translate-fuzzy">

Las clases en Python siempre pueden contener una función \_\_init\_\_, que se ejecuta cuando la clase es llamada para crear un objeto. Por lo tanto, vamos a poner aquí todo lo que queremos que ocurra cuando nuestra herramienta línea comienza.


</div>


```python
self.view = FreeCADGui.ActiveDocument.ActiveView
```


<div class="mw-translate-fuzzy">

En una clase, por lo general querrás incluir *self.* antes de un nombre de variable, para que sea fácilmente accesible por todas las funciones dentro y fuera de esa clase. Aquí, vamos a utilizar self.view para acceder y manipular la vista 3D activa.


</div>


```python
self.stack = []
```


<div class="mw-translate-fuzzy">

Aquí creamos una lista vacía que contendrá los puntos 3D enviados por la función getpoint.


</div>


```python
self.callback = self.view.addEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.getpoint)
```


<div class="mw-translate-fuzzy">

Aquí viene la parte importante: Dado que en realidad se trata de una escena [Coin3d](http://www.coin3d.org/), FreeCAD utiliza el mecanismo de devolución de llamada de Coin, que permite que una función sea llamada cada vez que sucede un determinado evento de escena. En nuestro caso, estamos creando una devolución de llamada para eventos [SoMouseButtonEvent](http://doc.coin3d.org/Coin/group__events.html), y lo conduciremos a la función getpoint. Ahora, cada vez que un botón del ratón sea pulsado o soltado, la función getpoint será ejecutada.


</div>


<div class="mw-translate-fuzzy">

Ten en cuenta que también hay una alternativa a addEventCallbackPivy(), llamada addEventCallback(), que dispensa del uso de pivy. Pero como pivy es una forma muy eficaz y natural para acceder a cualquier parte de la escena de Coin, es mucho mejor usarlo tanto como se pueda!


</div>


{{Top}}


```python
def getpoint(self, event_cb):
```


<div class="mw-translate-fuzzy">

Ahora definimos la función getpoint, que se ejecutará cuando el botón del ratón se pulsa en una vista 3D. Esta función recibe un argumento, que llamaremos event_cb. A partir de este evento de devolución de llamada podemos tener acceso al objeto de evento, que contiene varias piezas de información (más información [aquí](Code_snippets#Observing_mouse_events_in_the_3D_viewer_via_Python.md)).


</div>


```python
if event.getState() == SoMouseButtonEvent.DOWN:
```


<div class="mw-translate-fuzzy">

La función getpoint se llamará cuando un botón del ratón sea pulsado o soltado. Pero queremos escoger un punto 3D sólo cuando se presiona (de lo contrario obtendríamos dos puntos 3D muy cerca uno del otro). Por lo tanto, debes comprobar eso aquí.


</div>


```python
pos = event.getPosition()
```


<div class="mw-translate-fuzzy">

Aquí obtenemos las coordenadas de pantalla del cursor del ratón


</div>


```python
point = self.view.getPoint(pos[0], pos[1])
```


<div class="mw-translate-fuzzy">

Esta función nos da un vector de FreeCAD (x,y,z) que contiene el punto 3D que se encuentra en el plano focal, justo debajo del cursor de nuestro ratón. Si estás en vista de cámara, imagina un rayo proveniente de la cámara, pasando por el cursor del ratón, y alcanzando el plano focal. Ahí está nuestro punto 3D. Si estamos en una vista ortogonal, el rayo es paralelo a la dirección de la vista.


</div>


```python
self.stack.append(point)
```


<div class="mw-translate-fuzzy">

Añadimos nuestro nuevo punto a la pila


</div>


```python
if len(self.stack) == 2:
```

¿Tenemos ya suficientes puntos? si es así, entonces vamos a trazar la línea!


```python
l = Part.LineSegment(self.stack[0], self.stack[1])
```


<div class="mw-translate-fuzzy">

Aquí se utiliza la función line() del [Módulo de Pieza](Part_Workbench/es.md) que crea una línea a partir de dos vectores de FreeCAD. Todo lo que creamos y modificamos dentro del módulo de Pieza, se queda en el módulo de Pieza . Así, hasta ahora, hemos creado un elemento de línea. No está ligado a un objeto de nuestro documento activo, por lo que no aparece nada en la pantalla.


</div>


```python
shape = l.toShape()
```


<div class="mw-translate-fuzzy">

El documento de FreeCAD sólo puede aceptar formas desde el módulo de Pieza. Las formas son el tipo más genérico del módulo de Pieza. Por lo tanto, debemos convertir nuestra línea en una forma antes de añadirla al documento.


</div>


```python
Part.show(shape)
```


<div class="mw-translate-fuzzy">

El módulo de Pieza tiene una función, show(), que es muy útil ya que crea un nuevo objeto en el documento y le conecta a una forma. También podrías haber creado primero un nuevo objeto en el documento, y a continuación vincularle a la forma manualmente.


</div>


```python
self.view.removeEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.callback)
```


<div class="mw-translate-fuzzy">

Como ya hemos terminado con nuestra línea, vamos a quitar el mecanismo de devolución de llamada, que consume unos preciosos ciclos de CPU.


</div>


{{Top}}


<div class="mw-translate-fuzzy">

## Pruebas y Uso del archivo de guión 

Ahora, vamos a guardar nuestro archivo de guión en un lugar donde el intérprete de Python de FreeCAD lo encuentre. Cuando importa los módulos, el intérprete mirará en los siguientes lugares: las rutas de instalación de Python, el directorio bin de FreeCAD, y todos los directorios de módulos FreeCAD. Por lo tanto, la mejor solución es crear un nuevo directorio en una de los FreeCAD [Mod directories](Installing_more_workbenches/es.md), y salvar nuestro script en él. Por ejemplo, vamos a hacer un directorio \"MyScripts\", y salvamos nuestro script como \"exercise.py\".


</div>

Now let\'s save our script in a folder where the FreeCAD Python interpreter can find it. When importing modules, the interpreter will look in the following places: the Python installation paths, the FreeCAD **bin** folder, and all FreeCAD **Mod** (module) folders. So the best solution is to create a new folder in one of the **Mod** folders. Let\'s create a **MyScripts** folder there and save our script in it as **exercise.py**.


<div class="mw-translate-fuzzy">

Ahora, todo está listo, vamos a empezar FreeCAD, cree un nuevo documento, y, en el intérprete de Python, ejecute:


</div>


```python
import exercise
```


<div class="mw-translate-fuzzy">

Si no aparece ningún mensaje de error, eso significa que nuestro script de ejercicio se ha cargado. Ahora puede comprobar su contenido con:


</div>


```python
dir(exercise)
```


<div class="mw-translate-fuzzy">

El comando dir() es un comando integrado de Python que muestra el contenido de un módulo. Podemos ver que nuestra clase line() está ahí, esperandonos. Ahora vamos a probarlo:


</div>


```python
'line' in dir(exercise)
```

Now let\'s test it:


```python
exercise.line()
```


<div class="mw-translate-fuzzy">

A continuación, haz clic dos veces en la vista 3D, y \.... ¡bingo!, ¡aquí está nuestra línea! Para hacerlo de nuevo, simplemente escribe exercise.line() otra vez, y otra vez, y otra vez \... Estas contento, ¿no?


</div>


{{Top}}


<div class="mw-translate-fuzzy">

## Incluyendo el archivo de guión en la interfaz de FreeCAD 

Ahora, para que nuestra nueva herramienta línea sea realmente buena, debe tener un botón en la interfaz, para que no sea necesario escribir todas estas cosas cada vez. La forma más fácil es transformar nuestro nuevo directorio MyScripts en un completo entorno de FreeCAD. Es fácil, todo lo que se necesita es poner un archivo llamado **InitGui.py** dentro de tu directorio MyScripts. El InitGui.py contendrá las instrucciones para crear un nuevo entorno (workbench), y le añadimos nuestra nueva herramienta. Además, también habrá que transformar un poco nuestro código del ejercicio, para que la herramienta line() sea reconocida como un comando oficial de FreeCAD. Comencemos por crear un archivo InitGui.py, y escribir el siguiente código en él:


</div>

For our new line tool to be really useful, and to avoid having to type all that stuff, it should have a button in the interface. One way to do this is to transform our new **MyScripts** folder into a full FreeCAD workbench. This is easy, all that is needed is to put a file called **InitGui.py** inside the **MyScripts** folder. **InitGui.py** will contain the instructions to create a new workbench, and add our new tool to it. Besides that we will also need to change our exercise code a bit, so the `line()` tool is recognized as an official FreeCAD command. Let\'s start by creating an **InitGui.py** file, and writing the following code in it:


```python
class MyWorkbench (Workbench):

    MenuText = "MyScripts"

    def Initialize(self):
        import exercise
        commandslist = ["line"]
        self.appendToolbar("My Scripts", commandslist)

Gui.addWorkbench(MyWorkbench())
```


<div class="mw-translate-fuzzy">

A estas alturas, ya debes entender el archivo de guión anterior por ti mismo, supongo: Creamos una nueva clase que llamamos MyWorkbench, le damos un título (MenuText), y definimos una función initialize() que se ejecutará cuando el entorno se cargue en FreeCAD. En esa función, se carga el contenido de nuestro archivo del ejercicio, y los comandos de FreeCAD que se encuentran dentro se anexan en una lista de comandos. A continuación, hacemos una barra de herramientas llamada \"Mi Scripts\" y le asignamos nuestra lista de comandos. Finalmente, por supuesto, sólo tenemos una herramienta, por lo que nuestra lista de comandos contiene un solo elemento. Ahora, una vez que nuestro entorno está listo, lo añadimos a la interfaz principal.


</div>


<div class="mw-translate-fuzzy">

Pero esto aún no funciona, porque un comando de FreeCAD debe estar formateado de una determinada manera para poder funcionar. Así que tendremos que transformar un poco nuestra herramienta line(). Nuestro nuevo archivo de guión exercise.py tendrá después este aspecto:


</div>


```python
import FreeCADGui, Part
from pivy.coin import *

class line:

    """This class will create a line after the user clicked 2 points on the screen"""

    def Activated(self):
        self.view = FreeCADGui.ActiveDocument.ActiveView
        self.stack = []
        self.callback = self.view.addEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.getpoint)

    def getpoint(self, event_cb):
        event = event_cb.getEvent()
        if event.getState() == SoMouseButtonEvent.DOWN:
            pos = event.getPosition()
            point = self.view.getPoint(pos[0], pos[1])
            self.stack.append(point)
            if len(self.stack) == 2:
                l = Part.LineSegment(self.stack[0], self.stack[1])
                shape = l.toShape()
                Part.show(shape)
                self.view.removeEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.callback)

    def GetResources(self):
        return {'Pixmap': 'path_to_an_icon/line_icon.png', 'MenuText': 'Line', 'ToolTip': 'Creates a line by clicking 2 points on the screen'}

FreeCADGui.addCommand('line', line())
```


<div class="mw-translate-fuzzy">

Lo que hicimos aquí es transformar nuestra función \_\_init\_\_() en una función Activated(), porque cuando se ejecutan comandos de FreeCAD, automáticamente se ejecuta la función Activated(). También hemos añadido una función GetResources(), que informa a FreeCAD de donde puede encontrar el icono de la herramienta, y cual será el nombre y la descripción de nuestra herramienta. Cualquier imagen jpg, png o svg funcionará como un icono. Puede ser de cualquier tamaño, pero lo mejor es utilizar un tamaño que esté cerca del aspecto final, como 16x16, 24x24 o 32x32. A continuación, añadimos la clase line() como un comando oficial de FreeCAD con el método addCommand().


</div>


<div class="mw-translate-fuzzy">

Eso es todo, ahora sólo hay que reiniciar FreeCAD y tendremos un agradable entorno nuevo con una nueva herramienta line() de nuestra marca!


</div>


{{Top}}

## ¿Quieres más? 


<div class="mw-translate-fuzzy">

Si te gustó este ejercicio, ¿por qué no tratar de mejorar esta pequeña herramienta? Hay muchas cosas que se pueden hacer, como por ejemplo:

-   Agregar asistencia para los usuarios: hasta ahora hemos hecho una herramienta muy burda, el usuario podría verse un poco perdido cuando la utiliza. Se podría añadir alguna información, diciéndole qué hacer a continuación. Por ejemplo, podrías mostrar mensajes en la consola de FreeCAD. ¡Echa un vistazo en el módulo de FreeCAD.Console
-   Añadir la posibilidad de teclear de forma manual las coordenadas de los puntos 3D. Mira la función input() de Python, por ejemplo
-   Añadir la posibilidad de incluir más de 2 puntos
-   Añadir eventos para otras cosas: Ahora sólo comprobamos eventos de botón del ratón, ¿que tal si también hace algo cuando el ratón se mueva, como mostrar las coordenadas actuales?
-   Dar un nombre al objeto creado

No dudes en escribir tus preguntas o ideas en la [forum](http://forum.freecadweb.org/)!


</div>

Don\'t hesitate to ask questions or share ideas on the [forum](https://forum.freecadweb.org/)! {{Top}}



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Line drawing function/es
