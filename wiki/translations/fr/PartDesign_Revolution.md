---
 GuiCommand:
   Name: PartDesign_Revolution
   Name/fr: PartDesign Révolution
   MenuLocation: PartDesign , Créer une fonction additive , Révolution
   Workbenches: PartDesign_Workbench/fr
   SeeAlso: PartDesign_Groove/fr
---

# PartDesign Revolution/fr

## Description

L\'outil **Révolution** produit un solide par révolution d\'une esquisse ou d\'un objet 2D sélectionné autour d\'un axe donné.

![](images/PartDesign_Revolution_example.svg )



*Ci-dessus : l'esquisse (A) est révolutionnée de 270 degrés dans le sens antihoraire autour de l'axe (B) ; le solide résultant (C) est montré à droite.*



## Utilisation

1.  Sélectionnez une seule esquisse ou une ou plusieurs faces du corps.
2.  Appuyez sur le bouton **<img src="images/PartDesign_Revolution.svg" width=24px> [Révolution](PartDesign_Revolution/fr.md)**.
3.  Définissez les paramètres de la révolution,voir [Options](#Options.md) ci-dessous.
4.  Appuyez sur le bouton **OK**.

## Options

Lors de la création d\'une révolution, ou après avoir double-cliqué sur une révolution existante dans la [vue en arborescence](Tree_view/fr.md), le panneau de tâches **Paramètres de la révolution** s\'affiche. Il propose les paramètres suivants :

![](images/partdesign_revolution_parameters.png )

### Type


{{Version/fr|1.0}}

Type offre cinq façons différentes de spécifier l\'angle de la révolution :

#### Dimension

Entrez une valeur numérique pour l**\'angle** de la révolution. Avec l\'option **Symétrique au plan**, la révolution s\'étendra à la moitié de l\'angle donné de chaque côté de l\'esquisse ou de la face.



#### À la dernière 

La révolution sera prolongée jusqu\'à la dernière face du support qu\'il rencontre dans sa direction. S\'il n\'y a pas de support, un message d\'erreur apparaît.



#### La plus proche 

La révolution sera prolongée jusqu\'à la première face rencontrée dans sa direction. S\'il n\'y a aucun support rencontré, un message d\'erreur apparaîtra.



#### Jusqu\'à une face 

La révolution sera prolongée jusqu\'à une face. Appuyez sur le bouton **Face** et sélectionnez une face ou un [plan de référence](PartDesign_Plane/fr.md) du corps.



#### Deux dimensions 

Cela permet d\'entrer un deuxième angle dans lequel la révolution doit s\'étendre dans la direction opposée. Les directions peuvent être inversées en cochant l\'option **Inversé**.



### Axe

Spécifie l\'axe de la révolution :

-   **Axe vertical de l\'esquisse** : sélectionne l\'axe vertical de l\'esquisse.
-   **Axe d\'esquisse horizontal** : sélectionne l\'axe horizontal de l\'esquisse.
-   **Ligne de construction** : sélectionne une ligne de construction de l\'esquisse utilisée par la révolution. La liste déroulante contient une entrée pour chaque ligne de construction. La première ligne de construction sera étiquetée *Ligne de construction 1*.
-   **Axe (X/Y/Z) de base** : sélectionne l\'axe X, Y ou Z de l\'origine du corps.
-   **Sélectionner une référence\...** : permet de sélectionner une ligne droite ou une [ligne de référence](PartDesign_Line/fr.md) du corps.

Remarquez que lors d\'un changement d\'axe, l\'option **Inversé** peut être (dé)cochée automatiquement.



### Angle

Définit l\'angle de la révolution. Cette option n\'est disponible que si **Type** est sur **Dimension** ou **Deux dimensions**. Les angles supérieurs à 360° ne sont pas possibles. Les valeurs négatives ne le sont pas non plus, utilisez plutôt l\'option **Inversé**.



### Symétrique au plan 

Cochez cette option pour étendre la révolution de la moitié de l\'angle donné de chaque côté de l\'esquisse ou de la face. Cette option n\'est disponible que si **Type** est sur **Dimension**.



### Inversé

Inverse la direction de la révolution.



### 2ème angle 


{{Version/fr|1.0}}

Définit l\'angle de la révolution dans la direction opposée. Cette option n\'est disponible que si **Type** est sur **Deux dimensions** et que **Angle** est inférieur à 360°.



## Propriétés



### Données


{{TitleProperty|Part Design}}

-    **Refine|Bool**
    


{{TitleProperty|Revolution}}

-    **Type|Enumeration**
    

-    **Base|Vector**: (lecture seulement)

-    **Axis|Vector**: (lecture seulement)

-    **Angle|Angle**
    

-    **Up To Face|LinkSub**
    

-    **Angle2|Angle**
    

-    **Reference Axis|LinkSub**
    


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
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Revolution/fr
