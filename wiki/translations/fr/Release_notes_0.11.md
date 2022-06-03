# Release notes 0.11/fr
# Notes de version 0.11 

Ceci est un sommaire des plus importants changements et nouvelles fonctionnalités disponibles dans la version 0.11 de FreeCAD. La liste complète est disponible [ici](http   *//www.freecadweb.org/tracker/changelog_page.php).

<img alt="" src=images/FreeCAD011.png  style="width   *800px;">

Une capture d\'écran de la version 0.11

\_\_TOC\_\_

### Général

-   Le [Projet de traduction FreeCAD](http   *//crowdin.net/project/freecad) a reçu une aide précieuse de beaucoup de volontaires de par le monde et FreeCAD est désormais livré en pas moins de 15 langues    * anglais, allemand, français, italien, suédois, espagnol, portugais, russe, ukrainien, norvégien, afrikaans, finnois, chinois simplifié, croate et néerlandais. Plusieurs autres langues sont en cours d\'élaboration pour les prochaines versions.

![](images/release011-translation.jpg )

-   Plusieurs améliorations ont été apportées à FreeCAD, par exemple l\'arbre hiérarchique permet désormais des groupements en piles complexes d\'objets, afin de rendre l\'historique de géométries facilement accessible et modifiable. Des améliorations à l\'API Python permettent aussi aux objets de mieux interagir avec l\'arbre, définir leur comportement, leurs icônes, etc.

![](images/release011-dependency.jpg )

-   Le copier/coller a été amélioré, afin de copier aisément des objets entre des documents.
-   L\'[atelier Pièce](Part_Workbench/fr.md) comporte de nouveau outils tels que la mise en miroir et les congés et chanfreins d\'arêtes.

### Esquisse et conception de pièces 

-   Le solveur de contraintes de l\'[atelier Sketcher](Sketcher_Workbench/fr.md) a été totalement récrit et même s\'il est toujours incomplet, l\'Esquisseur dispose d\'un bon éventail d\'outils tels que des lignes, rectangles et cercles, et des contraintes telles que coïncidence de points, parallélisme, longueur fixe ou contraintes horizontales et verticales.

-   En plus de l\'Esquisseur, un nouvel atelier Conception de pièces permet maintenant de construire rapidement des solides à partir d\'esquisses. Dorénavant dans FreeCAD, tout est paramétrique, en tout temps vous pouvez retourner en arrière et changer votre esquisse, et toute géométrie basée sur l\'esquisse s\'adaptera automatiquement.

![](images/release011-sketcher.jpg )

![](images/Movie.png ) Exemples   * [Démo de l\'Esquisseur](http   *//www.youtube.com/watch?v=hvXupH5bA0E) • [Démo de Conception de pièces](http   *//www.youtube.com/watch?v=7ih9Jp3OAwA)

### Simulation de robot 

-   L\'[atelier Robot](Robot_Workbench/fr.md) dispose de plus d\'outils en interface graphique et est maintenant assez fonctionnel pour vous permettre de simuler des mouvements de robots industriels.

![](images/release011-robot.jpg )

### Planche à dessin 

-   L\'accrochage a été grandement optimisé et fonctionne maintenant très rapidement, même sur des objets complexes.
-   L\'outil \"Trimex\" permet maintenant d\'extruder des faces simples, offrant ainsi un raccourci pratique à l\'outil Extrusion de l\'atelier Pièce.
-   La méthodologie de la planche à dessin vers la mise en plan a aussi été optimisée    * tous les objets créés avec l\'atelier Planche à dessin peuvent être maintenant placées dans une mise en plan, et ils offrent tous les mêmes possibilités de modification que les objets pièces standards, offrant la possibilité de changer leur position sur la feuille, les faire pivoter et redimensionner à la volée. Ils offrent aussi quelques fonctionnalités supplémentaires, comme le remplissage par hachures.

![](images/release011-draft-drawing.jpg )

-   La Planche à dessin offre aussi de nouveaux outils tel que les polygones réguliers et les BSplines
-   Un nouvel outil d\'édition permet de modifier la géométrie de la plupart des objets de la planche à dessin.

![](images/release011-draft.jpg )

-   Le texte des cotes peut maintenant être édité ou déplacé, et les fils (wires) peuvent se terminer avec une flèche, ce qui permet de les utiliser pour les annotations
-   Plusieurs commandes telles que déplacer, pivoter ou coter permettent de créer des copies multiples sans quitter l\'outil
-   L\'atelier Planche à dessin s\'est aussi dotée d\'une [API](Draft_API/fr.md) Python.
-   L\'importation DXF supporte maintenant les attributs de blocs

![](images/Movie.png ) Exemples    * [Démo de la Planche à dessin](http   *//www.youtube.com/watch?v=Q7cG-LQK8Ps)

### Images

-   L\'atelier image dispose maintenant d\'un objet plan image (ImagePlane) afin d\'afficher une image dans la scène 3D, ce qui peut être utile pour construire des géométries à partir de plans numérisés

### Documentation

-   Plusieurs traductions du [manuel FreeCAD](Online_Help_Toc/fr.md) sont maintenant très avancées. Consultez la page principale !


{{languages/fr | {{en|Release_notes_0.11}} {{de|Release_notes_0.11/de}} {{es|Release_notes_0.11/es}} {{it|Release_notes_0.11/it}} {{pl|Release_notes_0.11/pl}} {{ru|Release_notes_0.11/ru}} }}

[Category   *News](Category_News.md) [Category   *Documentation](Category_Documentation.md) [Category   *Releases](Category_Releases.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 0.11/fr
