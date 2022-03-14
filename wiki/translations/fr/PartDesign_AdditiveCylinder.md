---
- GuiCommand:/fr
   Name:PartDesign AdditiveCylinder
   Name/fr:PartDesign Cylindre additif
   MenuLocation:Conception de pièces → Créer une primitive additive → Cylindre additif
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   Version:0.17
   SeeAlso:[Créer une primitive d'addition](PartDesign_CompPrimitiveAdditive/fr.md), [Cylindre soustractif](PartDesign_SubtractiveCylinder/fr.md)
---

# PartDesign AdditiveCylinder/fr

## Description

Insère un Cylindre primitif dans un corps actif comme première fonction, ou le fusionne aux autres fonctions existantes.

<img alt="" src=images/PartDesign_AdditiveCylinder_example.png  style="width:200px;">

## Utilisation

1.  Presser le bouton **<img src="images/PartDesign_AdditiveCylinder.svg" width=24px> '''Cylindre Additif'''**. **Remarque** : Le Cylindre additif fait partie d\'un menu déroulant d\'icônes appelé \"Créer une primitive additive\". Après démarrage de FreeCAD , le cylindre additif est le second affiché dans la barre d\'outils. Pour atteindre le bouton Cylindre, cliquer sur le bouton flèche vers le bas et choisissez le cylindre additif dans le menu.
2.  Renseigner les paramètres de la primitive et de l\'[ancrage](Part_EditAttachment/fr.md).
3.  Clic **OK**.
4.  Un cylindre apparaît dans le corps actif.

## Options


{{PartDesign Tools navi/fr}}

Le Cylindre peut être édité après sa création de deux façons :

-   Double-cliquez le dans l\'arborescence ou faire un clic droit dessus et sélectionnez **Éditer la primitive** dans le menu contextuel. Cela fait apparaître les paramètres des Primitives.
-   Via l\'[Éditeur de propriétés](Property_editor/fr.md).

## Propriétés

-    {{PropertyData/fr|Attachment}}: définit les modes d\'ancrage ainsi que le décalage d\'ancrage. Voir [Part Ancrage](Part_EditAttachment/fr.md).

-    {{PropertyData/fr|Label}}: donne le nom du cylindre, changer si nécessaire.

-    {{PropertyData/fr|Radius}}: c\'est la valeur du rayon de la base du cylindre.

-    {{PropertyData/fr|Angle}}: angle de rotation (360° pour un cylindre complet, 0 à 360° pour un quartier).

-    {{PropertyData/fr|Height}}: la hauteur du cylindre entre les deux faces.

-    {{PropertyData/fr|First Angle}}: angle dans la première direction. {{Version/fr|0.20}}

-    {{PropertyData/fr|Second Angle}}: angle dans la seconde direction. {{Version/fr|0.20}}





{{PartDesign_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveCylinder/fr
