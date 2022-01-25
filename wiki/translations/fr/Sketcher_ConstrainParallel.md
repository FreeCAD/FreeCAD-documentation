---
- GuiCommand:/fr
   Name:Sketcher ConstrainParallel
   Name/fr:Sketcher Contrainte parallèle
   MenuLocation:Sketch → Contraintes d'esquisse → Contrainte parallèle
   Workbenches:[Sketcher](Sketcher_Workbench/fr.md)
   Shortcut:**Maj** + **P**
   SeeAlso:[Sketcher Contrainte verticale](Sketcher_ConstrainVertical/fr.md), [Sketcher Contrainte horizontale](Sketcher_ConstrainHorizontal/fr.md)
---

# Sketcher ConstrainParallel/fr

## Description

La **Contrainte parallèle** force deux éléments sélectionnés, lignes droites ou arêtes à devenir parallèles.

## Opérations

L\'esquisse contient deux lignes, orientées de façon aléatoire.

<img alt="" src=images/ConstrainParallel1.png  style="width:500px;">



*Sélectionnez les deux lignes en cliquant successivement sur chacune d'elle.*

<img alt="" src=images/ConstrainParallel2.png  style="width:500px;">

Appliquez la contrainte parallèle par :

-   Appuyez sur le bouton **[<img src=images/Sketcher_ConstrainParallel.svg style="width:16px"> [Contrainte parallèle](Sketcher_ConstrainParallel/fr.md)** dans la barre d\'outils des contraintes de Sketcher en sélectionnant l\'élément de menu Constraint Parallel dans le sous-menu des contraintes de Sketcher du Sketcher (Atelier d\'esquisse sélectionné) ou élément de menu Part Design (Atelier de Part Design sélectionné).
-   Utilisez le raccourci clavier **Shift** + **P**.
-   Utilisez l\'entrée **Sketch → Contraintes d'esquisse → Contrainte parallèle** dans le menu supérieur.

<img alt="" src=images/ConstrainParallel3.png  style="width:500px;">



*Résultat : les lignes sélectionnées sont forcées d'être parallèles les unes aux autres. Changer l'orientation d'une ligne changera l'orientation de l'autre pour qu'elle soit la même.*

## Script


```pythonSketch.addConstraint(Sketcher.Constraint('Parallel', Line1, Line2))```

La page [Sketcher : Écrire des scripts](Sketcher_scripting/fr.md) explique les valeurs qui peuvent être utilisées pour `Line1` et `Line2` et contient d\'autres exemples sur la façon de créer des contraintes à partir de scripts Python.





{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainParallel/fr
