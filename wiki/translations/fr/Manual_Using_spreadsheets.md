# Manual:Using spreadsheets/fr
{{Manual:TOC}}

L\'<img alt="" src=images/Workbench_Spreadsheet.svg  style="width:16px;"> [atelier Spreadsheet](Spreadsheet_Workbench/fr.md) dans FreeCAD permet aux utilisateurs de créer et de gérer des [feuilles de calcul](https://fr.wikipedia.org/wiki/Tableur), telles que celles faites avec [Excel](https://fr.wikipedia.org/wiki/Microsoft_Excel) ou [Calc de LibreOffice](https://fr.wikipedia.org/wiki/LibreOffice#Calc), directement dans leurs projets de conception. Il permet de saisir, d\'organiser et de manipuler des données sous forme de tableau, qui peuvent ensuite être liées à divers paramètres et modèles dans le projet.

L\'un de ses principaux avantages est son utilisation dans la modélisation paramétrique. Les feuilles de calcul peuvent être reliées aux dimensions et aux propriétés des modèles 3D, ce qui en fait un outil essentiel pour les modifications dynamiques de la conception. Par exemple, l\'ajustement d\'une valeur dans la feuille de calcul mettra automatiquement à jour la dimension correspondante dans le modèle.

Outre la gestion des valeurs, l\'atelier est excellent pour la gestion des données, en stockant des informations essentielles telles que les propriétés des matériaux, les dimensions et les paramètres de l\'ensemble du projet. Cela s\'avère particulièrement utile dans les projets complexes où plusieurs valeurs doivent être référencées ou ajustées.

Les feuilles de calcul permettent également aux utilisateurs de saisir des formules pour les calculs et la gestion des données. Ces formules peuvent faire référence à d\'autres cellules du tableur ou à des paramètres du modèle 3D, ce qui rend l\'ensemble du processus de conception adaptable et réactif aux changements.

Il peut s\'intégrer de manière transparente à d\'autres ateliers FreeCAD, ce qui permet une interaction entre les données et les composants du modèle. Cette intégration centralise le contrôle des différents aspects du projet, ce qui en facilite la gestion. L\'interface est simple, ressemblant à un tableur traditionnel, ce qui la rend familière et facile à utiliser pour ceux qui sont déjà habitués à des programmes comme Excel ou LibreOffice Calc.

En pratique, l\'atelier Spreadsheet est polyvalent pour différents cas d\'utilisation, notamment la définition de paramètres à l\'échelle du projet, la gestion des nomenclatures et l\'exécution de calculs personnalisés qui influencent les décisions de conception. Il simplifie les projets complexes en centralisant le contrôle des paramètres en un seul endroit.

Dans l\'exemple suivant, nous allons créer quelques objets, récupérer certaines de leurs propriétés dans une feuille de calcul, puis utiliser la feuille de calcul pour piloter directement les propriétés d\'autres objets.



### Lire des propriétés 

-   Commencez par passer à l'<img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [atelier Part](Part_Workbench/fr.md) et créez quelques objets : un <img alt="" src=images/Part_Box.svg  style="width:16px;"> [cube](Part_Box/fr.md), un <img alt="" src=images/Part_Cylinder.svg  style="width:16px;"> [cylindre](Part_Cylinder/fr.md) et une <img alt="" src=images/Part_Sphere.svg  style="width:16px;"> [sphère](Part_Sphere/fr.md).
-   Modifiez leur propriété **Placement** (ou utilisez l\'outil <img alt="" src=images/Draft_Move.svg  style="width:16px;"> [Draft Déplacer](Draft_Move/fr.md)) pour les séparer un peu, afin que nous puissions mieux observer les effets de ce que nous allons faire :

<img alt="" src=images/Exercise_spreadsheet_01.jpg  style="width:600px;">

-   Maintenant, on va extraire des informations sur ces objets. Passez à l\'<img alt="" src=images/Workbench_Spreadsheet.svg  style="width:16px;"> [atelier Spreadsheet](Spreadsheet_Workbench/fr.md).
-   Appuyez sur le bouton <img alt="" src=images/Spreadsheet_Create.png  style="width:16px;"> **Créer une feuille de calcul**.
-   Double-cliquez sur l\'objet Spreadsheet dans la vue en arborescence. L\'éditeur de feuille de calcul s\'ouvre :

<img alt="" src=images/FreeCAD_Spreedsheet.png  style="width:600px;">

Bien que l\'éditeur de feuilles de calcul de FreeCAD ne soit pas aussi riche en fonctionnalités que des applications dédiées comme Excel ou LibreOffice Calc, il fournit des outils essentiels pour la plupart des tâches de conception. Les utilisateurs peuvent ajuster les propriétés des cellules telles que la taille, la couleur et l\'alignement, et fusionner ou diviser les cellules pour une meilleure organisation. Les formules de base ou les références à d\'autres cellules sont prises en charge, ce qui permet une manipulation simple des données. Ce qui le distingue, c\'est son intégration profonde avec l\'environnement de modélisation de FreeCAD, où les modifications apportées à la feuille de calcul peuvent automatiquement mettre à jour les dimensions du modèle en temps réel. Bien qu\'il ne dispose pas de fonctions avancées telles que les tableaux croisés dynamiques ou les graphiques, son orientation vers la conception paramétrique en fait un outil puissant pour la gestion des données de conception directement dans FreeCAD.

Dans FreeCAD, au-delà des fonctionnalités standard des tableurs, il existe une fonction particulièrement utile : la possibilité de référencer non seulement d\'autres cellules, mais aussi des objets au sein du document et d\'extraire des valeurs de leurs propriétés. Par exemple, vous pouvez extraire les propriétés des objets 3D qui sont visibles dans l\'onglet **Données** de l**\'Éditeur de propriétés** lorsqu\'un objet est sélectionné. Cela permet une intégration transparente entre la feuille de calcul et le modèle 3D, facilitant la liaison et l\'automatisation des modifications basées sur les paramètres des objets de la conception, offrant ainsi un flux de travail plus dynamique et interconnecté.

-   Commençons par saisir quelques textes dans les cellules A1, A2 et A3, afin de nous souvenir de ce qui est quoi par la suite, par exemple **Cube Length**, **Cylinder Radius** et **Sphere Radius**. Pour saisir du texte, il suffit d\'écrire dans le champ « Contenu » au-dessus de la feuille de calcul, ou de double-cliquer sur une cellule.
-   Récupérons maintenant la longueur réelle de notre cube. Dans la cellule B1, tapez **=Cube.Length**. Vous remarquerez que le tableur dispose d\'un mécanisme d\'auto-complétion, qui est en fait le même que l\'éditeur d\'expressions que nous avons utilisé dans le chapitre précédent.
-   Faites de même pour les cellules B2 (**=Cylinder.Radius**) et B3 (**=Sphere.Radius**).

<img alt="" src=images/FreeCAD_Spreedsheet_Autocomplete.png  style="width:600px;">

-   Bien que ces résultats soient exprimés avec leurs unités, les valeurs peuvent être manipulées comme n\'importe quel nombre, essayez, par exemple, d\'entrer dans la cellule C1 : **=B1\*2**.
-   Nous pouvons maintenant modifier une de ces valeurs dans l\'éditeur de propriétés, et la modification sera immédiatement reflétée dans la feuille de calcul. Par exemple, modifions la longueur de notre cube à **20mm** :

<img alt="" src=images/FreeCAD_Spreedsheet_Multipl.png  style="width:600px;">

La page de l\'<img alt="" src=images/Workbench_Spreadsheet.svg  style="width:16px;"> [atelier Spreadsheet](Spreadsheet_Workbench/fr.md) décrit plus en détail toutes les opérations et fonctions disponibles que vous pouvez utiliser dans les feuilles de calcul.



### Écrire des propriétés 

Une autre fonctionnalité puissante de l\'atelier Spreadsheet de FreeCAD est la possibilité non seulement de lire les valeurs des propriétés des objets 3D, mais aussi de leur attribuer des valeurs. Cela permet de contrôler les dimensions et les attributs des objets directement à partir de la feuille de calcul. Cependant, l\'une des règles fondamentales de FreeCAD est que les dépendances circulaires sont interdites, ce qui signifie qu\'une feuille de calcul ne peut pas à la fois lire et écrire sur le même objet. Cela créerait une situation où l\'objet dépendrait de la feuille de calcul tandis que la feuille de calcul dépendrait également de l\'objet, ce qui conduirait à une configuration invalide. Pour éviter cela, une deuxième feuille de calcul est généralement créée pour gérer l\'écriture des valeurs, ce qui garantit une séparation claire entre les processus de lecture et d\'écriture.

-   Nous pouvons maintenant fermer l\'onglet du tableur (sous la vue 3D). Ce n\'est pas obligatoire, il n\'y a aucun problème à garder plusieurs fenêtres de feuilles de calcul ouvertes.
-   Appuyez à nouveau sur le bouton <img alt="" src=images/Spreadsheet_Create.svg  style="width:16px;"> **Nouvelle feuille de calcul**.
-   Changez le nom de la nouvelle feuille de calcul en quelque chose de plus significatif, comme **Input** (faites-le en cliquant avec le bouton droit de la souris sur le nouvel objet feuille de calcul et en choisissant **Renommer**).
-   Double-cliquez sur la feuille de calcul Input pour ouvrir l\'éditeur de feuille de calcul.
-   Dans la cellule A1, mettons un texte descriptif, par exemple : \"Cube dimensions\"
-   Dans la cellule B1, écrivons **=5mm** (l\'utilisation du signe = permet de s\'assurer que la valeur est interprétée comme une valeur unitaire, et non comme un texte).
-   Pour pouvoir utiliser cette valeur en dehors de la feuille de calcul, nous devons donner un nom, ou un alias, à la cellule B1. Cliquez avec le bouton droit de la souris sur la cellule, cliquez sur **Propriétés** et sélectionnez l\'onglet **Alias**. Donnez-lui un nom, par exemple **cubedims** :

<img alt="" src=images/FreeCAD_Spreedsheet_Alias.png  style="width:600px;">

-   Appuyez sur **OK**, puis fermer l\'onglet de la feuille de calcul
-   Sélectionnez l\'objet cube.
-   Dans l\'éditeur de propriétés, cliquez sur l\'icône <img alt="" src=images/Bound-expression-unset.png  style="width:16px;"> **expression** située sur le côté droit du champ **Length**. Cela ouvrira l\'[éditeur d\'expressions](Expressions/fr.md), où vous pouvez écrire **Spreadsheet001.cubedims**. Répétez ceci pour **Height** et **Width** :

<img alt="" src=images/FreeCAD_SpreedSheet_Dim.png  style="width:600px;">

La raison pour laquelle nous utilisons « Spreadsheet001 » au lieu de « Input » dans l\'expression est que chaque objet dans un document FreeCAD a un nom interne unique et une étiquette plus conviviale. Alors que l\'étiquette est ce qui apparaît dans l\'arborescence, le nom interne est utilisé pour identifier de manière unique les objets dans le document. FreeCAD vous permet d\'attribuer la même étiquette à plusieurs objets si vous réglez vos préférences, mais le nom interne reste unique. Pour toute opération nécessitant l\'identification d\'un objet sans ambiguïté, FreeCAD utilise le nom interne plutôt que l\'étiquette, car l\'étiquette peut se référer à plusieurs objets. Pour trouver le nom interne d\'un objet, il est utile de garder le panneau de sélection (accessible via Affichage → Panneaux) ouvert. Ce panneau affichera toujours le nom interne de l\'objet sélectionné, ce qui vous permettra d\'utiliser la bonne référence dans vos expressions.

<img alt="" src=images/FreeCAD_SpreedSheet_SelectionView.png  style="width:600px;">

En utilisant des alias de cellules dans l\'atelier Spreadsheet de FreeCAD, il est possible de stocker des « valeurs de référence » dans le document, ce qui facilite la gestion et la modification des paramètres clés. Par exemple, une feuille de calcul peut contenir les dimensions d\'un modèle, ce qui permet de référencer ces valeurs tout au long de la conception. Cette approche simplifie le processus de mise à jour du modèle. Si de nouvelles dimensions sont nécessaires, il suffit d\'ouvrir la feuille de calcul, d\'ajuster les valeurs et le modèle sera automatiquement mis à jour pour refléter ces changements. Cette méthode rationalise la gestion des versions et améliore l\'efficacité, en particulier dans la modélisation paramétrique, où les dimensions changent fréquemment en fonction des exigences du projet.

Enfin, notez que les contraintes dans une esquisse peuvent également recevoir la valeur d\'une cellule de tableur :

Vous pouvez également donner des alias aux contraintes dimensionnelles (horizontales, verticales ou distances) dans une esquisse (vous pouvez ensuite utiliser ces valeurs à l\'extérieur de l'esquisse) :

<img alt="" src=images/FreeCAD_SpreedSheet_Rectangle.png  style="width:600px;">

**Télécharger**

-   Le fichier produit dans cet exercice: <https://github.com/yorikvanhavre/FreeCADmanual/Blob/master/files/spreadsheet.FCStd>

**Lire plus d\'informations**

-   [Atelier Spreadsheet](Spreadsheet_Workbench/fr.md)
-   [Expressions](Expressions/fr.md)



---
⏵ [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Using spreadsheets/fr
