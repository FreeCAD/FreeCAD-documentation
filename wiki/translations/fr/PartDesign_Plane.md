---
- GuiCommand:/fr
   Name:PartDesign Plane
   Name/fr:PartDesign Plan de référence
   MenuLocation:Conception de pièces → Créez une référence → Créer un plan de référence
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   Version:0.17
   SeeAlso:[PartDesign Point de référence](PartDesign_Point/fr.md), [PartDesign Ligne de référence](PartDesign_Line/fr.md)
---

## Description

Crée un **plan de référence** qui peut être utilisé comme référence pour les esquisses ou toute autre géométrie de référence. Les esquisses peuvent être attachées aux plans de référence. ![](images/Datum_plane.png ) *Plan de référence traversant les 3 coins du cube avec sur le dessus l\'esquisse d\'un cylindre en utilisant le plan de référence X-Y.*

## Prérequis

Un plan de référence, à partir de FreeCAD 0.18, ne peut être créé qu'à l'intérieur d'un <img alt="" src=images/PartDesign_Body.svg  style="width:16px;"> [Corps](PartDesign_Body/fr.md). Chaque corps a une origine qui est masquée par défaut. Pour pouvoir faire référence aux plans de base d\'origine, rendez visible l\'origine. Vous pouvez le faire avant de créer un plan de référence.

## Utilisation

1.  Appuyez sur le bouton **<img src="images/PartDesign_Plane.svg" width=16px> [Créer un nouveau plan de référence](PartDesign_Plane/fr.md)**.
2.  Définissez les paramètres du plan. Sélectionnez une première référence dans la vue 3D pour filtrer les modes [Part Ancrage](Part_EditAttachment/fr.md) disponibles.
3.  En fonction de la référence sélectionnée, un ou plusieurs modes d\'ancrage de pièces peuvent être disponibles dans la liste. Le plus probable sera automatiquement sélectionné et affiché en gras dans la liste. Le texte *Ancré avec le mode* ainsi que le nom du mode d\'ancrage de la pièce apparaissent en vert en haut du panneau Paramètres.
4.  Pour ajouter une référence supplémentaire, appuyez sur le bouton **Référence** suivant. Une fois appuyé, son étiquette devient *Sélection en cours\...* jusqu\'à ce qu\'une sélection soit faite.
5.  Sélectionnez un mode d\'ancrage de la pièce dans la liste.
6.  **Offsets:** Définit les valeurs d\'ancrage de décalage. **Remarquez** que les décalages x, y et z représentent le système de coordonnées local du plan de référence, pas le système de coordonnées mondial. Par conséquent, le décalage z est toujours le décalage le long du vecteur normal du plan de référence.
7.  **Rotation:** Changer \"Autour de l\'axe x\" fait tourner le plan autour de son axe X local. Changer \"Autour de l\'axe y\" fait tourner le plan autour de son axe Y local. Changer \"Autour de l\'axe z\" fait pivoter le plan autour de son axe Z local.
8.  Appuyez sur **OK**.

## Options

Double-cliquez sur l\'étiquette DatumPlane dans l\'arborescence du modèle ou cliquez avec le bouton droit de la souris et sélectionnez **Modifier la référence** dans le menu contextuel pour modifier ses paramètres. Pour plus de détails sur le mode d\'ancrage et le décalage de l\'ancrage, voir [Part Ancrage](Part_EditAttachment/fr.md).

## Propriétés

-    {{PropertyData/fr|MapMode}}: répertorie le mode d\'ancrage utilisé.

-    {{PropertyData/fr|Attachment Offset}}: applique une transformation (translation et rotation) en référence au placement de l\'ancrage.

-    {{PropertyData/fr|Label}}: nom donné à l\'objet, ce nom peut être changé à la convenance.





{{PartDesign Tools navi

}} 
