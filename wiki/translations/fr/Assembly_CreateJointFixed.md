---
 GuiCommand:
   Name: Assembly CreateJointFixed
   Name/fr: Assembly Liaison fixe
   MenuLocation: Assemblage , Créer une liaison fixe
   Workbenches: Assembly_Workbench/fr
   Shortcut: **F**
   Version: 1.0
   SeeAlso: 
---

# Assembly CreateJointFixed/fr

## Description

L\'outil <img alt="" src=images/Assembly_CreateJointFixed.svg  style="width:24px;"> [Assembly Liaison fixe](Assembly_CreateJointFixed/fr.md) crée une liaison qui verrouille deux pièces de l\'assemblage, empêchant tout mouvement ou rotation.



## Utilisation

1.  Vous pouvez pouvez sélectionner deux entités géométriques de deux parties différentes. Les autres sélections seront rejetées.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Assembly_CreateJointFixed.svg" width=16px> [Créer une liaison fixe](Assembly_CreateJointFixed/fr.md)**.
    -   Sélectionnez l\'option **Assemblage → <img src="images/Assembly_CreateJointFixed.svg" width=16px> Créer une liaison fixe** du menu.
    -   Utiliser le raccourci clavier : **F**.
3.  Les pièces présélectionnées sont déplacées pour se rencontrer au niveau des entités sélectionnées.
4.  La fenêtre de dialogue **Créer une liaison** s\'ouvre dans le [panneau des tâches](Task_panel/fr.md) avec la liste des entités présélectionnées.
5.  Vous pouvez modifier le type de liaison dans la liste déroulante :
    -   Sélectionnez **Fixe**.
        1.  Si la liste de sélection est vide : sélectionnez deux entités géométriques.
        2.  Les pièces sont déplacées pour se rencontrer au niveau des entités sélectionnées.
        3.  Vous pouvez entrer une valeur de *Décalage*.
        4.  Vous pouvez entrer une valeur de *Rotation*.
        5.  Vous pouvez appuyer sur **<img src="images/Button_sort.svg" width=16px>** pour changer la direction de la liaison.
    -   Sélectionnez **Pivot**.
        1.  Si la liste de sélection est vide : sélectionnez deux entités géométriques.
        2.  Les pièces sont déplacées pour se rencontrer au niveau des entités sélectionnées.
        3.  Vous pouvez entrer une valeur de *Décalage*.
        4.  Vous pouvez appuyer sur **<img src="images/Button_sort.svg" width=16px>** pour changer la direction de la liaison.
        5.  Vous pouvez également cocher l\'option **Angle minimum** et rentrez une valeur.
        6.  Vous pouvez également cocher l\'option **Angle maximum** et rentrez une valeur.

        -   Sélectionnez **Pivot glissant**.

        1.  Si la liste de sélection est vide : sélectionnez deux entités géométriques.
        2.  Vous pouvez appuyer sur **<img src="images/Button_sort.svg" width=16px>** pour changer la direction de la liaison.
        3.  Vous pouvez également cocher l\'option **Longueur minimum** et rentrez une valeur.
        4.  Vous pouvez également cocher l\'option **Longueur maximum** et rentrez une valeur.
        5.  Vous pouvez également cocher l\'option **Angle minimum** et rentrez une valeur.
        6.  Vous pouvez également cocher l\'option **Angle maximum** et rentrez une valeur.

        -   Sélectionnez **Glissière**.

        1.  Si la liste de sélection est vide : sélectionnez deux entités géométriques.
        2.  Vous pouvez entrer une valeur de *Rotation*.
        3.  Vous pouvez appuyer sur **<img src="images/Button_sort.svg" width=16px>** pour changer la direction de la liaison.
        4.  Vous pouvez également cocher l\'option **Longueur minimum** et rentrez une valeur.
        5.  Vous pouvez également cocher l\'option **Longueur maximum** et rentrez une valeur.

        -   Sélectionnez **Bille**.

        1.  Si la liste de sélection est vide : sélectionner deux entités géométriques.

        -   Sélectionnez **Distance**.

        1.  Si la liste de sélection est vide : sélectionnez deux entités géométriques.
        2.  Vous pouvez entrer une valeur de *Distance*.
        3.  Vous pouvez appuyer sur **<img src="images/Button_sort.svg" width=16px>** pour changer la direction de la liaison.
    -   Sélectionnez **Parallèle**.
        1.  Si la liste de sélection est vide : sélectionnez deux entités géométriques.
        2.  Vous pouvez également appuyer sur **<img src="images/Button_sort.svg" width=16px>** pour changer la direction de la liaison.

        -   Sélectionnez **Perpendiculaire**.

        1.  Si la liste de sélection est vide : sélectionnez deux entités géométriques.

        -   Sélectionnez **Angle**.

        1.  Si la liste de sélection est vide : sélectionnez deux entités géométriques.
        2.  Vous pouvez pouvez entrer une valeur *Angle*.
    -   Sélectionnez **Crémaillère**.
        1.  Si la liste de sélection est vide : sélectionnez deux entités géométriques de deux parties différentes qui ont été précédemment utilisées pour définir une liaison glissière et une liaison pivot. (La direction du curseur et l\'axe de rotation doivent être perpendiculaires)
        2.  Entrez vous aussi une valeur de *Rayon primitif*.
    -   Sélectionnez **Hélicoïde**.
        1.  Si la liste de sélection est vide : sélectionnez deux entités géométriques de deux parties différentes qui ont été précédemment utilisées pour définir un joint coulissant et un joint à rotule. (La direction du curseur et l\'axe de rotation doivent être parallèles)
        2.  Entrez vous aussi une valeur de *Rayon primitif*.
    -   Sélectionnez **Engrenage**.
        1.  Si la liste de sélection est vide : sélectionnez deux entités géométriques de deux pièces différentes qui ont été précédemment utilisées pour définir deux articulations en croix différentes.
        2.  Vous pouvez entrer une valeur de *Rayon 1*.
        3.  Vous pouvez entrer une valeur de *Rayon 2*.
        4.  Vous pouvez cocher/décocher l\'option **Rotation inversée**. (décocher sélectionne l\'option **Courroie**). Ne fonctionne pas pour la 1.0 RC jusqu\'à présent.
    -   Sélectionnez **Courroie**.
        1.  Si la liste de sélection est vide : sélectionnez deux entités géométriques de deux pièces différentes qui ont été précédemment utilisées pour définir deux liaisons pivot différentes.
        2.  Vous pouvez entrer une valeur de *Rayon 1*.
        3.  Vous pouvez entrer une valeur de *Rayon 2*.
        4.  Vous pouvez cocher/décocher l\'option **Rotation inversée**. (cocher sélectionne l\'option **Engrenage**). Ne fonctionne pas pour la 1.0 RC jusqu\'à présent.
6.  Les pièces sont déplacées pour se retrouver au niveau des entités sélectionnées.
7.  Appuyez sur **OK** pour fermer l\'outil.



## Remarques

-   Une liaison fixe peut être utilisée comme un actionneur pour contrôler le mouvement d\'une simulation cinématique. L\'action de la molette de la souris dans le panneau des tâches réorganise immédiatement les pièces connectées.
    -   Le décalage se traduit par une translation le long de l\'axe Z local, les décalages négatifs sont acceptés.
    -   La rotation tourne autour de l\'axe Z local, les angles \> 360° et même les angles négatifs sont acceptés.



## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet **Fixed** est dérivé d\'un [App FeaturePython](App_FeaturePython/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :



### Données


{{TitleProperty|Joint}}

-    **Activated|Bool**: indique si la liaison est active.

-    **Distance|Float**: enregistre la **Distance** de la liaison Distance. Est également utilisé par les liaisons Crémaillère et Hélicoïde pour enregistrer le **Rayon primitif** et par les liaisons Engrenage et Courroie pour enregistrer le **Rayon1**.

-    **Distance2|Float**: deuxième distance de la liaison. Elle n\'est utilisée que par les liaisons Engrenage et Courroie pour enregistrer **Rayon2**.

-    **Distance2|Float**: deuxième distance de la liaison. Elle n\'est utilisée que par la liaison engrenage pour enregistrer le deuxième rayon.

-    **Joint Type|Ennumeration**: type de liaison. ({{Value|Fixed}}, {{Value|Revolute}}, {{Value|Cylindrical}}, {{Value|Slider}}, {{Value|Ball}}, {{Value|Distance}}, {{Value|Parallel}}, {{Value|Perpendicular}}, {{Value|Angle}}, {{Value|RackPinion}}, {{Value|Screw}}, {{Value|Gears}}, {{Value|Belt}})

Propriétés supprimées (v.1.0.0-RC-38728) Il s\'agit des propriétés qui pouvaient être utilisées pour animer :

-    **Offset|Vector**: vecteur de décalage de la liaison.

-    **Rotation|Float**: rotation de la liaison.


{{TitleProperty|Joint Connector 1}}

-    **Detach1|Bool**: ceci empêche placement1 d\'être recalculé, ce qui permet un positionnement personnalisé de l\'emplacement.

-    **Offset1|Placement**: décalage d\'attachement du premier connecteur de la liaison. (ajouté avec la v.1.0.0-RC-38728)

-    **Placement1|Placement**: système de coordonnées locales dans l\'objet reference1 qui sera utilisé pour la liaison.

-    **Reference1|XlinkSubHidden**: première référence de la liaison.

Propriétés supprimées :

-    **Element1|String**: élément sélectionné du premier objet.

-    **Object1|String**: premier objet de la liaison.

-    **Part1|Link**: première pièce de la liaison.

-    **Vertex1|String**: sommet sélectionné du premier objet.


{{TitleProperty|Joint Connector 2}}

-    **Detach2|Bool**: ceci empêche placement2 d\'être recalculé, ce qui permet un positionnement personnalisé de l\'emplacement.

-    **Offset2|Placement**: décalage d\'attachement du deuxième connecteur de la liaison. (ajouté avec la v.1.0.0-RC-38728)

-    **Placement2|Placement**: système de coordonnées locales dans l\'objet reference2 qui sera utilisé pour la liaison.

-    **Reference2|XlinkSubHidden**: deuxième référence de la liaison.

Propriétés supprimées :

-    **Element2|String**: élément sélectionné du deuxième objet.

-    **Object2|String**: deuxième objet de la liaison.

-    **Part2|Link**: deuxième pièce de la liaison.

-    **Vertex2|String**: sommet sélectionné du deuxième objet.


{{TitleProperty|Limits}}

-    **Angle Max|Float**: limite maximale de l\'angle entre les deux systèmes de coordonnées (entre leurs axes X).

-    **Angle Min|Float**: limite minimale de l\'angle entre les deux systèmes de coordonnées (entre leurs axes X).

-    **Enable Angle Max|Bool**: active la limite maximale de l\'angle de la liaison.

-    **Enable Angle Min|Bool**: active la limite minimale de l\'angle de la liaison.

-    **Enable Length Max|Bool**: active la limite de longueur maximale de la liaison.

-    **Enable Length Min|Bool**: active la limite de longueur minimale de la liaison.

-    **Length Max|Float**: limite maximale de la distance entre les deux systèmes de coordonnées (entre leurs axes Z).

-    **Length Min|Float**: limite minimale de la distance entre les deux systèmes de coordonnées (entre leurs axes Z).

Propriété supprimée :

-    **Enable Limits|Bool**: cette liaison utilise-t-elle des limites ?





{{Assembly_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly CreateJointFixed/fr
