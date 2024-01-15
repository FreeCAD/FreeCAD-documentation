# 3D view/fr
## Introduction




La [vue 3D](3D_view/fr.md) de FreeCAD est une instance d'une [scène graphique](Scenegraph/fr.md) Coin3D qui forme la fenêtre la plus importante de l\'[interface](interface/fr.md). Coin3D est une bibliothèque qui implémente le standard de description de scène OpenInventor 2.1.

Certaines propriétés de la vue, telles que la couleur d\'arrière-plan, le style de [navigation à la souris](Mouse_navigation/fr.md) et les étapes de zoom, peuvent être configurées dans l\'[éditeur de préférences](Preferences_Editor/fr.md).

<img alt="" src=images/FreeCAD_3D_view.png  style="width:600px;">



*La [vue 3D](3D_view/fr.md) est une composante de l'[interface](interface/fr.md) de FreeCAD. Par défaut, elle affiche un petit widget avec les axes de coordonnées et le cube de navigation, également avec des axes de coordonnées. La grille peut être affichée et configurée en chargeant l'[atelier Draft](Draft_Workbench/fr.md).*

## Actions

Comme la [vue arborescente](tree_view/fr.md) répertorie la plupart des objets visibles dans la vue 3D, la plupart des actions sont identiques à celles pouvant être exécutées à partir de la [vue arborescente](tree_view/fr.md).

Lorsque l\'[atelier Start](Start_Workbench/fr.md) par défaut est actif, un clic droit sur la vue 3D n'affiche qu'une commande :

-    **[Styles de navigation](Mouse_navigation/fr.md)**: différents styles de boutons à utiliser avec une souris 3 boutons ou un trackpad pour ordinateur portable.

Cependant, une fois qu\'un [atelier](Workbenches/fr.md) est chargé, des commandes supplémentaires sont disponibles :

-    **Actions de lien**: [Créer un lien](Std_LinkMake/fr.md).

    -   
        **Créer un groupe de liens**
        
        : [Groupe simple](Std_LinkMakeGroup/fr.md), [Groupe avec liens](Std_LinkMakeGroup/fr.md), [Groupe avec liens de transformation](Std_LinkMakeGroup/fr.md).

-    **[Tout adapter](Std_ViewFitAll/fr.md)**: effectue un panoramique et un zoom sur la vue pour qu\'elle s\'adapte à tous les objets du document à l\'écran.

-    **[Ajuster la sélection](Std_ViewFitSelection/fr.md)**: effectue un panoramique et un zoom sur la vue afin d'ajuster parfaitement l'objet actuellement sélectionné à l'écran.

-    **[Style de dessin](Std_DrawStyle/fr.md)**: tel quel, lignes plates, ombrées, fil de fer, points, ligne cachée, aucun ombrage.

-    **[Vues standard](Std_View_Menu/fr.md)**: [Isométrique](Std_ViewIsometric/fr.md), [Avant](Std_ViewFront/fr.md), [Haut](Std_ViewTop/fr.md), [Droite](Std_ViewRight/fr.md), [Arrière](Std_ViewRear/fr.md), [Bas](Std_ViewBottom/fr.md), [Gauche](Std_ViewLeft/fr.md), [Rotation à gauche](Std_ViewRotateLeft/fr.md), [Rotation à droite](Std_ViewRotateRight/fr.md).

-    **Mesure**: [Basculer mesure](View_Measure_Toggle_All/fr.md), [Effacer mesure](View_Measure_Clear_All/fr.md).

-    **Fenêtre de document**: [Ancrée](Std_ViewDockUndockFullscreen/fr.md), [Désancrée](Std_ViewDockUndockFullscreen/fr.md) et [Plein écran](Std_ViewDockUndockFullscreen/fr.md).

De plus, en fonction de l\'atelier et de l\'objet actifs, d\'autres commandes contextuelles peuvent devenir disponibles.

Par exemple, avec l\'[atelier Part](Part_Workbench/fr.md) et un objet sélectionné :

-    **[Apparence](Std_SetAppearance/fr.md)**: lance la boîte de dialogue pour modifier la couleur et la taille des lignes et des sommets, ainsi que la couleur des faces.

-    **[Basculer la visibilité](Std_ToggleVisibility/fr.md)**: rend l\'objet visible ou invisible dans la vue 3D.

-    **[Sélectionnable](Std_ToggleSelectability/fr.md)**: rend l'objet non sélectionnable dans la vue 3D ; utilisez à nouveau cette commande pour annuler son effet. Il fixe l\'attribut `Selectable` de l\'objet sur `True` ou `False`. Modifiez la propriété en basculant {{PropertyView/fr|Sélectionnable}} dans l\'[éditeur de propriété](property_editor/fr.md).

-    **[Aller à la sélection](Std_TreeSelection/fr.md)**: développez l\'[arborescence](tree_view/fr.md) pour afficher l\'objet sélectionné dans la hiérarchie.

-    **[Couleur aléatoire](Std_RandomColor/fr.md)**: attribue une couleur aléatoire à l\'objet. Il définit l\'attribut `ShapeColor` de l\'objet sur un triplet `(r,g,b)` avec une arborescence flottante aléatoire comprise entre 0 et 1. Modifiez la propriété en modifiant {{PropertyView/fr|Shape Color}} dans l\'[éditeur de propriétés](property_editor/fr.md).

-    **[Supprimer](Std_Delete/fr.md)**: supprime l\'objet du document et de la vue 3D en appelant la fonction `removeObject()` du document.

Un autre exemple, avec l\'[atelier Draft](Draft_Workbench/fr.md) et un objet sélectionné, affiche les mêmes commandes que pour l\'[atelier Part](Part_Workbench/fr.md), mais aussi :

-    **Draft**: commandes de création et de modification d\'objets à partir de l\'[atelier Draft](Draft_Workbench/fr.md).

-    **Utilitaires**: commandes contextuelles supplémentaires fournies par l\'[atelier Draft](Draft_Workbench/fr.md).



## Détails

FreeCAD utilise la bibliothèque Quarter pour utiliser Coin3D dans un environnement Qt.

Il est possible d\'interagir directement avec le scénario 3D depuis la [console Python](Python_console/fr.md) à l\'aide de la bibliothèque Python Pivy.

Pour plus d\'informations, voir la documentation de l\'utilisateur expert :

-   [Scéne graphique](Scenegraph/fr.md), description de Coin3D.
-   [Pivy](Pivy/fr.md), utilisation de Coin3D à partir de la console Python.
-   [Bibliothèques tierces](Third_Party_Libraries/fr.md) utilisées par FreeCAD.
-   Documentation C++ de [Coin3D](https://grey.colorado.edu/coin3d/index.html).


{{Interface navi

}}



---
⏵ [documentation index](../README.md) > 3D view/fr
