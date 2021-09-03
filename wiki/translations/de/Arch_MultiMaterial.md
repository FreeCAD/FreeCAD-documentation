---
- GuiCommand:/de
   Name:Arch MultiMaterial
   Name/de:Arch MehrfachMaterial
   Workbenches:[Arch](Arch_Workbench/de.md), [BIM](BIM_Workbench/de.md)
   MenuLocation:Arch → Material Werkzeuge → Mehrfach-Material
   SeeAlso:[Arch SetMaterial](Arch_SetMaterial/de.md), [Arch CompSetMaterial](Arch_CompSetMaterial/de.md)
---

## Beschreibung

Das Multi-Material Werkzeug definiert eine Liste von [Materialien](Material/de.md) mit, für jedes Material, einen Namen und einem Dickenwert. Diese Multimaterialliste kann dann zu einem [Bogen](Arch_Workbench/de.md) Objekt anstelle eines einzelnen [Arch Material](Arch_SetMaterial/de.md) hinzugefügt werden.

![](images/Arch_multimaterial_example.png )

Nicht alle Arch Objekte können derzeit Multimaterialien verwenden, und die Verwendung von Multimaterialien ist unterschiedlich. Derzeit:

-   <img alt="" src=images/Arch_Wall.svg  style="width:24px;"> [Walls](Arch_Wall.md) with a MultiMaterial will use the material definitions and thicknesses to create a multi-layer wall
-   <img alt="" src=images/Arch_Window.svg  style="width:24px;"> [Windows](Arch_Window.md) with a MultiMaterial will attribute materials with a given name defined inside the MultiMaterial to window components with a same name or type (see below). Material thickness is not considered.
-   <img alt="" src=images/Arch_Panel.svg  style="width:24px;"> [Panels](Arch_Panel.md) with a MultiMaterial will use the material definitions and thicknesses to create a multi-layer panel

## Anwendung

1.  Create first a series of **<img src="images/Arch_SetMaterial.svg" width=16px> [Arch Materials](Arch_SetMaterial.md)** that you will need in your Multi-Material.
2.  Optionally, select an Arch object you wish to attribute the new Multi-Material to.
3.  Press the **<img src="images/Arch_MultiMaterial.svg" width=16px> [Multi-Material](Arch_MultiMaterial.md)** button.
4.  Set the desired material layers.

## Optionen

![](images/Arch_multimaterial_panel.png )

Während der Erstellung oder Änderung eines MehrfachMaterials durch doppelklicken im Baum sind die folgenden Optionen verfügbar:

-   **Duplicate** another existing Multi-Material from the same document. This only copies the values over, and doesn\'t link the two multi-materials in any way.
-   The **Name** field will also set the material object\'s Label
-   The **Composition** list is the list of the different material layers that compose this multi-material. Each layer has a name, a material and a thickness value.
-   Click **Add** to add a new layer, **Up** to move a selected layer up, **Down** to move a selected layer down, or **Del** to delete a selected layer.
-   Double-click the **name** of a layer to edit it, the material will offer you a drop-down list of available [Arch Materials](Arch_SetMaterial.md) in the same document, and thickness can be set to any value in any unit
-   Name and Material fields are mandatory. Thickness can be left blank (it will then adopt a value of 0).
-   When a multi-material contains layers with a thickness of zero, that thickness is considered variable. Arch objects that use the multi-material, such as Walls and Panels, will treat that accordingly, and give that layer the remaining space available given their own width or thickness.
-   If you name the different components of a multi-material \"Frame\", \"Solid panel\", \"Glass panel\" or \"Louvre\", and apply that material to a window, the given materials will be applied to the corresponding window components.

## Bezug zu IFC {#bezug_zu_ifc}

Dies entspricht in etwa einer Kombination aus [IfcMaterialLayerSet](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/link/ifcmateriallayerset.htm) und [IfcMaterialLayer](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/link/ifcmateriallayer.htm).

## Begrenzungen

## Skripten





 
