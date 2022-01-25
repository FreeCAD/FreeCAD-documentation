---
- GuiCommand:/es
   Name:Arch Panel Sheet   Name/es:Arch Panel Sheet
   MenuLocation:Arch → Panel tools → Panel Sheet
   Workbenches:[Arch](Arch_Workbench/es.md)
   Shortcut:**P** **S**
   SeeAlso:[Arch Panel](Arch_Panel/es.md)
---

# Arch Panel Sheet/es


</div>

## Descripción

Esta herramienta permite construir una lámina 2D, incluyendo cualquier número de objetos [Arch Panel Cut](Arch_Panel_Cut/es.md), o cualquier otro objeto 2D como los realizados por [Draft Workbench](Draft_Workbench/es.md) y [Sketcher Workbench](Sketcher_Workbench/es.md). La lámina del panel se hace típicamente para cortes de layout que se realizarán por una máquina CNC. Estas hojas pueden luego exportarse a un archivo [DXF](Draft_DXF/es.md).

<img alt="" src=images/Arch_Wikihouse_03.jpg  style="width:1024px;">

<img alt="" src=images/Arch_Wikihouse_04.jpg  style="width:1024px;">

*La imagen de arriba muestra cómo aparecen las láminas del panel cuando se exportan a DXF.*

## Utilización


<div class="mw-translate-fuzzy">

1.  Opcionalmente, seleccione uno o más objetos [Arch Panel Cut](Arch_Panel_Cut/es.md) o cualquier otro objeto 2D que se encuentre en el plano XY
2.  Presione el botón **<img src="images/_Arch_Panel_Sheet.png" width=16px> [Arch Panel Sheet](Arch_Panel_Sheet/es.md)
**, o presione **P** y luego **S**
3.  Ajuste las propiedades deseadas


</div>

## Opciones

-   Después de crear la lámina del panel, con o sin objetos secundarios, se puede agregar/eliminar cualquier otro objeto secundario a/desde la lámina del panel haciendo doble clic en ella en la vista de árbol y agregando o quitando objetos de su carpeta de grupo
-   Hacer doble clic en el panel en la vista de árbol también le permite mover los objetos contenidos en esta lámina, o mover su etiqueta
-   Es posible crear automáticamente paneles compuestos de más de una lámina de un material, mediante el aumento de su propiedad de láminas
-   Las láminas del panel pueden mostrar un margen, que es útil para asegurarse de que siempre haya un espacio determinado entre los objetos internos y el borde de la lámina
-   Cuando las láminas del Panel se exportan a DXF, los contornos, agujeros internos, etiquetas de sus hijos internos se colocan en diferentes capas, como se muestra en la imagen de arriba

## Propiedades

### Data


<div class="mw-translate-fuzzy">

-    {{PropertyData/es|Height}}: la altura de la lámina

-    {{PropertyData/es|Width}}: el ancho de la lámina

-    {{PropertyData/es|Fill Ratio}}: El porcentaje del área de la lámina que se llena con cortes (automático)

-    {{PropertyData/es|Tag Text}}: el texto para mostrar

-    {{PropertyData/es|Tag Size}}: el tamaño del texto de la etiqueta

-    {{PropertyData/es|Tag Position}}: la posición del texto de la etiqueta. Mantener (0,0,0) para la posición central automática

-    {{PropertyData/es|Tag Rotation}}: la rotación del texto de la etiqueta

-    {{PropertyData/es|Font File}}: la fuente del texto de la etiqueta

-    {{PropertyData/es|Make Face}}: si es verdadero, el panel es una Part cara, de lo contrario, una Part wire

-    {{PropertyData/es|Grain Direction}}: Esto le permite informar la dirección principal de la fibra del panel (sentido horario, 0 ° significa arriba)

-    {{PropertyView/es|Margin}}: un margen que se puede mostrar dentro del borde del panel

-    {{PropertyView/es|Show Margin}}: Activa/desactiva la visualización del margen

-    {{PropertyView/es|Show Grain}}: muestra una textura de fibra (Make Face debe establecerse en True)


</div>

### View

-    **Margin**: A margin that can be displayed inside the panel border

-    **Show Margin**: Turns the display of the margin on/off

-    **Show Grain**: Shows a fiber texture (Make Face must be set to True)

## Scripting


<div class="mw-translate-fuzzy">

## Programación


</div>


<div class="mw-translate-fuzzy">

La herramienta Hoja de panel puede utilizarse en [macros](macros/es.md) y desde la consola de Python mediante la siguiente función:


</div>


```python
Sheet = makePanelSheet(panels=[], name="PanelSheet")
```

-   Creates a `Sheet` object from `panels`, which is a list of [Arch Panel](Arch_Panel.md) objects.

Ejemplo:


```python
import FreeCAD, Draft, Arch

Rect = Draft.makeRectangle(500, 200)
Polygon = Draft.makePolygon(5, 750)

p1 = FreeCAD.Vector(1000, 0, 0)
p2 = FreeCAD.Vector(2000, 400, 0)
p3 = FreeCAD.Vector(1250, 800, 0)
Wire = Draft.makeWire([p1, p2, p3], closed=True)

Panel1 = Arch.makePanel(Rect, thickness=36)
Panel2 = Arch.makePanel(Polygon, thickness=36)
Panel3 = Arch.makePanel(Wire, thickness=36)
FreeCAD.ActiveDocument.recompute()

Cut1 = Arch.makePanelCut(Panel1)
Cut2 = Arch.makePanelCut(Panel2)
Cut3 = Arch.makePanelCut(Panel3)
Cut1.ViewObject.LineWidth = 3
Cut2.ViewObject.LineWidth = 3
Cut3.ViewObject.LineWidth = 3
FreeCAD.ActiveDocument.recompute()

Sheet = Arch.makePanelSheet([Cut1, Cut2, Cut3])
```

## Tutoriales


<div class="mw-translate-fuzzy">

-   [Wikihouse porting tutorial](Wikihouse_porting_tutorial/es.md)


</div>


<div class="mw-translate-fuzzy">


{{docnav|[Panel Cut](Arch_Panel_Cut.md)|[Nest](Arch_Nest.md)|[Arch](Arch_Workbench/es.md)|IconL=Arch_Panel_Cut.svg |IconC=Workbench_Arch.svg |IconR=Arch_Nest.svg}}


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Panel Sheet/es
