---
- GuiCommand:/fr
   Name:PartDesign SubtractivePrism
   Name/fr:PartDesign Prisme soustractif
   MenuLocation:Part Design → Créer une primitive soustractive → Prisme soustractif
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   Version:0.17
   SeeAlso:[PartDesign Primitives soustractives](PartDesign_CompPrimitiveSubtractive/fr.md), [PartDesign Prisme additif](PartDesign_AdditivePrism/fr.md)
---

# PartDesign SubtractivePrism/fr

## Description

Insère un Prisme soustractif dans le corps actif. Sa forme est soustraite du solide existant.

![](images/PartDesign_SubtractivePrism_example.svg )

À Gauche : le Corps actif est en gris et le prisme soustractif est en rouge transparent ; le résultat final est à droite.



## Utilisation

1.  Pressez le bouton **<img src="images/PartDesign_SubtractivePrism.svg" width=24px> '''Prisme soustractif'''**. **Remarque** : Le Prisme soustractif fait partie du menu d\'icônes appelé *Créer une primitive soustractive*. Après le lancement de FreeCAD, le cube soustractif est affiché par défaut dans la barre d\'outils. Pour obtenir le Prisme soustractif, cliquez sur la flèche vers le bas et choisissez Prisme soustractif dans le menu.
2.  Définir les paramètres primitifs et de l\'[ancrage](Part_EditAttachment/fr.md).
3.  Cliquez sur **OK**.
4.  Un prisme apparaît dans le corps actif.

## Options

Il est possible de créer des prismes biaisés en spécifiant des angles par rapport au vecteur normal de l\'ancrage choisi.

Le Prisme peut être éditée après sa création de deux façons :

-   Double-cliquez le dans l\'arborescence ou faire un clic droit dessus et sélectionnez **Éditer la primitive** dans le menu contextuel. Cela fait apparaître les paramètres des Primitives.
-   Via l\'[Éditeur de propriétés](Property_editor/fr.md).



## Propriétés

-    **Attachment**: définit les modes d\'ancrage ainsi que le décalage d\'ancrage. Voir [Part Ancrage](Part_EditAttachment/fr.md).

-    **Label**: donne le nom du Prisme, changez le si nécessaire.

-    **Polygon**: nombre de cotés de la section du polygone.

-    **Circumradius**: [rayon circonscrit](https://fr.wikipedia.org/wiki/Cercle_circonscrit) du polygone de la section du prisme.

-    **Height**: hauteur du prisme.

-    **First Angle**: angle dans la première direction.

-    **Second Angle**: angle dans la deuxième direction.





{{PartDesign_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractivePrism/fr
