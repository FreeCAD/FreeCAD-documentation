---
 GuiCommand:
   Name: Sketcher ConstrainVertical
   Name/fr: Sketcher Contrainte verticale
   MenuLocation: Esquisse , Contraintes d'esquisse , Contrainte verticale
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **V**
   SeeAlso: Sketcher_ConstrainHorizontal/fr
---

# Sketcher ConstrainVertical/fr

## Description

Permet de créér une contrainte de verticalité sur les lignes ou segments de polylignes sélectionnés. Depuis {{VersionPlus/fr|0.17}}, on peut aussi contraindre des sommets verticalement. Plus d\'un élément peut être sélectionné.



## Utilisation

1.  Sélectionnez les lignes ou les sommets à contraindre verticalement
2.  Pour lancer la commande de contrainte verticale :
    -   Appuyez sur l\'icône **[<img src=images/Sketcher_ConstrainVertical.svg style="width:16px"> [Contrainte verticale](Sketcher_ConstrainVertical/fr.md)**.
    -   Utilisez le raccourci clavier **V**.
    -   Utilisez l\'entrée **Esquisse → Contraintes d'esquisse → [<img src=images/Sketcher_ConstrainVertical.svg style="width:16px"> Contrainte verticale**.
3.  Sinon, l\'outil peut être lancé sans sélection préalable, et il attendra une sélection.
4.  Clic droit ou appuyez une fois sur **Echap** pour quitter l\'outil.



## Script


```pythonSketch.addConstraint(Sketcher.Constraint('Vertical', Line))```

La page [Sketcher Scripts](Sketcher_scripting/fr.md) explique les valeurs qui peuvent être utilisées pour `Line` et contient d\'autres exemples sur la façon de créer des contraintes à partir de scripts Python.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainVertical/fr
