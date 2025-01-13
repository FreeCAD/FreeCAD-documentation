# Manual:Preparing models for 3D printing/fr
{{Manual:TOC}}

L\'un des principaux objectifs de FreeCAD est de concevoir des objets qui peuvent être transformés en produits physiques réels. Ces conceptions peuvent être partagées avec d\'autres pour la fabrication ou, de plus en plus, exportées directement vers des [imprimantes 3D](https://fr.wikipedia.org/wiki/Impression_3D) ou des [fraiseuses à commande numérique et machines à commande numérique](https://fr.wikipedia.org/wiki/Fraisage) pour une fabrication automatisée. Avec FreeCAD, vous pouvez créer des modèles précis et détaillés qui sont prêts pour diverses méthodes de production. Ce chapitre vous guidera dans le processus de préparation de vos modèles pour ces machines, en vous assurant qu\'ils répondent aux spécifications nécessaires pour une fabrication réussie, que vous travailliez avec une équipe ou que vous gériez l\'ensemble du processus vous-même.

Si vous avez été soigneux lors de la modélisation, la plupart des défis associés à l\'impression 3D de votre modèle devraient déjà être minimisés. Les principaux aspects sur lesquels il faut se concentrer sont les suivants :

-   **S\'assurer que vos objets sont solides** : tout comme les objets du monde réel, vos modèles 3D doivent être solides. FreeCAD, en particulier avec l\'atelier PartDesign, vous aide à vous assurer que vos modèles restent solides tout au long du processus de conception. Le logiciel vous avertit si une opération compromet la solidité de l\'objet. En outre, l\'atelier Part propose l\'outil <img alt="" src=images/Part_CheckGeometry.svg  style="width:16px;"> [Vérifier la géométrie](Part_CheckGeometry/fr.md), qui vous permet d\'identifier les défauts potentiels ou les problèmes susceptibles d\'interférer avec le processus d\'impression 3D.

-   **Confirmation de l\'exactitude des dimensions** : la précision est essentielle. Ce que vous concevez dans FreeCAD se traduira directement par des mesures dans le monde réel. Un millimètre dans FreeCAD est un millimètre dans l\'objet physique, c\'est pourquoi chaque dimension doit être soigneusement étudiée et vérifiée pour en garantir l\'exactitude.

-   **Gestion de la dégradation** : il est important de se rappeler qu\'aucune imprimante 3D ou machines à commande numérique ne peut traiter directement les fichiers FreeCAD. Ces machines utilisent le G-Code, un langage machine avec différents dialectes en fonction de la machine ou du fournisseur. Le processus de conversion de votre modèle en G-Code peut souvent être effectué automatiquement par un logiciel de slicer, mais vous avez également la possibilité de le faire manuellement pour un meilleur contrôle. Cependant, au cours de cette conversion, une certaine perte de détails ou de qualité est inévitable, en particulier lors de la conversion du modèle en un format de maillage pour l\'impression. Vous devez vous assurer que cette dégradation reste dans des limites acceptables et n\'affecte pas la fonctionnalité ou l\'apparence de votre objet final.

-   **Compatibilité des formats d\'exportation** : pour l\'impression 3D, le format STL est le plus couramment utilisé, mais il convertit intrinsèquement votre modèle en un maillage de triangles, ce qui peut entraîner une perte de détails. Il est essentiel de choisir la bonne résolution lors de l\'exportation vers STL, en trouvant un équilibre entre la conservation des détails et la taille du fichier. De même, pour l\'usinage CNC, des formats comme STEP ou IGES sont préférables car ils conservent mieux que STL l\'intégrité géométrique originale de la conception. Le choix du bon format garantit la précision de la conversion en G-Code.

-   **Analyse et étalonnage du maillage** : avant d\'exporter votre modèle vers un slicer ou un générateur de parcours d\'une CNC, il est conseillé d\'effectuer une analyse de maillage à l\'aide de l\'[atelier Mesh](Mesh_Workbench/fr.md) de FreeCAD afin de détecter les irrégularités, les arêtes non pliables ou d\'autres problèmes de maillage qui pourraient compliquer le processus de fabrication. En outre, même avec un modèle parfait, assurez-vous que votre imprimante 3D ou votre machine CNC est correctement calibrée (par exemple, pour le nivellement du lit, les réglages du moteur pas à pas ou la configuration de l\'extrudeuse) afin d\'éviter les problèmes de qualité dans le produit final.

Dans les sections suivantes, nous supposerons que vous avez déjà pris soin de créer des modèles solides aux dimensions correctes. Nous allons maintenant nous concentrer sur la gestion du processus de conversion en G-Code, en veillant à ce que votre modèle conserve la qualité nécessaire pour l\'impression 3D ou l\'usinage CNC. En tenant compte de ces considérations, vous serez mieux équipé pour produire des objets physiques réussis directement à partir de vos modèles FreeCAD.



### Exporter vers les slicers 

La technique la plus courante pour préparer un modèle 3D à l\'impression consiste à exporter l\'objet 3D de FreeCAD vers un logiciel spécialisé appelé « slicer ». Le slicer génère du G-code en découpant le modèle en fines couches, que l\'imprimante 3D suivra pour construire l\'objet couche par couche. Étant donné que de nombreuses imprimantes 3D, en particulier les modèles fabriqués à la maison ou par des amateurs, ont des configurations uniques, les programmes de slicer offrent un large éventail de paramètres avancés. Ces réglages vous permettent de personnaliser des paramètres clés, tels que la hauteur des couches, la vitesse d\'impression, la densité de remplissage et les structures de support, afin que le G-code soit adapté aux caractéristiques et aux capacités spécifiques de votre imprimante.

De nombreux slicers offrent également des fonctions de simulation et de validation de l\'impression qui sont très utiles pour prévisualiser le processus d\'impression. Vous pouvez visualiser le parcours de l\'outil pour chaque couche, ce qui permet de détecter les problèmes potentiels tels que les surplombs qui peuvent nécessiter des supports ou les zones où le refroidissement peut être insuffisant. Cette validation avant impression garantit que votre modèle est correctement préparé avant le début de l\'impression, ce qui permet d\'éviter les échecs d\'impression ou le gaspillage de matériau.

Les slicers incluent souvent des informations supplémentaires, telles que l\'estimation du temps d\'impression, de l\'utilisation des matériaux et du coût en fonction du filament ou de la résine utilisés. Cela vous permet de prendre des décisions éclairées sur le processus d\'impression et d\'ajuster les paramètres dans un souci d\'efficacité ou de conservation des matériaux. Bien que les subtilités de l\'impression 3D, telles que l\'étalonnage de la machine, la sélection des matériaux et le post-traitement, dépassent le cadre de ce guide, nous nous concentrerons sur la manière d\'exporter correctement votre modèle FreeCAD et d\'utiliser le logiciel de slicer pour s\'assurer que le résultat est correct et optimisé pour votre imprimante spécifique.



### Convertir des objets en maillage 

Aucun des slicers actuellement disponibles ne peut accepter directement la géométrie solide produite dans FreeCAD. Les slicers comme Cura et PrusaSlicer travaillent avec des formats basés sur des [maillages](https://fr.wikipedia.org/wiki/Maillage_polygonal) tels que STL, OBJ ou 3MF, qui représentent la géométrie de la surface de l\'objet à l\'aide d\'un réseau de triangles. Par conséquent, pour utiliser un modèle créé dans FreeCAD, il faut d\'abord le convertir dans un format de maillage que ces slicers peuvent interpréter.

Le format le plus couramment utilisé pour l\'impression 3D est le STL. L\'une des raisons pour lesquelles le STL est privilégié est sa simplicité : il représente la géométrie 3D sous la forme d\'un maillage de triangles sans inclure de détails complexes tels que les couleurs, les matériaux ou les textures. Cette approche minimaliste garantit la légèreté des fichiers STL et leur compatibilité avec la quasi-totalité des slicers et des imprimantes 3D, ce qui en fait le standard de l\'industrie. Les fichiers OBJ et 3MF sont également pris en charge, mais ils peuvent contenir des informations supplémentaires telles que des textures et des matériaux, qui sont inutiles pour la plupart des tâches d\'impression 3D et peuvent compliquer le processus de découpage.

Heureusement, la conversion d\'un objet solide en maillage dans FreeCAD est simple, même si la reconversion d\'un maillage en solide est une opération plus compliquée. Au cours du processus de conversion, il est essentiel de garder à l\'esprit qu\'une certaine dégradation de la qualité du modèle peut se produire, en particulier lors de la réduction d\'une géométrie complexe en un simple maillage triangulaire. Vous devez vous assurer que cette dégradation reste dans des limites acceptables pour maintenir la précision de votre objet imprimé.

Dans FreeCAD, l\'[atelier Mesh](Mesh_Workbench/fr.md) gère toutes les tâches liées au maillage. Cet atelier contient des outils non seulement pour la conversion entre les objets Part et Mesh, mais aussi pour l\'analyse et la réparation des maillages. Bien que la manipulation des maillages ne soit pas l\'objectif principal de FreeCAD, elle devient essentielle lors de la préparation des modèles pour l\'impression 3D. Les objets Mesh sont largement utilisés dans d\'autres applications, et l\'atelier Mesh vous permet de gérer et d\'ajuster entièrement ces objets, en veillant à ce qu\'ils soient prêts pour l\'étape suivante du processus d\'impression.

-   Convertissons la pièce Lego que nous avons créée dans le dernier chapitre en un maillage STL. La géométrie peut être téléchargée à la fin de ce chapitre.
-   Ouvrez le fichier FreeCAD contenant la pièce Lego.
-   Passez à l\'[atelier Mesh](Mesh_Workbench/fr.md)
-   Sélectionnez la brique Lego
-   Sélectionnez le menu **Maillages → Créer un maillage à partir d\'une forme**.
-   Un panneau de tâches s\'ouvre avec plusieurs options. Certains algorithmes de maillage supplémentaires (Mefisto ou Netgen) peuvent ne pas être disponibles, en fonction de la façon dont votre version de FreeCAD a été compilée. L\'algorithme de maillage Standard sera toujours présent. Il offre moins de possibilités que les deux autres, mais est tout à fait suffisant pour les petits objets qui entrent dans la taille d\'impression maximale d\'une imprimante 3D.

<img alt="" src=images/FreeCAD_MeshLego.png  style="width:600px;">

-   Sélectionnez le maillage **standard** et laissez la valeur de déviation à la valeur par défaut de **0.10**. Appuyez sur **OK**.
-   Un objet mesh sera créé, exactement par dessus notre objet solide. Pour comparer les deux vous pouvez soit cacher le solide, soit déplacer l\'un des objets par rapport à l'autre.
-   Modifiez la propriété **Affichage → Style de représentation** du nouvel objet maillage en **Filaire ombré** afin de voir comment s\'est déroulée la triangulation.
-   Si vous n\'êtes pas satisfait et pensez que le résultat est trop grossier, vous pouvez répéter l'opération, en abaissant la valeur de déviation. Dans l\'exemple ci-dessous, le maillage gauche a utilisé la valeur par défaut de **0.10**, tandis que celui de droite utilise **0.01** :

<img alt="" src=images/Exercise_meshing_02.jpg  style="width:600px;">

Dans la plupart des cas, les valeurs par défaut donneront un résultat satisfaisant.

-   Nous pouvons maintenant exporter notre maillage à un format de maillage, par exemple [STL](https://fr.wikipedia.org/wiki/Fichier_de_st%C3%A9r%C3%A9olithographie), actuellement le format le plus utilisé dans l\'impression 3D, en utilisant le menu **Fichier → Exporter** et choisir le format de fichier STL.

Dans FreeCAD, l\'atelier Mesh propose plusieurs algorithmes pour convertir un modèle solide en maillage, notamment Standard, Mefisto, Netgen et Gmsh. L\'algorithme Standard est couramment utilisé pour les objets de petite et moyenne taille, car il offre un équilibre entre la vitesse et la qualité du maillage. Lors de la création d\'un maillage, deux paramètres essentiels sont l\'écart de surface et l\'écart angulaire. L\'écart de surface détermine dans quelle mesure le maillage suit la géométrie d\'origine. Des valeurs plus faibles permettent d\'obtenir un maillage plus fin et plus précis, mais peuvent entraîner une augmentation de la taille des fichiers. La déviation angulaire définit l\'ampleur de la déviation autorisée en fonction des changements d\'angle du modèle, en particulier pour les courbes et les arêtes vives. D\'autres options, telles que la déviation de surface relative, vous permettent d\'ajuster la précision de manière dynamique en fonction de l\'échelle du modèle, et des fonctions telles que l\'application de couleurs de face ou la définition de segments de maillage par couleur sont utiles pour le rendu avancé ou le regroupement de différentes régions du modèle. Une fois le maillage généré, il peut être exporté dans des formats tels que STL, OBJ ou 3MF, qui sont essentiels pour préparer les modèles à l\'impression 3D. La qualité du maillage est essentielle pour que les imprimantes 3D interprètent correctement le modèle. Le choix du bon algorithme de maillage et des paramètres de déviation peut donc avoir une incidence considérable sur le résultat final de l\'impression.



### Utiliser PrusaSlicer 

[PrusaSlicer](https://github.com/prusa3d/prusaslicer/releases) est une application qui convertit les objets STL, OBJ et 3MF en G-code qui peut être envoyé directement aux imprimantes 3D. Comme FreeCAD, il est gratuit, open-source et disponible sur Windows, Mac OS et Linux. Bien qu\'il soit développé par Prusa Research et optimisé pour les imprimantes 3D Prusa, PrusaSlicer peut être utilisé avec presque toutes les imprimantes 3D, ce qui le rend polyvalent pour une large gamme de machines. PrusaSlicer est basé sur Slic3r, le logiciel slicer original, mais avec des améliorations significatives et des mises à jour plus fréquentes. Slic3r n\'est plus activement mis à jour, tandis que PrusaSlicer continue d\'évoluer, ajoutant de nouvelles fonctionnalités telles que des hauteurs de couche adaptatives, des supports d\'arbre et des stratégies d\'impression améliorées.

Configurer correctement un slicer pour l\'impression 3D est un processus complexe qui nécessite une bonne compréhension des capacités de votre imprimante 3D. Bien que la génération de G-code sans cette connaissance puisse résulter en un fichier qui ne fonctionne pas bien sur d\'autres imprimantes, PrusaSlicer fournit toujours un excellent moyen de vérifier que votre fichier STL est correctement formaté et imprimable. Les fonctions de simulation du slicer vous permettent de prévisualiser les chemins du G-code et de vérifier tout problème d\'impression potentiel avant de commencer l\'impression réelle.

Voici notre fichier STL exporté, ouvert dans PrusaSlicer. En appuyant simplement sur le bouton **slice**, le logiciel divise votre modèle en couches, génère les parcours d\'outils pour l\'imprimante 3D et applique les paramètres de vitesse et de température nécessaires. Il calcule le remplissage, les structures de soutien et les périmètres, puis crée le G-code, qui contient des instructions détaillées pour l\'imprimante. Vous pouvez prévisualiser le modèle découpé couche par couche, vérifier le temps d\'impression estimé et l\'utilisation du filament, et enfin enregistrer ou envoyer le G-code à votre imprimante pour le processus d\'impression proprement dit.

<img alt="" src=images/FreeCAD_PrusaSlicer.png  style="width:600px;">

Outre PrusaSlicer, il existe plusieurs autres logiciels de découpe disponibles pour l\'impression 3D. [Cura](https://ultimaker.com/fr/software/ultimaker-cura/), développé par Ultimaker, est l\'un des slicers open-source les plus populaires et prend en charge une large gamme d\'imprimantes avec une personnalisation poussée. [Simplify3D](https://www.simplify3d.com/) est un slicer payant connu pour ses fonctionnalités avancées et sa génération efficace de parcours d\'outils. [MatterControl](https://www.matterhackers.com/store/l/mattercontrol/sk/MKZGTDW6) est un slicer open-source qui inclut également des outils de CAO de base, tandis que [IdeaMaker](https://www.raise3d.com/fr/ideamaker/) offre une interface conviviale avec des hauteurs de couche adaptatives, développée par Raise3D. Enfin, [OrcaSlicer](https://github.com/SoftFever/OrcaSlicer), une option open-source plus récente basée sur PrusaSlicer et Bambu Studio, offre des fonctionnalités supplémentaires pour diverses imprimantes. Chaque slicer possède des atouts uniques, ce qui fait que le meilleur choix dépend des modèles d\'imprimantes spécifiques et des exigences d\'impression.



### Générer du G-code 

L\'<img alt="" src=images/Workbench_CAM.svg  style="width:16px;"> [atelier CAM](CAM_Workbench/fr.md) de FreeCAD fournit des options avancées pour générer du G-code directement pour les machines CNC, offrant une plus grande flexibilité et un meilleur contrôle par rapport aux outils de découpage automatique tels que ceux utilisés pour l\'impression 3D. Alors que les slicers d\'impression 3D peuvent convertir automatiquement un modèle en G-code avec un minimum de données, le fraisage CNC nécessite une implication beaucoup plus importante de l\'utilisateur pour assurer un contrôle précis des parcours d\'outils, des vitesses, des profondeurs et d\'autres paramètres d\'usinage. L\'atelier CAM est donc essentiel pour les tâches qui exigent un G-code précis, en particulier pour le fraisage CNC, où la complexité de la machine et la variété des opérations (comme la coupe, le perçage et le contournage) exigent une planification minutieuse.

Dans l\'atelier CAM, la génération de parcours en G-code est hautement personnalisable. Elle comprend des outils permettant de générer des parcours machine complets pour diverses opérations ou, au contraire, de construire des segments partiels de G-code et de les assembler pour obtenir une opération de fraisage complète. Cette approche modulaire vous permet de personnaliser chaque étape du processus d\'usinage, en optimisant les parcours d\'outils en fonction de l\'efficacité, du type de matériau et des capacités spécifiques de la machine.

Le processus de CAM est en effet beaucoup plus complexe que l\'impression 3D, car les machines à commande numérique utilisent des outils différents et doivent tenir compte de l\'enlèvement de matière, de la géométrie de l\'outil et des marges de sécurité, qui sont tous configurés manuellement. Dans FreeCAD, la construction d\'un projet CAM simple nécessite de définir des parcours d\'outils, d\'ajuster les profondeurs de coupe, de sélectionner les outils appropriés et de configurer les décalages, les avances et les vitesses de travail. Contrairement aux logiciels de slicer, qui gèrent la plupart de ces opérations automatiquement, l\'atelier CAM vous laisse le contrôle, ce qui le rend hautement personnalisable, mais aussi plus complexe.

Bien que la génération de parcours de fraisage CNC soit un sujet trop vaste pour être traité en détail ici, nous allons montrer comment créer un projet CAM simple dans FreeCAD. Bien que nous ne nous attarderons pas sur tous les détails de l\'usinage CNC dans le monde réel, ce guide vous présentera les étapes essentielles, en mettant l\'accent sur le niveau d\'entrée requis pour garantir des résultats précis et efficaces. Cette complexité supplémentaire est essentielle pour les projets CNC, où la précision et la personnalisation sont essentielles pour obtenir les résultats d\'usinage souhaités.

-   Chargez le fichier contenant notre pièce de Lego, et passez à l\'<img alt="" src=images/Workbench_CAM.svg  style="width:16px;"> [atelier CAM](CAM_Workbench/fr.md).
-   Appuyez sur le bouton <img alt="" src=images/CAM_Job.svg  style="width:16px;"> [Créer une tâche](CAM_Job/fr.md) et sélectionnez notre pièce de lego.
-   Comme cette section n\'a pas pour but de fournir un tutoriel approfondi de l\'atelier CAM, nous utiliserons les valeurs par défaut. Si vous souhaitez un tutoriel plus détaillé, veuillez vous référer à [CAM Tutoriel pas à pas pour l\'impatient](CAM_Walkthrough_for_the_Impatient/fr.md). Gardez à l\'esprit que dans l\'atelier de CAM, un corps pour le stock est automatiquement créé autour de votre objet, représentant la matière première qui sera usinée. Pour l\'instant, ce corps de stock s\'étend sur 1 mm dans toutes les directions à partir de l\'objet.

<img alt="" src=images/FreeCAD_CAM1.png  style="width:600px;">

-   La première étape consiste à supprimer les matériaux inutiles autour de notre objet. À ce stade, nous partons d\'un bloc solide de matériau brut et nous devons découper la brique de Lego à partir de ce bloc. Ce processus consiste à définir les parcours d\'outils qui découperont progressivement l\'excès de matière, en laissant derrière eux la forme souhaitée de la brique Lego.

-   L\'image suivante montre la configuration de l\'atelier CAM de FreeCAD pour l\'usinage d\'un bloc Lego. L\'arborescence du modèle comprend des opérations de modélisation solide telles que Protrusion, Cavité et Répétition linéaire, qui ont été utilisées pour façonner la pièce. Une tâche est créée, contenant des parcours d\'outils sous les opérations qui définissent la manière dont la matière sera enlevée du stock. L\'outil par défaut est sélectionné pour l\'usinage et le corps-modèle représente la pièce 3D sur laquelle on travaille. Cette configuration prépare l\'objet à la génération du G-code pour contrôler la CNC.

<img alt="" src=images/FreeCAD_CAMtree.png  style="width:600px;">

-   Avant de commencer à découper le matériau excédentaire, nous allons procéder à quelques ajustements de l\'outil de fraisage qui sera utilisé. Bien que l\'atelier CAM vous permette de définir des outils personnalisés, nous allons, pour des raisons de simplicité, modifier l\'outil par défaut. Ainsi, les paramètres seront optimisés pour notre projet sans qu\'il soit nécessaire de créer un nouvel outil à partir de zéro.

-   Cliquez sur le texte **TC:Outil par défaut**. Cela ouvrira l**\'éditeur du contrôleur d\'outil**. Modifiez les vitesses d\'avance et les vitesses de broche comme indiqué sur l\'image. Les vitesses d\'avance pour la coupe horizontale et verticale sont réglées sur 2000 mm/min, tandis que la vitesse de la broche est réglée sur 2000 RPM avec une rotation vers l\'avant. Ces paramètres contrôlent le mouvement et la vitesse de coupe de l\'outil pendant le processus d\'usinage.

<img alt="" src=images/FreeCAD_toolController.png  style="width:600px;">

-   Double-cliquez sur l\'outil lui-même et modifiez son diamètre à 1 mm.
-   Nous sommes maintenant prêts à retirer l\'excédent de matériau du bloc et à découper progressivement la géométrie Lego. Ce processus impliquera les parcours d\'outils que nous avons définis, afin de s\'assurer que la forme finale correspond à la conception prévue.
-   Cliquez sur l\'option <img alt="" src=images/CAM_Profile.svg  style="width:16px;"> [Profilage](CAM_Profile/fr.md). Cette option est utilisée pour découper le matériau inutile autour du périmètre de la pièce, en façonnant efficacement les limites extérieures pour obtenir les dimensions générales de la pièce Lego.
-   Normalement, vous n\'aurez pas à modifier les valeurs par défaut, à l\'exception du **Décalage supplémentaire** situé dans l\'onglet Opération. Réglez cette option à 1 mm pour vous assurer que l\'objet restant correspond correctement aux limites du Lego.
-   Une fois que vous avez appuyé sur **appliquer**, vous devriez être en mesure de voir ces lignes vertes autour de l\'objet. Ces lignes visualisent le parcours que notre objet de découpe suivra lors de la découpe du bloc initial.

<img alt="" src=images/FreeCAD_CAMProfile.png  style="width:600px;">

-   L\'étape suivante consiste à créer les 6 cylindres extrudés sur la face supérieure du bloc Lego.
-   Choisissez la face supérieure et cliquez sur le bouton <img alt="" src=images/CAM_Pocket_Shape.svg  style="width:16px;"> [Créer une poche](CAM_Pocket_Shape/fr.md). Dans l\'onglet **Extensions**, activez les Extensions et cliquez sur le bord de la face supérieure (il devrait normalement être automatiquement ajouté dans la boîte de longueur par défaut.
-   Enfin, dans l\'onglet **Opération**, entrez -1.5 mm dans la case **Extension de passage** et changez l\'option de motif en Décalage du zigzag.
-   Appuyez sur **appliquer** et fermez l\'onglet.
-   De la même manière, nous pouvons créer les trois cylindres au bas de la pièce Lego.
-   Nous pouvons facilement visualiser les étapes suivies pendant le fraisage de l\'objet en utilisant l\'option <img alt="" src=images/CAM_SimulatorGL.svg  style="width:16px;"> [Simulateur GL](CAM_SimulatorGL/fr.md).

**Téléchargements**

-   Le fichier STL généré dans cet exercice: <https://github.com/yorikvanhavre/FreeCADmanual/Blob/master/files/lego.stl>
-   Le fichier généré lors de cet exercice: <https://github.com/yorikvanhavre/FreeCADmanual/Blob/master/files/path.FCStd>
-   Le fichier G-code généré dans cet exercice: <https://github.com/yorikvanhavre/FreeCADmanual/Blob/master/files/lego.gcode>

**Lire plus d\'informations**

-   [L'atelier Mesh](Mesh_Workbench/fr.md)
-   [Le format de fichier STL](https://en.wikipedia.org/wiki/STL_%28file_format%29)
-   [Slic3r](http://slic3r.org/)
-   [Cura](https://ultimaker.com/en/products/cura-software)
-   [L'atelier Cura](https://github.com/cblt2l/FreeCAD-CuraEngine-Plugin)
-   [L'atelier CAM](CAM_Workbench/fr.md)
-   [Camotics](http://camotics.org/)



### Vidéos

-   [Comment utiliser FreeCAD pour l\'impression 3D \| Utilisation de la branche Realthunder](https://www.youtube.com/playlist?list=PL6Fiih6ItYsWCE20KtUJYpiDPrCA2rVpN) Une playlist de vidéos par Maker Tales sur la façon d\'utiliser FreeCAD pour l\'impression 3D.



---
⏵ [documentation index](../README.md) > [CAM](Category_CAM.md) > [Mesh](Category_Mesh.md) > [Tutorials](Category_Tutorials.md) > Manual:Preparing models for 3D printing/fr
