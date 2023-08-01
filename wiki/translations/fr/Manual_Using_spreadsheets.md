# Manual:Using spreadsheets/fr
{{Manual:TOC/fr}}

FreeCAD dispose d\'un autre atelier intéressant à explorer : l'[atelier Spreadsheet](Spreadsheet_Workbench/fr.md). Cet atelier permet de créer des [feuilles de calcul](https://fr.wikipedia.org/wiki/Tableur) telles que celles réalisées avec [Excel](https://fr.wikipedia.org/wiki/Microsoft_Excel) ou [Calc de LibreOffice](https://fr.wikipedia.org/wiki/LibreOffice#Calc) directement dans FreeCAD. Ces feuilles de calcul peuvent ensuite être remplies avec des données extraites de votre modèle et peuvent également effectuer une série de calculs entre les valeurs. Les feuilles de calcul peuvent être exportées sous forme de fichiers CSV, qui peuvent être importés dans n\'importe quelle autre application de tableur.

Dans FreeCAD, cependant, les feuilles de calcul ont une utilité supplémentaire : leurs cellules peuvent recevoir un nom et peuvent être référencées par n\'importe quel champ pris en charge par le moteur des [expressions](Expressions/fr.md). Cela transforme les feuilles de calcul en puissantes structures de contrôle, où les valeurs insérées dans des cellules spécifiques peuvent générer des dimensions du modèle. Il n\'y a qu\'une chose à garder à l\'esprit, car FreeCAD interdit les dépendances circulaires entre les objets, une même feuille de calcul ne peut pas être utilisée pour définir une propriété d\'un objet et, en même temps, récupérer une valeur de propriété à partir du même objet. Cela voudrait dire que la feuille de calcul et l\'objet sont interdépendants.

Dans l\'exemple suivant, nous allons créer quelques objets, récupérer certaines de leurs propriétés dans une feuille de calcul, puis utiliser la feuille de calcul pour générer directement les propriétés d\'autres objets.

### Lecture de propriétés 

-   Commencez par passer à l'[atelier Part](Part_Workbench/fr.md) et créez quelques objets : un <img alt="" src=images/Part_Box.svg  style="width:16px;"> [cube](Part_Box/fr.md), un <img alt="" src=images/Part_Cylinder.svg  style="width:16px;"> [cylindre](Part_Cylinder/fr.md) et une <img alt="" src=images/Part_Sphere.svg  style="width:16px;"> [sphère](Part_Sphere/fr.md).
-   Modifiez leur propriété de **Placement** (ou utilisez l\'outil <img alt="" src=images/Draft_Move.svg  style="width:16px;"> [Draft Déplacer](Draft_Move/fr.md)) pour les séparer un peu, afin que nous puissions mieux observer les effets de ce que nous allons faire :

![](images/Exercise_spreadsheet_01.jpg )

-   Maintenant, on va extraire des informations sur ces objets. Passez à l\'[atelier Spreadsheet](Spreadsheet_Workbench/fr.md).
-   Appuyez sur le bouton <img alt="" src=images/Spreadsheet_Create.png  style="width:16px;"> **Créer une feuille de calcul**.
-   Double-cliquez sur l\'objet Spreadsheet dans la vue en arborescence. L\'éditeur de feuille de calcul s\'ouvre :

![](images/Exercise_spreadsheet_02.jpg )

L\'éditeur de feuilles de calcul de FreeCAD, bien qu\'il ne soit pas aussi complet et puissant que les applications de tableurs plus complètes que nous avons énumérées ci-dessus, a néanmoins la plupart des outils et des fonctions de base couramment utilisés, comme la possibilité de modifier l\'aspect des cellules (Taille, couleur, alignement), joindre et diviser les cellules, utiliser des formules telles que **=2+2**, ou référencer d\'autres cellules avec **=B1**.

Dans FreeCAD, en plus de ces comportements communs, on a ajouté une possibilité très intéressante : la possibilité de faire référence non seulement à d\'autres cellules, mais aussi d\'autres objets du document, et de récupérer des valeurs à partir de leurs propriétés. Par exemple, récupérons quelques propriétés des 3 objets que nous avons créés ci-dessus. Les propriétés sont ce que nous pouvons voir dans la fenêtre de l\'éditeur de propriétés, sous l\'onglet **Données** (Data), lorsqu\'un objet est sélectionné.

-   Commençons par entrer quelques textes dans les cellules A1, A2 et A3, alors nous nous souvenons de ce qui se passera plus tard, par exemple **Cube Length** (longueur de l'arête du cube), **Cylinder Radius** (rayon du cylindre) et **Sphere Radius** (rayon de la sphère). Pour entrer du texte, écrivez simplement dans le champ \"Conteneur\" disposé au-dessus de la feuille de calcul ou double-cliquez sur une cellule.
-   Maintenant, récupérons la longueur réelle de notre cube. Dans la cellule B1, tapez **=Cube.Length**. Vous remarquerez que la feuille de calcul possède un mécanisme de remplissage automatique, qui est en fait le même que l\'éditeur d\'expression que nous avons utilisé dans le chapitre précédent.
-   Faites de même pour la cellule B2 (**=Cylinder.Radius**) et B3 (**=Sphere.Radius**).

![](images/Exercise_spreadsheet_03.jpg )

-   Bien que ces résultats soient exprimés avec leurs unités, les valeurs peuvent être manipulées comme n\'importe quel nombre, essayez, par exemple, d\'entrer dans la cellule C1 : **=B1\*2**.
-   Nous pouvons maintenant modifier une de ces valeurs dans l\'éditeur de propriétés, et la modification sera immédiatement reflétée dans la feuille de calcul. Par exemple, modifions la longueur de notre cube à **20mm** :

![](images/Exercise_spreadsheet_04.jpg )

La page de l\'[atelier Spreadsheet](Spreadsheet_Workbench/fr.md) décrit plus en détail toutes les opérations et fonctions disponibles que vous pouvez utiliser dans les feuilles de calcul.

### Ecriture de propriétés 

Une autre utilisation très intéressante de l'atelier Feuilles de calcul dans FreeCAD est de faire le contraire de ce que nous avons fait jusqu\'ici : au lieu de lire les valeurs des propriétés des objets 3D, nous pouvons également attribuer des valeurs à ces objets. Rappelez-vous, cependant, une des règles fondamentales de FreeCAD : les dépendances circulaires sont interdites. Nous ne pouvons donc pas utiliser la même feuille de calcul pour lire **et** écrire des valeurs sur un objet 3D. Cela rendrait l\'objet dépendant de la feuille de calcul, qui dépendrait également de l\'objet. Au lieu de cela, nous allons créer une autre feuille de calcul.

-   Nous pouvons maintenant fermer l\'onglet tableur (sous la vue 3D). Ceci n\'est pas obligatoire, il n\'y a pas de problème pour ouvrir plusieurs feuilles de calcul.
-   Appuyez de nouveau sur le bouton <img alt="" src=images/Spreadsheet_Create.png  style="width:16px;"> **Créer une feuille de calcul**.
-   Modifiez le nom de la nouvelle feuille de calcul en quelque chose de plus significatif, comme **Input** (faites-le en cliquant avec le bouton droit de la souris sur la nouvelle feuille de calcul et en choisissant **Renommer**).
-   Double-cliquez sur la feuille de calcul **Input** pour ouvrir l\'éditeur du tableur.
-   Dans la cellule A1, mettons un texte descriptif, par exemple: \"Dimensions du cube\".
-   Dans la cellule B1, écrivez **=5mm** (en utilisant le signe = on s\'assure que la valeur est interprétée comme une valeur numérique, pas un texte).
-   Maintenant, pour pouvoir utiliser cette valeur en dehors de la feuille de calcul, nous devons donner un nom ou alias à la cellule B1. Cliquez avec le bouton droit sur la cellule, cliquez sur **Propriétés** et sélectionnez l\'onglet **Alias**. Donnez-lui un nom, tel que **cubedims** :

![](images/Exercise_spreadsheet_05.jpg )

-   Appuyez sur **OK**, puis fermez l\'onglet tableur.
-   Sélectionnez l\'objet cube.
-   Dans l\'éditeur de propriétés, cliquez sur la petite icône <img alt="" src=images/Bound-expression-unset.png  style="width:16px;"> **expression** située sur le côté droit du champ **Longueur**. Cela ouvrira l\'[éditeur d\'expressions](Expressions/fr.md), où vous pouvez écrire **Spreadsheet001.cubedims**. Répétez ceci pour **Hauteur** et **Largeur** :

![](images/Exercise_spreadsheet_06.jpg )

Vous pourriez vous demander pourquoi nous devons utiliser \"Spreadsheet001\" au lieu de \"Input\" dans l\'expression ci-dessus. C\'est parce que chaque objet, dans un document FreeCAD, a un **nom interne**, unique dans le document, et une **étiquette**, qui apparait dans l\'arborescence. Si vous désactivez l\'option appropriée dans la fenêtre des préférences, FreeCAD vous permettra de donner la même étiquette à plus d\'un objet. C\'est pourquoi toutes les opérations devant identifier un objet de manière unique utiliseront le nom interne au lieu du libellé, qui pourrait désigner plus d\'un objet. Le moyen le plus simple de connaître le nom interne d\'un objet est en gardant ouvert le panneau **Afficher la sélection** (barre de menu Affichage → Panneaux), il indiquera toujours le nom interne d\'un objet sélectionné :

![](images/Exercise_spreadsheet_07.jpg )

En utilisant des alias dans les cellules dans des feuilles de calcul, nous pouvons utiliser une feuille de calcul pour stocker des \"valeurs de base\" dans un document FreeCAD. Cela peut être utilisé, par exemple, pour avoir certaines dimensions d\'un modèle et pour stocker ces dimensions dans une feuille de calcul. Il devient alors très facile de produire un autre modèle avec des dimensions différentes, il s\'agit simplement d\'ouvrir le fichier et de modifier quelques dimensions dans la feuille de calcul.

Enfin, notez que les contraintes dans un croquis peuvent également recevoir la valeur d\'une cellule de tableur :

![](images/Exercise_spreadsheet_08.jpg )

Vous pouvez également donner des alias aux contraintes dimensionnelles (horizontales, verticales ou distances) dans une esquisse (vous pouvez ensuite utiliser ces valeurs à l\'extérieur de l'esquisse) :

![](images/Exercise_spreadsheet_09.jpg )

**Télécharger**

-   Le fichier produit dans cet exercice: <https://github.com/yorikvanhavre/FreeCADmanual/Blob/master/files/spreadsheet.FCStd>

**Lire plus d\'informations**

-   [Atelier Spreadsheet](Spreadsheet_Workbench/fr.md)
-   [Le moteur des Expressions](Expressions/fr.md)



---
⏵ [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Using spreadsheets/fr
