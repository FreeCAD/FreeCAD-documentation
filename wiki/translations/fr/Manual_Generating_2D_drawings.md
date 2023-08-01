# Manual:Generating 2D drawings/fr
{{Manual:TOC/fr}}

Lorsque votre modèle ne peut pas être imprimé ou fraisé directement par une machine, par exemple s\'il est trop grand (un bâtiment) ou qu\'il nécessite un assemblage manuel une fois les pièces prêtes, vous devrez généralement expliquer à une autre personne comment le faire. Dans les domaines techniques (ingénierie, architecture, etc.), cela se fait généralement avec des dessins. Les dessins sont remis à la personne responsable de l\'assemblage du produit final et vous expliquent comment procéder.

Les exemples typiques sont les instructions Ikea, les dessins d\'architecture ([Dessins d\'architecture](https://fr.wikipedia.org/wiki/Dessin_d%27architecture)) et les plans ([blueprints](https://fr.wikipedia.org/wiki/Blueprint)). Ces dessins contiennent généralement non seulement le dessin lui-même, mais aussi de nombreuses annotations, telles que les textes, dimensions, chiffres, symboles qui aideront les autres à comprendre ce qui doit être fait et comment.

Dans FreeCAD, l\'atelier chargé de faire de tels dessins est l'<img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [Atelier TechDraw](TechDraw_Workbench/fr.md).

L'atelier TechDraw vous permet de créer des feuilles, qui peuvent être vides ou utiliser un [TechDraw Modèle](TechDraw_Templates/fr.md) pour avoir déjà une série d\'éléments sur la feuille, comme des bordures et un titre. Sur ces feuilles, vous pouvez ensuite placer des vues des objets 3D que vous avez modélisés précédemment et configurer la façon dont ces vues apparaîtront sur la feuille. Vous pouvez également placer toutes sortes d\'annotations sur la feuille, telles que les dimensions, les textes et autres symboles couramment utilisés dans les dessins techniques.

Les feuilles de dessin, une fois complétées, peuvent être imprimées ou exportées sous forme de fichiers [SVG](https://fr.wikipedia.org/wiki/Scalable_Vector_Graphics), PDF ou [DXF](https://fr.wikipedia.org/wiki/Drawing_eXchange_Format).

Dans l\'exercice suivant, nous verrons comment créer un dessin simple d\'un modèle de chaise trouvé dans la [bibliothèque FreeCAD](https://github.com/FreeCAD/FreeCAD-library) (Industrial Design → Chairs → IkeaLikeChair). La bibliothèque FreeCAD peut facilement être ajoutée à votre installation FreeCAD (reportez-vous au chapitre de ce [Manuel : Installation](Manual:Installing/fr.md)), ou vous pouvez télécharger simplement le modèle à partir de la page Web de la bibliothèque ou via le lien direct fourni au bas de ce chapitre.

![](images/Exercise_TechDraw_01.svg )

-   Chargez le fichier IkeaLikeChair à partir de la bibliothèque. Vous pouvez choisir entre la version .[FCStd](File_Format_FCStd/fr.md), qui chargera l\'historique de la modélisation complète, ou la version .[step](STEP/fr.md), qui ne créera qu\'un seul Objet, sans l\'historique. Comme nous n\'aurons plus besoin de modéliser maintenant, il est préférable de choisir la version .step, car le fichier sera plus facile à manipuler.

![](images/Parts_library.jpg )

-   Passer à l'<img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [atelier TechDraw](TechDraw_Workbench/fr.md)
-   Appuyez sur le bouton <img alt="" src=images/TechDraw_PageTemplate.svg  style="width:16px;"> [TechDraw Page à partir d\'un modèle](TechDraw_PageTemplate/fr.md).
-   Sélectionnez le modèle **A4_Portrait_ISO7200TD**. Un nouvel onglet s\'ouvrira dans votre fenêtre FreeCAD montrant la nouvelle page.
-   Dans la [vue en arborescence](tree_view/fr.md) (ou dans l\'onglet modèle), sélectionnez le modèle de chaise. Il sera très probablement nommé quelque chose comme \"Open CASCADE STEP translator.\"
-   Appuyez sur le bouton <img alt="" src=images/TechDraw_View.svg  style="width:16px;"> [TechDraw Vue](TechDraw_View/fr.md).
-   Un objet Vue sera créé sur notre page. Sélectionnez l\'objet Vue dans l\'arborescence puis donnez à la vue les [propriétés](TechDraw_View/fr#Vue.md) dans l\'onglet de données de la vue combinée:
    -   Sous la catégorie Base:
        -   X: 70 mm
        -   Y: 120 mm
        -   Rotation: 0
        -   Échelle: 0,1
    -   Sous la catégorie Projection (appuyez sur la flèche déroulante pour modifier individuellement les composants x, y et z de ces propriétés):
        -   Direction: \[0 0 1\]
        -   XDirection: \[0 -1 0\] (changez d\'abord le champ y, puis le champ x)
-   Nous avons maintenant une belle vue de dessus de notre chaise. Appuyez sur le bouton <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width:16px;"> [TechDraw Bascule des cadres](TechDraw_ToggleFrame/fr.md) pour désactiver les cadres, étiquettes et sommets de vue.

![](images/Exercise_drawing_02.jpg )

-   Répétez l\'opération deux fois pour créer deux autres vues. Nous allons définir leurs valeurs X et Y, qui indiquent la position de la vue sur la page, afin de les distinguer de la vue de dessus, et leur orientation, pour créer différentes orientations de vue. Donnez à chaque nouvelle vue les propriétés suivantes :
    -   View001 (vue de face) : X: 70, Y: 220, Scale: 0.1, Rotation: 0, Direction: (-1,0,0), XDirection: (0,-1,0)
    -   View002 (vue latérale) : X: 150, Y: 220, Scale: 0.1, Rotation: 0, Direction: (0,-1,0), XDirection: (1,0,0)
-   Nous obtenons alors la page suivante :

![](images/Exercise_TechDraw_04.png )

-   Notez qu\'il peut y avoir des moyens plus faciles d\'obtenir les vues que vous souhaitez. Vous pouvez simplement [faire pivoter](Manual:Navigating_in_the_3D_view/fr.md) la vue 3D de votre modèle, et une fois que vous avez la vue souhaitée, sélectionnez le modèle dans l\'arborescence et appuyez sur <img alt="" src=images/TechDraw_View.svg  style="width:16px;"> Nouvelle Vue. Cela insérera automatiquement une vue avec les propriétés de rotation et de direction souhaitées. Vous pouvez également utiliser l\'outil <img alt="" src=images/TechDraw_ProjectionGroup.svg  style="width:16px;"> [TechDraw Groupe de projection](TechDraw_ProjectionGroup/fr.md).

-   Nous pouvons modifier l\'aspect de nos vues si nous le voulons, par exemple, nous pouvons changer leur propriété **Line Width** (Largeur de ligne) (sous l\'onglet Vue dans la vue combinée) à 0,5.

Nous allons maintenant placer des dimensions et des indications sur notre dessin. Il existe deux façons d\'ajouter des cotes à un modèle: l\'une consiste à placer les cotes à l\'intérieur du modèle 3D, à l\'aide de l\'outil <img alt="" src=images/Draft_Dimension.svg  style="width:16px;"> [Draft Dimension](Draft_Dimension/fr.md) de l\'[atelier Draft](Draft_Workbench/fr.md) puis en plaçant une vue de ces dimensions sur notre feuille avec l\'outil <img alt="" src=images/TechDraw_DraftView.svg  style="width:16px;"> [TechDraw Vue Draft](TechDraw_DraftView/fr.md). L\'autre consiste à faire les choses directement sur la feuille TechDraw. Nous utiliserons cette dernière méthode.

-   Appuyez sur le bouton <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width:16px;"> pour activer les sommets.
-   Utilisez Ctrl + Clic gauche de la souris pour sélectionner les deux sommets entre lesquels vous souhaitez mesurer la distance.
-   Appuyez sur le bouton <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:16px;"> [TechDraw Cote de longueur](TechDraw_LengthDimension/fr.md).

![](images/Exercise_TechDraw_05.png )

-   Répétez l\'opération jusqu\'à ce que toutes les dimensions que vous souhaitez indiquer soient placées. Utilisez les outils <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width:16px;"> [TechDraw Cote verticale](TechDraw_VerticalDimension/fr.md) et <img alt="" src=images/TechDraw_HorizontalDimension.svg  style="width:16px;"> [TechDraw Cote horizontale](TechDraw_HorizontalDimension/fr.md) le cas échéant.
-   Prenez une minute pour regarder les [propriétés](TechDraw_LengthDimension/fr#Propri.C3.A9t.C3.A9s.md) de l\'objet Dimension dans la vue combinée.
-   Veuillez noter que si vous dimensionnez une vue [axonométrique](https://en.wikipedia.org/wiki/Axonometric_projection) (par exemple, une vue isométrique) au lieu d\'une vue [multiview](https://en.wikipedia.org/wiki/Multiview_projection) (par exemple, vue de face) comme nous l\'avons fait ici, vous devrez utiliser l\'outil <img alt="" src=images/TechDraw_LinkDimension.svg  style="width:16px;"> [TechDraw Lier une dimension](TechDraw_LinkDimension/fr.md) pour obtenir une dimension précise.

![](images/Exercise_TechDraw_07.png )

-   Nous allons maintenant placer les deux légendes illustrées dans l\'image ci-dessus en utilisant l\'outil <img alt="" src=images/TechDraw_Balloon.svg  style="width:16px;"> [TechDraw Bulles](TechDraw_Balloon/fr.md).

![](images/Exercise_TechDraw_06.png )

1.  En regardant la page dans la [Vue 3D](3D_view/fr.md), sélectionnez la vue à laquelle le ballon sera attaché comme indiqué dans l\'image ci-dessus.
2.  Appuyez sur le bouton <img alt="" src=images/TechDraw_Balloon.svg  style="width:16px;"> Bulle.
3.  Le curseur est maintenant affiché sous forme d\'icône de bulle. Cliquez sur la page pour placer l\'origine de la bulle à la position souhaitée.
4.  La bulle peut être déplacée vers la position souhaitée.
5.  Modifiez les propriétés de la bulle en double-cliquant sur l\'étiquette de la bulle ou sur l\'objet de la bulle dans la [Vue en arborescence](Tree_view/fr.md). Cela ouvrira la boîte de dialogue de la bulle. Définissez le champ Valeur sur le texte souhaité et modifiez la sélection du menu déroulant Symbole sur **None** (aucun).
6.  Appuyez sur **OK**.
7.  Répétez l\'opération pour la deuxième légende.

-   Nous allons maintenant remplir le bloc de titre de la feuille.
    -   Assurez-vous que les cadres de vue, les étiquettes et les sommets sont visibles. Sinon, appuyez sur le bouton <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width:16px;"> Bascule.
    -   Modifiez le texte dans chaque section du bloc de titre de la feuille en cliquant sur le petit carré vert à gauche du texte.

Notre page peut maintenant être exportée au format SVG pour être plus développée dans des applications graphiques comme [Inkscape](http://www.inkscape.org) ou au format DXF. Sélectionnez la page dans la [vue en arborescence](Tree_view/fr.md) puis sélectionnez le menu **Fichier → Exporter**. Le format DXF est importable dans presque toutes les applications de CAO 2D existantes. Les pages TechDraw peuvent également être directement imprimées ou exportées au format PDF.

**Téléchargements**

-   Le fichier créé lors de cet exercice: [drawing.FCStd](https://github.com/JoshuaCall/FreeCAD-manual/blob/master/files/drawing.FCStd)
-   La feuille SVG produite à partir de ce fichier: [drawing.svg](https://github.com/JoshuaCall/FreeCAD-manual/blob/master/files/drawing.svg)

**Lire plus d\'informations**

-   [Atelier TechDraw](TechDraw_Workbench/fr.md)
-   [TechDraw Comment créer un modèle](TechDraw_TemplateHowTo/fr.md)
-   [Tutoriel d\'introduction à TechDraw](Basic_TechDraw_Tutorial/fr.md)
-   [La bibliothèque FreeCAD](https://github.com/FreeCAD/FreeCAD-library)
-   [Inkscape](http://www.inkscape.org)

**Regarder les tutoriels**

-   [la playlist TechDraw de Sliptonic](https://www.youtube.com/watch?v=7LbOmSGW9F0&list=PLEuOia-QxyFKQnmM1U9yVo7eNrK_Mcln8)
-   [Symboles et vues](https://www.youtube.com/watch?v=cggBR1Ghq7k)



---
⏵ [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Generating 2D drawings/fr
