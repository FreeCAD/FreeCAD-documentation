---
 GuiCommand:
   Name: Sketcher Translate
   Name/fr: Sketcher Dupliquer en matrice
   MenuLocation: Esquisse , Outils d'esquisse , Déplacer/dupliquer en matrice
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **W**
   Version: 1.0
   SeeAlso: 
---

# Sketcher Translate/fr

## Description

L\'outil <img alt="" src=images/Sketcher_Translate.svg  style="width:24px;"> [Sketcher Déplacer/dupliquer](Sketcher_Translate/fr.md) déplace ou permet de créer des copies des éléments sélectionnés. Les copies sont réparties uniformément dans une ou deux directions.



## Utilisation

Voir aussi : [Aides au dessin](Sketcher_Workbench/fr#Aides_au_dessin.md).

Pos-OVP = [Paramètres d\'affichage](Sketcher_Preferences/fr#Général.md) de position. {{Version/fr|1.0}}
Dim-OVP = Paramètres d\'affichage des dimensions. {{Version/fr|1.0}}



### Déplacer une géometrie 

1.  Sélectionnez une ou plusieurs arêtes et/ou des [objets Point](Sketcher_CreatePoint/fr.md). Les contraintes limitées aux éléments sélectionnés sont également traitées. Toutes les autres contraintes associées aux éléments seront supprimées.
2.  Il existe plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Sketcher_Translate.svg" width=16px> [Déplacer/dupliquer en matrice](Sketcher_Translate/fr.md)**.
    -   Sélectionnez l\'option **Esquisse → Outils d'esquisse → <img src="images/Sketcher_Translate.svg" width=16px> Déplacer/dupliquer en matrice** du menu.
    -   Cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **<img src="images/Sketcher_Translate.svg" width=16px> Déplacer/dupliquer en matrice** du menu contextuel.
    -   Utilisez le raccourci clavier : **W**.
3.  Le curseur se transforme en croix avec l\'icône de l\'outil.
4.  La section **Paramètres de la matrice** est ajoutée en haut de la [fenêtre de dialogue de l\'esquisse](Sketcher_Dialog/fr.md).
5.  Choisissez le point de départ du vecteur de translation, ou avec Pos-OVP : entrez ses coordonnées X et/ou Y.
6.  Choisissez le point final du vecteur de translation, ou avec Dim-OVP : entrez la longueur et/ou l\'angle du vecteur. L\'angle est relatif à l\'axe X de l\'esquisse.
7.  Les éléments sont déplacés. Aucune contrainte basée sur Pos-OVP ou Dim-OVP n\'est ajoutée.



### Copier une géometrie 

1.  Sélectionnez une ou plusieurs arêtes et/ou des [objets Point](Sketcher_CreatePoint/fr.md). Les contraintes limitées aux éléments sélectionnés sont également traitées.
2.  Lancer l\'outil comme expliqué ci-dessus.
3.  Le curseur se transforme en croix avec l\'icône de l\'outil.
4.  La section **Paramètres de translation** est ajoutée en haut de la [fenêtre de dialogue de l\'esquisse](Sketcher_Dialog/fr.md).
5.  Vous pouvez modifier le nombre de **Copies** le long du premier vecteur :
    -   Entrez un nombre.
    -   Appuyez sur la touche **U** pour augmenter le nombre.
    -   Appuyez sur la touche **J** pour diminuer le nombre.
6.  Vous pouvez également modifier le nombre de **rangées** le long du deuxième vecteur :
    -   Entrez un nombre.
    -   Appuyez sur la touche **R** pour augmenter le nombre.
    -   Appuyez sur la touche **F** pour diminuer le nombre.
7.  Vous pouvez cocher la case **Appliquer des contraintes d\'égalité** pour exclure les contraintes dimensionnelles de l\'opération et appliquer à la place des <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:16px;"> [contraintes d\'égalité](Sketcher_ConstrainEqual.md) entre les objets originaux et leurs copies.
8.  Choisissez le point de départ du premier vecteur, ou avec Pos-OVP : entrez ses coordonnées X et/ou Y. Ce vecteur définit le décalage entre les copies. Ce vecteur définit le décalage entre les copies.
9.  Choisissez le point final du premier vecteur, ou avec Dim-OVP : entrez la longueur et/ou l\'angle du vecteur. L\'angle est relatif à l\'axe X de l\'esquisse.
10. S\'il y a deux lignes ou plus : choisissez le point final du second vecteur, ou avec Dim-OVP : entrez la longueur et/ou l\'angle du vecteur. L\'angle est relatif à l\'axe X de l\'esquisse. Ce vecteur définit le décalage entre les lignes.
11. Les éléments sont copiés. Aucune contrainte basée sur Pos-OVP ou Dim-OVP n\'est ajoutée.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Translate/fr
