---
- GuiCommand:/ru
   Name:Arch MultiMaterial   Name/ru:Arch MultiMaterial
   MenuLocation:Архитектура → Multi-Material
   Workbenches:[Arch](Arch_Workbench/ru.md)
---

# Arch MultiMaterial/ru


</div>

## Описание

The Multi-Material tool defines a list of [materials](Material.md) with, for each material, a name and a thickness value. This multi-materials list can then be added to an [Arch](Arch_Workbench.md) object instead of a single [Arch Material](Arch_SetMaterial.md) .

![](images/Arch_multimaterial_example.png )

Not all Arch objects can currently make use of multi-materials, and the use they do of it differs. Currently:

-   <img alt="" src=images/Arch_Wall.svg  style="width:24px;"> [Walls](Arch_Wall.md) with a MultiMaterial will use the material definitions and thicknesses to create a multi-layer wall
-   <img alt="" src=images/Arch_Window.svg  style="width:24px;"> [Windows](Arch_Window.md) with a MultiMaterial will attribute materials with a given name defined inside the MultiMaterial to window components with a same name or type (see below). Material thickness is not considered.
-   <img alt="" src=images/Arch_Panel.svg  style="width:24px;"> [Panels](Arch_Panel.md) with a MultiMaterial will use the material definitions and thicknesses to create a multi-layer panel

## Использование

1.  Create first a series of **<img src="images/Arch_SetMaterial.svg" width=16px> [Arch Materials](Arch_SetMaterial.md)** that you will need in your Multi-Material.
2.  Optionally, select an Arch object you wish to attribute the new Multi-Material to.
3.  Press the **<img src="images/Arch_MultiMaterial.svg" width=16px> [Multi-Material](Arch_MultiMaterial.md)** button.
4.  Set the desired material layers.

## Опции

![](images/Arch_multimaterial_panel.png )

Upon creating or editing a multi-material by double-clicking it in the tree, the following options are available:

-   **Duplicate** another existing Multi-Material from the same document. This only copies the values over, and doesn\'t link the two multi-materials in any way.
-   The **Name** field will also set the material object\'s Label
-   The **Composition** list is the list of the different material layers that compose this multi-material. Each layer has a name, a material and a thickness value.
-   Click **Add** to add a new layer, **Up** to move a selected layer up, **Down** to move a selected layer down, or **Del** to delete a selected layer.
-   Double-click the **name** of a layer to edit it, the material will offer you a drop-down list of available [Arch Materials](Arch_SetMaterial.md) in the same document, and thickness can be set to any value in any unit
-   Name and Material fields are mandatory. Thickness can be left blank (it will then adopt a value of 0).
-   When a multi-material contains layers with a thickness of zero, that thickness is considered variable. Arch objects that use the multi-material, such as Walls and Panels, will treat that accordingly, and give that layer the remaining space available given their own width or thickness.
-   If you name the different components of a multi-material \"Frame\", \"Solid panel\", \"Glass panel\" or \"Louvre\", and apply that material to a window, the given materials will be applied to the corresponding window components.

## Relation to IFC 

This roughly corresponds to a combination of [IfcMaterialLayerSet](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/link/ifcmateriallayerset.htm) and [IfcMaterialLayer](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/link/ifcmateriallayer.htm).

## Limitations

## Scripting


<div class="mw-translate-fuzzy">


{{docnav/ru|[Material](Arch_SetMaterial.md)|[Schedule](Arch_Schedule.md)|[Arch](Arch_Workbench.md)|IconL=Arch_SetMaterial.png |IconC=Workbench_Arch.svg |IconR=Arch_Schedule.svg}}


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch MultiMaterial/ru
