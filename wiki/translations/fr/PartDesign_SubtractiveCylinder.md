---
 GuiCommand:
   Name: PartDesign SubtractiveCylinder
   Name/fr: PartDesign Cylindre soustractif
   MenuLocation: Part Design , Créer une primitive soustractive , Cylindre soustractif
   Workbenches: PartDesign_Workbench/fr
   Version: 0.17
   SeeAlso: PartDesign_CompPrimitiveSubtractive/fr, PartDesign_AdditiveCylinder/fr
---

# PartDesign SubtractiveCylinder/fr

## Description

Insère un cylindre primitif soustractif dans le Corps actif. Sa forme est soustraite du solide existant.

![](images/PartDesign_SubtractiveCylinder_example.svg )

*À gauche, le corps actif (A) en gris et le cylindre soustractif (B) en rouge transparent ; le résultat final est à droite.*



## Utilisation

1.  Presser le bouton **<img src="images/PartDesign_SubtractiveCylinder.svg" width=24px> '''Cylindre soustractif'''**. **Remarque** : le Cylindre soustractif fait partie du menu d\'icônes appelé *Créer une primitive soustractive*. Après le lancement de FreeCAD, le cube soustractif est affiché par défaut dans la barre d\'outils. Pour obtenir le Cylindre soustractif, cliquer sur la flèche vers le bas et choisissez Cylindre soustractif dans le menu.
2.  Définir les paramètres primitifs et de l\'[ancrage](Part_EditAttachment/fr.md).
3.  Cliquer sur **OK**.
4.  Un cylindre apparaît dans le corps actif.

## Options

Il est possible de créer des cylindres biaisés en spécifiant des angles par rapport au vecteur normal de l\'ancrage choisi. {{Version/fr|0.20}}

Le Cylindre peut être édité après sa création de deux façons :

-   Double-cliquez le dans l\'arborescence ou faire un clic droit dessus et sélectionnez **Éditer la primitive** dans le menu contextuel. Cela fait apparaître les paramètres des Primitives.
-   Via l\'[Éditeur de propriétés](Property_editor/fr.md).



## Propriétés

-    **Attachment**: définit les modes d\'ancrage ainsi que le décalage d\'ancrage. Voir [Part Ancrage](Part_EditAttachment/fr.md).

-    **Label**: donne le nom du cylindre, changer si nécessaire.

-    **Radius**: valeur du rayon de la base du cylindre.

-    **Angle**: angle de rotation (360° pour un cylindre complet, 0 à 360° pour un quartier).

-    **Height**: hauteur du cylindre entre les deux faces.

-    **First Angle**: angle dans la première direction. {{Version/fr|0.20}}

-    **Second Angle**: angle dans la seconde direction. {{Version/fr|0.20}}





{{PartDesign_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveCylinder/fr
