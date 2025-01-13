# Manual:Traditional modeling, the CSG way/fr
{{Manual:TOC}}

La [géométrie de construction de solides](https://fr.wikipedia.org/wiki/G%C3%A9om%C3%A9trie_de_construction_de_solides) (CSG en anglais : *Constructive Solid Geometry*) décrit la manière fondamentale de travailler avec la géométrie solide en 3D. Elle consiste à créer des objets complexes en ajoutant ou en retirant des pièces de solides à l\'aide d\'opérations booléennes telles que l\'union, la soustraction ou l\'intersection.

Comme nous l\'avons vu plus haut dans ce manuel, FreeCAD prend en charge différents types de géométrie. Cependant, le type le plus préféré et le plus pratique pour la conception d\'objets 3D du monde réel dans FreeCAD est la géométrie solide [BREP](https://fr.wikipedia.org/wiki/B-Rep), principalement prise en charge par l'[atelier Part](Part_Workbench/fr.md). La représentation des limites est une méthode de représentation des formes à l\'aide de leurs limites spatiales. Elle définit un objet 3D en spécifiant ses surfaces, ses arêtes et ses sommets. Les aspects clés de la BREP sont les faces, qui sont les éléments de surface de l\'objet, les arêtes, les lignes de démarcation où deux faces se rencontrent, et les sommets, les points où les arêtes convergent.

La technique BREP présente plusieurs avantages. Tout d\'abord, elle définit les surfaces à l\'aide d\'équations mathématiques, ce qui permet une modélisation précise et exacte. Cette précision est cruciale pour les applications d\'ingénierie où des dimensions exactes sont requises. En outre, la technique BREP fournit des surfaces lisses et détaillées, contrairement au [maillage polygonal](https://fr.wikipedia.org/wiki/Maillage_polygonal) qui approxime les surfaces courbes avec des facettes. Ceci est similaire à la différence entre les images vectorielles, qui évoluent sans perte de qualité, et les images bitmap, qui peuvent apparaître pixellisées lorsqu\'elles sont agrandies. BREP conserve des informations topologiques complètes sur l\'objet, y compris les relations entre les faces, les arêtes et les sommets, ce qui est essentiel pour les opérations complexes telles que les calculs booléens et le filtrage.

Les maillages polygonaux sont constitués de sommets, d\'arêtes et de faces formant des triangles ou des quadrilatères. Ils sont plus simples et plus rapides pour le rendu, mais manquent de précision. Lorsqu\'elles sont agrandies ou imprimées à grande échelle, les mailles présentent des surfaces à facettes plutôt que des courbes lisses. En revanche, la BREP utilise des courbes et des surfaces définies mathématiquement, ce qui lui confère une précision et une douceur supérieures. Les modèles BREP sont préférables pour les applications de CAO où la précision n\'est pas négociable.

Dans FreeCAD, la géométrie basée sur la technique BREP est gérée par [OpenCasCade](https://fr.wikipedia.org/wiki/Open_CASCADE_Technology), une bibliothèque de logiciels à code ouvert. L\'interface principale entre FreeCAD et le noyau OpenCasCade est l\'atelier Part, qui sert de base à la plupart des autres ateliers, en fournissant des outils essentiels pour créer et manipuler des objets BREP. L\'atelier Part comprend des outils permettant de créer des primitives, telles que des formes de base comme des boîtes, des cylindres et des sphères, d\'effectuer des opérations booléennes comme la combinaison, l\'intersection et la soustraction de formes, et de réaliser des transformations, y compris le déplacement, la rotation, la mise à l\'échelle et le clonage d\'objets.

Bien que d\'autres ateliers de FreeCAD, tels que les ateliers PartDesign et Surface, offrent des outils plus avancés pour construire et manipuler la géométrie, ils s\'appuient sur l\'atelier Part sous-jacent. Il est utile de comprendre le fonctionnement interne des objets Part et de maîtriser les outils de base de Part. Souvent, ces outils plus simples permettent de résoudre des problèmes que des outils plus complexes ne peuvent pas traiter efficacement.

<img alt="" src=images/Mesh_vs_brep.jpg  style="width:600px;">

La différence entre les deux géométries peut être comparée à celle existant entre les images au format bitmap et les images vectorielles. Comme pour les images bitmap, les maillons polygonaux ont leurs surfaces courbes fractionnées en une série de points. Si vous regardez de très près ou imprimiez en très grand un objet maillé, vous n'allez pas voir une surface courbe mais une surface facettée. Dans les images vectorielles et les données BREP, la position de n\'importe quel point sur une courbe n\'est pas stockée dans la géométrie mais est calculée à la volée, générant une précision exacte.

Pour illustrer le fonctionnement de l'atelier Part, nous modéliserons cette table en utilisant uniquement des opérations CSG (à l\'exception des vis, pour lesquelles nous utiliserons l\'une des extensions, et les dimensions qui seront vues au chapitre suivant) :

<img alt="" src=images/Exercise_table_complete.jpg  style="width:600px;">

Créons un nouveau document (**Ctrl+N** ou menu **Fichier → Nouveau**) pour recevoir la conception de notre table. Le document est initialement appelé « Nouveau » dans l\'onglet Modèle du panneau Vue combinée, mais si vous enregistrez le document (**Ctrl+Shift+S** ou menu **Fichier → Enregistrer sous**) en tant que nouveau document FreeCAD appelé « table.FCStd », le document sera renommé « table », ce qui permet d\'identifier plus clairement le projet. Nous utiliserons le mm comme unité de longueur. N\'hésitez pas à changer d\'unité selon vos préférences en utilisant le menu situé dans le coin inférieur droit.

Maintenant basculez sur l\'atelier Part et commencez à créer la première patte de la table:

-   Appuyez sur le bouton <img alt="" src=images/Part_Box.svg  style="width:16px;"> 
**Cube**
-   Sélectionnez le cube obtenu, puis définissez les propriétés suivantes (onglet **Données**) :
    -   Longueur : 80 mm
    -   Largeur : 80 mm
    -   Hauteur : 750 mm
-   Dupliquez la boîte en appuyant sur **Ctrl + C** puis sur **Ctrl + V** (ou menu **Édition → Copier** et **Coller**) (à première vue il n\'y a pas de différences, les deux objets se superposant)
-   Sélectionnez le nouvel objet Cube001 en cliquant dessus à partir de l\'onglet Modèle situé à gauche
-   Changez sa position en modifiant ses propriétés de placement :
    -   Position x : 8 mm
    -   Position y : 8 mm

Vous devriez obtenir deux boîtes hautes, distante de 8 mm l\'une de l\'autre :

![](images/Exercise_table_01.jpg )

-   Maintenant, nous pouvons soustraire l\'une de l\'autre: Sélectionnez la **première**, c\'est-à-dire celle qui va **rester**, puis avec la touche CTRL enfoncée, sélectionnez **l\'autre** qui sera **soustraite** (l\'ordre est important) et appuyez sur le bouton <img alt="" src=images/Part_Cut.svg  style="width:16px;"> **Soustraction** (soustraction booléenne)  :

![](images/Exercise_table_02.jpg )

Observez que l\'objet nouvellement créé, appelé \"Cut\", contient toujours les deux cubes que nous avons utilisés comme les opérandes. En fait, les deux cubes sont toujours présents dans le document, ils ont simplement été cachés et regroupés sous l\'objet \"Cut\" dans l\'arborescence. Vous pouvez toujours les sélectionner en développant la flèche à côté de l\'objet \"Cut\" et, si vous le souhaitez, les rendre visibles à nouveau en cliquant droit sur eux ou en modifiant l\'une de leurs propriétés.

Vous pouvez également utiliser l\'outils Soustraction et d\'autres outils booléens via la \"Vue combinée\" avec <img alt="" src=images/Part_Boolean.svg  style="width:16px;"> [Part Opération booléenne](Part_Boolean/fr.md). Cela donne un moyen plus explicite mais plus long de le faire.

-   Maintenant, créez les trois autres pieds en copiant notre boîte de base 6 autres fois. Puisqu\'elle est toujours copiée, vous pouvez simplement coller (Ctrl + V) 6 fois. Modifiez leur position comme suit :
    -   Cube002: x: 0, y: 800 mm
    -   Cube003: x: 8 mm, y: 792 mm
    -   Cube004: x: 1200 mm, y: 0
    -   Cube005: x: 1192 mm, y: 8 mm
    -   Cube006: x: 120 mm, y: 800 m
    -   Cube007: x: 1192 mm, y: 792 mm

-   Faites les trois autres coupes en sélectionnant d\'abord le cube \"hôte\" puis le cube à soustraire. Nous avons maintenant quatre objets Cut:

![](images/Exercise_table_03.jpg )

Vous avez peut-être pensé qu\'au lieu de dupliquer le cube de base six fois, nous aurions pu dupliquer le pied complet trois fois. C\'est tout à fait vrai. Dans FreeCAD, il existe plusieurs façons d\'obtenir le même résultat. C\'est un point important à retenir parce que lorsque nous progresserons vers des objets plus complexes, certaines opérations pourraient ne pas donner un résultat satisfaisant. Nous devrons alors essayer d\'autres façons.

-   Nous allons maintenant faire des trous pour les vis en utilisant la même méthode de coupe. Puisque nous avons besoin de 8 trous, deux dans chaque pied, nous pourrions faire 8 objets à soustraire. Au lieu de cela, voici une autre manière: créons quatre cylindres en utilisant l\'outil <img alt="" src=images/Part_Cylinder.svg  style="width:16px;"> 
**Cylindre** (un cylindre pour deux pieds). Vous pouvez à nouveau en faire un seul et le copier ensuite. Donnez à tous les cylindres un rayon de 6 mm. Cette fois, nous devrons les faire pivoter, ce qui se fait également par la propriété **Placement** de l\'onglet Données *(**Remarque :** changez la propriété de l\'Axe*avant*de modifier la valeur de l\'angle ou la rotation ne sera pas appliqué)*
    -   Cylindre : hauteur : 1300 mm, angle : 90°, axe : x:0, y:1, z:0, position : x : -10 mm, y : 40 mm, z : 720 mm
    -   Cylinder001 : hauteur : 1300 mm, angle : 90°, axe : x:0, y:1, z:0, position : x : -10 mm, y : 840 m, z : 720 mm
    -   Cylinder002 : hauteur : 900 mm, angle : 90°, axe : x:-1, y:0, z:0, position : x : 40 mm, y : -10 mm, z : 700 m
    -   Cylinder003 : hauteur : 900 mm, angle : 90°, axe : x:-1, y:0, z:0, position : x : 1240 mm, y : -10 mm, z :700 mm

![](images/Exercise_table_04.jpg )

Vous remarquerez que les cylindres sont un peu plus longs que nécessaire. C\'est parce que comme dans toutes les applications 3D solides, les opérations booléennes dans FreeCAD sont parfois trop sensibles à des situations face-sur-face et pourraient échouer. En faisant cela, nous nous sommes placés dans une situation sûre.

-   Maintenant, faisons les soustractions. Sélectionnez le premier pied, puis, avec la touche CTRL enfoncée, sélectionnez un des cylindres qui le traversent, appuyez sur le bouton **Soustraction**. Le trou sera fait et le cylindre caché. Vous le trouverez dans l\'arborescence en développant le pied percé.
-   Sélectionnez un autre pied percé par ce cylindre caché, puis répétez l\'opération. Cette fois-ci, sélectionnez le cylindre dans l\'arborescence avec Ctrl +, puiqu\'il est caché dans la vue 3D (vous pouvez également le rendre visible pour le sélectionner dans la vue 3D). Répétez ceci pour les autres pieds jusqu\'à ce que chacun d\'eux ait ses deux trous :

![](images/Exercise_table_05.jpg )

Comme vous pouvez le voir, chaque pied est devenu une série assez longue d\'opérations. Tout cela reste paramétrique, et vous pouvez changer n\'importe quel paramètre de l\'une des anciennes opérations à tout moment. Dans FreeCAD, nous nous référons souvent à cette pile comme «historique de la modélisation» (ou parfois arbre de construction), car elle porte en fait tout l'historique des opérations que vous avez effectuées.

Une autre particularité de FreeCAD est que le concept de l\'objet 3D et le concept de l\'opération 3D ont tendance à se fondre en une même chose. La soustraction est à la fois une opération et l'objet 3D résultant de cette opération. Dans FreeCAD, cela s\'appelle une \"fonctionnalité\", plutôt que objet ou opération.

Maintenant, faisons le plateau de la table, ce sera un simple bloc de bois, faisons-le avec une autre **Boîte** :

-   Boîte : longueur : 1260 mm, largeur : 860 mm, hauteur : 80 mm, position : x : 10 mm, y : 10 mm, z : 670 mm.

Dans l\'onglet **Vue**, vous pouvez lui donner une belle couleur brunâtre, semblable à celle du bois, en changeant sa propriété **Shape Color** :

Maintenant que nos cinq pièces sont complètes, c\'est le moment pour leur donner des noms plus parlant que \"Cut015\". En cliquant avec le bouton droit sur les objets dans l\'arborescence (ou en appuyant sur **F2**), vous pouvez les renommer de façon plus significative pour vous-même ou pour une autre personne qui ouvrirait votre travail plus tard. On dit souvent que le fait de donner simplement des noms concrets à vos objets est beaucoup plus important que la façon dont vous les modélisez.

-   Nous allons maintenant placer des vis. Il existe aujourd\'hui une extension extrêmement utile développé par un membre de la communauté FreeCAD que vous trouverez dans le dépôt des extensions de FreeCad ([github FreeCAD addons](https://github.com/FreeCAD/FreeCAD-addons)) appelé [Fasteners](https://github.com/shaise/FreeCAD_FastenersWB). Il facilite l\'insertion de vis. L\'installation d'ateliers supplémentaires est simple et est décrite dans les pages du [Gestionnaire des extensions](Std_AddonMgr/fr.md).
-   Une fois que vous avez installé l'atelier Fasteners et redémarré FreeCAD, il apparait dans la liste des ateliers, et nous pouvons l'utiliser. Ajouter une vis à l\'un de nos trous est effectué en sélectionnant d\'abord l\'arête circulaire de notre trou :

<img alt="" src=images/FastenerWorkbench.png  style="width:600px;">

-   Ensuite, nous pouvons appuyer sur une des icônes de vis de l'atelier Fasteners, par exemple le **boulon hexagonal EN 1665 à brides, série lourde**. La vis sera placée et alignée sur notre trou, et le diamètre sera automatiquement sélectionné pour correspondre à la taille de notre trou. Parfois, la vis est inversée, ce que nous pouvons corriger en **inversant son sens**. Nous pouvons également définir son décalage à 2mm, pour suivre la même règle que nous avons utilisée entre la table et les pieds :

<img alt="" src=images/FastenerWorkbench_sel.png  style="width:600px;">

-   Répétez ceci pour tous les trous et notre table est complète !

Comme indiqué précédemment, dans FreeCAD, vous pouvez obtenir le même résultat en suivant des étapes différentes. Pour le démontrer, créons le même tableau en utilisant une méthodologie différente. Rappelez-vous qu\'il n\'y a pas de bonne ou de mauvaise méthode, il n\'y a que la créativité de chacun.

Nous allons commencer de la même manière : en créant un cube avec les dimensions suivantes : longueur 80 mm, largeur 8 mm, et hauteur 750 mm

-   Créez un cube en sélectionnant le bouton <img alt="" src=images/Part_Box.svg  style="width:16px;"> **Cube** et définissez les propriétés suivantes (dans l\'onglet **Données**) :
    -   Longueur : 80 mm
    -   Largeur : 8 mm
    -   Hauteur : 750 mm
-   Ensuite, nous allons créer un <img alt="" src=images/Part_Cylinder.svg  style="width:16px;"> **Cylindre** avec les propriétés suivantes :
    -   rayon : 6 mm, hauteur : 100 mm, angle : 90°, axe : x : 1, y : 0, z : 0, position : x : 40 mm, y : 40 mm, z : 720 mm
-   Ensuite, nous allons appliquer l\'outil de coupe. Sélectionnez le cube et, avec la touche CTRL enfoncée, sélectionnez le cylindre. Gardez à l\'esprit que l\'ordre est important pour définir lequel reste. Appuyez ensuite sur le bouton <img alt="" src=images/Part_Cut.svg  style="width:16px;"> **Couper**.
-   Nous allons ensuite copier et coller l\'objet coupé en appuyant sur **Ctrl+C** puis **Ctrl+V** (ou menu **Édition → Copier** et **Coller**) :
    -   angle : 90°, axe : x : 0, y : 0, z : 1, position : x : 8 mm
-   Sélectionnez les deux objets et appliquez l\'outil <img alt="" src=images/Part_Fuse.svg  style="width:16px;"> **Union**. Les deux objets sont maintenant fusionnés et nous avons un pied.
-   Copiez et collez le pied fusionné, en le positionnant à
    -   angle : 90°, axe : x : 0, y : 0, z : 1, position y : 800 mm.
-   Sélectionnez les deux pieds et créez un <img alt="" src=images/Part_Compound.svg  style="width:16px;"> **composé**.
-   Copiez et collez le composé, en le positionnant à :
    -   angle : 180°, axe : x:0, y:0, z:1, position x : 1200 mm, y : 800 mm. Nous avons nos pieds.

Créons le plateau de la table.

-   Créez un cube aux dimensions suivantes :
    -   Longueur : 752 mm
    -   Largeur : 1184 mm
    -   Hauteur : 784 mm
    -   Position x : 8 mm, y : 8 mm, z : 670 mm.

Maintenant, nous continuons de la même manière que précédemment si nous souhaitons ajouter des vis (nous l\'espérons).

<img alt="" src=images/Tabble_alternative_complete.png  style="width:600px;">

**La structure interne des objets Part**

Comme nous l\'avons vu plus haut, il est possible dans FreeCAD de sélectionner non seulement des objets entiers, mais aussi des parties d\'objets, comme la bordure circulaire de notre trou de vis. C\'est le bon moment pour jeter un coup d\'œil rapide à la façon dont les objets Pièce sont construits en interne. Chaque atelier qui produit une géométrie de Part sera basé sur ces objets :

-   **Sommets** : ce sont les points (généralement les extrémités) sur lesquels tout le reste est construit. Par exemple, une ligne a deux sommets.
-   **Arêtes** : les arêtes sont des géométries linéaires comme des lignes, des arcs, des ellipses ou des courbes [NURBS](https://fr.wikipedia.org/wiki/NURBS). Elles ont généralement deux sommets, mais certaines n\'en ont qu\'un (un cercle fermé par exemple).
-   **Polylignes** : une polyligne est une séquence d\'arêtes connectées par leurs extrémités. Elle peut contenir des arêtes de n\'importe quel type et elle peut être fermée ou non.
-   **Faces** : les faces peuvent être planes ou courbes. Elles peuvent être formées par une polyligne fermée, qui forme l\'arête de la face, ou plusieurs polylignes dans le cas où la face a des trous.
-   **Coques** : les coques sont simplement un groupe de faces reliées par leurs arêtes. Elle peut être ouverte ou fermée.
-   **Solides** : lorsqu\'une coque est hermétiquement fermée, c\'est-à-dire qu\'elle n\'a pas de « fuite », elle devient un solide. Les solides comportent la notion d\'intérieur et d\'extérieur. De nombreux ateliers s\'appuient sur cette notion pour s\'assurer que les objets qu\'ils produisent peuvent être construits dans le monde réel.
-   **Composés** : les composés sont simplement des agrégats d\'autres formes, quel que soit leur type, en une seule forme.

Dans la vue 3D, vous pouvez sélectionner individuellement des **sommets**, des **arêtes** ou des **faces**. En sélectionnant l\'un d'entre eux, vous sélectionnez également l\'objet entier.

**Une note sur le design partagé**

Vous pourriez regarder la table ci-dessus et penser que sa conception n\'est pas bonne. La fixation des pieds sur le plateau de table est probablement trop faible. Vous voudriez peut-être ajouter des pièces de renfort ou simplement vous avez d\'autres idées pour mieux la faire. C\'est là que le partage devient intéressant. Vous pouvez téléchargez le fichier effectué pendant cet exercice à partir du lien ci-dessous et le modifier pour l\'améliorer. Ensuite, si vous partagez ce fichier amélioré, d\'autres pourraient être en mesure de le rendre encore mieux ou utiliser votre table dans leurs projets. Votre conception pourrait alors donner d\'autres idées à d\'autres personnes, et peut-être vous aurez aidé un petit peu à faire un monde meilleur \...

**Téléchargements**

Le fichier produit dans cet exercice: <https://github.com/yorikvanhavre/FreeCADmanual/blob/master/files/table.FCStd>

**Lire plus d'informations**

-   [Atelier Part ](Part_Workbench/fr.md)
-   [Le dépôt FreeCAD addons](https://github.com/FreeCAD/FreeCAD-addons)
-   [L'atelier Fasteners](https://github.com/shaise/FreeCAD_FastenersWB)



---
⏵ [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Traditional modeling, the CSG way/fr
