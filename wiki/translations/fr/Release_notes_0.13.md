# Release notes 0.13/fr
Ceci est un résumé des changements les plus intéressants survenus dans FreeCAD depuis la dernière version. Voyez [ici (en anglais)](http://www.freecadweb.org/tracker/changelog_page.php) la liste complète des changements.

Les versions plus anciennes : [0.12](Release_notes_0.12/fr.md) - [0.11](Release_notes_0.11/fr.md)

![800px](images/FreeCAD013.jpg)

*modélisé dans FreeCAD par psicofil*

## Generalités

-   **Préférences de couleur** : Vous en avez assez du bon vieux « formes grisées avec arêtes noires », l\'aspect par défaut dans FreeCAD ? Ces couleurs ainsi que d\'autres couleurs par défaut sont maintenant modifiables dans les préférences de l\'utilisateur (**Affichage → Couleur**).
-   **Alignement** : deux formes peuvent être alignées l\'une contre l\'autre en saisissant jusqu\'à 3 points avec cet outil disponible dans le menu Édition.
-   FreeCAD est maintenant disponible en 22 langues en plus de l\'anglais.

## Module de mise en plan (Drawing) 

-   **Masque** : Un nouvel objet [Masque](Drawing_Clip/fr.md) permet de placer des objets à l\'intérieur de vues rectangulaires coupées, sur les pages de dessin.
-   **Texte de cartouche éditable** : Lors de la conception d\'un [modèles de feuille](Drawing_templates/fr.md), il est maintenant possible d\'ajouter des textes éditables. Ces textes sont alors directement modifiables dans FreeCAD.
-   **Annotation** : Un nouvel objet [annotation](Drawing_Annotation/fr.md) pour placer facilement et rapidement des blocs de textes sur une page de dessin.
-   **Vues orthogonales** : Un nouvel outil de [vues orthogonales](Drawing_Orthoviews/fr.md) facilite la création de vues multiples alignées, selon la projection européenne ou américaine.
-   **Vue web** : Parce que le moteur de rendu SVG utilisé par le module de mise en plan ne supporte pas toutes les fonctionnalités SVG, ce bouton permet de visionner l\'aspect d\'une page de dessin dans le navigateur WebKit, qui supporte pleinement le format SVG. Cette mesure est provisoire, jusqu\'à ce que le moteur de rendu de mise en plan passe définitivement à QebKit\...
-   **Exportation DXF** : il est maintenant possible d\'exporter une vue d\'une page directement au format DXF.
-   Des correctifs de bogues permettent maintenant l\'impression des pages à l\'échelle.

## Module esquisse (Sketcher) 

-   **Création de point**

![](images/Release-0.13-PointTool.png )

Les points peuvent maintenant être ajoutés et utilisés comme un élément à part entière dans l\'esquisse.

-   **Origine d\'esquisse**

![](images/Release-0.13-Origin.png )

L\'utilisateur peut maintenant utiliser l\'origine de l\'esquisse pour définir la géométrie, ainsi que les axes du dessin.

-   **Contraintes de tangence, et, de perpendicularité des arcs et des cercles.**
-   **Contraintes par rapport à des géométrie externes (projetées).**
-   **Amélioration de la comptabilisation des degrés de liberté de l\'esquisse.**
-   **Contrainte de symétrie par rapport à un point de symétrie (contrainte du point médian)**.

-   **Amélioration de l\'aspect visuel des contraintes et des étiquettes de données :**

![](images/Release-0.13-SketcherDimensions.png )

-   -   Chaque étiquette de contrainte (y compris les flèches) est mise à l\'échelle automatiquement par rapport à la scène graphique 3D.
    -   Le texte des contraintes dimensionnelles Distance X, distance Y et rayon peut être positionné librement.
    -   De petites améliorations sur le chevauchement des icônes de contraintes et correctifs de gels de l\'interface.
    -   Le texte des étiquettes s\'inverse lorsque la vue est orientée du côté opposé.

-   **Les croquis entièrements contraints sont désormais mis en surbrillance :**

![La couleur de l\'esquisse passe du blanc au vert pour indiquer qu\'elle est parfaitement contrainte. Ces couleurs par défaut peuvent être personnalisées.](images/Release-0.13-SketcherFullyConstrained.png )

-   **Sélection rectangulaire englobante**.

![](images/Release-0.13-RubberBandSelection.png )

Les géométrie (points, lignes et courbes) peuvent être sélectionnés en faisant glisser la souris dans la fenêtre modèle, pour créer une sélection rectangulaire englobante.

-   **Fonctionnalités étendues de l\'outil Polyligne :** à l\'aide de la touche **m** on peut basculer entre les modes arc, ligne et parmi les transitions libres, tangentes, et perpendiculaires au segment précédent.

-   **Appliquer une esquisse sur une face** est un nouvel outil qui permet d\'associer une esquisse existante à la face sélectionnée d\'un solide. Ceci permet l\'utilisation de l\'esquisse pour des fonctions telles que Protrusion ou Cavité ([exemple sur le forum](http://forum.freecadweb.org/viewtopic.php?f=3&t=3907&p=30704#p30704)).

-   **Petites améliorations:**
    -   Lors de la construction d\'une géométrie, une info-bulle s\'affiche à côté du curseur, donnant des informations sur la commande.
    -   L\'outil **Vue normale au plan d\'esquisse** fait maintenant partie de la barre d\'outil du module Sketcher pour un accès rapide.

## Planche à dessin (module Draft) 

-   **Mode Tâches** : le mode Tâches du module **Draft** est maintenant activé par défaut. N\'ayez pas peur, si vous aimiez la barre d\'outils, elle est toujours disponible dans les préférences paramètres Draft.
-   **Importation DXF** : Désormais l\'importation de fichiers **.DXF** prend en charge les points (comprendre [Draft Point](Draft_Point/fr.md)) et les fils (comprendre ([Draft Wire](Draft_Wire/fr.md))).
-   **Tout nouveau système d\'accrochage (snapping)** : Le système d\'[accrochage (Snap)](Draft_Snap/fr.md) du module Draft a été totalement réécrit. Il est maintenant beaucoup plus facile à étendre et plus facile à utiliser dans d\'autres scripts et modules, il a maintenant de nouveaux icônes, de nouveaux curseurs, et il dispose de sa propre barre d\'outils qui permet d\'activer/désactiver individuellement les types d\'accrochage par un simple clic de souris ou le système entier.

![800px](images/013-draft-snap.jpg)

-   **Mode de contrainte amélioré** : lors de la saisie de points 3D, en plus de la fonction existante **Shift** pour contraindre, vous pouvez maintenant limiter le déplacement en X, Y ou Z en appuyant sur ​​les touches **X**, **Y** ou **Z**. Une deuxième pression désactive le mode de contrainte.
-   **Conversion Draft \<-\> Sketch** : La planche à dessin (atelier Draft) dispose désormais d\'un nouvel outil de conversion, **[Draft vers Esquisse](Draft_Draft2Sketch/fr.md)**, qui permet de convertir les objets **Draft** sélectionnés (ou toute autre forme plane) en esquisse (**Sketch**), et vice-versa.
-   **Outil Clone** : cet outil pratique permet de faire une ou plusieurs copie(s) du ou des objet(s) sélectionné(s). Lorsque l\'original est modifié, le clone est mis à jour automatiquement. Le clone peut être déplacé, pivoté, et a également une propriété d\'échelle qui permet de changer la taille de la copie.
-   **Importateur SVG** : désormais, l\'importateur SVG supporte beaucoup mieux les courbes de Bézier.
-   **Coins arrondis** : plusieurs objets Draft ([Fils (Wires)](Draft_Wire/fr.md), [Rectangles](Draft_Rectangle/fr.md) et [Polygones](Draft_Polygon/fr.md)) ont maintenant une propriété **Rayon de congé (Fillet Radius)**, qui arrondit leurs coins avec la valeur donnée au rayon.

![800px](images/013-draft-fillet.jpg)

-   **Projection 2D** : Le nouvel outil [Shape2DView](Draft_Shape2DView/fr.md), permet de placer rapidement une vue 2D d\'un objet sélectionné dans le document. Vous pouvez spécifier le vecteur de projection.

![800px](images/013-draft-shape2dview.jpg)

## Module architectural (Arch) 

-   **Intégration du module Draft** : Les modules **Arch** et **Draft** sont désormais étroitement liés. Les outils **Arch** utilisent le [système d\'accochage Draft](Draft_Snap/fr.md), et tous les outils Draft sont présents dans l\'atelier **Arch**. Par ailleurs, si vous le souhaitez, vous pouvez aussi désactiver complètement le module Draft (Préférences → Draft → Masquer l\'établi Draft).
-   **Nouvel outil Mur**\' : L\'outil [Mur](Arch_Wall/fr.md) a été grandement amélioré, et dispose désormais d\'un mode de dessin direct, qui est activé lorsque vous appuyez sur le bouton **Mur** sans objet sélectionné, ce qui vous permet de dessiner des murs comme de simples lignes. Quand vous ajoutez un mur à un mur existant, la connexion se fait automatiquement.

![800px](images/013-arch-wall.jpg)

-   **Nouvel outil toiture** : Un nouvel outil [Toiture](Arch_Roof/fr.md) est maintenant disponible dans le module **Arch**, et permet de créer rapidement une toiture en pente à partir d\'une face sélectionnée.
-   **Nouvel outil fenêtre** : Les [fenêtres](Arch_Window/fr.md) sont désormais créées à partir de formes planes qui contiennent au moins un filaire, tel qu\'un rectangle Draft ou une esquisse. Si cet objet a été dessiné directement sur la face d\'un mur, la fenêtre découpera automatiquement une ouverture dans le mur.
-   **Nouveau système de sections** : Il est désormais très simple de créer des plans 2D, coupes et élévations de votre modèle : placez un objet [plan de coupe](Arch_SectionPlane/fr.md), orientez-le comme vous le souhaitez, modifier-le pour y inclure les objets à afficher, et vous avez terminé !
-   **Nouveau moteur de rendu solide** : En plus du moteur de rendu 2D filaire OpenCasCADe actuellement utilisé par le module de [mise en plan](Drawing_Workbench/fr.md), le module **Arch** dispose désormais d\'un nouveau moteur de rendu 2D qui est capable d\'afficher les faces pleines sur une feuille de dessin .SVG, ce qui donne des vues 2D beaucoup plus agréables.

![800px](images/013-arch-vrm.jpg)

-   **Importation IFC [IfcOpenShell](http://www.ifcopenshell.org)** : le module **Arch** peut maintenant utiliser [IfcOpenShell](http://www.ifcopenshell.org) s\'il est installé sur votre système. Cela améliore l\'importation du format [IFC](http://fr.wikipedia.org/wiki/Industry_Foundation_Classes), et l\'importation du contenu total du fichier IFC est garantie.
-   **De nouveaux objets étage et bâtiment** : Les bâtiments et les étages sont maintenant des groupes, de sorte que vous pouvez, à partir de l\'arborescence, leur ajouter ou supprimer des objets avec un simple glisser-déposer.
-   **Nouveau système d\'axes** : Une nouvelle fonctionnalité [système d\'axes](Arch_Axis/fr.md) a été ajoutée, ce qui permet de disposer rapidement des systèmes complexes d\'axes. Ces axes peuvent alors être ajoutés à des objets [Structure](Arch_Structure/fr.md), de sorte qu\'ils se propagent automatiquement sur ​​les nœuds de la grille.

![800px](images/013-arch-axes.jpg)

-   **Objets Arch à partir de maillages** : Des [murs](Arch_Wall/fr.md) et [structures](Arch_Structure/fr.md) peuvent désormais être générés directement à partir de maillages, à condition qu\'ils soit fermés, solides et que toutes les arêtes soient [manifold](http://doc.spatial.com/index.php/Manifold_and_Non-manifold_Objects). Cela permet la transformation très rapide des géométries importées d\'autres applications telles que [Blender](http://www.blender.org) en objets Arch valides.

## Module Pièce (Part) 

-   **Affiner la forme** est un nouvel outil qui nettoie les faces d\'une forme après des opérations booléennes multiples. Il peut être configuré pour s\'exécuter automatiquement après des opérations booléennes via les préférences.
-   L**\'outil de lissage** permet d\'extruder un ensemble de surfaces complexes ou un solide à travers une série d\'esquisses ou d\'objets Draft.
-   L**\'outil de balayage** permet d\'extruder un ensemble de surfaces complexes ou un solide à travers une série d\'esquisses ou d\'objets Draft et une trajectoire (esquisse, arête ou objet Draft).
-   L**\'outil Décalage** permet de décaler une surface ou une forme.
-   L**\'outil Évidement** permet d\'évider un solide en définissant une épaisseur de paroi et une ou plusieurs faces à défoncer.
-   Le **Générateur de formes** et **Créer des primitives** font maintenant partie de la barre d\'outil Pièce pour un accès rapide.

## Module Part Design 

-   Les fonctions **Protrusion** et **Cavité** bénéficient de nouveaux paramètres d\'extrusion : au dernier/au premier, jusqu\'à la face, 2 dimensions assymétriques par rapport au plan d\'esquisse, et symétrique au plan.
-   Les fonctions **Chanfrein** et **Congé** permettent maintenant la sélection d\'une face : toutes les arêtes extérieures et intérieures seront traitées.
-   **Révolution** : une ligne de construction dans l\'esquisse peut être utilisée comme axe de révolution.
-   La nouvelle fonction **Enlèvement de matière par révolution** permet de couper de la matière du solide en appliquant une révolution sur une esquisse.
-   Les nouvelles fonctions de transformation **Répétition linéaire**, **Répétition circulaire**, **Symétrie** et **Transformation multiple** permettent d\'aligner et de distribuer des protrusions ou des cavités sur un solide.
-   Un **assistant de conception d\'arbres (Shaft design wizard)** vous aide à concevoir des arbres.

## Module navire (Ship module) 

-   [Nouveau Module navire](FreeCAD-Ship_s60_tutorial/fr.md) (tutoriel)

## Souris 3D 

-   Le support pour souris 3D (Spaceball, Space Navigator) a été ajouté à la version de Windows.
-   Un nouvel onglet **Spaceball Motion** a été ajouté dans la boîte de dialogue **Personnaliser** pour affiner les paramètres de votre souris 3D comme vous le voulez, directement à partir de FreeCAD.

!!FUZZY!!== OpenSCAD module ==

-   Ce tout nouveau module (expérimental) soutient les fonctions d\'importation des fichiers **OpenSCAD** dans FreeCAD. Ce format est très populaire dans la communauté **[RepRap](http://fr.wikipedia.org/wiki/RepRap)** et sur le site de partage de modèles 3D [Thingiverse](http://www.thingiverse.com/).
-   Le script OpenSCAD peut être exécuté depuis FreeCAD, par OpenSCAD (s\'il est installé sur votre ordinateur), le résultat apparait dans votre document FreeCAD.
-   Pour plus d\'informations, consultez la page du wiki FreeCAD [Module OpenSCAD](OpenSCAD_Workbench/fr.md)



---
⏵ [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 0.13/fr
