---
 GuiCommand:
   Name: Arch ToggleIfcBrepFlag
   Name/fr: Arch Basculer en B-rep IFC
   MenuLocation: Utilitaires , Activer/désactiver l'indicateur B-rep de l'IFC
   Workbenches: BIM_Workbench/fr
   SeeAlso: Arch_IfcExplorer/fr, Arch_IFC/fr
---

# Arch ToggleIfcBrepFlag/fr

## Description

L\'outil **Arch Basculer en B-rep IFC** active/désactive l\'indicateur IfcBrep d\'un objet sélectionné [BIM](BIM_Workbench/fr.md) (la valeur par défaut est toujours désactivée). Si l\'indicateur est activé lors de l\'exportation de l\'objet au format IFC, l\'objet sera exporté sous forme de [IfcFacetedBrep](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcgeometricmodelresource/lexical/ifcfacetedbrep.htm), même si une exportation de niveau supérieur telle que IfcExtrudedAreaSolid ou IfcBooleanResult est possible. Bien que les objets IfcFacetedBrep sont plus lourds et moins modifiables (ils perdent des informations de géométrie tels que l\'historique de la modélisation), ils sont souvent sujets à moins d\'erreurs. Dans certains cas la définition de cet indicateur permet de résoudre les problèmes d\'objets qui ne sont pas exportés correctement lorsque cet indicateur n\'est pas défini.



## Utilisation

1.  Selectionnez un objet Arch.
2.  Sélectionnez l\'option **Utilitaires → <img src="images/Arch_ToggleIfcBrepFlag.svg" width=16px> Activer/désactiver l'indicateur B-rep de l'IFC** du menu.





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch ToggleIfcBrepFlag/fr
