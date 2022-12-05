# Manual:Navigating in the 3D view/fr
{{Manual:TOC/fr}}

### Un mot sur l\'espace 3D 

Si c\'est votre premier contact avec une application 3D, vous devez d\'abord saisir certains concepts. Dans le cas contraire, vous pouvez sauter cette section sans problème.

L\'espace FreeCAD 3D est un espace euclidien ([Espace Euclidien](https://fr.wikipedia.org/wiki/Espace_euclidien)). Il a un point d\'origine et trois axes: X, Y et Z. Si vous regardez votre scène d\'en haut, de manière conventionnelle, l\'axe X pointe vers la droite, l'axe Y vers l\'arrière, et l\'axe Z vers le haut. Dans le coin inférieur droit de la vue FreeCAD, vous pouvez toujours voir d\'où vous regardez la scène :

![](images/Axes_orientation.png )

Chaque point de chaque objet de cet espace peut être repéré par ses coordonnées (x, y, z). Par exemple, un point avec des coordonnées (2, 3, 1) se situera à 2 unités sur l\'axe X, 3 unités sur l\'axe Y et 1 unité sur l\'axe Z :

![](images/3dspace_coordinates.jpg )

Vous pouvez regarder cette scène sous n\'importe quel angle comme si vous teniez une caméra. Cette caméra peut être déplacée à gauche, à droite, en haut et en bas (panoramique), tourner autour de ce que vous regardez (rotation) et vous rapprocher ou vous éloigner de la scène (zoom).

### La vue 3D FreeCAD 

#### Navigation à la souris 

La navigation dans la [vue 3D](3D_view/fr.md) FreeCAD peut se faire avec une souris, un périphérique Navigateur spacial, le clavier, un pavé tactile ou une combinaison de ceux-ci. FreeCAD propose plusieurs [modes de navigation](Mouse_navigation/fr.md) qui déterminent comment les trois opérations de manipulation de la vue de base (panoramique, rotation et zoom) sont effectuées, ainsi que la façon de sélectionner des objets sur l\'écran. Les modes de navigation sont accessibles à partir de l\'écran Préférences ou directement en cliquant avec le bouton droit n\'importe où sur la [vue 3D](3D_view/fr.md):

![](images/FreeCAD-v0-18-NavigationModePopup.png )

Chacun de ces modes attribue différentes actions aux boutons de la souris ou boutons de souris + combinaison de touches du clavier ou des fonctions à la souris à ces quatre opérations. Le tableau suivant montre les principaux modes disponibles :

++++++
| Mode             | Panoramique                                                                                                                                                                                                                                                                            | Rotation                                                                                                                                                                                                                                                                                   | Zoom                                                                                                                                                                                                                                                                                    | Sélection                                                                                                                                           |
+==================+========================================================================================================================================================================================================================================================================================+============================================================================================================================================================================================================================================================================================+=========================================================================================================================================================================================================================================================================================+=====================================================================================================================================================+
| OpenInventor     | ![Clic sur le bouton central de la souris](images/Pan-mouse.svg )                                                                                                                                                                                    | ![Clic sur le bouton gauche de la souris](images/Select-mouse.svg )                                                                                                                                                                                       | ![Rotation du bouton central de la souris](images/Zoom-mouse.svg )                                                                                                                                                                                    | Maintenir **Ctrl** + glisser ![Clic sur le bouton gauche de la souris](images/Select-mouse.svg ) |
++++++
| CAD **(défaut)** | ![Clic sur le bouton central de la souris](images/Pan-mouse.svg ) ou ![Clic sur le bouton droit de la souris + touche CTRL enfoncée](images/Pan-mouse-CTRL.svg )                              | ![Enfoncer le bouton central puis gauche de la souris](images/Rotate-mouse.svg ) ou ![Clic sur le bouton droit de la souris + touche SHIFT enfoncée](images/Rotate-mouse-SHIFT.svg ) | ![Rootation du bouton central de la souris](images/Zoom-mouse.svg ) ou ![Clic sur le bouton droit de la souris + touches CTRL + SHIFT enfoncées](images/Zoom-mouse-CTRL-SHIFT.svg ) | ![Clic sur le bouton gauche de la souris](images/Select-mouse.svg )                                                |
++++++
| Blender          | Maintenir **Shift** + glisser ![Clic sur le bouton central de la souris](images/Pan-mouse.svg ) ou ![Clic sur les boutons gauche et droit puis déplacez](images/Mouse_LMB%2BRMB.svg ) | ![Clic sur le bouton central de la souris](images/Pan-mouse.svg )                                                                                                                                                                                        | ![Rotation du bouton central de la souris](images/Zoom-mouse.svg )                                                                                                                                                                                    | ![Clic sur le bouton gauche de la souris](images/Select-mouse.svg )                                                |
++++++
| Touchpad         | Maintenir **Shift** + glisser ![Touchpad (souris) pointeur](images/Touchpad.png )                                                                                                                                                               |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                          | ![Clic sur le touchpad (souris) bouton gauche](images/Select-touchpad.png )                                   |
|                  |                                                                                                                                                                                                                                                                                        | **Alt**                                                                                                                                                                                                                                                                                | **⇞ Pg.Préc**                                                                                                                                                                                                                                                                       |                                                                                                                                                     |
|                  |                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                      |                                                                                                                                                     |
|                  |                                                                                                                                                                                                                                                                                        | \+ ![Touchpad (souris) pointeur](images/Touchpad.png )                                                                                                                                                                                                                | / **⇟ Pg.Suiv**                                                                                                                                                                                                                                                       |                                                                                                                                                     |
++++++
| Gesture          | glisser ![Clic sur le bouton droit de la souris](images/Pan-mouse-Ctrl.svg )                                                                                                                                                                           | glisser ![Clic sur le bouton gauche de la souris](images/Select-mouse.svg )                                                                                                                                                                               | ![Rotation du bouton central de la souris](images/Zoom-mouse.svg )                                                                                                                                                                                    | ![Clic sur le bouton gauche de la souris](images/Select-mouse.svg )                                                |
++++++
| OpenCascade      | ![Clic sur le bouton central de la souris](images/Pan-mouse.svg )                                                                                                                                                                                    | ![Enfoncer le bouton central puis droit de la souris](images/Rotate-mouse-MMB+RMB.svg )                                                                                                                                                       | ![Rotation dubouton central de la souris](images/Zoom-mouse.svg )                                                                                                                                                                                      | ![Clic sur le bouton gauche de la souris](images/Select-mouse.svg )                                                |
++++++

#### Navigation par le clavier 

Certaines commandes du clavier sont toujours disponibles et ce, quel que soit le mode de navigation :

-    **Ctrl**\+ {{ASCII|43}} et **Ctrl** + {{ASCII|22}} pour zoom avant et zoom arrière

-   les touches flèches {{ASCII|17}}{{ASCII|16}}{{ASCII|30}}{{ASCII|31}} pour déplacer la vue vers la gauche ou la droite et vers le haut ou le bas

-    **Shift**\+ {{ASCII|17}} et **Shift** + {{ASCII|16}} pour faire pivoter la vue de 90 degrés

-   le clavier numérique, {{ASCII|48}}{{ASCII|49}}{{ASCII|50}}{{ASCII|51}}{{ASCII|52}}{{ASCII|53}}{{ASCII|54}}, pour les sept vues standard:

<img alt="" src=images/Std_ViewIsometric.svg  style="width:24px;"> [Isometrique](Std_ViewIsometric/fr.md), <img alt="" src=images/Std_ViewFront.svg  style="width:24px;"> [Avant](Std_ViewFront/fr.md), <img alt="" src=images/Std_ViewTop.svg  style="width:24px;"> [Dessus](Std_ViewTop/fr.md), <img alt="" src=images/Std_ViewRight.svg  style="width:24px;"> [Droite](Std_ViewRight/fr.md), <img alt="" src=images/Std_ViewRear.svg  style="width:24px;"> [Arrière](Std_ViewRear/fr.md), <img alt="" src=images/Std_ViewBottom.svg  style="width:24px;"> [Dessous](Std_ViewBottom/fr.md), et <img alt="" src=images/Std_ViewLeft.svg  style="width:24px;"> [Gauche](Std_ViewLeft/fr.md)

-    **V**
    **O**mettra la vue en <img alt="" src=images/View-isometric.svg  style="width:24px;"> [mode orthographique](Std_OrthographicCamera/fr.md).

-   alors que **V****P** mettra la vue en <img alt="" src=images/View-perspective.svg  style="width:24px;"> [mode en perspective](Std_PerspectiveCamera/fr.md).

-    **Ctrl**vous permettra de sélectionner plus d\'un objet ou élément

Ces contrôles sont également disponibles dans le [menu Affichage](Std_View_Menu/fr.md) et certains dans la barre d\'outils Affichage.

#### Utilisation du cube de navigation 

Dans la configuration par défaut, un [Cube de navigation](Navigation_Cube/fr.md) se trouve dans le coin supérieur droit de l\'écran 3D. Il peut être utilisé pour faire pivoter l\'objet affiché d\'un angle défini, réinitialiser l\'affichage vers une des vues standard ou changer le mode d\'affichage.

![](images/FreeCAD-v0-18-NavCube_SelectCorner.png )

Lorsque vous utilisez le cube de navigation, un point de contrôle devient bleu clair lorsque le pointeur survole sa zone sensible. Si la zone située sous le pointeur ne change pas de couleur, le fait de cliquer dessus n\'aura aucun effet. Au moment de la rédaction de ce document (v0.18), certains problèmes d'enregistrement empêchent l'activation de toutes les parties de certains points de contrôle.

En cliquant sur une face, la vue passe à cette face. En cliquant sur un coin, vous passez à une vue avec ce coin dirigé vers vous.

En cliquant sur l\'un des quatre triangles, la vue pivotera de 45 degrés dans la direction indiquée. En cliquant sur l\'une des deux flèches incurvées en haut, la vue pivotera de 45 degrés dans la direction indiquée autour d\'une ligne pointant vers vous.

Le cube de navigation peut être déplacé vers n'importe quelle partie de l'affichage 3D en le faisant glisser. Le bouton de glissement (gauche) de la souris doit être enfoncé à l\'intérieur du cube pour déclencher le glissement. Le cube ne se déplacera qu\'avec le déplacement du pointeur de la souris hors du cube.

Un petit mini-cube, situé dans le coin inférieur droit de la zone, active un menu déroulant vous permettant de changer de mode de visualisation.

### Sélection d\'objets 

Les objets dans la vue 3D peuvent être sélectionnés en cliquant dessus avec la souris (voir détails au-dessus) en fonction du mode de navigation. Un seul clic sélectionnera l\'objet et l\'un de ses sous-composants (arête, face, sommet). Double-cliquer sélectionnera l\'objet et tous ses sous-composants. Vous pouvez sélectionner plus d\'un sous-composant voire différents sous-composants de différents objets en appuyant sur la touche CTRL. Cliquer avec le bouton de sélection sur une partie vide de la vue 3D désélectionnera tout.

Un panneau appelé \"Afficher la Sélection\", disponible dans le menu Affichage, peut également être activé. Il vous montrera la sélection en cours :

![](images/Selection_view.jpg )

Vous pouvez également utiliser l\'affichage de sélection pour sélectionner des objets en recherchant un objet particulier.

**Pour en savoir plus** :

-   [Les modes de navigation FreeCAD](Mouse_navigation/fr.md)
-   [Le cube de navigation](Navigation_Cube/fr.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Manual:Navigating in the 3D view/fr
