---
- GuiCommand:/fr
   Name:Sketcher RestoreInternalAlignmentGeometry
   Name/fr:Sketcher Géométrie interne
   MenuLocation:Esquisse → Outils d'esquisse → Afficher/masquer la géométrie interne
   Workbenches:[Sketcher](Sketcher_Workbench/fr.md)
   Shortcut:**Z** **I**
   SeeAlso:
---

# Sketcher RestoreInternalAlignmentGeometry/fr

## Description

La commande supprime les éléments inutilisés alignés sur la géométrie interne ou recrée les éléments manquants.



## Utilisation

-   Sélectionnez un élément d\'une esquisse qui prend en charge l\'alignement interne ([Ellipse](Sketcher_CreateEllipseByCenter/fr.md), [Arc d\'ellipse](Sketcher_CreateArcOfEllipse/fr.md), [Arc d\'hyperbole](Sketcher_CreateArcOfHyperbola/fr.md), [Arc de parabole](Sketcher_CreateArcOfParabola/fr.md) ou [B-spline](Sketcher_CreateBSpline/fr.md)).
-   Lancez la commande en cliquant sur un bouton de la barre d'outils **[<img src=images/Sketcher_RestoreInternalAlignmentGeometry.svg style="width:16px"> [Afficher/masquer la géométrie interne](Sketcher_RestoreInternalAlignmentGeometry/fr.md)** ou choisissez **Esquisse → Outils d'esquisse → [<img src=images/Sketcher_RestoreInternalAlignmentGeometry.svg style="width:16px"> Afficher/masquer la géométrie interne** ou utilisez le raccourci clavier.

S\'il existe des emplacements d\'alignement libres pour l\'élément sélectionné, une nouvelle géométrie de construction est créée et alignée sur les emplacements disponibles. Si tous les emplacements d\'alignement sont occupés, la géométrie interne non utilisée est supprimée (l\'élément est considéré comme inutilisé s\'il n\'est contraint à rien d\'autre).



## Exemple

1.  Créez une nouvelle ellipse. Les nouvelles ellipses sont toujours entièrement emballées. Vous verrez une ellipse et un tas de géométries de construction: diamètre majeur, diamètre mineur, foyers.
2.  Sélectionnez une ligne de petit diamètre et appuyez sur **Suppr**. Le diamètre a disparu, mais l\'ellipse reste. Comment récupérer le diamètre?
3.  Sélectionnez l\'ellipse et appelez la commande **[<img src=images/Sketcher_RestoreInternalAlignmentGeometry.svg style="width:16px"> [Afficher/masquer la géométrie interne](Sketcher_RestoreInternalAlignmentGeometry/fr.md)**. Le diamètre est restauré.
4.  Maintenant, contraignez le diamètre principal de l\'ellipse à une certaine longueur. Sélectionnez l\'ellipse et appelez la commande **[<img src=images/Sketcher_RestoreInternalAlignmentGeometry.svg style="width:16px"> [Afficher/masquer la géométrie interne](Sketcher_RestoreInternalAlignmentGeometry/fr.md)**.

**Résultat :** le petit diamètre et les foyers sont supprimés, mais le grand diamètre est conservé car il participe à d\'autres contraintes. Le centre de l\'ellipse reste également car il est inhérent comme le centre d\'un cercle.





{{Sketcher_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher RestoreInternalAlignmentGeometry/fr
