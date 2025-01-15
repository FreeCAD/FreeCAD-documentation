---
 GuiCommand:
   Name: PartDesign SubtractiveTorus
   Name/fr: PartDesign Tore soustractif
   MenuLocation: PartDesign , Créer une  primitive soustractive , Tore soustractif
   Workbenches: PartDesign_Workbench/fr
   Version: 0.17
   SeeAlso: PartDesign_CompPrimitiveSubtractive/fr, PartDesign_AdditiveTorus/fr
---

# PartDesign SubtractiveTorus/fr

## Description

Insère un Tore primitif soustractif dans le corps actif. Sa forme est soustraite du solide existant.

![](images/PartDesign_SubtractiveTorus_example.svg ) *À gauche, le corps actif (A) en gris et le tore soustractif (B) en rouge transparent ; le résultat final est à droite.*



## Utilisation

1.  Presser le bouton **<img src="images/PartDesign_SubtractiveTorus.svg" width=24px> '''Tore soustractif'''**. **Remarque** : Le Tore soustractif fait partie du menu d\'icônes appelé *Créer une primitive soustractive*. Après le lancement de FreeCAD, le cube additif est affiché par défaut dans la barre d\'outils. Pour obtenir le Tore soustractif, cliquer sur la flèche vers le bas et choisissez Tore soustractif dans le menu.
2.  Définir les paramètres primitifs et de l\'[ancrage](Part_EditAttachment/fr.md).
3.  Cliquer sur **OK**.
4.  Un tore apparaît dans le corps actif.

## Options

Le Tore peut être éditée après sa création de deux façons :

-   Double-cliquez le dans l\'arborescence ou faire un clic droit dessus et sélectionnez **Éditer la primitive** dans le menu contextuel. Cela fait apparaître les paramètres des Primitives.
-   Via l\'[Éditeur de propriétés](Property_editor/fr.md).



## Propriétés

-    **Attachment**: définit les modes d\'ancrage ainsi que le décalage d\'ancrage. Voir [Part Ancrage](Part_EditAttachment/fr.md).

-    **Label**: donne le nom du tore, changer si nécessaire.

-    **Radius1**: rayon imaginaire de l\'orbite autour de laquelle la section circulaire tourne. (La distance entre le centre du tore et le centre de la section transversale tournante)

-    **Radius2**: rayon de la section circulaire du tore.

-    **Angle1**: (Nommé *Paramètre V* dans les paramètres de la primitive) troncature inférieure du tore, parallèle à la section circulaire (-180° dans un tore complet). Un bogue dans les sources entraîne des résultats inattendus lors du changement d\'Angle1.

-    **Angle2**: (sans nom dans les paramètres de la primitive) troncature supérieure de l\'ellipsoïde, parallèle à la section circulaire (180° dans un tore complet). Un bogue dans les sources entraîne des résultats inattendus lors du changement d\'Angle2.

-    **Angle3**: (nommé *Paramètre U* dans les paramètres de la primitive) angle de rotation de la section circulaire (360° dans un tore complet).



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveTorus/fr
