---
- GuiCommand:/es
   Name:Arch Panel
   Name/es:Arch Panel
   MenuLocation:Arch → Panel Tools → Panel
   Workbenches:[Arch](Arch_Workbench/es.md)
   Shortcut:**P** **A**
   Version:0.15
   SeeAlso:[Arch Panel Cut](Arch_Panel_Cut/es.md), [Arch Panel Sheet](Arch_Panel_Sheet/es.md)
---

# Arch Panel/es


</div>

## Descripción

Esta herramienta le permite construir todo tipo de elementos tipo panel, típicamente para construcciones de paneles como el proyecto [WikiHouse](http://www.wikihouse.cc/), pero también para todo tipo de objetos que se basan en un perfil plano.

<img alt="" src=images/Arch_Panel_example.jpg  style="width:700px;">

*La imagen de arriba muestra una serie de objetos del panel, simplemente hechos de contornos 2D importados de un archivo DXF. Luego se pueden rotar y ensamblar para crear estructuras.*


<div class="mw-translate-fuzzy">

Desde la versión 0.17, el Arch panel también se puede usar para crear perfiles corrugados o trapezoidales:


</div>

<img alt="" src=images/Arch_panel_wave.jpg  style="width:700px;">

## Utilización


<div class="mw-translate-fuzzy">

1.  Seleccione una forma 2D (borrador de objeto, cara o boceto) - opcional
2.  Presione el botón **<img src="images/_Arch_Panel.png" width=16px> [Arch Panel](Arch_Panel/es.md)
**, o presione **P** luego las teclas **A**
3.  Ajuste las propiedades deseadas


</div>


<div class="mw-translate-fuzzy">

## Limitaciones


</div>


<div class="mw-translate-fuzzy">

-   Actualmente no existe un sistema automático para producir placas de corte 2D a partir de objetos del panel, pero esa característica está en los planes y se agregará en el futuro.
-   Esta herramienta no está disponible en versiones de FreeCAD antes de 0.15


</div>

## Opciones


<div class="mw-translate-fuzzy">

-   Los paneles comparten las propiedades y comportamientos comunes de todos [Arch Components](Arch_Component/es.md)
-   El grosor de un panel se puede ajustar después de la creación
-   Presione **ESC** o el botón **'''Cancel'''** para cancelar el comando actual.
-   Hacer doble clic en el panel en la vista de árbol después de haber sido creado le permite ingresar al modo de edición y acceder y modificar sus adiciones y sustracciones
-   Es posible crear paneles formados automáticamente por más de una capa de un material, al aumentar su propiedad sheets/hojas.
-   Los paneles pueden hacer uso de [Multi-Materials](Arch_MultiMaterial/es.md). Al usar un multi-material, el panel se convertirá en multicapa, utilizando los espesores especificados por el multi-material. Cualquier capa con un espesor de cero tendrá su espesor definido automáticamente por el espacio restante definido por el propio valor de Grosor del Panel, después de restar las otras capas.


</div>

## Propiedades


<div class="mw-translate-fuzzy">

-    {{PropertyData/es|Length}}: la longitud del panel

-    {{PropertyData/es|Width}}: El ancho del panel

-    {{PropertyData/es|Thickness}}: el grosor del panel

-    {{PropertyData/es|Area}}: el área del panel (automático)

-    {{PropertyData/es|Sheets}}: la cantidad de hojas de material de las que está hecho el panel

-    {{PropertyData/es|Wave Length}}: la longitud de la ola para paneles corrugados

-    {{PropertyData/es|Wave Height}}: la altura de la ola para paneles corrugados

-    {{PropertyData/es|Wave Type}}: el tipo de onda para paneles corrugados, curvados o trapezoidales

-    {{PropertyData/es|Wave direction}}: la orientación de las ondas para paneles corrugados


</div>


<div class="mw-translate-fuzzy">

## Programación


</div>


<div class="mw-translate-fuzzy">

La herramienta Panel puede usarse en [macros](macros/es.md) y desde la consola de Python utilizando la siguiente función:


</div>


```python
Panel = makePanel(baseobj=None, length=0, width=0, thickness=0, placement=None, name="Panel")
```

-   Creates a `Panel` object from the given `baseobj`, which is a closed profile, and the given extrusion `thickness`.
    -   If no `baseobj` is given, you can provide the numerical values for the `length`, `width`, and `thickness` to create a block panel.
-   If a `placement` is given, it is used.

Ejemplo: 
```python
import FreeCAD, Draft, Arch

Rect = Draft.makeRectangle(1000, 400)
Panel = Arch.makePanel(Rect, thickness=36)
```

## Tutoriales


<div class="mw-translate-fuzzy">

-   [Wikihouse porting tutorial](Wikihouse_porting_tutorial/es.md)


</div>


<div class="mw-translate-fuzzy">


{{docnav/es|[Arch CompPanel](Arch_CompPanel.md)|[Panel Cut](Arch_Panel_Cut.md)|[Arch](Arch_Workbench.md)|IconL=Arch_CompPanel.png |IconC=Workbench_Arch.svg |IconR=Arch_Panel_Cut.svg}}


</div>

---
[documentation index](../README.md) > [Arch](Category_Arch.md) > [Arch](Arch_Workbench.md) > Arch Panel/es
