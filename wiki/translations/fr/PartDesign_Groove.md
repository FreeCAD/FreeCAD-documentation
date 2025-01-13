---
 GuiCommand:
   Name: PartDesign_Groove
   Name/fr: PartDesign Rainure
   MenuLocation: PartDesign , Créer une fonction soustractive , Rainure
   Workbenches: PartDesign_Workbench/fr
   SeeAlso: PartDesign_Revolution/fr
---

# PartDesign Groove/fr

## Description

L\'outil **Rainure** fait pivoter une esquisse ou un profil sélectionné autour d\'un axe donné en découpant la matière du support.

![](images/PartDesign_Groove_example.svg )



*Ci-dessus : l'esquisse (A) tourne autour de l'axe (B).<br>La rainure résultante sur le solide (C) est illustrée à droite.*



## Utilisation

1.  Sélectionnez une seule esquisse ou une ou plusieurs faces du corps.
2.  Appuyez sur le bouton **<img src="images/PartDesign_Groove.svg" width=16px> [Rainure](PartDesign_Groove/fr.md)**.
3.  Définissez les paramètres de la rainure, voir [Options](#Options.md) ci-dessous.
4.  Appuyez sur le bouton **OK**.

## Options

Lors de la création d\'une rainure, ou après avoir double-cliqué sur une rainure existante dans la [vue en arborescence](Tree_view/fr.md), le panneau de tâches **Paramètres de la rainure** s\'affiche. Il propose les paramètres suivants :

![](images/partdesign_groove_parameters.png )

### Type


{{Version/fr|1.0}}

Type offre cinq façons différentes de spécifier l\'angle de la rainure :

#### Dimension

Entrez une valeur numérique pour l**\'angle** de la rainure. Avec l\'option **Symétrique au plan**, la rainure s\'étendra à la moitié de l\'angle donné de chaque côté de l\'esquisse ou de la face.



#### À travers tout 

La rainure sera prolongée jusqu\'à la dernière face du support qu\'elle rencontrera dans sa direction. Avec l\'option **Symétrique au plan**, la rainure traversera tout le matériau dans les deux directions.



#### La plus proche 

La rainure sera prolongée jusqu\'à la première face du support qu\'elle rencontrera dans sa direction.



#### Jusqu\'à une face 

La rainure sera prolongée jusqu\'à une face. Appuyez sur le bouton **Face** et sélectionnez une face ou un [plan de référence](PartDesign_Plane/fr.md) du corps.



#### Deux dimensions 

Cela permet d\'entrer un deuxième angle dans lequel la rainure doit s\'étendre dans la direction opposée. Les directions peuvent être inversées en cochant l\'option **Inversé**.



### Axe

Spécifie l\'axe de la rainure :

-   **Axe vertical de l\'esquisse** : sélectionne l\'axe vertical de l\'esquisse.
-   **Axe d\'esquisse horizontal** : sélectionne l\'axe horizontal de l\'esquisse.
-   **Ligne de construction** : sélectionne une ligne de construction de l\'esquisse utilisée par la rainure. La liste déroulante contient une entrée pour chaque ligne de construction. La première ligne de construction sera étiquetée *Ligne de construction 1*.
-   **Axe (X/Y/Z) de base** : sélectionne l\'axe X, Y ou Z de l\'origine du corps.
-   **Sélectionner une référence\...** : permet de sélectionner une ligne droite ou une [ligne de référence](PartDesign_Line/fr.md) du corps.

Remarquez que lors d\'un changement d\'axe, l\'option **Inversé** peut être (dé)cochée automatiquement.

### Angle

Définit l\'angle de la rainure. Cette option n\'est disponible que si **Type** est sur **Dimension** ou **Deux dimensions**. Les angles supérieurs à 360° ne sont pas possibles. Les valeurs négatives ne le sont pas non plus, utilisez plutôt l\'option **Inversé**.



### Symétrique au plan 

Cochez cette option pour étendre la rainure de la moitié de l\'angle donné de chaque côté de l\'esquisse ou de la face, si **Type** est sur **Dimension**, ou **A travers tout** si c\'est **Type**.



### Inversé

Inverse la direction de la rainure.



### 2ème angle 


{{Version/fr|1.0}}

Définit l\'angle de la rainure dans la direction opposée. Cette option n\'est disponible que si **Type** est sur **Deux dimensions** et que **Angle** est inférieur à 360°.



## Propriétés



### Données


{{TitleProperty|Groove}}

-    **Type|Enumeration**
    

-    **Base|Vector**: (lecture seulement)

-    **Axis|Vector**: (lecture seulement)

-    **Angle|Angle**
    

-    **Angle2|Angle**
    

-    **Up To Face|LinkSub**
    

-    **Reference Axis|LinkSub**
    


{{TitleProperty|Part Design}}

-    **Refine|Bool**
    


{{TitleProperty|Sketch Based}}

-    **Profile|LinkSub**
    

-    **Midplane|Bool**
    

-    **Reversed|Bool**
    

-    **Allow Multi Face|Bool**
    



## Remarques

-   Une <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width:16px;"> [PartDesign Forme liée](PartDesign_ShapeBinder/fr.md) ne peut pas être utilisée pour le profil.
-   Lors de l\'utilisation d\'une <img alt="" src=images/PartDesign_SubShapeBinder.svg  style="width:16px;"> [PartDesign Sous forme liée](PartDesign_SubShapeBinder/fr.md) pour le profil, la sélection de la liaison dans la [vue en arborescence](Tree_view/fr.md) échouera, mais la face de la liaison devra être sélectionnée dans la [vue 3D](3D_view/fr.md).





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Groove/fr
