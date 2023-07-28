# Which workbench should I choose/fr
Si vous êtes nouveau dans FreeCAD, il y a de fortes chances que vous vous demandiez avec quel [atelier](Workbenches/fr.md) vous devriez commencer à travailler. Cette page vous aidera à choisir par où commencer.

Les ateliers sont des ensembles d\'outils, de boutons, de panneaux et d\'autres éléments d\'interface regroupés. Il s\'agit en quelque sorte d\'une application à l\'intérieur d\'une application. Dans FreeCAD, les ateliers regroupent généralement un ensemble d\'outils adaptés à un usage particulier, comme le dessin 2D, la conception d\'objets 3D, la conception de bateaux, la conception de trajectoires de robots, la conception de bâtiments, et bien plus encore.

FreeCAD est livré avec plusieurs [ateliers intégrés](Workbenches/fr.md), mais de [nombreux autres ateliers sont disponibles](External_workbenches/fr.md) et peuvent être facilement installés via le [gestionnaire des extensions](Std_AddonMgr/fr.md).

Les nouveaux utilisateurs de FreeCAD commencent généralement par utiliser et apprendre un ou deux ateliers particuliers, puis explorent d\'autres domaines de FreeCAD et ajoutent les outils qu\'ils trouvent intéressants. Cependant, avant de plonger dans des ateliers particuliers, assurez-vous de lire les pages [Démarrer avec FreeCAD](Getting_started/fr.md) et [Manuel : Navigation dans la vue 3D](Manual:Navigating_in_the_3D_view/fr.md) car elles fournissent des connaissances génériques dont vous aurez besoin partout dans FreeCAD. Le [Manuel : Introduction](Manual:Introduction/fr.md) est un autre bon moyen de découvrir FreeCAD pas à pas, de manière linéaire.

Le premier atelier que vous devriez utiliser dépend de ce que vous avez l\'intention de faire avec FreeCAD. Nous voyons généralement les nouveaux utilisateurs arriver avec l\'une des exigences suivantes :



## Je n\'ai aucune expérience en CAO et je souhaite concevoir et imprimer en 3D un objet 

C\'est probablement le cas d\'utilisation le plus courant parmi les nouveaux utilisateurs de FreeCAD, et c\'est ce que FreeCAD fait le mieux. Il dispose d\'un atelier spécifique pour cela : l\'[atelier PartDesign](PartDesign_Workbench/fr.md). PartDesign contient également tous les outils de l\'[atelier Sketcher](Sketcher_Workbench/fr.md), ce qui vous permet d\'apprendre et d\'utiliser deux ateliers en un.

Lorsque vous démarrez un nouveau modèle avec PartDesign, vous devez généralement commencer par créer un [corps (body en anglais)](PartDesign_Body/fr.md). Un corps est à la fois un conteneur pour les sous-formes et le résultat, votre objet final. Pensez \"un objet = un corps\". Le corps, bien qu\'il puisse être composé de plusieurs parties, doit toujours représenter un seul objet assemblé, sans aucune pièce détachée. La plupart des opérations que vous effectuez sur ou à l\'intérieur d\'un corps vous empêcheront de créer des pièces détachées.

Le plus souvent, les opérations effectuées à l\'intérieur d\'un organisme sont les suivantes :

1.  [Dessiner une forme 2D fermée](Sketcher_NewSketch/fr.md) (également appelée [esquisses](Sketcher_Workbench/fr.md)) sur un plan de l\'espace 3D (par exemple, sur le plan (XY) ou sur une face d\'une pièce existante). L\'esquisse est une fonction très puissante de FreeCAD. Elle peut contenir des segments linéaires ou courbes, mais aussi des éléments complexes tels que des contraintes ou une géométrie de construction.
2.  [Extruder cette forme](PartDesign_Pad/fr.md) pour qu\'elle forme un solide
3.  Utiliser ce solide comme [addition](PartDesign_Pad/fr.md) ou une [soustraction](PartDesign_Pocket/fr.md) d\'un autre solide
4.  Vous pouvez appliquer des finitions telles que des [congés](PartDesign_Fillet/fr.md) sur certaines faces

Répétez ce processus jusqu\'à ce que vous obteniez votre objet fini. Consultez la liste des tutoriels ci-dessous pour obtenir des informations plus approfondies et des exemples de processus de modélisation typiques. Lorsque vous avez terminé de modéliser votre objet, il est temps de l\'envoyer à l\'imprimante 3D. Cela signifie généralement

1.  Assurez-vous que votre imprimante 3D est installée et qu\'une application de découpe est prête (une application chargée de transformer un objet 3D en commandes pour l\'imprimante, telle que [slic3r](https://slic3r.org/) ou [cura](https://ultimaker.com/software/ultimaker-cura)).
2.  Sélectionnez votre corps (votre objet final)
3.  Allez au menu Fichier -\> Exporter et exportez votre objet dans un format supporté par votre application de slicer, généralement le format STL.
4.  Ouvrez le fichier STL dans le slicer, réglez les paramètres corrects pour votre imprimante et appuyez sur le bouton \"imprimer\".

Il existe de nombreux autres endroits dans cette documentation pour en savoir plus sur le flux de travail de PartDesign et sur l\'utilisation de Sketcher :

-   En savoir plus sur l\'[atelier PartDesign](PartDesign_Workbench/fr.md)
-   En savoir plus sur l\'[atelier Sketcher](Sketcher_Workbench/fr.md)
-   Tutoriel : [Créer une pièce simple avec PartDesign](Creating_a_simple_part_with_PartDesign/fr.md)
-   Tutoriel : [Tutoriel d\'introduction Part Design](Basic_Part_Design_Tutorial/fr.md)
-   Tutoriel : [Manuel: Modélisation pour la conception de produits](Manual:Modeling_for_product_design/fr.md)
-   Tutoriel : [Exporter des STL ou OBJ](Export_to_STL_or_OBJ/fr.md)



## J\'ai de l\'expérience avec SolidWorks ou quelque chose de similaire. Je veux faire de la conception de produits et des assemblages 

La première partie de votre cas d\'utilisation est assez similaire à la précédente. Vous utiliserez typiquement l\'[atelier PartDesign](PartDesign_Workbench/fr.md) qui contient également tous les outils de l\'[atelier Sketcher](Sketcher_Workbench/fr.md). Vous concevrez généralement un corps pour chaque pièce de votre assemblage.

Une fois que vous avez obtenu vos différentes pièces, vous devez les assembler. FreeCAD ne dispose pas pour l\'instant d\'un atelier d\'assemblage unique et par défaut. Il existe plutôt plusieurs modules complémentaires d\'assemblage que vous pouvez facilement installer via le [gestionnaire des extensions](Std_AddonMgr/fr.md) :

-   L\'[atelier A2plus](A2plus_Workbench/fr.md) fournit des outils pour créer des assemblages en plusieurs parties. C\'est le plus ancien que nous ayons dans FreeCAD. Il est né avant que des fonctionnalités avancées comme les objets App Link ne soient disponibles dans FreeCAD, il est donc plus basique et plus simple, ce qui peut être un problème ou un avantage.
-   L\'[atelier Assembly3](Assembly3_Workbench/fr.md) est utilisé pour réaliser l\'assemblage de différents corps contenus dans un seul fichier ou dans plusieurs documents. Il a servi de banc d\'essai pour l\'objet App Link qui a finalement été inclus dans le code principal. Il s\'agit de la solution la plus complexe, qui prend en charge des éléments tels que la cinématique interactive.
-   L\'[atelier Assembly4](Assembly4_Workbench/fr.md) est une solution basée sur le moteur d\'expression amélioré et l\'objet App Link développé dans la branche Assembly3. Assembly4 ne fonctionne pas avec un solveur de contraintes, mais utilise le moteur d\'expression pour positionner les corps par rapport aux systèmes de coordonnées locales (LCS).

Le choix de la meilleure solution dépend de vos besoins et il n\'est pas facile de le savoir à l\'avance. Nous vous suggérons d\'essayer d\'abord Assembly4, puis Assembly3 si vous avez besoin de quelque chose de plus complexe ou A2Plus si c\'est trop complexe pour vos besoins.



## J\'ai de l\'expérience avec AutoCAD ou quelque chose de similaire. Je veux faire du dessin en 2D 

Bien que FreeCAD soit avant tout une application 3D, il dispose de tous les outils nécessaires pour dessiner et annoter des conceptions 2D complexes, telles que des plans de maison, et pour les imprimer, les exporter au format PDF ou les exporter dans d\'autres formats pris en charge par d\'autres applications CAO 2D traditionnelles, telles que DXF ou DWG.

L\'atelier de choix pour le dessin 2D est l\'[atelier Draft](Draft_Workbench/fr.md). Draft dispose de tous les outils que l\'on trouve couramment dans les applications CAO traditionnelles, tels que les lignes, les rectangles, les arcs, les splines, les hachures, les textes ou les dimensions, et les outils permettant de modifier les objets, tels que le déplacement, la rotation, l\'extension, la mise à l\'échelle, le décalage, etc.

Les objets que vous dessinez peuvent être regroupés à l\'aide de groupes ou de calques, et les dessins que vous créez peuvent être exportés sous forme de fichiers DXF/DWG, ou placés à une certaine échelle sur une feuille qui représente une feuille de papier. Cette feuille peut ensuite être imprimée ou exportée sous forme de fichier PDF.

Contrairement aux applications de CAO 2D traditionnelles, FreeCAD est avant tout une application de CAO 3D. La première étape à franchir lorsque vous commencez à travailler avec les outils de dessin est donc de choisir le plan de l\'espace 3D dans lequel vous souhaitez dessiner votre projet. Traditionnellement, cela se fait dans le plan XY, qui serait un plan horizontal posé sur le sol, à l\'altitude zéro.

Dans Draft, vous faites cela en définissant votre [plan de travail](Draft_SelectPlane/fr.md). Le plan de travail est l\'endroit où les prochaines opérations de dessin (ligne, rectangle, etc.) seront effectuées. Vous pouvez changer le plan de travail à tout moment, mais vous pouvez aussi configurer FreeCAD pour qu\'il démarre toujours avec le plan de travail réglé sur le plan XY et ne plus vous en préoccuper.

Veillez à lire comment [naviguer dans l\'espace 3D](Manual:Navigating_in_the_3D_view/fr.md), afin de savoir comment définir votre point de vue pour regarder directement votre plan de travail depuis le haut et revenir à ce point de vue si vous vous en éloignez. Vous disposerez ainsi d\'un espace de travail confortable, similaire à l\'application que vous connaissez.

Une fois votre plan de travail défini, il ne vous reste plus qu\'à commencer à dessiner. Explorez la [liste des outils de Draft disponibles](Draft_Workbench/fr.md). Ils se comporteront essentiellement de la même manière que les autres applications de CAO 2D. Par exemple, dessinez des lignes qui représentent les limites d\'un terrain, ou un rectangle qui représente une maison.

Lorsque vous travaillez avec Draft, vous dessinez généralement en taille réelle. Un mètre est un mètre. Assurez-vous de configurer vos [unités de travail](Units/fr.md) à votre convenance. Utilisez également les [outils d\'aimantation](Draft_Snap/fr.md) pour positionner vos points avec précision.

Vous pouvez regrouper vos objets en utilisant des [groupes](Std_Group/fr.md) ou des [calques](Draft_Layer/fr.md). Les calques sont simplement des groupes qui peuvent contrôler la couleur et d\'autres aspects des objets qui y sont placés.

Lorsque votre dessin est prêt à être exporté, il vous suffit de sélectionner tout ce que vous souhaitez exporter (ou les groupes/calques qui les contiennent) et d\'utiliser le menu Fichier -\> Exporter puis de choisir le format DXF ou DWG. Notez que les possibilités DWG de FreeCAD dépendent d\'un [logiciel externe](Draft_DXF/fr#DWG.md).

Pour imprimer ou exporter votre dessin sous forme de fichier PDF, vous utilisez l\'[atelier TechDraw](TechDraw_Workbench/fr.md). TechDraw est utilisé pour créer des feuilles imprimables, y placer des modèles et d\'autres éléments graphiques, ainsi que des vues de vos modèles 2D ou 3D. Un flux de travail typique avec Draft et TechDraw se compose de :

1.  Définissez votre plan de travail comme étant le plan XY (supérieur)
2.  Créez votre dessin à l\'aide des outils de Draft
3.  Veillez à regrouper tous les composants de votre dessin dans des groupes ou des calques, et à avoir un groupe racine ou un conteneur de calques qui contient tous les calques ou sous-groupes de votre dessin. Il est ainsi plus facile de le placer en une seule fois sur une feuille. En règle générale, vous créez un groupe différent pour chaque dessin, afin de pouvoir contrôler leur position et leur échelle de manière indépendante sur la feuille.
4.  Passez à l\'atelier TechDraw
5.  Créez une nouvelle page
6.  Définissez ou ajustez votre modèle de page
7.  Pour chacun de vos dessins sous Draft, utilisez l\'outil [vue de Draft](TechDraw_DraftView/fr.md) pour en créer une vue sur la feuille
8.  Ajustez l\'échelle et la position de chaque vue
9.  Imprimez ou sauvegardez la feuille en tant que fichier PDF à partir du menu TechDraw

Voici plus d\'informations sur le dessin et le dessin 2D dans FreeCAD :

-   Tous les outils de l\'[atelier Draft](Draft_Workbench/fr.md).
-   Tutoriel : [Manuel : Dessin 2D traditionnel](Manual:Traditional_2D_drafting/fr.md)
-   Tutoriel : [Tutoriel Draft](Draft_tutorial/fr.md)
-   Tutoriel : [Sketcher : Tutoriel d\'introduction](Basic_Sketcher_Tutorial/fr.md). Sketcher peut être utilisé pour créer des éléments 2D beaucoup plus complexes et avancés que ce que vous pouvez faire dans Draft



## J\'ai une certaine expérience avec Revit ou ArchiCAD ou une autre application BIM. Je veux faire de la modélisation BIM 

L\'atelier de votre choix est le [atelier BIM](BIM_Workbench/fr.md). Il ne fait pas partie des ateliers intégrés à FreeCAD, vous devez l\'installer via le [gestionnaire des extensions](Std_AddonMgr/fr.md). L\'[atelier Arch](Arch_Workbench/fr.md), fourni avec FreeCAD, est un sous-ensemble minimal des outils de l\'atelier BIM, qui permettra à vos modèles BIM d\'être correctement ouverts sur n\'importe quelle installation de FreeCAD, même sans l\'atelier BIM.

L\'atelier BIM contient tous les outils que l\'on trouve habituellement dans les applications BIM pour modéliser les éléments de construction, tels que mur, fenêtre, porte, etc. Il contient également la plupart des [Outils de Draft](Draft_Workbench/fr.md) et utilise le même concept de [plan de travail](Draft_SelectPlane/fr.md) où vos prochains objets se trouveront sur le plan de travail en cours.

Il n\'y a pas d\'organisation stricte de structure de bâtiments (ex. étages) dans FreeCAD. Vous pouvez choisir de grouper vos objets BIM par [groupes](Std_Group/fr.md) ou par [calques](Draft_Layer/fr.md), comme dans Draft, mais vous pouvez aussi utiliser l\'objet [Partie de bâtiment](Arch_BuildingPart/fr.md) pour représenter des niveaux ou des bâtiments, et obtenir une organisation similaire à celle que l\'on trouve habituellement dans d\'autres applications BIM.

La plupart des outils BIM, tels que les murs et les fenêtres, créent eux-mêmes un objet en sélectionnant des options dans le panneau des tâches et en cliquant sur des points dans la vue 3D, mais ils peuvent également fonctionner en sélectionnant d\'autres objets au préalable. Par exemple, vous pouvez dessiner un mur en sélectionnant l\'outil Mur puis en cliquant sur deux points. Vous pouvez également commencer par dessiner une ligne ou une polyligne, puis, une fois cet objet sélectionné, appuyer sur le bouton Mur. Un mur sera construit au-dessus de cette polyligne et l\'utilisera comme ligne de base. Si vous modifiez la polyligne, le mur sera modifié en conséquence.

Les différents outils BIM tels que mur, fenêtre, colonne, etc\... produiront un objet mur, fenêtre ou colonne correspondant. Cependant, le type de l\'objet produit est défini par et seulement par sa propriété **IFC type**, qui peut être modifiée à tout moment. Vous pouvez donc utiliser l\'outil Mur pour modéliser une poutre par exemple. Il suffit de changer son type IFC de \"wall\" à \"beam\" par la suite.

De même, tout objet créé avec un autre atelier ou même une autre application peut devenir un objet BIM. En utilisant l\'outil [Composant](Arch_Component/fr.md), vous pouvez ajouter des propriétés BIM (y compris la propriété IFC Type) à n\'importe quel autre objet.

Après avoir créé un modèle BIM, qui n\'est rien d\'autre qu\'un modèle 3D dans lequel tous les objets ont des propriétés BIM/IFC définies, vous pouvez effectuer plusieurs opérations telles que :

-   L\'exporter au [format IFC](Arch_IFC/fr.md) en sélectionnant le conteneur racine de votre modèle (groupe ou partie de bâtiment) et en cliquant sur le menu Fichier -\> Exporter et en sélectionnant IFC. Le format IFC est le format d\'échange standard pour les modèles BIM et est pris en charge par toutes les applications BIM.
-   Extraire des dessins 2D tels que des plans d\'étage, des sections ou des élévations. Pour ce faire, placez des [plans d\'élévation](Arch_SectionPlane/fr.md) dans votre modèle.
-   Créer des dessins à partir de ces plans d\'élévation. Ceci est fait soit (et de préférence) en tant qu\'étape intermédiaire, en utilisant l\'outil [Vue 2D d\'une forme](Draft_Shape2DView/fr.md), qui peut ensuite être annoté avec les outils de Draft ou directement placé sur une feuille TechDraw en utilisant l\'outil [Vue d\'un objet Arch](TechDraw_ArchView/fr.md).
-   Créer des plannings ou des tableaux de quantités en utilisant l\'outil [Nomenclature](Arch_Schedule/fr.md) et l\'[atelier Spreadsheet](Spreadsheet_Workbench/fr.md).
-   Exporter votre modèle vers une autre application pour créer des rendus 3D, telle que [Blender](https://blender.org). Cela se fait généralement en sélectionnant les objets que vous souhaitez exporter, puis en utilisant le menu Fichier -\> Exporter et en choisissant un format bien supporté par ces applications, tel que OBJ ou DAE. Notez qu\'il existe un [Importateur de FreeCAD](https://gist.github.com/yorikvanhavre/e873d51c8f0e307e333fe595c429ba87) disponible pour Blender, qui lui permet d\'ouvrir directement des fichiers FreeCAD.

Voici plus d\'informations sur la modélisation BIM dans FreeCAD :

-   Les outils de l\'[atelier BIM](BIM_Workbench/fr.md)
-   Les tutoriels : [Architecture et BIM](Tutorials/fr#Architecture_et_BIM.md)



## Je n\'ai aucune idée précise de ce que je veux faire. Je veux juste explorer FreeCAD 

La meilleure façon de procéder est probablement de parcourir le [Manuel FreeCAD](Manual:Introduction/fr.md). Le manuel est conçu comme une séquence de chapitres progressifs et imprimables qui vous guidera doucement à travers tout ce qu\'il y a à savoir sur FreeCAD.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Which workbench should I choose/fr
