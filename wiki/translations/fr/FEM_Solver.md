# FEM Solver/fr
{{TOCright}}



## Préface

Cette page rassemble des informations sur les solveurs par éléments finis utilisés par l\'[atelier FEM](FEM_Workbench/fr.md). L\'interface entre un solveur et FreeCAD dans le pré-traitement ainsi que dans le post-traitement se fait par le biais de fichiers texte. Cela signifie qu\'en théorie, tout solveur pouvant être configuré et contrôlé au moyen de fichiers texte est capable de fonctionner avec FreeCAD; un analyseur et un rédacteur appropriés des fichiers d'entrée et de sortie doivent être programmés pour que cette communication fonctionne. Un sujet de forum pour discuter et annoncer tout ce qui concerne les différents solveurs peut être trouvé ici : [Sujet de discussion sur les solveurs FEM généraux](https://forum.freecadweb.org/viewtopic.php?f=18&t=26326).

Wikipedia [répertorie de nombreux packages logiciels d\'éléments finis](https://en.wikipedia.org/wiki/List_of_finite_element_software_packages). Une comparaison peut être trouvée sur [feacompare.com](https://feacompare.com/).



### Solveurs disponibles dans diverses distributions Linux 

Le dépôt [FreeCAD-dependencies](https://github.com/luzpaz/FreeCAD-dependencies) suit les dépendances de FreeCAD sur de nombreuses distributions Linux. La page [FEM.md](https://github.com/luzpaz/FreeCAD-dependencies/blob/master/FC-Workbenches/FEM.md) examine les solveurs FEA open source pouvant être utilisés avec l\'[atelier FEM](FEM_Workbench/fr.md). La page affiche la version d\'un solveur particulier dans le référentiel d\'une distribution Linux particulière. Cette information est utile pour savoir si un solveur est actuel ou obsolète et doit être mis à niveau.

L\'information est également discutée sur le forum : [supported and not supported Solver](https://forum.freecadweb.org/viewtopic.php?f=18&t=26326&start=10#p270325).



## Solvers avec une interface dans FreeCAD 

Ces solveurs sont bien intégrés à FreeCAD, ce qui signifie qu'il est possible de configurer et d'exécuter un projet de simulation à partir de l'interface graphique et des boutons de FEM Workbench.

### CalculiX

Il s\'agit du premier solveur intégré à fonctionner avec l\'atelier FEM. CalculiX est principalement conçu pour les analyses statiques, thermomécaniques et modales. Plus d\'informations sur ce solveur se trouvent dans [CalculiX pour l\'analyse par la méthode des éléments finis](FEM_CalculiX/fr.md).

### Elmer

Le solveur multiphysique Elmer a été intégré à FreeCAD en tant que projet du [Google Summer of Code 2017](Google_Summer_of_Code_2017.md) : [site web principal](https://www.csc.fi/web/elmer), [portail communautaire](http://www.elmerfem.org./), [dépôt du code](https://github.com/ElmerCSC/elmerfem), [intégration d\'Elmer (GSoC) - journal d\'activité (sujet du forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=22576).

### Mystran

Mystran est un programme d\'analyse structurelle qui utilise le format de fichier Nastran. Il est publié sous la licence MIT. Ce qui signifie qu\'il semble OpenSource. Voir [site web principal](https://www.mystran.com/), [dépôt du code](https://github.com/dr-bill-c/MYSTRAN) et [sujet du forum sur Mystran](https://forum.freecadweb.org/viewtopic.php?t=46171).

### Z88

Le solveur Z88 est conçu pour les simulations statiques linéaires en mettant l\'accent sur l\'enseignement de la méthode des éléments finis. C\'était le deuxième solveur à être [intégré à FreeCAD](https://forum.freecadweb.org/viewtopic.php?f=18&t=15568). L\'intégration a ensuite été améliorée en tant que projet du [Google Summer of Code 2017](Google_Summer_of_Code_2017.md).

Voir les informations :

-   [Site principal](https://fr.z88.de/z88os/), [page de téléchargement](https://fr.z88.de/download-z88os/), [dépôt du code source](https://github.com/LSCAD/Z88OS) (et binaires précompilés).
-   Notes de publication: [Z88os V15 publié le 17.07.2017](https://forum.z88.de/viewtopic.php?f=18&t=885), [Z88os V13 publié le 20.05.2009](https://forum.z88.de/viewtopic.php?t=90) (version dans Debian Jessie 8, Stretch 9, Buster 10).
-   [Comment utiliser Z88 dans FEM? (sujet du forum)](https://forum.freecadweb.org/viewtopic.php?t=23318).

Il existe deux versions, Z88OS est l\'édition open source, tandis que Z88Aurora est un logiciel gratuit et comprend une interface graphique et des méthodes de solution supplémentaires.



## Solveurs implémentés comme ateliers externes 

Ces solveurs ne sont pas intégrés dans [atelier FEM](FEM_Workbench/fr.md) ce qui signifie qu\'ils ont besoin d\'une interface distincte pour configurer un projet de simulation. Ceci est réalisé par [macros](Macros/fr.md) ou [Ateliers externes](External_workbenches/fr.md).

### DualSPHysics

[DualSPHysics](https://dual.sphysics.org/) est un ensemble de bibliothèques C ++, CUDA et Java qui utilisent le [hydrodynamique des particules lissées](https://en.wikipedia.org/wiki/Smoothed-particle_hydrodynamics) (SPH) modèle nommé [SPHysics](https://wiki.manchester.ac.uk/sphysics/index.php/Main_Page) pour étudier les phénomènes d\'écoulement en surface libre tels que les vagues.

DesignSPHysics est un atelier externe intégré à FreeCAD qui fournit une interface graphique à DualSPHysics : [site principal](https://design.sphysics.org/), [dépôt du code](https://github.com/dualsphysics/DesignSPHysics), [Projet intéressant: Simulateur de fluide DesignSPHysics (sujet du forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=20595).

DesignSPHysics peut être installé via le [Gestionnaire des extensions](Std_AddonMgr/fr.md).



### FastHenry et FasterCap 

FastHenry et FasterCap sont des solveurs de champ de capacitif et de résistance-inductance développés par FastFieldSolvers: [site principal](https://www.fastfieldsolvers.com/default.asp), [page de téléchargement](https://www.fastfieldsolvers.com/download.htm) (code binaire et source), [forum](https://www.fastfieldsolvers.com/forum/).

[Atelier EM](EM_Workbench/fr.md) est un établi externe créé pour servir de front-end à ces solveurs électromagnétiques. FastHenry, pour l\'analyse d\'impédance magnéto-quasi statique en 3D, est entièrement pris en charge, tandis que FasterCap est accessible via certaines macros Python.

Voir : [ElectroMagnetic Workbench (sujet principal du forum)](https://forum.freecadweb.org/viewtopic.php?f=9&t=33372), [Electromagnetic Workbench - de nouveau (sujet du forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=31920), [FreeCAD for ElectroMagnetics (sujet du forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=5400), [dépôt du code pour l\'atelier](https://github.com/ediloren/EM-Workbench-for-FreeCAD)

L\'atelier EM peut être installé via le [Gestionnaire des extensions](Std_AddonMgr/fr.md).

### fcFEM

fcFEM est un solveur par éléments finis pour les études structurelles et mécaniques, implémenté en Python, et qui peut être exécuté directement à partir de FreeCAD sans faire appel à des solveurs binaires externes. Par conséquent, il peut être considéré comme le propre solutionneur interne de FreeCAD.

fcFEM a été conçu pour surmonter certaines limitations d'autres solveurs, tels que CalculiX, afin de réaliser diverses études d'ingénierie structurale.

Certains des problèmes qui sont censés être résolus par ce solveur incluent

-   Analyses de mailles mixtes (solide-shell) pour traiter des colonnes composites ou des composants architecturaux préfabriqués: [FEM object types (sujet du forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=21029&p=216682&hilit=sandwich#p216682).
-   Les éléments de poutre et de shell améliorés, car les éléments de poutre de CalculiX semblent donner des résultats erronés: [CalculiX 3-node Beam Element (sujet du forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=27903&hilit=beam#p226038), [FEM object types (sujet du forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=21029&start=100), [Example for 1D analysis (sujet du forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=16044).
-   Contrôle de la longueur d\'arc pour surmonter les points limites pour l\'analyse de l\'effondrement élasto-plastique: [FEM - Tubular Connection with Shell Elements (sujet du forum)](https://forum.freecadweb.org/viewtopic.php?f=24&t=26921&hilit=riks#p215325).
-   Éléments d\'interface d\'épaisseur nulle pour diverses applications, comme le béton post-contraint avec frottement: [pre-stressed pre/post-tensioned concrete bridge (sujet du forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=30286&hilit=classical&start=20#p259636).

L\'auteur considère que FreeCAD est une bonne plate-forme de prototypage permettant de configurer, de tester et de visualiser rapidement différents problèmes structurels. Il est donc très utile de disposer d\'un solveur intégré et flexible. Voir le fil principal, [fcFEM - FEA from start to finish (sujet principal du forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=33974).

fcFEM est présenté sous la forme d\'une bibliothèque python et d\'une macro. Vous pouvez le télécharger à partir du [dépôt de github](https://github.com/HarryvL/fcFEM). Il sera éventuellement disponible à partir du [gestionnaire des extensions](Std_AddonMgr/fr.md) ou sera distribué avec FreeCAD lui-même.

### OpenFoam

[OpenFoam](https://openfoam.org/) est un outil puissant pour la simulation [Mécanique des fluides numérique](https://fr.wikipedia.org/wiki/M%C3%A9canique_des_fluides_num%C3%A9rique) (CFD en anglais) distribué sous la forme d\'une série de bibliothèques C++.

OpenFoam est disponible dans FreeCAD via deux ateliers externes :

-   [Cfd](https://github.com/qingfengxia/Cfd) à l\'origine par Qingfeng Xia.
-   [CfdOF](https://github.com/jaheyns/CfdOF) un fork de Cfd axé sur la facilité d\'utilisation.

Alors que Cfd est destiné à être complet en fonctionnalités pour les utilisateurs avancés, CfdOF se concentre sur les utilisateurs qui débutent dans le monde de CFD et OpenFoam.

Pour Cfd : [update on FreeCAD + OpenFOAM fluid dynamic computation (sujet du forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=13699), [Progress of the general Computational Fluid Dynamics (CFD) workbench: CfdWorkbench (ancien sujet du forum)](https://forum.freecadweb.org/viewtopic.php?f=37&t=22993).

Pour CfdOF : [Computational Fluid Dynamics (CFD) workbench using OpenFOAM (sujet du forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=21576), [matériel de formation](http://opensim.co.za/training.html).

Les deux ateliers peuvent être installés via le [Gestionnaire des extensions](Std_AddonMgr/fr.md) et disposent d\'un espace de discussion dans le [sous-forum CfdOF/CFD](https://forum.freecadweb.org/viewforum.php?f=37).



## Implémentation en cours 

### FEniCS

FEniCS est un cadre informatique permettant de résoudre des équations aux dérivées différentielles (PDE) avec des interfaces de programmation de haut niveau en Python et C ++. Il peut être utilisé pour établir des problèmes scientifiques dans des formulations d\'éléments finis qui peuvent ensuite être résolus numériquement.

Voir : [site principale](https://fenicsproject.org/), [Fenics as Solver (sujet du forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=4677).

[FenicsSolver](https://github.com/qingfengxia/FenicsSolver) est une plate-forme de simulation permettant de traiter des problèmes multi-corps, multi-physique (couplés) et multi-échelles. Il espère intégrer le solveur FEniCS à la fois dans [atelier FEM](FEM_Workbench/fr.md) et dans l\'[atelier extérieur](External_workbenches/fr.md) Cfd afin que le système résultant fonctionne comme une alternative gratuite à Comsol ou à Moose. FenicsSolver est développé par le même auteur de Cfd.

### OOFEM

[OOFEM](http://www.oofem.org/) est un programme FEM orienté objet de l\'Université technique tchèque destiné à résoudre les problèmes de mécanique, de transport et de mécanique des fluides.

Il a été mentionné qu'il présentait certains avantages par rapport à CalculiX comme les éléments d'interface ([pre-stressed pre/post-tensioned concrete bridge (sujet du forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=30286&start=20#p260275)) et le contrôle de la longueur d\'arc pour l\'analyse de l\'effondrement élasto-plastique ([FEM - Tubular Connection with Shell Elements (sujet du forum)](https://forum.freecadweb.org/viewtopic.php?f=24&t=26921&hilit=Arc#p215325)).

L\'intégration préliminaire dans l\'atelier FEM a été effectuée. Voir : [OOFem (sujet principal du forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=31288), [p126338 test request, multiple solvers (sujet du forum)](https://forum.freecadweb.org/viewtopic.php?t=15568&start=20#).

Jusqu\'à ce que l\'intégration du solveur soit terminée et que le nouveau code soit fusionné dans le dépôt principal de FreeCAD, les fichiers requis pour utiliser le solveur dans FEM Workbench peuvent être téléchargés à partir d\'un [fork de FreeCAD](https://github.com/berndhahnebach/FreeCAD_bhb/tree/femoofem/src/Mod/Fem/).

### MBDyn

-   Logiciel d\'analyse polyvalent opensource Multibody Dynamics
-   [MBDyn](https://www.mbdyn.org/)
-   [FreeCAD as pre-post processor for MBDyn (sujet du forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=39165)



## Solveurs non intégrés 

Les solveurs suivants n\'ont pas été intégrés à FreeCAD mais ils ont suscité un certain intérêt de la part de la communauté des utilisateurs. Si un développeur souhaite créer un pont de communication pour un solveur particulier, il ou elle doit consulter le [FEM subforum](https://forum.freecadweb.org/viewforum.php?f=18) pour obtenir des conseils et une assistance.

Les articles suivants sont peut-être obsolètes, mais les informations qu'ils contiennent peuvent néanmoins être utiles pour comprendre comment intégrer des solveurs dans FreeCAD.

-   [Module d\'extension FEM](Extend_FEM_Module/fr.md)
-   [Tutoriel pour ajouter des équations MEF](Add_FEM_Equation_Tutorial/fr.md)
-   [Tutoriel pour ajouter des contraintes MEF](Add_FEM_Constraint_Tutorial/fr.md)

### ADAPy

Voir [ADAPy](https://github.com/Krande/adapy/) et [ADA - Assembly for Design & Analysis (sujet du forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=64929).



### Agros2D et Hermes 

[Agros2D](http://www.agros2d.org/) est un programme graphique multiplateforme conçu pour la résolution de différents problèmes physiques. En interne, il utilise les bibliothèques C++ de [Hermes](http://www.hpfem.org/hermes/) pour la résolution de systèmes d\'équations différentielles partielles (EDP) non linéaires simples et complexes dépendant du temps, en utilisant une version générale de la méthode des éléments finis [(hp-FEM)](https://en.wikipedia.org/wiki/Hp-FEM). Code principal [dépôt](https://github.com/hpfem/hermes) et des [tutoriaux](https://github.com/hpfem/hermes-tutorial).



### Code-Aster et Code-Saturne 

[Code-Aster](https://www.code-aster.org/) est un solveur multiphysique à code source ouvert. Avec le pré-processeur Salomé-Meca, ils forment une plate-forme de simulation développée par EDF-GDF, le plus grand groupe énergétique français. Il s\'agissait d\'un des premiers packages dont l\'inclusion dans FreeCAD avait été envisagée: [FreeCAD and Code-Aster/Salome-Meca (sujet du forum)](https://forum.freecadweb.org/viewtopic.php?t=2839).

[Code-Saturne](https://www.code-saturne.org/cms/) est un logiciel gratuit et à code source ouvert développé et publié par EDF pour résoudre les problèmes de la dynamique des fluides numérique (CFD).

### FElt

[FElt](http://felt.sourceforge.net/) est un package d\'éléments finis permettant de résoudre les problèmes d\'analyse structurelle linéaire et statique. Le [code original](https://sourceforge.net/projects/felt/) est obsolète. Il a donc été créé dans un [nouveau dépôt](https://github.com/Sudhanshu-Dubey14/felt) pour relancer le projet et le rendre actif et le rendre compilable dans un système moderne.

Il a été suggéré dans les forums de procéder à une analyse des cadres en béton armé (assemblages de poutres et de colonnes) à l\'aide d\'éléments de poutre 1D : [Automation in Design (sujet du forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=17061&start=20#p268503), [Felt in FEM Workbench (sujet du forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=33463).

### Frame3DD

[Frame3DD](http://frame3dd.sourceforge.net/) est un logiciel pour l\'analyse structurelle statique et dynamique de cadres et de fermes en 2D et 3D, [principal dépôt](https://github.com/pslack/frame3dd). Un lecteur préliminaire pour les fichiers d\'entrée a été annoncé dans les forums : [Test read data from Frame3DD file](https://forum.freecadweb.org/viewtopic.php?f=24&t=19428). Sujet général dans le forum FEM : [Frame3DD](https://forum.freecadweb.org/viewtopic.php?f=18&t=43389).

### Impact FEM 

-   <http://www.impact-fem.org/> (lien cassé)

### libMesh

[libMesh](https://libmesh.github.io/) est une bibliothèque d\'éléments finis c ++ pour la solution numérique d\'équations aux dérivées différentielles avec pour objectif principal de prendre en charge les calculs de raffinement de maillage adaptatif (AMR) en parallèle : [dépôt du code](https://github.com/libMesh/libmesh).

Il a été suggéré d\'intégrer cette bibliothèque dans FreeCAD dans le cadre du [Google Summer of Code project](Google_Summer_of_Code.md) : [GSOC 2019 Configuration Management Project (sujet du forum)](https://forum.freecadweb.org/viewtopic.php?f=8&t=35493).

### Modelica

[Modelica](https://www.modelica.org/) est un langage permettant de modéliser et d\'optimiser des systèmes physiques complexes et interconnectés, par exemple des systèmes mécaniques, électriques, thermiques, hydrauliques et autres. Le langage lui-même et ses bibliothèques standard sont open source. Certains environnements de simulation basés sur Modelica, tels que Dymola de Catia, sont propriétaires mais il existe également des implémentations libres telles que [OpenModelica](https://openmodelica.org/) et [JModelica](https://jmodelica.org/).

Avec FreeCAD, Modelica a été suggéré pour aider à réaliser des animations mais plus généralement il pourrait être utilisé en ingénierie mécanique et en génie du bâtiment pour résoudre des équations et optimiser une conception particulière : [Modelica (sujet du forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=32556).

Le package [PyFMI](https://pypi.org/project/PyFMI/) contient des liaisons Python qui fonctionnent avec les modèles FMU qui sont des modèles normalisés au format binaire produits par des environnements Modelica conformes, notamment Dymola, OpenModelica et JModelica. Il a été suggéré que cette bibliothèque pourrait aider FreeCAD à se connecter à un système [Modelica (sujet du forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=32556#p272632).

### Mumps

[Mumps](http://mumps-solver.org/) est un solveur générique pour les systèmes massifs d\'équations qui traite généralement de la factorisation et du fonctionnement sur des matrices clairsemées. Il a été mentionné dans le forum : [Test request, multiple solvers (sujet du forum)](https://forum.freecadweb.org/viewtopic.php?t=15568&start=20#p126087).

Il n'effectue pas d'analyse par éléments finis directement mais il peut être utilisé en interne par d'autres progiciels tels que Code-Aster.

### Nastran

Nastran est un programme d\'analyse structurelle développé par la NASA dans les années 1970. Les versions modernes sont des produits commerciaux et des sources fermées. Toutefois, ses anciennes versions, [Nastran-93](https://github.com/nasa/NASTRAN-93) et [Nastran-95](https://github.com/nasa/NASTRAN-95) ont été publiées en open source en 2015. [Nastran (sujet du forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=12753).

Il n\'y a pas de support technique pour le code open source et il est probablement difficile à compiler dans un système moderne.

### OpenSees

[OpenSees](https://opensees.berkeley.edu/) est un logiciel cadre permettant de développer des applications permettant de simuler des systèmes structurels et géotechniques principalement dans le domaine de l\'ingénierie parasismique. [OpenSees, the Open System for Earthquake Engineering Simulation (sujet du forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=20745) et [Relicensing of OpenSees (sujet du forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=31922).

### PolyFEM

[PolyFEM](https://polyfem.github.io/) est une simple bibliothèque d\'éléments finis en C++ et Python. Nous proposons un large éventail d\'équations différentielles partielles courantes, telles que : Laplace, Helmholtz, élasticité linéaire, élasticité Saint-Venant, élasticité Néo-Hookéenne et Stokes. [PolyFEM (sujet du forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=42857).

### Sparselizard

[Sparselizard](http://www.sparselizard.org/) est une bibliothèque d\'éléments finis C ++ open source rapide, générale, multiphysique, p-adaptative, fonctionnant sous Linux, Mac et Windows. Elle est utilisée pour concevoir des microdispositifs de nouvelle génération (transducteurs à ultrasons, micromiroirs, microvannes, entraînements à peigne, \...) et est soigneusement validée par rapport aux solutions analytiques, aux logiciels tiers et aux mesures des dispositifs fabriqués. Elle semble être développée par l\'équipe du générateur de maillage gmsh.

### SU2

[SU2](https://su2code.github.io/) est un ensemble d'outils logiciels développés en C ++ et en Python pour la résolution des [équation partielle différentielle](https://en.wikipedia.org/wiki/Partial_differential_equation) et des problèmes d\'optimisation sous contrainte PDE sur des maillages non structurés. Il est particulièrement utilisé dans les domaines de l\'aérodynamique et de la dynamique des fluides numérique (CFD).

### Technog

Technog Professional est un programme source fermé permettant de réaliser des simulations géotechniques telles que des glissements de terrain, des pieux, la stabilité des pentes et des calculs de génie civil (réponse de la maçonnerie et des tremblements de terre), [site web](http://www.feat.nl/) (lien cassé).

Technog a été utilisé avec succès dans FreeCAD en tant que substitut de CalculiX bien que le nombre d'éléments pouvant être gérés par la version d'essai soit limité : [Integration of tochnog solver in FreeCAD FEM (sujet du forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=26772).

### XC

[XC](http://www.xcengineering.xyz/) est un programme FEA conçu pour résoudre des problèmes structurels en génie civil comme une analyse de coque réelle. Il utilise les bibliothèques OpenSees : [dépôt principal](https://github.com/xcfem/xc), [XC, opensource structural engineering FEM code (sujet du forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=31262).


{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM Solver/fr
