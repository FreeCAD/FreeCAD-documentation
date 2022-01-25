---
- GuiCommand:/fr
   Name:Part_Cut
   Name/fr:Part Soustraction
   MenuLocation:Pièce → Opération booléenne → Soustraction
   Workbenches:[Part](Part_Workbench/fr.md)
   SeeAlso:[Part Opération booléenne](Part_Boolean/fr.md), [Part Union](Part_Fuse/fr.md), [Part Intersection](Part_Common/fr.md), 
---

# Part Cut/fr

## Description

Coupe (soustrait) un objet à un autre, le dernier sélectionné étant soustrait au premier. Cette opération est totalement paramétrique : les composants peuvent être modifiés et le résultat recalculé.

**Remarque :** Cette commande est une forme automatisée de <img alt="" src=images/Part_Boolean.svg  style="width:24px;"> [Part Opération booléenne](Part_Boolean/fr.md).

[480px\|left\|Cut](IMAGE:Part_Cut_01.png.md)

## Utilisation

1.  Sélectionnez deux formes
2.  Lancez la commande Part Soustraction de plusieurs manières :
    -   Appuyez sur le bouton **![](images/) '''Executer une soustraction sur deux formes'''** dans la barre d\'outils Part
    -   Utilisez l\'entrée **Pièce → Opération booléenne → Soustraction** depuis le menu Part

## Entrées supportées 

Les objets utilisés doivent être des formes [OpenCASCADE](OpenCASCADE/fr.md). Exemples : les trucs faits avec un des ateliers Part, PartDesign, Sketcher. Pas de maillages (sauf s\'ils ont été convertis en formes) - pour les maillages, il existe des outils booléens spécifiques dans l\'atelier MeshDesign.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Cut/fr
