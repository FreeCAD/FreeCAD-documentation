---
 TutorialInfo:r
   Topic: Architecture
   Level: Intermédiaire
   Time: 60 minutes
   Author: https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=21943 vocx
   FCVersion: 0.18 ou ultérieure
   Files: aucun
}}



## Introduction

Ce didacticiel montre comment placer des fenêtres Arch et des portes Arch personnalisées dans un modèle de bâtiment. Il utilise l\'atelier Draft, l\'atelier Arch et l\'atelier Sketcher.

Les outils couramment utilisés sont: Draft Grille, Draft Aimantation, Draft Polyligne, Arch Mur, Arch Fenêtre et Sketcher Esquisse. L\'utilisateur doit être familiarisé avec les esquisses contraignantes.

Ce tutoriel est inspiré des tutoriels de jpg87 publiés dans les forums FreeCAD.

-   Arch Créer une fenêtre personnalisée
-   Arch: Comment utiliser votre fenêtre personnalisée

Voir également le fil suivant pour plus d\'informations sur la position des fenêtres et des portes.

-   Discussion: Orientation des fenêtres et des portes

Voir également la page suivante pour quelques vidéos sur la façon d\'aligner les fenêtres.

-   L\'atelier utilisé pour créer des projets architecturaux s\'appelle Arch



## Installation

1\. Ouvrez FreeCAD, créez un nouveau document vide et passez à l\'atelier Arch

2\. Assurez-vous que vos unités sont correctement définies dans le menu **Edition , Préférences , Général , Unités**. Par exemple, {{incode   MKS }}{: mediawiki} est bon pour gérer les distances dans un bâtiment typique; de plus, définissez le nombre de décimales sur {{incode   4}}{: mediawiki} pour considérer même les plus petites fractions du mètre.

3\. Utilisez le bouton Draft Visibilité de la grille pour afficher une grille avec une résolution suffisante. Vous pouvez modifier l\'apparence de la grille dans le menu **Edition , Préférences , Draft , Grille et ancrage , Grille**. Définissez des lignes tous les {{incode   50 mm}}{: mediawiki}, avec des lignes principales toutes les {{incode   20}}{: mediawiki} lignes  et {{incode   1000 lignes}}{: mediawiki} au total .

4\. Zoom arrière de la vue 3D si vous êtes trop près de la grille.

Nous sommes maintenant prêts à créer un mur simple sur lequel nous pouvons positionner les fenêtres et les portes.



## Placement d\'un mur 

5\. Utilisez l\'outil Draft Fil pour créer un fil. Allez dans le sens antihoraire.

:   5.1. Premier point dans ; dans la boîte de dialogue, saisissez **0** **m** **Enter**, **4** **m** **Enter**, {{ KEY\   0}} **m**{: mediawiki} **Enter**.
:   5.2. Deuxième point dans ; dans la boîte de dialogue, saisissez **2** **m** **Enter**, **0** **m** **Enter**, {{ KEY\   0}} **m**{: mediawiki} **Enter**.
:   5.3. Troisième point dans ; dans la boîte de dialogue, saisissez **4** **m** **Enter**, **0** **m** **Enter**, {{ KEY\   0}} **m**{: mediawiki} **Enter**.
:   5.4. Quatrième point dans ; dans la boîte de dialogue, entrez **6** **m** **Enter**, **2** **m** **Enter**, {{ KEY\   0}} **m**{: mediawiki} **Enter**.
:   5.4. Cinquième point dans ; dans la boîte de dialogue, saisissez **6** **m** **Enter**, **5** **m** **Enter**, {{ KEY\   0}} **m**{: mediawiki} **Enter**.
:   5.5. Sur le pavé numérique, appuyez sur **A** pour terminer le fil.
:   5.6. Dans le pavé numérique, appuyez sur **0** pour obtenir une vue axonométrique du modèle.
:   
    **Note:**assurez-vous que la case **Relative** est désactivée si vous donnez des coordonnées absolues.
:   
    **Note 2:**les points peuvent également être définis avec le pointeur de la souris en choisissant les intersections sur la grille, à l\'aide de la barre d\'outils Draft Aimantation et de la méthode Draft Aimantation Grille .
:   
    **Note 3:**vous pouvez également créer des formes par programmation en créant des scripts dans Python. Attention, la plupart des fonctions attendent leur saisie en millimètres.


{{Code   code: 
import FreeCAD
import Draft

p = FreeCAD.Vector,
FreeCAD.Vector,
FreeCAD.Vector,
FreeCAD.Vector,
FreeCAD.Vector

w = Draft.makeWire
---

# Tutorial custom placing of windows and doors/fr

 
6\. Sélectionnez `DWire` et cliquez sur l\'outil [Arch Mur](Arch_Wall/fr.md); le mur est immédiatement créé avec une largeur (épaisseur) par défaut de 0,2 m et une hauteur de 3 m.

<img alt="" src=images/01_T02_wire_wall.png  style="width:600px;">



*align=center|Fil de base pour le mur*

<img alt="" src=images/02_T02_just_wall.png  style="width:600px;">



*align=center|Mur construit à partir du fil*



## Placement de portes et fenêtres prédéfinies 

7\. Cliquez sur l\'outil [Arch Fenêtre](Arch_Window/fr.md); comme préréglage, sélectionnez `Simple door` et modifiez la hauteur à 2 m.

:   7.1. Changez l\'accrochage en [Draft Milieu](Draft_Snap_Midpoint/fr.md) et essayez de sélectionner le bord inférieur du mur frontal; faites pivoter la [vue standard](Std_View_Menu/fr.md) si nécessaire pour vous aider à choisir le bord et non la face du mur; lorsque le milieu est actif, cliquez pour placer la porte.
:   7.2. Cliquez à nouveau sur l\'outil [Arch Fenêtre](Arch_Window/fr.md) et placez une autre porte, mais cette fois au milieu du mur arrière; faites pivoter la [vue standard](Std_View_Menu/fr.md) si nécessaire.

<img alt="" src=images/03_T02_wall_place_doors.png  style="width:600px;">



*align=center|Accrochage au milieu du bord inférieur du mur pour placer la porte*


:   
    **Note:**la `Sill height` est la distance entre le sol et le bord inférieur de l\'élément. Pour les portes, la `Sill height` (Hauteur du seuil) est généralement de 0 m car les portes touchent normalement le sol; d\'autre part, les fenêtres ont une séparation habituelle de 0,5 m à 1,5 m du sol. `Sill height` ne peut être définie que lors de la création initiale de la fenêtre ou de la porte à partir d\'un préréglage. Une fois la fenêtre ou la porte insérée, modifiez son emplacement en éditant la {{PropertyData/fr|Position}} du vecteur `[x, y, z]` de l\'[Sketcher Esquisse](Sketcher_Workbench/fr.md) sous-jacente.



## Création de portes et fenêtres personnalisées 

8\. Passez à l\'[atelier Sketcher](Sketcher_Workbench/fr.md); sélectionnez la partie du mur à droite qui n\'a pas de porte; cliquez sur [Nouvelle esquisse](Sketcher_NewSketch/fr.md); sélectionnez **FlatFace** comme méthode de pièce jointe. Si la géométrie existante obstrue votre vue, cliquez sur la [Vue en section](Sketcher_ViewSection/fr.md) pour la supprimer.

9\. Dessinez une esquisse quelconque contenant trois fils fermés. Assurez-vous de fournir des contraintes à tous les fils.

:   9.1. Le fil extérieur est le plus gros et définira les principales dimensions de l\'objet fenêtre, ainsi que la taille du trou créé lorsqu\'il est intégré dans un [Arch Mur](Arch_Wall/fr.md). Assurez-vous que les dimensions sont nommées correctement, par exemple `Width` et `Height`. Une contrainte définit également la courbure du fil extérieur; donnez-lui un nom approprié, comme `HeightCurve`.
:   9.2. Le deuxième fil est décalé du fil extérieur et, ensemble, ils définissent la largeur du cadre fixe de la fenêtre. Nommez le décalage de manière appropriée, par exemple `FrameFixedOffset`. Il sera utilisé pour les décalages verticaux et horizontaux supérieurs. Le décalage du bas, s\'il est défini sur zéro, aura pour effet que le cadre fixe touche le bas de la fenêtre; cela peut être utilisé pour modéliser une porte au lieu d\'une fenêtre. Donnez-lui un nom approprié, comme `FrameFixedBottom`.
:   9.3. Le troisième fil, le plus à l\'intérieur, est décalé du deuxième fil, et avec lui, ils définissent le cadre de la fenêtre qui peut s\'ouvrir. Le fil le plus à l\'intérieur définit également la taille du panneau de verre. Encore une fois, donnez des noms significatifs à ces décalages, par exemple, `FrameInnerOffset` et `FrameInnerBottom`.
:   9.4. Afin de construire avec succès l\'esquisse, utilisez les contraintes horizontales ([Sketcher Contrainte horizontale](Sketcher_ConstrainHorizontal/fr.md)) et verticales ([Sketcher Contrainte verticale](Sketcher_ConstrainVertical/fr.md)) pour les côtés droits; utilisez la géométrie de construction auxiliaire ([Sketcher Géométrie de construction](Sketcher_ToggleConstruction/fr.md)) et les contraintes tangentielles ([Sketcher Contrainte tangente](Sketcher_ConstrainTangent/fr.md)) pour placer correctement les arcs de cercle en haut. Comme dans ce cas, la fenêtre est symétrique, considérez les contraintes d\'égalité ([Sketcher Contrainte d\'egalité](Sketcher_ConstrainEqual/fr.md)), symétrique ([Sketcher Contrainte de symétrie](Sketcher_ConstrainSymmetric/fr.md)) et de point sur objet ([Sketcher Contrainte Point sur un objet](Sketcher_ConstrainPointOnObject/fr.md)) là où cela a du sens.

![](images/04_T02_window_constraints_outer_frame.png )



*align=center|Contraintes pour les fils extérieurs de l'esquisse qui forment la fenêtre*

![](images/05_T02_window_constraints_inner_frame.png )



*align=center|Contraintes pour les fils intérieurs de l'esquisse qui forment la fenêtre*

10\. Une fois l\'esquisse entièrement contrainte, appuyez sur **Close** pour quitter l\'esquisse ([Sketcher Quitter l\'esquisse](Sketcher_LeaveSketch/fr.md)).

:   10.1. Puisqu\'une face du mur a été sélectionnée lors de l\'étape initiale de création de l\'esquisse, l\'esquisse est coplanaire avec cette face; cependant, il peut être dans la mauvaise position, loin du mur. Si tel est le cas, ajustez {{PropertyData/fr|Position}} dans {{PropertyData/fr|Attachment Offset}}. Définissez {{PropertyData/fr|Position}} sur `[4 m, 1 m, 0 m]` de sorte que l\'esquisse soit centrée dans le mur et à un mètre au-dessus du niveau du sol.
:   10.2. Vous pouvez voir les contraintes nommées sous {{PropertyData/fr|Constraints}}. Les valeurs peuvent être modifiées pour voir les cotes de changement d\'esquisse immédiatement.

<img alt="" src=images/07_T02_window_sketch_in_wall.png  style="width:600px;">



*align=center|Esquisse de fenêtre déplacée à la position souhaitée sur le mur*

<img alt="" src=images/06_T02_window_sketch_properties_constraints.png  style="width:600px;">



*align=center|Contraintes nommées de l'esquisse, qui peuvent être modifiées sans entrer dans l'esquisse*

11\. Revenez à l\'[atelier Arch](Arch_Workbench/fr.md) et, avec le nouveau `Sketch002` sélectionné, utilisez [Arch Fenêtre](Arch_Window/fr.md). Une fenêtre sera créée et fera un trou dans le mur. La fenêtre est créée à partir d\'une esquisse personnalisée, et non à partir d\'un préréglage, elle doit donc être modifiée pour afficher correctement ses composants, à savoir le cadre fixe, le cadre intérieur et le panneau de verre.

<img alt="" src=images/08_T02_window_basic_in_wall.png  style="width:600px;">



*align=center|Fenêtre personnalisée créée à partir de l'esquisse; elle n'a toujours pas de cadre approprié, ni de verre*



## Configuration de la fenêtre personnalisée 

12\. Dans l\'arborescence, sélectionnez `Sketch002` sous-jacent à `Window` et appuyez sur **Espace** ou modifiez la propriété {{PropertyView/fr|Visibility}} en `True`.

13\. Double-cliquez sur `Window` dans l\'arborescence pour commencer à l\'éditer.

:   13.1. Dans la boîte de dialogue `Window elements`, il y a deux volets, `Wires` et `Components`. Il y a trois fils, `Wire0`, `Wire1` et `Wire2`, et un composant, `Default`. Les fils font référence aux boucles fermées qui ont été dessinées dans l\'esquisse; les composants définissent les zones de l\'esquisse qui seront extrudées pour créer des cadres ou des panneaux de verre avec des épaisseurs réelles; ces zones sont délimitées par les fils. Une fenêtre créée à partir d\'un preset a déjà deux composants, `OuterFrame` et `Glass`. La fenêtre personnalisée doit être modifiée pour avoir une structure similaire.

![](images/09_T02_window_edit_default.png )



*align=center|Boîte de dialogue pour modifier une fenêtre ou une porte*


:   13.2. Cliquez sur `Default`, puis sur le bouton **Remove** pour l\'éliminer.





:   13.3. Cliquez sur **Add**; cela montre les propriétés d\'un nouveau composant comme `Name`, `Type`, `Wires`, `Thickness`, `Offset`, { {incode\|Hinge}} et `Opening mode`. Donnez un nom, tel que `OuterFrame`, choisissez `Frame` pour `Type`, et cliquez sur `Wire0` puis `Wire1` ; ils doivent être mis en évidence dans la fenêtre 3D. Ajoutez une petite valeur pour `Thickness`, `15 mm` et cochez la case pour ajouter la valeur par défaut. Cette valeur par défaut est la longueur affectée à la propriété {{PropertyData/fr|Frame}}; une valeur par défaut similaire peut être attribuée à la propriété {{PropertyData/fr|Offset}}. Cliquez sur le bouton **+Create/update component** pour terminer la modification du composant.





:   13.4. Cliquez sur **Add**; donnez un autre nom, tel que `InnerFrame`, choisissez `Frame` pour `Type`, et cliquez sur `Wire1` puis `Wire2` . Ajoutez un `Thickness`, `60 mm`, et `Offset`, `15 mm`. Cliquez ensuite sur le bouton **+Create/update component**.





:   13.5. Cliquez sur **Add**; donnez un autre nom, tel que `Glass`, choisissez `Glass panel` pour `Type`, et cliquez sur `Wire2`. Ajoutez un `Thickness`, `10 mm`, et `Offset`, `40 mm`. Cliquez ensuite sur le bouton **+Create/update component**. Si l\'un des trois composants doit être modifié, sélectionnez-le et appuyez sur **Edit**; les modifications ne sont enregistrées qu\'après avoir appuyé sur le bouton **+Create/update component**.

![](images/10_T02_window_edit_components.png )



*align=center|Modification d'un composant précédemment défini d'une fenêtre ou d'une porte*


:   13.6. Si tout est défini, cliquez sur **Close** pour terminer l\'édition de la fenêtre. L\'esquisse peut redevenir masquée, mais la fenêtre affichera des éléments solides distincts pour `OuterFrame`, `InnerFrame` et `Glass`. Donnez une valeur de `100 mm` à {{PropertyData/fr|Frame}} pour attribuer une épaisseur par défaut, qui sera ajoutée à la valeur spécifiée dans le composant `OuterFrame`.

![](images/11_T02_window_property_view.png )



*align=center|Vue des propriétés de la fenêtre pour ajouter la longueur du cadre par défaut, la longueur du décalage et d'autres options*

<img alt="" src=images/12_T02_window_finished.png  style="width:600px;">



*align=center|Fenêtre finie avec des composants appropriés intégrés dans le mur*



## Duplication de la fenêtre personnalisée 

14\. Dans l\'arborescence, sélectionnez `Window` et son sous-jacent `Sketch002`. Puis allez dans **Edition → Copier la sélection**, et répondez **No** si on vous demande de dupliquer les dépendances non sélectionnées. Un nouveau `Window001` et `Sketch003` apparaîtront dans la même position que les éléments d\'origine.

15\. Sélectionnez le nouveau `Sketch003`. Accédez à la propriété {{PropertyData/fr|Map Mode}} et cliquez sur les points de suspension à côté de la valeur `FlatFace`. Dans la fenêtre 3D, sélectionnez le côté gauche du mur qui n\'a aucun élément; faites pivoter la [vue standard](Std_View_Menu/fr.md) si nécessaire. Modifiez `Attachment offset` en \[-1 m, 0 m, 0 m\] pour centrer la fenêtre, puis cliquez sur **OK**. L\'esquisse et la fenêtre doivent apparaître dans une nouvelle position.

:   
    **Note:**[Part Ancrage](Part_EditAttachment/fr.md) peut également être effectuée en passant à [atelier Part](Part_Workbench/fr.md), puis en utilisant le menu **Pièce → Attachment**.

![](images/13_T02_sketch_attachment_edit.png )



*align=center|Boîte de dialogue pour modifier le plan d'association de l'esquisse*

16\. Vous pouvez ajuster les dimensions de la nouvelle fenêtre en modifiant les paramètres nommés dans `Sketch003` sous {{PropertyData/fr|Contraintes}}, par exemple, définissez `Height` à `2 m` et `Frame Fixed Bottom` à `0 m`. Appuyez ensuite sur **Ctrl**+**R** pour [recalculer](recompute/fr.md) le modèle. Si le mur n\'affiche pas un plus grand trou pour la nouvelle fenêtre, sélectionnez le mur dans l\'arborescence, faites un clic droit et choisissez `Mark to recompute`, puis appuyez sur **Ctrl**+**R** à nouveau.

17\. Ces opérations ont changé la position de la nouvelle fenêtre, mais l\'ouverture dans le mur n\'a pas l\'air correcte. Il est incliné, c\'est-à-dire que le trou n\'est pas perpendiculaire à la face du mur et qu\'il peut même couper d\'autres parties du mur. Le problème est que `Window001` a conservé les informations {{PropertyData/fr|Normal}} de l\'original `Window`.

<img alt="" src=images/14_T02_sketch_2_attached_slanted.png  style="width:600px;">



*align=center|Ouverture incorrecte dans le mur en raison d'une mauvais normale de la fenêtre*



## Normales des portes et fenêtres 

18\. Chaque objet [Arch Fenêtre](Arch_Window/fr.md) contrôle l\'extrusion de son corps et l\'ouverture qui est créée dans sa paroi hôte au moyen de sa {{PropertyData/fr|Normal}}.

La normale est un vecteur `[x, y, z]` qui indique une direction perpendiculaire à un mur. Lorsqu\'un préréglage de fenêtre ou de porte est créé avec l\'outil [Arch Fenêtre](Arch_Window/fr.md) directement sur un [Arch Mur](Arch_Wall/fr.md), la normale est automatiquement calculée et la fenêtre ou la porte résultante est correctement alignée; les deux premiers objets, `Door` et `Door001`, ont été créés de cette manière.

De la même manière, lorsqu\'une esquisse est créée en sélectionnant une surface plane, elle est orientée sur ce plan. Ensuite, lorsque l\'outil [Arch Fenêtre](Arch_Window/fr.md) est utilisé, la fenêtre utilisera normalement la direction perpendiculaire à l\'esquisse. Ce fut le cas avec le troisième objet, la `Window` personnalisée.

Si la fenêtre existe déjà et doit être déplacée, comme c\'était le cas avec l\'objet `Window001` dupliqué, l\'esquisse doit être remappée sur un autre plan; cela déplace à la fois l\'esquisse et la fenêtre, mais celle-ci ne met pas automatiquement à jour sa normale, elle contient donc des informations d\'extrusion incorrectes. La normale doit être calculée manuellement et écrite dans {{PropertyData/fr|Normal}}.

Les trois valeurs du vecteur normal sont calculées comme suit. 
```python
x = -sin(angle)
y = cos(angle)
z = 0
``` Où `angle` est l\'angle de l\'axe Z local de l\'esquisse par rapport à l\'axe Y global.

Lorsqu\'une esquisse est créée, elle a toujours deux axes, un X local (rouge) et un Y local (vert). Si l\'esquisse est mappée sur le plan de travail global XY, ces axes sont alignés; mais si l\'esquisse est mappée sur les plans XZ globaux ou YZ globaux, comme cela est courant avec les fenêtres et les portes (les esquisses sont \"debout\"), alors le Z local (bleu) forme un angle avec l\'axe Y global; cet angle varie de -180 à 180 degrés. L\'angle est considéré comme positif s\'il s\'ouvre dans le sens antihoraire, et il est négatif s\'il s\'ouvre dans le sens horaire, en partant de l\'axe Y global.

<img alt="" src=images/15_T02_sketch_local_coordinates.png  style="width:600px;">



*align=center|Coordonnées locales d'une esquisse "debout", c'est-à-dire mappée sur le plan XZ global*

<img alt="" src=images/16_T02_sketch_correct_normal_direction.png  style="width:600px;">



*align=center|Directions prévues des normales pour chaque porte et fenêtre*

Si nous regardons la géométrie créée jusqu\'à présent, nous voyons les normales suivantes.

`Door`
:   Le Z local est aligné sur le Y global, par conséquent, l \'`angle` est nul. Le vecteur normal est


```python
x = -sin(0) = 0
y = cos(0) = 1
z = 0
```

ou {{PropertyData/fr|Normal}} est `[0, 1, 0]`.

`Door001`
:   Le Z local est tourné de 90 degrés par rapport au Y global, par conséquent, le `angle` est de 90 (positif, car il s\'ouvre dans le sens antihoraire). Le vecteur normal est


```python
x = -sin(90) = -1
y = cos(90) = 0
z = 0
```

ou {{PropertyData/fr|Normal}} est `[-1, 0, 0]`.

`Window`
:   Le Z local est tourné de 45 degrés par rapport au Y global, donc le `angle` est de 45 (positif, car il s\'ouvre dans le sens antihoraire). Le vecteur normal est


```python
x = -sin(45) = -0.7071
y = cos(45) = 0.7071
z = 0
```

ou {{PropertyData/fr|Normal}} est `[-0.7071, 0.7071, 0]`.

`Window001`
:   La direction Z locale est trouvée en utilisant l\'outil [Draft Dimension](Draft_Dimension/fr.md) et en mesurant l\'angle que fait le tracé du mur (`Wire`) avec l\'axe Y global ou toute ligne alignée dessus. Cet angle est `26.57`; l\'angle souhaité est le complément de cela, donc 90 - 26.57 = 63.43.

Cela signifie que l\'axe Z local est tourné de 63,43 degrés par rapport au Y global, par conséquent, l\'`angle` est de -63,46 (négatif, car il s\'ouvre dans le sens des aiguilles d\'une montre). Le vecteur normal est 
```python
x = -sin(-63.43) = 0.8943
y = cos(-63.43) = 0.4472
z = 0
``` Par conséquent {{PropertyData/fr|Normal}} devrait être changé en `[0.8943, 0.4472, 0]`.

Après avoir effectué ces modifications, recalculez le modèle avec **Ctrl**+**R**. Si le mur ne met pas à jour le trou, sélectionnez-le dans l\'arborescence, faites un clic droit et choisissez `Mark to recompute` puis appuyez à nouveau sur **Ctrl**+**R**.

19\. L\'orientation de l\'extrusion de la fenêtre est résolue, ainsi que l\'ouverture dans le mur.

<img alt="" src=images/17_T02_sketch_2_attached_correctly.png  style="width:600px;">



*align=center|Ouverture correcte dans le mur en raison de la bonne  normale de la fenêtre*



## Remarques finales 

20\. Comme démontré, l\'emplacement initial de la [Arch Fenêtre](Arch_Window/fr.md) est très important. L\'utilisateur doit soit

-   utilisez l\'outil [Arch Fenêtre](Arch_Window/fr.md) pour insérer et aligner automatiquement un préréglage sur un mur, ou
-   mappez une esquisse sur le mur souhaité et construisez la fenêtre après cela.

Si une fenêtre existe déjà et qu\'elle doit être déplacée, l\'esquisse de support doit être remappée sur un nouveau plan et les {{PropertyData/fr|Normal}} de la fenêtre doivent être recalculées.

La nouvelle direction normale peut être obtenue en mesurant l \'`angle` du nouveau mur par rapport à l\'axe Y global, en considérant si cet angle est positif (sens antihoraire) ou négatif (sens horaire), et en utilisant une formule simple. 
```python
x = -sin(angle)
y = cos(angle)
z = 0
```

Pour confirmer que les opérations sont correctes, la grandeur absolue du vecteur normal doit être de un. C\'est, 
```python
abs(N) = 1 = sqrt(x^2 + y^2 + z^2)
abs(N) = 1 = sqrt(sin^2(angle) + cos^2(angle) + z^2)
```


  {{Sketcher Tools navi}}



---
⏵ [documentation index](../README.md) > [Arch](Category_Arch.md) > [Draft](Category_Draft.md) > [Sketcher](Category_Sketcher.md) > Tutorial custom placing of windows and doors/fr
