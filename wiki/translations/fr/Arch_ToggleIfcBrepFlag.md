---
- GuiCommand:/fr
   Name:Arch ToggleIfcBrepFlag
   Name/fr:Arch Bascule marqueur Brep IFC
   MenuLocation:Arch → Utilitaires → Activer/désactiver le marqueur Brep IFC
   Workbenches:[Arch](Arch_Workbench/fr.md)
   SeeAlso:[Arch Explorateur IFC](Arch_IfcExplorer/fr.md), [Arch IFC](Arch_IFC/fr.md)
---

# Arch ToggleIfcBrepFlag/fr

## Description

Cet outil active/désactive l\'indicateur IfcBrep d\'un objet [Arch](Arch_Workbench/fr.md) sélectionné (la valeur par défaut est toujours off). Si l\'indicateur est activé lors de l\'exportation de l\'objet au format IFC, l\'objet sera exporté sous forme de [IfcFacetedBrep](http://www.buildingsmart-tech.org/ifc/IFC4/final/html/schema/ifcgeometricmodelresource/lexical/ifcfacetedbrep.htm), même si une exportation de niveau supérieur telle que IfcExtrudedAreaSolid ou IfcBooleanResult est possible. Bien que les objets IfcFacetedBrep sont plus lourds et moins modifiables (ils perdent des informations de géométrie tels que l\'historique de la modélisation), ils sont souvent sujets à moins d\'erreurs. Dans certains cas la définition de cet indicateur permet de résoudre les problèmes d\'objets qui ne sont pas exportés correctement lorsque cet indicateur n\'est pas défini.

## Utilisation

1.  Selectionnez un objet Arch
2.  Sélectionnez le bouton **<img src="images/Arch_ToggleIfcBrepFlag.svg" width=16px>** ou **Arch** → **Utilitaires** → **<img src="images/Arch_ToggleIfcBrepFlag.svg" width=16px> [Activer/désactiver le marqueur Brep IFC](Arch_ToggleIfcBrepFlag/fr.md)** dans le menu supérieur.

---
[documentation index](../README.md) > [Arch](Category_Arch.md) > [Arch](Arch_Workbench.md) > Arch ToggleIfcBrepFlag/fr
