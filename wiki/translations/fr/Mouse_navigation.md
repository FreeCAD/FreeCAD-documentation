





{{TOCright}}

## Vue d\'ensemble 

La **navigation par la souris** dans FreeCAD décrit les commandes utilisées pour naviguer visuellement dans l\'espace 3D et interagir avec les objets affichés. FreeCAD prend en charge plusieurs styles de navigation à la souris. Le style de navigation par défaut est appelé \"CAD Navigation\" et est très simple et pratique, mais FreeCAD fournit également des styles de navigation alternatifs que vous pouvez choisir en fonction de vos préférences.

## Navigation

La gestuelle de la souris utilisée pour la manipulation d\'objets varie en fonction du style de navigation sélectionné ; le style choisi est utilisé pour tous les ateliers.

Il y a deux façons de changer le style de navigation :

-   Dans les [Préférences](Preferences_Editor/fr#Navigation.md) ; menu **Édition → Préférences → Affichage → Vue 3D → Navigation 3D**.
-   En cliquant avec le bouton droit de la souris dans une zone vide de la vue 3D, puis en sélectionnant **Styles de navigation → ...** dans le menu contextuel.

### Mode CAD (par défaut) 

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
|Pan_mode_text=Pan mode: maintenez la touche **Ctrl** enfoncée, appuyez simultanément sur le bouton droit de la souris, puis déplacez le pointeur. {{Version/fr|0.17}}
|Zoom_text=Utilisez la molette de la souris pour zoomer et dézoomer.

En cliquant sur le bouton central de la souris, la vue est recentrée sur l'emplacement du curseur.
|Zoom_mode_text=Mode zoom: maintenez les touches **Ctrl** et **Maj** enfoncées, appuyez simultanément sur le bouton droit de la souris, puis déplacez le pointeur. {{Version/fr|0.17}}
|Rotate_view_text=Maintenez le bouton central de la souris enfoncé, appuyez ensuite sur le bouton gauche de la souris, puis déplacez le pointeur.

Lorsque le bouton central de la souris est enfoncé l'emplacement du curseur détermine le centre de rotation. La rotation fonctionne comme une balle qui tourne autour de son centre. Si les boutons sont relâchés avant d'arrêter le mouvement de la souris, la vue continue [sa rotation](spinning/fr.md), si cette option est activée.

Double cliquer avec le bouton central de la souris définit un nouveau centre de rotation.
|Rotate_view_mode_text=Mode rotation: maintenez la touche **Maj** enfoncée, appuyez simultanément sur le bouton droit de la souris, puis déplacez le pointeur. {{Version/fr|0.17}}
|Rotate_view_alt_text=Maintenez le bouton central de la souris enfoncé, appuyez ensuite sur le bouton droit de la souris, puis déplacez le pointeur.

Avec cette méthode, le bouton central de la souris peut être relâché si vous maintenez le bouton droit de la souris enfoncé.

Les utilisateurs qui utilisent la souris avec leur main droite peuvent trouver cette méthode plus facile que la première.
}}

### Mode OpenInventor 

Le mode de navigation OpenInventor (anciennement Inventor) s\'inspire de [Open Inventor](https://fr.wikipedia.org/wiki/Inventor_(bibliothèque_logicielle)). Pour sélectionner des objets, vous devez maintenir la touche **Ctrl** enfoncée.

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

### Mode Blender 

Le style de navigation **Blender** a été modélisé d\'après [Blender](https://www.blender.org). Auparavant, il n\'y avait pas de panoramique uniquement à la souris ; il fallait toujours maintenir appuyé la touche **Maj**. Cela a changé en 2016, maintenant vous pouvez maintenir les boutons gauche et droit de la souris enfoncés. {{Blender Navigation
|Select_name=Sélection
|Pan_name=Mouvement panoramique
|Zoom_name=Zoom
|Rotate_view_name=Rotation de la vue
|Shift=**Maj**
|Select_text=Cliquez avec le bouton gauche de la souris sur l'objet que vous souhaitez sélectionner.
|Pan_text=Maintenez la touche **Maj** enfoncée, appuyez ensuite sur le bouton central de la souris, et déplacez le pointeur.

Vous pouvez également maintenir enfoncé les boutons gauche et droit de la souris, et déplacer le pointeur.
|Zoom_text=Utilisez la molette de la souris pour zoomer et dézoomer.
|Rotate_view_text=Appuyez sur le bouton central de la souris, et déplacez le pointeur.
}}

### Mode Touchpad 

En mode Touchpad, le mouvement panoramique, le zoom et la rotation de vue nécessitent une touche modificatrice en plus du pavé tactile. {{Touchpad Navigation
|Select_name=Sélection
|Pan_name=Mouvement panoramique
|Zoom_name=Zoom
|Rotate_view_name=Rotation de la vue
|Shift=**Maj**
|Ctrl=**Ctrl**
|Alt=**Alt**
|PageUp=**PageUp**
|PageDown=**PageDown**
|Select_text=Cliquez avec le bouton gauche sur l'objet que vous souhaitez sélectionner.
|Pan_text=Maintenez la touche **Maj** enfoncée, et déplacez le pointeur.
|Zoom_text=Utiliser les touches **PageUp** et **PageDown** pour zoomer et dézoomer.
|Zoom_alt_text=Alternativement : Maintenez les touches **Maj** et **Ctrl** enfoncées, puis déplacez le pointeur.
|Rotate_view_text=Maintenez la touche **Alt** enfoncée, puis déplacez le pointeur.
|Rotate_view_alt_text=Alternativement : Maintenez la touche **Maj** enfoncée ainsi que le bouton gauche, puis déplacez le pointeur.
}}

### Mode Gestuel 

Ce style de navigation a été adapté pour faciliter l\'utilisation avec un écran tactile et un stylet. Néanmoins il peut aussi être utilisé avec la souris, et est recommandé pour l\'utilisation d\'un Mac avec un pavé tactile. {{Gesture Navigation
|Select_name=Sélection
|Pan_name=Mouvement panoramique
|Zoom_name=Zoom
|Rotate_view_name=Rotation de la vue
|Tilt_view_name=Basculement de la vue
|Select_text=Cliquez avec le bouton gauche de la souris sur l'objet que vous souhaitez sélectionner.
|Select_gesture_text=Cliquez pour sélectionner.
|Pan_text=Maintenez le bouton droit de la souris enfoncé et déplacez le pointeur.
|Pan_gesture_text=Glisser avec deux doigts.

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

### Mode Gestuelle-Maya 

Dans le mode Gestuelle-Maya, le panoramique, le zoom et la rotation de la vue nécessitent la touche **Alt** et un bouton de la souris, par conséquent, une souris à trois boutons est requise. Il est également possible d\'utiliser des gestes car ce mode a été développé par rapport au [mode de navigation par gestes](#Mode_Gestuel.md). {{MayaGesture Navigation
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

### Mode Revit 

Ce style est introduit dans la version 0.18.


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

### Mode OpenCascade 

Ce style est introduit dans la version 0.18.


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

## Sélectionner des objets 

### Sélection simple 

Les objets peuvent être sélectionnés en cliquant avec le bouton gauche de la souris sur l\'objet, soit dans la [vue 3D](3D_view/fr.md), soit dans la [vue arborescente](tree_view/fr.md).

### Présélection

Un mécanisme de *présélection* permet de mettre les objets en surbrillance et d\'afficher des informations à leur sujet lorsque le curseur de la souris les survole. Si vous n\'aimez pas ce comportement, ou si vous avez un PC modeste, vous pouvez désactiver la présélection dans les préférences.

## Manipulation d\'objets 

FreeCAD propose des [*manipulateurs*](Manipulator/fr.md) qui sont des poignées pouvant être utilisés pour modifier l\'apparence, la forme ou d\'autres paramètres d\'un objet.

## Support matériel 

FreeCAD supporte aussi quelques [périphériques d\'entrée 3D](3D_input_devices/fr.md).

## Mac OS X 

Récemment nous avons créé un [post sur le forum](http://forum.freecadweb.org/viewtopic.php?f=3&t=3592&start=0) des utilisateurs Mac pour qui ces combinaisons de touches et boutons de souris ne fonctionneraient pas comme prévu. Malheureusement, aucun des développeurs n\'est possesseur d\'un Mac, pas plus que les autres contributeurs réguliers. Nous avons besoin de votre aide pour déterminer les combinaisons de touches et boutons de souris fonctionnelles afin que nous puissions les renseigner sur ce wiki.






