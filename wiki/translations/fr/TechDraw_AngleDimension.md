---
 GuiCommand:
   Name: TechDraw AngleDimension
   Name/fr: TechDraw Cote angulaire
   MenuLocation: TechDraw , Dimensions , Insérer une cote angulaire
   Workbenches: TechDraw_Workbench/fr
   SeeAlso: TechDraw_3PtAngleDimension/fr
---

# TechDraw AngleDimension/fr

## Description

L\'outil **TechDraw Cote angulaire** ajoute une cote angulaire à une vue. Cette cote indique l\'angle intérieur entre deux arêtes droites.

<img alt="" src=images/TechDraw_Dimension_Angle_example.png  style="width:200px;"> 
*Mesure d'angle entre deux arêtes*



## Comment faire 

1.  Sélectionnez deux arêtes droites. La géométrie peut être sélectionnée dans la [vue 3D](3D_view/fr.md) ou dans le dessin.
2.  Si vous avez sélectionné la géométrie dans la vue 3D : ajoutez la bonne vue TechDraw à la sélection en la sélectionnant dans la [vue en arborescence](Tree_view/fr.md).
3.  Il y a plusieurs façons de lancer l\'outil :
    -   
        {{Version/fr|1.0}}
        
        : si la [préférence](TechDraw_Preferences/fr#Cotes.md) **outils de cotation** est réglée sur {{Value|Outil unique}} (par défaut) : appuyez sur la flèche vers le bas à droite du bouton **<img src="images/TechDraw_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** et sélectionnez l\'option **<img src="images/TechDraw_AngleDimension.svg" width=16px> Insérer une cote angulaire** du menu déroulant.

    -   Si cette préférence a une valeur différente (et dans {{VersionMinus/fr|0.21}}) : appuyez sur le bouton **<img src="images/TechDraw_AngleDimension.svg" width=16px> [Insérer une cote angulaire](TechDraw_AngleDimension/fr.md)**.

    -   Sélectionnez l\'option **TechDraw → Dimensions → <img src="images/TechDraw_AngleDimension.svg" width=16px> Insérer une cote angulaire** du menu.
4.  Une cote est ajoutée à la vue.
5.  La cote peut être déplacée jusqu\'à la position souhaitée.
6.  Si nécessaire, ajoutez des tolérances comme décrit sur [cette page](TechDraw_Geometric_dimensioning_and_tolerancing/fr#Tolérances.md).



### Affichage des mesures 3D 

Voir [TechDraw Cote de longueur](TechDraw_LengthDimension/fr#Affichage_des_mesures_3D.md).



### Changer les propriétés 

Pour modifier les propriétés d\'un objet dimension, double-cliquez dessus dans le dessin ou dans la [vue en arborescence](Tree_view/fr.md). Cela ouvrira la [boîte de dialogue Dimension](TechDraw_LengthDimension/fr#Bo.C3.AEte_de_dialogue_Dimension.md).

## Limitations

Les objets Cote sont vulnérables au \"[problème de nommage topologique](Topological_naming_problem/fr.md)\". Voir [TechDraw Cote de longueur](TechDraw_LengthDimension/fr.md).



## Remarques

Voir [TechDraw Cote de longueur](TechDraw_LengthDimension/fr#Remarques/fr.md).



## Propriétés

Voir [Cote de longueur](TechDraw_LengthDimension/fr#Propri.C3.A9t.C3.A9s/fr.md).





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw AngleDimension/fr
