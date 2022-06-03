# Manual:Creating FEM analyses/fr
{{Manual   *TOC/fr}}

FEM, en anglais Finite Element Method, signifie Méthode des éléments finis ([Méthode des éléments finis](https   *//fr.wikipedia.org/wiki/M%C3%A9thode_des_%C3%A9l%C3%A9ments_finis)). Il s\'agit d\'un vaste sujet mathématique que dans FreeCAD nous pouvons résumer par moyen de calculer les propagations à l\'intérieur d\'un objet 3D en le coupant en petits morceaux et en analysant l\'impact de chaque petit morceau sur ses voisins. Cela a plusieurs utilisations dans les domaines de l\'ingénierie et de l\'électromagnétisme. Nous examinerons plus en profondeur une seule utilisation déjà développée dans FreeCAD qui simule des déformations dans des objets soumis à des forces et à des poids.

L\'obtention de cette simulation se fait dans FreeCAD avec l\'[atelier FEM](FEM_Workbench/fr.md). Cela implique différentes étapes    * préparer la géométrie, définir son matériau, effectuer le maillage, diviser en parties plus petites, comme nous l\'avons fait dans le chapitre ([Préparer les objets pour l'impression 3D](Manual   *Preparing_models_for_3D_printing/fr.md)) et finalement calculer la simulation.

<img alt="" src=images/Exercise_fem_01.jpg  style="width   *600px;">

### Préparation de FreeCAD 

La simulation elle-même est réalisée par un autre logiciel utilisé par FreeCAD pour obtenir les résultats. Il existe plusieurs applications de simulation FEM intéressantes et disponibles. L'[Atelier FEM](FEM_Workbench/fr.md) vous permet de choisir parmi ces applications. Cependant, actuellement, seul [CalculiX](http   *//www.calculix.de/) est entièrement implémenté. Un autre logiciel, appelé [NetGen](https   *//sourceforge.net/projects/netgen-mesher/), en charge de la génération du maillage de subdivision est également nécessaire. Des instructions détaillées pour installer ces deux composants sont fournies dans la documentation FreeCAD ([Installation de FEM](FEM_Install/fr.md)).

### Préparation de la géométrie 

Nous allons commencer avec la maison que nous avons modélisée dans le chapitre de modélisation BIM ([Modélisation BIM](Manual   *BIM_modeling/fr.md)). Certains changements doivent néanmoins être apportés pour rendre le modèle adapté aux calculs FEM. Nous écartons les objets que nous ne voulons pas inclure dans le calcul, comme la porte et la fenêtre, et assemblons tous les objets restants en un seul.

-   Chargez le modèle de maison que nous avons modélisé précédemment ([house model](https   *//github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/house.FCStd)).
-   Supprimez ou masquez l\'objet de la page, les plans de section et les dimensions, de sorte qu'il ne nous reste que notre modèle.
-   Cachez la fenêtre, la porte et la dalle de sol.
-   Masquez également les poutres métalliques du toit. Comme ce sont des objets très différents du reste de la maison, nous simplifierons notre calcul en ne les incluant pas. Au lieu de cela, nous considérons que la dalle du toit est directement placée sur le dessus du mur.
-   Maintenant, déplacez la dalle du toit vers le bas, de sorte qu\'elle repose sur le mur    * éditez l\'objet **Rectangle** que nous avons utilisé comme base de la dalle du toit et changez son **Positionnement-\> Position-\> Valeur X** de 3,18 m à 3,00 m.
-   Notre modèle est maintenant propre    *

   *   <img alt="" src=images/Exercise_fem_02.jpg  style="width   *600px;">

-   L'atelier FEM ne peut actuellement calculer des déformations que sur un seul objet. Par conséquent, nous devons fusionner nos deux objets (le mur et la dalle). Passez à l'[Atelier Pièce](Part_Workbench/fr.md), sélectionnez les deux objets et appuyez sur le bouton **<img src="images/Part_Fuse.svg" width=16px> [Union](Part_Fuse/fr.md)**. Nous avons maintenant obtenu un objet fusionné    *

   *   <img alt="" src=images/Exercise_fem_03.jpg  style="width   *600px;">

### Création de l\'analyse 

-   Nous sommes maintenant prêts à commencer une analyse FEM. Passons à l'[atelier FEM](FEM_Workbench/fr.md).
-   Sélectionnez l\'objet résultat de la fusion.
-   Appuyez sur le bouton **<img src="images/FEM_Analysis.svg" width=16px> [Conteneur d'analyse](FEM_Analysis/fr.md)**.
-   Une nouvelle analyse sera créée et des panneaux de configuration seront ouverts. Ici, vous pouvez définir les paramètres de maillage à utiliser pour produire le maillage FEM. Le paramètre principal à éditer est la **taille maximale** qui définit la taille maximale (en millimètres) de chaque pièce du maillage. Pour l\'instant, nous pouvons laisser la valeur par défaut de 1000    *

   *   <img alt="" src=images/Exercise_fem_04.jpg  style="width   *600px;">

-   Après avoir appuyé sur **OK** et quelques secondes de calcul, notre maillage FEM est maintenant prêt    *

   *   <img alt="" src=images/Exercise_fem_05.jpg  style="width   *600px;">

-   Nous pouvons maintenant définir le matériau à appliquer à notre maillage. Ceci est important car, en fonction de la force matérielle, notre objet réagira différemment aux forces qui lui sont appliquées. Sélectionnez l\'objet d\'analyse et appuyez sur le bouton **<img src="images/FEM_MaterialSolid.svg" width=16px> [Créer un matériau FEM pour le solide](FEM_MaterialSolid/fr.md)**.
-   Un panneau de tâches s\'ouvrira pour nous permettre de choisir un matériau. Dans la liste déroulante Matériaux, choisissez le matériau en **béton générique** (en anglais Concrete-generic) et appuyez sur le bouton **OK**.

   *   <img alt="" src=images/Exercise_fem_06.jpg  style="width   *600px;">

-   Nous sommes maintenant prêts à appliquer des forces. Commençons par préciser quelles faces sont fixées au sol et ne peuvent donc pas bouger. Appuyez sur le bouton **<img src="images/FEM_ConstraintFixed.svg" width=16px> [FEM Contrainte fixée](FEM_ConstraintFixed/fr.md)**.
-   Cliquez sur la face inférieure de notre bâtiment et appuyez sur le bouton **OK**. La face inférieure est maintenant indiquée comme inamovible    *

   *   <img alt="" src=images/Exercise_fem_07.jpg  style="width   *600px;">

-   Nous allons maintenant ajouter une charge sur la face supérieure, qui pourrait représenter, par exemple, un poids massif sur le toit. Pour cela, nous utiliserons une contrainte de pression. Appuyez sur le bouton **<img src="images/FEM_ConstraintPressure.svg" width=16px> [Contrainte de pression](FEM_ConstraintPressure/fr.md)**.
-   Cliquez sur la face supérieure du toit, mettez la pression sur **10 MPa** (la pression est appliquée par millimètre carré) et cliquez sur le bouton **OK**. Notre force est maintenant appliquée    *

   *   <img alt="" src=images/Exercise_fem_08.jpg  style="width   *600px;">

-   Nous sommes maintenant prêts à commencer le calcul. Sélectionnez l\'objet **CalculiX** dans l\'arborescence et appuyez sur le bouton **<img src="images/FEM_SolverControl.svg" width=16px> [Lancement des calculs](FEM_SolverControl/fr.md)**.
-   Dans le panneau de tâches qui s\'ouvrira, cliquez d\'abord sur le bouton **Write .inp file** pour créer le fichier d\'entrée pour CalculiX, puis le bouton **Run CalculiX**. Quelques instants après, le calcul sera effectué    *

   *   <img alt="" src=images/Exercise_fem_09.jpg  style="width   *600px;">

-   Nous pouvons maintenant regarder les résultats. Fermez le panneau des tâches et voyez qu\'un nouvel objet **Résultats** a été ajouté à notre analyse.
-   Double-cliquez sur l\'objet **Résultats**.
-   Définissez le type de résultat que vous souhaitez voir sur le maillage, par exemple \"déplacement absolu\", cochez la case à cocher **affichage** sous **Déplacement** et déplacez le curseur à côté de celui-ci. Vous pourrez voir la déformation augmenter lorsque vous appliquez plus de force    *

   *   <img alt="" src=images/Exercise_fem_10.jpg  style="width   *600px;">

Les résultats affichés par l\'atelier FEM ne sont évidemment pas suffisantes pour prendre des décisions dans la vie réelle sur le dimensionnement des structures et les matériaux. Ils peuvent par contre donner déjà des informations intéressantes sur la façon dont les forces s\'appliquent sur une structure et quelles sont les zones faibles qui seront le plus stressées.

**Téléchargements**

-   Le fichier créé lors de cet exercice   * <https   *//github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/fem.FCStd>

**Lire plus d\'informations**

-   [L\'atelier FEM](FEM_Workbench/fr.md)
-   [Installation des composants requis pour l\'atelier FEM](FEM_Install/fr.md)
-   [CalculiX](http   *//www.calculix.de)
-   [NetGen](https   *//sourceforge.net/projects/netgen-mesher)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Creating FEM analyses/fr
