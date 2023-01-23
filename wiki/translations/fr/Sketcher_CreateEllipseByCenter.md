---
- GuiCommand:/fr
   Name:Sketcher CreateEllipseByCenter
   Name/fr:Sketcher Ellipse par son centre
   MenuLocation:Esquisse → Géométries d'esquisse → Créer une ellipse par son centre
   Workbenches:[Sketcher](Sketcher_Workbench/fr.md)
   Shortcut:**G** **E** **E**
   Version:0.15
   SeeAlso:[Sketcher Ellipse par 3 points](Sketcher_CreateEllipseBy3Points/fr.md), [Sketcher Cercle](Sketcher_CreateCircle/fr.md), [Sketcher Arc d'ellipse](Sketcher_CreateArcOfEllipse/fr.md)
---

# Sketcher CreateEllipseByCenter/fr



## Description

Cet outil dessine une ellipse en choisissant trois points: le centre, la fin du rayon majeur, le rayon mineur. Lors du démarrage de l\'outil, le pointeur de la souris passe à une croix blanche avec une icône d\'ellipse rouge. En outre, les coordonnées sont affichées en temps réel.

<img alt="" src=images/Sketcher_EllipseExample1.png‎  style="width:500px;"> 
*La séquence de clics est indiquée par des flèches jaunes avec des nombres.<br>
C est le centre, a - diamètre principal, b - diamètre mineur, F1, F2 sont les foyers.*



## Utilisation

-   Cliquer sur le bouton de la barre d\'outils, en choisissant l\'élément de menu, ou en utilisant le raccourci clavier (il faut d\'abord attribuer la touche dans [Personnalisation de l\'interface](Interface_Customization/fr.md)).
-   Le premier clic dans la vue 3D, définit le centre de l\'ellipse. Le deuxième clic définit le premier rayon et l\'orientation de l\'ellipse. Le troisième clic définit l\'autre rayon (la distance de la ligne définie par les deux premiers clics est le deuxième rayon).
-   Après le troisième clic, l\'ellipse est créée, ainsi que l\' ensemble de géométrie de construction (en traits bleu) aligné (diamètre principal, diamètre mineur, deux foyers). La géométrie de la construction peut être supprimée manuellement si elle n\'est pas nécessaire et recréée ultérieurement. Voir [contrainte d\'alignement interne](Sketcher_ConstrainInternalAlignment/fr.md) et [Afficher/masquer la géométrie interne](Sketcher_RestoreInternalAlignmentGeometry/fr.md).
-   En appuyant sur **Echap** ou en cliquant sur le bouton droit de la souris, vous annulez la fonction.



## Particularités

-   Les axes majeurs et mineurs des ellipses sont stricts et ne peuvent pas être échangés en redimensionnant l\'ellipse. Ceci est une conséquence du paramétrage du solveur utilisé (centre (x, y), focus1 (x, y) et longueur de rayon mineur (b)) et le même comportement strict d\'OpenCascade. L\'ellipse doit être tournée pour échanger les axes.
-   L\'ellipse peut fonctionner comme un cercle lorsque ses lignes de diamètre majeur et mineur sont supprimées, et l\'un des foyers est contraint de coïncider avec le centre. Mais la contrainte de rayon ne fonctionnera pas sur un tel cercle.
-   Déplacer l\'ellipse par un bord donne le même résultat que le centre de l\'ellipse.





{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateEllipseByCenter/fr
