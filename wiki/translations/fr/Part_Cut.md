---
- GuiCommand:
   Name:Part_Cut
   Name/fr:Part Soustraction
   MenuLocation:Part → Opération booléenne → Soustraction
   Workbenches:[Part](Part_Workbench/fr.md)
   SeeAlso:[Part Opération booléenne](Part_Boolean/fr.md), [Part Union](Part_Fuse/fr.md), [Part Intersection](Part_Common/fr.md), 
---

# Part Cut/fr

## Description

Coupe (soustrait) un objet à un autre, le dernier sélectionné étant soustrait au premier. Cette opération est totalement paramétrique : les composants peuvent être modifiés et le résultat recalculé.

**Remarque :** cette commande est une forme automatisée de l\'<img alt="" src=images/Part_Boolean.svg  style="width:24px;"> [Part Opération booléenne](Part_Boolean/fr.md).

[480px\|left\|Cut](IMAGE:Part_Cut_01.png.md)



## Utilisation

1.  Sélectionnez deux formes
2.  Lancez la commande Part Soustraction de plusieurs manières :
    -   Appuyez sur le bouton **![](images/) '''Soustraction'''** dans la barre d\'outils Part
    -   Utilisez l\'entrée **Part → Opération booléenne → Soustraction** depuis le menu Part



## Entrées prises en charge 

Les objets utilisés doivent être des formes d\'[OpenCASCADE](OpenCASCADE/fr.md). Par exemple, les objets créés à l\'aide des ateliers Part, PartDesign ou Sketcher. Pour les maillages, il existe des outils booléens dédiés dans l\'[atelier MeshDesign](Mesh_Workbench/fr.md).



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Cut/fr
