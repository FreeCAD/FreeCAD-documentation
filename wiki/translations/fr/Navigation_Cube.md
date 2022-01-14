# Navigation Cube/fr
{{TOCright}}

## Introduction

Le **cube de navigation** donne des informations visuelles sur l\'orientation de la caméra dans la [vue 3D](3D_view/fr.md) en cours et peut être utilisé pour la modifier. Par défaut, il est visible et se trouve dans le coin supérieur droit de la vue.

Le cube de navigation a été mis à jour dans la version 0.20 de FreeCAD et le reste de cette page décrit cette version. Dans la version 0.19 de FreeCAD, le comportement principal est identique mais certaines fonctionnalités sont manquantes.

![](images/Navigation_Cube_Example.png )

Le cube de navigation se compose de plusieurs parties :

-   Le [cube principal](#Cube_principal.md)
-   Six [flèches directionnelles](#Fl.C3.A8ches_directionnelles.md).
-   Le [bouton de vue inversée](#Bouton_de_vue_invers.C3.A9e.md). (en haut à droite) {{Version/fr|0.20}}
-   Le [menu du mini-cube](#Menu_du_mini-cube.md) (en bas à droite)
-   Les indicateurs des axes X, Y et Z

Toutes les composantes, à l\'exception des indicateurs d\'axe, peuvent être cliquées.

## Utilisation

### Cube principal 

Le cube principal comporte 26 faces : 6 faces principales carrées, 12 faces de bord rectangulaires ({{Version/fr|0.20}}) et 8 faces d\'angle triangulaires. En cliquant sur l\'une d\'entre elles, la caméra sera réorientée de façon à ce que sa direction soit perpendiculaire à la face sélectionnée.

### Flèches directionnelles 

Il existe six flèches directionnelles : quatre flèches triangulaires et deux flèches courbes. En cliquant sur l\'une des flèches triangulaires, vous ferez pivoter la [vue 3D](3D_view/fr.md) autour d\'une ligne perpendiculaire à la direction de la flèche. Si vous cliquez sur une flèche courbe, la [vue 3D](3D_view/fr.md) tournera autour de la direction de la flèche.

### Bouton de vue inversée 

En cliquant sur le bouton rond dans le coin supérieur droit du cube de navigation, vous ferez pivoter la [vue 3D](3D_view/fr.md) de 180 degrés autour de l\'axe vertical de la vue.

### Menu du mini-cube 

En cliquant sur le petit cube dans le coin inférieur droit du cube de navigation, un menu s\'affiche avec les options suivantes :

-    **[Orthographique](Std_OrthographicCamera/fr.md)**: passe à une vue orthographique.

-    **[Perspective](Std_PerspectiveCamera/fr.md)**: permet d\'obtenir une vue en perspective.

-    **[Isometrique](Std_ViewIsometric/fr.md)**: permet de passer à une vue isométrique.

-    **[Ajuster le zoom](Std_ViewFitAll/fr.md)**: effectue un zoom et un panoramique de la caméra de façon à ce que tous les objets visibles tiennent dans la vue.

## Personnalisation

### Déplacement du cube de navigation 

L\'ensemble du cube de navigation peut être déplacé en appuyant sur la souris n\'importe où sur le cube principal et en la faisant glisser. La structure ne commencera à se déplacer que lorsque le curseur aura dépassé l\'un des bords du cube principal.

### Préférences

Le cube de navigation est contrôlé par plusieurs préférences : **Édition → Préférences... → Affichage → Navigation → Cube de navigation**. Voir [Réglage des préférences](Preferences_Editor/fr#Navigation.md).

### Options avancées 

L\'atelier externe [Cube Menu](Interface_Customization/fr#Menu_Cube.md) permet d\'accéder plus facilement à plusieurs options de personnalisation plus avancées.







[<img src="images/Property.png" style="width:16px"> User Documentation](Category_User_Documentation.md)

---
[documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > Navigation Cube/fr
