---
- GuiCommand:
   Name:PartDesign SubtractiveCone
   Name/fr:PartDesign Cône soustractif
   MenuLocation:Part Design → Créer une primitive soustractive → Cône soustractif
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   Version:0.17
   SeeAlso:[PartDesign Primitives soustractives](PartDesign_CompPrimitiveSubtractive/fr.md), [PartDesign Cône additif](PartDesign_AdditiveCone/fr.md)
---

# PartDesign SubtractiveCone/fr

## Description

Insère un Cône primitif soustractif dans le Corps actif. Sa forme est soustraite du solide existant.

![](images/PartDesign_SubtractiveCone_example.png )

*À gauche : le corps actif (A) montré en gris et le cône soustractif (B) est en rouge transparent; le résultat final est à droite.*

## Utilisation

1.  Pressez le bouton **<img src="images/PartDesign_AdditiveCone.svg" width=24px> '''Cône Soustractif'''**. **Remarque** : le Cône soustractif fait partie du menu d\'icônes appelé *Créer une primitive soustractive*. Après le lancement de FreeCAD, le cube soustractif est affiché par défaut dans la barre d\'outils. Pour obtenir le Cône soustractif, cliquer sur la flèche vers le bas et choisissez Cône soustractif dans le menu.
2.  Définissez les paramètres de la primitive (pour un cône complet, mettez un des rayons à zéro) et l\'[Ancrage](Part_EditAttachment/fr.md).
3.  Cliquez sur **OK**.
4.  Un cône apparaît dans le corps actif.

## Options

Le Cône peut être édité après sa création de deux façons :

-   Double-cliquez le dans l\'arborescence ou faire un clic droit dessus et sélectionnez **Éditer la primitive** dans le menu contextuel. Cela fait apparaître les paramètres des Primitives.
-   Via l\'[Éditeur de propriétés](Property_editor/fr.md).

## Propriétés

-    **Attachment**: définit les modes d\'ancrage ainsi que le décalage d\'ancrage. Voir [Part Ancrage](Part_EditAttachment/fr.md).

-    **Label**: donne le nom du cône, changer si nécessaire.

-    **Radius1**: valeur du rayon de la base du cône.

-    **Radius2**: valeur du rayon du sommet du cône tronqué. Une valeur non nulle crée un cône tronqué.

-    **Height**: hauteur du cône le long de son axe.

-    **Angle**: angle de rotation de la section transversale (360° pour un cône complet).





{{PartDesign_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveCone/fr
