

## Préface


{{TOCright}}

Cette page rassemble des informations sur les solveurs par éléments finis utilisés par [Atelier FEM](FEM_Workbench/fr.md). L\'interface entre un solveur et FreeCAD dans le pré-traitement ainsi que dans le post-traitement se fait par le biais de fichiers texte. Cela signifie qu\'en théorie, tout solveur pouvant être configuré et contrôlé au moyen de fichiers texte est capable de fonctionner avec FreeCAD; un analyseur et un rédacteur appropriés des fichiers d'entrée et de sortie doivent être programmés pour que cette communication fonctionne. Un sujet de forum pour discuter et annoncer tout ce qui concerne les différents solveurs peut être trouvé ici : [Sujet de discussion sur les solveurs FEM généraux](https://forum.freecadweb.org/viewtopic.php?f=18&t=26326).

Wikipedia [répertorie de nombreux packages logiciels d\'éléments finis](https://en.wikipedia.org/wiki/List_of_finite_element_software_packages). Une comparaison peut être trouvée sur [feacompare.com](https://feacompare.com/).

### Solveurs disponibles dans diverses distributions Linux {#solveurs_disponibles_dans_diverses_distributions_linux}

Le dépôt [FreeCAD-dependencies](https://github.com/luzpaz/FreeCAD-dependencies) suit les dépendances de FreeCAD sur de nombreuses distributions Linux. La page [FEM.md](https://github.com/luzpaz/FreeCAD-dependencies/blob/master/FC-Workbenches/FEM.md) examine les solveurs FEA open source pouvant être utilisés avec [atelier FEM](FEM_Workbench/fr.md). La page affiche la version d\'un solveur particulier dans le référentiel d\'une distribution Linux particulière. Cette information est utile pour savoir si un solveur est actuel ou obsolète et doit être mis à niveau.

L\'information est également discutée sur le forum: [supported and not supported Solver](https://forum.freecadweb.org/viewtopic.php?f=18&t=26326&start=10#p270325).

## Solvers avec une interface dans FreeCAD {#solvers_avec_une_interface_dans_freecad}

Ces solveurs sont bien intégrés à FreeCAD, ce qui signifie qu'il est possible de configurer et d'exécuter un projet de simulation à partir de l'interface graphique et des boutons de FEM Workbench.

### CalculiX

Il s\'agit du premier solveur intégré à fonctionner avec l\'atelier FEM. CalculiX est principalement conçu pour les analyses statiques, thermomécaniques et modales. Plus d\'informations sur ce solveur se trouvent dans [CalculiX pour l\'analyse par la méthode des éléments finis](FEM_CalculiX/fr.md).

### Elmer

Le solveur multiphysique Elmer a été intégré à FreeCAD en tant que projet [Google Summer of Code 2017](Google_Summer_of_Code_2017.md) project: [main website](https://www.csc.fi/web/elmer), [community portal](http://www.elmerfem.org./), [code repository](https://github.com/ElmerCSC/elmerfem), [Elmer Integration (GSoC) - Activity Log](https://forum.freecadweb.org/viewtopic.php?f=18&t=22576) (fil de discussion).

### Z88

Le solveur Z88 est conçu pour les simulations statiques linéaires en mettant l\'accent sur l\'enseignement de la méthode des éléments finis. C\'était le deuxième solveur à être [intégré à FreeCAD](https://forum.freecadweb.org/viewtopic.php?f=18&t=15568). L\'intégration a ensuite été améliorée en tant que projet [Google Summer of Code 2017](Google_Summer_of_Code_2017.md).

Voir les informations:

-   [Site principal](https://fr.z88.de/z88os/), [page de téléchargement](https://fr.z88.de/download-z88os/), [dépôt du code source](https://github.com/LSCAD/Z88OS) (et binaires précompilés).
-   Notes de publication: [Z88os V15 publié le 17.07.2017](https://forum.z88.de/viewtopic.php?f=18&t=885), [Z88os V13 publié le 20.05.2009](https://forum.z88.de/viewtopic.php?t=90) (version dans Debian Jessie 8, Stretch 9, Buster 10).
-   [Comment utiliser Z88 dans FEM?](https://forum.freecadweb.org/viewtopic.php?t=23318) (discussion sur le forum).

Il existe deux versions, Z88OS est l\'édition open source, tandis que Z88Aurora est un logiciel gratuit et comprend une interface graphique et des méthodes de solution supplémentaires.

## Solveurs implémentés comme ateliers externes {#solveurs_implémentés_comme_ateliers_externes}

Ces solveurs ne sont pas intégrés dans [atelier FEM](FEM_Workbench/fr.md) ce qui signifie qu\'ils ont besoin d\'une interface distincte pour configurer un projet de simulation. Ceci est réalisé par [macros](Macros/fr.md) ou [Ateliers externes](External_workbenches/fr.md).

### OpenFoam

[OpenFoam](https://openfoam.org/) est un outil puissant pour la simulation [1](https://en.wikipedia.org/wiki/Computational_fluid_dynamics) (CFD) distribué sous la forme d\'une série de bibliothèques C ++.

OpenFoam est disponible dans FreeCAD via deux ateliers externes:

-   [Cfd](https://github.com/qingfengxia/Cfd) à l\'origine par Qingfeng Xia.
-   [CfdOF](https://github.com/jaheyns/CfdOF) un fork de Cfd axé sur la facilité d\'utilisation.

Alors que Cfd est destiné à être complet en fonctionnalités pour les utilisateurs avancés, CfdOF se concentre sur les utilisateurs qui débutent dans le monde de CFD et OpenFoam.

Pour Cfd: [mise à jour sur le calcul dynamique des fluides FreeCAD + OpenFOAM](https://forum.freecadweb.org/viewtopic.php?f=18&t=13699) (sujet du forum), \[<https://forum.freecadweb.org/viewtopic>. php? f = 37 & t = 22993 Progression de l\'atelier de calcul général en dynamique des fluides computationnelle (CFD): CfdWorkbench\] (ancien fil).

Pour CfdOF: [Atelier de travail sur la dynamique des fluides numérique (CFD) à l\'aide d\'OpenFOAM](https://forum.freecadweb.org/viewtopic.php?f=18&t=21576), [.html matériel de formation](http://opensim.co.za/training).

Les deux ateliers peuvent être installés via [Addon manager](Std_AddonMgr/fr.md), et les deux disposent d\'un espace de discussion dans le [sous-forum CfdOF/CFD](https://forum.freecadweb.org/viewforum.php?f=37).

### DualSPHysics

[DualSPHysics](https://dual.sphysics.org/) est un ensemble de bibliothèques C ++, CUDA et Java qui utilisent le [hydrodynamique des particules lissées](https://en.wikipedia.org/wiki/Smoothed-particle_hydrodynamics) (SPH) modèle nommé [SPHysics](https://wiki.manchester.ac.uk/sphysics/index.php/Main_Page) pour étudier les phénomènes d\'écoulement en surface libre tels que les vagues.

DesignSPHysics est un atelier externe intégré à FreeCAD qui fournit une interface graphique à DualSPHysics: [site principal](https://design.sphysics.org/), [dépôt du code](https://github.com/dualsphysics/DesignSPHysics), [Projet intéressant: Simulateur de fluide DesignSPHysics](https://forum.freecadweb.org/viewtopic.php?f=18&t=20595) (sujet du forum).

DesignSPHysics peut être installé via le [Gestionnaire d\'Addon](Std_AddonMgr/fr.md).

### FastHenry et FasterCap {#fasthenry_et_fastercap}

FastHenry et FasterCap sont des solveurs de champ de capacitif et de résistance-inductance développés par FastFieldSolvers: [site principal](https://www.fastfieldsolvers.com/default.asp), [page de téléchargement](https://www.fastfieldsolvers.com/download.htm) (code binaire et source), [forum](https://www.fastfieldsolvers.com/forum/).

[Atelier EM](EM_Workbench/fr.md) est un établi externe créé pour servir de front-end à ces solveurs électromagnétiques. FastHenry, pour l\'analyse d\'impédance magnéto-quasi statique en 3D, est entièrement pris en charge, tandis que FasterCap est accessible via certaines macros Python.

Voir: [ElectroMagnetic Workbench](https://forum.freecadweb.org/viewtopic.php?f=9&t=33372) (fil principal), [atelier électromagnétique](https://forum.freecadweb.org/viewtopic.php?f=18&t=31920), [FreeCAD for ElectroMagnetics](https://forum.freecadweb.org/viewtopic.php?f=18&t=5400), [dépôt du code](https://github.com/ediloren/EM-Workbench-for-FreeCAD) pour l\'atelier.

L\'atelier EM peut être installé via le [Gestionnaire d\'Addon](Std_AddonMgr/fr.md)

### fcFEM

fcFEM est un solveur par éléments finis pour les études structurelles et mécaniques, implémenté en Python, et qui peut être exécuté directement à partir de FreeCAD sans faire appel à des solveurs binaires externes. Par conséquent, il peut être considéré comme le propre solutionneur interne de FreeCAD.

fcFEM a été conçu pour surmonter certaines limitations d'autres solveurs, tels que CalculiX, afin de réaliser diverses études d'ingénierie structurale.

Certains des problèmes qui sont censés être résolus par ce solveur incluent

-   Analyses de mailles mixtes (solide-shell) pour traiter des colonnes composites ou des composants architecturaux préfabriqués: [FEM object types](https://forum.freecadweb.org/viewtopic.php?f=18&t=21029&p=216682&hilit=sandwich#p216682).
-   Les éléments de poutre et de coque améliorés, car les éléments de poutre de CalculiX semblent donner des résultats erronés: [Élément de faisceau CalculiX à 3 nœuds](https://forum.freecadweb.org/viewtopic.php?f=18&t=27903&hilit=beam#p226038), \[ <https://forum.freecadweb.org/viewtopic.php?f=18&t=21029&start=100> FEM object types\], [Exemple d\'analyse 1D](https://forum.freecadweb.org/viewtopic.php?f=18&t=16044).
-   Contrôle de la longueur d\'arc pour surmonter les points limites pour l\'analyse de l\'effondrement élasto-plastique: [FEM - Connexion tubulaire avec des éléments de coque](https://forum.freecadweb.org/viewtopic.php?f=24&t=26921&hilit=riks#p215325).
-   Éléments d\'interface d\'épaisseur nulle pour diverses applications, comme le béton post-contraint avec frottement: [pre-stressed pre/post-tensioned concrete bridge](https://forum.freecadweb.org/viewtopic.php?f=18&t=30286&hilit=classical&start=20#p259636).

L\'auteur considère que FreeCAD est une bonne plate-forme de prototypage permettant de configurer, de tester et de visualiser rapidement différents problèmes structurels. Il est donc très utile de disposer d\'un solveur intégré et flexible. Voir le fil principal, [fcFEM - FEA de bout en bout](https://forum.freecadweb.org/viewtopic.php?f=18&t=33974).

fcFEM est présenté sous la forme d\'une bibliothèque python et d\'une macro. Vous pouvez le télécharger à partir du [dépôt de github](https://github.com/HarryvL/fcFEM). Il sera éventuellement disponible à partir du [gestionnaire d\'Addon](Std_AddonMgr/fr.md) ou sera distribué avec FreeCAD lui-même.

## Implémentation en cours {#implémentation_en_cours}

### FEniCS

FEniCS est un cadre informatique permettant de résoudre des équations aux dérivées différentielles (PDE) avec des interfaces de programmation de haut niveau en Python et C ++. Il peut être utilisé pour établir des problèmes scientifiques dans des formulations d\'éléments finis qui peuvent ensuite être résolus numériquement.

Voir: [main website](https://fenicsproject.org/), [Fenics as Solver](https://forum.freecadweb.org/viewtopic.php?f=18&t=4677) (fil du forum).

[FenicsSolver](https://github.com/qingfengxia/FenicsSolver) est une plate-forme de simulation permettant de traiter des problèmes multi-corps, multi-physique (couplés) et multi-échelles. Il espère intégrer le solveur FEniCS à la fois dans [atelier FEM](FEM_Workbench/fr.md) et dans l\'[atelier extérieur](External_workbenches/fr.md) Cfd afin que le système résultant fonctionne comme une alternative gratuite à Comsol ou à Moose. FenicsSolver est développé par le même auteur de Cfd.

### OOFEM

[OOFEM](http://www.oofem.org/) est un programme FEM orienté objet de l\'Université technique tchèque destiné à résoudre les problèmes de mécanique, de transport et de mécanique des fluides.

Il a été mentionné qu'il présentait certains avantages par rapport à CalculiX comme les éléments d'interface ([re-stressed pre/post-tensioned concrete bridge](https://forum.freecadweb.org/viewtopic.php?f=18&t=30286&start=20#p260275)) et le contrôle de la longueur d\'arc pour l\'analyse de l\'effondrement élasto-plastique ([FEM - Tubular Connection with Shell Elements](https://forum.freecadweb.org/viewtopic.php?f=24&t=26921&hilit=Arc#p215325)).

L\'intégration préliminaire dans FEM Workbench a été effectuée. Voir: [OOFem](https://forum.freecadweb.org/viewtopic.php?f=18&t=31288) (fil principal), [p126338 demande de test, solveurs multiples](https://forum.freecadweb.org/viewtopic.php?t=15568&start=20#).

Jusqu\'à ce que l\'intégration du solveur soit terminée et que le nouveau code soit fusionné dans le dépôt principal de FreeCAD, les fichiers requis pour utiliser le solveur dans FEM Workbench peuvent être téléchargés à partir d\'un [fork de FreeCAD](https://github.com/berndhahnebach/FreeCAD_bhb/tree/femoofem/src/Mod/Fem/).

### MBDyn

-   Logiciel d\'analyse polyvalent OpenSource Dynamics multicorps
-   <https://www.mbdyn.org/>
-   <https://forum.freecadweb.org/viewtopic.php?f=18&t=39165>

## Solveurs non intégrés {#solveurs_non_intégrés}

Les solveurs suivants n\'ont pas été intégrés à FreeCAD mais ils ont suscité un certain intérêt de la part de la communauté des utilisateurs. Si un développeur souhaite créer un pont de communication pour un solveur particulier, il ou elle doit consulter le [FEM subforum](https://forum.freecadweb.org/viewforum.php?f=18) pour obtenir des conseils et une assistance.

Les articles suivants sont peut-être obsolètes, mais les informations qu'ils contiennent peuvent néanmoins être utiles pour comprendre comment intégrer des solveurs dans FreeCAD.

-   [Module d\'extension FEM](Extend_FEM_Module/fr.md)
-   [Tutoriel pour ajouter des équations MEF](Add_FEM_Equation_Tutorial/fr.md)
-   [Tutoriel pour ajouter des contraintes MEF](Add_FEM_Constraint_Tutorial/fr.md)

### Agros2D et Hermes {#agros2d_et_hermes}

[Agros2D](http://www.agros2d.org/) est un programme graphique multiplateforme conçu pour résoudre différents problèmes physiques. Il utilise les bibliothèques C ++ [Hermes](http://www.hpfem.org/hermes/) pour la résolution de systèmes d'équations aux dérivées différentielles non linéaires dépendantes du temps simples et complexes à l'aide d'une version générale de la méthode des éléments finis \[https : //en.wikipedia.org/wiki/Hp-FEM (hp-FEM)\]. Code principal [référentiel](https://github.com/hpfem/hermes) et [tutorials](https://github.com/hpfem/hermes-tutorial).

### Code-Aster et Code-Saturne {#code_aster_et_code_saturne}

[Code-Aster](https://www.code-aster.org/) est un solveur multiphysique à code source ouvert. Avec le pré-processeur Salomé-Meca, ils forment une plate-forme de simulation développée par EDF-GDF, le plus grand groupe énergétique français. Il s\'agissait d\'un des premiers packages dont l\'inclusion dans FreeCAD avait été envisagée: [FreeCAD et Code-Aster/Salome-Meca](https://forum.freecadweb.org/viewtopic.php?t=2839) (fil du forum).

[Code-Saturne](https://www.code-saturne.org/cms/) est un logiciel gratuit et à code source ouvert développé et publié par EDF pour résoudre les problèmes de la dynamique des fluides numérique (CFD).

### FElt

[FElt](http://felt.sourceforge.net/) est un package d\'éléments finis permettant de résoudre les problèmes d\'analyse structurelle linéaire et statique. Le [code original](https://sourceforge.net/projects/felt/) est obsolète. Il a donc été créé dans un [nouveau dépôt](https://github.com/Sudhanshu-Dubey14/felt) pour relancer le projet et le rendre actif et le rendre compilable dans un système moderne.

Il a été suggéré dans les forums de procéder à une analyse des cadres en béton armé (assemblages de poutres et de colonnes) à l\'aide d\'éléments de poutre 1D: [Automation in Design](https://forum.freecadweb.org/viewtopic.php?f=18&t=17061&start=20#p268503), [Felt in FEM Workbench](https://forum.freecadweb.org/viewtopic.php?f=18&t=33463).

### Frame3DD

[Frame3DD](http://frame3dd.sourceforge.net/) est un progiciel destiné à l\'analyse structurelle statique et dynamique de cadres et de fermes 2D et 3D, \[dépôt principal <https://github.com/pslack/frame3dd>\]. Un lecteur préliminaire de fichiers d'entrée a été annoncé dans les forums:

[Test read data from Frame3DD file.](https://forum.freecadweb.org/viewtopic.php?f=24&t=19428) Sujet général du forum FEM. <https://forum.freecadweb.org/viewtopic.php?f=18&t=43389> .

### Impact FEM {#impact_fem}

-   <http://www.impact-fem.org/> (lien cassé)

### libMesh

[libMesh](https://libmesh.github.io/) est une bibliothèque d\'éléments finis c ++ pour la solution numérique d\'équations aux dérivées différentielles avec pour objectif principal de prendre en charge les calculs de raffinement de maillage adaptatif (AMR) en parallèle: [code repository](https://github.com/libMesh/libmesh).

Il a été suggéré d\'intégrer cette bibliothèque à FreeCAD dans le cadre d\'un [projet](https://forum.freecadweb.org/viewtopic.php?f=8&t=35493) [Google Summer of Code](Google_Summer_of_Code_2020.md).

### Modelica

[Modelica](https://www.modelica.org/) est un langage permettant de modéliser et d\'optimiser des systèmes physiques complexes et interconnectés, par exemple des systèmes mécaniques, électriques, thermiques, hydrauliques et autres. Le langage lui-même et ses bibliothèques standard sont open source. Certains environnements de simulation basés sur Modelica, tels que Dymola de Catia, sont propriétaires mais il existe également des implémentations libres telles que [OpenModelica](https://openmodelica.org/) et [JModelica](https://jmodelica.org/).

Avec FreeCAD, Modelica a été suggéré pour aider à réaliser des animations mais plus généralement il pourrait être utilisé en ingénierie mécanique et en génie du bâtiment pour résoudre des équations et optimiser une conception particulière: [= 32556 Modelica](https://forum.freecadweb.org/viewtopic.php?f=18&t) (fil du forum).

Le package [PyFMI](https://pypi.org/project/PyFMI/) contient des liaisons Python qui fonctionnent avec les modèles FMU qui sont des modèles normalisés au format binaire produits par des environnements Modelica conformes, notamment Dymola, OpenModelica et JModelica. Il a été suggéré que cette bibliothèque pourrait aider FreeCAD à se connecter à un système [Modelica](https://forum.freecadweb.org/viewtopic.php?f=18&t=32556#p272632) (forum post).

### Mumps

[Mumps](http://mumps-solver.org/) est un solveur générique pour les systèmes massifs d\'équations qui traite généralement de la factorisation et du fonctionnement sur des matrices clairsemées. Il a été mentionné dans le forum: [demande de tests, plusieurs solveurs](https://forum.freecadweb.org/viewtopic.php?t=15568&start=20#p126087).

Il n'effectue pas d'analyse par éléments finis directement mais il peut être utilisé en interne par d'autres progiciels tels que Code-Aster.

### Mystran

Mystran est un programme d\'analyse structurelle qui utilise le format de fichier de Nastran. Il est livré sous license MIT. Ce qui signifie que cela semble OpenSource. A voir sur [Mystran](https://www.mystran.com/) et sur github [Mystran-github](https://github.com/dr-bill-c/MYSTRAN) et sur le forum FreeCAD [Mystran-FreeCAD-forum](https://forum.freecadweb.org/viewtopic.php?t=46171).

### Nastran

Nastran est un programme d\'analyse structurelle développé par la NASA dans les années 1970. Les versions modernes sont des produits commerciaux et des sources fermées. Toutefois, ses anciennes versions, [Nastran-93](https://github.com/nasa/NASTRAN-93) et [Nastran-95](https://github.com/nasa/NASTRAN-95) ont été publiées en open source en 2015. Message du forum: [Nastran](https://forum.freecadweb.org/viewtopic.php?f=18&t=12753).

Il n\'y a pas de support technique pour le code open source et il est probablement difficile à compiler dans un système moderne.

### OpenSees

[OpenSees](http://opensees.berkeley.edu/) est un logiciel cadre permettant de développer des applications permettant de simuler des systèmes structurels et géotechniques principalement dans le domaine de l\'ingénierie parasismique. Topic sur le forum <https://forum.freecadweb.org/viewtopic.php?f=18&t=20745> et <https://forum.freecadweb.org/viewtopic.php?f=18&t=31922>

### PolyFEM

[PolyFEM](https://polyfem.github.io/) PolyFEM est une simple bibliothèque d\'éléments finis C++ et Python. Nous proposons un large éventail de PDEs courants, notamment: Laplace, Helmholtz, élasticité linéaire, élasticité Saint-Venant, élasticité néo-hookéenne et Stokes. Sujet du formulaire <https://forum.freecadweb.org/viewtopic.php?f=18&t=42857>

### Sparselizard

\[<http://www.sparselizard.org/> Sparselizard est une bibliothèque d\'éléments finis C ++ open source rapide, générale, multiphysique, p-adaptative, fonctionnant sous Linux, Mac et Windows. Elle est utilisée pour concevoir des microdispositifs de nouvelle génération (transducteurs à ultrasons, micromiroirs, microvannes, entraînements à peigne, \...) et est soigneusement validée par rapport aux solutions analytiques, aux logiciels tiers et aux mesures des dispositifs fabriqués. Elle semble être développée par l\'équipe du générateur de maillage gmsh.

### SU2

[SU2](https://su2code.github.io/) est un ensemble d'outils logiciels développés en C ++ et en Python pour la résolution des [équation partielle différentielle](https://en.wikipedia.org/wiki/Partial_differential_equation) et des problèmes d\'optimisation sous contrainte PDE sur des maillages non structurés. Il est particulièrement utilisé dans les domaines de l\'aérodynamique et de la dynamique des fluides numérique (CFD).

### Technog

Technog Professional est un programme source fermé permettant de réaliser des simulations géotechniques telles que des glissements de terrain, des pieux, la stabilité des pentes et des calculs de génie civil (réponse de la maçonnerie et des tremblements de terre), [site web](http://www.feat.nl/) (lien cassé).

Technog a été utilisé avec succès dans FreeCAD en tant que substitut de CalculiX bien que le nombre d'éléments pouvant être gérés par la version d'essai soit limité: [Integration of tochnog solver in FreeCAD FEM](https://forum.freecadweb.org/viewtopic.php?f=18&t=26772) (sujet du forum).

### XC

[XC](http://www.xcengineering.xyz/) est un programme FEA conçu pour résoudre des problèmes structurels en génie civil comme une analyse de coque réelle. Il utilise les bibliothèques OpenSees: [référentiel principal](https://github.com/xcfem/xc), [XC, opensource structural engineering FEM code](https://forum.freecadweb.org/viewtopic.php?f=18&t=31262) (sujet du forum).


{{FEM Tools navi

}}  
