---
- GuiCommand:/fr
   Name:Sketcher ConstrainInternalAlignment
   Name/fr:Sketcher Contrainte d'alignement interne
   MenuLocation:Esquisse → Contraintes d'esquisse → Contrainte d'alignement interne
   Workbenches:[Sketcher](Sketcher_Workbench/fr.md)
   Shortcut:
   Version:0.15
   SeeAlso:[Sketcher Basculer géométrie interne](Sketcher_RestoreInternalAlignmentGeometry/fr.md), [Sketcher Ellipse](Sketcher_CreateEllipseByCenter/fr.md)
---

# Sketcher ConstrainInternalAlignment/fr

## Description

Cette Contrainte d\'alignement interne aligne les lignes et les points à des endroits particuliers d\'un élément complexe d\'esquisse (il y a juste un élément \"complexe\" jusqu\'à présent, l\'[Ellipse](Sketcher_CreateEllipseByCenter/fr.md)).

Pour l\'**[<img src=images/Sketcher_CreateEllipseByCenter.svg style="width:16px"> [Ellipse](Sketcher_CreateEllipseByCenter/fr.md)** et l\'**[<img src=images/Sketcher_CreateArcOfEllipse.svg style="width:16px"> [Arc d'ellipse](Sketcher_CreateArcOfEllipse/fr.md)**, l\'outil prend en charge les lignes contraignantes pour devenir des diamètres majeurs et mineurs et contraint les **[<img src=images/Sketcher_CreatePoint.svg style="width:16px"> [points](Sketcher_CreatePoint/fr.md)** aux positions des foyers de l\'ellipse.

La contrainte s\'adresse aux utilisateurs expérimentés car son utilisation n\'est pas aussi simple que pour les autres contraintes. Il existe un outil d\'aide appelé **[<img src=images/Sketcher_RestoreInternalAlignmentGeometry.svg style="width:16px"> [Afficher/Masquer géométrie interne](Sketcher_RestoreInternalAlignmentGeometry/fr.md)** qui évite d\'avoir à appeler la Contrainte d\'alignement interne manuellement.



## Opération sur une ellipse 

1.  Sélectionnez les éléments à aligner et une ellipse. L\'ellipse doit être sélectionnée en dernier. Jusqu\'à deux lignes et jusqu\'à deux points sont acceptés.
2.  Lancer la contrainte peut se faire de plusieurs manières :
    -   En appuyant sur le bouton **[<img src=images/Sketcher_ConstrainInternalAlignment.svg style="width:16px"> [Contrainte d'alignement interne](Sketcher_ConstrainInternalAlignment/fr.md)** dans la barre d\'outils.
    -   Utilisation de l\'entrée **Esquisse → Contraintes d'esquisse → [<img src=images/Sketcher_ConstrainInternalAlignment.svg style="width:16px"> Contrainte d'alignement interne** dans le menu supérieur.

La première ligne qui a été sélectionnée s\'aligne pour devenir le diamètre majeur de l\'ellipse (mais si ce n\'est pas déjà occupé par une autre ligne, sinon il deviendra le diamètre mineur). La deuxième ligne est aligné pour devenir le rayon mineur. Les lignes sont automatiquement passés en mode [construction](Sketcher_ToggleConstruction/fr.md).

De même, le premier point est contraint à devenir le premier foyer inoccupé, et le second point va à l\'autre foyer.

**Remarque :** par défaut, les nouvelles ellipses ont une géométrie de construction interne. Lorsque cela définit déjà complètement l\'ellipse, vous ne pouvez pas utiliser directement la contrainte Contrainte d\'alignement interne. Vous devez d\'abord supprimer la géométrie de construction ou des parties de celle-ci. Si vous ne voyez pas la géométrie de construction, sélectionnez l\'ellipse et utilisez l\'outil **[<img src=images/Sketcher_RestoreInternalAlignmentGeometry.svg style="width:16px"> [Afficher/Masquer géométrie interne](Sketcher_RestoreInternalAlignmentGeometry/fr.md)** pour la rendre visible .



## Script


```python
Sketch.addConstraint(Sketcher.Constraint('InternalAlignment:EllipseMajorDiameter', index_of_line, index_of_ellipse))
Sketch.addConstraint(Sketcher.Constraint('InternalAlignment:EllipseMinorDiameter', index_of_line, index_of_ellipse))
Sketch.addConstraint(Sketcher.Constraint('InternalAlignment:EllipseFocus1', index_of_point, 1, index_of_ellipse))
Sketch.addConstraint(Sketcher.Constraint('InternalAlignment:EllipseFocus2', index_of_point, 1, index_of_ellipse))
```

Remarques :

:   
    `Sketch`est un objet d\'esquisse.

:   Le nombre `1` dans les appels de ciblage représente le point de départ d\'un élément de point (il est ignoré).

:   L\'argument `index_of_point` doit être un point, il ne peut pas être utilisé pour indiquer par exemple l\'extrémité d\'un bord.

La page [Sketcher Scripts](Sketcher_scripting/fr.md) explique les valeurs qui peuvent être utilisées pour `index_of_line`, `index_of_point` et `index_of_ellipse` et contient d\'autres exemples sur la façon de créer des contraintes à partir de scripts Python.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainInternalAlignment/fr
