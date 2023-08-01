---
- GuiCommand:/fr
   Name:Sketcher ConstrainDistance
   Name/fr:Sketcher Contrainte dimensionnelle
   MenuLocation:Esquisse → Contraintes d'esquisse → Contrainte de dimension
   Workbenches:[Sketcher](Sketcher_Workbench/fr.md)
   Shortcut:**K** **D**
   SeeAlso:[Sketcher Contrainte distance en X](Sketcher_ConstrainDistanceX/fr.md), [Sketcher Contrainte distance en Y](Sketcher_ConstrainDistanceY/fr.md)
---

# Sketcher ConstrainDistance/fr

## Description

La **Contrainte dimensionnelle** définit la longueur d\'une ligne, la distance perpendiculaire entre un point et une ligne, la distance entre deux points ou ; {{Version/fr|0.21}}, la distance entre les bords de deux cercles ou entre le bord d\'un cercle et une ligne.

![](images/Sketcher_ConstrainDistance_example.png )



## Utilisation

1.  Choisissez une ligne, ou un point et une ligne, ou deux points, ou les bords de deux cercles, ou le bord d\'un cercle et une ligne.
2.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **[<img src=images/Sketcher_ConstrainDistance.svg style="width:16px"> [Contrainte de dimension](Sketcher_ConstrainDistance/fr.md)**
    -   Utilisez les raccourcis clavier **K** puis **D**
    -   Utilisez l\'entrée **Esquisse → Contraintes d'esquisse → [<img src=images/Sketcher_ConstrainDistance.svg style="width:16px"> Contrainte de dimension** dans le menu supérieur.
3.  Une boîte de dialogue contextuelle s\'ouvre pour modifier ou confirmer la valeur. Appuyez sur **OK** pour valider.

**Remarque :** l\'outil de contrainte peut également être démarré sans sélection préalable (en dehors du cas de cercle à cercle et de cercle à ligne). Pour définir la distance perpendiculaire entre un point et une droite, le point doit être sélectionné en premier. Par défaut, la commande sera en mode continu afin de créer de nouvelles contraintes; appuyez sur le bouton droit de la souris ou sur **Echap** pour quitter la commande.



### Suggestion

Le cas échéant envisagez d\'utiliser de préférence les fonctions de contrainte **[<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> [Sketcher Contrainte distance en X](Sketcher_ConstrainDistanceX/fr.md)** ou **[<img src=images/Sketcher_ConstrainDistanceY.svg style="width:16px"> [Sketcher Contrainte distance en Y](Sketcher_ConstrainDistanceY/fr.md)**. Ces contraintes sont plus robustes et plus rapides à calculer que la **contrainte dimensionnelle**.



## Script

Distance depuis l\'origine :


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Edge, PointOfEdge, -1, 1, App.Units.Quantity('123.0 mm')))```

Distance entre deux sommets :


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Edge1, PointOfEdge1, Edge2, PointOfEdge2, App.Units.Quantity('123.0 mm')))```

Longueur de ligne (l\'interface graphique permet de sélectionner l\'arête elle-même, mais ce n\'est qu\'un raccourci pour utiliser les deux extrémités d\'une même ligne) :


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Line, 1, Line, 2, App.Units.Quantity('123.0 mm')))```

Distance du point (`Edge, PointOfEdge`) au point perpendiculaire sur la ligne (`Line`) :


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Edge, PointOfEdge, Line, 0, App.Units.Quantity('123.0 mm')))```

Distance entre les bords de deux cercles :


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Circle1, 0, Circle2, 0, App.Units.Quantity('123.0 mm')))```

La page [Sketcher Scripts](Sketcher_scripting/fr.md) explique les valeurs qui peuvent être utilisées pour `Edge`, `Edge1`, `Edge2`, `PointOfEdge`, `PointOfEdge1`, `PointOfEdge2`, `Ligne`, `Cercle1` et `Cercle2`, et contient d\'autres exemples sur la façon de créer des contraintes à partir de scripts Python.





{{Sketcher_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDistance/fr
