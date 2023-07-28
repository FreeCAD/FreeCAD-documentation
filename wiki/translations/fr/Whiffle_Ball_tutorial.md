# Whiffle Ball tutorial/fr
---
- TutorialInfo:/fr
   Topic: Conception de produits
   Level: Débutant
   Time:30 minutes
   Author:r-frank et vocx
   FCVersion:0.17 et plus
   Files:[https://github.com/FreeCAD/Examples/blob/master/Whiffle_Ball_Tutorial_ExampleFiles/WhiffleBall_Tutorial_FCWiki.FCStd?raw=true WhiffleBall_Tutorial_FCWiki.FCStd]
}}



## Introduction

Ce tutoriel a été écrit à l\'origine par Roland Frank († 2017, r-frank). Il a été réécrit et illustré par vocx.

Ce tutoriel est là pour vous apprendre à utiliser l\'[atelier Part](Part_Workbench/fr.md).

L\'atelier Part a été le premier atelier. Il fournit les éléments géométriques de base qui peuvent être utilisés comme blocs de construction pour d'autres ateliers. L\'atelier Part est destiné à être utilisé dans un flux de travaux classique [Géométrie Solide Constructive](Constructive_solid_geometry/fr.md) (CSG). Pour un flux de travail plus moderne utilisant des esquisses, des blocs et des fonctions, utilisez l\'[atelier PartDesign](PartDesign_Workbench/fr.md).

Vous vous exercerez à :

-   insérer des primitives
-   en modifiant les paramètres de ces objets primitifs
-   en modifiant leur [placement](placement/fr.md)
-   au moyen d\'opérations booléennes

![](images/10_T03_Part_ball_fillet.png ) 
*Modèle terminé de la balle à trous*



## Installation

1\. Ouvrez FreeCAD, créez un nouveau document vide avec **Fichier → [Nouveau](File:Std_New.svg   16px]] [[Std_New/fr.md)** et passez à l\'[atelier Part](Part_Workbench/fr.md).

:   1.1. Appuyez sur le bouton **[Vue isométrique](File:Std_ViewIsometric.svg   16px]] [[Std_ViewIsometric/fr.md)** ou appuyez sur **0** sur le pavé numérique pour changer la vue à isométrique pour mieux visualiser les solides 3D.
:   1.2. Appuyez sur le bouton **[Tout afficher](File:Std_ViewFitAll.svg   16px]] [[Std_ViewFitAll.md)** chaque fois que vous ajoutez des objets afin de faire un panoramique et un zoom sur la [Vue 3D](3D_view/fr.md) afin que tous les éléments sont visibles dans la vue.
:   1.3. Maintenez **Ctrl** pendant que vous cliquez pour sélectionner plusieurs éléments. Si vous avez sélectionné quelque chose de mal ou que vous voulez tout désélectionner, cliquez simplement sur un espace vide dans la [Vue 3D](3D_view/fr.md).



## Insérer des cubes primitifs 

2\. Insérez un cube primitif en cliquant sur **![](images/)**.

:   2.1. Sélectionnez {{incode   Cube}} dans la [Vue en arborescence](Tree_view/fr.md).
:   2.2. Modifiez les dimensions dans l\'onglet **Data** de l\'[Éditeur de propriétés](Property_editor/fr.md).
:   2.3. Remplacez **Length** par {{incode   90 mm}}.
:   2.4. Remplacez **Width** par {{incode   90 mm}}.
:   2.5. Remplacez **Height** par {{incode   90 mm}}.

3\. Dans l\'onglet **Data** de l\'[Éditeur de propriétés](Property_editor/fr.md), cliquez sur la valeur **Placement** pour que le bouton points de suspension **...** apparaisse sur la droite.

:   3.1. Appuyez sur les points de suspension pour ouvrir la boîte de dialogue [Placement](Std_Placement/fr.md).
:   3.2. Modifiez les valeurs de **Translation**.
:   3.3. Remplacez **X** par {{incode   -45 mm}}.
:   3.4. Remplacez **Y** par {{incode   -45 mm}}.
:   3.5. Remplacez **Z** par {{incode   -45 mm}}.
:   3.6. Appuyez sur le bouton **OK** pour fermer la boîte de dialogue.

4\. Répétez le processus en insérant un deuxième cube plus petit en cliquant sur **![](images/)**.

:   4.1. Le deuxième cube sera créé avec le même nom, mais avec un numéro supplémentaire pour distinguer l\'objet.
:   4.2. Sélectionnez {{incode   Cube001}} dans la [Vue en arborescence](Tree_view/fr.md) et modifiez les dimensions et le placement comme avec l\'objet précédent.
:   4.3. Remplacez **Length** par {{incode   80 mm}}.
:   4.4. Remplacez **Width** par {{incode   80 mm}}.
:   4.5. Remplacez **Height** par {{incode   80 mm}}.
:   4.6. Ouvrez la boîte de dialogue [Placement](Std_Placement.md).
:   4.7. Remplacez **X** par {{incode   -40 mm}}.
:   4.8. Remplacez **Y** par {{incode   -40 mm}}.
:   4.9. Remplacez **Z** par {{incode   -40 mm}}.
:   4.10. Appuyez sur le bouton **OK** pour fermer la boîte de dialogue.



## Modifier les propriétés visuelles 

5\. Les opérations précédentes créent un cube plus petit à l\'intérieur d\'un cube plus grand. Pour visualiser cela, nous pouvons modifier les propriétés **View** dans l\'[Éditeur de propriétés](Property_editor/fr.md).

:   5.1. Sélectionnez {{incode   Cube001}}, le plus petit cube, dans la [Vue en arborescence](Tree_view/fr.md) et changez la couleur. Dans l\'onglet **Vue**, cliquez sur la valeur **Shape Color** pour ouvrir la boîte de dialogue **Select color**, puis choisissez une couleur verte; modifiez également la valeur de **Line Width** en {{incode   2.0}}.
:   5.2. Sélectionnez {{incode   Cube}}, le plus grand cube, dans la [Vue en arborescence](Tree_view/fr.md). Dans l\'onglet **Vue**, modifiez la valeur de **Transparency** en {{incode   70}}.

![](images/01_T03_Part_cubes_visibility.png ) 
*Cube solide à l'intérieur d'un autre cube solide*



## Insérer des cylindres primitifs 

6\. Insérez un cylindre primitif en cliquant sur **![](images/)**.

:   6.1. Sélectionnez {{incode   Cylinder}} dans la [Vue en arborescence](Tree_view/fr.md).
:   6.2. Modifiez les dimensions dans l\'onglet **Data** de l\'[Éditeur de propriétés](Property_editor/fr.md).
:   6.3. Remplacez **Radius** par {{incode   27,5 mm}}.
:   6.4. Remplacez **Height** par {{incode   120 mm}}.
:   6.5. Ouvrez la boîte de dialogue [Placement](Std_Placement/fr.md).
:   6.6. Remplacez **Z** par {{incode   -60 mm}}.
:   6.7. Appuyez sur le bouton **OK** pour fermer la boîte de dialogue.

7\. Répétez le processus en insérant un deuxième cylindre en cliquant sur **![](images/)**.

:   7.1. Le deuxième cylindre sera créé avec le même nom, mais avec un numéro supplémentaire pour distinguer l\'objet.
:   7.2. Sélectionnez {{incode   Cylinder001}} dans la [vue en arborescence](Tree_view/fr.md) et modifiez les dimensions et le placement comme avec l\'objet précédent.
:   7.3. Remplacez **Radius** par {{incode   27,5 mm}}.
:   7.4. Remplacez **Height** par {{incode   120 mm}}.
:   7.5. Ouvrez la boîte de dialogue [Placement](Std_Placement/fr.md).
:   7.6. Remplacez **Y** par {{incode   60 mm}}.
:   7.7. Remplacez **Rotation** par {{incode   Rotation axis with angle}}; **Axis** à {{incode   X}} (en fixant les valeurs de {{incode   X}}, {{incode   Y}} et {{incode   Z}} des valeurs de l\'axe à {{incode   1}}, {{incode   0}} et {{incode   0}} respectivement) et **Angle** à {{incode   90 deg}}.
:   7.8. Appuyez sur le bouton **OK** pour fermer la boîte de dialogue.

8\. Insérez un autre cylindre. Cette fois, créez un doublon afin que le rayon et la hauteur ne doivent pas être modifiés, seulement son placement.

:   8.1. Sélectionnez {{incode   Cylinder001}} dans la [Vue en arborescence](Tree_view/fr.md) et allez dans le menu **Edition → [[Std_DuplicateSelection/fr   Dupliquer une sélection]]**. Cela créera {{incode   Cylinder002}}.
:   8.2. Ouvrez la boîte de dialogue [Placement](Std_Placement/fr.md).
:   8.3. Changez **X** en {{incode   -60 mm}}, et changez **Y** en {{incode   0 mm}}.
:   8.4. Changez **Rotation** par {{incode   Rotation axis with angle}}; **Axis** à {{incode   Y}} et **Angle** à {{incode   90 deg}}.
:   8.5. Appuyez sur le bouton **OK** pour fermer la boîte de dialogue.



## Modifier les propriétés visuelles 

9\. Les opérations précédentes créent trois cylindres qui se croisent et qui croisent également les cubes. Pour mieux visualiser cela, nous pouvons modifier les propriétés **View** dans l\'[Éditeur de propriétés](Property_editor/fr.md).

:   9.1. Sélectionnez {{incode   Cube001}}, le plus petit cube, dans la [Vue en arborescence](Tree_view/fr.md) et modifiez la transparence. Dans l\'onglet **View**, modifiez la valeur de **Transparency** en {{incode   70}}.
:   9.2. Sélectionnez {{incode   Cylinder}}, dans l\'onglet **View**, cliquez sur la valeur **Shape Color** pour ouvrir la boîte de dialogue **Select color**, puis choisissez une couleur rouge .
:   9.3. Sélectionnez {{incode   Cylinder001}}, dans l\'onglet **View**, cliquez sur la valeur **Shape Color** pour ouvrir la boîte de dialogue **Select color**, puis choisissez une couleur bleue .
:   9.4. Sélectionnez {{incode   Cylinder002}}, dans l\'onglet **View**, cliquez sur la valeur **Shape Color** pour ouvrir la boîte de dialogue **Select color**, puis choisissez une couleur rose .
:   9.5. Sélectionnez les trois cylindres, dans l\'onglet **View** changez également la valeur de **Line Width** en {{incode   2.0}}.

![](images/02_T03_Part_cylinders_visibility.png ) 
*Cylindres solides qui se croisent et les cubes solides.*



## Union et Soustraction 

10\. Dans la [Vue en arborescence](Tree_view/fr.md), sélectionnez {{incode   Cube001}} (le cube intérieur plus petit) et les cylindres de l\'arbre, puis appuyez sur **[Union](File:Part_Fuse.svg   16px]] [[Part_Fuse/fr.md)**. Cela créera un objet {{incode   Fusion}}.

11\. Effectuez ensuite une coupe booléenne du {{incode   Cube}} (cube plus grand) et du nouvel objet {{incode   Fusion}}.

:   11.1. Dans la [Vue en arborescence](Tree_view/fr.md), sélectionnez d\'abord {{incode   Cube}}, puis {{incode   Fusion}}.
:   11.2. Appuyez ensuite sur **[Soustraction](File:Part_Cut.svg   16px]] [[Part_Cut/fr.md)**. Cela créera un objet {{incode   Cut}}.
:   
    **Remarque:**l\'ordre dans lequel vous sélectionnez les objets est important pour l\'opération de soustraction. L\'objet de base est sélectionné en premier et l\'objet de soustraction vient à la fin.
:   11.3. Si les couleurs semblent étranges, sélectionnez le nouvel objet {{incode   Cut}}, allez dans l\'onglet **View**, cliquez sur la valeur **Shape Color** pour ouvrir la **Select color**, puis choisissez une couleur grise; modifiez également la valeur de **Line Width** en {{incode   2.0}}.

![](images/03_T03_Part_cube_cut.png ) 
*Forme creuse produite en coupant un cube et trois cylindres à partir d'un plus gros cube.*



## Insérer des cubes primitifs pour couper les coins du solide partiel 

Maintenant, nous allons créer plus de cubes qui seront utilisés comme outils de coupe pour couper les coins de l\'objet {{incode   Cut}} précédemment obtenu.

12\. Cliquez sur **![](images/)**.

:   12.1. Sélectionnez {{incode   Cube002}} dans la [Vue en arborescence](Tree_view/fr.md) et modifiez les dimensions et l\'emplacement.
:   12.2. Remplacez **Length** par {{incode   140 mm}}.
:   12.3. Remplacez **Width** par {{incode   112 mm}}.
:   12.4. Remplacez **Height** par {{incode   112 mm}}.
:   12.5. Ouvrez la boîte de dialogue [Placement](Std_Placement/fr.md).
:   12.6. Remplacez **X** par {{incode   -70 mm}}.
:   12.7. Remplacez **Y** par {{incode   -56 mm}}.
:   12.8. Remplacez **Z** par {{incode   -56 mm}}.
:   12.9. Appuyez sur **OK**.

13\. Cliquez sur **![](images/)**.

:   13.1. Sélectionnez {{incode   Cube003}} dans la [Vue en arborescence](Tree_view/fr.md) et modifiez les dimensions et l\'emplacement.
:   13.2. Remplacez **Length** par {{incode   180 mm}}.
:   13.3. Remplacez **Width** par {{incode   180 mm}}.
:   13.4. Remplacez **Height** par {{incode   180 mm}}.
:   13.5. Ouvrez la boîte de dialogue [Placement](Std_Placement/fr.md).
:   13.6. Remplacez **X** par {{incode   -90 mm}}.
:   13.7. Remplacez **Y** par {{incode   -90 mm}}.
:   13.8. Remplacez **Z** par {{incode   -90 mm}}.
:   13.9. Appuyez sur **OK**.

Nous dupliquerons à nouveau les deux objets précédents pour les utiliser à nouveau comme objets de coupe.

14\. Sélectionnez uniquement {{incode   Cube002}} dans la [Vue en arborescence](Tree_view/fr.md) et allez dans **Edition → [[Std_DuplicateSelection/fr   Dupliquer une sélection]]**. Cela créera {{incode   Cube004}}.

15\. Sélectionnez uniquement {{incode   Cube003}} dans la [Vue en arborescence](Tree_view/fr.md) et allez dans **Edition → [[Std_DuplicateSelection/fr   Dupliquer une sélection]]**. Cela créera {{incode   Cube005}}.

16\. Pour mieux visualiser cela, nous pouvons modifier les propriétés **View** dans l\'[Éditeur de propriétés](Property_editor/fr.md).

:   16.1. Sélectionnez l\'objet {{incode   Cut}}, dans l\'onglet **View**, cliquez sur la valeur **Shape Color** pour ouvrir la boîte de dialogue **Select color**, puis choisissez un couleur bleue.
:   16.2. Sélectionnez tous les nouveaux cubes, {{incode   Cube002}}, {{incode   Cube003}}, {{incode   Cube004}} et {{incode   Cube005}}, dans l\'onglet **View**, modifiez la valeur de **Transparency** à {{incode   80}}.

![](images/04_T03_Part_cube_additional.png ) 
*Cubes externes supplémentaires qui seront utilisés comme objets de coupe pour le solide interne.*



## Couper les coins partie 1 

17\. Dans la [Vue en arborescence](Tree_view/fr.md) sélectionnez {{incode   Cube002}} et {{incode   Cube003}}.

:   17.1. Ouvrez la boîte de dialogue [Placement](Std_Placement/fr.md).
:   17.2. Cochez l\'option **Apply incremental changes**; notez que toutes les valeurs de **Translation** sont remises à zéro.
:   17.3. Remplacez **Rotation** par {{incode   Rotation axis with angle}}; **Axis** à {{incode   X}} et **Angle** à {{incode   45 deg}}, puis cliquez sur **Apply**. Cela appliquera une rotation autour de l\'axe X et réinitialisera le champ **Angle** à zéro.
:   17.4. Modifiez à nouveau **Rotation**, maintenant **Axis** en {{incode   Z}} et **Angle** en {{incode   45 deg}}, puis cliquez sur { {Button\   Apply}}. Cela appliquera une rotation autour de l\'axe Z local et réinitialisera le champ **Angle** à zéro.
:   17.5. Cliquez sur **OK** pour fermer la boîte de dialogue.

18\. Dans la [Vue en arborescence](Tree_view/fr.md) désélectionnez les objets; puis sélectionnez d\'abord {{incode   Cube003}}, le plus gros cube, puis {{incode   Cube002}}, le plus petit cube.

:   18.1. Appuyez ensuite sur **[Soustraction](File:_Part_Cut.svg   16px]] [[Part_Cut/fr.md)**. Cela créera {{incode   Cut001}}. C\'est un corps évidé qui coupe le {{incode   Cut}} initial uniquement à certains coins.

19\. Pour mieux visualiser cela, nous pouvons modifier les propriétés **View** dans l\'[Éditeur de propriétés](Property_editor/fr.md).

:   19.1. Sélectionnez {{incode   Cube004}} et {{incode   Cube005}}, dans l\'onglet **View**, puis changez la valeur de **Visibility** en {{incode   false}}, ou appuyez sur **Espace** au clavier.
:   19.2. Sélectionnez {{incode   Cut001}}, cliquez sur la valeur **Shape Color** pour ouvrir la boîte de dialogue **Select color**, puis choisissez une couleur rouge; modifiez également la valeur de **Transparency** en {{incode   90}}.

![](images/05_T03_Part_cube_additional_cut_1.png ) 
*Un solide tourné et évidé, qui sera utilisé comme objet de coupe pour certains coins du solide interne.*



## Couper les coins partie 2 

20\. Dans la [Vue en arborescence](Tree_view/fr.md), sélectionnez {{incode   Cut001}}, dans l\'onglet **View**, changez la valeur de **Visibility** en {{incode   false }}, ou appuyez sur **Espace** au clavier.

21\. Dans la [Vue en arborescence](Tree_view/fr.md), sélectionnez {{incode   Cube004}} et {{incode   Cube005}}, dans l\'onglet **View**, modifiez la valeur de **Visibility ** à {{incode   true}}, ou appuyez sur **Espace** au clavier.

:   21.1. Ouvrez la boîte de dialogue [Placement](Std_Placement/fr.md).
:   21.2. Cochez l\'option **Apply incremental changes**; notez que toutes les valeurs de **Translation** sont remises à zéro.
:   21.3. Remplacez **Rotation** par {{incode   Rotation axis with angle}}; **Axis** à {{incode   X}}, et **Angle** à {{incode   45 deg}}, puis cliquez sur **Apply**. Cela appliquera une rotation autour de l\'axe X et réinitialisera le champ {{incode   Angle}} à zéro.
:   21,4. Changez à nouveau **Rotation**, maintenant **Axis** en {{incode   Z}}, et **Angle** en {{incode   -45 deg}}, puis cliquez sur **Apply**. Cela appliquera une rotation autour de l\'axe Z local et réinitialisera le champ **Angle** à zéro.
:   21.5. Cliquez sur **OK** pour fermer la boîte de dialogue.

18\. Dans la [Vue en arborescence](Tree_view/fr.md) désélectionnez les objets; puis sélectionnez d\'abord {{incode   Cube005}}, le plus gros cube, puis {{incode   Cube004}}, le plus petit cube.

:   18.1. Appuyez ensuite sur **[Soustraction](File:_Part_Cut.svg   16px]] [[Part_Cut/fr.md)**. Cela créera {{incode   Cut002}}. C\'est un corps évidé qui coupe le {{incode   Cut}} initial uniquement à certains coins.

23\. Pour mieux visualiser cela, nous pouvons modifier les propriétés **View** dans l\'[Éditeur de propriétés](Property_editor/fr.md).

:   23.1. Sélectionnez {{incode   Cut002}}, cliquez sur la valeur **Shape Color** pour ouvrir la boîte de dialogue **Select color**, puis choisissez une couleur rose; modifiez également la valeur de **Transparency** en {{incode   90}}.

![](images/06_T03_Part_cube_additional_cut_2.png ) 
*Un solide tourné et évidé, qui sera utilisé comme objet de coupe pour certains coins du solide interne.*



## Finalisation du modèle 

24\. Assurez-vous que tous les objets sont visibles. Dans la [Vue en arborescence](Tree_view/fr.md), sélectionnez tous les objets, dans l\'onglet **View**, changez la valeur de **Visibility** en {{incode   true}}, ou appuyez sur {{ KEY\|Espace}} sur le clavier.

![](images/07_T03_Part_ball_additional_both.png ) 
*Le solide creux interne, ainsi que les objets externes qui serviront à le découper.*

25\. Dans la [Vue en arborescence](Tree_view/fr.md), désélectionnez les objets; puis sélectionnez d\'abord {{incode   Cut}}, puis {{incode   Cut001}}.

:   25.1. Appuyez ensuite sur **[Soustraction](File:Part_Cut.svg   16px]] [[Part_Cut/fr.md)**. Cela créera {{incode   Cut003}}.

![](images/08_T03_Part_ball_cut_1.png ) 
*e solide creux interne, coupé par {{incode   Cut001*.}}

26\. Dans la [Vue en arborescence](Tree_view/fr.md), désélectionnez les objets; puis sélectionnez d\'abord {{incode   Cut003}}, puis {{incode   Cut002}}.

:   26.1. Appuyez ensuite sur **[Soustraction](File:Part_Cut.svg   16px]] [[Part_Cut/fr.md)**. Cela créera {{incode   Cut004}}. C\'est le dernier objet.
:   26.2. Sélectionnez {{incode   Cut004}}, cliquez sur la valeur **Shape Color** pour ouvrir la boîte de dialogue **Select color**, puis choisissez une couleur verte; modifiez également la valeur de **Line Width** en {{incode   2.0}}.

![](images/09_T03_Part_ball_cut_2.png ) 
*Le solide creux interne, coupé par {{incode   Cut001* et `Cut002`. Modèle final.}}

27\. Les objets réels n\'ont pas d\'arêtes ou d\'angles parfaitement nets, il est donc possible d\'appliquer un congé aux arêtes pour affiner le modèle.

:   27.1. Dans la [Vue en arborescence](Tree_view/fr.md), sélectionnez {{incode   Cut004}} puis appuyez sur **[Congé](File:Part_Fillet.svg   16px]] [[Part_Fillet/fr.md)**.
:   27.2. Dans le [Panneau des tâches](Task_panel/fr.md) de **Fillet edges**, allez dans **Selection**, choisissez **Select bords**, puis appuyez sur **All**. Comme **Fillet type** choisissez {{incode   Constant radius}}, puis définissez **Radius** sur {{incode   1 mm}}.
:   24.3. Appuyez sur **OK**. Cela créera un objet {{incode   Fillet}}.
:   27.4. Dans l\'onglet **View**, modifiez la valeur de **Line Width** en {{incode   2.0}}.

![](images/10_T03_Part_ball_fillet.png ) 
*Modèle terminé de la balle à trous avec des congés appliqués sur les bords.*


 {{Userdocnavi
---



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Category_Part.md) > Whiffle Ball tutorial/fr
