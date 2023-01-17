---
- GuiCommand:/fr
   Name:Sketcher ConstrainRadius
   Name/fr:Sketcher Contrainte rayon
   MenuLocation:Esquisse → Contraintes d'esquisse → Contrainte de rayon ou de poids
   Workbenches:[Sketcher](Sketcher_Workbench/fr.md)
   Shortcut:**K** **R**
   SeeAlso:[Sketcher Contrainte dimensionnelle](Sketcher_ConstrainDistance/fr.md), [Sketcher Contrainte de distance en X](Sketcher_ConstrainDistanceX/fr.md), [Sketcher Contrainte de distance en Y](Sketcher_ConstrainDistanceY/fr.md)
---

# Sketcher ConstrainRadius/fr

## Description

Cette contrainte contraint la valeur du rayon d\'un cercle ou d\'un arc à avoir une valeur spécifique. Si plus d\'un cercle ou d\'un arc est sélectionné avant de lancer la commande :

-   Si la contrainte est appliquée en mode \"Référence\", une nouvelle contrainte de référence est ajoutée à chaque objet séparément selon les règles ci-dessus.
-   Si la contrainte est appliquée en mode \"Normal\", les règles suivantes s\'appliquent :
    -   Une contrainte de référence est appliquée séparément sur chaque objet qui est une géométrie externe.
    -   Des **[<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Contraintes d'égalités](Sketcher_ConstrainEqual/fr.md)** sont appliquées séquentiellement entre tous les objets de géométrie réelle/construction et une contrainte dimensionnelle est appliquée au premier objet sélectionné selon les règles ci-dessus.

NB : les pôles des B-splines ne peuvent pas être mélangés avec d\'autres types d\'objets dans la sélection.

![](images/Sketcher_ConstrainRadius_example.png )



## Utilisation

1.  Sélectionnez un ou plusieurs cercles ou arcs.
2.  Appuyez sur la touche **[<img src=images/Sketcher_ConstrainRadius.svg style="width:16px"> [Contrainte de rayon](Sketcher_ConstrainRadius/fr.md)**.
3.  Une boîte de dialogue s\'ouvre pour éditer ou confirmer la valeur. Appuyez sur **OK** pour valider. Si plusieurs cercles / arcs ont été sélectionnés, toutes les contraintes adopteront cette valeur. Modifiez leurs valeurs séparément en double-cliquant sur l\'étiquette de cote dans la vue 3D. ou, dans la liste des contraintes, double-cliquez sur la contrainte ou cliquez avec le bouton droit de la souris et sélectionnez **Modifier la valeur**.
4.  En option, l'étiquette de cote et la ligne peuvent être déplacées et pivotées dans la vue 3D en cliquant sur la valeur et en les faisant glisser tout en maintenant le bouton gauche de la souris enfoncé.

**Remarque :** l\'outil de contrainte peut également être démarré sans sélection préalable. Par défaut, la commande sera en mode Continu pour créer de nouvelles contraintes. Appuyez une fois sur le bouton droit de la souris ou sur **Echap** pour quitter la commande.



## Script


```pythonSketch.addConstraint(Sketcher.Constraint('Radius', ArcOrCircle, App.Units.Quantity('123.0 mm')))```

La page [Sketcher Scripts](Sketcher_scripting/fr.md) explique les valeurs qui peuvent être utilisées pour `ArcOrCircle` et contient d\'autres exemples sur la façon de créer des contraintes à partir de scripts Python.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainRadius/fr
