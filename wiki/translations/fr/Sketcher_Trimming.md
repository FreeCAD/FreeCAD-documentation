---
- GuiCommand:/fr
   Name:Sketcher Trimming
   Name/fr:Sketcher Ajuster une arête
   MenuLocation:Sketch → Géométries d'esquisse → Ajuster l'arête
   Workbenches:[Sketcher](Sketcher_Workbench/fr.md)
   Version:0.12
   SeeAlso:[Sketcher Prolonger l'arête](Sketcher_Extend/fr.md)
---

## Description

Cet outil ajuste la ligne jusqu\'à la première intersection rencontrée, à l\'intérieur ou à l\'extérieur d\'une forme.

![](images/SketcherTrimExample1.png ) ![](images/SketcherTrimExample2.png ) ![](images/SketcherTrimExample3.png )

## Utilisation

1.  Appuyer sur le bouton **<img src=images/Sketcher_Trimming.svg style="width:16px"> [Ajuster une arête par rapport...](Sketcher_Trimming/fr.md)**. Le pointeur de la souris se transforme en une croix blanche avec un symbole d\'ajustement rouge.
2.  Cliquer sur l\'arête que vous voulez ajuster.
3.  Le segment de ligne sera coupé à la ou aux lignes se chevauchant les plus proches. S\'il y a d\'autres éléments d\'esquisse des deux côtés de la position cliquée,le morceau cliqué est découpé.
4.  Appuyer sur **Échap** ou sur le bouton droit de la souris pour mettre fin à la fonction.

## Limitations

-    {{VersionMinus/fr|0.18}}Les arcs d\'hyperbole et de parabole ainsi que les courbes B-splines ne peuvent pas être ajustée.





{{Sketcher Tools navi

}}  
