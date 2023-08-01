---
- GuiCommand:/fr
   Name:PartDesign AdditiveCone
   Name/fr:PartDesign Cône additif
   MenuLocation:Part Design → Créer une primitive additive → Cône additif
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   Version:0.17
   SeeAlso:[PartDesign Primitives additives](PartDesign_CompPrimitiveAdditive/fr.md), [PartDesign Cône soustractif](PartDesign_SubtractiveCone.md)
---

# PartDesign AdditiveCone/fr

## Description

Insère un Cône primitif dans un corps actif comme première fonction, ou le fusionne avec les fonctions existantes.

<img alt="" src=images/PartDesign_AdditiveCone_example.png  style="width:200px;">



## Utilisation

1.  Pressez le bouton **<img src="images/PartDesign_AdditiveCone.svg" width=24px> '''Cône additif'''**. **Remarque** : le Cône additif fait partie du menu d\'icônes appelé *Créer une primitive additive*. Après le lancement de FreeCAD, le cube additif est affiché par défaut dans la barre d\'outils. Pour obtenir le Cône additif, cliquer sur la flèche vers le bas et choisissez Cône additif dans le menu.
2.  Définissez les paramètres de la primitive (pour un cône complet, mettez un des rayons à zéro) et de l\'[Part ancrage](Part_EditAttachment/fr.md).
3.  Cliquez sur **OK**.
4.  Un cône apparaît dans le corps actif.

## Options

Le Cône peut être éditée après sa création de deux façons :

-   Double-cliquez le dans l\'arborescence ou faire un clic droit dessus et sélectionnez **Éditer la primitive** dans le menu contextuel. Cela fait apparaître les paramètres des Primitives.
-   Via l\'[Éditeur de propriétés](Property_editor/fr.md).



## Propriétés

-    **Attachment**: définit les modes d\'ancrage ainsi que le décalage d\'ancrage. Voir [Part Ancrage](Part_EditAttachment/fr.md).

-    **Label**: donne le nom du cône, changer si nécessaire.

-    **Radius1**: valeur du rayon de la base du cône.

-    **Radius2**: valeur du rayon du sommet du cône tronquer. Si zéro le cône sera pointu.

-    **Height**: valeur du rayon du sommet du cône tronquer. Si zéro le cône sera pointu.

-    **Angle**: angle de rotation (360° pour un cône complet, 0 à 360° pour un quartier).





{{PartDesign_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveCone/fr
