---
- GuiCommand:/de
   Name:Arch MultiMaterial
   Name/de:Arch MehrfachMaterial
   MenuLocation:Arch → Material Werkzeuge → Mehrfach-Material
   Workbenches:[Arch](Arch_Workbench/de.md), [BIM](BIM_Workbench/de.md)
   Version:0.17
   SeeAlso:[Arch SetMaterial](Arch_SetMaterial/de.md), [Arch CompSetMaterial](Arch_CompSetMaterial/de.md)
---

# Arch MultiMaterial/de



## Beschreibung

Das Multi-Material-Werkzeug definiert eine Liste von [Materialien](Material.md) mit einem Namen und einem Dickenwert für jedes Material. Diese Multimaterialliste kann dann zu einem [Arch](Arch_Workbench/de.md)-Objekt anstelle eines einzelnen [Arch-Materials](Arch_SetMaterial/de.md) hinzugefügt werden.

![](images/Arch_multimaterial_example.png )

Nicht alle Arch-Objekte können derzeit Multimaterialien verwenden, und die Verwendung von Multimaterialien ist unterschiedlich. Derzeit:

-   <img alt="" src=images/Arch_Wall.svg  style="width:24px;"> [Wände](Arch_Wall/de.md) mit einem Mehrfachmaterial werden die Materialdefinitionen und -dicken verwenden, um eine mehrlagige Wand zu erstellen
-   Bei <img alt="" src=images/Arch_Window.svg  style="width:24px;"> [Fenstern](Arch_Window/de.md) mit einem Mehrfachmaterial werden die Materialien mit einem Namen innerhalb dieses Mehrfachmaterials, der zu Fensterkomponenten mit gleichem Namen oder Typ (s.u.) passt, diesen Komponenten zugeordnet. Materialdicken werden nicht berücksichtigt.
-   <img alt="" src=images/Arch_Panel.svg  style="width:24px;"> [Paneele](Arch_Panel/de.md) mit einem Mehrfachmaterial werden die Materialdefinitionen und -dicken verwenden, um ein mehrlagiges Paneel zu erstellen



## Anwendung

1.  Erstelle zuerst eine Reihe von **<img src="images/Arch_SetMaterial.svg" width=16px> [Arch Material](Arch_SetMaterial/de.md)**ien, die du in deinem Mehrfachmaterial benötigst.
2.  Optional wähle ein Arch-Objekt, dem du das neue Mehrfachmaterial zuordnen möchtest.
3.  Drücke die **<img src="images/Arch_MultiMaterial.svg" width=16px> [Mehrfachmaterial](Arch_MultiMaterial/de.md)**-Schaltfläche.
4.  Setze die gewünschten Materialebenen.



## Optionen

![](images/Arch_multimaterial_panel.png )

Während der Erstellung oder Änderung eines Mehrfachmaterials durch Doppelklicken im Baum sind die folgenden Optionen verfügbar:

-   **Duplicate** another existing Multi-Material from the same document. This only copies the values over, and doesn\'t link the two multi-materials in any way.
-   The **Name** field will also set the material object\'s Label
-   The **Composition** list is the list of the different material layers that compose this multi-material. Each layer has a name, a material and a thickness value.
-   Click **Add** to add a new layer, **Up** to move a selected layer up, **Down** to move a selected layer down, or **Del** to delete a selected layer.
-   Double-click the **name** of a layer to edit it, the material will offer you a drop-down list of available [Arch Materials](Arch_SetMaterial.md) in the same document, and thickness can be set to any value in any unit
-   Name and Material fields are mandatory. Thickness can be left blank (it will then adopt a value of 0).
-   When a multi-material contains layers with a thickness of zero, that thickness is considered variable. Arch objects that use the multi-material, such as Walls and Panels, will treat that accordingly, and give that layer the remaining space available given their own width or thickness.
-   If you name the different components of a multi-material \"Frame\", \"Solid panel\", \"Glass panel\" or \"Louvre\", and apply that material to a window, the given materials will be applied to the corresponding window components.



## Bezug zu IFC 

Dies entspricht in etwa einer Kombination aus [IfcMaterialLayerSet](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/link/ifcmateriallayerset.htm) und [IfcMaterialLayer](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/link/ifcmateriallayer.htm).



## Begrenzungen



## Skripten



---
![](images/Button_right.svg) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch MultiMaterial/de
