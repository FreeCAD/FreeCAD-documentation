# Release notes 0.17/fr
<div id="itsfree" style="text-align:left;color:black;background:#f6f6f6;margin:1em 7em;padding:0.5em 2em;border:2px solid #a7d7f9;">

*Cette version de FreeCAD est dédiée à notre ami Roland Frank [qui nous a quittés en 2017](https://forum.freecadweb.org/viewtopic.php?f=8&t=25673). Il était un membre actif et apprécié du forum FreeCAD, et ses tutoriels vidéo sur les chaînes Youtube [Learn FreeCAD](https://www.youtube.com/watch?v=_HEvhclR4-o&list=PL6fZ68Cq3L8k0JhxnIVjZQN26cn9idJrj) et [BPLFRE](https://www.youtube.com/watch?v=m49z0weonog&list=PLsrwVwvqYb8G4Ri0iz1JIebsOXkgoytAY) ont aidé de nombreuses personnes à démarrer avec FreeCAD.*


</div>

FreeCAD 0.17 a été publié le 6 avril 2018. Vous pouvez l\'obtenir depuis la page de [GitHub](https://github.com/FreeCAD/FreeCAD/releases/tag/0.17). Ceci est un résumé des changements les plus intéressants. La liste complète des changements peut être trouvée dans le [MantisBT bugtracker FC 0.17 changelog](https://www.freecadweb.org/tracker/changelog_page.php?version_id=73). Les anciennes notes de publication de FreeCAD peuvent être trouvées dans [Liste des fonctions](Feature_list/fr#Notes_de_versions.md).

<img alt="" src=images/Release017_Title.jpg  style="width:800px;"> 
*Garden Railway Coach O & K (par l\'utilisateur de FreeCAD \"Garden Railway Coach O & K\", voir [Users Showcase](http://forum.freecadweb.org/viewtopic.php?f=24&t=17261))*

## Points forts 

Deux années se sont écoulées depuis la sortie de la version 0.16 précédente, mais l\'équipe FreeCAD n\'est pas restée inactive pendant ce temps. Plus de 6 800 révisions ont été ajoutées au code source de FreeCAD. A titre de comparaison, c\'est plus de trois fois le travail effectué entre les v0.16 et 0.15! La plupart des ateliers existants ont bénéficié d\'améliorations et deux nouveaux ateliers ont été ajoutés. De nouveaux modules supplémentaires ont également été développés par la communauté. Quelques-uns des points forts :

L\'atelier **PartDesign** (conception de pièces) a été complètement révisé. Un nouveau conteneur Body (Corps) contient désormais une chaîne de fonctions et lève l\'exigence de mappage (Ancrage) des esquisses sur les faces planes. De nouveaux outils pour créer une géométrie de référence tels que des points, des axes et des plans rendent PartDesign beaucoup plus polyvalent. ![](images/PartDesign_Body_tree.png )

Le nouveau <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestionnaire d\'Addon](Std_AddonMgr/fr.md) disponible dans le menu Outils (précédemment disponible en tant que [addons installer macro](https://github.com/FreeCAD/FreeCAD-addons)) facilite l\'installation et la mise à jour des modules complémentaires et des macros sur Windows, Mac OS X et Linux. <img alt="" src=images/Addon_manager_v017.png  style="width:300px;">

Le **Sketcher** (atelier d\'esquisses) prend maintenant en charge la création de B-spline avec de nombreuses façons de contrôler les courbes et d\'afficher les informations de la courbe. <img alt="" src=images/FC017_Sketcher_B-spline_01.png  style="width:300px;">

Le nouvel atelier **TechDraw** (mise en plan) vise à remplacer l\'atelier Drawing et fournit déjà plus de fonctionnalités que l\'ancien atelier Drawing. <img alt="" src=images/TechDraw_Workbench_Example.png  style="width:300px;">

## Généralités

-   Yorik van Havre a écrit \"[Le Manuel FreeCAD](Manual:Introduction/fr.md)\" comme un livre d\'introduction sur l\'utilisation de FreeCAD.
-   Le recalcul de document peut maintenant être désactivé / activé via le menu contextuel.
-   Il y a un nouveau style de navigation Revit.
-   Un nouvel indicateur de navigation en bas à droite de la fenêtre FreeCAD permet un accès rapide aux styles de navigation.

![](images/FC017_Navigation_Indicator_01.png ) ![](images/FC017_Navigation_Indicator_02.png )

-   Le [graphique de dépendance](Std_DependencyGraph/fr.md) a bénéficié d\'améliorations graphiques.
-   L\'importation STEP utilise le nouveau [conteneur Part](Std_Part/fr.md) et l\'utilise pour organiser un assemblage STEP importé en sous-assemblages, en suivant de plus près la structure du document original. stpZ (un format STEP compressé) est maintenant supporté.
-   La plupart des icônes de FreeCAD ont été retravaillées pour mieux se conformer aux [directives de Tango](http://tango.freedesktop.org/Tango_Icon_Theme_Guidelines).

-   Le projet FreeCAD reconnaît les contributions de sa communauté en ajoutant un onglet Remerciements dans la fenêtre de dialogue *À propos de FreeCAD*. Les nouvels onglets Licence et Bibliothèques listent la licence de FreeCAD et fournissent de l\'information sur les bibliothèques tierces utilisées.

<img alt="" src=images/AboutFreeCAD_Credits.png  style="width:300px;">

## Atelier Arch (architecture) 

-   Nouvel outil [Tableur](Arch_Schedule/fr.md): Cet outil a été complètement réécrit et offre maintenant un moyen beaucoup plus flexible de rassembler les données du document dans une feuille de calcul, en utilisant différents types de requêtes, comme compter tous les objets d\'un certain type, ou additionner le volume total d\'une certaine catégorie d\'objets.

-   Nouvel ensemble d\'[outils de tuyauterie](Arch_Pipe/fr.md) pour la conception de systèmes de tuyauterie. Vous pouvez utiliser des lignes, des croquis ou du filaire comme base pour placer des tubes et créer automatiquement des connexions entre 2 ou 3 tubes.

-   L\'outil [Structure](Arch_Structure/fr.md) a maintenant été étendu avec une série de nouveaux préréglages pour construire des éléments préfabriqués en béton.

-   Au cours de l\'édition 2017 [Google Summer of Code](Google_Summer_of_Code.md), à laquelle participait FreeCAD, l\'outil [Ferraillage](Arch_Rebar/fr.md) a été considérablement étendu et a gagné une interface utilisateur conviviale pour ajouter facilement plusieurs types de barres de renfort à vos structures en béton.

<img alt="" src=images/Arch_Rebar_preview.png  style="width:640px;">

-   Les [fenêtres](Arch_Window/fr.md) ont gagné plusieurs améliorations, telles que la possibilité de définir les sous-composants comme ouvrables, afficher les symboles d\'ouverture, apparaître ouvert, et avoir des panneaux persiennes.

<img alt="" src=images/Arch_Door_preview.png  style="width:640px;">

-   Les outils [Axes](Arch_Axis/fr.md) ont également été réécrits, et permettent des systèmes plus complexes en combinant différentes séries d\'axes ensemble. Ils peuvent également être personnalisés pour montrer différents types de situations tels que les niveaux.

-   Un nouvel outil [Grille](Arch_Grid/fr.md) permet de créer facilement des objets de base de type tableur en étirant, en joignant ou en divisant des cellules. Ces objets de grille peuvent être utilisés comme systèmes d\'axes ou comme bases pour des agencements complexes de fenêtres ou de panneaux.

-   Les nouveaux [Outils à panneaux](Arch_Panel_Cut/fr.md) ont été spécialement conçus pour les constructions de panneaux. Ils permettent de construire un modèle composé de [Panneaux](Arch_Panel/fr.md), puis de générer des feuilles de découpe qui peuvent être utilisées par [l\'atelier Path](Path_Workbench/fr.md) pour générer du code machine de découpe.

-   Un nouvel outil [Découpage optimisé](Arch_Nest/fr.md) (encore expérimental) permet de composer des feuilles de découpage en plaçant automatiquement des formes 2D dans une forme contenant.

-   [Multi-materiaux](Arch_MultiMaterial/fr.md) a été introduit dans l\'atelier Arch. Il permet de créer automatiquement des parois multicouches, ou de contrôler les différents matériaux des objets composés tels que les fenêtres.

-   L\'exportateur de l\'atelier Arch OBJ et DAE prend désormais en charge les matériaux, à la fois lors de l\'importation et de l\'exportation.

-   Le support d\'importation pour le format [3DS](Arch_3DS/fr.md) a été ajouté.

## L\'atelier Draft (Planche à dessin) 

-   [Système de groupage Automatique](Draft_AutoGroup/fr.md): L\'atelier Draft dispose désormais d\'un bouton de regroupement automatique dans sa barre d\'outils principale. Une fois activé, tous les objets Draft et Arch nouvellement créés seront automatiquement placés dans ce groupe.

-   [Outil d\'inclinaison](Draft_Slope/fr.md): Lorsqu\'il est utilisé sur une [Droite Draft](Draft_Line/fr.md) ou un [Objet filaire Draft](Draft_Wire/fr.md), cet outil vous permettra de lui donner une pente / inclinaison donnée. C\'est-à-dire que les points intermédiaires et terminaux auront une valeur Z inférieure, de sorte que l\'objet entier aura une inclinaison constante. Ceci est utile pour utiliser les droites ou les objets filaires comme base pour les objets nécessitant une inclinaison précise, tels que les vitres de toit ou les tuyaux d\'égout.

-   [Proxy du plan de travail](Draft_SetWorkingPlaneProxy/fr.md): Lorsque vous travaillez avec [Plans de travail Draft](Draft_SelectPlane/fr.md), vous devez souvent stocker les emplacements du plan de travail que vous utilisez souvent. Ceci est maintenant possible en plaçant l\'un de ces mandataires dans votre document. Il se souviendra de l\'emplacement actuel du plan de travail et pourra également restaurer la visibilité actuelle et / ou la visibilité des objets.

<img alt="" src=images/Draft_WP_preview.png  style="width:640px;">

-   [Étirement](Draft_Stretch/fr.md): L\'atelier Draft a maintenant un outil d\'étirement qui permet de déplacer les sommets de plusieurs objets Draft en même temps.

-   [Étiquettes Draft](Draft_Label/fr.md): Avec cet outil, on peut placer des étiquettes dans le document, qui est composé d\'un morceau de texte et d\'une ligne de repère qui peut être libre ou coller à un objet spécifique. Le texte peut être fait pour afficher un morceau de texte personnalisé, ou afficher automatiquement le contenu d\'une propriété de l\'objet cible.

<img alt="" src=images/Draft_Label_Preview.png  style="width:640px;">

## Atelier FEM 

-   FEM Mesh
    -   **L\'objet Gmsh** est un objet maillé qui permet d\'utiliser l\'outil de maillage [Gmsh](http://gmsh.info/) à l\'intérieur de FreeCAD. Diverses options de Gmesh sont supportées.
    -   **L\'objet de couche limite pour gmsh** permet de créer une couche limite.
    -   **L\'objet Groupe de mailles pour gmsh** permet de créer des nœuds et des groupes d\'éléments. Les noms peuvent être modifiés par l\'utilisateur.
    -   **L\'objet région de maillage pour gmsh** permet de définir des régions de maillage avec une taille d\'éléments de maillage différente pour les nœuds, les arêtes, les faces et les volumes.
    -   L\'outil **GUI clear mesh** efface le maillage mais conserve tous les ajustements de maillage. C\'est très pratique si les fichiers doivent être partagés.
    -   L\'outil **GUI imprimer info mesh** imprimer toutes sortes d\'informations de maillage.
    -   **GUI fournisseur de vue maillée** est capable d\'afficher le maillage carré ainsi que les éléments maillés hexaèdre, pentaèdre et pyramide.
    -   Le **Modèle de données de maillage** a été mis à jour vers [SMESH](http://salome-platform.org) à la version 7.7.1 <https://github.com/FreeCAD/FreeCAD/commit/666a3e5a>
    -   L**\'API Mesh** a été étendue pour lire des données de groupe de mailles sur les données de maillage FreeCAD SMESH FEM par Python. C\'était la base de l\'objet de groupe Gmsh.
    -   **Mesh API** a été étendu pour exporter des groupes de mailles au format de fichier Abaqus et CalculiX inp.
    -   **L\'outil de maillage FEM 2** convertit une surface d\'un maillage de volume en un maillage pour le module de maillage de FreeCAD.
    -   **Problèmes de maillage:** Les jacobiens non positifs sont un problème souvent vu dans les maillages FEM. Les éléments qui ont des jacobiens non positifs dans le solveur CalculiX sont colorés dans FreeCAD.
    -   **Fenics** Import et export du format de maille Fenics a été ajouté.

-   Objets
    -   **L\'objet de rotation de poutre** permet l\'analyse des poutres tournées autour de leur axe principal.
    -   **L\'objet matériau non linéaire** ajoute un comportement matière non linéaire à FreeCAD FEM. Il prend en charge le changement linéaire de la courbe de contrainte.
    -   **Matière fluide** \...
    -   **Contrainte vitesse initiale du flux** \...
    -   **Contrainte Limite de fluide**
    -   **Contrainte potentiel électrostatique** \...
    -   **Contrainte source de chaleur du corps** \...
    -   **Contrainte transformer** \...
    -   **Contrainte Température** \...
    -   **Contrainte contact** \...
    -   **Contrainte plan de rotation** \...
    -   **Contrainte poids propre** \...

-   Solveur
    -   **Solver frame work** a été écrit à partir de zéro lors d\'un projet Google Summer of Code.
    -   Ajout du support pour le logiciel de résolution de problèmes FEM **ElmerFEM**, <https://www.csc.fi/web/elmer>.
    -   A l\'intérieur du cadre de travail, le type d\'analyse peut être choisi par un **objet d\'équation**(solveur d\'Elmer seulement, ATM.)
    -   Un support de base pour le logiciel de résolution FEM **Z88**, <https://fr.z88.de/z88os/>, a été ajouté.
    -   **CalculiX** a été porté sur le travail du cadre de résolution. L\'objet ccxtools solveur reste dans FreeCAD FEM car il est très bien testé et a des pré-vérifications étendues.

-   Analyse Calculix
    -   **Coupled Thermal Structural Analysis** \...
    -   **1D pipe Analyse de flux Analyse** \...
    -   **Coupled Beam Shell Solid modèles** \...

-   Post-traitement standard
    -   **Shell et faisceau sortie 3D** Permettent de sortir l\'analyse de la coque et du faisceau comme sortie solide 3D pour voir les contraintes dans les sections.
    -   **Peeq strain** La prise en charge d\'une contrainte plastique équivalente a été ajoutée à l\'objet résultat, au lecteur de résultat et au post-traitement vtk.

-   Post-traitement étendu
    -   **VTK** Un post-traitement étendu basé sur [VTK](https://www.vtk.org/) a été ajouté.
    -   **Filtre de clip** \...
    -   **Filtre de clip scalaire** \...
    -   **Filtre de Coupe** \...
    -   **Filtre d\'Enveloppe vectorielle** \...
    -   **Stress linéarisé** \...
    -   **Data at point** Un outil pour obtenir les données de résultat pour un point spécifique.
    -   **Data along line** Un outil pour obtenir les données de résultat pour une ligne spécifique imprimée sous forme de diagramme.

-   Corrections, code et autres choses
    -   La **suite de tests unitaires** pour le banc de travail FEM a été étendue.
    -   La **base de code** a été massivement améliorée.
    -   La plupart du code FEM a été porté sur **Python3**.
    -   En outre, il y a eu des tonnes de bugs trouvés et corrigés.
    -   Toutes les icônes ont été redessinées et associées aux directives.
    -   **Code formating** Il ne devrait plus y avoir d\'onglets et d\'espaces blancs dans tout le code source FEM.
    -   Les codes Python sont conformes à la plupart des règles de **flake8**.
    -   Des dizaines de **fautes de frappe** dans le code source ont été corrigées (à ce que je sache cela s\'applique à l\'ensemble de FreeCAD, luzpaz les trouve toutes comme une aiguille dans la botte de foin).

Quelques images <img alt="" src=images/bridge-all.png  style="width:640px;"> <img alt="" src=images/bridge-detail.png  style="width:640px;">

## Atelier Part 

-   Le noyau de modélisation géométrique Open Cascade a été mis à jour de la version 6.8.0 à la version 7.2.0 (la version actuelle de l\'OCC peut dépendre de la plateforme / distribution). Cette version apporte beaucoup de corrections de bogues dans les opérations booléennes, l\'algorithme de suppression de ligne cachée, ainsi que l\'ajout de nouvelles fonctionnalités à l\'atelier Part.

-   Nouvelles fonctionnalités: [Fragments booléens](Part_BooleanFragments/fr.md), [Tranchage](Part_Slice/fr.md) et [XOR](Part_XOR/fr.md).

-   Grâce aux nouvelles fonctionnalités ci-dessus, les solides composites (compsolids) peuvent désormais être créés dans FreeCAD. Ils sont d\'une grande utilité dans FEM.

-   [Connexion de parois](Part_JoinConnect/fr.md) la performance et la fiabilité ont été améliorées, et l\'outil a été rendu plus polyvalent.

-   Nouvelle fonction: [Décalage 2D](Part_Offset2D/fr.md), pour décaler des contours plans.

-   Amélioration: L\'outil [Extrusion de pièce](Part_Extrude.md) prend désormais en charge la direction normale paramétrique, la direction contrôlée par le bord lié, l\'inversion, la 2ème longueur, le 2ème angle de dépouille et la symétrie. En outre, la case à cocher Créer un Solide est maintenant cochée automatiquement si vous ouvrez la boîte de dialogue et que l\'objet sélectionné est un contour fermé (par exemple, une esquisse).

-   Amélioration: L\'outil [Solide par révolution](Part_Revolve/fr.md) supporte maintenant le lien paramétrique à l\'axe de révolution.

-   Le nouvel utilitaire [Ancrage](Part_EditAttachment/fr.md) accessible depuis le menu *Pièce → Attachement \...* peut être utilisé pour ancrer paramétriquement la plupart des types d\'objets à une autre géométrie.

-   Le nouveau [conteneur Part](Std_Part/fr.md) peut être utilisé pour regrouper la plupart des types de formes et pour les déplacer comme une unité. Il contient également des plans et des axes standard auxquels attacher des objets. Il servira de base pour le futur atelier d\'assemblage en fournissant un moyen de déplacer les pièces. Il est disponible dans tous les ateliers à partir d\'une barre d\'outils avec [Groupe](Std_Group/fr.md).

## Atelier PartDesign (Conception de pièces) 

L\'atelier PartDesign a connu d\'importants changements, fruit des efforts conjugués de plusieurs développeurs sur une période de 5 ans. <img alt="" src=images/PartDesign017-teaser-motor-core.png  style="width:800px;">

-   Le nouveau conteneur [Body (Corps)](PartDesign_Body/fr.md) contient une chaîne de fonctionnalités PartDesign constituant un seul solide contigu. Il contient également des plans et des axes standard auxquels attacher des objets. Grâce au conteneur Body, il n\'est plus nécessaire de mapper (ancrer) les esquisses aux faces lors de l\'ajout de fonctionnalités. Cette exigence était une limitation majeure de l\'ancien PartDesign, qui pouvait entraîner la rupture de nombreux modèles lors des changements de paramètres. Donc, il est maintenant recommandé d\'éviter de mapper des esquisses aux faces autant que possible.

-   Nouvelles fonctionnalités additives et soustractives: [Primitives](PartDesign_CompPrimitiveAdditive/fr.md), [Lissage](PartDesign_AdditiveLoft/fr.md), [Balayage](PartDesign_AdditivePipe/fr.md), [Evidement ou coque](PartDesign_Thickness/fr.md).

-   Les nouvelles entités de référence [plans](PartDesign_Plane/fr.md), [droites](PartDesign_Line/fr.md) et [ points](PartDesign_Point/fr.md) sont utiles pour placer des esquisses, l\'alignement et servir d\'axes de révolution.

-   Nouvelle commutation automatique entre PartDesign et Sketcher. Lorsque vous créez une nouvelle esquisse à partir de l\'atelier PartDesign, une fois le support d\'esquisse défini, l\'interface utilisateur bascule automatiquement vers l\'atelier Esquisse et ses outils en mode d\'édition. Lorsque l\'esquisse est fermée, l\'interface utilisateur revient à l\'atelier PartDesign et restaure la vue à son état précédent. Ainsi, les outils Sketcher ont été supprimés des barres d\'outils PartDesign pour libérer de l\'espace pour les nouvelles fonctionnalités PartDesign.

## Atelier Path 

L\'atelier Path a été massivement révisé en version 0.17. La révision a vu la suppression de tout le code HeeksCNC plus ancien et le remplacement du wrapper python libarea avec le nouveau module Path-Area. En conséquence, les opérations sont devenues beaucoup plus puissantes, plus rapides, avec une base de code simplifiée.

-   La prise en charge des opérations 2.5D est complète, y compris [contournage](Path_Profile/fr.md), [fraisage de face](Path_MillFace/fr.md), [poche ou chambrage](Path_Pocket_Shape/fr.md), [profilage](Path_Profile/fr.md), et [perçage](Path_Drilling/fr.md)

-   Prise en charge limitée des opérations [profilage 3D](Path_Pocket_3D/fr.md).

-   Path peut utiliser un [panneau Arch](Arch_Panel/fr.md) comme objet de base pour regrouper plusieurs parties pour la découpe 2D.

-   Introduction de [Tâche](Path_Job/fr.md). La tâche est maintenant un objet central du flux de travail de Path. Elle organise et coordonne plusieurs opérations, outils, stock, orientation des pièces et alignement. Une Tâche personnalisée peut être sauvegardée en tant que \'Modèle de Tâche\' et réutilisée pour rationaliser la configuration des futures tâches. Les feuilles de configuration du travail fournissent un mécanisme pour automatiser la configuration des paramètres de profondeur et de vitesse.

-   Toutes les opérations ont une organisation de panneau de tâches cohérente.

-   Nouveau ou amélioré [post-processeurs](Path_Post/fr.md) pour LinuxCNC, Smoothieboard, GRBL, Phillips, OpenSBP (shopbot), Roland Modela, Centroid, Fablin, et Dynapath. La plupart des post-processeurs prennent en charge les arguments.

-   Amélioration de la [bibliothèque d\'outils](Path_ToolLibraryEdit/fr.md) et de l\'éditeur.

-   L\'outil [Inspecteur de parcours](Path_Inspect/fr.md) permet de mettre en évidence des commandes individuelles pour visualiser le parcours d\'usinage et explorer le gcode.

-   L\'outil [Simulateur d\'usinage](Path_Simulator/fr.md) effectue une coupe simulée en 3D pour visualiser l\'exécution du parcours d\'usinage.

-   Les opérations d\'habillage peuvent être utilisées pour affiner les opérations de base et ajouter de la complexité. Des déguisements existent pour les coins [\'dogbone\'](Path_DressupDogbone/fr.md), [balises d\'attente](Path_DressupTag/fr.md), [rampe d\'entrée d\'usinage](Path_DressupRampEntry/fr.md), et [découpage au cutter](Path_DressupDragKnife/fr.md) \'actions de coin\'

## Atelier Sketcher (esquisseur) 

-   Les esquisses peuvent maintenant être attachées de différentes manières, pas seulement aux faces planes comme c\'était le cas auparavant. L\'accrochage perpendiculaire aux bords est particulièrement important, ce qui est utile pour créer des profils pour la fonction [Balayage ](Part_Sweep/fr.md).

-   Les liens de géométries externes ne sont plus limités uniquement à l\'objet auquel l\'esquisse est mappée (liée). La géométrie provenant d\'autres esquisses est prise en charge. Des liens de géométrie externes peuvent être créés dans un conteneur Part, ou un conteneur Body, ou même un projet entier si les conteneurs Part et Body ne sont pas utilisés.

-   Automatisation de la visibilité: maintenant, lorsque vous commencez à éditer une esquisse, les objets qui en dépendent sont automatiquement masqués pour désencombrer la vue, et les objets utilisés pour les liens de géométrie externes sont automatiquement affichés; les anciennes visibilités sont restaurées lorsque vous fermez l\'esquisse.

-   Nouveau mode de création continue de contrainte: les outils de contrainte sont maintenant actifs même sans aucun élément sélectionné. Appuyez sur une contrainte, puis sélectionnez les objets auxquels appliquer la contrainte.

-   Nouveaux outils d\'arc d\'hyperbole et d\'arc de parabole.

-   Nouvel outil d\'édition d\'extension de bord.

-   Nouvel outil de création de B-spline, avec de nombreuses façons de contrôler les courbes (degré, multiplicité des nœuds, poids du point de contrôle) et informations d\'affichage (polygone de contrôle, peigne de courbure, indicateur de multiplicité de nœuds).

![](images/FC017_Sketcher_B-spline_01.png )

-   Nouvel outil **Carbon Copy** pour copier la géométrie d\'une autre esquisse.

-   L\'espace virtuel bascule toutes les contraintes vers un \"espace virtuel\" différent, en les cachant en effet de la vue.

-   La zone Liste de contraintes inclut la possibilité de masquer l\'alignement interne, ainsi que le masquage individuel des contraintes à l\'aide d\'une case à cocher.

-   La contrainte \"Block\" supprime tous les degrés de liberté d\'un élément de géométrie en utilisant une seule contrainte. Il devrait être particulièrement utile pour travailler avec les B-Splines, qui sont lourdes à contraindre.

-   Nouveau polygone régulier avec nombre de côtés défini par l\'utilisateur.

-   Les solveurs d\'esquisse alternatifs sont disponibles via \"Afficher le contrôle du solveur avancé dans la barre des tâches\" dans les préférences de Sketcher (Esquisseur).

-   L\'ordre de rendu basé sur le style de géométrie permet de réordonner entre la géométrie normale, la construction et la géométrie externe. Utile lorsque ces types de géométrie se chevauchent.

-   Le solveur substitue automatiquement une combinaison de contrainte coïncidente + contrainte tangente à une contrainte tangente point-à-point, car la première est une utilisation incorrecte qui induit une erreur de tolérance qui peut causer d\'autres problèmes dans le modèle. L\'utilisateur est averti de la substitution par une boîte de dialogue qui peut être désactivée dans les préférences de l\'Esquisse en décochant \"Notifier les substitutions automatiques de contraintes\".

-   Nouvelle case à cocher dans la vue des tâches en mode édition \"Eviter les contraintes automatiques redondantes\".

-   Les contraintes horizontales et verticales peuvent être utilisées pour aligner les points sélectionnés.

## Atelier Spreadsheet (Feuille de calcul ou tableur) 

-   Un importateur de fichier Excel a été ajouté.

## Atelier Surface 

-   Une nouvelle addition dans la v0.17, l\'atelier Surface propose (pour l\'instant) 4 commandes fonctionnelles de création de surface.

## Atelier TechDraw (Mise en plan) 

[TechDraw](TechDraw_Workbench/fr.md) est un nouvel atelier de création de dessins techniques qui vise à remplacer l\'atelier de dessin vieillissant Drawing. FreeCAD v0.17 est toujours livré avec l\'atelier de dessin Drawing afin que vous puissiez toujours ouvrir et modifier vos fichiers contenant des pages de Drawing, mais Drawing sera supprimé progressivement dans une prochaine version. Quelques-unes des nouveautés passionnantes apportées par TechDraw:

-   La plupart des outils de l\'atelier Drawing ont une contrepartie TechDraw.
-   Création et manipulation de vue plus faciles. Les vues peuvent être saisies par leur bordure avec la souris et déplacées sur la page. L\'alignement des vues orthogonales peut être verrouillé.
-   Meilleure gestion du type de ligne (dur, lisse, iso, couture). Meilleure suppression des lignes cachées grâce à une bibliothèque mise à jour [OCC](Glossary#OCC.md).
-   Vue en coupe, création d\'une vue de détail.
-   Meilleure gestion des modèles.
-   Le dimensionnement est maintenant supporté par de multiples outils de dimensionnement: horizontal, vertical, longueur, radial, diamètre, angulaire.
-   Outils de décoration: hachures, hachures compatibles avec les spécifications Autodesk PAT, symboles, images.

## Modules Additionnels 

Certains des nouveaux modules de la communauté qui ont été créés.

-   L\'[atelier Manipulator](https://github.com/easyw/Manipulator) vise à aider au positionnement, au déplacement, à la rotation et à la prise de mesure des objets 3D (y compris sous PartDesign) via une interface conviviale.

-   [Curves (Courbes)](https://github.com/tomate44/CurvesWB), une collection d\'outils pour créer et éditer des courbes et des surfaces [NURBS](https://fr.wikipedia.org/wiki/NURBS).

-   [Nurbs](https://github.com/microelly2/freecad-nurbs), une collection de scripts pour gérer des surfaces et des courbes de forme libre.

-   [Silk](https://github.com/edwardvmills/Silk), une collection d\'outils de modélisation de surface NURBS axés sur la continuité de faible degré et de couture.

-   L\'[atelier Flamingo](Flamingo_Workbench.md), un ensemble de commandes personnalisées et d\'objets qui aident à concevoir des structures et des pipelines plus rapidement.

-   [Civil Engineering/Transportation Workbench](Civil_Engineering_Workbench.md)

-   [GDT](https://github.com/juanvanyo/FreeCAD-GDT), dimensionnement géométrique et tolérancement (GD&T).

-   [InventorLoader](https://github.com/jmplonka/InventorLoader) importer des fichiers Autodesk Inventor (en cours).

-   [Kicad StepUp Workbench](https://www.freecadweb.org/wiki/KicadStepUp_Workbench) est destiné à aider les utilisateurs de KiCad et FreeCAD dans la collaboration ECAD et MCAD.



---
![](images/Button_right.svg) [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 0.17/fr
