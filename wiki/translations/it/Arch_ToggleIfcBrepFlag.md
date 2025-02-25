---
 GuiCommand:
   Name: Arch ToggleIfcBrepFlag
   Name/it: Attiva/Disattiva flag Ifc Brep
   MenuLocation: Arch , Utilità , Attiva/Disattiva flag Ifc Brep
   Workbenches: Arch_Workbench/it
   SeeAlso: Arch_IfcExplorer/it, Arch_IFC/it
---

# Arch ToggleIfcBrepFlag/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Questo strumento attiva o disattiva il contrassegno Ifc BREP di un oggetto [Arch](Arch_Workbench/it.md) selezionato (di default è sempre disattivato). Se il contrassegno è attivo, quando esportato in IFC, l\'oggetto viene esportato come un oggetto [IfcFacetedBrep](http://www.buildingsmart-tech.org/ifc/IFC4/final/html/schema/ifcgeometricmodelresource/lexical/ifcfacetedbrep.htm), anche se è possibile un tipo di esportazione di livello superiore, come IfcExtrudedAreaSolid o IfcBooleanResult. Anche se di oggetti IfcFacetedBrep sono più pesanti e meno modificabili (perdono alcune informazioni sulla geometria, come la storia di modellazione), sono spesso meno soggetti ad errori. L\'impostazione di questo contrassegno permette di risolvere alcuni casi di oggetti che non vengono esportati correttamente quando il contrassegno non è impostato.


</div>



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare un oggetto Arch.
2.  Selezionare il pulsante **<img src="images/Arch_ToggleIfcBrepFlag.svg" width=16px>** o **Arch** → **Utilità** → **<img src="images/Arch_ToggleIfcBrepFlag.svg" width=16px> [Attiva/Disattiva flag Ifc Brep](Arch_ToggleIfcBrepFlag/it.md)** dal menu principale.


</div>


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch ToggleIfcBrepFlag/it
