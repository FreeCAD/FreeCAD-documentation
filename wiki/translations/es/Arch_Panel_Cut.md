---
- GuiCommand:/es
   Name:Arch Panel Cut
   Name/es:Arch Corte de Panel
   MenuLocation:Arch → Panel Tools → Panel Cut
   Workbenches:[Arch](Arch_Workbench/es.md)
   Shortcut:**P** **C**
   SeeAlso:[Arch Panel](Arch_Panel/es.md), [[Arch Panel Sheet/es]], [[Arch Nest/es]], [[Path Workbench/es]]
---

# Arch Panel Cut/es


</div>

## Descripción


<div class="mw-translate-fuzzy">

Esta herramienta crea, en el documento 3D, una vista 2D plana de un [Arch Panel](Arch_Panel/es.md), que se incluirá en una [Arch Panel Sheet](Arch_Panel_Sheet/es.md) o se exportará directamente a [DXF](Draft_DXF/es.md).


</div>


<div class="mw-translate-fuzzy">

![](images/Arch_Wikihouse_02.jpg )


</div>

## Como utilizar 


<div class="mw-translate-fuzzy">

1.  Seleccione uno o más objetos [Arch Panel](Arch_Panel/es.md)
2.  Presione el botón **<img src="images/Arch_Panel_Cut.png" width=16px> [Arch Panel Cut](Arch_Panel_Cut/es.md)
**, o presione **P** luego la tecla **C**
3.  Ajuste las propiedades deseadas


</div>

## Opciones

-   Si el panel no es plano (corrugado, por ejemplo), el relieve no aparecerá en el corte del panel. Esta herramienta es útil principalmente para paneles planos
-   El corte del panel puede mostrar una etiqueta. Esta etiqueta puede ser una línea de texto personalizada o puede mostrar automáticamente la etiqueta, la etiqueta o la descripción de su panel vinculado.
-   Para ser útil en el mecanizado CNC, la etiqueta debe escribirse con una fuente adhesiva, donde las letras son polilíneas simples que la máquina puede seguir fácilmente. Al momento de la creación, el objeto Corte de Panel utilizará automáticamente la fuente especificada en Editar → Preferencias → Borrador → Textos y dimensiones → Fuente ShapeString
-   Al hacer doble clic en el corte del panel en la vista de árbol después de haber sido creado, puede ingresar al modo de edición y modificar la posición de la etiqueta.
-   Cuando necesite diseñar diferentes Cortes de panel juntos, los Cortes de panel pueden mostrar un margen, que es útil para asegurarse de que siempre haya un cierto espacio entre un corte y otro.

## Propiedades


<div class="mw-translate-fuzzy">

-    {{PropertyData/es|Source}}: el objeto [Arch Panel](Arch_Panel/es.md) mostrado por este corte

-    {{PropertyData/es|Tag Text}}: el texto para mostrar. Puede ser %tag%, %label% o %description% para mostrar la etiqueta o etiqueta del panel

-    {{PropertyData/es|Tag Size}}: el tamaño del texto de la etiqueta

-    {{PropertyData/es|Tag Position}}: la posición del texto de la etiqueta. Mantener (0,0,0) para la posición central automática

-    {{PropertyData/es|Tag Rotation}}: la rotación del texto de la etiqueta

-    {{PropertyData/es|Font File}}: la fuente del texto de la etiqueta

-    {{PropertyView/es|Margin}}: un margen que se puede mostrar fuera de la forma de corte del panel

-    {{PropertyView/es|Show Margin}}: Activa/desactiva la visualización del margen

-    {{PropertyData/es|Make Face}}: si es verdadero, el panel es una cara de la pieza, de lo contrario, una Part Wire


</div>

### View

-    **Margin**: A margin that can be displayed outside the panel cut shape

-    **Show Margin**: Turns the display of the margin on/off


<div class="mw-translate-fuzzy">

## Programación


</div>


<div class="mw-translate-fuzzy">

La herramienta Panel puede usarse en [macros](macros/es.md) y desde la consola de Python utilizando la siguiente función:


</div>


```python
View = makePanelCut(panel, name="PanelView")```

-   Creates a `View` object (2D projection) from the existing `panel`.

Ejemplo: 
```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(500, 0, 0)
p3 = FreeCAD.Vector(500, 50, 0)
p4 = FreeCAD.Vector(550, 50, 0)
p5 = FreeCAD.Vector(600, 0, 0)
p6 = FreeCAD.Vector(1000, 0, 0)
p7 = FreeCAD.Vector(1000, 400, 0)
p8 = FreeCAD.Vector(600, 400, 0)
p9 = FreeCAD.Vector(600, 350, 0)
p10 = FreeCAD.Vector(550, 350, 0)
p11 = FreeCAD.Vector(500, 400, 0)
p12 = FreeCAD.Vector(0, 400, 0)

Wire = Draft.makeWire([p1, p2, p3, p4, p5, p6,
                       p7, p8, p8, p9, p10, p11, p12], closed=True)
Panel = Arch.makePanel(Wire, thickness=36)
FreeCAD.ActiveDocument.recompute()

View = Arch.makePanelCut(Panel)
View.ViewObject.LineWidth = 3
FreeCAD.ActiveDocument.recompute()
```

## Tutoriales


<div class="mw-translate-fuzzy">

-   [Wikihouse porting tutorial](Wikihouse_porting_tutorial/es.md)


</div>


<div class="mw-translate-fuzzy">


{{docnav/es|[Panel](Arch_Panel.md)|[Panel Sheet](Arch_Panel_Sheet.md)|[Arch](Arch_Workbench/es.md)|IconL=Arch_Panel.svg |IconC=Workbench_Arch.svg |IconR=Arch_Panel_Sheet.svg}}


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Panel Cut/es
