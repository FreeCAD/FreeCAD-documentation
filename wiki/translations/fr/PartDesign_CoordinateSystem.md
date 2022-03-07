---
- GuiCommand:/fr
   Name:PartDesign CoordinateSystem
   Name/fr:PartDesign Système de coordonnées local
   MenuLocation:Conception de pièces → Créer un système de coordonnées local
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   Version:0.18
   SeeAlso:[PartDesign Point de référence](PartDesign_Point/fr.md), [PartDesign Ligne de référence](PartDesign_Line/fr.md), [PartDesign Plan de référence](PartDesign_Plane/fr.md)
---

# PartDesign CoordinateSystem/fr

## Description

Crée un **système de coordonnées local** qui peut être utilisé comme référence pour une autre géométrie de référence. Cela aide également à identifier l\'orientation de la géométrie de référence dans un espace 3D. ![](images/PartDesign_LocalCoordinateSystem_Example.png ) 
*Système de coordonnées local provenant de l'origine d'un plan de référence.*

## Utilisation

1.  Appuyez sur le bouton **[<img src=images/PartDesign_CoordinateSystem.svg style="width:16px"> [Créer un système de coordonnées local](PartDesign_CoordinateSystem/fr.md)**.
2.  Définir les paramètres du système de coordonnées. Sélectionnez une première référence dans la vue 3D pour filtrer les modes de liaison disponibles.
3.  En fonction de la référence sélectionnée, un ou plusieurs modes de pièce jointe peuvent être disponibles dans la liste. Le plus probable sera automatiquement sélectionné et affiché en gras dans la liste. Le texte *Attaché avec le mode* ainsi que le nom du mode de pièce jointe apparaissent en vert en haut du panneau des paramètres.
4.  Pour ajouter une référence supplémentaire, appuyez sur le bouton **Référence** suivant. Une fois appuyé, son étiquette devient *Sélection en cours\...* jusqu\'à ce qu\'une sélection soit faite.
5.  Sélectionnez un mode de pièce jointe dans la liste.
6.  Définir les valeurs de décalage de pièce jointe.
7.  Appuyez sur **OK**.

## Options

Double-cliquez sur l\'étiquette **Local\_CS** dans l\'arborescence du modèle ou cliquez avec le bouton droit de la souris et sélectionnez **Modifier la référence** dans le menu contextuel pour modifier ses paramètres. Pour plus de détails sur le mode Ancrage et le décalage dans Ancrage, voir [Part Ancrage](Part_EditAttachment/fr.md).

## Propriétés

### Données

-    **MapMode**: Répertorie le mode d\'ancrage utilisé.

-    **Attachment Reversed**: Indique si le système de coordonnées est inversé en orientation.

-    **Attachment Offset**: Applique une transformation (translation et rotation) en référence à l\'emplacement de la référence.

-    **Placement**: Indique les coordonnées et l'alignement de l'origine du système de coordonnées.

-    **Label**: Nom donné à l\'objet, ce nom peut être modifié à tout moment.

## Script


```python
lcs = App.activeDocument().addObject( 'PartDesign::CoordinateSystem', 'LCS' )
```





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign CoordinateSystem/fr
