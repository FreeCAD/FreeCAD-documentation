# Tutorial for open windows/fr
{{TutorialInfo/fr
|Topic=Architecture
|Level=Débutant
|Time=60 minutes
|Author=[https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=21943 vocx]
|FCVersion=0.18 ou ultérieure
|Files=aucun
}}

## Introduction

Ce tutoriel montre comment placer des [Arch Fenêtres](Arch_Window/fr.md) et des portes dans un modèle de bâtiment, comment les afficher comme ouvertes dans la vue 3D et comment créer un dessin 2D (projection en plan et en élévation) pour le modèle. Il utilise l\'[atelier Draft](Draft_Workbench/fr.md), l\'[atelier Arch Workbench](Arch_Workbench/fr.md) et l\'[atelier TechDraw](TechDraw_Workbench/fr.md).

Les outils couramment utilisés sont: [Draft Grille](Draft_Snap_Grid/fr.md), [Draft Accrochage](Draft_Snap/fr.md), [Draft Fil](Draft_Wire/fr.md), [Arch Mur](Arch_Wall/fr.md), [Arch Fenêtre](Arch_Window/fr.md), [Arch Plan de section](Arch_SectionPlane/fr.md) et [TechDraw Vue architecturale](TechDraw_ArchView/fr.md).

Voir également la page suivante pour quelques vidéos sur la façon de travailler avec des fenêtres et des portes.

-   [L\'atelier utilisé pour créer des projets architecturaux s\'appelle Arch](http://help-freecad-jpg87.fr/04_arch_ind.php)

## Installation

1\. Ouvrez FreeCAD, créez un nouveau document vide et passez à l\'[atelier Arch](Arch_Workbench/fr.md)

2\. Assurez-vous que vos unités sont correctement définies dans le menu **Edition → Préférences → Général → Unités**. Par exemple, `MKS (m/kg/s/degré)` est bon pour gérer les distances dans un bâtiment typique; de plus, définissez le nombre de décimales sur `4` pour considérer même les plus petites fractions du mètre.

3\. Utilisez le bouton [Draft Visibilité de la grille](Draft_ToggleGrid/fr.md) pour afficher une grille avec une résolution suffisante. Vous pouvez modifier l\'apparence de la grille dans le menu **Edition → Préférences → Draft → Grille et ancrage → Grille**. Définissez des lignes tous les `50 mm`, avec des lignes principales toutes les `20` lignes (tous les mètres) et `1000 lignes` au total (la grille couvre une superficie de 50 mx 50 m).

4\. [Zoom arrière](Std_ViewZoomOut/fr.md) de la vue 3D si vous êtes trop près de la grille.

Nous sommes maintenant prêts à créer un bâtiment simple avec des murs fermés, deux portes et deux fenêtres.

## Placement d\'un mur 

5\. Utilisez l\'outil [Draft Fil](Draft_Wire/fr.md) pour créer un fil fermé. Allez dans le sens antihoraire.

:   5.1. Premier point à (0, 0, 0); dans la boîte de dialogue, saisissez **0** **m** **Enter**, **0** **m** **Valider**, {{ KEY\|0}} **m** **Valider**.
:   5.2. Deuxième point à (3, 0, 0). Appuyez sur **X** pour contraindre le mouvement à l\'axe X; entrez la valeur **3** **m** **Valider**.
:   5.3. Troisième point à (3, 4, 0). Appuyez sur **Y** pour contraindre le mouvement à l\'axe Y; entrez la valeur **4** **m** **Valider**.
:   5.4. Quatrième point à (0, 4, 0). Appuyez sur **X** pour contraindre le mouvement à l\'axe X; entrez la valeur **-** **3** **m** **Valider**.
:   5.5. Appuyez sur **O** pour fermer le fil et fermer l\'outil.
:   5.6. Au pavé numérique, appuyez sur **0** pour obtenir une [vue axonométrique](Std_View_Menu/fr.md) du modèle.
:   
    **Remarque:**les points peuvent également être définis avec le pointeur de la souris en choisissant les intersections sur la grille, à l\'aide de la barre d\'outils [Draft Accrochage](Draft_Snap/fr.md) et de la méthode [Draft Grille](Draft_Snap_Grid/fr.md).

6\. Sélectionnez `DWire` et remplacez la propriété {{PropertyData/fr|Make Face}} par `False`.

7\. Sélectionnez `DWire` et cliquez sur l\'outil [Arch Mur](Arch_Wall/fr.md). le mur est immédiatement créé avec une largeur (épaisseur) par défaut de 0,2 m et une hauteur de 3 m.

:   
    **Remarque:**si la propriété {{PropertyData/fr|Make Face}} de `DWire` est `True`, cette étape créerait un bloc solide, au lieu d\'utiliser uniquement le contour de `DWire`.

<img alt="" src=images/01_T01_wire_wall.png  style="width:600px;"> 
*align=center|Fil de base pour le mur; c'est un fil fermé qui ne fait pas une face*

<img alt="" src=images/02_T01_just_wall.png  style="width:600px;"> 
*align=center|Mur construit à partir du fil*

## Placement de portes et fenêtres 

8\. Cliquez sur l\'outil [Arch Fenêtre](Arch_Window/fr.md); comme préréglage, sélectionnez `Simple door` et modifiez la hauteur à 2 m.

:   8.1. Changez l\'accrochage en [Draft Milieu](Draft_Snap_Midpoint/fr.md) et essayez de sélectionner le bord inférieur du mur frontal; faites pivoter la [vue standard](Std_View_Menu/fr.md) si nécessaire pour vous aider à choisir le bord et non la face du mur; lorsque le milieu est actif, cliquez pour placer la porte.
:   8.2. Cliquez à nouveau sur l\'outil [Arch Fenêtre](Arch_Window/fr.md) et placez une autre porte, mais cette fois au milieu du mur arrière; faites pivoter la [vue standard](Std_View_Menu/fr.md) si nécessaire.

<img alt="" src=images/03_T01_wall_place_door_rear.png  style="width:600px;"> 
*align=center|Accrochage au milieu du bord inférieur du mur pour placer la porte*

9\. Cliquez sur l\'outil [Arch Fenêtre](Arch_Window/fr.md); comme préréglage, sélectionnez `Open 1-pane` et changez la `Sill height` à 1 m.

:   9.1. Conservez l\'accrochage sur [Draft Milieu](Draft_Snap_Midpoint.md) et essayez de sélectionner le bord inférieur du mur latéral gauche; faites pivoter la [vue standard](Std_View_Menu/fr.md) si nécessaire pour vous aider à choisir le bord et non la face du mur; lorsque le milieu est actif, cliquez pour placer la fenêtre.





:   
    **Remarque:**la `Sill height` (Hauteur du seuil) est la distance entre le sol et le bord inférieur de l\'élément. Pour les portes, la `Sill height` est généralement de 0 m car les portes touchent normalement le sol; d\'autre part, les fenêtres ont une séparation habituelle de 0,5 m à 1,5 m du sol.





:   9.2. Cliquez à nouveau sur l\'outil [Arch Fenêtre](Arch_Window/fr.md) et placez une autre fenêtre, mais cette fois au milieu du mur droit; faites pivoter la [vue standard](Std_View_Menu/fr.md) si nécessaire. Cette fois, faites la largeur (longueur) de la fenêtre de 1,5 m, puis faites à nouveau la `Sill height` 1 m.

<img alt="" src=images/04_T01_wall_place_door_side_right.png  style="width:600px;"> 
*align=center|Accrochage au milieu du bord inférieur du mur pour placer la fenêtre*

:   
    **Remarque:**le paramètre `Sill height` ne peut être défini que lors de la création initiale de la fenêtre avec un préréglage. Une fois la fenêtre insérée, modifiez son emplacement en éditant le vecteur {{PropertyData/fr|Position}} `[x, y, z]` du [Sketcher Sketch](Sketcher_Sketch/fr.md) sous-jacent.





:   9.3. Déplacez `Window001` un peu plus haut. Sélectionnez le `Sketch003` sous-jacent et changez sa {{PropertyData/fr|Position}} de `[3.1 m, 2.0 m, 1.0 m]` à `[3.1 m, 2.0 m, 1.6 m]`. L\'ensemble de `Window001` doit monter. Le mur peut encore montrer une ouverture dans la position précédente; si cela se produit, faites un clic droit sur l\'élément `Wall`, sélectionnez `Mark to recompute`, puis appuyez sur **Ctrl**+**R** pour [recalculer](recompute/fr.md) le modèle.

<img alt="" src=images/04.1_T01_wall_built.png  style="width:600px;"> 
*align=center|Mur construit avec portes et fenêtres*


**Remarque:**

lorsque vous placez une fenêtre ou une porte avec un préréglage, survolez l\'élément au-dessus du [Arch Mur](Arch_Wall/fr.md) et attendez que l\'élément tourne pour qu\'il soit parallèle à ce mur. Visez le bord inférieur du mur et utilisez `Sill height` pour ajuster la distance par rapport au sol. Si cela est difficile, utilisez le mode d\'accrochage [Draft Le plus proche](Draft_Snap_Near.md) de la barre d\'outils [Draft Accrochage](Draft_Snap/fr.md) pour insérer l\'élément n\'importe où sur la face du mur, puis ajustez sa {{PropertyData/fr|Position}} manuellement comme décrit ci-dessus. Le fait d\'avoir plusieurs modes [Draft Accrochage](Draft_Snap/fr.md) actifs en même temps peut entraîner des problèmes de placement de l\'élément, essayez donc avec une seule option à la fois.


**Remarque 2:**

occasionnellement, la fenêtre peut être placée à l\'extérieur du [Arch Mur](Arch_Wall/fr.md); tant que l\'élément est parallèle à ce mur, vous devriez pouvoir corriger la position manuellement.

## Ouvertures des portes 

10\. Dans l\'arborescence, sélectionnez `Sketch` sous-jacent à `Door` et appuyez sur **Espace** ou modifiez la propriété {{PropertyView/fr|Visibility}} en `True`

11\. Double-cliquez sur `Door` dans l\'arborescence pour commencer à l\'éditer.

:   11.1.. Dans le cadre `Window elements`, il y a deux volets, `Wires` et `Components`.
:   
    **Remarque:**avec un simple préréglage de porte, il y a deux fils, `Wire0` et `Wire1`, et deux composants, `OuterFrame` et `Door`. Une [Arch Porte](Arch_Door/fr.md) conçue sur mesure peut avoir plus de fils et de composants.





:   11.2. Cliquez sur `Door`, puis sur le bouton **Edition**. Cela montre les propriétés du composant `Door` comme par exemple `Name`, `Type`, `Wires`, `Thickness`, `Offset`, `Hinge` et `Opening mode`.
:   11.3. Dans la vue 3D, sélectionnez une seule arête verticale dans l\'esquisse visible de la porte, puis cliquez sur le bouton **Obtenir l'arête sélectionnée**. Le bouton doit devenir un nom d\'arête, par exemple **Edge8**.
:   11.4. Changez le `Opening mode` en **Arc 90**, ou toute autre option.
:   11.5. Cliquez sur le bouton **+Create/update component** puis sur **Fermer** pour terminer la modification de la porte. L\'esquisse peut redevenir masquée.

![](images/05_T01_window_edit.png ) *align=center|Dialogue pour modifier une fenêtre ou une porte*

![](images/06_T01_window_edit_component.png ) *align=center|Dialogue pour éditer les éléments qui composent une fenêtre ou une porte*

<img alt="" src=images/06.1_T01_window_edit_wire_door_front.png  style="width:600px;"> 
*align=center|Bord vertical de l'esquisse choisie comme charnière pour une porte*

12\. Sélectionnez `Door` et donnez à la propriété {{PropertyData/fr|Opening}} une valeur de 45. Le panneau plein de la porte doit s\'ouvrir vers l\'intérieur du bâtiment.

13\. Sélectionnez `Door` et changez la propriété {{PropertyData/fr|Symbol Elevation}} en `True`; le bout du fil créé indique quel côté de la porte s\'ouvre; il est plus facile de voir si la vue est en [vue de face](Std_ViewFront/fr.md). Changez la propriété {{PropertyData/fr|Symbol Plan}} en `True`; un arc de cercle devrait indiquer l\'étendue de l\'ouverture de la porte; il est plus facile de voir si la vue est en [vue de dessus](Std_ViewTop/fr.md).

14\. Répétez les étapes avec `Door001` et le `Sketch001` sous-jacent pour ouvrir la porte à 75 degrés vers l\'intérieur du bâtiment. Activez également les symboles d\'élévation et de plan.

![](images/07_T01_window_property_view.png ) *align=center|Vue des propriétés de la porte pour modifier la valeur d'ouverture, l'élévation du symbole, le plan du symbole et d'autres options*

<img alt="" src=images/08_T01_window_symbol_elevation.png  style="width:600px;"> 
*align=center|Porte avec symbole d'élévation d'ouverture, vue de face*

<img alt="" src=images/09_T01_window_symbol_plan.png  style="width:600px;"> 
*align=center|Porte avec symbole de plan, vue de dessus*

## Ouvertures des fenêtres 

10\. Dans l\'arborescence, sélectionnez `Sketch002` sous-jacent à `Window` et appuyez sur **Espace** ou modifiez la propriété {{PropertyView/fr|Visibility}} en `True`.

11\. Double-cliquez sur `Window` dans l\'arborescence pour commencer à l\'éditer.

:   16.1. Cliquez sur le composant `InnerFrame`, puis sur le bouton **Edition**.





:   16.2. Dans la vue 3D, sélectionnez une seule arête verticale de `Sketch002`. Les fils représentant `OuterFrame` et `InnerFrame` sont très proches l\'un de l\'autre, donc [zoomer avant](Std_ViewZoomIn/fr.md) aussi près que possible de l\'esquisse pour sélectionner le fil approprié. Cliquez ensuite sur le bouton **Get selected edge**. Le bouton doit devenir un nom d\'arête, par exemple **Edge12**.
:   
    **Remarque:**lorsqu\'il y a beaucoup de solides à l\'écran qu\'il devient difficile de sélectionner une seule arête, passez en [mode filaire](Std_DrawStyle/fr#Filaire.md) pour supprimer les faces de ces objets solides et ne voir que les fils, bords et contours.





:   16.3. Remplacez `Opening mode` par `Arc 90 inv`, ou toute autre option.

12\. Sélectionnez `Window` et donnez à la propriété {{PropertyData/fr|Opening}} une valeur de 45. Le cadre intérieur contenant le verre transparent doit s\'ouvrir vers l\'intérieur du bâtiment.

13\. Sélectionnez `Window` et changez la propriété {{PropertyData/fr|Symbol Elevation}} en `True`; le bout du fil créé indique quel côté de la fenêtre s\'ouvre; il est plus facile de voir si la vue est en [vue de gauche](Std_ViewLeft/fr.md). Changez la propriété {{PropertyData/fr|Symbol Plan}} en `True`; un arc de cercle devrait indiquer l\'étendue de l\'ouverture de la fenêtre; il est plus facile de voir si la vue est en [vue de dessus](Std_ViewTop/fr.md).

19\. Répétez les étapes avec `Window001` et le sous-jacent `Sketch003` pour ouvrir la fenêtre à 75 degrés. Affichez également les symboles d\'élévation et de plan. Dans ce cas, ne choisissez pas un fil vertical du `InnerFrame` comme charnière, mais choisissez le fil horizontal supérieur. Cela signifie que cette fenêtre s\'ouvrira différemment de l\'autre fenêtre. Le symbole d\'élévation sera mieux vu à partir d\'une [vue du côté droit](Std_View_Menu/fr.md). Le symbole du plan sera mieux vu de la [vue de face](Std_ViewFront/fr.md); cependant, puisque le mur obstrue la vue, vous pouvez changer sa {{PropertyView/fr|Transparency}} en une valeur telle que 85 pour voir à travers; vous pouvez également changer son {{PropertyView/fr|Display Mode}} en `Wireframe` pour n\'afficher que ses bords. <img alt="" src=images/06.2_T01_window_edit_wire_side_right.png  style="width:600px;"> 
*align=center|Bord vertical de l'esquisse choisie comme charnière pour une fenêtre*

<img alt="" src=images/10_T01_window_all_symbol_axonometric.png  style="width:600px;"> 
*align=center|Symboles d'élévation et de plan pour tous les éléments, vue axonométrique*

<img alt="" src=images/11_T01_window_all_symbol_top.png  style="width:600px;"> 
*align=center|Symboles d'élévation et de plan pour tous les éléments, vue de dessus*

## Réalisation d\'un plan d\'étage du bâtiment 

20\. Toujours dans l\'[atelier Arch](Arch_Workbench/fr.md), sélectionnez tous les composants de l\'arborescence, les [Arch Murs](Arch_Wall/fr.md), les deux [Arch Fenêtres](Arch_Window/fr.md) et les deux [Arch Portes](Arch_Door/fr.md), puis utilisez l\'outil [Arch Plan de section](Arch_SectionPlane/fr.md) pour créer un élément `Section`.


**Remarque:**

changez la propriété {{PropertyData/fr|Arrow size}} du plan de section en une valeur plus grande, par exemple, `200 mm`, afin que la direction de la section soit clairement visible dans la fenêtre 3D.

<img alt="" src=images/11.1_T01_Arch_SectionPlane_all.png  style="width:600px;"> 
*align=center|Plan de section coupant des objets solides, y compris des murs, des portes et des fenêtres*

21\. Passez à l\'[atelier TechDraw](TechDraw_Workbench/fr.md) et insérez une nouvelle page avec l\'outil [TechDraw Page par défaut](TechDraw_PageDefault/fr.md); un nouvel objet `Page` est créé et la vue passe à cette page. La page insérée est une feuille A4 standard en orientation paysage, entourée d\'un cadre de base. Utilisez l\'outil [TechDraw Page à partir d\'un modèle](TechDraw_PageTemplate/fr.md) si vous devez créer une nouvelle page en utilisant un modèle [SVG](SVG/fr.md) particulier.

22\. Sélectionnez `Section` et utilisez l\'outil [TechDraw Vue Arch](TechDraw_ArchView/fr.md) pour créer un objet `ArchView` dans la page. Très probablement, le nouvel objet ne sera pas visible dans la page car il a une très grande échelle de `1`, c\'est-à-dire 1:1. Cela signifie que chaque mètre dans la vue 3D est affiché comme mètre dans la vue de page; comme la page ne mesure que 0.297 m x 0.210 m, la plupart des éléments sont trop grands pour tenir dans cette page à leur échelle naturelle.

23\. Sélectionnez cet objet `ArchView` et changez la propriété {{PropertyData/fr|Scale}} en `0.02`, ce qui équivaut à 1:50, une échelle adaptée aux bâtiments typiques. Cela signifie que chaque mètre dans la vue 3D sera affiché comme 20 mm dans la page. L\'objet doit apparaître au centre de la page et peut être déplacé vers une meilleure position sur le côté gauche. Les deux portes doivent avoir l\'air ouvertes, mais seule la fenêtre de gauche doit avoir l\'air ouverte. La raison pour laquelle la fenêtre de droite n\'apparaît pas dans la projection est que le plan défini par `Section` ne traverse pas cette fenêtre de droite.

<img alt="Section view of the building, A4 sheet, scale 1:50" src=images/12_T01_TechDraw_window_all_symbols.png  style="width:600px;"> 
*align=center|Plan de section coupant des objets solides, y compris des murs, des portes et des fenêtres*

24\. Revenez à l\'[atelier Arch ](Arch_Workbench/fr.md). Dans l\'arborescence, sélectionnez à nouveau tous les composants et utilisez l\'outil [Arch Plan de section](Arch_SectionPlane/fr.md) pour créer un deuxième élément `Section001`.

:   24.1. Sélectionnez `Section001` et remplacez la propriété {{PropertyData/fr|Position}} par `[1.5 m, 2.0 m, 1.8 m]`. Ce deuxième plan coupe tous les objets Arch.
:   24.2. Revenez à [atelier TechDraw](TechDraw_Workbench/fr.md). Sélectionnez `Section001`, utilisez l\'outil [TechDraw Vue Arch](TechDraw_ArchView/fr.md) pour créer `ArchView001` et définissez {{PropertyData/fr|Scale}} sur `0.02`. La nouvelle vue de la page TechDraw montre maintenant toutes les ouvertures dans les [Arch Murs](Arch_Wall/fr.md) produites par les portes et les fenêtres.


**Remarque:**

définissez {{PropertyData/fr|All On}} sur `True` pour les objets [TechDraw Vue architecturale](TechDraw_ArchView/fr.md) afin que tous les éléments coupés par le plan soient visibles sur la page, quel que soit leur état de visibilité dans la fenêtre 3D. L\'option {{PropertyData/fr|Show Fill}} peut également être définie sur `True` pour dessiner une nuance sur les solides qui ont été coupés par le plan de coupe.

<img alt="" src=images/13_T01_TechDraw_window_all_symbols_higher.png  style="width:600px;"> 
*align=center|Vue en section du bâtiment, avec un deuxième plan coupé, feuille A4, échelle 1:50*

## Faire une projection d\'élévation du bâtiment 

25\. Revenez à l\'[atelier Arch](Arch_Workbench/fr.md). Dans l\'arborescence, sélectionnez tous les composants, le [Arch Mur](Arch_Wall/fr.md), les deux [Arch Fenêtre](Arch_Window/fr.md) s et les deux [Arch Portes](Arch_Door/fr.md), puis utilisez l\'outil [Arch Plan de section](Arch_SectionPlane/fr.md) pour créer un troisième élément `Section002`.

:   25.1. Faites pivoter `Section002`, de sorte qu\'il coupe verticalement à travers le bâtiment. Modifiez les propriétés {{PropertyData/fr|Axis}} en `[1, 0, 0]` et **Angle** en `90`.
:   25.2. Remplacez {{PropertyData/fr|Position}} par `[1.5 m, -1 m, 1.5 m]`, de sorte que le plan soit devant le bâtiment.

<img alt="" src=images/14.1_T01_Arch_SectionPlane_three.png  style="width:600px;"> 
*align=center|Plans de section qui coupent ou regardent le bâtiment et les objets solides*

26\. Revenez à l\'[atelier TechDraw](TechDraw_Workbench/fr.md) et utilisez l\'outil [TechDraw Vue Arch](TechDraw_ArchView/fr.md) sur `Section002`; n\'oubliez pas d\'ajuster l\'échelle à `0.02` (1:50). Remplacez {{PropertyData/fr|Rotation}} par `-90` pour corriger l\'apparence des projections. Disposez `ArchView002` à côté des autres vues de la page. Cette troisième projection regarde le bâtiment de face.

<img alt="" src=images/14_T01_TechDraw_window_all_symbols_elevation.png  style="width:600px;"> 
*align=center|Vue de section du bâtiment, deux vues de dessus et une vue d'élévation, feuille A4, échelle 1:50*

## Interaction Arch et TechDraw 

Au moment de la rédaction de ce document (FreeCAD 0.18, novembre 2018), l\'[atelier TechDraw](TechDraw_Workbench/fr.md) ne peut afficher dans ses pages que ce que l\'[atelier Arch](Arch_Workbench/fr.md) exporte en [SVG](SVG/fr.md). Cela signifie que l\'apparence des éléments inclus dans l\'outil [Arch Plan de section](Arch_SectionPlane/fr.md) et affichés par l\'outil [TechDraw Vue Arch](TechDraw_ArchView/fr.md) est contrôlée par l\'[atelier Arch](Arch_Workbench/fr.md).

l\'[atelier TechDraw](TechDraw_Workbench/fr.md) n\'a qu\'un contrôle minimal sur la façon dont il affiche ces objets [Arch Plan de section](Arch_SectionPlane/fr.md) (`ArchView`). Par conséquent, les rapports de bogue et les demandes de fonctionnalités liées à l\'affichage des éléments Arch doivent être déposés auprès des deux ateliers.

Une interaction plus étroite entre les ateliers est prévue pour les futures versions de FreeCAD. Dans ces versions, on s\'attend à ce que les problèmes de longue date soient résolus, tels que le contrôle des caractéristiques des lignes et des faces (largeur de ligne, couleur de ligne, couleur de face, motifs de hachures, etc\...).


{{Tutorials navi

}}   {{TechDraw Tools navi}}

---
[documentation index](../README.md) > [Arch](Category:Arch.md) > Tutorial for open windows/fr
