# Manual:BIM modeling/fr
}





{{Manual:TOC/fr}}

BIM signifie [Building Information Modeling](https://en.wikipedia.org/wiki/Building_information_modeling). La définition exacte du contenu varie, mais nous pouvons simplement dire que c\'est comme cela que les bâtiments et autres grandes structures comme les ponts, les tunnels, etc. sont modélisés aujourd\'hui. Les modèles BIM sont généralement basés sur des modèles 3D et incluent également une série de couches d\'informations supplémentaires, telles que des informations sur les matériaux, des relations avec d\'autres objets ou modèles ou des instructions spéciales pour la construction ou la maintenance. Ces informations supplémentaires permettent toutes sortes d\'analyses avancées du modèle, telles que la résistance structurelle, les estimations de coût et de temps de construction, ou les calculs de consommation d\'énergie.

L\'[atelier Arch](Arch_Workbench/fr.md) de FreeCAD met en œuvre une série d\'outils et d\'installations pour la modélisation BIM. Bien qu\'il ait un but différent, il est conçu pour fonctionner dans une intégration étroite avec le reste de FreeCAD : Tout ce qui est fait avec n\'importe quel autre atelier de FreeCAD peut devenir un objet Arch ou être utilisé comme base pour un objet Arch.

Comme dans l'[atelier PartDesign](PartDesign_Workbench/fr.md), les objets produits par l'atelier Arch sont destinés à être construits dans le monde réel. Par conséquent, ils doivent être des **solides**. Les outils de l'atelier Arch s\'occupent généralement de cela automatiquement, et fournissent également des outils utiles pour vous aider à vérifier la validité des objets.

L\'atelier Arch comprend également tous les outils de l'[atelier Draft](Draft_Workbench/fr.md) et utilise son réseau et son système d\'accrochage. Avant de commencer, il est toujours recommandé de parcourir les pages de préférences de Draft et Arch et de configurer les paramètres par défaut à votre convenance.

Dans ce chapitre, nous verrons comment modéliser ce petit bâtiment :

![](images/Exercise_arch_01.jpg )

et produire un plan et une vue en coupe de celui-ci :

![](images/Exercise_arch_02.jpg )

-   Créez un nouveau document et passez à l'[atelier Arch](Arch_Workbench/fr.md).
-   Depuis le menu **Edition → Préférences → Draft → Grille et aimantation** et réglez:
    -   **Lignes principales toutes les** `10`.
    -   **Espacement de la grille** `1000mm` pour avoir une grille d\'un mètre, ce qui convient à la taille de notre bâtiment.
    -   **Taille de la grille** `100 lignes`.
-   Sur la barre d\'outils **Aimantation**, assurez-vous que le bouton <img alt="" src=images/Draft_Snap_Grid.svg  style="width:16px;"> [Aimantation Grille](Draft_Snap_Grid/fr.md) soit activé, afin que nous puissions utiliser la grille autant que possible.
-   Si vous ne voyez pas les axes, cliquez sur le bouton <img alt="" src=images/Draft_Snap_Grid.svg  style="width:16px;"> [Aimantation grille](Draft_Snap_Grid/fr.md).
-   Réglez le [Plan de travail](Draft_SelectPlane/fr.md) sur le plan **XY**
-   Faites un zoom arrière et un panoramique pour voir la zone de (0,0) à (4,3). Voir [Navigation par la souris](Mouse_navigation/fr.md) pour obtenir des instructions.
-   Dessinez quatre lignes avec l\'outil <img alt="" src=images/Draft_Line.svg  style="width:16px;"> [Draft Ligne](Draft_Line/fr.md). Vous pouvez entrer les coordonnées manuellement ou simplement sélectionner les points sur la grille avec la souris :
    -   Du point (0,0) au point (0,3)
    -   Du point (0,3) au point (4,3)
    -   Du point (4,3) au point (4,0)
    -   Du point (4,0) au point (0,0)

REMARQUE: en raison d\'un bogue dans la version 0.18, assurez-vous de faire les lignes dans cet ordre et dans cette direction.

![](images/Exercise_arch_03.jpg )

Notez que nous avons toujours dessiné dans la même direction (dans le sens des aiguilles d\'une montre). Cela n\'est pas nécessaire, mais veillera à ce que les murs que nous construirons à la suite aient tous les mêmes directions gauche et droite. Vous pourriez également penser que nous aurions simplement pu tracer un rectangle ici, ce qui est vrai. Mais les quatre lignes nous permettront d\'illustrer mieux comment ajouter un objet à un autre.

-   Une fois que vous avez créé les lignes, vérifiez leurs points de départ et d\'arrivée et ajustez-les si nécessaire pour les obtenir exactement.

![](images/Manual-BIM_Modeling_-_Adjusting_Lines.png )

-   Sélectionnez la première ligne, puis appuyez sur le bouton <img alt="" src=images/Arch_Wall.svg  style="width:16px;"> [Arch Mur](Arch_Wall/fr.md).
-   Répétez ceci pour les 3 autres lignes, jusqu\'à ce que vous ayez 4 murs.
-   Sélectionnez les quatre murs et définissez leur propriété **Hauteur** à **3.00m** et leur propriété **Alignement** à **gauche**. Si vous n\'avez pas dessiné les lignes dans le même ordre que nous l\'avons fait plus haut, certains des murs pourraient avoir leurs directions gauche et droite inversées et il faudra peut-être régler **Alignement** à **droite**. Vous obtiendrez quatre murs croisés, à l\'intérieur des lignes de base :

![](images/Exercise_arch_04.jpg )

Maintenant, nous devons joindre ces murs, de sorte qu\'ils se croisent correctement. Ceci n\'est pas nécessaire lorsque vos murs sont dessinés de manière qu\'ils se connectent déjà proprement, mais ici nous devons, car ils se croisent. Dans Arch, cela se fait en élisant l\'un des murs pour être le \"hôte\", et en ajoutant les autres, en tant que \"ajouts\". Tous les objets d\'Arch peuvent avoir n\'importe quel nombre d\'ajouts (objets dont la géométrie sera ajoutée à la géométrie de l\'hôte), et de soustractions (objets dont la géométrie sera soustraite). Les ajouts et soustractions d\'un objet peuvent être modifiés à tout moment en double-cliquant sur l\'objet dans l\'arborescence.

-   Sélectionnez les quatre murs en appuyant sur la touche **Ctrl**, le dernier étant le mur que vous avez choisi de devenir l\'hôte.
-   Appuyez sur le bouton <img alt="" src=images/Arch_Add.svg  style="width:16px;"> [Arch Ajouter](Arch_Add/fr.md). Les quatre murs ont maintenant été transformés en un seul :

![](images/Exercise_arch_05.jpg )

Les parois individuelles sont cependant toujours accessibles, en développant l\'objet mur dans l\'arborescence (petite flèche).

-   Plaçons maintenant une porte. Dans FreeCAD, les portes sont considérées comme un cas particulier des fenêtres, ce qui se fait à l\'aide de l\'outil [Fenêtre](Arch_Window/fr.md).
-   Commencez par sélectionner le mur. Ceci n\'est pas indispensable, mais une bonne habitude à prendre. Si un objet est sélectionné lors du démarrage de l\'outil Fenêtre, vous forcerez la fenêtre à s'insérer dans cet objet même si vous vous placez sur un autre objet.
-   Réglez le [Draft Plan de travail](Draft_SelectPlane/fr.md) sur **auto** donc nous ne sommes pas restreints au plan de masse.
-   Appuyez sur le bouton <img alt="" src=images/Arch_Window.svg  style="width:16px;"> [Arch Fenêtre](Arch_Window/fr.md).
-   Dans le panneau de création de la fenêtre, sélectionnez le modèle **Porte vitrée** et définissez sa **largeur** à 0,9 m et sa **hauteur** à 2,1 m.
-   Assurez-vous que l\'option Aimantation au point <img alt="" src=images/Draft_Snap_Near.svg  style="width:16px;"> [le plus proche](Draft_Snap_Near/fr.md) est activée afin que nous puissions aimanter les objets aux faces.
-   Placez votre fenêtre à peu près au milieu de la face avant du mur :

![](images/Exercise_arch_06.jpg )

Après avoir cliqué, notre fenêtre est placée sur la bonne face, mais pas exactement où nous voulons :

![](images/Exercise_arch_07.jpg )

-   Nous pouvons maintenant définir l\'emplacement précis en développant le mur et les objets de la fenêtre dans l\'arborescence et en changeant la propriété de **Placement** de l\'esquisse de base de notre porte. Réglez sa position sur **x = 2m, y = 0, z = 0**. Notre fenêtre est maintenant exactement là où nous le voulons :

![](images/Exercise_arch_08.jpg )

-   Répétez l\'opération pour placer une fenêtre: sélectionnez le mur, appuyez sur l\'outil Fenêtre, sélectionnez le préréglage **Ouverture à 2 vantaux** (Open 2-pane) et placez une fenêtre de 1 m x 1 m dans la même face que la porte. Réglez le placement de l\'esquisse sous-jacente à la position **x = 0,6m, y = 0, z = 1,1 m**, de sorte que la ligne supérieure de la fenêtre soit alignée sur le haut de la porte.

![](images/Exercise_arch_09.jpg )

Les fenêtres sont toujours construites sur des esquisses. Il est facile de créer des fenêtres personnalisées en créant d\'abord une esquisse sur une face, puis en la transformant en une fenêtre en la sélectionnant, puis en appuyant sur le bouton Fenêtre. Ensuite, les paramètres de création de la fenêtre, c\'est-à-dire les lignes de l\'esquisse, doivent être extrudés et de plus peuvent être redéfinis en double-cliquant sur la fenêtre dans l\'arborescence. Maintenant, créons une dalle :

-   Réglez le [Draft Plan de travail](Draft_SelectPlane/fr.md) sur le plan **XY**.
-   Créez un <img alt="" src=images/Draft_Rectangle.svg  style="width:16px;"> [Draft Rectangle](Draft_Rectangle/fr.md) avec une **longueur** de 5m, une **hauteur** de 4m et placez-le à la position **x: -0.5m, y: -0.5m, z: 0**.
-   Sélectionnez le rectangle.
-   Cliquez sur l\'outil <img alt="" src=images/Arch_Structure.svg  style="width:16px;"> [Arch Structure](Arch_Structure/fr.md) pour créer une dalle à partir du rectangle.
-   Réglez la propriété de **hauteur** de la dalle à 0,2 m et sa direction **normale** à (0,0,-1) car nous voulons qu\'elle soit extrudée vers le bas. Nous pourrions aussi simplement l\'avoir déplacée de 0,2 m vers le bas, mais il est toujours recommandé de conserver les objets extrudés au même endroit que leur profil de base.
-   Définissez la propriété **Ifc Type** de la dalle sur **slab** (dalle). Ceci n\'est pas nécessaire dans FreeCAD, mais il est important pour l\'exportation IFC car il garantira que l\'objet est exporté avec le type IFC correct.

![](images/Exercise_arch_10.jpg )

-   Utilisons maintenant l\'une des présélections structurelles pour créer une poutre métallique. Cliquez sur le bouton <img alt="" src=images/Arch_Structure.svg  style="width:16px;"> [Arch Structure](Arch_Structure/fr.md), sélectionnez un préréglage **HEB 180** et définissez sa hauteur à **4m**. Placez-le n\'importe où:

![](images/Exercise_arch_11.jpg )

Réglez son **placement** en ajustant son **angle** à 90 ° dans l\'axe (1,0,0), et sa **position** sur x: 90 mm, y: 3,5 m, z: 3,09 m. Cela positionnera la poutre exactement sur l\'une des parois latérales :

![](images/Exercise_arch_12.jpg )

-   Nous devons maintenant dupliquer cette poutre plusieurs fois. Nous pourrions le faire en utilisant l\'outil <img alt="" src=images/Draft_Clone.svg  style="width:16px;"> [Draft Cloner](Draft_Clone/fr.md) mais il y a une meilleure façon de faire toutes les copies à la fois en utilisant une copie en réseau :
-   Sélectionnez la poutre.
-   Appuyez sur le bouton <img alt="" src=images/Draft_OrthoArray.svg  style="width:16px;"> [Draft Réseau](Draft_OrthoArray/fr.md).
-   Définissez le **Nombre d\'éléments** pour la direction X du réseau à 6, définissez le nombre pour les directions Y et Z à 1, et appuyez sur **OK**.
-   Développez la propriété du réseau **interval X** et appuyez sur la petite icône **expression** (<img alt="" src=images/Bound-expression-unset.png  style="width:16px;">) située sur le côté droit du champ X. Cela ouvrira un [éditeur d\'expressions](Expressions/fr.md) :

![](images/Exercise_arch_13.jpg )

-   Écrivez **(4m-180mm)/5** dans le champ d\'expression, et appuyez sur **OK**. Cela définira la valeur x à 0.764 (4m est la longueur totale de notre paroi avant, 180mm est la largeur de la poutre, c\'est pourquoi elle s\'appelle HEB180, et nous voulons un cinquième de cet espace comme intervalle entre chaque poutre) :

![](images/Exercise_arch_14.jpg )

-   Nous pouvons maintenant construire facilement une dalle simple sur le dessus, en dessinant un rectangle directement sur le plan supérieur des poutres. Sélectionnez une face supérieure d\'une des poutres.
-   Appuyez sur le bouton <img alt="" src=images/Draft_SelectPlane.svg  style="width:16px;"> [Draft Plan de travail](Draft_SelectPlane/fr.md). Le plan de travail est maintenant réglé sur cette face.
-   Créez un <img alt="" src=images/Draft_Rectangle.svg  style="width:16px;"> [Draft Rectangle](Draft_Rectangle/fr.md) en l'accrochant sur deux points opposés des poutres frontières :

![](images/Exercise_arch_15.jpg )

-   Sélectionnez le rectangle.
-   Cliquez sur le bouton <img alt="" src=images/Arch_Structure.svg  style="width:16px;"> [Arch Structure](Arch_Structure/fr.md) et créez une dalle avec une hauteur de **0,2 m**.

Voilà, notre modèle est maintenant terminé. Nous devrions maintenant l\'organiser afin qu\'il s'exporte correctement vers IFC. Le format IFC exige que tous les objets d\'un bâtiment se trouvent à l\'intérieur d\'un objet de construction, et éventuellement dans un historique. Il exige également que tous les bâtiments soient placés sur un site, mais l\'exportateur IFC de FreeCAD ajoutera automatiquement un site par défaut si nécessaire, donc nous n\'avons pas besoin d\'en ajouter un ici.

-   Sélectionnez les deux dalles, le mur et le réseau de poutres.
-   Appuyez sur le bouton <img alt="" src=images/Arch_Floor.svg  style="width:16px;"> [Arch Niveaux](Arch_Floor/fr.md).
-   Sélectionnez le niveau que nous venons de créer.
-   Appuyez sur le bouton <img alt="" src=images/Arch_Building.svg  style="width:16px;"> [Arch Bâtiment](Arch_Building/fr.md).

Notre modèle est maintenant prêt à exporter :

![](images/Exercise_arch_16.jpg )

Le [format IFC](https://en.wikipedia.org/wiki/Industry_Foundation_Classes) est l\'un des atouts les plus précieux dans un monde BIM gratuit, car il permet l\'échange de données entre toute application et acteur du monde de la construction, de manière ouverte (le format est ouvert, gratuit et maintenu par un consortium indépendant). L\'exportation de vos modèles BIM comme IFC garantit que tout le monde peut les voir et les analyser, peu importe l\'application utilisée.

Dans FreeCAD, l\'importation et l\'exportation IFC se font en interconnectant un autre logiciel, appelé [IfcOpenShell](http://ifcopenshell.org/). Pour pouvoir exporter vers IFC depuis FreeCAD, le paquet [IfcOpenShell-Python](http://ifcopenshell.org/python) doit être installé sur votre système. Assurez-vous de sélectionner celui qui utilise la même version Python que FreeCAD. La version Python utilisée par FreeCAD est donnée lors de l\'ouverture du panneau **Vue -\> Panneaux -\> console Python** dans FreeCAD. Lorsque cela est fait, nous pouvons alors exporter notre modèle :

-   Sélectionnez l\'objet de niveau supérieur que vous souhaitez exporter, c\'est-à-dire l\'objet Bâtiment.
-   Sélectionnez le menu **Fichier -\> Exporter -\> Industry Foundation Classes** et enregistrez votre fichier.
-   Le fichier IFC résultant peut maintenant être ouvert dans un large éventail d\'applications et de visionneuses (l\'image ci-dessous montre le fichier ouvert dans la visionneuse gratuite [IfcPlusPlus](http://www.ifcquery.com/)). Il est important de vérifier le fichier exporté dans une telle application de visualisation avant de le distribuer à d\'autres personnes afin de vérifier que toutes les données contenues dans le fichier sont correctes. FreeCAD lui-même peut également être utilisé pour rouvrir le fichier IFC résultant.

![](images/Exercise_arch_17.jpg )

Nous allons maintenant placer quelques dimensions. Contrairement au [ chapitre précédent](Manual:Generating_2D_drawings/fr.md), où nous avons dessiné toutes les dimensions directement sur la feuille de Dessin, nous allons utiliser une autre méthode ici, et placer [des dimensions Draft](Draft_Dimension/fr.md) directement dans le modèle 3D. Ces dimensions seront ensuite automatiquement placées sur la feuille de dessin. Nous allons d\'abord faire deux groupes pour nos dimensions, un pour les dimensions qui apparaîtront dans la vue en plan (coupe horizontale dans le langage du bâtiment), et un autre pour celles qui apparaissent sur l\'élévation (vue de face dans le langage du bâtiment).

-   Cliquez avec le bouton droit de la souris sur le document «maison» dans l\'arborescence et créez deux nouveaux groupes : **Dimensions du plan** et **Dimensions de l\'élévation**.
-   Réglez le [Draft Plan de travail](Draft_SelectPlane/fr.md) sur le plan **XY**.
-   Assurez-vous que l'option <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:16px;"> [Accrochage restreint](Draft_Snap_WorkingPlane/fr.md) est activée, de sorte que tout ce que vous dessinez reste sur le plan de travail.
-   Dessinez quelques <img alt="" src=images/Draft_Snap_Dimensions.svg  style="width:16px;"> [Dimensions](Draft_Snap_Dimensions/fr.md), par exemple comme sur l\'image ci-dessous. En appuyant sur **Shift** et **Ctrl** tout en cliquant sur les points de cote, vous obtiendrez des options supplémentaires.

![](images/Exercise_arch_18.jpg )

-   Sélectionnez toutes vos cotes et faites-les glisser vers le groupe **Dimensions du Plan** dans l\'arborescence.
-   Réglez le [plan de travail](Draft_SelectPlane/fr.md) sur le plan **XZ**, c\'est-à-dire le plan vertical frontal.
-   Répétez l\'opération, dessinez quelques cotes et placez-les dans le groupe **Dimensions d\'élévation**.

![](images/Exercise_arch_19.jpg )

Nous allons maintenant préparer un ensemble de vues à partir de notre modèle, à placer sur une page de dessin. Nous pouvons le faire avec les outils de l\'atelier Drawing, comme nous l\'avons vu dans le chapitre précédent, mais l\'atelier Arch offre également un outil avancé tout-en-un pour produire des vues de plan, de section et d\'élévation appelées [Arch Plan de coupe](Arch_SectionPlane/fr.md). Nous allons maintenant ajouter deux de ces plans de coupe pour créer une vue en plan et une vue en élévation.

-   Sélectionnez l\'objet Bâtiment (building) dans l\'arborescence
-   Appuyez sur le bouton <img alt="" src=images/Arch_SectionPlane.svg  style="width:16px;"> [Arch Plan de coupe](Arch_SectionPlane/fr.md) .
-   Définir sa propriété **Display Height** (hauteur d\'affichage) à 5m, sa **Display Length** (longueur d\'affichage) à 6m, donc nous englobons notre maison (ce n\'est pas nécessaire, mais ce sera mieux, car cela montrera naturellement à quoi sert cet outil), et sa position **Placement** à x: 2m, y: 1.5m, z: 1.5m.
-   Vérifiez la liste des objets pris en considération par le plan de coupe en double-cliquant dessus dans la [vue en arborescence](Tree_view/fr.md). Les plans de coupe ne restituent que les objets spécifiés du modèle, pas tous. Les objets pris en considération par le plan de coupe peuvent être modifiés ici.

![](images/Exercise_arch_20.jpg )

-   Répétez l\'opération pour créer un autre plan de coupe, donnez-lui la même longueur et hauteur d\'affichage, et donnez-lui le **Placement** suivant: position: x: 2m, y: -2m, z: 1.5m, angle: 90 °, axe: x: 1, y: 0, z: 0. Assurez-vous que ce nouveau plan de coupe considère également l\'objet Bâtiment.

![](images/Exercise_arch_21.jpg )


**Le développement de l'[atelier Drawing](Drawing_Workbench/fr.md) s'est arrêté dans FreeCAD 0.16, et le nouvel [atelier TechDraw](TechDraw_Workbench/fr.md) visant à le remplacer a été introduit en v0.17. Le plan de travail de dessin peut être supprimé dans les versions ultérieures. Utilisez plutôt le Workbench TechDraw.**

-   Maintenant, nous avons tout ce dont nous avons besoin, et nous pouvons créer notre feuille de dessin. Commencez par passer à l' [atelier Drawing](Drawing_Workbench/fr.md) et créez une nouvelle page par défaut <img alt="" src=images/Drawing_Landscape_A3.png  style="width:16px;"> [page de dessin A3 Paysage](Drawing_Landscape_A3/fr.md) (ou sélectionnez un autre modèle si vous le souhaitez).
-   Sélectionnez le premier plan de coupe, utilisé pour la vue en plan.
-   Appuyez sur le bouton <img alt="" src=images/Drawing_DraftView.png  style="width:16px;"> [Draft Dessin](Draft_Drawing/fr.md). Cet outil offre quelques fonctionnalités supplémentaires par rapport à l\'outil de conception de dessin standard [Drawing Insérer une vue](Drawing_View/fr.md) et prend en charge les plans de coupe de l\'atelier Arch.
-   Donnez à la nouvelle vue les propriétés suivantes :
    -   X: 50
    -   Y: 140
    -   Échelle: 0,03
    -   Largeur de ligne: 0.15
    -   Montrer la coupe: vrai
    -   Afficher le remplissage: vrai
-   Sélectionnez l\'autre plan de coupe et créez une nouvelle vue, avec les propriétés suivantes :
    -   X: 250
    -   Y: 150
    -   Échelle: 0,03
    -   Rendu: solide

![](images/Exercise_arch_22.jpg )

Nous allons maintenant créer deux nouvelles vues, une pour chaque groupe de dimensions.

-   Sélectionnez le groupe Dimensions du plan.
-   Appuyez sur le bouton Créer une <img alt="" src=images/Drawing_DraftView.png  style="width:16px;"> [Draft vue](Draft_Drawing/fr.md).
-   Donnez à la nouvelle vue les propriétés suivantes :
    -   X: 50
    -   Y: 140
    -   Échelle: 0,03
    -   Largeur de ligne: 0.15
    -   Taille de la police: 10mm
-   Répétez l\'opération pour l\'autre groupe, avec les paramètres suivants :
    -   X: 250
    -   Y: 150
    -   Échelle: 0,03
    -   Largeur de ligne: 0.15
    -   Taille de la police: 10mm
    -   Direction: 0, -1,0
    -   Rotation: 90 °

Notre page est maintenant prête, et nous pouvons l\'exporter vers les formats SVG ou DXF, ou l\'imprimer. Le format SVG vous permet d\'ouvrir le fichier en utilisant des applications d\'illustration telles que [Inkscape](http://www.inkscape.org), avec lesquelles vous pouvez rapidement améliorer les dessins techniques et les transformer en dessins de présentation beaucoup plus agréable. Il offre beaucoup plus de possibilités que le format DXF.



## Téléchargements

-   Le fichier produit lors de cet exercice: <https://github.com/yorikvanhavre/FreeCADmanual/Blob/master/files/house.FCStd>
-   Le fichier IFC exporté à partir du fichier ci-dessus: <https://github.com/yorikvanhavre/FreeCADmanual/Blob/master/files/house.ifc>
-   Le fichier SVG exporté à partir du fichier ci-dessus: <https://github.com/yorikvanhavre/FreeCADmanual/Blob/master/files/house.svg>



## En relation 

-   [Atelier BIM](BIM_Workbench.md)
-   [Atelier Arch](Arch_Workbench/fr.md)
-   [Draft Plan de travail](Draft_SelectPlane/fr.md)
-   [Draft Paramètres d\'accrochage](Draft_Snap/fr.md)
-   [Expressions](Expressions/fr.md)
-   [Le format IFC](https://fr.wikipedia.org/wiki/Industry_Foundation_Classes)
-   [IfcOpenShell](http://ifcopenshell.org/)
-   [IfcPlusPlus](http://ifcplusplus.com/)
-   [Inkscape](http://www.inkscape.org)



---
![](images/Button_right.svg) [documentation index](../README.md) > [BIM](Category_BIM.md) > [Arch](Category_Arch.md) > Manual:BIM modeling/fr
