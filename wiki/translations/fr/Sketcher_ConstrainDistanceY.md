---
 GuiCommand:
   Name: Sketcher ConstrainDistanceY
   Name/fr: Sketcher Contrainte de distance en Y
   MenuLocation: Esquisse , Géométries d'esquisse , Contrainte de distance verticale
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **I**
   SeeAlso: Sketcher_ConstrainDistanceX/fr, Sketcher_ConstrainDistance/fr
---

# Sketcher ConstrainDistanceY/fr

## Description

Fixe la distance verticale entre 2 points ou extrémités de lignes. Si un seul point est sélectionné, la distance est définie par rapport à l\'origine de l\'esquisse.

![](images/Sketcher_ConstraintDistanceY_example.png )



## Utilisation

1.  Choisissez un ou deux points ou une ligne.
2.  Lancez l\'outil de plusieurs manières:
    -   Appuyez sur le bouton **[<img src=images/Sketcher_ConstrainDistanceY.svg style="width:16px"> [Contrainte distance verticale](Sketcher_ConstrainDistanceY/fr.md)** dans la barre d\'outils.
    -   Utilisez le raccourci clavier **I**
    -   Utilisez **Esquisse → Contraintes d'esquisse → [<img src=images/Sketcher_ConstrainDistanceY.svg style="width:16px"> Contrainte distance verticale** dans le menu supérieur.
3.  Une boîte de dialogue contextuelle s\'ouvre pour modifier ou confirmer la valeur. Appuyez sur **OK** pour valider.

**Remarque :** l\'outil de contrainte peut également être démarré sans sélection préalable, mais nécessitera la sélection de 2 points ou d\'une ligne. Pour définir une distance par rapport à l\'origine, le point d\'origine de l\'esquisse devra également être sélectionné. Par défaut, la commande sera en mode continu afin de créer de nouvelles contraintes; appuyez sur le bouton droit de la souris ou sur **Echap** pour quitter la commande.



## Script

Distance depuis l\'origine :


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceY', Edge, PointOfEdge, -1, 1, App.Units.Quantity('123.0 mm')))```

Distance entre deux sommets :


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceY', Edge1, PointOfEdge1, Edge2, PointOfEdge2, App.Units.Quantity('123.0 mm')))```

Étendue verticale de la ligne (l\'interface graphique permet de sélectionner l\'arête elle-même, mais ce n\'est qu\'un raccourci pour utiliser les deux extrémités de la même ligne):


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceY', Line, 1, Line, 2, App.Units.Quantity('123.0 mm')))```

La page [Sketcher Scripts](Sketcher_scripting/fr.md) explique les valeurs qui peuvent être utilisées pour `Edge1`, `Edge2`, `Edge`, ` PointOfEdge1`, ` PointOfEdge2`, `PointOfEdge` et `Line` et contient d\'autres exemples sur la façon de créer des contraintes à partir de scripts Python.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDistanceY/fr
