# Macro Solid Sweep/es
{{Macro/es
|Name=Solid Sweep
|Icon=Macro_Solid_Sweep.png
|Translate=Solid Sweep
|Description=Crea un sólido barriendo un perfil a lo largo de una trayectoria.
|Author=Normandc
|Version=1.0
|Date=2011-12-03
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/6/6d/Macro_Solid_Sweep.png ToolBar Icon]
}}

## Descriptivo

Esta macro crea un sólido barriendo un perfil 2D a lo largo de una trayectoria previamente seleccionada en la vista 3D. Los elementos 2D se pueden crear con las herramientas habituales de FreeCAD.

El sólido resultante no es paramétrico. Si cambias el perfil o la trayectoria, necesitarás ejecutar la macro de nuevo.

<img alt="A few examples of sweeping all using the same oblong section and three kinds of trajectory." src=images/Solid_sweep.png‎  style="width:500px;">


<div class="mw-translate-fuzzy">

## Como se utiliza 

-   Crea dos elementos 2D, uno para la sección y otro para la trayectoria, de los tipos indicados abajo.
-   Selecciona, en el árbol del Proyecto o en la vista 3D, primero la trayectoria y después el perfil. El orden es importante!
-   Abre el gestor de macros, selecciona la macro y pulsa en \"Ejecutar\".
-   Se creará un sólido **barrido** en el árbol del Proyecto.


</div>


<div class="mw-translate-fuzzy">

## Elementos 2D soportados 

-   Contornos
-   <img alt="" src=images/Sketcher_NewSketch.png  style="width:32px;"> [Croquis](Sketcher_Workbench/es.md)
-   ![](images/Draft_BSpline.png ) [BSplines](Draft_BSpline/es.md)
-   Primitivas 2D del menú *Parametricas → <img alt="" src=images/Part_CreatePrimitives.png  style="width:32px;"> [Crear Primitivas](Part_CreatePrimitives/es.md) \...* (circunferencia, hélice)


</div>

## Trucos

-   La sección debe ser un perfil cerrado o el resultado no será un sólido.
-   La sección no necesita ubicarse en la trayectoria, pero es preferible que sea normal a ella.
-   La trayectoria puede ser un perfil abierto o cerrado (circunferencias, o líneas y arcos) pero todos los elementos deben ser tangentes o la forma resultante será inesperada. Por ejemplo, una trayectoria con esquinas rectas como un rectángulo no producirá un sólido.
-   Si el sólido se retuerce, edita la macro para cambiar el valor de *isFrenet* a cero y prueba de nuevo.
-   Configurar la variable *makeSolid* a cero en la macro producirá una colección de superficies con finales abiertos.

## La macro 

ToolBar Icon ![](images/Macro_Solid_Sweep.png )

**Macro\_Solid\_Sweep.FCMacro**


{{MacroCode|code=
import Part, FreeCAD, math, PartGui, FreeCADGui
from FreeCAD import Base

# get the selected objects, with first selection for the trajectory and second for the section
s = FreeCADGui.Selection.getSelection()
try:
     shape1=s[0].Shape
     shape2=s[1].Shape
except:
     print "Wrong selection"

traj = Part.Wire([shape1])
section = Part.Wire([shape2])

# create Part objec in the current document
myObject=App.ActiveDocument.addObject("Part::Feature","Sweep")

# variable makeSolid = 1 to create solid, 0 to create surfaces
makeSolid = True #1
isFrenet = True #1

# create a 3D shape and assigh it to the current document
Sweep = Part.Wire(traj).makePipeShell([section],makeSolid,isFrenet)
myObject.Shape = Sweep

}}

## Créditos

Gracias a [Wmayer](User_Wmayer.md) por su ayuda al escribir esta macro.

Dos ejemplo de uso se pueden ver en [este hilo del foro](http://forum.freecadweb.org/viewtopic.php?f=8&t=1222&start=50#p11120), así como enlaces para descargar archivos FCStd. Utilizando una hélice como trayectoria, un sólido barrido se puede utilizar para crear un tornillo.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Solid Sweep/es
