---
 GuiCommand:
   Name: Arch Site
   Name/es: Arquitectura Ubicación
   MenuLocation: Arquitectura , Ubicación
   Workbenches: Arch_Workbench/es
   Shortcut: **S** **I**
   SeeAlso: Arch_Floor/es, Arch_Building/es
---

# Arch Site/es


</div>



## Descripción


<div class="mw-translate-fuzzy">

El Arquitectura Ubicación es un objeto especial que combina propiedades de un objeto de grupo estándar de FreeCAD y objetos de Arch. Es particularmente adecuado para representar un sitio de proyecto completo o terreno. En trabajos arquitectónicos basados en IFC, se usa principalmente para organizar su modelo, al contener objetos [Edificio](Arch_Building/es.md). El sitio también se usa para administrar y mostrar un terreno físico, y puede calcular volúmenes de tierra para agregar o eliminar.


</div>



## Utilización


<div class="mw-translate-fuzzy">

1.  Opcionalmente, seleccionar uno o más objetos a ser incluidos en tu nueva ubicación
2.  Pulse el botón **<img src="images/Arch_Site.svg" width=16px> [Arquitectura Ubicación](Arch_Site/es.md)
**, o pulsar las teclas **S** y **I**


</div>



## Opciones


<div class="mw-translate-fuzzy">

-   Después de la creación de una ubicación, puedes añadirle más objetos arrastrando y soltándolos en la vista en árbol o utilizando la herramienta **<img src="images/Arch_Add.svg" width=16px> [Arquitectura Añadir](Arch_Add/es.md)**. Esto solo determina qué objeto forma parte del sitio determinado y no tiene ningún efecto en el terreno en sí.
-   Puedes eliminar objetos de una ubicación arrastrando y soltándolos fuera en la vista de árbol o utilizando la herramienta **<img src="images/Arch_Remove.png" width=16px> [Arquitectura Eliminar](Arch_Remove/es.md)
**
-   Puede agregar un objeto de terreno editando la propiedad **Terreno** del Sitio. El terreno debe ser una caparazón o superficie abierta.
-   Puede agregar volúmenes para agregar o restar del terreno base, haciendo doble clic en el Sitio y agregando objetos a sus grupos Resta o Adiciones. Los objetos deben ser sólidos.

-   La propiedad **Vector Extrusión** se puede usar para resolver algunos problemas que pueden aparecer al trabajar con sustracciones y adiciones. Para realizar esas adiciones / sustracciones, la superficie del terreno se extruye en un sólido, que luego se une / resta apropiadamente. Dependiendo de la topología del terreno, esta extrusión puede fallar con el vector de extrusión predeterminado. Por lo tanto, es posible que pueda solucionar el problema cambiando este a un valor diferente.


</div>



## Propiedades

### Data


<div class="mw-translate-fuzzy">

### Datos

-    **Address**: la calle y el número de este sitio

-    **Postal Code**: el código postal o postal de este sitio

-    **City**: La ciudad de este sitio

-    **Country**: El país de este sitio

-    **Latitude**: la latitud de este sitio

-    **Longitude**: la longitud de este sitio

-    **Url**: una URL que muestra este sitio en un sitio web de mapas

-    **Projected Area**: el área de la proyección de este objeto en el plano XY

-    **Perimeter**: la longitud del perímetro de este terreno

-    **Addition Volume**: el volumen de tierra que se agregará a este terreno

-    **Subtraction Volume**: el volumen de tierra que se eliminará de este terreno

-    **Extrusion Vector**: un vector de extrusión para usar cuando se realizan operaciones booleanas

-    **Remove Splitter**: elimina los divisores de la forma resultante

-    **Declination**: El ángulo entre el Norte verdadero y la dirección Norte en este documento, es decir, el eje Y. {{version/es|0.18}} Esto significa que por defecto el Norte apunta al eje Y, y el Este al eje X; el ángulo se incrementa en sentido contrario a las agujas del reloj. Esta propiedad se conocía anteriormente como **Desviación Norte**.

-    **Fichero EPW**: Permite adjuntar un archivo EPW de la [Ladybug EPW data website](https://www.ladybug.tools/epwmap/) a este sitio. Esto es necesario para mostrar los diagramas de rosa de los vientos {{version/es|0.19}}


</div>

### View

-    **Solar Diagram**: Shows or hides the solar diagram

-    **Solar Diagram Color**: The color of the solar diagram

-    **Solar Diagram Position**: The position of the solar diagram

-    **Solar Diagram Scale**: The scale of the solar diagram

-    **Wind Rose**: Shows or hides the wind rose diagram (requires the **EPW File** data property filled, and the Ladybug Python module installed (see below)



## Flujo de trabajo típico 


<div class="mw-translate-fuzzy">

Comienza creando un objeto que represente tu terreno. Debe ser una superficie abierta, no un sólido. Por ejemplo, es fácil importar datos de malla, que se pueden convertir en una Forma de Parte desde el menú **Pieza → Crear Forma desde Malla**. A continuación, cree un objeto Sitio, y establezca su propiedad **Terreno** a la Pieza que acabamos de crear:


</div>

![](images/Arch_site_example_01.jpg )

Cree algunos volúmenes (deben ser sólidos) que representen las áreas que desea que se excaven o rellenen. Haga doble clic en el objeto del Sitio en la Vista en árbol y agregue estos volúmenes a los grupos Adiciones o Restas. Haga clic en Aceptar.

![](images/Arch_site_example_02.jpg )

La geometría del sitio se volverá a calcular y se volverán a calcular las áreas, el perímetro y las propiedades de volúmenes.

![](images/Arch_site_example_03.jpg )



## Diagramas solares y eólicos 


<div class="mw-translate-fuzzy">

Si [Ladybug](https://www.ladybug.tools/ladybug.html) está instalado en su sistema, [Arch Sites](Arch_Site/es.md) puede mostrar un diagrama solar y/o una rosa de los vientos. Para ello, **Longitud**, **Latitud** y **Declinación** (antes **Desviación Norte**) deben estar correctamente configurados, y **Diagrama Solar** o **Rosa de Viento** configurados a `True`. Respectivamente {{Version/es|0.17}} y {{Version/es|0.19}}


</div>

**Note**: If you don\'t have Ladybug, [pysolar](http://pysolar.org/) is still supported to generate solar diagrams, but not wind roses. Pysolar 0.7 or above is required. However, Ladybug is a much more powerful tool that will probably be used more in the future, so we recommend using it instead of pysolar. Ladybug can be installed simply via [pip](https://github.com/ladybug-tools/ladybug).

![](images/Freecad-solar-diagram.jpg )

## Scripting


<div class="mw-translate-fuzzy">

## Guión


**Ver también:**

[Borrador API](Arch_API/es.md) y [Fundamentos de Guión FreeCAD](FreeCAD_Scripting_Basics/es.md).


</div>


<div class="mw-translate-fuzzy">

La herramienta Ubicación se puede utilizar en [macros](macros/es.md) y desde la consola de [Python](Python/es.md) utilizando la siguiente función:


</div>


```python
Site = makeSite(objectslist=None, baseobj=None, name="Site")
```

-   Crea un objeto `Site` a partir de `objectslist`, que es una lista de objetos, o `baseobj`, que es un `Shape` o `Terrain`.

Ejemplo: 
```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
Wall = Arch.makeWall(baseline, length=None, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

Building = Arch.makeBuilding([Wall])
Site = Arch.makeSite([Building])

FreeCAD.ActiveDocument.recompute()
FreeCAD.Gui.ActiveDocument.ActiveView.viewIsometric()
```



### Diagrama solar 

Siempre que el módulo `pysolar` esté presente, se puede añadir un diagrama solar al sitio. Establezca los ángulos de longitud, latitud y declinación según corresponda, así como una escala adecuada para el tamaño de su modelo.

Tenga en cuenta que se requiere Pysolar 0.7 o superior, y esta versión sólo funciona con Python 3.


```python
Site.Longitude = -46.38
Site.Latitude = -23.33
Site.Declination = 30
#Site.Compass = True

Site.ViewObject.SolarDiagram = True
Site.ViewObject.SolarDiagramScale = 10000
FreeCAD.ActiveDocument.recompute()
```



### Diagrama solar independiente del ubicación 

Se puede crear un diagrama solar con la siguiente función, independientemente de cualquier sitio. 
```python
Node = makeSolarDiagram(longitude, latitude, scale=1, complete=False)
```

-   Crea un diagrama solar como un nodo Pivy, utilizando `longitude` y `latitude`, con un `scale` opcional.
-   Si `complete` es `True`, se dibujan los 12 meses, que muestran el [analemma](https://en.wikipedia.org/wiki/Analemma) solar completo.


```python
import FreeCADGui, Arch

Node = Arch.makeSolarDiagram(-46.38, -23.33, scale=10000, complete=True)
FreeCAD.Gui.ActiveDocument.ActiveView.getSceneGraph().addChild(Node)
```


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > Arch Site/es
