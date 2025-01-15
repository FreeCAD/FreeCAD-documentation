---
 GuiCommand:
   Name: PartDesign AdditiveTorus
   Name/fr: PartDesign Tore Additif
   MenuLocation: PartDesign , Créer une primitive additive , Tore additif
   Workbenches: PartDesign_Workbench/fr
   Version: 0.17
   SeeAlso: PartDesign_CompPrimitiveAdditive/fr, PartDesign_SubtractiveTorus/fr
---

# PartDesign AdditiveTorus/fr

## Description

Insérer un tore Primitif dans un corps actif (body) comme fonction de base, ou le fusionne aux fonctions existantes.

<img alt="" src=images/PartDesign_AdditiveTorus_example.png  style="width:200px;">



## Utilisation

1.  Presser le bouton **<img src="images/PartDesign_AdditiveTorus.svg" width=24px> '''Tore additif'''**. **Remarque** : Le Tore additif fait partie du menu d\'icônes appelé *Créer une primitive additive*. Après le lancement de FreeCAD, le cube additif est affiché par défaut dans la barre d\'outils. Pour obtenir le Tore additif, cliquer sur la flèche vers le bas et choisissez Tore additif dans le menu.
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

-    **Radius1**: rayon imaginaire de l\'orbite autour de laquelle la section circulaire tourne. (La distance entre le centre du tore et le centre de la section transversale tournante).

-    **Radius2**: rayon de la section circulaire du tore.

-    **Angle1**: (nommé *Paramètre V* dans dans les paramètres de la primitive) parallèle à la partie inférieure de la section circulaire (-180° pour un tore entier). Un bogue dans les sources provoque des résultats inattendus lors de la modification de Angle1.

-    **Angle2**: (sans nom dans les paramètres de la primitive) réduit la hauteur telle une ellipsoïde, parallèle à la section circulaire (180° pour un tore entier). Un bogue dans les sources provoque des résultats inattendus lors de la modification de Angle1.

-    **Angle3**: (nommé *Paramètre U* dans les paramètres de la primitive) angle de rotation de la section circulaire (anneau partiel) (180°pour un tore entier).



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveTorus/fr
