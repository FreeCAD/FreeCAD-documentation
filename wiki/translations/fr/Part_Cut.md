---
 GuiCommand:
   Name: Part_Cut
   Name/fr: Part Soustraction
   MenuLocation: Part , Opération booléenne , Soustraction
   Workbenches: Part_Workbench/fr
   SeeAlso: Part_Boolean/fr, Part_Fuse/fr, Part_Common/fr, 
---

# Part Cut/fr

## Description

L\'outil <img alt="" src=images/Part_Cut.svg  style="width:24px;"> **Part Soustraction** soustrait un objet Part à un autre, le dernier sélectionné est soustrait au premier. Cette opération est totalement paramétrique : les composants peuvent être modifiés et le résultat recalculé.

L\'outil est une forme automatisée de <img alt="" src=images/Part_Boolean.svg  style="width:24px;"> [Part Opération booléenne](Part_Boolean/fr.md).

<img alt="" src=images/Part_Cut_01.png  style="width:480px;">



## Utilisation

1.  Sélectionnez deux formes.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Part_Cut.svg" width=16px> [Soustraction](Part_Cut/fr.md)**.
    -   Utilisez l\'option **Part → Opération booléenne → <img src="images/Part_Cut.svg" width=16px> Soustraction** du menu.



## Objets pris en charge 

Les objets utilisés doivent être des formes d\'[OpenCASCADE](OpenCASCADE/fr.md). Par exemple, les objets créés à l\'aide des ateliers Part, PartDesign ou Sketcher. Pour les maillages, il existe des outils booléens dédiés à l\'[atelier Mesh](Mesh_Workbench/fr.md).





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Cut/fr
