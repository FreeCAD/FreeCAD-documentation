# Mouse navigation/fr
{{TOCright}}

## Présentation

La **navigation par la souris** dans FreeCAD consiste en des commandes utilisées pour naviguer visuellement dans l\'espace 3D et interagir avec les objets affichés. FreeCAD supporte plusieurs styles de navigation à la souris. Le style de navigation par défaut est appelé [Mode CAD](#Mode_CAD.md). Il est très simple et pratique mais FreeCAD fournit également plusieurs autres styles de navigation à choisir. Le style sélectionné est utilisé pour tous les ateliers.

Pour plus d\'informations sur la sélection d\'objets, voir [Méthodes de sélection](Selection_methods/fr.md).

Pour plus d\'informations sur la manipulation des objets, voir [Std Transformation manipulation](Std_TransformManip/fr.md).

## Sélection d\'un style de navigation 

1.  Faites l\'une des choses suivantes :
    -   Appuyez sur le bouton **[<img src=images/NavigationCAD.svg style="width:16px">** de la [Barre d\'état](Status_bar/fr.md).
    -   Cliquez du bouton droit de la souris sur une zone vide dans la [Vue 3D](3D_view/fr.md) et sélectionnez **Styles de navigation** dans le menu contextuel.
    -   Utilisez les [Réglages des préférences](Preferences_Editor/fr#Navigation.md). Dans le menu, sélectionnez **Edition → Préférences** et ensuite **Affichage → Navigation → Navigation 3D**.
2.  Sélectionnez un style dans la liste.
3.  Modifiez éventuellement le **Style d'orbite** : appuyez sur le bouton **[<img src=images/NavigationCAD.svg style="width:16px">** dans la [Barre d\'état](Status_bar/fr.md) puis choisissez **Paramètres → Style d'orbite**. Voir [Réglages des préférences](Preferences_Editor/fr#Navigation.md).
4.  Vous pouvez également modifier le **Mode de rotation**. Voir [Réglages des préférences](Preferences_Editor/fr#Navigation.md).
5.  Si le mode de navigation **CAD** est sélectionné : modifiez éventuellement le paramètre **Permettre l'animation**. Voir [Réglages des préférences](Preferences_Editor/fr#Navigation.md).

## Styles de navigation disponibles 

### Mode Blender 

Le style de navigation Blender s\'inspire de [Blender](https://www.blender.org).


{{Blender Navigation
|Select_name=Sélection
|Pan_name=Mouvement panoramique
|Zoom_name=Zoom
|Rotate_view_name=Rotation de la vue
|Shift=**Maj**
|Select_text=Cliquez avec le bouton gauche de la souris sur l'objet que vous souhaitez sélectionner.
|Pan_text=Maintenez la touche **Maj** enfoncée, appuyez ensuite sur le bouton central de la souris et déplacez le pointeur.

Vous pouvez également maintenir enfoncé les boutons gauche et droit de la souris, et déplacer le pointeur.
|Zoom_text=Utilisez la molette de la souris pour zoomer et dézoomer.
|Rotate_view_text=Appuyez sur le bouton central de la souris, et déplacez le pointeur.
}}

### Mode CAD 

C\'est le style de navigation par défaut. Il permet à l\'utilisateur un contrôle simple de la vue et ne nécessite pas l\'utilisation de touches du clavier, sauf pour effectuer des sélections multiples.


{{CAD Navigation
|Select_name=Sélection
|Pan_name=Mouvement panoramique
|Zoom_name=Zoom
|Rotate_view_name=Rotation<br>1ère méthode
|Rotate_view_alt_name=Rotation<br>2è méthode
|Ctrl=**Ctrl**
|Shift=**Maj**
|Select_text=Cliquez avec le bouton gauche de la souris sur l'objet que vous souhaitez sélectionner.

Maintenez la touche **Ctrl** enfoncée pour sélectionner plusieurs objets.
|Pan_text=Maintenez le bouton central de la souris enfoncé et déplacez le pointeur pour déplacer l'objet.
|Pan_mode_text=Pan mode: maintenez la touche **Ctrl** enfoncée, appuyez simultanément sur le bouton droit de la souris, puis déplacez le pointeur.
|Zoom_text=Utilisez la molette de la souris pour zoomer et dézoomer.

En cliquant sur le bouton central de la souris, la vue est recentrée sur l'emplacement du curseur.
|Zoom_mode_text=Mode zoom: maintenez les touches **Ctrl** et **Maj** enfoncées, appuyez simultanément sur le bouton droit de la souris, puis déplacez le pointeur.
|Rotate_view_text=Maintenez le bouton central de la souris enfoncé, appuyez ensuite sur le bouton gauche de la souris, puis déplacez le pointeur.

Si les boutons sont relâchés avant que vous n'arrêtiez le mouvement de la souris, la vue continue de tourner, si cette option est activée.

Double cliquer avec le bouton central de la souris définit un nouveau centre de rotation.
|Rotate_view_mode_text=Mode rotation: maintenez la touche **Maj** enfoncée, appuyez simultanément sur le bouton droit de la souris, puis déplacez le pointeur.
|Rotate_view_alt_text=Maintenez le bouton central de la souris enfoncé, appuyez ensuite sur le bouton droit de la souris, puis déplacez le pointeur.

Avec cette méthode, le bouton central de la souris peut être relâché si vous maintenez le bouton droit de la souris enfoncé.

Les utilisateurs qui utilisent la souris avec leur main droite peuvent trouver cette méthode plus facile que la première.
}}

### Mode Gesture 

Ce style a été conçu pour être utilisé avec un écran tactile et un stylo. Néanmoins, il peut également être utilisé avec une souris et il est recommandé de l\'utiliser avec un Mac doté d\'un pavé tactile.


{{Gesture Navigation
|Select_name=Sélection
|Pan_name=Mouvement panoramique
|Zoom_name=Zoom
|Rotate_view_name=Rotation de la vue
|Tilt_view_name=Basculement de la vue
|Select_text=Cliquez avec le bouton gauche de la souris sur l'objet que vous souhaitez sélectionner.
|Select_gesture_text=Cliquez pour sélectionner.
|Pan_text=Maintenez le bouton droit de la souris enfoncé et déplacez le pointeur.
|Pan_gesture_text=Faites glisser avec deux doigts.

Vous pouvez également cliquer et maintenir, puis glisser. Cela simule le panoramique avec le bouton droit de la souris.
|Zoom_text=Utilisez la molette de la souris pour zoomer et dézoomer.
|Zoom_gesture_text=Pincez ou écartez avec deux doigts.
|Rotate_view_text=Maintenez le bouton gauche de la souris enfoncé et déplacez le pointeur.
Dans [l'atelier Sketcher](Sketcher_Workbench/fr.md) et d'autres modes d'édition, ce comportement est désactivé. Maintenez la touche **Alt** enfoncée tout en appuyant sur le bouton de la souris pour passer en mode de rotation.

Pour fixer le point de focus pour la rotation de la caméra, cliquez sur ce point avec le bouton central de la souris. Sinon, pointez le curseur sur ce point et appuyez sur la touche **H** du clavier.
|Rotate_view_gesture_text=Glissez avec un doigt pour tourner.

Maintnez la touche **Alt** enfoncée si vous êtes dans [Sketcher](Sketcher_Workbench.md).
|Tilt_view_text=Maintenez les boutons gauche et droit de la souris enfoncés, et déplacer le pointeur latéralement.
|Tilt_view_gesture_text=Faites pivoter la ligne imaginaire formée par deux points de contact.

Dans la v0.18 ce mode est désactivé par défaut. Pour l'activer, allez dans **Édition → Préférences → Affichage**, et décochez la case "Désactiver gestuelle de basculement écran tactile".
}}

### Mode MayaGesture 

Dans le mode de navigation MayaGesture, le panoramique, le zoom et la rotation de la vue nécessitent la touche **Alt** ainsi qu\'un bouton de la souris; une souris à trois boutons est donc nécessaire. Il est également possible d\'utiliser des gestes car ce mode a été développé par rapport au mode de [navigation Gesture](#Mode_Gesture.md).


{{MayaGesture Navigation
|Select_name=Sélection
|Pan_name=Mouvement panoramique
|Zoom_name=Zoom
|Rotate_view_name=Rotation de la vue
|Alt=**Alt**
|Select_text=Cliquez avec le bouton gauche de la souris sur l'objet que vous souhaitez sélectionner.
|Pan_text=Maintenez la touche **Alt** et le bouton central de la souris enfoncés, puis déplacez le pointeur.
|Zoom_text=Maintenez la touche **Alt** et le bouton droit de la souris enfoncés, puis déplacez le pointeur.

Vous pouvez également utilisez la molette de la souris pour zoomer et dézoomer.
|Rotate_view_text=Maintenez la touche **Alt** et le bouton gauche de la souris enfoncés, puis déplacez le pointeur.
}}

### Mode OpenCascade 

Le style de navigation OpenCascade s\'inspire d\'[OpenCascade](https://www.opencascade.com/).


{{OpenCascade Navigation
|Select_name=Sélection
|Pan_name=Mouvement panoramique
|Zoom_name=Zoom
|Rotate_view_name=Rotation de la vue
|Ctrl=**Ctrl**
|Select_text=Cliquez avec le bouton gauche de la souris sur l'objet que vous souhaitez sélectionner.
|Pan_text=Appuyez sur le bouton central de la souris, puis déplacez le pointeur.
|Zoom_text=Utilisez la molette de la souris pour zoomer et dézoomer.

Vous pouvez également maintenir la touche **Ctrl** et le bouton gauche de la souris enfoncés, puis déplacer le pointeur.
|Rotate_view_text=Maintenez la touche **Ctrl** et le bouton droit de la souris enfoncés, puis déplacer le pointeur.
}}

### Mode OpenInventor 

Le mode de navigation OpenInventor (anciennement Inventor) s\'inspire d\'[Open Inventor](https://fr.wikipedia.org/wiki/Inventor_(bibliothèque_logicielle)). Pour sélectionner des objets, vous devez maintenir la touche **Ctrl** enfoncée.

Ce mode n\'est pas basé sur Autodesk Inventor.


{{OpenInventor Navigation
|Select_name=Sélection
|Pan_name=Mouvement panoramique
|Zoom_name=Zoom
|Rotate_view_name=Rotation de la vue
|Ctrl=**Ctrl**
|Select_text=Maintenez la touche **Ctrl** enfoncée, cliquez ensuite avec le bouton gauche de la souris sur l'objet que vous souhaitez sélectionner.
|Pan_text=Appuyez sur le bouton central de la souris, puis  déplacez le pointeur.
|Zoom_text=Utilisez la molette de la souris pour zoomer et dézoomer.

Alternativement : Maintenez le bouton central de la souris enfoncé, pressez ensuite le bouton gauche de la souris, puis déplacez le pointeur.
|Rotate_view_text=Appuyez sur le bouton gauche de la souris, puis déplacez le pointeur.
}}

### Mode OpenSCAD 

Le style de navigation OpenSCAD s\'inspire d\'[OpenSCAD](https://openscad.org/).


{{Version/fr|0.20}}


{{OpenSCAD_Navigation
|Select_name=Sélection
|Pan_name=Mouvement panoramique
|Zoom_name=Zoom
|Rotate_view_name=Rotation de la vue
|Shift=**Maj**
|Select_text=Appuyez le bouton gauche de la souris sur un objet que vous voulez sélectionner.
|Pan_text=Maintenir le bouton droit de la souris, puis déplacer le pointeur.
|Zoom_text=Maintenir le bouton central de la souris, puis déplacer le pointeur.
Vous pouvez également maintenir **Maj** et le bouton droit de la souris enfoncés, puis déplacer le pointeur.
|Rotate_view_text=Maintenir le bouton gauche de la souris, puis déplacer le pointeur.
}}

### Mode Revit 

Le style de navigation Revit s\'inspire de [Revit](https://fr.wikipedia.org/wiki/Revit).


{{Revit Navigation
|Select_name=Sélection
|Pan_name=Mouvement panoramique
|Zoom_name=Zoom
|Rotate_view_name=Rotation de la vue
|Shift=**Maj**
|Select_text=Cliquez avec le bouton gauche de la souris sur l'objet que vous souhaitez sélectionner.
|Pan_text=Appuyez sur le bouton central de la souris, puis déplacez le pointeur.

Vous pouvez également maintenir enfoncé les boutons gauche et droit de la souris, et déplacer le pointeur.

|Zoom_text=Utilisez la molette de la souris pour zoomer et dézoomer.
|Rotate_view_text=Maintenez la touche **Maj** et le bouton central de la souris enfoncés, puis déplacez le pointeur.

Vous pouvez également maintenir enfoncé le bouton central de la souris, puis aussi le bouton droit, et déplacer le pointeur.
}}

### Mode TinkerCAD 

Le style de navigation TinkerCAD s\'inspire de [TinkerCAD](https://fr.wikipedia.org/wiki/Tinkercad).


{{Version/fr|0.20}}


{{TinkerCAD Navigation
|Select_name=Sélection
|Pan_name=Mouvement panoramique 
|Zoom_name=Zoom
|Rotate_view_name=Rotation de la vue 
|Select_text=Appuyez le bouton gauche de la souris sur un objet que vous voulez sélectionner.
|Pan_text=Maintenir le bouton central de la souris, puis déplacer le pointeur.
|Zoom_text=Utiliser la molette de la souris pour faire un zoom avant ou arrière.
|Rotate_view_text=Appuyez sur le bouton droit de la souris, puis déplacez le pointeur.
}}

### Mode Touchpad 

Dans la navigation Touchpad, le panoramique, le zoom et la rotation de la vue nécessitent une touche de modification en même temps que le pavé tactile.


{{Touchpad Navigation
|Select_name=Sélection
|Pan_name=Mouvement panoramique
|Zoom_name=Zoom
|Rotate_view_name=Rotation de la vue
|Shift=**Maj**
|Ctrl=**Ctrl**
|Alt=**Alt**
|PageUp=**Page précédente**
|PageDown=**Page suivante**
|Select_text=Cliquez avec le bouton gauche sur l'objet que vous souhaitez sélectionner.
|Pan_text=Maintenez la touche **Maj** enfoncée et déplacez le pointeur.
|Zoom_text=Utiliser les touches **Page précédente** et **Page suivante** pour zoomer et dézoomer.
|Zoom_alt_text=Autre possibilité, maintenez les touches **Maj** et **Ctrl** enfoncées, puis déplacez le pointeur.
|Rotate_view_text=Maintenez la touche **Alt** enfoncée, puis déplacez le pointeur.
|Rotate_view_alt_text=Autre possibilité, maintenez la touche **Maj** enfoncée ainsi que le bouton gauche, puis déplacez le pointeur.
}}

## Support matériel 

FreeCAD supporte aussi quelques [périphériques d\'entrée 3D](3D_input_devices/fr.md).

## Mode recommandé pour macOS 

Sur les MacBooks équipés d\'un pavé tactile, la navigation Gesture fonctionne très bien mais les gestes ont une signification particulière :

-   Zoom : faire glisser avec deux doigts.
-   Rotation : faire glisser avec trois doigts.
-   Panoramique : **Ctrl** + trois doigts.

## Développer un mode personnalisé 

Le tutoriel [Ajout d\'une nouvelle option de navigation à la souris à FreeCAD](Adding_a_new_mouse_navigation_option_to_FreeCAD/fr.md) oriente les développeurs qui souhaitent développer une option de navigation à la souris personnalisée. Une certaine familiarité avec la syntaxe C++ est requise.

---
[documentation index](../README.md) > Mouse navigation/fr
