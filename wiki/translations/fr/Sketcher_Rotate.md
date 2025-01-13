---
 GuiCommand:
   Name: Sketcher Rotate
   Name/fr: Sketcher Pivoter/dupliquer
   MenuLocation: Esquisse , Outils d'esquisse , Pivoter/dupliquer
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **Z** **P**
   Version: 1.0
   SeeAlso: 
---

# Sketcher Rotate/fr

## Description

L\'outil <img alt="" src=images/Sketcher_Rotate.svg  style="width:24px;"> [Sketcher Pivoter/dupliquer](Sketcher_Rotate/fr.md) fait pivoter ou permet de créer des copies pivotées des éléments sélectionnés. Les copies sont réparties uniformément le long de l\'angle de rotation.



## Utilisation

Voir aussi : [Aides au dessin](Sketcher_Workbench/fr#Aides_au_dessin.md).

Pos-OVP = [Paramètres d\'affichage](Sketcher_Preferences/fr#Général.md) de position. {{Version/fr|1.0}}
Dim-OVP = Paramètres d\'affichage des dimensions. {{Version/fr|1.0}}

1.  Sélectionnez une ou plusieurs arêtes et/ou [objets Point](Sketcher_CreatePoint.md). Les contraintes, à l\'exception des contraintes [horizontales](Sketcher_ConstrainHorizontal/fr.md) et [verticales](Sketcher_ConstrainVertical/fr.md), limitées aux éléments sélectionnés sont également traitées. Si les éléments originaux sont tournés, toutes les autres contraintes qui leur sont associées seront supprimées.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le **<img src="images/Sketcher_Rotate.svg" width=16px> [Pivoter/dupliquer](Sketcher_Rotate/fr.md)**.
    -   Sélectionnez l\'option **Sketcher → Outils Sketcher → <img src="images/Sketcher_Rotate.svg" width=16px> Pivoter/dupliquer** du menu.
    -   Cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **<img src="images/Sketcher_Rotate.svg" width=16px> Pivoter/dupliquer** du menu contextuel.
    -   Raccourci clavier : **Z** puis **P**.
3.  Le curseur se transforme en croix avec l\'icône de l\'outil.
4.  La section **Paramètres de rotation** est ajoutée en haut de la [fenêtre de dialogue de l\'esquisse](Sketcher_Dialog/fr.md).
5.  Vous pouvez modifier le nombre de **copies** (si le nombre est égal à zéro, les éléments d\'origine sont pivotés) :
    -   Entrez un nombre.
    -   Appuyez sur la touche **U** pour augmenter le nombre.
    -   Appuyez sur la touche **J** pour diminuer le nombre.
6.  Vous pouvez cocher la case **Appliquer des contraintes d\'égalité** pour exclure les contraintes dimensionnelles de l\'opération, et appliquer à la place des <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:16px;"> [contraintes d\'égalité](Sketcher_ConstrainEqual/fr.md) entre les objets originaux et leurs copies.
7.  Choisissez le centre de rotation, ou avec Pos-OVP : entrez ses coordonnées X et/ou Y.
8.  Choisissez un point pour définir l\'angle de départ, ou avec Dim-OVP : saisissez-le.
9.  Choisissez un point pour définir l\'angle de rotation, ou avec Dim-OVP : saisissez-le.
10. Les éléments originaux sont pivotés ou des copies pivotées sont créées. Aucune contrainte basée sur Pos-OVP ou Dim-OVP n\'est ajoutée.



## Remarques

-   Il peut être conseillé d\'utiliser [Sketcher Supprimer l\'alignement des axes](Sketcher_RemoveAxesAlignment/fr.md) avant d\'utiliser cet outil.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Rotate/fr
