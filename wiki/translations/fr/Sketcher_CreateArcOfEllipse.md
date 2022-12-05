---
- GuiCommand:/fr
   Name:Sketcher CreateArcOfEllipse
   Name/fr:Sketcher Arc d'ellipse
   MenuLocation:Sketch → Géométries d'esquisse → Créer un arc d'ellipse
   Workbenches:[Sketcher](Sketcher_Workbench/fr.md)
   Shortcut:**G** **E** **A**
   Version:0.15
   SeeAlso:[Sketcher Ellipse par son centre](Sketcher_CreateEllipseByCenter/fr.md), [Sketcher Arc](Sketcher_CompCreateArc/fr.md)
---

# Sketcher CreateArcOfEllipse/fr

## Description

Cet outil dessine une ellipse en choisissant trois points: le centre, la fin du rayon majeur, le rayon mineur. Lors du démarrage de l\'outil, le pointeur de la souris passe à une croix blanche avec une icône d\'ellipse rouge. En outre, les coordonnées sont affichées en temps réel.

<img alt="" src=images/Sketcher_ArcOfEllipseExample1.png‎  style="width:500px;"> 
*La séquence de clics est indiquée par des flèches jaunes avec des nombres. C est le centre, a - diamètre principal, b - diamètre mineur, F1, F2 sont les foyers.*

## Utilisation

-   Cliquer sur le bouton **[<img src=images/Sketcher_CreateArcOfEllipse.svg style="width:16px"> [Créer un arc d'ellipse](Sketcher_CreateArcOfEllipse/fr.md)**.
-   Le premier clic dans la vue 3D, définit le centre de l\'ellipse. Le deuxième clic définit le premier rayon et l\'orientation de l\'ellipse. Le troisième clic définit l\'autre rayon et le début de l\'arc. le quatrième clic définit le point final.
-   Après le quatrième clic, l\'arc d\'ellipse est créée, ainsi que l\' ensemble de géométrie de construction (en traits bleu) aligné (diamètre principal, diamètre mineur, deux foyers). La géométrie de la construction peut être supprimée manuellement si elle n\'est pas nécessaire et recréée ultérieurement. Consulter [contrainte d\'alignement interne](Sketcher_ConstrainInternalAlignment/fr.md) et [Afficher/masquer la géométrie interne](Sketcher_RestoreInternalAlignmentGeometry/fr.md).
-   En appuyant sur **Echap** ou en cliquant sur le bouton droit de la souris, vous annulez la fonction.

## Particularités

-   Les axes majeurs et mineurs des ellipses sont stricts et ne peuvent pas être échangés en redimensionnant l\'ellipse. Ceci est une conséquence de la paramétrage du solveur utilisé (centre (x, y), focus1 (x, y) et longueur de rayon mineur (b)) et le même comportement strict de OpenCascade. L\'ellipse doit être tournée pour échanger les axes.
-   L\'arc d\'Ellipse peut fonctionner comme un arc de cercle lorsque ses lignes de diamètre majeur et mineur sont supprimées, et l\'un des foyers est contraint de coïncider avec le centre. Mais la contrainte de rayon ne fonctionnera pas sur une telle ellipse.
-   Déplacer l\'ellipse par un bord donne le même résultat que le centre de l\'ellipse.





{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateArcOfEllipse/fr
