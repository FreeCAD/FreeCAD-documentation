---
- GuiCommand:
   Name: Sketcher ConstrainEqual
   Name/fr: Sketcher Contrainte d'égalité
   MenuLocation: Esquisse - Contraintes d'esquisse - Contrainte d'égalité
   Workbenches: [Sketcher](Sketcher_Workbench/fr.md)
   Shortcut: **E**
   SeeAlso: [Sketcher Contrainte rayon](Sketcher_ConstrainRadius/fr.md)
---

# Sketcher ConstrainEqual/fr

## Description

La Contrainte d\'égalité contraint deux ou plusieurs segments de ligne, polyligne ou de rectangle d\'avoir une longueur égale. Si elle est appliquée à des arcs de cercles ou des cercles, leurs rayons sont contraints à devenir égaux. La contrainte ne peut pas être appliquée à des primitives géométriques qui ne sont pas du même type (par exemple des segments de ligne et des arcs).



## Opérations

L\'exemple d\'esquisse ci-dessous contient un certain nombre de primitives (ligne, polyligne, rectangle, arc et cercle).

![](images/EqualConstraint1.png )

Sélectionnez deux ou plusieurs segments de ligne (par exemple la ligne et un côté du rectangle).

![](images/EqualConstraint2.png )

Cliquez sur **[<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Contrainte d'égalité ](Sketcher_ConstrainEqual/fr.md)** dans la barre d\'outils Sketcher (soit l\'atelier Sketcher soit l\'atelier Part Design) ou sélectionnez l\'élément de menu Contrainte d\'égalité dans le sous-menu Contraintes d\'esquisse du menu Sketch ou Part Design selon l\'atelier sélectionné (Sketcher ou Part Design) pour appliquer la contrainte aux éléments sélectionnés.

![](images/EqualConstraint3.png )

Maintenant, sélectionnez l\'arc et le cercle dans l\'esquisse.

![](images/EqualConstraint4.png )

et appliquez **[<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Contrainte d'égalité](Sketcher_ConstrainEqual/fr.md)** comme auparavant.

![](images/EqualConstraint5.png )

Maintenant, sélectionnez le segment de ligne, tous les segments de la polyligne et un des côtés du rectangle qui n\'est pas contraint,

![](images/EqualConstraint6.png )

et appliquez **[<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Contrainte d'égalité](Sketcher_ConstrainEqual/fr.md)** comme auparavant.

![](images/EqualConstraint7.png )

Sélectionnez le segment de ligne et l\'arc,

![](images/EqualConstraint8.png )

et appliquez à nouveau **[<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Contrainte d'égalité](Sketcher_ConstrainEqual/fr.md)**. Un message indique que les éléments contraints doivent être du même type géométrique (lignes de courbure nulle ou lignes de courbure non nulle).

![](images/EqualConstraint9.png )



## Script


```pythonSketch.addConstraint(Sketcher.Constraint('Equal', Edge1, Edge2))```

La page [Sketcher Scripts](Sketcher_scripting/fr.md) explique les valeurs qui peuvent être utilisées pour `Edge1` et `Edge2` et contient d\'autres exemples sur la façon de créer des contraintes à partir de scripts Python.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainEqual/fr
