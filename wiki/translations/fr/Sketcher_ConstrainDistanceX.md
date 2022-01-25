---
- GuiCommand:/fr
   Name:Sketcher ConstrainDistanceX
   Name/fr:Sketcher Contrainte distance en X
   MenuLocation:Sketch → Contraintes d'esquisse → Contrainte distance horizontale
   Workbenches:[Sketcher](Sketcher_Workbench/fr.md)
   Shortcut:**Maj** + **H**
   SeeAlso:[Sketcher Contrainte dimensionnelle](Sketcher_ConstrainDistance/fr.md), [Sketcher Contrainte distance verticale](Sketcher_ConstrainDistanceY/fr.md)
---

# Sketcher ConstrainDistanceX/fr

## Description

Fixe la distance verticale entre 2 points ou fin de lignes. Si un seul point est sélectionné, la distance sera définie par rapport à l\'origine de l\'esquisse.

![](images/Constraint_H_Distance.png )

## Utilisation

1.  Choisissez un ou deux points ou une ligne.
2.  Appelez l\'outil de plusieurs manières:
    -   Appuyez sur le bouton **[<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> [Fixer la distance horizontale...](Sketcher_ConstrainDistanceX/fr.md)** dans la barre d\'outils.
    -   Utilisez le raccourci clavier **Maj** + **H**. (**H** est pour **H**orizontal)
    -   Utilisez **Sketch → Contraintes d'esquisse → [<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> Contrainte distance horizontale** dans le menu supérieur.
3.  Une boîte de dialogue contextuelle s\'ouvre pour modifier ou confirmer la valeur. Appuyez sur **OK** pour valider.

**Remarque :** l\'outil de contrainte peut également être démarré sans sélection préalable, mais nécessitera la sélection de 2 points ou d\'une ligne. Pour définir une distance par rapport à l\'origine, le point d\'origine de l\'esquisse devra également être sélectionné. Par défaut, la commande sera en mode continu afin de créer de nouvelles contraintes; appuyez sur le bouton droit de la souris ou sur **ÉCHAP** pour quitter la commande.

## Script

Distance depuis l\'origine :


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceX', Edge, PointOfEdge, App.Units.Quantity('123.0 mm')))```

Distance entre deux sommets :


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceX', Edge1, PointOfEdge1, Edge2, PointOfEdge2, App.Units.Quantity('123.0 mm')))```

Étendue horizontale de la ligne (l\'interface graphique permet de sélectionner l\'arête elle-même, mais ce n\'est qu\'un raccourci pour utiliser les deux extrémités de la même ligne):


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceX', Line, 1, Line, 2, App.Units.Quantity('123.0 mm')))```

La page [Sketcher : Écrire des scripts](Sketcher_scripting/fr.md) explique les valeurs qui peuvent être utilisées pour `Edge1`, `Edge2`, `Edge`, ` PointOfEdge1`, ` PointOfEdge2`, `PointOfEdge` et `Line` et contient d\'autres exemples sur la façon de créer des contraintes à partir de scripts Python.





{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDistanceX/fr
