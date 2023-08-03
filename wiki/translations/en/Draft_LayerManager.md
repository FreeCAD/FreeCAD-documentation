---
 GuiCommand:
   Name: Draft LayerManager
   MenuLocation: Utilities , Manage layers...
   Workbenches: Draft_Workbench, Arch_Workbench
   Version: 0.21
   SeeAlso: BIM_Workbench, Draft_Layer
---

# Draft LayerManager/en

## Description

The layers manager allows you to manage [layers](Draft_Layer.md). Layers are a special kind of group that controls the visual properties of objects placed inside of it. By changing the properties of the Layer, such as line width, line color, shape color and transparency, the changes are propagated to its child objects. Layers don\'t interfere with any other FreeCAD structure such as [groups](Std_Group.md) or [Building parts](Arch_BuildingPart.md), so any object can be at the same time part of a layer and part of a group. Layers are always automatically kept in a special \"Layers\" group.

<img alt="" src=images/BIM_layers_screenshot.png  style="width:800px;">

Layers are imported and exported from/to [IFC](Arch_IFC.md) and [DXF/DWG](Draft_DXF.md).

The layers manager allows you to manage your layers, add or remove layers, or change their visual properties. To add objects to a layer, simply drag them into the layer in the tree view. To remove them, drag them from the layer and drop them into the document root.

## Usage

TBD



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft LayerManager/en
