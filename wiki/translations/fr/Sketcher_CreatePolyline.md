---
- GuiCommand:/fr
   Name:Sketcher CreatePolyline
   Name/fr:Sketcher Polyligne
   MenuLocation:Sketch → Géométries d'esquisse → Créer une polyligne
   Workbenches:[Sketcher](Sketcher_Workbench/fr.md)
   SeeAlso:[Sketcher Ligne](Sketcher_CreateLine/fr.md)
---

## Description

Cet outil fonctionne comme l\'outil [Ligne](Sketcher_CreateLine/fr.md), mais dessine des segments de droite et des arcs continus et reliés par leurs sommets en cliquant des points dans la vue 3D. Lorsque l\'outil est activé, le pointeur de la souris se change en croix blanche avec une icône de Polyligne rouge. Les coordonnées du pointeur sont affichées en bleu à côté de la croix, et sont mises à jour en temps réel.

![](images/Sketcher_PolylineExample1.png )


*Polyligne commençant par une ligne, un arc tangent, un arc perpendiculaire puis une ligne tangente.*

## Utilisation

L\'outil Polyligne commence toujours par un segment de droite: cliquez, déplacez la souris puis cliquez. Déplacez la souris à nouveau. Après avoir placé le premier segment de ligne, l\'outil de polyligne du Sketcher a plusieurs modes qui peuvent être basculés avec la touche **M**. Par exemple, vous pouvez dessiner des arcs tangents ou perpendiculaires à la suite d\'un segment de ligne ou d\'arc. Appuyez plusieurs fois sur la touche **M** pour basculer entre ces différents modes:

1.  Appuyez sur la touche **M**: le nouveau segment est une ligne perpendiculaire au segment précédent.
2.  Appuyez de nouveau sur la touche **M**: le nouveau segment est une ligne tangente au segment précédent.
3.  Appuyez de nouveau sur la touche **M**: le nouveau segment est un arc tangent au segment précédent.
4.  Appuyez de nouveau sur la touche **M**: le nouveau segment est un arc perpendiculaire (à gauche) du segment précédent.
5.  Appuyez de nouveau sur la touche **M**: le nouveau segment est un arc qui est perpendiculaire (à droite) du segment précédent.
6.  Appuyez de nouveau sur la touche **M**: Vous êtes de nouveau dans l\'état où vous avez commencé; la ligne n\'est connectée qu\'avec une coïncidence avec le segment précédent.

-    {{VersionPlus/fr|0.18}}Lorsque vous êtes dans l\'un des modes arc, maintenez la touche **Ctrl** (Pour MacOS touche: **CMD**) enfoncée et déplacez le curseur pour aligner l\'arc par incréments de 45 degrés par rapport au segment de polyligne précédemment créé.

-   Cliquer des points dans un espace libre de la vue 3D, ou sur un élément existant (le mode \"Contraintes auto\" doit être activé dans le panneau Tâches).

-   Appuyer sur **Echap** ou cliquer sur le bouton droit de la souris avant de fermer la polyligne en une boucle met fin à la polyligne actuelle et vous pouvez continuer avec une nouvelle polyligne.

-   Appuyer sur **Echap** ou cliquer sur le bouton droit de la souris après avoir fermé la polyligne en une boucle met fin à la fonction polyligne.





{{Sketcher Tools navi

}}  
