# Arch ToggleIfcBrepFlag/es
---
- GuiCommand:   Name: Arch ToggleIfcBrepFlag   Workbenches: [[Arch_Workbench/es   Arch]]|MenuLocation: Arch - Utilities - Toggle Ifc Brep flag   Shortcut:    SeeAlso: ---


</div>

## Descripción


<div class="mw-translate-fuzzy">

Esta herramienta activa / desactiva el indicador IfcBrep de un objeto [ Arch](Arch_Workbench/es.md) (el valor predeterminado siempre está desactivado). Si el indicador está activado, cuando se exporta a IFC, el objeto se exportará como [IfcFacetedBrep](http://www.buildingsmart-tech.org/ifc/IFC4/final/html/schema/ifcgeometricmodelresource/lexical/ifcfacetedbrep.htm) objeto, incluso si es posible un tipo de exportación de nivel superior como IfcExtrudedAreaSolid o IfcBooleanResult. Aunque los objetos IfcFacetedBrep son más pesados ​​y menos editables (pierden cierta información de geometría, como el historial de modelado), a menudo son menos propensos a errores. La configuración de este indicador permite resolver algunos casos de objetos que no se exportan correctamente cuando el indicador no está establecido.


</div>


<div class="mw-translate-fuzzy">

## Utilización


</div>


<div class="mw-translate-fuzzy">

1.  Seleccione un objeto Arch
2.  Seleccione el menú Arch → Utilities → {{KEY | <img src="images/_Arch_ToggleIfcBrepFlag.png_" width= 16px> [ Toggle IfcBrepFlag](Arch_ToggleIfcBrepFlag_.md)}}


</div>



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch ToggleIfcBrepFlag/es
