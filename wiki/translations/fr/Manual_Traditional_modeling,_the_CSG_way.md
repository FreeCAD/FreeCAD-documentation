# Manual:Traditional modeling, the CSG way/fr
{{Manual   *TOC/fr}}

La [géométrie de construction de solides](wikipedia   *fr_Géométrie_de_construction_de_solides.md) (CSG en anglais    * *Constructive Solid Geometry*) décrit la manière la plus simple de travailler avec la géométrie 3D des solides. Elle crée des objets complexes en ajoutant/enlevant des éléments de volumes en utilisant des opérations booléennes telles que l\'union, la soustraction ou l\'intersection de solides.

Comme nous l\'avons vu plus tôt dans ce manuel, FreeCAD peut gérer de nombreux types de géométrie. La géométrie préférée et la plus utile pour la conception d\'objets 3D avec FreeCAD, c\'est-à-dire les objets du monde réel, est sans aucun doute la géométrie [BREP](https   *//fr.wikipedia.org/wiki/G%C3%A9om%C3%A9trie_de_construction_de_solides), principalement prise en charge par l'([atelier Part](Part_Workbench/fr.md)). Contrairement aux maillages de polygones ([Mesh (objet)](https   *//fr.wikipedia.org/wiki/Mesh_(objet))), constitués uniquement de points et triangles, les objets BREP ont leurs faces définies par des courbes mathématiques, qui permettent une précision absolue, peu importe l\'échelle.

![](images/Mesh_vs_brep.jpg )

La différence entre les deux géométries (BREP et maillage polygonal) peut être comparée à celle existant entre les images au format bitmap et les images vectorielles. Comme pour les images bitmap, les maillons polygonaux ont leurs surfaces courbes fractionnées en une série de points. Si vous regardez de très près ou imprimiez en très grand un objet maillé, vous n'allez pas voir une surface courbe mais une surface facettée. Dans les images vectorielles et les données BREP, la position de n\'importe quel point sur une courbe n\'est pas stockée dans la géométrie mais est calculée à la volée, générant une précision exacte.

Dans FreeCAD, toute la géométrie basée sur BREP est gérée par un autre logiciel open source, [OpenCasCade](https   *//fr.wikipedia.org/wiki/Open_CASCADE_Technology). L\'interface principale entre FreeCAD et le noyau OpenCasCade est l'atelier Part. La plupart des autres ateliers créent leurs fonctionnalités par dessus l'atelier Part.

Bien que d\'autres ateliers proposent souvent des outils plus avancés pour construire et manipuler la géométrie, tous manipulent les objets Part, il est très utile de savoir comment ces objets fonctionnent en interne et peuvent utiliser les outils de Part. Plus simples, ils peuvent très souvent vous aider à contourner les problèmes que des outils les plus intelligents ne parviennent pas à résoudre correctement.

Pour illustrer le fonctionnement de l'atelier Part, nous modéliserons cette table, en utilisant uniquement des opérations CSG (à l\'exception des vis, pour lesquelles nous utiliserons l\'un des greffons (addons), et les dimensions, qui seront vues dans le chapitre suivant)    *

![](images/Exercise_table_complete.jpg )

Créez un nouveau document (**Ctrl+N** ou par le menu Fichier → Nouveau document). Le document reçoit le nom \"Sans nom1\" dans la Vue Combinée. Si vous le sauvegardez (**Ctrl+Shift+S** ou par le menu Fichier → Enregistrer sous) comme un nouveau document FreeCAD avec le nom \"table.Fcstd\" alors le document sera renommé \"table\", ce qui est plus facile à identifier.

Maintenant basculez sur l\'atelier Part et commencez à créer la première patte de la table   *

-   Appuyez sur le bouton <img alt="" src=images/Part_Box.svg  style="width   *16px;"> 
**Cube**
-   Sélectionnez le cube obtenu, puis définissez les propriétés suivantes (dans l\'onglet **Données**)   *
    -   Longueur   * 80mm (ou 8cm, ou 0.8m, FreeCAD fonctionne dans n\'importe quelle unité)
    -   Largeur   * 80mm
    -   Hauteur   * 75cm
-   Dupliquez la boîte en appuyant sur **Ctrl + C** puis sur **Ctrl + V** (ou menu Édition → Copier et coller) (à première vue il n\'y a pas de différences, les deux objets se superposant)
-   Sélectionnez le nouvel objet Cube001 en cliquant dessus à partir de l\'onglet Modèle situé à gauche
-   Changez sa position en modifiant ses propriétés de placement    *
    -   Position x   * 8mm
    -   Position y   * 8mm

Vous devriez obtenir deux boîtes hautes, distante de 8 mm l\'une de l\'autre    *

![](images/Exercise_table_01.jpg )

-   Maintenant, nous pouvons soustraire l\'une de l\'autre   * Sélectionnez la **première**, c\'est-à-dire celle qui va **rester**, puis avec la touche CTRL enfoncée, sélectionnez **l\'autre** qui sera **soustraite** (l\'ordre est important) et appuyez sur le bouton <img alt="" src=images/Part_Cut.svg  style="width   *16px;"> **Soustraction** (soustraction booléenne)     *

![](images/Exercise_table_02.jpg )

Observez que l\'objet nouvellement créé, appelé \"Cut\", contient toujours les deux cubes que nous avons utilisés comme les opérandes. En fait, les deux cubes sont toujours présents dans le document, ils ont simplement été cachés et regroupés sous l\'objet \"Cut\" dans l\'arborescence. Vous pouvez toujours les sélectionner en développant la flèche à côté de l\'objet \"Cut\" et, si vous le souhaitez, les rendre visibles à nouveau en cliquant droit sur eux ou en modifiant l\'une de leurs propriétés.

Vous pouvez également utiliser l\'outils Soustraction et d\'autres outils booléens via la \"Vue combinée\" avec <img alt="" src=images/Part_Boolean.svg  style="width   *16px;"> [Part Opération booléenne](Part_Boolean/fr.md). Cela donne un moyen plus explicite mais plus long de le faire.

-   Maintenant, créez les trois autres pieds en copiant notre boîte de base 6 autres fois. Puisqu\'elle est toujours copié, vous pouvez simplement coller (Ctrl + V) 6 fois. Modifiez leur position comme suit    *
    -   cube002   * x   * 0, y   * 80cm
    -   cube003   * x   * 8mm, y   * 79.2cm
    -   cube004   * x   * 120cm, y   * 0
    -   cube005   * x   * 119.2cm, y   * 8mm
    -   cube006   * x   * 120cm, y   * 80cm
    -   cube007   * x   * 119.2cm, y   * 79.2cm

-   Faites les trois autres coupes en sélectionnant d\'abord le cube \"hôte\" puis le cube à soustraire. Nous avons maintenant quatre objets Cut   *

![](images/Exercise_table_03.jpg )

Vous avez peut-être pensé qu\'au lieu de dupliquer le cube de base six fois, nous aurions pu dupliquer le pied complet trois fois. C\'est tout à fait vrai. Dans FreeCAD, il existe plusieurs façons d\'obtenir un même résultat. C\'est un point important à retenir parce que lorsque nous progresserons vers des objets plus complexes, certaines opérations pourraient ne pas donner un résultat satisfaisant. Nous devrons alors essayer d\'autres façons.

-   Nous allons maintenant faire des trous pour les vis en utilisant la même méthode de coupe. Puisque nous avons besoin de 8 trous, deux dans chaque pied, nous pourrions faire 8 objets à soustraire. Au lieu de cela, voici une autre manière   * créons quatre cylindres en utilisant l\'outil <img alt="" src=images/Part_Cylinder.svg  style="width   *16px;"> **Cylindre** (un cylindre pour deux pieds). Vous pouvez à nouveau en faire un seul et le copier ensuite. Donnez à tous les cylindres un rayon de 6 mm. Cette fois, nous devrons les faire pivoter, ce qui se fait également par la propriété **Placement** de l\'onglet Données \'\'(**Note   *** changez la propriété de l\'Axe *avant* de modifier la valeur de l\'angle ou la rotation ne sera pas appliqué)\'\'
    -   Cylindre   * hauteur   * 130cm, angle   * 90 °, axe   * x   * 0, y   * 1, position   * x   * -10mm, y   * 40mm, Z   * 72cm
    -   Cylindre001   * hauteur   * 130cm, angle   * 90 °, axe   * x   * 0, y   * 1, position   * x   * -10mm, y   * 84cm, Z   * 72cm
    -   Cylindre002   * hauteur   * 90cm, angle   * 90 °, axe   * x   * -1, y   * 0, position   * x   * 40mm, y   * -10mm, Z   * 70cm
    -   Cylindre003   * hauteur   * 90cm, angle   * 90 °, axe   * x   * -1, y   * 0, position   * x   * 124cm, y   * -10mm, Z   * 70cm

![](images/Exercise_table_04.jpg )

Vous remarquerez que les cylindres sont un peu plus longs que nécessaire. C\'est parce que comme dans toutes les applications 3D solides, les opérations booléennes dans FreeCAD sont parfois trop sensibles à des situations face-sur-face et pourraient échouer. En faisant cela, nous nous sommes placés dans une situation sûre.

-   Maintenant, faisons les soustractions. Sélectionnez le premier pied, puis, avec la touche CTRL enfoncée, sélectionnez un des cylindres qui le traversent, appuyez sur le bouton **Soustraction**. Le trou sera fait et le cylindre caché. Vous le trouverez dans l\'arborescence en développant le pied percé.
-   Sélectionnez un autre pied percé par ce cylindre caché, puis répétez l\'opération. Cette fois-ci, sélectionnez le cylindre dans l\'arborescence avec Ctrl +, puiqu\'il est caché dans la vue 3D (vous pouvez également le rendre visible pour le sélectionner dans la vue 3D). Répétez ceci pour les autres pieds jusqu\'à ce que chacun d\'eux ait ses deux trous    *

![](images/Exercise_table_05.jpg )

Comme vous pouvez le voir, chaque pied est devenu une série assez longue d\'opérations. Tout cela reste paramétrique, et vous pouvez changer n\'importe quel paramètre de l\'une des anciennes opérations à tout moment. Dans FreeCAD, nous nous référons souvent à cette pile comme «historique de la modélisation» (ou parfois arbre de construction), car elle porte en fait tout l'historique des opérations que vous avez effectuées.

Une autre particularité de FreeCAD est que le concept de l\'objet 3D et le concept de l\'opération 3D ont tendance à se fondre en une même chose. La soustraction est à la fois une opération et l'objet 3D résultant de cette opération. Dans FreeCAD, cela s\'appelle une \"fonctionnalité\", plutôt que objet ou opération.

-   Maintenant, faisons le dessus de la table, ce sera un simple bloc de bois ; faisons-le avec une autre **Boîte** de longueur   * 126cm, largeur   * 86cm, hauteur   * 8cm, position   * x   * 10mm, y   * 10mm, z, 67cm. Dans l\'onglet Affichage, vous pouvez lui donner une couleur marron pour simuler le bois en changeant sa **Propriété couleur**    *

![](images/Exercise_table_06.jpg )

Notez que, bien que les pieds aient 8 mm d\'épaisseur, nous les avons placé à 10 mm, créeant un jeu de 2 mm avec le plateau de la table. Ce n\'est pas nécessaire bien sûr. Cela n\'arrivera pas avec la vraie table mais c\'est une pratique courante utilisée dans ce genre de modèles \"assemblés\". Cela aide les personnes qui regardent le modèle à comprendre que ce sont des pièces indépendantes et qui devront être jointes ensemble manuellement plus tard.

Maintenant que nos cinq pièces sont complètes, c\'est le moment pour leur donner des noms plus parlant que \"Cut015\". En cliquant avec le bouton droit sur les objets dans l\'arborescence (ou en appuyant sur **F2**), vous pouvez les renommer de façon plus significative pour vous-même ou pour une autre personne qui ouvrirait votre travail plus tard. On dit souvent que le fait de donner simplement des noms concrets à vos objets est beaucoup plus important que la façon dont vous les modélisez.

-   Nous allons maintenant placer des vis. Il existe aujourd\'hui un addon extrêmement utile développé par un membre de la communauté FreeCAD que vous trouverez dans le dépôt des greffons FreeCad ([FreeCAD addons](https   *//github.com/FreeCAD/FreeCAD-addons)) appelé [Fasteners](https   *//github.com/shaise/FreeCAD_FastenersWB). Il facilite l\'insertion de vis. L\'installation d'ateliers supplémentaires est simple et est décrite dans les pages du [Gestionnaire des Addons](Std_AddonMgr/fr.md).
-   Une fois que vous avez installé l'atelier Fasteners et redémarré FreeCAD, il apparait dans la liste des ateliers, et nous pouvons l'utiliser. Ajouter une vis à l\'un de nos trous est effectué en sélectionnant d\'abord l\'arête circulaire de notre trou    *

![](images/Exercise_table_07.jpg )

-   Ensuite, nous pouvons appuyer sur une des icônes de vis de l'atelier Fasteners, par exemple le **boulon hexagonal EN 1665 à brides, série lourde**. La vis sera placée et alignée sur notre trou, et le diamètre sera automatiquement sélectionné pour correspondre à la taille de notre trou. Parfois, la vis est inversée, ce que nous pouvons corriger en **inversant son sens**. Nous pouvons également définir son décalage à 2mm, pour suivre la même règle que nous avons utilisée entre la table et les pieds    *

![](images/Exercise_table_08.jpg )

Répétez ceci pour tous les trous et notre table est complète !

**La structure interne des objets Part**

Comme nous l\'avons vu ci-dessus, il est possible dans FreeCAD de sélectionner non seulement des objets entiers, mais aussi des éléments de ces objets, comme par exemple la bordure circulaire de notre trou de vis. C\'est le bon moment pour regarder rapidement la façon dont les objets Part sont construits en interne. Chaque atelier qui produit une géométrie Part sera basée sur ceux-ci    *

-   **Sommets**    * ce sont des points (généralement des points d\'extrémité) sur lesquels tout le reste est construit. Par exemple, une ligne comporte deux sommets.
-   **Arêtes**    * les arêtes sont de la géométrie linéaire comme les lignes, les arcs, les ellipses ou les courbes [NURBS](https   *//fr.wikipedia.org/wiki/NURBS). Elles ont généralement deux sommets, mais certains cas particuliers en ont seulement un (un cercle fermé par exemple).
-   **Lignes composites**    * une ligne composite est une succession d\'arêtes connectées par leurs extrémités. Elle peut contenir des arêtes de n\'importe quel type, et elle peut être fermée ou non.
-   **Faces**    * les faces peuvent être planaires ou courbes. Elles peuvent être formées par une ligne composite fermée, celle-ci génère la bordure extérieure de la face, ou plus d\'une dans le cas où la face a des trous.
-   **Coquilles**    * les coquilles sont simplement un groupe de faces reliées par leurs bords. Elles peuvent être ouvertes ou fermées.
-   **Solides**    * lorsqu\'une coquille est complètement fermée, c\'est-à-dire qu\'elle n\'a pas de \"fuite\", elle devient solide. Les solides portent la notion d\'intérieur et d\'extérieur. De nombreux ateliers s\'appuient sur cette notion pour que les objets qu\'ils produisent puissent être construits dans le monde réel.
-   **Composés**    * Les composés sont simplement des agrégats d\'autres formes, quel que soit leur type, en une seule forme.

Dans la vue 3D, vous pouvez sélectionner individuellement des **sommets**, des **arêtes** ou des **faces**. En sélectionnant l\'un d'entre eux, vous sélectionnez également l\'objet entier.

**Une note sur le design partagé**

Vous pourriez regarder la table ci-dessus et penser que son design n\'est pas bon. La fixation des pieds sur le plateau de table est probablement trop faible. Vous voudriez peut-être ajouter des pièces de renfort ou simplement vous avez d\'autres idées pour mieux la faire. C\'est là que le partage devient intéressant. Vous pouvez téléchargez le fichier effectué pendant cet exercice à partir du lien ci-dessous et le modifier pour l\'améliorer. Ensuite, si vous partagez ce fichier amélioré, d\'autres pourraient être en mesure de le rendre encore mieux ou utiliser votre table dans leurs projets. Votre conception pourrait alors donner d\'autres idées à d\'autres personnes, et peut-être vous aurez aidé un petit peu à faire un monde meilleur \...

**Téléchargements**

Le fichier produit dans cet exercice   * <https   *//github.com/yorikvanhavre/FreeCADmanual/blob/master/files/table.FCStd>

**Lire plus d'informations**

-   [Atelier Part ](Part_Workbench/fr.md)
-   [Le dépôt FreeCAD addons](https   *//github.com/FreeCAD/FreeCAD-addons)
-   [L'atelier Fasteners](https   *//github.com/shaise/FreeCAD_FastenersWB)




[Category   *Tutorials](Category_Tutorials.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Traditional modeling, the CSG way/fr
