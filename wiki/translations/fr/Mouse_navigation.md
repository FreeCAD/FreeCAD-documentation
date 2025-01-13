# Mouse navigation/fr
## Présentation

La **navigation par la souris** dans FreeCAD consiste en des commandes utilisées pour naviguer visuellement dans l\'espace 3D et interagir avec les objets affichés. FreeCAD supporte plusieurs styles de navigation à la souris. Le style de navigation par défaut est appelé [Style CAD](#Style_CAD.md). Il est très simple et pratique mais FreeCAD fournit également plusieurs autres styles de navigation. Le style sélectionné est utilisé pour tous les ateliers.

Pour plus d\'informations sur la sélection d\'objets, voir [Méthodes de sélection](Selection_methods/fr.md).

Pour plus d\'informations sur la manipulation des objets, voir [Std Transformer](Std_TransformManip/fr.md).



## Sélection d\'un style de navigation 

1.  Faites l\'une des choses suivantes :
    -   Appuyez sur le bouton **[<img src=images/NavigationCAD_dark.svg style="width:16px">** de la [barre d\'état](Status_bar/fr.md).
    -   Cliquez du bouton droit de la souris sur une zone vide dans la [vue 3D](3D_view/fr.md) et sélectionnez **Styles de navigation** dans le menu contextuel.
    -   Utilisez les [réglages des préférences](Preferences_Editor/fr#Navigation.md). Dans le menu, sélectionnez **Édition → Préférences** et ensuite **Affichage → Navigation → Navigation 3D**.
2.  Sélectionnez un style dans la liste.
3.  Vous pouvez modifier le **style d'orbite** : appuyez sur le bouton **[<img src=images/NavigationCAD_dark.svg style="width:16px">** dans la [barre d\'état](Status_bar/fr.md) puis choisissez **Paramètres → Style d'orbite**. Voir [Réglages des préférences](Preferences_Editor/fr#Navigation.md).
4.  Vous pouvez également modifier le **mode de rotation**. Voir [Réglages des préférences](Preferences_Editor/fr#Navigation.md).
5.  Si le mode de navigation **CAD** est sélectionné, vous pouvez modifier le paramètre **Permettre l'animation**. Voir [Réglages des préférences](Preferences_Editor/fr#Navigation.md).



## Styles de navigation disponibles 

Avec tous les styles de navigation, à moins de sélectionner des objets dans une esquisse en mode édition, vous devez maintenir **Ctrl** pour sélectionner plusieurs objets.

Les options de clavier suivantes sont disponibles pour tous les styles :

-    **Ctrl**\+ {{ASCII|43}} et **Ctrl** + {{ASCII|22}} ou **PgUp** et **PgDn** pour respectivement zoomer et dézoomer.

-   Les touches fléchées, {{ASCII|17}}{{ASCII|16}}{{ASCII|30}}{{ASCII|31}}, permettent les déplacements gauche/droite et haut/bas de la vue.

-    **Shift**\+ {{ASCII|17}} et **Maj** + {{ASCII|16}} pour faire pivoter la vue de 90 degrés.



### Style Blender 

Le style de navigation Blender s\'inspire de [Blender](https://www.blender.org).


{{Blender Navigation
|Select_name=Sélection
|Zoom_name=Zoom
|Rotate_view_name=Rotation de la vue
|Pan_name=Panorama

|Shift=**Maj**

|Select_text=Cliquez avec le bouton gauche de la souris sur l'objet que vous souhaitez sélectionner.

|Zoom_text=Utilisez la molette de la souris pour zoomer et dézoomer.

|Rotate_view_text=Maintenez enfoncé le bouton central de la souris, puis déplacez le pointeur.

|Pan_text=Maintenez enfoncé **Maj** et le bouton central de la souris, puis déplacez le pointeur.

Vous pouvez également maintenir enfoncé les boutons gauche et droit de la souris, et déplacer le pointeur.
}}



### Style CAD 

C\'est le style de navigation par défaut. Il permet à l\'utilisateur un contrôle simple de la vue et ne nécessite pas l\'utilisation de touches du clavier, sauf pour effectuer des sélections multiples.


{{CAD Navigation
|Select_name=Sélection
|Zoom_name=Zoom
|Rotate_view_name=Rotation<br>1ère méthode
|Rotate_view_alt_name=Rotation<br>Méthode alternative
|Pan_name=Panorama

|Ctrl=**Ctrl**
|Shift=**Maj**

|Select_text=Cliquez avec le bouton gauche de la souris sur l'objet que vous souhaitez sélectionner.

|Zoom_text=Utilisez la molette de la souris pour zoomer et dézoomer.

Cliquez sur le bouton central de la souris recentre la vue sur l'emplacement du curseur.

|Rotate_view_text=Maintenez enfoncé le bouton central de la souris, puis appuyez et maintenez le bouton gauche de la souris, puis déplacez le pointeur.

Si les boutons sont relâchés avant que vous n'arrêtiez le mouvement de la souris, la vue continue de tourner, si cette option est activée.

Un double clic avec le bouton central de la souris définit un nouveau centre de rotation.

|Rotate_view_alt_text=Maintenez enfoncé le bouton central de la souris enfoncé, appuyez ensuite sur le bouton droit de la souris, puis déplacez le pointeur.

Avec cette méthode, le bouton central de la souris peut être relâché si vous maintenez le bouton droit de la souris enfoncé.

Les utilisateurs qui utilisent la souris avec leur main droite peuvent trouver cette méthode plus facile que la première.

|Pan_text=Maintenez enfoncé le bouton central de la souris, puis déplacez le pointeur.

|Zoom_mode_text=Mode zoom : maintenez enfoncés **Ctrl** et **Maj**, appuyez une fois sur le bouton droit de la souris, puis déplacez le pointeur.

|Rotate_view_mode_text=Mode rotation: maintenez enfoncé **Maj**, appuyez une fois sur le bouton droit de la souris, puis déplacez le pointeur.

|Pan_mode_text=Mode panoramique : maintenez enfoncé **Ctrl**, appuyez une fois sur le bouton droit de la souris, puis déplacez le pointeur.
}}



### Style Gesture 

Ce style a été conçu pour être utilisé avec un écran tactile et un stylo. Néanmoins, il peut également être utilisé avec une souris et il est recommandé de l\'utiliser avec un Mac doté d\'un pavé tactile.


{{Gesture Navigation
|Select_name=Sélection
|Zoom_name=Zoom
|Rotate_view_name=Rotation de la vue
|Pan_name=Panorama
|Tilt_view_name=Basculement de la vue

|Select_text=Cliquez avec le bouton gauche de la souris sur l'objet que vous souhaitez sélectionner.

|Zoom_text=Utilisez la molette de la souris pour zoomer et dézoomer.

|Rotate_view_text=Maintenez enfoncé le bouton gauche de la souris, puis déplacez le pointeur.
Dans [Sketcher](Sketcher_Workbench/fr.md) et les autres modes d'édition, ce comportement est désactivé. Maintenez enfoncé **Alt** en appuyant sur le bouton de la souris pour passer en mode rotation.

Pour définir le point de focalisation de la caméra pour la rotation, cliquez sur un point avec le bouton central de la souris. Vous pouvez également pointer le curseur sur un point et appuyer sur **H** au clavier.

|Pan_text=Maintenez enfoncé le bouton droit de la souris, puis déplacez le pointeur.

|Tilt_view_text=Maintenez enfoncés les boutons gauche et droit de la souris, puis déplacez le pointeur latéralement.

|Select_gesture_text=Tapotez pour sélectionner.

|Zoom_gesture_text=Faites glisser deux doigts (pincement) pour les rapprocher ou les éloigner.

|Rotate_view_gesture_text=Glissez avec un doigt pour faire pivoter.

Maintenez enfoncé **Alt** si vous êtes dans [Sketcher](Sketcher_Workbench/fr.md).

|Pan_gesture_text=Faites glisser avec deux doigts.

Vous pouvez également tapoter et maintenir, puis glisser. Cela simule le panoramique avec le bouton droit de la souris.

|Tilt_view_gesture_text=Faites pivoter la ligne imaginaire formée par deux points de contact.

Cette méthode est désactivée par défaut. Pour l'activer, allez dans **Édition → Préférences → Affichage → Navigation** puis décochez la case "Désactiver l’inclinaison par geste de l’écran tactile".
}}



### Style MayaGesture 

Dans le style de navigation MayaGesture, le panoramique, le zoom et la rotation de la vue nécessitent la touche **Alt** ainsi qu\'un bouton de la souris : une souris à trois boutons est donc nécessaire. Il est également possible d\'utiliser des gestes car ce style a été développé par rapport au [style Gesture](#Style_Gesture.md).


{{MayaGesture Navigation
|Select_name=Sélection
|Zoom_name=Zoom
|Rotate_view_name=Rotation de la vue
|Pan_name=Panorama
|Tilt_view_name=Basculement de la vue

|Alt=**Alt**

|Select_text=Cliquez avec le bouton gauche de la souris sur l'objet que vous souhaitez sélectionner.

|Zoom_text=Utilisez la molette de la souris pour zoomer et dézoomer.

Vous pouvez également maintenir enfoncé **Alt** et le bouton droit de la souris, puis déplacer le pointeur.

|Rotate_view_text=Maintenez enfoncé **Alt** et le bouton gauche de la souris, puis déplacez le pointeur.

|Pan_text=Maintenez enfoncé **Alt** et le bouton central de la souris, puis déplacez le pointeur.

|Tilt_view_text=Maintenez enfoncé **Alt** et les deux boutons gauche et droit de la souris, puis déplacez le pointeur latéralement.
}}



### Style OpenCascade 

Le style de navigation OpenCascade s\'inspire d\'[OpenCascade](https://www.opencascade.com/).


{{OpenCascade Navigation
|Select_name=Sélection
|Zoom_name=Zoom
|Rotate_view_name=Rotation de la vue
|Pan_name=Panorama

|Ctrl=**Ctrl**

|Select_text=Cliquez avec le bouton gauche de la souris sur l'objet que vous souhaitez sélectionner.

|Zoom_text=Utilisez la molette de la souris pour zoomer et dézoomer.

Vous pouvez également maintenir enfoncé **Ctrl** et le bouton gauche de la souris, puis déplacer le pointeur.

|Rotate_view_text=Maintenez enfoncé le bouton central de la souris, appuyez ensuite sur le bouton droit de la souris, puis déplacez le pointeur.

Vous pouvez également maintenir enfoncé **Ctrl** et le bouton droit de la souris, puis déplacer le pointeur.

|Pan_text=Maintenez enfoncé le bouton central de la souris, puis déplacez le pointeur. Il est possible de maintenir **Ctrl**.
}}



### Style OpenInventor 

Le style de navigation OpenInventor (anciennement Inventor) s\'inspire d\'[Open Inventor](https://fr.wikipedia.org/wiki/Inventor_(bibliothèque_logicielle)). Pour sélectionner des objets, vous devez maintenir la touche **Maj** ou **Ctrl** enfoncée.

Ce style n\'est pas basé sur Autodesk Inventor.


{{OpenInventor Navigation
|Select_name=Sélection
|Zoom_name=Zoom
|Rotate_view_name=Rotation de la vue
|Pan_name=Panorama

|Shift=**Maj**

|Select_text=Maintenez enfoncé **Maj**, puis appuyez sur le bouton gauche de la souris sur un objet que vous souhaitez sélectionner.

Maintenez enfoncé **Ctrl** à la place pour sélectionner plusieurs objets.

|Zoom_text=Utilisez la molette de la souris pour zoomer et dézoomer.

Vous pouvez également maintenir enfoncé le bouton central de la souris, puis maintenir le bouton gauche de la souris enfoncé et déplacer le pointeur.

|Rotate_view_text=Maintenez enfoncé le bouton gauche de la souris, puis déplacez le pointeur.

|Pan_text=Maintenez enfoncé le bouton central de la souris, puis déplacez le pointeur.
}}



### Style OpenSCAD 

Le style de navigation OpenSCAD s\'inspire d\'[OpenSCAD](https://openscad.org/).


{{OpenSCAD_Navigation
|Select_name=Sélection
|Zoom_name=Zoom
|Rotate_view_name=Rotation de la vue
|Pan_name=Panorama

|Shift=**Maj**

|Select_text=Cliquez avec le bouton gauche de la souris sur l'objet que vous souhaitez sélectionner.

{{VersionMinus/fr|0.21}} Maintenez enfoncés **Ctrl** et **Maj** lorsque vous appuyez sur le bouton de la souris pour faire glisser un objet dans une esquisse en mode édition.

|Zoom_text=Utilisez la molette de la souris pour zoomer et dézoomer.

Vous pouvez également maintenir enfoncé le bouton central de la souris, puis déplacez le pointeur.

Ou maintenir enfoncé **Maj** et le bouton droit de la souris, puis déplacez le pointeur.

|Rotate_view_text=Maintenez enfoncé le bouton gauche de la souris, puis déplacez le pointeur.

Sinon, lorsqu'une esquisse est en mode édition, maintenez enfoncé le bouton central de la souris, puis appuyez sur le bouton droit de la souris et maintenez-le enfoncé, puis déplacez le pointeur.

|Pan_text=Maintenez enfoncé le bouton droit de la souris, puis déplacez le pointeur.
}}



### Style Revit 

Le style de navigation Revit s\'inspire de [Revit](https://fr.wikipedia.org/wiki/Revit).


{{Revit Navigation
|Select_name=Sélection
|Zoom_name=Zoom
|Rotate_view_name=Rotation de la vue
|Pan_name=Panorama

|Shift=**Maj**

|Select_text=Cliquez avec le bouton gauche de la souris sur l'objet que vous souhaitez sélectionner.

|Zoom_text=Utilisez la molette de la souris pour zoomer et dézoomer.

|Rotate_view_text=Maintenez enfoncé **Maj** et le bouton central de la souris, puis déplacez le pointeur.

Vous pouvez également maintenir enfoncé le bouton central de la souris, puis maintenir enfoncé le bouton droit de la souris et déplacer le pointeur.

|Pan_text=Maintenez enfoncé le bouton central de la souris, puis déplacez le pointeur.

Vous pouvez également maintenir enfoncé les boutons gauche et droit de la souris, et déplacer le pointeur.
}}



### Style TinkerCAD 

Le style de navigation TinkerCAD s\'inspire de [TinkerCAD](https://fr.wikipedia.org/wiki/Tinkercad).


{{TinkerCAD Navigation
|Select_name=Sélection
|Zoom_name=Zoom
|Rotate_view_name=Rotation de la vue
|Pan_name=Panorama

|Select_text=Cliquez avec le bouton gauche de la souris sur l'objet que vous souhaitez sélectionner.

|Zoom_text=Utilisez la molette de la souris pour zoomer et dézoomer.

|Rotate_view_text=Maintenez enfoncé le bouton droit de la souris, puis déplacez le pointeur.

|Pan_text=Maintenez enfoncé le bouton central de la souris, puis déplacez le pointeur.
}}



### Style Touchpad 

Avec le style de navigation Touchpad, le panoramique, le zoom et la rotation de la vue nécessitent une touche de modification ainsi que le pavé tactile. Ce style peut également être utilisé avec une souris.


{{Touchpad Navigation
|Select_name=Sélection
|Zoom_name=Zoom
|Rotate_view_name=Rotation de la vue
|Pan_name=Panorama

|Ctrl=**Ctrl**
|Shift=**Maj**
|Alt=**Alt**

|Select_text=Cliquez avec le bouton gauche de la souris sur l'objet que vous souhaitez sélectionner.

|Zoom_text=Maintenez enfoncés **Ctrl** et **Maj**, puis déplacez le pointeur.

|Rotate_view_text=Maintenez enfoncé **Alt**, puis déplacez le pointeur.

Vous pouvez également maintenir enfoncé **Maj** et le bouton gauche de la souris, puis déplacer le pointeur.

|Pan_text=Maintenez enfoncé **Maj**, puis déplacez le pointeur.
}}



## Prise en charge du matériel 

FreeCAD prend aussi en charge quelques [périphériques d\'entrée 3D](3D_input_devices/fr.md).



## Style recommandé pour macOS 

Sur les MacBooks équipés d\'un pavé tactile, le style de navigation Gesture fonctionne très bien mais les gestes ont une signification particulière :

-   Zoom : faites glisser avec deux doigts.
-   Rotation : faites glisser avec trois doigts.
-   Panoramique : **Ctrl** + trois doigts.



---
⏵ [documentation index](../README.md) > Mouse navigation/fr
