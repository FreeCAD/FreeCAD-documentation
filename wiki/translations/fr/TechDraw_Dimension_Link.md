---
- GuiCommand:/fr
   Name:TechDraw Dimension Link
   Name/fr:TechDraw Lier une dimension
   MenuLocation:TechDraw → Dimensions →  Lier une cotation à une géométrie 3D
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md)
   SeeAlso:[TechDraw Vue](TechDraw_View/fr.md), [TechDraw Groupe de projection](TechDraw_ProjectionGroup/fr.md)
---

## Description

L\'outil Dimension Link crée un lien entre la géométrie 3D et une ou plusieurs dimensions projetées existantes sur une page. Ce lien permet à la dimension d\'utiliser des valeurs 3D réelles au lieu de valeurs projetées 2D.

L\'utilisation la plus courante de l\'outil Dimension Link est la cotation des vues isométriques dans un groupe de projection. La longueur projetée d\'un bord dans une vue isométrique ne sera bien sûr pas nécessairement égale à la longueur réelle du bord. Dans une vue orthogonale, les longueurs projetées et réelles seront égales.

Dimension Link demande à la dimension de calculer sa valeur directement à partir de la géométrie 3D.

## Utilisation

1.  Créez une cote appropriée sur la page de dessin en utilisant l\'un des outils [TechDraw Cote de longueur](TechDraw_Dimension_Length/fr.md), [TechDraw Cote horizontale](TechDraw_Dimension_Horizontal/fr.md), etc. Cette cote sera au bon endroit sur la page mais affichera la dimension de la valeur projetée.
2.  Sélectionnez la géométrie dans la vue 3D, par exemple une arête, qui correspond à la géométrie projetée de votre cote.
3.  Appuyez sur le bouton**<img src="images/TechDraw_Dimension_Link.svg" width=16px> [TechDraw Lier une cote à une géométrie 3D](TechDraw_Dimension_Link/fr.md)
**
4.  Une boîte de dialogue va s\'ouvrir. Sélectionnez 1 ou plusieurs dimensions à associer à la géométrie 3D sélectionnée.
5.  Appuyer sur **OK**.

Une fois l\'opération de liaison terminée, la propriété {{PropertyData/fr|MeasureType}} de la dimension passe de `Projected` à `True`.

## Limitations

1.  Les liens de dimension sont très sensibles au problème de \"nommage topologique\". Consultez les informations de l\'outil [TechDraw Cote de longueur](TechDraw_Dimension_Length/fr.md) pour plus d\'informations. Il est recommandé que les dimensions liées constituent l\'une des dernières étapes de votre processus de dessin.




1.  L\'outil Lien ne vous empêchera pas de créer des liens illogiques, vous devez donc choisir le bon bord dans la vue 3D lors de la création du lien.




1.  Il n\'y a actuellement aucun moyen de rompre un lien; vous pouvez redéfinir {{PropertyData/fr|MeasureType}} (type de dimension) sur `Projected`(projetée) et la dimension utilisera la valeur projetée au lieu de la valeur liée.

Notez que si la dimension à lier est basée sur deux sommets, vous devez en sélectionner deux dans la vue 3D. De même, si la dimension est basée sur une arête, vous devez sélectionner une arête dans la vue 3D.

## Propriétés

1.  La propriété MeasureType (type de dimension) d\'une dimension liée sera modifiée de \"Projected (projetée)\" à \"True (réelle)\".

## Script


**Voir aussi:**

[TechDraw API](TechDraw_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Lien de dimension peut être utilisé dans des [macros](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide des fonctions suivantes:


```python
to be defined
```





{{TechDraw Tools navi

}}  
