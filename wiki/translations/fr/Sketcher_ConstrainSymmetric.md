---
- GuiCommand:/fr
   Name:Sketcher ConstrainSymmetric
   Name/fr:Sketcher Contrainte symétrique
   MenuLocation:Esquisse → Contraintes d'esquisse → Contrainte symétrique
   Workbenches:[Sketcher](Sketcher_Workbench/fr.md)
   Shortcut:**S**
   SeeAlso:[Sketcher Contrainte parallèle](Sketcher_ConstrainParallel/fr.md)
---

# Sketcher ConstrainSymmetric/fr

## Description

La **Contrainte symétrique** contraint deux points sélectionnés à devenir symétriques à une ligne donnée, à savoir, deux points sélectionnés sont contraints de se situer sur une normale (ligne) passant par les deux points et sont contraints d\'être équidistants à la normale (ligne). Alternativement, elle peut contraindre deux points à être symétriques par rapport à un troisième.



## Utilisation

<img alt="" src=images/SymmetricConstraint1.png  style="width:500px;">

Sélectionnez deux points (sommets) dans l\'esquisse et une ligne dans l\'esquisse. Les points sélectionnés et la ligne seront vert foncé.

<img alt="" src=images/SymmetricConstraint2.png  style="width:500px;">

Cliquez sur **[<img src=images/Sketcher_ConstrainSymmetric.svg style="width:16px"> [Constrain symmetric](Sketcher_ConstrainSymmetric.md)** ou sélectionnez l\'option Contrainte symétrique dans le sous-menu Contraintes d\'esquisse d\'Esquisse de l\'atelier Sketcher (ou Part Design).

Ceci appliquera la contrainte aux éléments sélectionnés.

<img alt="" src=images/SymmetricConstraint3.png  style="width:500px;">


**Remarque :**

avant la version 0.19 (voir correctif [1](https://github.com/FreeCAD/FreeCAD/pull/3746)), si vous souhaitiez définir une contrainte de symétrie par rapport à un point, l\'ordre de la sélection était important, selon que vous sélectionniez l\'outil avant ou après.

-   si vous cliquiez d\'abord sur l\'outil : sélectionnez le premier point, puis le point de référence de la symétrie et enfin le deuxième point.
-   si vous cliquiez sur l\'outil en dernier : sélectionnez le premier point, puis le deuxième point et enfin le point de référence de symétrie.

Voir le tracker [issue #4144](https://freecadweb.org/tracker/view.php?id=4144), et [forum thread](https://forum.freecadweb.org/viewtopic.php?f=3&t=39611).



## Script

Deux points et une ligne de symétrie :


```pythonSketch.addConstraint(Sketcher.Constraint('Symmetric', Line1, PointOfLine1, Line2, PointOfLine2, SymmetryLine))```

Deux points et un point de symétrie :


```pythonSketch.addConstraint(Sketcher.Constraint('Symmetric', Line1, PointOfLine1, Line2, PointOfLine2, LineS, PointOfLineS))```

Une ligne et un point de symétrie (dans l\'interface graphique, on peut sélectionner une ligne et un point. Cela utilise en interne la même forme que ci-dessus avec les deux extrémités de la même ligne) :


```pythonSketch.addConstraint(Sketcher.Constraint('Symmetric', Line, 1, Line, 2, LineS, PointOfLineS))```

La page [Sketcher Scripts](Sketcher_scripting/fr.md) explique les valeurs qui peuvent être utilisées pour `Line1`, `Line2`, `LineS`, `Line`, `PointOfLine1`, `PointOfLine2` et `PointOfLineS` et contient d\'autres exemples sur la façon de créer des contraintes à partir de scripts Python.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainSymmetric/fr
