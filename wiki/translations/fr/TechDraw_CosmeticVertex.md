---
- GuiCommand:/fr
   Name:TechDraw CosmeticVertex
   Name/fr:TechDraw Point cosmétique
   MenuLocation:TechDraw → Add Vertices → Ajouter un sommet cosmétique
   Workbenches:[Atelier TechDraw](TechDraw_Workbench/fr.md)
   Version:0.19
   SeeAlso:[TechDraw Point milieu](TechDraw_Midpoints/fr.md), [TechDraw Sommets quadrants](TechDraw_Quadrants/fr.md)
---


</div>

## Description

L\'outil Point cosmétique ajoute un [Vertex](Glossary/fr#V.md) (sommet) qui ne fait pas partie de la géométrie d\'origine à une vue. Ce point se comporte comme n\'importe quel autre point et peut être utilisé pour le dimensionnement.

<img alt="" src=images/TechDraw_CosmeticVertex_Sample.png  style="width:300px;"> 
*Point cosmétique utilisé pour créer une dimension supplémentaire*

## Utilisation

1.  Sélectionnez une vue dans le dessin.
2.  Appuyez sur le bouton **<img src="images/TechDraw_CosmeticVertex.svg" width=16px> [Ajouter un sommet cosmétique](TechDraw_CosmeticVertex/fr.md)**.
3.  Une boîte de dialogue de tâche s\'ouvre. Il permet de définir l\'emplacement du sommet cosmétique en sélectionnant un point ou en saisissant un décalage x, y par rapport au centre de la vue sélectionnée.
4.  Pour choisir une position, appuyez sur le bouton **Point Picker**. Cliquez sur une position dans la vue et appuyez ensuite sur **OK** pour créer le point. Pour quitter la sélection de points sans créer de sommet cosmétique, appuyez sur le bouton **Escape picking** dans la boîte de dialogue.

Pour supprimer un sommet cosmétique (Cosmetic Vertex), sélectionnez-le et utilisez le bouton de la barre d\'outils **<img src="images/TechDraw_CosmeticEraser.svg" width=16px> [TechDraw Gomme](TechDraw_CosmeticEraser/fr.md)**.

**Remarque:** vous ne pouvez pas modifier l\'emplacement du Cosmetic Vertex après sa création. Pour le moment, il n\'y a pas d\'autre moyen que de le supprimer et d\'en créer un nouveau.

## Propriétés

Les points cosmétiques n\'ont pas de propriétés propres car ils ne sont pas des objets du document. Ils partagent les paramètres de couleur et de taille avec des points de géométrie réguliers.

## Script


**Voir aussi:**

[TechDraw API](TechDraw_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

Les points cosmétiques sont accessibles par les [macros](Macros/fr.md) ou par la console [Python](Python/fr.md).


```python
dvp = App.ActiveDocument.View
org = App.Vector(0.0, 0.0, 0.0)
dvp.makeCosmeticVertex(org);

#lines too!
start = FreeCAD.Vector (1.0, 5.0, 0.0)
end = FreeCAD.Vector(1.0, -5.0, 0.0)
style = 2
weight = 0.75
pyGreen = (0.0, 0.0, 1.0, 0.0)
dvp.makeCosmeticLine(start,end,style, weight, pyGreen)
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}  
