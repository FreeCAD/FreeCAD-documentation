---
- GuiCommand:/it
   Name:Draft Layer
   Name/it:Strato
   Workbenches:[Draft](Draft_Workbench/it.md), [Arch](Arch_Workbench/it.md)
   MenuLocation:Draft → Utilità → Strato
   Version:0.19
   See also:[Draft AutoGruppo](Draft_AutoGroup/it.md)
---

# Draft Layer/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo [Strato](Draft_Layer/it.md) crea un tipo speciale di gruppo che controlla le proprietà visive degli oggetti posizionati al suo interno. Modificando le proprietà dello strato, come la larghezza della linea, il colore della linea, il colore della forma e la trasparenza, le modifiche vengono propagate agli oggetti che utilizzano la proprietà Strato.


</div>


<div class="mw-translate-fuzzy">

Questo strumento sostituisce Draft VisGroup a partire da FreeCAD 0.19.


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Andare nel menu **Draft → Utilità → <img src="images/Draft_Layer.svg" width=16px> Strato**.
2.  Modificare le proprietà di visualizzazione desiderate dello strato.


</div>

## Context menu 

### Layer container options 

For a Draft LayerContainer these additional options are available in the [Tree view](Tree_view.md) context menu:

-    **<img src="images/Draft_Layer.svg" width=16px> Merge layer duplicates**: merges all layers with the same base label.

:   The base label of a layer is its **Label** stripped of trailing digits and spaces. All layers with the same base label are merged into a single layer with the **Label** set to that base label. This does not work in FreeCAD version 0.19.

-    **<img src="images/Draft_NewLayer.svg" width=16px> Add new layer**: adds a new layer to the current document.

### Layer options 

For a Draft Layer these additional options are available in the [Tree view](Tree_view.md) context menu:

-    **<img src="images/button_right.svg" width=16px> [Activate this layer](Draft_AutoGroup.md)**: activates the selected layer.

-    **<img src="images/Draft_SelectGroup.svg" width=16px> [Select layer contents](Draft_SelectGroup.md)**: selects the objects inside the selected layer.

## Notes

-   A new layer can also be created with the [Draft AutoGroup](Draft_AutoGroup.md) command.
-   The [BIM Workbench](BIM_Workbench.md) offers a complete [layer manager tool](BIM_Layers.md) which will eventually be included in the [Draft Workbench](Draft_Workbench.md).

## Proprietà

See also: [Property editor](Property_editor.md).

A Draft Layer object is derived from an [App FeaturePython](App_FeaturePython.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Layer}}


<div class="mw-translate-fuzzy">

-    **Group**: specifica gli elementi che fanno parte del gruppo.

-   Proprietà visive che possono essere modificate e propagate agli oggetti: **Stile di disegno**, **Colore della linea**, **Larghezza della linea**, **Colore della forma**, **Trasparenza**, e **Visibilità**.


</div>

### View


{{TitleProperty|Layer}}

The properties in this section are applied to objects that are put inside the layer. And any changes to these properties are propagated to them. For two properties, **Line Color** and **Shape Color**, this behavior is optional.

-    **Draw Style|Enumeration**: specifies the draw style of the layer: {{value|Solid}}, {{value|Dashed}}, {{value|Dotted}} or {{value|Dashdot}}

-    **Line Color|Color**: specifies the line color of the layer.

-    **Line Width|Float**: specifies the line width of the layer.

-    **Override Line Color Children|Bool**: specifies if changes to the **Line Color** of the layer are propagated to the objects inside the layer.

-    **Override Shape Color Children|Bool**: specifies if changes to the **Shape Color** of the layer are propagated to the objects inside the layer.

-    **Shape Color|Color**: specifies the shape color of the layer.

-    **Transparency|Percent**: specifies the transparency of the layer.


{{TitleProperty|Print}}

-    **Line Print Color|Color**: specifies the line print color of the layer.

-    **Use Print Color|Bool**: specifies if the **Line Print Color|** of the layer is used when a [TechDraw DraftView](TechDraw_DraftView.md) is created from the objects inside the layer.

## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)


</div>


<div class="mw-translate-fuzzy">

Per aggiungere o rimuovere oggetti dallo strato, sovrascrivere semplicemente il suo attributo `Group`.


</div>


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

layer = Draft.make_layer(line_color=(1.0, 0.0, 0.0, 0.0),
                         shape_color=(1.0, 1.0, 0.0, 0.0))

polygon1 = Draft.make_polygon(5, radius=1000)
polygon2 = Draft.make_polygon(3, radius=500)
polygon3 = Draft.make_polygon(6, radius=220)
layer.Group = [polygon1, polygon2, polygon3]

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Layer/it
