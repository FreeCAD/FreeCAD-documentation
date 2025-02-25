---
 GuiCommand:
   Name: Draft Edit
   Name/fr: Draft Éditer
   MenuLocation: Modification , Éditer
   Workbenches: Draft_Workbench/fr
   Shortcut: **D** **E**
   SeeAlso: Std_Edit/fr
---

# Draft Edit/fr

## Description

La commande <img alt="" src=images/Draft_Edit.svg  style="width:24px;"> **Draft Éditer** place les objets sélectionnés en mode d\'édition. Dans ce mode, les propriétés des objets peuvent être modifiées graphiquement. En général, les nœuds peuvent être déplacés et, dans certains cas, les options du menu contextuel peuvent être sélectionnées. La commande peut gérer la plupart des objets Draft, mais aussi certains autres objets. Voir [Objets pris en charge](#Objets_pris_en_charge.md). Les objets Draft pris en charge peuvent aussi être mis en mode Draft Éditer avec la commande [Std Mode édition](Std_Edit/fr.md).

![](images/Draft_Edit_example.png ) 
*4 objets en mode Draft Éditer : une Draft Polyligne (rouge), un Draft Arc (noir), une Draft B-spline (vert) et une Draft Courbe de Bézier (magenta).*



## Utilisation

Voir aussi : [Draft Aimantation](Draft_Snap/fr.md) et [Draft Contrainte](Draft_Constrain/fr.md).

1.  Sélectionnez un ou plusieurs objets. Notez que bien que plusieurs objets puissent être en mode Draft Édition, les objets ne peuvent être édités qu\'un par un.
2.  Il existe plusieurs façons de lancer la commande :
    -   Si vous n\'avez pas encore sélectionné d\'objet : double-cliquez sur un objet dans la [vue en arborescence](Tree_view/fr.md). Cela ne fonctionne que pour les objets Draft pris en charge.
    -   Appuyez sur le bouton **<img src="images/Draft_Edit.svg" width=16px> [Éditer](Draft_Edit/fr.md)**.
    -   Sélectionnez l\'option **Modification → <img src="images/Draft_Edit.svg" width=16px> Éditer** dans le menu.
    -   Utilisez le raccourci clavier : **D** puis **E**.
    -   Pour un seul objet : sélectionnez l\'option **Edit** dans le menu contextuel de la [vue en arborescence](Tree_view/fr.md). Cela ne fonctionne que pour les objets Draft pris en charge. {{Version/fr|0.21}}
3.  Si vous n\'avez pas encore sélectionné d\'objet : sélectionnez un objet dans la [vue 3D](3D_view/fr.md).
4.  Les objets sélectionnés sont marqués par des nœuds temporaires et le [panneau principal des tâches](#Panneau_principal_des_t.C3.A2ches.md) s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
5.  En option, utiliser un menu contextuel de nœud ou de bord. Ces menus contextuels ne sont disponibles que pour certains objets Draft. Voir [Objets pris en charge](#Objets_pris_en_charge.md) pour plus d\'informations.
    -   Effectuez l\'une des opérations suivantes :
        -   Sur tous les systèmes d\'exploitation : maintenez la touche **E** enfoncée et cliquez sur le nœud ou le bord. Pour utiliser **E**, vous devrez peut-être cliquer une fois dans la [vue 3D](3D_view/fr.md) pour vous assurer qu\'elle a pris en compte le sujet en question.
        -   Sous Windows : maintenez la touche **Alt** enfoncée et cliquez sur le nœud ou l\'arête.
        -   Sous Linux : maintenez enfoncé **Shift**+**Alt**, **Ctrl**+**Alt** ou **Alt** et cliquez sur le nœud ou l\'arête.
        -   Sous macOS : maintenez la touche **Option** enfoncée et cliquez sur le nœud ou l\'arête.
    -   Sélectionnez une option dans le menu contextuel.
    -   Si l\'option sélectionnée nécessite la saisie d\'un point :
        -   Le [panneau des tâches des nœuds](#Modifier_les_n.C5.93uds_par_le_panneau_des_t.C3.A2ches.md) s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
        -   Choisissez un point dans la [vue 3D](3D_view/fr.md) ou rentrez les coordonnées et appuyez sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrer un point**.
6.  Déplacez un nœud de manière facultative :
    -   Cliquez sur le nœud dans la [vue 3D](3D_view/fr.md).
    -   Le [panneau des tâches du nœud](#Modifier_les_n.C5.93uds_par_le_panneau_des_t.C3.A2ches.md) s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
    -   Choisissez un point dans la [vue 3D](3D_view/fr.md) ou rentrez les coordonnées et appuyez sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrer un point**.
    -   Le résultat dépend de l\'objet et du nœud sélectionné.
7.  Appuyez sur **Échap** ou sur le bouton **Fermer** (le bouton en haut du panneau des tâches, sans l\'image) pour terminer la commande.

## Options

Les raccourcis clavier à caractère unique disponibles dans le panneau des tâches peuvent être modifiés. Voir [Draft Préférences](Draft_Preferences/fr.md). Les raccourcis mentionnés ici sont les raccourcis par défaut.



### Panneau principal des tâches 

-   Appuyez sur **Échap** ou sur le bouton **Fermer** pour terminer la commande.



### Modifier les nœuds par le panneau des tâches 

-   Pour saisir manuellement des coordonnées, entrez les valeurs X, Y et Z et appuyez sur **Entrée** après chacune. Vous pouvez aussi appuyer sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrer un point** lorsque vous avez les valeurs souhaitées. Il est conseillé de déplacer le pointeur hors de la [vue 3D](3D_view/fr.md) avant de saisir les coordonnées.
-   Pour utiliser des coordonnées polaires, entrez une valeur pour **Longueur** et une valeur pour **Angle**, et appuyez sur **Entrée** après chacune d\'elles.
-   Cochez la case **Angle** pour contraindre le pointeur à l\'angle spécifié.
-   Appuyez sur **R** ou cliquez sur la case à cocher **Relatif** pour activer le mode relatif. Si le mode relatif est activé, les coordonnées du point sélectionné sont relatives au point d\'origine, sinon elles sont relatives à l\'origine du système de coordonnées. {{Version/fr|1.0}}
-   Appuyez sur **G** ou cliquez sur la case **Global** pour basculer en mode global. Si le mode global est activé, les coordonnées sont relatives au système de coordonnées global, sinon elles sont relatives au système de coordonnées du [plan de travail](Draft_SelectPlane/fr.md).
-   Appuyez sur **S** pour activer ou désactiver [Draft Aimantation](Draft_Snap/fr.md).



## Objets pris en charge 



### <img alt="" src=images/Draft_Line.svg  style="width:24px;"> [Draft Ligne](Draft_Line/fr.md) et <img alt="" src=images/Draft_Wire.svg  style="width:24px;"> [Draft Polyligne](Draft_Wire/fr.md) 

-   Si le nœud de début ou de fin d\'une polyligne ouverte est déplacé de manière à coïncider, la polyligne est fermée.
-   Menu contextuel du noeud : {{Value|Supprimer un point}}. Il doit rester au moins deux points.
-   Menu contextuel de l\'arête : {{Value|Ajouter un point}}, {{Value|Ouvrir une polyligne}}/{{Value|Fermer une polyligne}} ({{Version/fr|0.21}}) et {{Value|Inverser une polyligne}}.



### <img alt="" src=images/Draft_Arc.svg  style="width:24px;"> [Draft Arc](Draft_Arc/fr.md) et <img alt="" src=images/Draft_Arc_3Points.svg  style="width:24px;"> [Draft Arc par 3 points](Draft_Arc_3Points/fr.md) 

-   Menu contextuel du nœud central : {{Value|Déplacer l'arc}}.
-   Menu contextuel du nœud de départ : {{Value|Définir le premier angle}}.
-   Menu contextuel du nœud final : {{Value|Définir le dernier angle}}.
-   Menu contextuel du nœud central : {{Value|Définir le rayon}}.
-   Menu contextuel du bord : {{Value|Inverser l'arc}}.



### <img alt="" src=images/Draft_Circle.svg  style="width:24px;"> [Draft Cercle](Draft_Circle/fr.md) 

-   Aucun menu contextuel pour cet objet.



### <img alt="" src=images/Draft_Ellipse.svg  style="width:24px;"> [Draft Ellipse](Draft_Ellipse/fr.md) 

-   Aucun menu contextuel pour cet objet.



### <img alt="" src=images/Draft_Rectangle.svg  style="width:24px;"> [Draft Rectangle](Draft_Rectangle/fr.md) 

-   Aucun menu contextuel pour cet objet.



### <img alt="" src=images/Draft_Polygon.svg  style="width:24px;"> [Draft Polygone](Draft_Polygon/fr.md) 

-   Aucun menu contextuel pour cet objet.



### <img alt="" src=images/Draft_BSpline.svg  style="width:24px;"> [Draft B-spline](Draft_BSpline/fr.md) 

-   Si le nœud de début ou de fin d\'une spline ouverte est déplacé de façon à ce qu\'ils coïncident, la spline est fermée.
-   Menu contextuel du nœud : {{Value|Supprimer un point}}. Pour une spline ouverte, il doit rester au moins deux points. Pour une spline fermée, le nombre minimum de points est de trois.
-   Menu contextuel de l\'arête : {{Value|Ajouter un point}}, {{Value|Ouvrir une polyligne}}/{{Value|Fermer une polyligne}} ({{Version/fr|0.21}}) et {{Value|Inverser une spline}} ({{Version/fr|0.21}}).



### <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:24px;"> [Draft Courbe de Bézier cubique](Draft_CubicBezCurve/fr.md) et <img alt="" src=images/Draft_BezCurve.svg  style="width:24px;"> [Draft Courbe de Bézier](Draft_BezCurve/fr.md) 

-   Si le nœud de début ou de fin d\'une courbe ouverte est déplacé de façon à ce qu\'ils coïncident, la courbe est fermée.
-   Menu contextuel du nœud : {{Value|Supprimer un point}}, {{Value|Rendre aigu}}, {{Value|Rendre tangent}} et {{Value|Rendre symétrique}}.
-   Menu contextuel de l\'arête : {{Value|Ajouter un point}}, {{Value|Ouvrir une polyligne}}/{{Value|Fermer une polyligne}} ({{Version/fr|0.21}}) et {{Value|Inverser la courbe}} ({{Version/fr|0.21}}).



### <img alt="" src=images/Draft_Dimension.svg  style="width:24px;"> [Draft Dimension](Draft_Dimension/fr.md) 

-   Les dimensions angulaires ne peuvent pas être éditées.
-   Les nœuds de début et de fin des dimensions paramétriques ne peuvent pas être déplacés.
-   Pas de menu contextuel pour cet objet.



### <img alt="" src=images/Arch_Wall.svg  style="width:24px;"> [Arch Mur](Arch_Wall/fr.md) 

-   Un seul noeud permettant de contrôler la hauteur du mur est affiché au-dessus de la **Placement** du mur.
-   Pas de menu contextuel pour cet objet.



### <img alt="" src=images/Arch_Structure.svg  style="width:24px;"> [Arch Structure](Arch_Structure/fr.md) 

-   Aucun menu contextuel pour cet objet.



### <img alt="" src=images/Arch_Window.svg  style="width:24px;"> [Arch Fenêtre](Arch_Window/fr.md) 

-   Aucun menu contextuel pour cet objet.



### <img alt="" src=images/Arch_Space.svg  style="width:24px;"> [Arch Espace](Arch_Space/fr.md) 

-   Aucun menu contextuel pour cet objet.



### <img alt="" src=images/Arch_Panel_Cut.svg  style="width:24px;"> [Arch Découpe de panneaux](Arch_Panel_Cut/fr.md) 

-   Aucun menu contextuel pour cet objet.



### <img alt="" src=images/Arch_Panel_Sheet.svg  style="width:24px;"> [Arch Panneau de feuille](Arch_Panel_Sheet/fr.md) 

-   Aucun menu contextuel pour cet objet.



### <img alt="" src=images/Part_Box.svg  style="width:24px;"> [Part Cube](Part_Box/fr.md) 

-   Aucun menu contextuel pour cet objet.



### <img alt="" src=images/Part_Cylinder.svg  style="width:24px;"> [Part Cylindre](Part_Cylinder/fr.md) 

-   Aucun menu contextuel pour cet objet.



### <img alt="" src=images/Part_Sphere.svg  style="width:24px;"> [Part Sphère](Part_Sphere/fr.md) 

-   Aucun menu contextuel pour cet objet.



### <img alt="" src=images/Part_Cone.svg  style="width:24px;"> [Part Cône](Part_Cone/fr.md) 

-   Aucun menu contextuel pour cet objet.



### <img alt="" src=images/Part_Line.svg  style="width:24px;"> [Part Ligne](Part_Line/fr.md) 

-   Aucun menu contextuel pour cet objet.



### <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Sketcher Esquisse](Sketcher_NewSketch/fr.md) 

-   Seules les esquisses qui contiennent une seule ligne non contrainte peuvent être éditées.
-   Pas de menus contextuels pour cet objet.



## Préférences

Voir aussi : [Réglage des préférences](Preferences_Editor/fr.md) et [Draft Préférences](Draft_Preferences/fr.md).

-   La couleur des nœuds temporaires est la même que celle des symboles d\'aimantation. Cette couleur peut être modifiée dans les préférences : **Édition → Préférences... → Draft → Grille et aimantation → Couleur des symboles d'aimantation**. Notez que cette couleur n\'est pas utilisée pour les nœuds temporaires affichés pour les [Draft Courbes de Bézier](Draft_BezCurve/fr.md). Ces noeuds utilisent la **Couleur de ligne** de la courbe à la place.
-   La taille des nœuds dépend de : **Édition → Préférences... → Affichage → Vue 3D → Taille des marqueurs**. {{Version/fr|1.0}}



## Script

Voir aussi : [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) et [FreeCAD Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

Il n\'existe pas de méthode Python pour les objets Draft Edition. Pour émuler les résultats de la commande, les propriétés géométriques des objets doivent être modifiées.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Edit/fr
