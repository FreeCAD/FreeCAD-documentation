---
- GuiCommand   */fr
   Name   *PartDesign Point
   Name/fr   *PartDesign Point de référence
   MenuLocation   *Part Design → Créez une référence → Créer un point de référence
   Workbenches   *[PartDesign](PartDesign_Workbench/fr.md)
   Version   *0.17
   SeeAlso   *[PartDesign Droite de référence](PartDesign_Line/fr.md), [PartDesign Plan de référence](PartDesign_Plane/fr.md)
---

# PartDesign Point/fr

## Description

Crée un **point de référence** qui peut être utilisé comme référence pour les esquisses ou toute autre géométrie de référence.

![](images/DatumPoint.png ) 
*Un point de référence attaché à une sphère avec un décalage d'ancrage de {{Value|2* dans la direction Z.}}

## Utilisation

1.  Appuyez sur le bouton **<img src="images/PartDesign_Point.svg" width=24px> '''Créer un point de référence'''** .
2.  Définissez les paramètres du point. Sélectionnez une première référence dans la vue 3D pour filtrer les modes d\'ancrage disponibles.
3.  Selon la référence sélectionnée, il peut y avoir un ou plusieurs modes d\'ancrage disponibles dans la liste. Le plus probable sera automatiquement sélectionné et affiché en gras dans la liste. Le texte *Mode d\'ancrage* ainsi que le nom du mode d\'ancrage apparaissent en vert en haut du panneau Paramètres.
4.  Pour ajouter une référence supplémentaire, appuyez sur le bouton suivant **Référence**. Une fois le bouton appuyé, son étiquette devient *Sélection\...* jusqu\'à ce qu\'une sélection soit faite.
5.  Sélectionnez un mode d\'ancrage dans la liste.
6.  Définissez les valeurs de décalage d\'ancrage.
7.  Appuyez sur **OK**.

## Options

Double-cliquez sur l\'étiquette Point de référence dans l\'arborescence du modèle ou cliquez avec le bouton droit de la souris et sélectionnez **Modifier la référence** dans le menu contextuel pour éditer ses paramètres. Pour plus de détails sur le mode de référencement et le décalage de la référence, voir [Part Ancrage](Part_EditAttachment/fr.md).

## Propriétés

-    **MapMode**   * répertorie le mode d\'ancrage utilisé.

-    **Attachment Offset**   * applique une transformation (translation et rotation) en référence au placement de l\'ancrage.

-    **Label**   * nom donné à l\'objet, ce nom peut être changé à la convenance.

## Limitations

-   Le point de référence ne peut pas être utilisé comme section pour les fonctions Balayage et Lissage.





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Point/fr
