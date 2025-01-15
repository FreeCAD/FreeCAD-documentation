---
 GuiCommand:
   Name: PartDesign AdditiveBox
   Name/fr: PartDesign Cube additif
   MenuLocation: PartDesign , Créer une primitive additive , Cube additif
   Workbenches: PartDesign_Workbench/fr
   Version: 0.17
   SeeAlso: PartDesign_CompPrimitiveAdditive/fr, PartDesign_SubtractiveBox/fr
---

# PartDesign AdditiveBox/fr

## Description

Insère un Cube primitif dans un corps actif (body) comme première fonction, ou le fusionne aux fonctions existantes.

<img alt="" src=images/PartDesign_AdditiveBox_example.png  style="width:200px;">



## Utilisation

1.  Presser le bouton **<img src="images/PartDesign_AdditiveBox.svg" width=24px> '''Cube additif'''**. **Remarque** : le cube additif fait partie d\'un menu d\'icônes appelé *Créer une primitive additive*. Après le démarrage de FreeCAD, le cube additif est celui affiché dans la barre d\'outils. Si une autre primitive est affichée, cliquer sur la flèche vers le bas et choisissez Cube additif.
2.  Définir les paramètres primitifs et de l\'[ancrage](Part_EditAttachment/fr.md).
3.  Cliquer sur **OK**.
4.  Un cube apparaît dans le corps actif.



## Options

Le Cube peut être édité après sa création de deux façons :

-   Double-cliquez le dans l\'arborescence ou faire un clic droit dessus et sélectionnez **Éditer la primitive** dans le menu contextuel. Cela fait apparaître les paramètres des Primitives.
-   Via l\'[éditeur de propriétés](Property_editor/fr.md).



## Propriétés

-    **Attachment**: définit les modes d\'ancrage ainsi que le décalage d\'ancrage. Voir [Part Ancrage](Part_EditAttachment/fr.md).

-    **Label**: donne le nom du cube, changer si nécessaire.

-    **Length**: longueur du cube sur l\'axe X.

-    **Width**: largeur du cube sur l\'axe Y.

-    **Height**: hauteur du cube sur l\'axe Z.



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveBox/fr
