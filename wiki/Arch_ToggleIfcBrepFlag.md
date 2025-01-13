---
 GuiCommand:
   Name: Arch ToggleIfcBrepFlag
   MenuLocation: Utils , Toggle IFC B-rep flag
   Workbenches: BIM_Workbench
   SeeAlso: Arch_IfcExplorer, Arch_IFC
---

# Arch ToggleIfcBrepFlag

## Description

The **Arch ToggleIfcBrepFlag** tool turns the IfcBrep flag of a selected [BIM](BIM_Workbench.md) object on/off (the default is always off). If the flag in on, when exported to IFC, the object will be exported as an [IfcFacetedBrep](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcgeometricmodelresource/lexical/ifcfacetedbrep.htm) object, even if a higher-level kind of export such as IfcExtrudedAreaSolid or IfcBooleanResult is possible. Although IfcFacetedBrep objects are heavier and less editable (they loose some geometry information such as the modeling history), they are often less error-prone. Setting this flag allows to solve some cases of objects that are not exported correctly when the flag is not set.

## Usage

1.  Select an Arch object.
2.  Select the **Utils → <img src="images/Arch_ToggleIfcBrepFlag.svg" width=16px> Toggle IFC B-rep flag** option from the menu.




 {{BIM_Tools_navi}}



---
⏵ [documentation index](../README.md) > Arch ToggleIfcBrepFlag
