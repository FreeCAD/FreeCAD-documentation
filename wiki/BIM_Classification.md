---
 GuiCommand:
   Name: BIM Classification
   MenuLocation: Manage , Manage classification...
   Workbenches: BIM_Workbench
---

# BIM Classification

## Description

The **Classification manager** allows you to attribute a standard class to a BIM object or material. Several classification systems are available in XML or IFC form (both are supported by this tool) from <https://github.com/Moult/IfcClassification>, or directly from their publishers, or from <https://www.graphisoft.com/downloads/archicad/BIM_Data.html>. To make these XML or IFC files known to FreeCAD they must be placed in a BIM subfolder of your FreeCAD user folder. The exact location for your system is informed on the BIM classification dialog. If both an IFC and XML file are available, the BIM Classification tool will prefer the IFC one.

 <img alt="" src=images/BIM_classification_screenshot.png  style="width:600px;">  
*Classification manager*

## Usage

-   Install one or more classification standard XML or IFC files as explained above
-   If you wish to add or edit a class for an object, select that object and press the BIM Classification button
-   If you wish to add or edit a class for a material, don\'t select anything and press the BIM Classification button. You will be able to browse the materials directly from the classification manager window



---
⏵ [documentation index](../README.md) > [BIM](BIM_Workbench.md) > BIM Classification
