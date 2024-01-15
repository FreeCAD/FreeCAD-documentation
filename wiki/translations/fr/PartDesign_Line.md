---
 GuiCommand:
   Name: PartDesign Line
   Name/fr: PartDesign Ligne de référence
   MenuLocation: Part Design , Créer une référence , Créer une ligne de référence
   Workbenches: PartDesign_Workbench/fr
   Version: 0.17
   SeeAlso: PartDesign_Point/fr, PartDesign_Plane/fr
---

# PartDesign Line/fr

## Description

Crée une **Ligne de référence** qui peut être utilisée comme référence pour les esquisses, les autres géométries de référence ou les fonctions. Par exemple, elle peut être utilisée comme axe de révolution pour les fonctions Révolution et Rainure circulaire.

<img alt="" src=images/datum_line.png  style="width:600px;"> 
*Deux lignes de référence à travers les coins opposés du cube se rencontrent au centre de la masse.*



## Utilisation

1.  Appuyez sur le bouton **<img src="images/PartDesign_Line.svg" width=24px> '''Créer une ligne de référence'''** .
2.  Définir les paramètres de la droite. Sélectionnez une première référence dans la vue 3D pour filtrer les modes de référence disponibles.
3.  Selon la référence sélectionnée, il peut y avoir un ou plusieurs modes d\'ancrage disponibles dans la liste. Le plus probable sera automatiquement sélectionné et affiché en gras dans la liste. Le texte *Ancré avec le mode* ainsi que le nom du mode d\'ancrage apparaissent en vert en haut du panneau Paramètres.
4.  Pour ajouter une référence supplémentaire, appuyez sur le bouton suivant **Référence**. Une fois le bouton appuyé, son étiquette devient *Sélection\...* jusqu\'à ce qu\'une sélection soit faite.
5.  Sélectionnez un mode d\'ancrage dans la liste.
6.  Définissez les valeurs de décalage d\'ancrage.
7.  Appuyez sur **OK**.

## Options

Double-cliquez sur l\'étiquette DatumLine dans l\'arborescence du modèle ou cliquez avec le bouton droit de la souris et sélectionnez **Modifier la référence** dans le menu contextuel pour éditer ses paramètres. Pour plus de détails sur le mode d\'ancrage et le décalage de l\'ancrage, voir [Part Ancrage](Part_EditAttachment/fr.md).



## Propriétés

-    **MapMode**: répertorie le mode d\'ancrage utilisé.

-    **Attachment Offset**: applique une transformation (translation et rotation) en référence au placement de l\'ancrage.

-    **Label**: nom donné à l\'objet, ce nom peut être changé à la convenance.





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Line/fr
