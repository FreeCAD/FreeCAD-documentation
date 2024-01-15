---
 GuiCommand:
   Name: TechDraw AxoHorizontalDimension
   Name/fr: TechDraw Cote axonométrique
   MenuLocation: TechDraw , Annotations , Cote axonométrique
   Workbenches: TechDraw_Workbench/fr
   Version: 0.21
---

# TechDraw AxoLengthDimension/fr

## Description

L\'outil **TechDraw Cote axonométrique** ajoute une cote à une vue axonométrique. La cote peut être la longueur d\'une arête ou la distance entre deux points.

<img alt="" src=images/TechDraw_AxoLengthDimensionExample.png  style="width:300px;"> 
*Cotes axonométriques basées sur un bord (bleu) et deux points (rouge)*



## Utilisation

1.  Faites l\'une des choses suivantes :
    -   Sélectionnez deux arêtes (e1 et e2 dans l\'image). La première arête définit la direction de la ligne de la cote et la distance mesurée. La deuxième arête définit la direction des lignes d\'extension.
    -   Sélectionnez deux arêtes (e3 et e4 dans l\'image) et deux points (v1 et v2 dans l\'image). La première arête définit la direction de la ligne de la cote. La deuxième arête définit la direction des lignes d\'extension. Les points déterminent la distance mesurée.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/TechDraw_AxoLengthDimension.svg" width=16px> [Cote axonométrique](TechDraw_AxoLengthDimension/fr.md)**.
    -   Sélectionnez l\'option **TechDraw → Dimensions → <img src="images/TechDraw_AxoLengthDimension.svg" width=16px> Cote axonométrique** du menu.
3.  Une cote axonométrique est ajoutée à la vue.
4.  La cote peut être déplacée jusqu\'à la position souhaitée.
5.  Si nécessaire, ajoutez des tolérances comme décrit sur [cette page](TechDraw_Geometric_dimensioning_and_tolerancing/fr#Tolérances.md).



### Affichage des mesures 3D 

Voir [TechDraw Cote de longueur](TechDraw_LengthDimension/fr#Affichage_des_mesures_3D.md).


{{VersionPlus/fr|0.22}}

: Lors de la cotation des arêtes parallèles aux axes du système de coordonnées global, la valeur réelle (3D) est automatiquement calculée et insérée dans l\'étiquette de dimension sous forme de texte.



### Changer les propriétés 

Pour modifier les propriétés d\'un objet dimension, double-cliquez dessus dans le dessin ou dans la [vue en arborescence](Tree_view/fr.md). Cela ouvrira la [boîte de dialogue Dimension](TechDraw_LengthDimension/fr#Bo.C3.AEte_de_dialogue_Dimension.md).





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw AxoLengthDimension/fr
