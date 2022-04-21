---
- GuiCommand:/fr
   Name:Sketcher ConstrainHorizontal
   Name/fr:Sketcher_Contrainte horizontale
   MenuLocation:Esquisse → Contraintes d'esquisse → Contrainte horizontale
   Workbenches:[Sketcher](Sketcher_Workbench/fr.md)
   Shortcut:**H**
   SeeAlso:[Sketcher Contrainte verticale](Sketcher_ConstrainVertical/fr.md)
---

# Sketcher ConstrainHorizontal/fr

## Description

La Contrainte horizontale oblige une ligne sélectionnée ou des lignes dans l\'esquisse à être parallèles à l\'axe horizontal de l\'esquisse.

## Utilisation

<img alt="" src=images/HorizontalConstraint1.png  style="width:500px;"> 
*Sélectionnez une ligne dans l'esquisse en cliquant dessus.*

<img alt="" src=images/HorizontalConstraint2.png  style="width:500px;"> 
*La ligne devient vert foncé.*

<img alt="" src=images/HorizontalConstraint3.png  style="width:500px;"> 
*Appliquez la contrainte horizontale en cliquant sur **[<img src=images/Sketcher_ConstrainHorizontal.svg style="width:16px"> [Contrainte horizontale](Sketcher_ConstrainHorizontal/fr.md)* dans la barre d'outils Contraintes de l'esquisse ou en sélectionnant l'élément de menu Contraindre horizontalement dans les Contraintes d'esquisse, sous-menu de l'élément du menu Esquisse dans l'atelier Sketcher (ou l'élément de menu Part Design de l'atelier Part Design). La ligne sélectionnée est contrainte d'être parallèle à l'axe horizontal de l'esquisse.**

<img alt="" src=images/HorizontalConstraint4.png  style="width:500px;"> 
*Plusieurs lignes peuvent être sélectionnées*

<img alt="" src=images/HorizontalConstraint5.png  style="width:500px;"> 
*puis en appliquant la contrainte comme décrit ci-dessus, elles sont contraintes d'être parallèles à l'axe horizontal de l'esquisse.*

## Script


```pythonSketch.addConstraint(Sketcher.Constraint('Horizontal', Line))```

La page [Sketcher Scripts](Sketcher_scripting/fr.md) explique les valeurs qui peuvent être utilisées pour `Line` et contient d\'autres exemples sur la façon de créer des contraintes à partir de scripts Python.





{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainHorizontal/fr
