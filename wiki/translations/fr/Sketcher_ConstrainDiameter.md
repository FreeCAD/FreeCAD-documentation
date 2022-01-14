---
- GuiCommand:/fr
   Name:Sketcher ConstrainDiameter
   Name/fr:Sketcher Contrainte diamètre
   MenuLocation:Sketch → Contraintes d'esquisse → Contraindre le diamètre
   Workbenches:[Sketcher](Sketcher_Workbench/fr.md)
   SeeAlso:[Sketcher Contrainte dimensionnelle](Sketcher_ConstrainDistance/fr.md), [Sketcher Contrainte de distance horizontale](Sketcher_ConstrainDistanceX/fr.md), [Sketcher Contrainte de distance verticale](Sketcher_ConstrainDistanceY/fr.md)
   Version:0.18
---

# Sketcher ConstrainDiameter/fr

## Description

Cette contrainte contraint la valeur du diamètre d\'un cercle ou d\'un arc à avoir une valeur spécifique. Si plus d\'un cercle ou d\'un arc est sélectionné avant de lancer la commande :

-   Si la contrainte est appliquée en mode \'Référence\', une nouvelle contrainte de référence est ajoutée à chaque objet séparément selon les règles ci-dessus.
-   Si la contrainte est appliquée en mode \'Normal\', les règles suivantes s\'appliquent
    -   Une contrainte de référence est appliquée séparément sur chaque objet qui est une géométrie externe.
    -   Des **[<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Contraintes d'égalité](Sketcher_ConstrainEqual/fr.md)** sont appliquées séquentiellement entre tous les objets de géométrie réelle/construction et une contrainte dimensionnelle est appliquée au premier objet sélectionné selon les règles ci-dessus.

NB : Les pôles B-spline ne peuvent pas être mélangés avec d\'autres types d\'objets dans la sélection.

## Comment l\'utiliser 

1.  Choisissez un ou plusieurs cercles ou arcs.
2.  Appuyez sur la touche **[<img src=images/Sketcher_ConstrainDiameter.svg style="width:16px"> [Contraindre le diamètre](Sketcher_ConstrainDiameter/fr.md)**
3.  Une boîte de dialogue s\'ouvre pour éditer ou confirmer la valeur. Appuyez sur **OK** pour valider. Si plusieurs cercles/arcs ont été sélectionnés, toutes les contraintes adopteront cette valeur. Modifiez leurs valeurs séparées en double-cliquant sur l\'étiquette de cote dans la vue 3D ou, dans la liste des contraintes, double-cliquez sur la contrainte ou cliquez avec le bouton droit de la souris et sélectionnez **Change value**.
4.  En option, l'étiquette de cote et la ligne peuvent être déplacées et pivotées dans la vue 3D en cliquant sur la valeur et en les faisant glisser tout en maintenant le bouton gauche de la souris enfoncé.

**Remarque:** l\'outil de contrainte peut également être démarré sans sélection préalable. Par défaut, la commande sera en mode Continu pour créer de nouvelles contraintes. Appuyez une fois sur le bouton droit de la souris ou sur **Echap** pour quitter la commande.

## Script


```pythonSketch.addConstraint(Sketcher.Constraint('Diameter', ArcOrCircle, App.Units.Quantity('123.0 mm')))```

La page [Sketcher : Écrire des scripts](Sketcher_scripting/fr.md) explique les valeurs qui peuvent être utilisées pour `ArcOrCircle` et contient d\'autres exemples sur la façon de créer des contraintes à partir de scripts Python.





{{Sketcher Tools navi

}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDiameter/fr
