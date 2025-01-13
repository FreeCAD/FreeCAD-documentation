---
 GuiCommand:
   Name: Part XOR
   Name/fr: Part OU exclusif
   MenuLocation: Part , Scinder , OU exclusif
   Workbenches: Part_Workbench/fr
   Version: 0.17
   SeeAlso: Part_BooleanFragments/fr, Part_Slice/fr, Part_CompJoinFeatures/fr, Part_Boolean/fr
---

# Part XOR/fr

## Description

La commande <img alt="" src=images/Part_XOR.svg  style="width:24px;"> **Part XOR** supprime la géométrie partagée par un nombre pair d\'objets et laisse un espace vide entre les objets concernés. Pour deux objets, elle représente une version symétrique de [Part Soustraction](Part_Cut/fr.md).

<img alt="" src=images/Part_XOR-01.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Part_XOR-02.png  style="width:300px;"> 
*Trois objets se chevauchant → Objet résultant*



## Utilisation

1.  Sélectionnez deux objets ou plus. Il est également possible de sélectionner un [Part Composé](Part_Compound/fr.md) contenant deux objets ou plus.
2.  Il existe plusieurs façons de lancer la commande :
    -   Sélectionnez l\'option **Part → Scinder → <img src="images/Part_XOR.svg" width=16px> OU exclusif** du menu.
    -   Appuyez sur le bouton **<img src="images/Part_XOR.svg" width=16px> [OU exclusif](Part_XOR/fr.md)**.



## Remarques

-   Les espaces vides sont difficiles à détecter si les objets sélectionnés n\'ont pas de faces coplanaires. Pour vérifier le résultat du OU exclusif, on peut alors utiliser [Std Couper selon des plans](Std_ToggleClipPlane/fr.md).



## Propriétés



## Script





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part XOR/fr
