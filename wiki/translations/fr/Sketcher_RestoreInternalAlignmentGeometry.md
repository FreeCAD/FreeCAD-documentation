---
 GuiCommand:
   Name: Sketcher RestoreInternalAlignmentGeometry
   Name/fr: Sketcher Géométrie interne d'alignement
   MenuLocation: Esquisse , Affichage , Afficher/masquer la géométrie interne
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **Z** **I**
   SeeAlso: 
---

# Sketcher RestoreInternalAlignmentGeometry/fr

## Description

L\'outil <img alt="" src=images/Sketcher_RestoreInternalAlignmentGeometry.svg  style="width:24px;"> [Sketcher Géométrie interne d\'alignement](Sketcher_RestoreInternalAlignmentGeometry/fr.md) supprime la géométrie interne des éléments ou recrée la géométrie interne manquante. L\'outil ne supprime pas les géométries internes associées à des contraintes.



## Utilisation

1.  Sélectionnez un ou plusieurs éléments d\'esquisse qui prennent en charge la géométrie interne ([ellipse](Sketcher_CreateEllipseByCenter/fr.md), [arc d\'ellipse](Sketcher_CreateArcOfEllipse/fr.md), [arc d\'hyperbole](Sketcher_CreateArcOfHyperbola/fr.md), [arc de parabole](Sketcher_CreateArcOfParabola/fr.md) ou [B-spline](Sketcher_CreateBSpline/fr.md)).
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Sketcher_RestoreInternalAlignmentGeometry.svg" width=16px> [Afficher/masquer la géométrie interne](Sketcher_RestoreInternalAlignmentGeometry/fr.md)**.
    -   Sélectionnez l\'option **Esquisse → Affichage → <img src="images/Sketcher_RestoreInternalAlignmentGeometry.svg" width=16px> Afficher/masquer la géométrie interne** du menu.
    -   Utilisez le raccourci clavier : **Z** puis **I**.
3.  La géométrie interne est supprimée pour les éléments sélectionnés ayant un jeu complet de géométrie interne, sinon la géométrie interne manquante est recréée.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher RestoreInternalAlignmentGeometry/fr
