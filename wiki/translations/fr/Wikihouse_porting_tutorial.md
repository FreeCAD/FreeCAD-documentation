---
- TutorialInfo:/fr
   Topic:Tutoriel de portage Wikihouse
   Level:Intermediaire/Avancé
   Time:60 minutes
   Author:
   FCVersion:
   Files:
---

# Wikihouse porting tutorial/fr





## Introduction

Ce tutoriel va vous montrer comment convertir les fichiers [SketchUp](http://www.sketchup.com/) utilisés par le projet [WikiHouse](http://wikihouse.cc/) en FreeCAD, en utilisant l\'outil [Arch Panneau](Arch_Panel/fr.md) dans FreeCAD. Le résultat est une copie complète du fichier SketchUp d\'origine, la différence est qu\'il est devenu entièrement paramétrique. Le niveau de paramétrage du fichier final dépend du travail que vous y consacrez, comme expliqué ci-dessous. Mais il est tout à fait possible de faire le travail pas à pas, et de reconstruire le fichier Wikihouse rapidement, et de laisser la plus longue conversion des profils de base aux esquisses pour plus tard.

Ce tutoriel nécessite une connaissance intermédiaire de FreeCAD, c\'est-à-dire que vous êtes capable de vous repérer entre les différents ateliers et outils, que vous êtes déjà capable de modéliser des objets simples, et surtout que vous êtes à l\'aise avec [Draft Déplacer](Draft_Move/fr.md) et [Draft Pivoter](Draft_Rotate/fr.md). Il utilisera principalement les outils de [Draft](Draft_Workbench/fr.md) et [Arch](Arch_Workbench/fr.md), mais la connaissance de l\'[atelier Sketcher](Sketcher_Workbench/fr.md) deviendra nécessaire lors de la conversion des profils de base en esquisses.

Puisque le projet Wikihouse est ouvert naturellement, les fichiers sont faciles à trouver sur le site Web du projet, mais aussi sur le [SketchUp 3D Warehouse](https://3dwarehouse.sketchup.com/search.html?q=wikihouse&backendClass=both) ou dans le projet [github repositories](https://github.com/wikihouseproject). Le format préféré utilisé par le projet est Sketchup, donc la plupart des fichiers que vous trouverez sont dans ce format.

Dans ce didacticiel, nous avons utilisé le fichier [Chassis](https://github.com/wikihouseproject/Microhouse/blob/master/microhouse_0.5_chassis.skp) du sous-projet Microhouse de Wikihouse.



## Préparation du fichier Sketchup 

La première chose à faire est d\'ouvrir le fichier dans SketchUp et de supprimer tout ce que vous ne voulez pas exporter. Nous n\'exporterons qu\'une seule section de la Microhouse, donc tout le reste doit être supprimé.

![](images/Arch_Wikihouse_05.jpg )

Les éléments de la Wikihouse, dans SketchUp, sont réalisés d\'une manière spécifique : En ajoutant de petites \"pièces\" ensemble afin de créer les différents composants :

![](images/Arch_Wikihouse_06.jpg )

Ce n\'est pas ainsi que nous allons procéder dans FreeCAD. Puisque l\'une des fonctions les plus puissantes de FreeCAD est les [esquisses constraintes](Sketcher_Workbench/fr.md), nous ferions mieux d\'en profiter, et de baser tous nos éléments de la Wikihouse sur des esquisses. De cette façon, la modification de n\'importe quelle pièce peut être faite dans l\'[atelier Sketcher](Sketcher_Workbench/fr.md), ce qui est beaucoup plus confortable.

Afin de transformer nos objets SketchUp en croquis FreeCAD, qui peuvent ensuite être utilisés pour créer des objets [Arch Panneau](Arch_Panel/fr.md), nous devons extraire une face plane de chaque pièce de la Wikihouse. L\'épaisseur sera rajoutée plus tard, dans FreeCAD, directement dans les propriétés du panneau d\'arche. De cette façon, nous conserverons également le paramétrage. Pour transformer chaque composant de la Wikihouse en une seule face plate, entrez dans chaque composant en double-cliquant dessus, puis sélectionnez chaque sous-composant, et faites un clic droit → Éclater, jusqu\'à ce que tous les sous-composants soient éclatés, et que votre composant ne soit composé que de faces et d\'arêtes :

![](images/Arch_Wikihouse_08.jpg )

Une fois que c\'est fait, sélectionnez tout ce qui se trouve dans votre composant, et désélectionnez, en faisant Shift + double-clic, chaque face avant de votre composant. Veillez à faire un double-clic au lieu d\'un simple clic, car sinon vous ne désélectionnerez que la face et non ses bords (que nous devrons également conserver). Après cela, nous aurons désélectionné tout ce que nous voulons conserver, il ne nous restera plus qu\'à appuyer sur la touche de suppression. Notre composant n\'est plus qu\'une grande face plate.

![](images/Arch_Wikihouse_07.jpg )

Répétez cette opération pour chaque composant. Comme beaucoup d\'entre eux sont dupliqués, ce n\'est pas une tâche aussi énorme qu\'il n\'y paraît. De plus, si vous n\'êtes pas familier avec le système Wikihouse, cette étape vous donnera une bonne compréhension de son fonctionnement.

Lorsque notre maison est entièrement composée d\'éléments plats, nous pouvons tout sélectionner et l\'exporter vers un fichier .dae, puis importer ce fichier dans FreeCAD. Assurez-vous de cocher la case \"trianguler tout\"



## Résolution du problème des doubles faces 

Il existe un problème désagréable pour lequel je n\'ai pas trouvé de meilleure solution : Les faces des maillages exportés de SketchUp au format .dae sont dupliquées. Chaque face devient en fait deux faces. Le moyen le plus simple que j\'ai trouvé jusqu\'à présent est d\'ouvrir le fichier exporté dans [Blender](http://www.blender.org) pour le réparer :

1.  Ouvrez le fichier dae dans Blender (**Fichier → Importer → Collada**).
2.  Sélectionnez un composant et appuyez sur **TAB** pour passer en mode édition.
3.  Appuyez sur **A** pour tout désélectionner, puis sur **A** à nouveau pour tout sélectionner.
4.  Appuyez sur **W** → Supprimer les doubles
5.  Appuyez sur **TAB** pour quitter le mode d\'édition.
6.  Répétez l\'opération pour tous les composants
7.  Enregistrez un nouveau fichier [DAE](Arch_DAE/fr.md) (**Fichier → Exportation → Collada**).

Normalement, l\'opération ci-dessus ne devrait pas modifier l\'échelle, mais il est toujours sage de vérifier, à l\'aide des outils de mesure, que la géométrie importée est à l\'échelle correcte avant d\'aller plus loin. Vous devrez peut-être modifier les paramètres d\'exportation Collada de Blender si nécessaire.



## Importer et convertir en polylignes 

Remarquez qu\'il peut être plus facile d\'aller par parties et de traiter + exporter les objets groupe par groupe, comme nous l\'avons fait ci-dessous, nous avons exporté seulement la première couche, faite d\'éléments jaunes dans SketchUp. Ces éléments arriveront dans FreeCAD en tant qu\'objets [Mesh](Mesh_Workbench/fr.md) :

![](images/Arch_Wikihouse_09.jpg )

L\'étape suivante consiste à créer des fils à partir de chacun de nos maillages. Il existe une macro pratique nommée [Macro Extract Wires from Mesh](Macro_Extract_Wires_from_Mesh/fr.md) qui fait exactement cela. Installez-la (consultez la page [Macros](Macros/fr.md) pour obtenir des instructions), puis, un par un (vous pouvez les faire tous en même temps, mais cette macro prend un certain temps), convertissez tous nos maillages en objets filaires :

![](images/Arch_Wikihouse_10.jpg )

Nous pourrions déjà créer des objets [Arch Panneau](Arch_Panel/fr.md) à partir de chacun de ces objets filiformes, simplement en les sélectionnant et en appuyant sur le bouton [Arch Panneau](Arch_Panel/fr.md). Cependant, leur forme de base ne serait pas paramétrique. Nous avons maintenant plusieurs options : Nous pouvons transformer chaque composant en une esquisse, à l\'aide de l\'outil [Draft Draft vers Esquisse](Draft_Draft2Sketch/fr.md), mais il s\'agira d\'esquisses plutôt lourdes, qui risquent de ne pas être très faciles à gérer sur une machine lente, ou nous pouvons transformer chaque polyligne (le contour et chaque trou) de l\'esquisse en une esquisse distincte. Cela nous permettrait, par exemple, de réutiliser un trou typique, de le faire une seule fois, puis de le dupliquer avec [Draft Cloner](Draft_Clone/fr.md) pour faire les autres trous. De cette façon, il suffirait d\'en éditer un pour les éditer tous.

La [Macro Extract Wires from Mesh](Macro_Extract_Wires_from_Mesh/fr.md) échoue aussi parfois à trouver des fils fermés à l\'intérieur d\'un maillage, ce qui ne produira pas des panneaux corrects. Une procédure simple pour recomposer les fils d\'un composant est la suivante :

1.  Sélectionner le composant, éventuellement cacher tout le reste pour mieux voir
2.  [Draft Rétrogradez](Draft_Downgrade/fr.md) le. Il sera éclaté en une série d\'arêtes individuelles
3.  Commencez à sélectionner les trous avec Ctrl ou en utilisant Shift + B pour faire une sélection par boîte.
4.  Appuyez sur [Draft Agréger](Draft_Upgrade/fr.md) pour transformer chaque trou en un fil individuel.
5.  Enfin, sélectionnez toutes les arêtes individuelles restantes dans l\'arbre, qui forment le contour, et [Draft Agréger](Draft_Upgrade/fr.md).
6.  Sélectionnez **Pièce → Créer un composé** pour réunir tous ces fils en un seul objet.
7.  Sélectionnez le composé et appuyez sur le bouton [Arch Panneau](Arch_Panel/fr.md).

![](images/Arch_Wikihouse_11.jpg )

Il y a plusieurs stratégies possibles ici, selon le degré d\'éditabilité et de précision dont vous avez besoin pour le résultat. L\'objet [Arch Panneau](Arch_Panel/fr.md) a besoin d\'un objet de base fait de fils. La façon dont cet objet est fabriqué n\'a pas d\'importance, qu\'il s\'agisse d\'une seule esquisse ou, comme dans l\'exemple ci-dessus, d\'un composé de différentes esquisses ou d\'un objet Draft.



## Convertir en esquisses 

Il est également possible de faire cette partie plus tard, vous pourriez déjà créer des panneaux à partir de chacun des composants, mais voyons déjà comment convertir un objet filaire en un esquisse :

1.  Créez une copie de votre objet filaire avec **Ctrl**+**C**, **Ctrl**+**V**. Ainsi, nous pouvons le modifier tout en le gardant à son emplacement correct.
2.  Déplacez et faites-le pivoter pour qu\'il se trouve dans le plan XY, en utilisant [Draft Déplacer](Draft_Move/fr.md) et [Draft Pivoter](Draft_Rotate/fr.md). Ce n\'est pas indispensable, mais le point suivant échoue parfois autrement
3.  Utilisez [Draft Draft vers Esquisse](Draft_Draft2Sketch/fr.md) pour transformer le fil en esquisse. Attention, cela peut échouer ou prendre beaucoup de temps pour les longues polylignes. Il est préférable de décomposer votre objet en lignes individuelles comme indiqué ci-dessus.
4.  Si la commande ci-dessus échoue, utiliser [Draft Agréger](Draft_Upgrade/fr.md) deux fois sur un objet filaire, pour le convertir en Face puis en [Draft Polyligne](Draft_Wire/fr.md), avant d\'utiliser [Draft Draft vers Esquisse](Draft_Draft2Sketch/fr.md), fonctionne généralement mieux, car le Draft Wire garde une meilleure trace de l\'ordre des vertices dans un fil.
5.  Les courbes sont constituées de plusieurs petits segments. Elles peuvent être laissées telles quelles, mais elles introduisent beaucoup de contraintes au niveau des extrémités. Il est préférable de les remplacer par des arcs. C\'est assez facile à faire, il suffit de supprimer les petits segments et de les remplacer par un arc. L\'arc peut ensuite être rendu tangentiel aux segments voisins, mais assurez-vous que la position de ces segments est verrouillée avant de le faire, car cette opération les fera bouger.
6.  Si vous avez travaillé avec plusieurs esquisses, faites-en un [Part Composé](Part_Compound/fr.md).
7.  Créez un [Arch Panneau](Arch_Panel/fr.md) à partir de celui-ci.
8.  Faites-le pivoter/remettre en place avec [Draft Déplacer](Draft_Move/fr.md) et [Draft Pivoter](Draft_Rotate/fr.md).

![](images/Arch_Wikihouse_12.jpg )



## Reconstruire la Wikihouse et exporter les panneaux découpés 

Veillez également à ne pas refaire les pièces dupliquées. Sélectionnez plutôt l\'outil [Draft Cloner](Draft_Clone/fr.md) pour dupliquer les pièces basées sur le même profil, de sorte qu\'elles partagent toutes le même objet de profil. Puis, puisque nous avons le contour au bon endroit pour l\'utiliser comme guide, il est assez facile de faire pivoter et de déplacer le clone dans sa position correcte avec [Draft Déplacer](Draft_Move/fr.md) et [Draft Pivoter](Draft_Rotate/fr.md).

Après un certain temps, toute notre section Microhouse est terminée.

![](images/Arch_Wikihouse_01.jpg )

Nous pouvons maintenant créer facilement les panneaux découpés, qui sont des fichiers DXF qui seront envoyés à l\'atelier qui coupera les panneaux réels. La façon la plus simple de procéder est de sélectionner tout ce qui se trouve dans votre document avec **Ctrl**+**A**, puis d\'utiliser l\'outil [Arch Découpe de panneaux](Arch_Panel_Cut/fr.md). Cela produira un objet Panneau découpé pour chaque objet Panneau trouvé dans la sélection. En les séparant, nous obtenons une vue claire de toutes nos pièces :

![](images/Arch_Wikihouse_02.jpg )

Il faut ensuite \"emboîter\" nos pièces, c\'est-à-dire les déplacer et les faire pivoter pour qu\'elles occupent le plus possible l\'espace d\'un panneau donné, afin de générer le moins de perte matérielle possible. Cette opération doit malheureusement être faite à la main, mais si vous utilisez un projet Wikihouse qui a déjà produit des panneaux découpés, les copier va assez vite :

1.  Pour être sûr que tout restera dans le plan XY, il est conseillé de régler le [Draft Plan de travail](Draft_SelectPlane/fr.md) sur XY (haut).
2.  Créez un [Arch Panneau de feuille](Arch_Panel_Sheet/fr.md).
3.  Donnez-lui les valeurs de largeur et de hauteur souhaitées (les maisons Wiki sont généralement imprimées sur des feuilles de contreplaqué de 122x244cm)
4.  Déplacez-la à un endroit approprié avec [Draft Déplacer](Draft_Move/fr.md).
5.  Optionnellement, définissez ses valeurs de marge pour vous aider à positionner les pièces découpées.
6.  Déplacez et faites pivoter les objets individuels [Arch panneaux découpés](Arch_Panel_Cut/fr.md) pour qu\'ils s\'insèrent dans la feuille de panneau.
7.  Lorsque vous êtes plus ou moins prêt, sélectionnez le panneau et double-cliquez dessus dans l\'arborescence pour passer en mode édition.
8.  Sélectionnez toutes les coupes de panneau que vous souhaitez y insérer (vous pouvez passer de l\'arborescence à l\'onglet \"projet\" pour sélectionner dans la [Vue en arborescence](Tree_view/fr.md)).
9.  Sélectionnez la section \"groupe\" dans la vue des tâches de la feuille de panneau.
10. Cliquez sur le bouton **Ajouter**.
11. Appuyez sur le bouton **OK**.

Dans la vue des tâches de la feuille de panneau, il y a également un bouton qui vous permet de déplacer les coupes de panneau individuelles après qu\'elles ont été insérées dans la feuille. Après un certain temps, nos feuilles sont prêtes :

![](images/Arch_Wikihouse_03.jpg )

La dernière étape consiste simplement à sélectionner toutes les feuilles, puis à les exporter au format DXF à partir du menu Fichier → Exporter. Le contenu des feuilles sera exporté séparé en différentes couches, avec le même code couleur couramment utilisé par le projet Wikihouse :

![](images/Arch_Wikihouse_04.jpg )

Ces fichiers sont prêts à être envoyés aux ateliers qui effectueront la découpe proprement dite. Il serait également possible de générer le code G à envoyer à la machine CNC directement à partir de FreeCAD, mais cela fera l\'objet d\'un autre tutoriel.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Wikihouse porting tutorial/fr
