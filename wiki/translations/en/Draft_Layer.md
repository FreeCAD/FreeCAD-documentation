---
- GuiCommand:
   Name:Draft Layer
   MenuLocation:Utilities → Layer
   Workbenches:[Draft](Draft_Workbench.md), [Arch](Arch_Workbench.md)
   Version:0.19
   SeeAlso:[Draft AutoGroup](Draft_AutoGroup.md), [Draft LayerManager](Draft_LayerManager.md)
---

# Draft Layer/en

## Description

The <img alt="" src=images/Draft_Layer.svg  style="width:24px;"> **Draft Layer** command creates a Draft Layer. A layer is a special kind of group with a number of [visual properties](#View.md). These properties, and any changes to them, are propagated to the objects placed inside the layer. The layers themselves are put in another special group: the Draft LayerContainer.

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Layer.svg" width=16px> [Draft Layer](Draft_Layer.md)** button.
    -   Select the **Utilities → <img src="images/Draft_Layer.svg" width=16px> Layer** option from the menu.
    -   If the layer container already exists: right-click it in the [Tree view](Tree_view.md) and select the **<img src="images/Draft_NewLayer.svg" width=16px> Add new layer** option from context menu.
2.  If it does not exist the layer container is created first.
3.  A layer is created and put in the layer container.
4.  Optionally change the [properties](#Properties.md) of the layer.
5.  Optionally put objects in the layer by drag and dropping them on the layer in the [Tree view](Tree_view.md). Objects can also be put in a layer by editing the **Group** property of the layer.
6.  Optionally [activate](#Layer_options.md) the layer.

## Context menu 

### Layer container options 

For a Draft LayerContainer these additional options are available in the [Tree view](Tree_view.md) context menu:

-    **<img src="images/Draft_Layer.svg" width=16px> Merge layer duplicates**: merges all layers with the same base label.

:   The base label of a layer is its **Label** stripped of trailing digits and spaces. All layers with the same base label are merged into a single layer with the **Label** set to that base label.

-    **<img src="images/Draft_NewLayer.svg" width=16px> Add new layer**: adds a new layer to the current document.

### Layer options 

For a Draft Layer these additional options are available in the [Tree view](Tree_view.md) context menu:

-    **<img src="images/button_right.svg" width=16px> [Activate this layer](Draft_AutoGroup.md)**: activates the selected layer.

-    **<img src="images/Draft_SelectGroup.svg" width=16px> [Select layer contents](Draft_SelectGroup.md)**: selects the objects inside the selected layer.

## Drag and drop behavior 


<small>(v0.21)</small> 

If you drop an object from a [Std Group](Std_Group.md), or a group-like object such as an [Arch BuildingPart](Arch_BuildingPart.md), on a layer in the [Tree view](Tree_view.md), it is not removed from the group, and vice versa. To remove an object from a layer it must be dropped on another layer or on the document node. There is no need to hold down the **Ctrl** key when dragging from or dropping on a layer.

## Notes

-   A new layer can also be created with the [Draft AutoGroup](Draft_AutoGroup.md) command.
-   The [BIM Workbench](BIM_Workbench.md) offers a complete [layer manager tool](BIM_Layers.md) which will eventually be included in the [Draft Workbench](Draft_Workbench.md).

## Properties

See also: [Property editor](Property_editor.md).

A Draft Layer object is derived from an [App FeaturePython](App_FeaturePython.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Layer}}

-    **Group|LinkList**: specifies the objects that are inside the layer.

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

## Scripting

See also: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To create a Draft Layer use the `make_layer` method of the Draft module. To add objects to, or remove objects from, a layer change its `Group` property.


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



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Layer/en
