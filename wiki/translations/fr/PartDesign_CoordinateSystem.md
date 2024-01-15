---
 GuiCommand:
   Name: PartDesign CoordinateSystem
   Name/fr: PartDesign Système de coordonnées local
   MenuLocation: Part Design , Créer un système de coordonnées local
   Workbenches: PartDesign_Workbench/fr
   Version: 0.18
   SeeAlso: PartDesign_Point/fr, PartDesign_Line/fr, PartDesign_Plane/fr
---

# PartDesign CoordinateSystem/fr

## Description

Crée un **système de coordonnées local** qui peut être utilisé comme référence pour une autre géométrie de référence. Cela aide également à identifier l\'orientation de la géométrie de référence dans un espace 3D. ![](images/PartDesign_LocalCoordinateSystem_Example.png ) 
*Système de coordonnées local provenant de l'origine d'un plan de référence.*



## Utilisation

1.  Cliquer sur le bouton **[<img src=images/PartDesign_CoordinateSystem.svg style="width:16px"> [Créer un système de coordonnées local](PartDesign_CoordinateSystem/fr.md)**.
2.  Pour définir les paramètres du système de coordonnées, sélectionner une première référence dans la vue 3D pour filtrer les modes d\'ancrage disponibles.
3.  En fonction de la référence sélectionnée, un ou plusieurs modes d\'ancrage peuvent être disponibles dans la liste. Le plus probable sera automatiquement sélectionné et affiché en gras dans la liste. Le texte *Ancré avec le mode* ainsi que le nom du mode d\'ancrage apparaissent en vert en haut du panneau des paramètres.
4.  Pour ajouter une référence supplémentaire, appuyez sur le bouton **Référence** suivant. Une fois appuyé, son étiquette devient *Sélection de\...* jusqu\'à ce qu\'une sélection soit faite.
5.  Sélectionner un mode d\'ancrage dans la liste.
6.  Définir les valeurs de décalage d\'ancrage.
7.  Appuyer sur **OK**.

## Options

Double-cliquez sur l\'étiquette **Local_CS** dans la vue en arborescence du modèle ou cliquez avec le bouton droit de la souris et sélectionnez **Modifier la référence** dans le menu contextuel pour modifier ses paramètres. Pour plus de détails sur le mode d\'ancrage et le décalage de l\'ancrage, voir [Part Ancrage](Part_EditAttachment/fr.md).



## Propriétés



### Données

-    **MapMode**: répertorie le mode d\'ancrage utilisé.

-    **Attachment Reversed**: indique si le système de coordonnées est inversé en orientation.

-    **Attachment Offset**: applique une transformation (translation et rotation) en référence à l\'emplacement de l\'ancrage.

-    **Placement**: indique les coordonnées et l'alignement de l'origine du système de coordonnées.

-    **Label**: nom donné à l\'objet, ce nom peut être modifié à tout moment.



## Script


```python
lcs = App.activeDocument().addObject( 'PartDesign::CoordinateSystem', 'LCS' )
```





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign CoordinateSystem/fr
