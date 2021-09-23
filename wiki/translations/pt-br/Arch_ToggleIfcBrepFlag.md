---
- GuiCommand:
   Name:Arch ToggleIfcBrepFlag
   MenuLocation:Arch → Utilities → Toggle Ifc Brep flag
   Workbenches:[Arch](Arch_Workbench.md)
   SeeAlso:[Arch IfcExplorer](Arch_IfcExplorer.md), [Arch IFC](Arch_IFC.md)
---

# Arch ToggleIfcBrepFlag/pt-br

## Descrição

This tool turns the IfcBrep flag of a selected [Arch](Arch_Workbench.md) object on/off (the default is always off). If the flag in on, when exported to IFC, the object will be exported as an [IfcFacetedBrep](http://www.buildingsmart-tech.org/ifc/IFC4/final/html/schema/ifcgeometricmodelresource/lexical/ifcfacetedbrep.htm) object, even if a higher-level kind of export such as IfcExtrudedAreaSolid or IfcBooleanResult is possible. Although IfcFacetedBrep objects are heavier and less editable (they loose some geometry information such as the modeling history), they are often less error-prone. Setting this flag allows to solve some cases of objects that are not exported correctly when the flag is not set.

## Utilização

1.  Select an Arch object.
2.  Select the **<img src="images/Arch_ToggleIfcBrepFlag.svg" width=16px>** button, or **Arch** → **Utilities** → **<img src="images/Arch_ToggleIfcBrepFlag.svg" width=16px> [Toggle IfcBrepFlag](Arch_ToggleIfcBrepFlag.md)** from the top menu.


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch ToggleIfcBrepFlag/pt-br
