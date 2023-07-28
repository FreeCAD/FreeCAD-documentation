---
- GuiCommand:/fr
   Name:Sketcher ConstrainBlock
   Name/fr:Sketcher Contrainte de blocage
   MenuLocation:Esquisse → Contraintes d'esquisse → Contrainte de blocage
   Workbenches:[Sketcher](Sketcher_Workbench/fr.md)
   Shortcut:**K** **B**
   Version:0.17
   SeeAlso:[Sketcher Contrainte fixe](Sketcher_ConstrainLock/fr.md)
---

# Sketcher ConstrainBlock/fr

## Description

La **Contrainte de blocage** permet de bloquer un élément en place à l\'aide d\'une seule contrainte.

Son principal usage est prévu pour les **[<img src=images/Sketcher_CreateBSpline.svg style="width:16px"> [B-splines](Sketcher_CreateBSpline/fr.md)** qui peuvent être difficiles à contraindre entièrement par ailleurs.



## Utilisation

1.  Sélectionner un élément à contraindre.
2.  Appuyer sur le bouton **[<img src=images/Sketcher_ConstrainBlock.svg style="width:16px"> [Contrainte de blocage](Sketcher_ConstrainBlock/fr.md)**.

Ou appuyez d\'abord sur le bouton, puis sélectionnez les éléments.



## Script


```pythonSketch.addConstraint(Sketcher.Constraint('Block', Edge))```

La page [Sketcher Scripts](Sketcher_scripting/fr.md) explique les valeurs qui peuvent être utilisées pour `Edge` et contient d\'autres exemples sur la façon de créer des contraintes à partir de scripts Python.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainBlock/fr
