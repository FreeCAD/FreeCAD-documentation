# Manual:Modeling for product design/fr
{{Manual:TOC/fr}}

[La Conception de produits](https://en.wikipedia.org/wiki/Product_design) est à l\'origine un terme commercial, mais dans le monde de la 3D, cela signifie souvent de modéliser quelque chose avec l\'idée d\'[impression 3D](https://en.wikipedia.org/wiki/3D_printing) ou, plus généralement, de le fabriquer avec une machine, imprimante 3D ou machine à commande numérique [CNC](https://en.wikipedia.org/wiki/Numerical_control).

Lorsque vous imprimez des objets en 3D, il est extrêmement important que vos objets soient des **solides**. Car ils deviendront des objets solides réels, c\'est évident. Rien ne les empêche d\'être creux à l\'intérieur, bien sûr. Mais vous devez toujours avoir une idée claire de quels points sont à l\'intérieur de la matière et quels points se trouvent à l\'extérieur, car l\'imprimante 3D ou la machine CNC doit savoir exactement ce qui est rempli de matière et ce qui ne l\'est pas. Pour cette raison, dans FreeCAD, l'atelier PartDesign ([PartDesign Workbench](PartDesign_Workbench.md)) est l\'outil idéal pour construire de telles pièces, car il veillera toujours pour vous à ce que vos objets restent des solides et réalisables.

Pour illustrer comment fonctionne l'atelier PartDesign, créons ce morceau bien connu de [Lego](https://en.wikipedia.org/wiki/Lego) :

![](images/Exercise_lego_01.jpg )

Ce qui est pratique avec les pièces de Lego est que les dimensions sont faciles à obtenir sur internet, au moins pour les pièces standard. Il est assez facile de les modéliser et de les imprimer sur une imprimante 3D, et avec un peu de patience (l\'impression 3D nécessite souvent beaucoup d\'ajustements et de réglages), vous pouvez créer des pièces totalement compatibles et qui s'encastrent parfaitement dans des blocs Lego d\'origine. Dans l'exemple ci-dessous, nous allons créer une pièce 1,5 fois plus grand que l\'original.

Nous allons maintenant utiliser exclusivement les outils des ateliers ([Sketcher](Sketcher_Workbench/fr.md)) et [PartDesign](PartDesign_Workbench/fr.md). Étant donné que tous les outils de l'atelier Sketcher sont également inclus dans l'atelier PartDesign, nous pouvons rester dans PartDesign et nous n\'aurons pas à basculer entre les deux.

Les objets Part Design sont entièrement basés sur des **esquisses**. Une esquisse est un objet 2D, composé d'éléments linéaires (lignes ou segments de droites, arcs de cercle ou ellipses) et de contraintes. Ces contraintes peuvent être appliquées soit sur des segments de droites, soit sur leurs points d\'extrémités ou leurs points centraux, et forceront la géométrie à adopter certaines règles. Par exemple, vous pouvez placer une contrainte verticale sur un segment de droite pour le forcer à rester vertical ou une contrainte de position (verrouillage) sur un point d\'extrémité pour lui interdire de se déplacer. Lorsqu\'une esquisse comporte une quantité définie de contraintes qui interdit les déplacements de tous les points de l'esquisse, nous parlons d\'une esquisse totalement contrainte. Quand il y a des contraintes redondantes, qui pourraient être supprimées sans que la géométrie ne puisse être déplacée, on dit qu'elle est sur-contrainte. Cela devrait être évité, et FreeCAD vous informera si un tel cas se produit.

Les esquisses disposent d'un mode d\'édition, où leur géométrie et leurs contraintes peuvent être modifiées. Quand vous avez terminé l\'édition, et quittez le mode d\'édition, les esquisses se comportent comme n\'importe quel autre objet FreeCAD, et peuvent être utilisées comme éléments de construction pour tous les outils de conception de pièces, mais aussi dans d\'autres ateliers, tels que l\'[atelier Part](Part_Workbench/fr.md) ou l\'[atelier Arch](Arch_Workbench/fr.md). L'[atelier Draft](Draft_Workbench/fr.md) dispose également d\'un outil qui convertit les éléments Draft en esquisses, et vice versa.

-   Commençons par modéliser une forme parallélipipédique qui sera la base de notre brique Lego. Plus tard nous allons creuser l\'intérieur et ajouter les 8 bossages sur le dessus. Commençons donc en faisant une esquisse rectangulaire que nous allons ensuite extruder :
-   Passez à l\'atelier de conception de pièces PartDesign ([Atelier PartDesign](PartDesign_Workbench/fr.md)).
-   Cliquez sur le bouton Nouvelle esquisse (<img alt="" src=images/Sketcher_NewSketch.svg  style="width:16px;"> [Sketcher Nouvelle esquisse](Sketcher_NewSketch/fr.md)). Une boîte de dialogue apparaîtra pour demander où vous voulez construire votre esquisse, choisissez le plan **XY**, qui est le plan \"sol\". L\'esquisse sera créée et sera immédiatement changée en mode édition, et la vue sera orientée pour regarder votre esquisse selon la normale au plan de travail.
-   Maintenant, nous pouvons dessiner un rectangle, en sélectionnant l\'outil <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:16px;"> [Sketcher Rectangle](Sketcher_CreateRectangle/fr.md) et en cliquant deux sommets en diagonale. Vous pouvez placer les deux points n\'importe où, car leur emplacement correct sera défini dans l\'étape suivante.
-   Vous remarquerez que quelques contraintes ont été automatiquement ajoutées à notre rectangle: les segments verticaux ont eu une contrainte verticale, les segments horizonaux une contrainte horizontale, et chaque sommet une contrainte point-sur-point qui collent les segments ensemble. Vous pouvez expérimenter le déplacement du rectangle en traînant ses lignes avec la souris, toute la géométrie continuera à obéir aux contraintes.

![](images/Exercise_lego_02.jpg )

-   Maintenant, ajoutons trois autres contraintes:
    -   Sélectionnez l\'un des segments verticaux et ajoutez une contrainte de distance vecticale (<img alt="" src=images/Constraint_VerticalDistance.svg  style="width:16px;"> [Contrainte distance en Y](Sketcher_ConstrainDistanceY.md)). Donnez-lui une dimension de 23,7 mm.
    -   Sélectionnez l\'un des segments horizontaux et ajoutez une contrainte de distance horizontale (<img alt="" src=images/Constraint_HorizontalDistance.svg  style="width:16px;"> [Sketcher Contrainte distance en X](Sketcher_ConstrainDistanceX/fr.md)). Donnez-lui la valeur de 47.7mm.
    -   Enfin, sélectionnez l\'un des points d\'angle, puis le point d\'origine (qui est le point à l'intersection des axes rouge et vert), puis ajoutez une contrainte de coïncidence (<img alt="" src=images/Constraint_PointOnPoint.svg  style="width:16px;"> [Sketcher Contrainte de coïncidence](Sketcher_ConstrainCoincident/fr.md)). Le rectangle va alors passer au point d\'origine et votre croquis devient vert, ce qui signifie qu'il est maintenant complètement contraint. Vous pouvez essayer de déplacer ses lignes ou points, rien ne bouge plus.

![](images/Exercise_lego_03.jpg )

Notez que la dernière contrainte point-sur-point n\'était pas absolument nécessaire. Vous n\'êtes jamais obligé de travailler avec des esquisses entièrement contraintes. Cependant, si nous allons imprimer ce bloc dans une imprimante 3D, il faudra maintenir notre pièce proche du point d\'origine (qui sera l\'origine de l\'espace dans lequel la tête de l\'imprimante peut se déplacer). En ajoutant cette contrainte, nous sommes assurés que notre pièce sera toujours \"ancrée\" à ce point d\'origine.

-   Notre esquisse de base est maintenant prête, nous pouvons quitter le mode d\'édition en appuyant sur le bouton **Fermer** en haut du panneau de tâches, ou simplement en appuyant sur la touche **Échap**. Si nécessaire, plus tard, nous pouvons réactiver le mode d\'édition à tout moment en double-cliquant sur le nom de l\'esquisse dans l'arbre de construction.
-   Extrudons l'esquisse en utilisant l\'outil Extrusion (<img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [PartDesign Protrusion](PartDesign_Pad/fr.md)) et donnons-lui une dimension de 14,4 mm. Les autres options peuvent être laissées à leurs valeurs par défaut:

![](images/Exercise_lego_04.jpg )

L'outil **Extrusion** se comporte comme l\'outil [Part Extrusion](Part_Extrude/fr.md) que nous avons utilisé dans le chapitre précédent. Il y a quelques différences, cependant, la principale étant qu\'un bloc ne peut pas être déplacé. Il est attaché pour toujours à son croquis. Si vous souhaitez modifier la position du bloc, vous devez déplacer l\'esquisse de base. Dans le contexte actuel, où nous voulons être sûr que rien ne bougera hors de sa position, il s\'agit d\'une sécurité supplémentaire.

-   Nous allons maintenant définir l\'intérieur du bloc, en utilisant l\'outil Poche ou Cavité (<img alt="" src=images/PartDesign_Pocket.svg  style="width:16px;"> [PartDesign Cavité](PartDesign_Pocket/fr.md)), qui est la version PartDesign de [Part Soustraction](Part_Cut/fr.md). Pour faire une poche, nous allons créer une esquisse sur la face inférieure de notre bloc qui sera utilisée pour enlever une partie du bloc.
-   Lorsque la face inférieure est sélectionnée, appuyez sur le bouton Nouvelle esquisse (<img alt="" src=images/Sketcher_NewSketch.svg  style="width:16px;"> [Sketcher Nouvelle esquisse](Sketcher_NewSketch/fr.md)).
-   Dessinez un rectangle sur la face.

![](images/Exercise_lego_05.jpg )

-   Nous allons maintenant contraindre le rectangle par rapport à la face inférieure. Pour ce faire, nous devons \"Importer\" certaines arêtes de la face avec l\'outil de (<img alt="" src=images/Sketcher_External.svg  style="width:16px;"> [Sketcher Géométrie externe](Sketcher_External/fr.md)). Utilisez cet outil sur les deux lignes verticales de la face inférieure :

![](images/Exercise_lego_06.jpg )

Vous remarquerez que seuls les bords (arêtes) de la face de base peuvent être ajoutés par cet outil. Lorsque vous créez une esquisse avec une face pré-sélectionnée, une relation est créée entre cette face et l\'esquisse, ce qui est important pour de nouvelles opérations. Vous pouvez toujours relier une esquisse à une autre face plus tard avec l\'outil (<img alt="" src=images/Sketcher_MapSketch.svg  style="width:16px;"> [Sketcher Appliquer une esquisse sur une face](Sketcher_MapSketch/fr.md)).

-   La géométrie externe n\'est pas \"réelle\", elle sera cachée lorsque nous quitterons le mode édition. Mais nous pouvons l\'utiliser pour placer des contraintes. Placez les 4 contraintes suivantes :
    -   Sélectionnez les deux points supérieurs à gauche du rectangle et sur la ligne importée de gauche et ajoutez une contrainte de distance horizontale (<img alt="" src=images/Constraint_HorizontalDistance.svg  style="width:16px;"> [Sketcher Contrainte de distance en X](Sketcher_ConstrainDistanceX/fr.md)) de 1,8 mm.
    -   Sélectionnez de nouveau les deux points supérieurs à gauche du rectangle et sur la ligne importée de gauche. Ajoutez une contrainte de distance vecticale (<img alt="" src=images/Constraint_VerticalDistance.svg  style="width:16px;"> [Sketcher Contrainte de distance en Y](Sketcher_ConstrainDistanceY/fr.md)) de 1,8 mm.
    -   Sélectionnez les deux points inférieurs à droite du rectangle et sur la ligne importée de droite et ajoutez une contrainte de distance horizontale (<img alt="" src=images/Constraint_HorizontalDistance.svg  style="width:16px;"> [Sketcher Contrainte de distance en X](Sketcher_ConstrainDistanceX/fr.md)) de 1,8 mm.
    -   Sélectionnez de nouveau les deux points inférieurs à droite du rectangle et sur la ligne importée de droite et ajoutez une contrainte de distance verticale (<img alt="" src=images/Constraint_VerticalDistance.svg  style="width:16px;"> [Sketcher Contrainte de distance en Y](Sketcher_ConstrainDistanceY/fr.md)) de 1,8 mm.

![](images/Exercise_lego_07.jpg )

Quittez le mode d\'édition et vous pouvez maintenant effectuer l\'opération de poche : l\'esquisse étant sélectionnée, appuyez sur le bouton Poche (<img alt="" src=images/PartDesign_Pocket.svg  style="width:16px;"> [PartDesign Cavité](PartDesign_Pocket/fr.md)). Donnez-lui une longueur de 12,6 mm, qui laissera la face supérieure de notre bloc avec une épaisseur de 1,8 mm (rappelez-vous, la hauteur totale de notre bloc était de 14,4 mm).

![](images/Exercise_lego_08.jpg )

-   Nous allons maintenant attaquer les 8 bossages sur la face supérieure. Pour ce faire, comme ils sont une répétition d\'une même fonction, nous utiliserons l\'outil pratique Copie Linéaire (<img alt="" src=images/PartDesign_LinearPattern.svg  style="width:16px;"> [PartDesign Répétition linéaire](PartDesign_LinearPattern/fr.md)) de l'atelier PartDesign, qui permet de modéliser une fois et de répéter la forme.
-   Commencez par sélectionner la face supérieure de notre bloc.
-   Créez une nouvelle esquisse (<img alt="" src=images/Sketcher_NewSketch.svg  style="width:16px;"> [Sketcher Nouvelle esquisse](Sketcher_NewSketch/fr.md)).
-   Créez deux cercles (<img alt="" src=images/Sketcher_Circle.png  style="width:16px;"> [Sketcher Cercles](Sketcher_CreateCircle/fr.md)).
-   Ajoutez une contrainte de rayon (<img alt="" src=images/Constraint_Radius.svg  style="width:16px;"> [Sketcher Contrainte rayon](Sketcher_ConstrainRadius/fr.md)) de 3,6 mm à chacun d\'eux.
-   Importez l'arête gauche de la face de base avec l\'outil Géométrie Externe (<img alt="" src=images/Sketcher_External.svg  style="width:16px;"> [Sketcher Géométrie externe](Sketcher_External/fr.md)).
-   Placez deux contraintes verticales et deux contraintes horizontales de 6 mm entre le centre de chaque cercle et les points d\'angle du bord importé, donc chaque cercle a son centre à 6mm de la bordure de la face :

![](images/Exercise_lego_09.jpg )

-   Notez comment, une fois de plus, lorsque vous verrouillez la position et la dimension de tous les éléments de votre esquisse, celle-ci devient complètement contrainte. Cela vous assure du résultat pour la suite. Vous pourriez modifier la première esquisse maintenant, tout ce que nous avons fait ensuite serait conservé.
-   Quittez le mode d\'édition, sélectionnez cette nouvelle esquisse et créez une extrusion (<img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [PartDesign Protrusion](PartDesign_Pad.md)) de 2.7mm :

![](images/Exercise_lego_10.jpg )

-   Notez que, comme précédemment avec la poche, puisque nous avons utilisé la face supérieure de notre bloc de base en tant que support pour cette dernière esquisse, toute opération PartDesign que nous effectuons avec cette esquisse sera correctement construite en haut de la forme de base : les deux bossages ne sont pas des objets indépendants, ils ont été extrudés directement de notre brique. C\'est le grand avantage de travailler avec l\'atelier Part Design : tant que vous prenez garde à construire une forme à partir de la forme précédente, vous construisez réellement un dernier objet solide.
-   Nous pouvons maintenant dupliquer nos deux bossages quatre fois, alors nous en aurons huit. Sélectionnez le dernier bossage que nous venons de créer.
-   Appuyez sur le bouton de copie linéaire (<img alt="" src=images/PartDesign_LinearPattern.svg  style="width:16px;"> [PartDesign Répétition linéaire](PartDesign_LinearPattern/fr.md)).
-   Donnez-lui une longueur de 36 mm (qui est l'amplitude totale que nous souhaitons occuper avec nos copies), dans la direction «Axe d\'esquisse horizontale», et faites-en 4 occurrences :

![](images/Exercise_lego_11.jpg )

-   Encore une fois, il faut voir que ce n\'est pas seulement une duplication d\'un objet, c\'est une \*caractéristique ou fonction\* de notre forme qui a été dupliquée, l\'objet final n\'est encore qu\'un seul objet solide.
-   Maintenant, travaillons sur les trois «tubes» qui remplissent le vide que nous avons créé sur la face inférieure. Nous avons plusieurs possibilités : créer une esquisse avec trois cercles, l'extruder puis créer une poche trois fois, ou créer une esquisse de base avec deux cercles concentriques et les extruder pour former le tube déjà complet, ou même d\'autres combinaisons. Comme toujours dans FreeCAD, il y a de nombreuses façons d\'atteindre un même résultat. Parfois, une façon ne fonctionnera pas comme nous voulons, et nous devons essayer d\'autres façons. Ici, nous allons prendre l\'approche la plus sûre, et faire les choses l'une après l\'autre.
-   Sélectionnez la face qui se trouve au fond de l\'espace que nous avons creusé précédemment à l\'intérieur du bloc.
-   Créez une nouvelle esquisse, ajoutez un cercle avec un rayon de 4.8825mm, importez le bord gauche de la face et positionnez le centre verticalement et horizontalement à 10,2 mm du coin supérieur de la face :

![](images/Exercise_lego_12.jpg )

Si vous avez du mal à sélectionner des fonctions masquant une partie du modèle, cela peut vous aider. Pour masquer une fonction, sélectionnez-la dans l\'arborescence et appuyez sur la touche Espace pour basculer la visibilité.

-   Quittez le mode d\'édition et ajoutez de la matière par extrusion sur une longueur de 12,6 mm.
-   Créez une copie linéaire de cette dernière extrusion, donnez-lui une longueur de 24mm et 3 occurrences. Nous avons maintenant trois bossages dans l\'espace creux :

![](images/Exercise_lego_13.jpg )

-   Maintenant, faisons les derniers trous. Sélectionnez la face circulaire du premier de nos trois bossages.
-   Créez une nouvelle esquisse, importez le bord circulaire de notre face, créez un cercle avec un rayon de 3,6 mm, et ajoutez une contrainte de coïncidence (<img alt="" src=images/Constraint_PointOnPoint.svg  style="width:16px;"> [Sketcher Contrainte de coïncidence](Sketcher_ConstrainCoincident.md)) entre le centre du cercle importé et celui notre nouveau cercle. Nous avons maintenant un cercle parfaitement centré, et une fois encore complètement contraint :

![](images/Exercise_lego_14.jpg )

-   Quittez le mode d\'édition et créez une poche à partir de cette esquisse, d\'une longueur de 12,6 mm.
-   Créez une copie linéaire de cette poche, avec une longueur de 24 mm et 3 occurrences. C\'est la dernière étape, notre pièce de lego est maintenant terminée, on peut lui donner une belle couleur pour marquer notre victoire !

![](images/Exercise_lego_15.jpg )

Vous remarquerez que l'historique de modélisation ou arbre de construction (ce qui apparaît dans l\'arborescence) est devenue assez long. Ceci est précieux car chaque étape de ce que nous avons fait peut être modifié plus tard. L'adaptation de ce modèle pour un autre type de brique, par exemple une avec 2x2 bossages, au lieu de 2x4, serait du gâteau, il faudrait simplement changer quelques dimensions et le nombre d\'occurrences dans les copies linéaires. Nous pourrions créer aussi facilement des pièces plus grandes qui n'existent pas dans le jeu original de Lego.

Mais nous pourrions aussi vouloir nous débarrasser de l'historique, par exemple si nous voulons modéliser un château avec cette brique, et ne voulons pas que cet historique soit répété 500 fois dans notre fichier.

Il existe deux façons simples de se débarrasser de l'historique, on utilise l\'outil [Part Création de copie simple](Part_SimpleCopy/fr.md) de l'[atelier Part](Part_Workbench/fr.md), qui créera une copie de notre pièce qui ne dépend plus de l\'historique (vous pouvez supprimer l\'historique complet après), l\'autre façon est d\'exporter la pièce dans un fichier STEP et de la réimporter.

**Assemblage**

Mais le meilleur des deux mondes existe également, qui est l\'atelier Assembly2 ([Assembly2 Workbench](https://github.com/hamish2014/FreeCAD_assembly2)), un greffon (addon) qui peut être installé à partir du dépôt [FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons). Cet atelier s\'appelle \"2\" car il existe également un atelier intégré d\'assemblage en développement, qui n\'est pas encore prêt. L'atelier Assembly2, cependant, fonctionne déjà très bien pour construire des assemblages, et comporte également quelques contraintes d\'objet à objet que vous pouvez utiliser pour contraindre la position d\'un objet par rapport à un autre. Dans l\'exemple ci-dessous, cependant, il sera plus rapide et plus facile de positionner les pièces à l\'aide des déplacements en translation (<img alt="" src=images/Draft_Move.svg  style="width:16px;"> [Draft Déplacer](Draft_Move/fr.md)) et en rotation (<img alt="" src=images/Draft_Rotate.png  style="width:16px;"> [Draft Rotation](Draft_Rotate/fr.md)) de l'atelier Draft que d\'utiliser les contraintes d'Assembly2.

-   Enregistrez le fichier tel qu\'il est actuellement.
-   Installez l'atelier Assembly2 ([Assembly2 Workbench](https://github.com/hamish2014/FreeCAD_assembly2)) et redémarrez FreeCAD.
-   Créez un nouveau document vide.
-   Passez à l'atelier Assembly2.
-   Appuyez sur **Importer une pièce à partir d\'un autre document FreeCAD**.
-   Sélectionnez le fichier que nous avons enregistré ci-dessus.
-   La pièce finale sera importée dans le document actuel. L\'atelier Assembly2 déterminera automatiquement quelle est la pièce finale dans notre fichier qui doit être utilisée, et le nouvel objet reste lié au fichier d'origine. Si nous revenons en arrière et modifions le contenu du premier fichier, nous pouvons appuyer sur le bouton **Mettre à jour les pièces importées dans l\'assemblage** pour les mettre à jour ici.
-   En utilisant le bouton*\' Importer une pièce à partir d\'un autre document FreeCAD*\' plusieurs fois, et en déplaçant et en orientant les pièces convenablement (avec les outils de l'atelier Draft ou en manipulant leurs propriétés de placement), nous pouvons créer rapidement un petit assemblage :

![](images/Exercise_lego_16.jpg )

**Téléchargements**

-   Le modèle produit lors de cet exercice: <https://github.com/yorikvanhavre/FreeCADmanual/Blob/master/files/lego.FCStd>

**Lire plus d\'informations**

-   [L'atelier Sketcher](Sketcher_Workbench.md)
-   [L'atelier Part Design](PartDesign_Workbench.md)
-   [L'atelier Assembly2](https://github.com/hamish2014/FreeCAD_assembly2)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Modeling for product design/fr
