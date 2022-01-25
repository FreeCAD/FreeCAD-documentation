# Draft Snap/fr
{{TOCright}}

## Description

Dans l\'<img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [atelier Draft](Draft_Workbench/fr.md) et l\'<img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [atelier Arch](Arch_Workbench/fr.md), vous pouvez créer une géométrie en sélectionnant des points dans la [Vue 3D](3D_view/fr.md) ou en saisissant des coordonnées dans le [Panneau des tâches](Task_panel/fr.md) des commandes. Une autre façon de sélectionner des points est l\'aimantation. L\'aimantation permet de sélectionner des points géométriques exacts sur des objets existants ou définis par ces objets ou la grille. Vous pouvez par exemple vous aimanter à l\'extrémité d\'une ligne, au centre d\'un cercle ou à l\'intersection de deux bords.

L\'aimantation est disponible avec la plupart des commandes de [Draft](Draft_Workbench/fr.md) et [Arch](Arch_Workbench/fr.md).

![](images/Draft_Snap_Endpoint_example.png ) 
*Aimantation au point d'extrémité d'une arête*

## Outils d\'aimantaion 

Ces outils sont disponibles dans la barre d\'outils Draft Aimantation et dans le [Draft widget aimantation](Draft_snap_widget/fr.md).

Remarquez que les bords circulaires ne doivent pas nécessairement être des cercles complets.

-   <img alt="" src=images/Draft_Snap_Lock.svg  style="width:32px;"> [Aimantation Verrouiller](Draft_Snap_Lock/fr.md) : active ou désactive l\'aimantation de manière globale.

-   <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:32px;"> [Aimantation Terminaison](Draft_Snap_Endpoint/fr.md): aimante aux extrémités des segments.

-   <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:32px;"> [Aimantation Milieu](Draft_Snap_Midpoint/fr.md) : aimante au point milieu des segments.

-   <img alt="" src=images/Draft_Snap_Center.svg  style="width:32px;"> [Aimantation Centre](Draft_Snap_Center/fr.md) : aimante au point central des faces et des arêtes circulaires et au point {{PropertyData/fr|Placement}} de [Draft Proxy de plan de travail](Draft_WorkingPlaneProxy/fr.md) et [Arch Partie de bâtiment](Arch_BuildingPart/fr.md).

-   <img alt="" src=images/Draft_Snap_Angle.svg  style="width:32px;"> [Aimantation Angle](Draft_Snap_Angle/fr.md) : aimante aux points cardinaux spéciaux des bords circulaires, aux multiples de 30° et 45°.

-   <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:32px;"> [Aimantation Intersection](Draft_Snap_Intersection/fr.md): aimante à l\'intersection de deux bords.

-   <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width:32px;"> [Aimantation Perpendiculaire](Draft_Snap_Perpendicular/fr.md) : aimante au point perpendiculaire sur les bords.

-   <img alt="" src=images/Draft_Snap_Extension.svg  style="width:32px;"> [Aimantation Extension](Draft_Snap_Extension/fr.md) : aimante à une ligne imaginaire qui s\'étend au-delà des extrémités des bords droits.

-   <img alt="" src=images/Draft_Snap_Parallel.svg  style="width:32px;"> [Aimantation Parallèle](Draft_Snap_Parallel/fr.md) : aimante à une ligne imaginaire parallèle aux bords droits.

-   <img alt="" src=images/Draft_Snap_Special.svg  style="width:32px;"> [Aimantation Spécial](Draft_Snap_Special/fr.md) : aimante à des points spéciaux définis par l\'objet.

-   <img alt="" src=images/Draft_Snap_Near.svg  style="width:32px;"> [Aimantation Le plus proche](Draft_Snap_Near/fr.md) : aimante au point le plus proche sur les faces ou les bords.

-   <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:32px;"> [Aimantation Orthogonal](Draft_Snap_Ortho/fr.md) : aimante sur des lignes imaginaires qui croisent le point précédent à 0°, 45°, 90° et 135°.

-   <img alt="" src=images/Draft_Snap_Grid.svg  style="width:32px;"> [Aimantation Grille](Draft_Snap_Grid/fr.md) : aimante aux intersections des lignes de la grille.

-   <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:32px;"> [Aimantation Plan de travail](Draft_Snap_WorkingPlane/fr.md) : projette le point d\'aimantation sur le [plan de travail](Draft_SelectPlane/fr.md) en cours.

-   <img alt="" src=images/Draft_Snap_Dimensions.svg  style="width:32px;"> [Aimantation Dimensions](Draft_Snap_Dimensions/fr.md) : montre les dimensions X et Y temporaires.

-   <img alt="" src=images/Draft_ToggleGrid.svg  style="width:32px;"> [Basculer la grille](Draft_ToggleGrid/fr.md) : active ou désactive la grille.

## Aimantation avancée 

-   Des points d\'aimantation supplémentaires peuvent être obtenus en combinant deux options d\'aimantation. Par exemple, en combinant [Draft Aimantation Orthogonal](Draft_Snap_Ortho/fr.md) et [Draft Aimantation Extension](Draft_Snap_Extension/fr.md), vous obtiendrez un point d\'accrochage à l\'intersection de leurs lignes imaginaires.
-   L\'aimantation peut être combinée avec des [constraintes](Draft_Constrain/fr.md).
-   Appuyez sur **Q** pour insérer un \"point d\'aimantation\" à l\'emplacement en cours du curseur. Vous pouvez vous aimanter aux axes orthogonaux des points d\'arrêt et aux intersections de ces axes. Si l\'option [Draft Aimantation Milieu](Draft_Snap_Midpoint/fr.md) est active, vous pouvez également vous fixer sur le point milieu entre deux points d\'arrêt.
-   Appuyez une ou plusieurs fois sur **** pour effectuer une aimantation sur un objet qui est masqué par d\'autres éléments géométriques. Cette opération est appelée \"cycle d\'aimantation\". Notez que vous devez déplacer légèrement le curseur dans la [Vue 3D](3D_view/fr.md) après avoir appuyé sur la touche.

![](images/Draft_Snap_example_cycling_1.png ) 
*Cycle d'aimantation 1 : le rectangle rouge a été créé en premier, il a donc la priorité d'aimantation. Sans le cycle d'aimantation, vous ne pouvez pas aimanter le rectangle vert, qui est recouvert par le rectangle rouge.*

![](images/Draft_Snap_example_cycling_2.png ) 
*Cycle d'aimantation 2 : après avoir utilisé la touche cycle d'aimantation une fois, le rectangle vert reçoit la priorité d'aimantation. L'aimantation au point milieu du bord vert superposé est maintenant possible.*

## Remarques

-   Plusieurs options d\'aimantation peuvent être actives en même temps, mais il est conseillé de n\'activer que celles dont vous avez réellement besoin. En activer trop peut ralentir les choses.
-   Ce n\'est pas une bonne idée d\'avoir [Draft Aimantation Le plus proche](Draft_Snap_Near/fr.md) actif en permanence car il est prioritaire sur de nombreuses autres options d\'aimantation.

## Préférences

Voir aussi : [Réglage des préférences](Preferences_Editor/fr.md) et [Draft Préférences](Draft_Preferences/fr.md).

Remarquez qu\'après avoir modifié certaines préférences, vous devez redémarrer FreeCAD.

-   Lorsqu\'une commande [Draft](Draft_Workbench/fr.md) ou [Arch](Arch_Workbench/fr.md) nécessitant la saisie de points est active, la distance maximale à laquelle [Draft Aimantation Grille](Draft_Snap_Grid/fr.md) détecte les intersections des lignes de la grille peut être modifiée à la volée en appuyant sur **[** (touche d\'augmentation) ou **]** (touche de diminution). Ce réglage est enregistré : **Outils → Modifier les paramètres... → BaseApp → Preferences → Mod → Draft → snapRange**. Elle peut également être modifiée dans le panneau des tâches de la commande [Draft Plan de travail](Draft_SelectPlane/fr.md).
-   Pour effectuer une aimantation uniquement lorsque la touche **Snap mod** est maintenue enfoncée :
    -   Désélectionner : **Edition → Préférences... → Draft → Grille et aimantation → Accrochage → Toujours aimanter (désactiver le mode d'aimantation)**.
    -   La touche **Snap mod** par défaut, **Ctrl**, peut être modifiée : **Edition → Préférences... → Draft → Grille et aimantation → Accrochage → Mode d'accrochage**.
-   Pour afficher la barre d\'outils Aimantation de Draft uniquement lorsqu\'une commande est active :
    -   Sélectionnez : **Edition → Préférences... → Draft → Grille et aimantation → Accrochage → Afficher la barre d'outils d'accrochage**.
    -   Sélectionnez : **Edition → Préférences... → Draft → Grille et aimantation → Accrochage → Masquer la barre d'outils d'accrochage après emploi**.
-   Les symboles d\'aimantation peuvent être modifiés : **Edition → Préférences... → Draft → Paramètres visuels → Paramètres visuels → Style des symboles d'aimantation**.
-   La couleur des symboles d\'accrochage et les dimensions de [Draft Aimantation Dimensions](Draft_Snap_Dimensions/fr.md) peuvent être modifiées : **Edition → Préférences... → Draft → Paramètres visuels → Paramètres visuels → Couleur**.
-   Les raccourcis clavier à un seul caractère mentionnés peuvent être modifiés : **Edition → Préférences... → Draft → Paramètres de l'interface utilisateur → Raccourcis des commandes**.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap/fr
