---
 GuiCommand:
   Name: BIM Layers
   MenuLocation: Manage , Manage layers...
   Workbenches: BIM_Workbench
---

# BIM Layers

## Description

The **Layers Manager** allows you to manage [layers](Draft_Layer.md). Layers are a special kind of group that controls the visual properties of objects placed inside of it. By changing the properties of the Layer, such as line width, line color, shape color and transparency, the changes are propagated to its child objects. Layers don\'t interfere with any other FreeCAD structure such as [groups](Std_Group.md) or [Building parts](Arch_BuildingPart.md), so any object can be at the same time part of a layer and part of a group.

 <img alt="" src=images/BIM_layers_screenshot.png  style="width:600px;">  
*Layers manager*

Layers are imported and exported from/to [IFC](Arch_IFC.md) and [DXF/DWG](Draft_DXF.md).

The layers manager allow you to manage your layers, add or remove layers, or change their visual properties. To add objects to a layer, simply drag them into the layer in the [tree view](Tree_view.md). To remove them, drag them from the layer and drop them into the document root.

## NativeIFC

This tool is the exact same as the [Draft LayerManager](Draft_LayerManager.md) tool, and creates the same layer object. There is only one difference: It has support for [NativeIFC](NativeIFC.md) objects:

-   An IFC icon will indicate if a layer is part of an IFC project or not
-   An **Assign IFC** button allows to move a layer to an IFC project and with that turn it into an IFC layer




 {{BIM_Tools_navi}}



---
⏵ [documentation index](../README.md) > [BIM](BIM_Workbench.md) > BIM Layers
