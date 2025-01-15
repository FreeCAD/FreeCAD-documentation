---
 GuiCommand:
   Name: BIM Layers
   Name/de: BIM Ebenen
   MenuLocation: Manage , Manage layers...
   Workbenches: BIM_Workbench/de
---

# BIM Layers/de



## Beschreibung

Der **Layers Manager** ermöglicht [Ebenen](Draft_Layer/de.md) (layer) zu verwalten. Ebenen sind eine spezielle Art von Gruppe (wie früher Transparentfolien, die zu einer Gesamtzeichnung übereinander gelegt wurden), die die visuellen Eigenschaften der auf ihnen platzierten Objekte steuern. Werden die Eigenschaften der Ebenen geändert, wie z. B. Linienbreite, Linienfarbe, Formfarbe und Transparenz, werden die Änderungen auf ihre untergeordneten Objekte übertragen. Ebenen greifen nicht in andere FreeCAD-Strukturen wie [Gruppen](Std_Group/de.md) oder [Gebäudeteile](Arch_BuildingPart/de.md) ein, so dass jedes Objekt gleichzeitig Teil einer Ebene und Teil einer Gruppe sein kann.

<img alt="" src=images/BIM_layers_screenshot.png  style="width:600px;"> 
*Layers-Manager*

Ebenen werden von/nach [IFC](Arch_IFC/de.md) und [DXF/DWG](Draft_DXF/de.md) importiert und exportiert.

Der Ebenenverwalter ermöglicht die Ebenen zu verwalten, Ebenen hinzuzufügen, zu entfernen oder ihre visuellen Eigenschaften zu ändern. Um Objekte zu einer Ebene hinzuzufügen, werden sie einfach auf die Ebene in der [Baumansicht](Tree_view.md) gezogen. Um sie zu entfernen, werden sie aus der Ebene herausgezogen und auf dem Dokumentstamm abgelegt.

## NativeIFC

This tool is the exact same as the [Draft LayerManager](Draft_LayerManager.md) tool, and creates the same layer object. There is only one difference: It has support for [NativeIFC](NativeIFC.md) objects:

-   An IFC icon will indicate if a layer is part of an IFC project or not
-   An **Assign IFC** button allows to move a layer to an IFC project and with that turn it into an IFC layer



---
⏵ [documentation index](../README.md) > [BIM](BIM_Workbench.md) > BIM Layers/de
