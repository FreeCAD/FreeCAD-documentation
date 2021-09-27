# Thread for Screw Tutorial/fr
{{TutorialInfo/fr
|Topic= Conception de produit
|Level= Avancé
|Time= 60 minutes
|Author=_, _, vocx
|FCVersion=0.19
|Files=[https://forum.freecadweb.org/viewtopic.php?f=36&t=44668 Updated: Thread for screw tutorial]
}}

## Introduction

Ce tutoriel est un ensemble de techniques pour modéliser les filetages de vis dans FreeCAD. Il a été mis à jour pour la v0.19, bien que le processus global soit essentiellement le même depuis la v0.14, lorsque le didacticiel a été initialement écrit. Le contenu mis à jour se concentre sur l\'utilisation de l\'[atelier PartDesign](PartDesign_Workbench/fr.md) <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> pour créer le filetage et de nouvelles illustrations pour les méthodes 0 à 3.

Dans les systèmes de CAO traditionnels, la modélisation des filetages de vis est déconseillée car elle impose une charge importante sur le noyau de modélisation, ainsi que sur le rendu des formes. Dans les systèmes traditionnels, un fil n\'a pas besoin d\'être représenté directement dans l\'espace 3D, car il peut être indiqué avec ses caractéristiques requises dans le dessin technique 2D envoyé pour la fabrication. Cependant, avec la vulgarisation de la fabrication additive (impression 3D), il existe désormais un réel besoin de modéliser les fils 3D, afin de les imprimer exactement comme prévu. C\'est à cela que sert ce didacticiel.

De nombreuses techniques présentées ici ont été collectées à partir de différents fils de discussion :

-   [Gathering thread modeling techniques](https://forum.freecadweb.org/viewtopic.php?f=3&t=12593)
-   [Creating a thread: Unexpected results](https://forum.freecadweb.org/viewtopic.php?f=3&t=6506)

Voir aussi des vidéos utiles :

-   [Introducing a strategy for designing a bolt without the commonly found problems.](https://forum.freecadweb.org/viewtopic.php?f=8&t=44259)

N\'oubliez pas que les formes de filetages prennent beaucoup de mémoire et que le fait d\'avoir un seul filetage dans un document peut augmenter considérablement la taille du fichier, il est donc conseillé à l\'utilisateur de créer des filetages uniquement lorsque cela est absolument nécessaire.

## Méthode 0. Récupération depuis une bibliothèques d\'objets 

L\'utilisation de modèles créés par d\'autres personnes est facile et permet de gagner du temps. Voir la page des [ateliers externes](external_workbenches/fr.md) pour plus d\'informations sur les outils externes.

En particulier, il est recommandé d\'installer deux ressources à partir du [gestionnaire de modules complémentaires](Std_AddonMgr/fr.md) :

-   [Fasteners Workbench](https://github.com/shaise/FreeCAD_FastenersWB), pour placer des vis et des rondelles paramétriques conformes aux normes ISO. Les vis et écrous par défaut ne montrent pas de filetage, mais cela peut être contrôlé en cochant la case \"Treared\".

## Nota1

Certaines petites vis /écrou ou grosse n'ont pas de filetage prédéfini

-   [BOLTSFC](https://github.com/berndhahnebach/BOLTSFC), pour placer des pièces normalisées de la bibliothèque BOLTS, qui suivent aussi les normes ISO.

## Nota2

Une vis et un écrou de même diamètre nominal ne sont pas exactement identique il y a un jeu généralement H7/g6 , si on fabrique un écrou par soustraction d\'un barreau fileté , et une vis par soustraction d\'un écrou , ceux-ci ne se visseront pas dans l\'absolu , en fabrication en impression 3D et CNC précise

<img alt="" src=images/T13_00_Threads_fasteners.png  style="width:" height="300px;"> 
*Diverses vis au standard ISO insérées avec l'atelier Fasteners. Une option à cocher (Threared) contrôle si un objet affiche le vrai filetage ou juste un simple cylindre.*

## Méthode 1. Utilisation de macros (obsolète) 

Dans le passé, la [macro BOLTS](Macro_BOLTS.md) était utilisée pour insérer les pièces de la bibliothèque BOLTS. Ceci est désormais obsolète. Utilisez plutôt l\'atelier BOLTSFC. ou Fasteners

Dans le passé, la [ macro Screw Maker](Macro_screw_maker1_2/fr.md), écrite par ulrich1a, était utilisée pour créer des boulons, des vis et des rondelles individuelles. Ceci est désormais obsolète. L\'atelier Fasteners, de shaise, comprend la macro de vissage complète, ainsi qu\'une barre d\'outils pour sélectionner le bon composant.

## Méthode 2. Atelier Fasteners 

Utilisez l\'atelier externe [Fasteners](Fasteners_Workbench/fr.md) pour ajouter/fixer diverses fixations aux pièces. Cet atelier peut être installé avec le [Gestionnaire d\'Addons](Std_AddonMgr/fr.md).

## Méthode 3. Faux filetages non hélicoïdaux 

Dans de nombreux cas, nous n\'avons pas besoin de vrais filetages, nous avons juste besoin d\'une indication visuelle que les filetages seront là.

Nous pouvons créer un faux filetage en utilisant un chemin non hélicoïdal, par exemple en tournant un profil en dents de scie, ou en empilant des disques avec des bords effilés. Ce faux filetage est difficile à distinguer du vrai fil hélicoïdal par une simple inspection. Cette méthode est bonne pour visualiser un objet semblable à un filetage, mais elle n\'est pas utile si nous devons imprimer en 3D un fil réel.

<img alt="" src=images/T13_01_Threads_comparison_fake_real.png  style="width:" height="300px;"> 
*A gauche : un simple boulon avec un faux filetage non hélicoïdal. A droite : un simple boulon avec un vrai filetage hélicoïdal. Lorsque l'impression 3D n'est pas nécessaire, un filetage simulé est souvent suffisant pour la visualisation.*

### Profil tournant en dents de scie 

1.  Cliquer sur **<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Body](PartDesign_Body.md)**.
2.  Cliquer sur **<img src=images/PartDesign_NewSketch.svg style="width:16px"> [PartDesign Nouvelle esquisse](PartDesign_NewSketch.md)**. Sélectionnez {{Value|XZ_Plane}}.
3.  Dessinez un croquis fermé avec le diamètre intérieur requis {{Value|10 mm}}, le diamètre extérieur autour de {{Value|12.6 mm}}, le pas {{Value|3 mm}}, le nombre de dents {{Value|8}} et la hauteur totale {{Value|30 mm}}.
4.  Sélectionnez l\'esquisse, puis cliquez sur **<img src=images/PartDesign_Revolution.svg style="width:16px"> [PartDesign Revolution](PartDesign_Revolution.md)**. Sélectionnez {{Value|Vertical sketch axis}} et appuyez sur **OK**.

<img alt="" src=images/T13_02_Threads_Sawtooth_sketch_profile.png  style="width:" height="300px;"> 
*Profil utilisé pour créer la révolution qui simulera un filetage.*

<img alt="" src=images/T13_03_Threads_Sawtooth_revolution_1.png  style="width:" height="300px;"> <img alt="" src=images/T13_04_Threads_Sawtooth_revolution_2.png  style="width:" height="300px;"> 
*Vue en coupe du filetage non hélicoïdal résultant produit par rotation du profil en dents de scie autour de l'axe vertical.*

### Disques empilables 

1.  Répétez les deux premières étapes de la section précédente.
2.  Dessinez une esquisse fermée avec le diamètre intérieur requis {{Value|10 mm}}, le diamètre extérieur de {{Value|12.6 mm}} et le pas {{Value|3 mm}} mais dessinez qu\'une seule dent de la dent de scie.
3.  Sélectionnez l\'esquisse, puis cliquez sur **<img src=images/PartDesign_Revolution.svg style="width:16px"> [PartDesign Révolution](PartDesign_Revolution/fr.md)**. Sélectionnez {{Value|Vertical sketch axis}} puis appuyez sur **OK**.
4.  Sélectionnez {{Value|Revolution}} puis cliquez sur **<img src=images/PartDesign_LinearPattern.svg style="width:16px"> [PartDesign Répétition linéaire](PartDesign_LinearPattern/fr.md)**. Sélectionnez {{Value|Vertical sketch axis}}. Pour un faux filetage avec un pas de {{Value|3 mm}}, définissez **Length** sur {{Value|3}} et **Occurrences** sur {{Value|2}} puis appuyez sur **OK**. Cela créera deux disques, l\'un au-dessus de l\'autre.
5.  Vous pouvez ajouter plus de disques en augmentant la valeur **Occurrences** dans la répétition linéaire et en augmentant la **Length** qui est la longueur totale du faux filetage.


**Length**

et **Occurrences** sont liés. Si la longueur est trop grande mais que le nombre d\'occurrences n\'est pas assez élevé, vous aurez des disques déconnectés et le calcul du Corps (Body) échouera car l\'objet résultant doit toujours être un [un seul solide contigu](PartDesign_Body/fr.md). Par exemple, pour obtenir une hauteur totale de {{Value|30 mm}}, définissez **Length** sur {{Value|27 mm}} et **Occurrences** sur {{Value|10}}.

Si vous le souhaitez, vous pouvez ajouter un **<img src=images/PartDesign_AdditiveCylinder.svg style="width:16px"> [PartDesign Cylindre additif](PartDesign_AdditiveCylinder/fr.md)** avec un diamètre égal au diamètre intérieur des disques et aussi haut que la hauteur totale du filetage. Cela réunira tous les disques en un seul solide, garantissant ainsi qu\'il n\'y aura pas de disques déconnectés.

<img alt="" src=images/T13_05_Threads_Stacked_discs_sketch.png  style="width:" height="300px;"> 
*Profil utilisé pour créer un disque de révolution qui sera utilisé pour simuler un filetage.*

<img alt="" src=images/T13_06_Threads_Stacked_discs_1.png  style="width:" height="300px;"> <img alt="" src=images/T13_07_Threads_Stacked_discs_2.png  style="width:" height="282px;"> 
*A gauche: disque unique créé par révolution. A droite: plusieurs disques placés dans un motif linéaire dans la direction Z simulant un filetage hélicoïdal.*

## Méthode 4. Balayage d\'un profil vertical 

### Atelier Part Design (Conception de pièces) 

Un vrai filetage consiste à faire suivre un profil fermé le long d\'une courbe hélicoïde (hélice)

1.  Dans l\'<img alt="" src=images/Workbench_Part.svg  style="width:24px;"> <img src=images/Part_Primitives.svg style="width:Atelier Part](Part_Workbench/fr.md), cliquez sur **[16px"> <img src=images/Part_Helix.svg style="width:Part Primitives](Part_Primitives/fr.md)** pour créer une **[16px"> [Part Hélice](Part_Helix/fr.md)**. Donnez-lui les valeurs appropriées pour le **Pas** {{Value|3 mm}}, la **Hauteur** {{Value|23 mm}} et un **Rayon** {{Value|10 mm}}.
2.  Basculez vers l\'<img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> <img src=images/PartDesign_Body.svg style="width:Atelier PartDesign](PartDesign_Workbench/fr.md) et cliquez sur **[16px"> [PartDesign Corps](PartDesign_Body/fr.md)**.
3.  Cliquez sur **<img src=images/PartDesign_NewSketch.svg style="width:16px"> [PartDesign Nouvelle esquisse](PartDesign_NewSketch/fr.md)**. Sélectionnez {{Value|XZ_Plane}}.
4.  Dessinez une esquisse fermée avec le profil requis pour les dents du filet, normalement une forme triangulaire. Dans ce cas, nous utiliserons une hauteur de {{Value|2.9 mm}}, qui est légèrement inférieure au pas {{Value|3.0 mm}} utilisé pour la trajectoire de l\'hélice. Le profil ne doit pas créer d\'auto-intersections lorsqu\'il est déplacé le long de l\'hélice, ni entre les corbures, ni au milieu. L\'esquisse présentée pour l\'empilement des disques ne peut donc pas être utilisée.
5.  Sélectionnez l\'esquisse, puis cliquez sur **<img src=images/PartDesign_AdditivePipe.svg style="width:16px"> [PartDesign Balayage additif](PartDesign_AdditivePipe/fr.md)**. Dans **Chemin le long duquel effectuer le balayage**, cliquez sur **Objet** et choisissez l\'objet hélice précédemment créé. Changez ensuite **Mode d'orientation** en {{Value|Frenet}} afin que le profil balaie la trajectoire sans se tordre, puis appuyez sur **OK**.
6.  Lorsque le dialogue demande une référence, choisissez {{Value|Créer une référence croisée}}.
7.  La bobine hélicoïdale est créée, mais il n\'y a ni corps central ni arbre.
8.  Cliquez sur **<img src=images/PartDesign_AdditiveCylinder.svg style="width:16px"> [PartDesign Cylindre additif](PartDesign_AdditiveCylinder/fr.md)** avec le **Rayon** approprié. {{Value|10 mm}} et **Hauteur** {{Value|29.9 mm}} pour toucher le reste du fil hélicoïdal et fusionner automatiquement avec lui.
9.  D\'autres opérations booléennes sont nécessaires pour façonner les extrémités abruptes de la bobine. Par exemple, vous pouvez utiliser des fonctions additives pour fournir une tête à la vis, et une pointe.

<img alt="" src=images/T13_08_Threads_Helical_thread_profile.png  style="width:" height="300px;"> <img alt="" src=images/T13_09_Threads_Helical_thread_path.png  style="width:" height="300px;"> A gauche : le profil de filet ; à droite l\'helice pour créer le chemin

<img alt="" src=images/T13_10_Threads_Helical_thread_coil.png  style="width:" height="300px;"> <img alt="" src=images/T13_11_Threads_Helical_thread_coil_sliced.png  style="width:" height="300px;"> A gauche le filet résultant , à droite la section

<img alt="" src=images/T13_12_Threads_Helical_thread_cylinder.png  style="width:" height="300px;"> <img alt="" src=images/T13_13_Threads_Helical_thread_finished.png  style="width:" height="300px;"> A gauche le filet est fusionner à la tige de vis ; à droite des élément sont ajoutés pour créer une vis

### Atelier Part (Pièces) 

Ce processus peut également être effectué à l\'aide des outils de l\'[Atelier Part](Part_Workbench/fr.md).

1.  Dans l\'<img alt="" src=images/Workbench_Part.svg  style="width:24px;"> <img src=images/Part_Primitives.svg style="width:Atelier Part](Part_Workbench/fr.md), cliquez sur **[16px"> <img src=images/Part_Helix.svg style="width:Part Primitives](Part_Primitives/fr.md)** pour créer une **[16px"> [Part Hélice](Part_Helix/fr.md)**. Donnez-lui les valeurs appropriées pour le **Pas** {{Value|3 mm}}, la **Hauteur** {{Value|23 mm}} et le **Rayon** {{Value|10 mm}}.
2.  Dans ce cas, vous n\'avez pas besoin d\'un **<img src=images/PartDesign_Body.svg style="width:16px"> <img src=images/Sketcher_NewSketch.svg style="width:PartDesign Corps](PartDesign_Body/fr.md)**. Passez à l\'<img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Atelier Sketcher](Sketcher_Workbench/fr.md), puis cliquez sur **[16px"> [Sketcher Nouvelle esquisse](Sketcher_NewSketch/fr.md)** et choisissez le plan global XZ.
3.  Ensuite, retournez dans l\'<img alt="" src=images/Workbench_Part.svg  style="width:24px;"> <img src=images/Part_Sweep.svg style="width:Atelier Part](Part_Workbench/fr.md) et utilisez **[16px"> [Part Balayage](Part_Sweep/fr.md)**.
4.  Sélectionnez l\'esquisse appropriée dans **Profil disponible** et cliquez sur la flèche pour la faire passer dans **Profils sélectionnés**.
5.  Cliquez sur **Chemin de balayage** et choisissez toutes les arêtes de l\'hélice existante dans la [vue\_3D](3D_view/fr.md). Cliquez sur **Fait**.
6.  Assurez-vous de cocher {{CheckBox|TRUE|Créer un solide}} et {{CheckBox|TRUE|Frenet}}. L\'obtention d\'un solide est la clé pour pouvoir effectuer des [Part Opérations booléennes](Part_Boolean/fr.md) avec la bobine résultante, sinon seule une surface sera produite.
7.  Cliquez sur **OK** pour quitter le dialogue et créer la bobine.

Vous pouvez maintenant ajouter d\'autres primitives comme des **<img src=images/Part_Cylinder.svg style="width:16px"> <img src=images/Part_Fuse.svg style="width:Part Cylindres](Part_Cylinder/fr.md)** ou d\'autres formes, afin d\'exécuter des **[16px"> <img src=images/Part_Cut.svg style="width:Part Unions](Part_Fuse/fr.md)** et des **[16px"> [Part Soustractions](Part_Cut/fr.md)** pour terminer la construction de la vis.

<img alt="" src=images/T13_14_Threads_components.png  style="width:" height="300px;"> <img alt="Création d\'un filer par balayage sur un profil vertical. 1 - le profil (un [sketch" src=images/Sketcher_Workbench/fr.md)). 2 - chemin de balayage ([Hélice](Part_Helix/fr.md)). 3 - résultat du balayage ([Balayage](Part_Sweep/fr.md))](thread-by-vertical-profile.png  style="width:500px;">

### Les clés du succès 

Lors de la génération du filet , les bords ne doivent pas se toucher (selfIntersection) faire la hauteur du profil plus petit que le pas : 0.01mm est suffisent

<img alt="" src=images/T13_15_Threads_self_intersection.png  style="width:" height="300px;"> <img alt="" src=images/T13_16_Threads_no_self_intersections_OK.png  style="width:" height="300px;"> Règle 1. le balayage ne doit pas s\'intersecter lui même. Un balayage qui s\'intersecte n\'est pas un solide valide. Les tentatives de fusion ou de soustraction échoueront très certainement. Cependant, pour de l\'impression 3D ou des besoins de visualisation, il peut être suffisant de laisser le filet et le cylindre non fusionné (s\'intersectant).

Le cylindre et le bord interieur du filet ne doivent pas être exactement tangent (coplanaire) 0.01mm est suffisent cet inconvénient n\'est visible parfois que une ou deux opérations booléenne suivante

<img alt="" src=images/T13_17_Threads_tangent_faces.png  style="width:" height="300px;"> <img alt="" src=images/T13_18_Threads_no_tangent_faces_OK.png  style="width:" height="300px;"> Règle 2. Rappelez vous que dans FreeCAD, l\'hélice est imprécise. Ainsi, un cylindre créé pour se superposer précisément avec un filet risquera de ne pas fusionner avec ce dernier. En général, évitez les géométrie coïncidente avec les éléments d\'un balayage, comme les faces tangentes, les arrêtes tangentes à des faces auxquelles elles ne sont pas connectées, les arrêtes coïncidentes et tangentes, etc\...

Le cylindre a une ligne génératrice , la face du profil du filet ne doit pas être dans le même plan , tourner le cylindre de quelque dégrés suffit , mais c\'est souvent plus simple de crée le profil sur un autre plan que XOZ qui est toujours le plan de génération d\'un cylindre

Astuce 1. Le rayon d\'une hélice n\'influe pas (à moins que l\'hélice ne soit conique). Tout ce qui compte est le pas et la hauteur de l\'hélice. Cela implique qu\'il est possible d\'utiliser une hélice générique pour fabriquer de nombreux filetages de même pas et de diamètre différent.

Astuce 2. Gardez l\'hélice courte (avec peu de tours). Les longs filetages ont tendance à faire échouer les opérations booléennes. Pensez plutôt à empiler des filetages courts pour en faire un long en utilisant [Draft Array](Draft_Array/fr.md) si vous rencontrez ce genre de situation problématique , en vérifiant de bien utiliser comme valeur de déplacement le même que le pas de l\'hélice , sur une vis celà se voit , dans un trou , ça peu passer inaperçu et causer problème dans un trou taraudé imprimer 3D

Pour une impression 3D on peu ne pas fusionner la pièce et le filet , celà diminurat la taille du fichier , mais attention de bien sélectionner les 2 pour faire le STL

### Avantages et inconvénients 

-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> Facile à comprendre.
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> Manière très naturelle de définir un profil de filetage.
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> Aucun problème avec le maillage de l\'objet résultant, contrairement à la méthode 4.

-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> En raison de l\'invalidité des balayages auto-entrecroisés, il est presque impossible de générer un filetage sans espace entre chaque dent, c\'est-à-dire sans face cylindrique droite sur les côtés intérieurs du filetage.
-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> Les opérations booléennes sont nécessaires pour obtenir un solide solide contigu. Les opérations booléennes prennent un temps relativement long à calculer et échouent souvent.
-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> Filetages avec un nombre élevé de tours sont problématiques.

## Méthode 5. Balayage d\'un profil horizontal 

### Généralités

L\'idée est de balayer un profil horizontal le long d\'une hélice. Le problème principal est de déterminer le profil à utiliser pour obtenir un tel filetage.

<img alt="" src=images/thread-by-horz-profile.png  style="width:600px;">

Si on utilise un cercle en guise de profil horizontal (le cercle doit être décentré par rapport à son origine, ce décentrage définissant la profondeur du filetage), le profil du filetage sera sinusoïdal.

Pour obtenir un profil standard en dent de scie, une paire de spirale d'Archimède doivent être fusionnées. La figure résultante est une forme cardioïde, qui est difficilement différentiable d\'un cercle quand la profondeur du filet est faible comparée à son diamètre (c\'est pourquoi un filetage \"épais\" est présenté sur la figure ci dessus).

### Génération du profil 

Se représenter ce que doit être le profil horizontal pour obtenir un profil vertical n\'est pas facile. Dans les cas simples comme les filets triangulaires ou trapézoïdale, cela peut être fait manuellement. Autrement, Il peuvent être créé en fabricant un filetage court avec la méthode 3, et en récupérant une tranche de ce dernier en faisant une [intersection](Part_Common/fr.md) entre le plan horizontal et le filet.

#### Profil pour un filetage triangulaire 

1.  Créer une spirale (d'Archimède) dans le plan XY.
    1.  fixer le nombre de tours à 0.5.
    2.  fixer le rayon du rayon interne du filetage, le rayon externe sera ce dernier plus la profondeur de coupe.
    3.  fixer la croissance pour doubler la profondeur de coupe du filet.
2.  [Part Mirroir](Part_Mirror/fr.md) la spirale dans le plan XY
3.  [Part Union](Part_Fuse/fr.md) la spirale et le miroir pour obtenir un filet fermé, en forme de cœur.

#### Profil pour une section quelconque 

<img alt="" src=images/thread-by-horz-profile-profileMake.png  style="width:1000px;">

1.  faire un profil de coupe (vertical). Assurez-vous que la hauteur de l\'esquisse correspond à la hauteur du filet dont vous avez besoin.
2.  fabriquer une hélice 1 de hauteur identique au pas et le pas identique au pas du filetage et dont le rayon d'hélice est égal à 0,42 \* diamètre nominal du filetage.
3.  Balayez le profil coupé le long de l\'hélice1. Définissez make solid et frenet à true.
4.  Faites un cercle de rayon nominal du filetage dans le plan x-y.
5.  Faites un profil à partir du cercle. (Part-workbench: utilitaire avancé pour créer des formes, ou [Draft Upgrade](Draft_Upgrade/fr.md) puis MakeFace = true)
6.  couper le profil avec le profil de balayage
7.  faire un clone à partir de la coupe (Draft workbench)
8.  Rétrograder le clone pour obtenir un filet. (Draft workbench) Ce filet est le profil horizontal nécessaire à cette méthode.
9.  Faites une hélice avec un rayon de rayon nominal du filet et un pas du filet et la hauteur du filet requis.
10. Passez le filet le long de l'hélice. Réglez solide et frenet sur true.

Vous avez terminé.

Credit: pas à pas tiré d\'un [post sur le forum par Ulrich1a](http://forum.freecadweb.org/viewtopic.php?f=3&t=6506#p52558), légèrement modifié.

Ces étapes sont aussi visibles dans cette vidéo de Gaurav Prabhudesai: <http://www.youtube.com/watch?v=fxKxSOGbDYs>

#### Pours et contres 

\+ Un filetage solide prêt à l\'emploi est créé directement par le balayage.

La réalisation du filetage sur la tige est fait immédiatement Si une opération Booléenne est requise , elle se fait immédiatement , plus rapide que la mèthode 3 les bouts de vis sont fait immédiatement les vis longues ne sont pas un problème un filetage sans espace n\'est pas un problème

\- la définition du profil du filetage est compliquée faire un découpage pose problème fichier imposant

### Méthode 5. Lofting entre les faces extrudées hélicoïdales 

### Généralités 

Les splines hélicoïdales extrudent les faces coaxiales pouvant être lobées, contrairement à l\'hélice paramétrique de FreeCAD. Deux splines hélicoïdales sont nécessaires pour définir un taraudage. Ces deux éléments peuvent être mis à l\'échelle à partir d\'une spline de bibliothèque, puis localisés et extrudés de manière appropriée pour obtenir le bon formulaire.

Les hélices paramétriques de FreeCAD ne sont pas vraiment hélicoïdales, mais les b-splines hélicoïdales ne sont pas difficiles à tracer. Une méthode manuelle consiste à aligner des dodécagones (polygones à 12 côtés) avec des intervalles de rayon de 5 mm/diamètre de 10 mm à des intervalles de 1/12 mm (0,08333.mm) et à tracer des splines d\'un sommet à l\'autre dans l\'ordre croissant et rotatif. disons 10 tours, de sorte que cette spline puisse être réutilisée en tant que fichier de bibliothèque pour l\'importation et la réutilisation. Il est pratique d'utiliser un pas de 10 mm de diamètre/1 mm pour faciliter la mise à l'échelle. Si vous le faites manuellement, dessiner un Dwire puis le convertir en b-spline est plus facile que de dessiner une spline. Les courbures ne sont pas calculées pendant le tracé, elles suivent donc le curseur et se cassent plus docilement.

Une fois que les splines sont redimensionnées à la bonne taille et situées de manière à ce que le loft ait le bon angle inclus entre les flancs du filetage, elles sont extrudées le long de leur axe, ce qui correspond à la longueur d\'un pas pour la spline interne, le pas externe/8.

<img alt="" src=images/splineextrudeloft.png  style="width:912px;">

Les filets ISO et autres ont été allégés, c\'est-à-dire que les bords intérieurs et extérieurs sont plutôt plats que nets, ce qui convient parfaitement aux utilisateurs de FreeCAD, car nous pouvons appliquer un lissage à la face hélicoïdale à la taille nominale de la fixation, alors qu\'une face interne ne peut pas être loft une spline de bord externe car une face est un profil fermé, une spline est ouverte. La norme ISO indique que la taille nominale des filetages externes a un pas de largeur de face/8. L\'image montre comment la géométrie est arrangée et les faces hélicoïdales qui en résultent. Ensuite, lissez entre les faces, puis un cylindre qui donne la face hélicoïdale interne, que ISO met à la hauteur/4 de la largeur, est ajouté aux filets.

![761PX](images/Threadform.PNG )

Cette méthode produit des solides fiables qui \"booléen\" correctement. Bien qu\'il ne produise pas de filetage de vis \"paramétrique\" dans les tailles standard, c\'est-à-dire qu\'il permet d\'accéder facilement à la forme par taille de fixation, il constitue un moyen simple de produire une bibliothèque précise à réutiliser, ainsi que des modèles de formes spécialisées telles que ACME ou des vis Archimédien. , sont également simples comme des one-offs. {{Tutorials navi}}  {{PartDesign Tools navi}} {{Sketcher Tools navi}}

---
[documentation index](../README.md) > Thread for Screw Tutorial/fr
