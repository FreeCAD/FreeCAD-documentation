---
- GuiCommand:/es
   Name:Arch Window
   Name/es:Arquitectura Ventana
   MenuLocation:Arquitectura → Ventana
   Workbenches:[Arquitectura](Arch_Workbench/es.md)
   Shortcut:**W** **I**
   SeeAlso:[Arquitectura Muro](Arch_Wall/es.md), [Arquitectura Añadir](Arch_Add/es.md)
---

# Arch Window/es

## Descripción

Un [Arquitectura Ventana](Arch_Window/es.md) es un objeto base para todo tipo de objetos \"incrustables\", como ventanas y puertas. Está diseñado para ser independiente, o \"alojado\" dentro de otro componente como un [Arquitectura Muro](Arch_Wall/es.md), [Arquitectura Estructura](Arch_Structure/es.md), o [Arquitectura Techo](Arch_Roof/es.md). Tiene su propia geometría, que puede estar formada por varios componentes sólidos (comúnmente un marco y paneles interiores), y también define un volumen que se sustrae de los objetos anfitriones, para crear una abertura.

Los objetos ventana se basan en objetos 2D cerrados, como [Borrador Rectángulos](Draft_Rectangle/es.md) o [Croquis](Sketcher_Workbench.md), que se utilizan para definir sus componentes internos. Por lo tanto, el objeto 2D base debe contener varios hilos cerrados, que pueden combinarse para formar paneles rellenos (un hilo) o marcos (varios hilos).

La herramienta Ventana presenta varios **preajustes**\'; esto permite al usuario crear tipos comunes de ventanas y puertas con ciertos parámetros editables, sin necesidad de que el usuario cree manualmente los objetos y componentes 2D base.

All information applicable to an [Arch Window](Arch_Window.md) also applies to an [Arch Door](Arch_Door.md), as it\'s the same underlying object. The main difference between a Window and a Door is that the Door has an internal panel that is shown opaque (the door itself), while the Window has a panel that is partially transparent (the glass).

<img alt="" src=images/Arch_Window_example.jpg  style="width:600px;"> 
*Ventana construida sobre un [Borrador Rectángulo](Draft_Rectangle/es.md), luego insertada en un [Arquitectura Muro](Arch_Wall/es.md). Usando la operación [Arquitectura Añadir](Arch_Add/es.md) se corta automáticamente una abertura correcta en el muro anfitrión.*

<img alt="" src=images/Arch_Window_example2.jpg  style="width:600px;"> 
*Complex window being constructed on top of a [Sketch](Sketcher_Workbench.md). When entering the window's edit mode you can create different components, set their thickness, and select and assign wires from the sketch to them.*

## Utilización

### Usando un preajustado 


<div class="mw-translate-fuzzy">

1.  Opcionalmente, seleccione un objeto Arch. Si no se selecciona ningún objeto, la ventana se insertará en el objeto debajo del mouse al colocar la ventana.
2.  Presione el botón {{KEY | <img src="images/_Arch_Window.png_" width= 16px> [[Arch Window]]}}, o presione {{KEY | W}} luego la tecla {{KEY | I}}
3.  Seleccione uno de los predefinidos en la lista
4.  Completa los parámetros deseados
5.  Presione el botón **Ok**


</div>

#### Additional presets 

If you install the [Parts Library](Parts_Library_Workbench.md) from the [Addon Manager](Std_AddonMgr.md), the window tool will search this library for additional presets. These presets are FreeCAD files containing a single window based on a parametric sketch that has named constrains. You may place additional presets in the {{FileName|parts_library}} directory so that they are found by the window tool.


{{FileName|$ROOT_DIR/Mod/parts_library/Architectural Parts/Doors/Custom/}}

{{FileName|$ROOT_DIR/Mod/parts_library/Architectural Parts/Windows/Custom/}}

It is also possible to place custom windows and doors in your user {{FileName|Arch}} directory. <small>(v0.20)</small> 


{{FileName|$ROOT_DIR/Mod/Arch/Doors/Custom/}}

{{FileName|$ROOT_DIR/Mod/Arch/Windows/Custom/}}

-   The {{FileName|$ROOT_DIR}} is the user directory where FreeCAD configuration files, macros, and external workbenches are stored. It can be found be entering `FreeCAD.getUserAppDataDir()` in the [Python console](Python_console.md).
    -   On Linux it is usually {{FileName|/home/username/.FreeCAD/}}
    -   On Windows it is usually {{FileName|C:\Users\username\Application Data\FreeCAD\}}
    -   On Mac OSX it is usually {{FileName|/Users/username/Library/Preferences/FreeCAD/}}
-   The subdirectory name {{FileName|Custom}} is just a suggestion, any name can be used. But the files must be placed in one or more subdirectories inside the {{FileName|Doors}} or {{FileName|Windows}} directories.

### Creando desde cero 

1.  Opcionalmente, seleccione una cara en el objeto Arch donde desee que se incluya la ventana
2.  Cambie al [Sketcher Workbench](Sketcher_Workbench.md)
3.  Crea un nuevo boceto
4.  Dibuja uno o más lineas cerradas
5.  Cerrar el boceto
6.  Vuelva al [Arch Workbench](Arch_Workbench.md)
7.  Presione el botón {{KEY | <img src="images/_Arch_Window.png_" width= 16px> [[Arch Window]]}}, o presione {{KEY | W}} luego la tecla {{KEY | I}}
8.  Ingrese al modo Editar haciendo doble clic en la ventana en la vista de árbol, para ajustar los componentes de la ventana

When creating the sketch, pay close attention to the creation order of the loops; the numbering of the \"wires\" in the [task panel](task_panel.md) (\"Window elements\") depends on this.

## Predefinidos

Los siguientes predefinidos están disponibles:

Image:ParametersDoorGlass.svg\|Glass door Image:ParametersDoorSimple.svg\|Simple door Image:ParametersWindowDouble.svg\|Double-opening window Image:ParametersWindowFixed.svg\|Fixed window Image:ParametersWindowSimple.svg\|Single-opening window Image:ParametersWindowStash.svg\|Sash-opening window

## Componentes constructivos 

Windows puede incluir 3 tipos de componentes: paneles, marcos y louvres. Los paneles y las louvres están hechos de una linea cerrada, que se extruye, mientras que los marcos están hechos de 2 o más lineas cerradas, donde cada uno se extruye, luego los más pequeños se restan del más grande. Puede acceder, crear, modificar y eliminar componentes de una ventana en el modo de edición (haga doble clic en la ventana en la vista de árbol). Los componentes tienen las siguientes propiedades:

-   **Nombre**: un nombre para el componente
-   **Tipo**: el tipo de componente. Puede ser \"Marco\", \"Panel de vidrio\", \"Panel sólido\" o \"Louvres\"
-   **Wires**: una lista de lineas separadas por comas en la que el componente se basa
-   **Grosor**: el espesor de extrusión del componente
-   **Z Offset**: la distancia entre el componente y su base 2D linea(s)
-   **Bisagra**: Esto le permite seleccionar un borde del objeto base 2D, luego establecer ese borde como una bisagra para este componente y los siguientes en la lista
-   **Modo de apertura**: si definió una bisagra en este componente o en cualquier otro anterior de la lista, establecer el modo de apertura permitirá que la ventana parezca abierta o que muestren símbolos de apertura 2D en planta o alzado.

<img alt="" src=images/Arch_Window_options.jpg  style="width:600px;">

## Opciones


<div class="mw-translate-fuzzy">

-   Windows comparte las propiedades y comportamientos comunes de todos [ Arch Components](Arch_Component.md)
-   Si la casilla **Autoincluir** en el panel de tareas de creación de ventanas está desmarcada, la ventana no se insertará en ningún objeto Anfitrion al momento de la creación.
-   Agregue una ventana seleccionada a [ Muro](Arch_Wall/es.md) seleccionando ambos, luego presione el botón {{KEY | <img src="images/_Arch_Add.png_" width= 16px> [[Arch Add]]}}.
-   Eliminar una ventana seleccionada de un [ muro](Arch_Wall/es.md) seleccionando la ventana, luego presionando el botón {{KEY | <img src="images/_Arch_Remove.png_" width= 16px> [[Arch Remove]]}}.
-   Cuando se usan predefinidos, a menudo es conveniente activar el \"Near\" [Draft Snap](Draft_Snap.md), para que pueda ajustar su ventana a una cara existente.
-   El agujero creado por una ventana en su objeto anfitrión está determinado por dos propiedades: **Profundidad del agujero** y **Hole Wire** ({{Version | 0.17}}). El número de Hole Wire se puede seleccionar en la vista 3D desde el panel de tareas de la ventana disponible al hacer doble clic en la ventana en la vista de árbol
-   Windows puede hacer uso de [ Multi-Materiales](Arch_MultiMaterial/es.md). La ventana buscará en el Multi-Material adjunto capas de material con el mismo nombre para cada uno de sus componentes de ventana, y lo usará si encuentra alguno. Por ejemplo, un componente llamado \"OuterFrame\" buscará en el Multi-Material adjunto, para una capa de material llamada \"OuterFrame\". Si se encuentra dicha capa de material, su material se atribuirá al componente OuterFrame. El valor de espesor de la capa de material no se tiene en cuenta.


</div>

## Aberturas


**See also:**

[Tutorial for open windows](Tutorial_for_open_windows.md)


<div class="mw-translate-fuzzy">

Las puertas y ventanas pueden aparecer parcial o totalmente abiertas en el modelo 3D, o pueden mostrar símbolos de apertura tanto en plano como en elevación. En consecuencia, estos también aparecerán en las vistas 2D extraídas generadas por [Draft Shape2DView/es](Draft_Shape2DView/es.md) o [TechDraw Workbench/es](TechDraw_Workbench/es.md) o [Drawing Workbench/es](Drawing_Workbench/es.md). Para obtener esto, al menos uno de los componentes de la ventana debe tener una bisagra y un modo de apertura definido (consulte la sección \"Componentes de la construcción\" más arriba). Luego, usando las propiedades **Apertura**, **Plan de símbolos** o **Elevación de símbolos**, puede configurar el aspecto de la ventana:


</div>

<img alt="" src=images/Arch_window_openings.png  style="width:600px;">


<div class="mw-translate-fuzzy">

<img alt="Una puerta que muestra de izquierda a derecha el plan de símbolos, la elevación del símbolo y las propiedades de apertura en el trabajo" src=images/Arch_window_openings.png  style="width:600px;">


</div>

## Defining window types 

Windows can also take advantage of other tools, specifically [PartDesign](PartDesign_Workbench.md) workflows, to define a type. A type is an object that defines the shape of the window. This is specially well suited to work with [App Parts](App_Part.md):

<img alt="" src=images/Arch_window_type_example.png  style="width:800px;">

[Download the example file shown above](https://github.com/FreeCAD/Examples/blob/master/Arch_Example_Files/Window_Type.FCStd)

### Example workflow 

-   Create a window frame object, a glass panel, and any other window component you need, using [Part Workbench](Part.md) or [PartDesign](PartDesign_Workbench.md) tools.
-   For example, create a base rectangular sketch for your window, then a profile sketch for the frame, and create a [Part Sweep](Part_Sweep.md) to sweep the profile around the base sketch. Create a [Part Offset2D](Part_Offset2D.md) from the base sketch, then a [Part Extrude](Part_Extrude.md) to create the glass panel
-   Make sure all these pieces have a unique, meaningful name (for example, \"Frame\" or \"Glass Panel\")
-   Create an [App Part](App_Part.md), and place all your subcomponents in it
-   Create a volume to be subtracted from the wall, for example by extruding the base sketch. Add this volume to the App Part. Make sure the volume is turned off
-   If using FreeCAD version 0.19 or later, you can add 3 properties to your App Part, by right-clicking its properties view, and check \"Show All\". Add the following properties (all of them are optional, the group doesn\'t matter):
    -   **Height** as a PropertyLength and link it, for example, to a vertical constraint of your base sketch
    -   **Width** as a PropertyLength and link it, for example, to a horizontal constraint of your base sketch
    -   **Subvolume** as a PropertyLink and link it to the volume to be subtracted that we created above
    -   **Tag** as a PropertyString

### Materials

Our window type is now ready. We can create window objects from it, simply by selecting the App Part and pressing the window button. The \"Height\", \"Width\", \"Subvolume\" and \"Tag\" properties of the window will be linked to the corresponding property of the App Part, if existing.

To build a material for type-based windows:

-   Create a [multi-material](Arch_MultiMaterial.md)
-   Create one entry in the multi-material for each component of your App Part. For example, one \"Frame\", one \"Glass panel\" as we used above. Make sure to use the exact same name.
-   Attribute that multi-material to each of the windows derived from the same type

You can use any other kind of workflow than the one described above, the important points to remember are:

-   The type object must be one object, no matter the type (App Part, PartDesign Body, Part Compound, or even another Arch Window)
-   The type object must have a \"Subvolume\" property (linked to the window\'s Subvolume property) for openings in host objects to work
-   The type object must have a \"Group\" property with different children with same names as multi-material items for multi-materials to work

## Propiedades

-    {{PropertyData/es | Height}}: El alto de esta ventana

-    {{PropertyData/es | Width}}: El ancho de esta ventana

-    {{PropertyData/es | Hole Depth}}: La profundidad del agujero creado por esta ventana en su objeto anfitrión

-    {{PropertyData/es | Hole Wire}}: el número de linea del objeto base que se usa para crear un agujero en el objeto anfitrión de esta ventana. Este valor puede establecerse gráficamente al hacer doble clic en la ventana en la vista de árbol. Establecer un valor de 0 hará que la ventana seleccione automáticamente su linea más grande para el agujero.

-    {{PropertyData/es | Window Parts}}: una lista de cadenas (5 cadenas por componente, configurando las opciones de componentes anteriores)

-    {{PropertyData/es | Louvre Width}}: si alguno de los componentes está configurado en \"Louvres\", esta propiedad define el tamaño de los elementos del louvre

-    {{PropertyData/es | Louvre Spacing}}: si alguno de los componentes está configurado en \"Louvres\", esta propiedad define el espacio entre los elementos del Louvre

-    {{PropertyData/es | Opening}}: todos los componentes que tienen su modo de apertura establecido, y siempre que se haya definido una bisagra en ellos o en un componente anterior de la lista, aparecerán abiertos en un porcentaje definido por este valor

-    {{PropertyData/es | Symbol Plan}}: muestra el símbolo de apertura 2D en el plan

-    {{PropertyData/es | Elevación de símbolo}}: muestra el símbolo de apertura 2D en alzado

## Scripting


<div class="mw-translate-fuzzy">

## Programación


</div>


<div class="mw-translate-fuzzy">

La herramienta Ventana puede usarse en [macros](macros/es.md) y desde la consola de Python utilizando la siguiente función:


</div>


```python
Window = makeWindow(baseobj=None, width=None, height=None, parts=None, name="Window")
```


<div class="mw-translate-fuzzy">


:   crea una ventana basada en el objeto dado


</div>

Ejemplo: 
```python
import FreeCAD, Draft, Arch

Rect1 = Draft.makeRectangle(length=900, height=3000)
Window = Arch.makeWindow(Rect1)
FreeCAD.ActiveDocument.recompute()
```

You can also create a Window from a preset. 
```python
Window = makeWindowPreset(windowtype, width, height, h1, h2, h3, w1, w2, o1, o2, placement=None)
```


<div class="mw-translate-fuzzy">

<img alt="" src=images/Arch_Window_example2.jpg  style="width:600px;">


</div>

Ejemplo: 
```python
import FreeCAD, Arch

base = FreeCAD.Vector(2000, 0, 0)
Axis = FreeCAD.Vector(1, 0, 0)
place=FreeCAD.Placement(base, FreeCAD.Rotation(Axis, 90))

Door = Arch.makeWindowPreset("Simple door",
                             width=900, height=2000,
                             h1=100, h2=100, h3=100, w1=200, w2=100, o1=0, o2=100,
                             placement=place)
```


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Window/es
