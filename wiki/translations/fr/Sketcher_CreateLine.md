---
- GuiCommand:/fr
   Name:Sketcher CreateLine
   Name/fr:Sketcher Ligne
   MenuLocation:Sketch → Géométries d'esquisse → Créer une ligne
   Workbenches:[Sketcher](Sketcher_Workbench/fr.md)
   Shortcut:L
   SeeAlso:[Sketcher Polyligne](Sketcher_CreatePolyline/fr.md)
---

## Description

Cet outil dessine une Ligne en cliquant deux points dans la vue 3D.

Lorsque l\'outil est activé, le pointeur de la souris se change en croix blanche avec une icône de ligne rouge. Les coordonnées à l\'écran du pointeur sont affichées à côté en bleu, et sont mises à jour en temps réel.

![](images/Sketcher_LineExample1.png‎ )

L\'objet ligne créé commence et se termine aux points donnés, mais la ligne est infinie en ce qui concerne les contraintes [Tangent](Sketcher_ConstrainTangent/fr.md), [Point sur objet](Sketcher_ConstrainPointOnObject/fr.md) et [Angle interne](Sketcher_ConstrainAngle/fr.md). Cela signifie par exemple qu'un point avec la contrainte [Point sur objet](Sketcher_ConstrainPointOnObject/fr.md) peut ne pas être situé entre les deux points donnés, mais peut se trouver en dehors des deux points sur l'extension de la ligne dessinée.

## Utilisation

-   Cliquer des points dans un espace libre de la vue 3D, ou sur un élément existant (les contraintes auto doivent être activées dans le panneau Tâches).
-   Appuyer sur **ÉCHAP** ou faire un clic droit avec la souris annule l\'opération.





{{Sketcher Tools navi

}}  
