# <img alt="Icône de l\'atelier Path" src=images/Workbench_Path.svg  style="width:64px;"> Path Workbench/fr


{{TOCright}}

## Introduction

L\'<img alt="" src=images/Workbench_Path.svg  style="width:24px;"> [atelier Path](Path_Workbench/fr.md) est utilisé pour produire les instructions machine pour les [machines à commande numérique (CNC)](https://fr.wikipedia.org/wiki/Programmation_de_commande_numérique) à partir d\'un modèle 3D FreeCAD. Celui-ci produit des objets 3D réels sur des machines CNC telles que des fraiseuses, des tours, des découpeuses laser ou similaires. Généralement, les instructions sont en langage [G-code](https://fr.wikipedia.org/wiki/Programmation_de_commande_num%C3%A9rique#Fonctions_pr%C3%A9paratoires_G). Un [exemple général de simulation de séquence de parcours d\'outils CNC](https://www.ange-softs.com/SIMULCNCHTML/index.html) est présenté ici.

<img alt="" src=images/pathwb.png  style="width:600px;">

Le flux de travail de l\'atelier Path de FreeCAD crée ces instructions machine comme suit :

-   Un modèle 3D est l\'objet de base, généralement créé à l\'aide d\'un ou plusieurs des ateliers <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Part Design](PartDesign_Workbench/fr.md), <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/fr.md) ou <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft](Draft_Workbench/fr.md).
-   Une [Path Tâche](Path_Job/fr.md) est créée dans l\'atelier Path. Celle-ci contient toutes les informations nécessaires pour générer le G-code nécessaire pour traiter l\'usinage sur une fraiseuse CNC : il y a le brut de matière (ou stock), le [gestionnaire d\'outils](Path_ToolLibraryEdit/fr.md) et elle suit certaines commandes contrôlant la vitesse et les mouvements (généralement en G-code).
-   Les [Path Outils](Path_Tools/fr.md) sont sélectionnés comme requis par les opérations d\'usinage.
-   Les parcours de l\'outil de fraisage sont créés en utilisant par ex. des opérations de [Contournage](Path_Profile/fr.md) et [Poche](Path_Pocket_3D/fr.md). Ces objets Path utilisent le langage G-code interne à FreeCAD, indépendant de la machine CNC.
-   Le travail est exporté en G-code, correspondant à votre machine. Cette étape s\'appelle *post-traitement*. Il y a différents post-processeurs disponibles.



## Concepts généraux 

L\'atelier Path génère le G-Code définissant les parcours d\'outils requis pour fabriquer le projet représenté par le modèle 3D sur la fraiseuse cible en [Format G-code interne de FreeCAD](Path_scripting/fr#Le_Format_G-code_interne_de_FreeCAD.md), qui est ensuite traduit dans le langage approprié pour le contrôleur CNC cible en sélectionnant le Post processeur approprié.

Le G-code est généré à partir des directives et des opérations contenues dans un Path Tâche. Le déroulement des tâches les répertorie dans l\'ordre desquelles elles seront exécutées. La liste est complétée en ajoutant des opérations, des habillages, des commandes supplémentaires de chemins et des modifications à partir du menu Path ou par les boutons de l\'interface graphique.

L\'atelier Path fournit des outils de gestion (bibliothèque, table d\'outils), d\'inspection de G-code et de simulation. Il relie le Post processeur et permet d\'importer et d\'exporter des modèles de Tâches.

L\'atelier Path possède des dépendances externes, notamment :

1.  Les unités du modèle 3D FreeCAD sont définies dans les paramètres **Édition → Préférences → Général → Onglet Unités Réglage des unités**. La configuration du Post processeur définit les unités G-code finales.
2.  Le chemin du fichier Macro et les tolérances géométriques sont définis dans l\'onglet **Édition → Préférences → Path → Job Préférences**.
3.  Les couleurs sont définies dans l\'onglet **Édition → Préférences → Path → Couleurs de chemin**.
4.  Les paramètres des éléments de maintien sont définis dans l\'onglet **Édition → Préférences → Path → Trajectoires additionnelles (Dressups)**.
5.  Pour que la qualité du modèle 3D de base respecte les exigences de l\'atelier Path, utilisez Vérifier la géométrie.

## Limitations

Certaines limitations actuelles dont vous devez être conscient :

-   La plupart des outils de Path ne sont pas de véritables outils 3D mais uniquement compatibles 2.5D. Cela signifie qu\'ils prennent une forme 2D fixe et peuvent la découper à une profondeur donnée. Cependant, il existe deux outils qui produisent de véritables chemins 3D: **<img src="images/Path_3DPocket.svg" width=24px> [Évidement 3D](Path_Pocket_3D/fr.md)** et **<img src="images/Path_Surface.svg" width=24px> [Surface](Path_Surface/fr.md)** (qui est toujours une [fonction expérimentale](Path_experimental/fr.md) en novembre 2020).
-   La plupart des ateliers Path sont conçus pour une fraiseuse/routeur CNC standard à 3 axes (xyz) simple, mais les outils de tour sont en cours de développement dans la version 0.19_pre.
-   La plupart des opérations dans l\'atelier Path renverront des chemins basés sur un outil/un trépan de fraise standard uniquement, quel que soit le type d\'outil/trépan affecté dans un contrôleur d\'outil donné, à l\'exception de **![](images/)_[Gravure](Path_Engrave/fr.md)** et **<img src="images/Path_Surface.svg" width=24px> [Surface](Path_Surface/fr.md)**.
-   Les opérations effectuées dans l\'atelier Path ne connaissent pas les mécanismes de serrage utilisés pour fixer le modèle à votre machine. Par conséquent, veuillez vérifier et simuler les chemins que vous générez avant d\'envoyer le code à votre machine. Si nécessaire, modélisez vos mécanismes de serrage dans FreeCAD afin de mieux inspecter les chemins générés. Recherchez les éventuelles collisions avec les fixations ou autres obstacles le long des trajectoires.



## Unités

La gestion des unités dans Path peut prêter à confusion. Il y a plusieurs points à comprendre :

1.  Les unités de base FreeCAD pour la longueur et le temps sont respectivement \'mm\' et \'s\'. La vélocité est donc \'mm/s\'. C\'est ce que FreeCAD stocke en interne indépendamment de toute autre chose
2.  Le schéma d\'unité par défaut utilise les unités par défaut. Si vous utilisez le schéma par défaut et que vous entrez un taux d\'avance sans chaîne d\'unité, il sera saisi en tant que \'mm/s\'
3.  La plupart des machines à commande numérique attendent un débit d\'alimentation sous forme de \'mm/min\' ou \'in/min\'. La plupart des post-processeurs convertissent automatiquement l\'unité lors de la génération de gcode.

Schémas :

1.  Changer le schéma dans les préférences change la chaîne d\'unité par défaut pour les champs d\'entrée. Si vous êtes un utilisateur Path et que vous préférez concevoir en métrique, il est fortement recommandé d\'utiliser le schéma \"Metric Small Parts & CNC\". Si vous concevez en unités américaines, Imperial Decimal et Building US fonctionneront
2.  Changer le schéma de votre unité préférée n\'aura aucun effet sur la sortie, mais aidera à éviter les erreurs de saisie

Sortie :

1.  La génération de l\'unité correcte en sortie relève de la responsabilité du post-processeur et n\'est effectuée qu\'à ce moment-là
2.  L\'unité de sortie de la machine n\'a aucun lien avec le schéma de votre unité sélectionnée
3.  Les post-processeurs produisent une sortie métrique (G21), une sortie impériale (G20) ou sont configurables.
4.  Post-processeurs configurables par défaut à la mesure (G21)
5.  Si vous voulez que votre post-processeur configurable produise un gcode impérial (G20), placez l\'argument correct dans votre config de sortie de travail (ie \--inches pour linuxcnc). Cela peut être stocké dans un modèle de travail et défini comme modèle par défaut pour le rendre automatique pour tous les travaux futurs

Path Inspection :

1.  Si vous utilisez l\'outil Path Inspection pour regarder le G-code, vous le verrez en \"mm/s\" car il n\'est pas post-traité.



## Hauteurs et profondeurs 

De nombreuses commandes ont différentes hauteurs et profondeurs :

<img alt="" src=images/Path-DepthsAndHeights.gif  style="width:500px;"> 
*Référence visuelle pour les propriétés de profondeur (paramètres)*



## Commandes

Certaines commandes sont expérimentales et ne sont pas disponibles par défaut. Pour les activer, voir [Path Fonctions expérimentales](Path_experimental/fr.md).



### Commandes du projet 

-   <img alt="" src=images/Path_Job.svg  style="width:32px;"> [Tâche](Path_Job/fr.md) : crée une nouvelle tâche CNC.

-   <img alt="" src=images/Path_Post.svg  style="width:32px;"> [Post-traitement](Path_Post/fr.md) : exporte un projet en G-code.

-   <img alt="" src=images/Path_Sanity.svg  style="width:32px;"> [Rechercher des erreurs](Path_Sanity/fr.md) : vérifie les valeurs manquantes dans la tâche sélectionnée.

-   <img alt="" src=images/Path_ExportTemplate.svg  style="width:32px;"> [Exporter un modèle](Path_ExportTemplate/fr.md) : exporte la tâche en cours en tant que modèle.



### Commandes d\'outils 

-   <img alt="" src=images/Path_Inspect.svg  style="width:32px;"> [Inspecter des commandes](Path_Inspect/fr.md) : affiche le G-code pour vérification.

-   <img alt="" src=images/Path_Simulator.svg  style="width:32px;"> [Simulateur FAO](Path_Simulator/fr.md) : montre l\'opération d\'usinage comme le ferait la machine.

-   <img alt="" src=images/Path_SelectLoop.svg  style="width:32px;"> [Terminer une boucle](Path_SelectLoop/fr.md) : complète une boucle à partir de deux arêtes sélectionnées.

-   <img alt="" src=images/Path_OpActiveToggle.svg  style="width:32px;"> [Activer une opération](Path_OpActiveToggle/fr.md) : utilisé pour activer ou désactiver une opération d\'usinage.

-   <img alt="" src=images/Path_ToolBitLibraryOpen.svg  style="width:32px;"> [Gestionnaire des outils coupants](Path_ToolBitLibraryOpen/fr.md) : ouvre un éditeur pour gérer les bibliothèques des outils coupants.

-   <img alt="" src=images/Path_ToolBitDock.svg  style="width:32px;"> [Sélecteur d\'outils coupants](Path_ToolBitDock/fr.md) : active le menu du sélecteur des outils coupants.



### Opérations de base 

-   <img alt="" src=images/Path_Profile.svg  style="width:32px;"> [Contournage](Path_Profile/fr.md) : crée une opération de contour de l\'ensemble du modèle ou à partir d\'une ou plusieurs faces ou arêtes sélectionnées.

-   <img alt="" src=images/Path_Pocket_Shape.svg  style="width:32px;"> [Poche](Path_Pocket_Shape/fr.md) : crée une opération de poche à partir d\'une ou de plusieurs poches sélectionnées.

-   <img alt="" src=images/Path_Drilling.svg  style="width:32px;"> [Perçage](Path_Drilling/fr.md) : effectue un cycle de perçage.

-   <img alt="" src=images/Path_MillFace.svg  style="width:32px;"> [Surfaçage](Path_MillFace/fr.md) : crée un parcours de surfaçage.

-   <img alt="" src=images/Path_Helix.svg  style="width:32px;"> [Parcours hélicoïdal](Path_Helix/fr.md) : crée un parcours hélicoïdal.

-   <img alt="" src=images/Path_Adaptive.svg  style="width:32px;"> [Adaptation](Path_Adaptive/fr.md) : crée une opération adaptatif de compensation et de profilage.

-   <img alt="" src=images/Path_Slot.svg  style="width:32px;"> [Rainure](Path_Slot/fr.md) : crée une opération de rainurage à partir d\'entités sélectionnées ou de points personnalisés. [**Fonctions expérimentales**](Path_experimental/fr.md).

-   <img alt="" src=images/Path_Engrave.svg  style="width:32px;"> [Gravure](Path_Engrave/fr.md) : crée un parcours de gravure.

-   <img alt="" src=images/Path_Deburr.svg  style="width:32px;"> [Ebavurage](Path_Deburr/fr.md) : crée un parcours d\'ébavurage.

-   <img alt="" src=images/Path_Vcarve.svg  style="width:32px;"> [Gravure en V](Path_Vcarve/fr.md) : crée un parcours d\'usinage en utilisant une forme d\'outil en V.



### Opérations 3D 

-   <img alt="" src=images/Path_Pocket_3D.svg  style="width:32px;"> [Évidement 3D](Path_Pocket_3D/fr.md) : crée un parcours d\'usinage pour une poche 3D.

-   <img alt="" src=images/Path_Surface.svg  style="width:32px;"> [Surface](Path_Surface/fr.md) : crée un parcours d\'usinage pour une surface 3D. [**Fonctions expérimentales**](Path_experimental/fr.md).

-   <img alt="" src=images/Path_Waterline.svg  style="width:32px;"> [Contour par lignes de niveau](Path_Waterline/fr.md) : crée un tracé défini par lignes de niveau pour une surface 3D. [**Fonctions expérimentales**](Path_experimental/fr.md).



### Finitions de parcours 

-   <img alt="" src=images/Path_DressupAxisMap.svg  style="width:32px;"> [Assigner un axe](Path_DressupAxisMap/fr.md): assigne un axe par un autre.

-   <img alt="" src=images/Path_DressupPathBoundary.svg  style="width:32px;"> [Limitation d\'une zone](Path_DressupPathBoundary/fr.md) : ajoute une finition aux limites à un parcours d\'usinage sélectionné.

-   <img alt="" src=images/Path_DressupDogbone.svg  style="width:32px;"> [Dégagement des angles](Path_DressupDogbone/fr.md) : ajoute une finition pour l\'usinage des coins à un parcours d\'usinage sélectionné.

-   <img alt="" src=images/Path_DressupDragKnife.svg  style="width:32px;"> [Lame rotative](Path_DressupDragKnife/fr.md) : ajoute une finition pour lame rotative à un parcours d\'usinage sélectionné.

-   <img alt="" src=images/Path_DressupLeadInOut.svg  style="width:32px;"> [Entrée/sortie](Path_DressupLeadInOut/fr.md) : ajoute un point d\'entrée et/ou de sortie à un parcours d\'usinage sélectionné.

-   <img alt="" src=images/Path_DressupRampEntry.svg  style="width:32px;"> [Rampe d\'entrée](Path_DressupRampEntry/fr.md) : ajoute une finition de rampe d\'entrée d\'usinage à un parcours d\'usinage sélectionné.

-   <img alt="" src=images/Path_DressupTag.svg  style="width:32px;"> [Attache](Path_DressupTag/fr.md) : ajoute une modification à la finition de l\'attache de maintien d\'un parcours sélectionné.

-   <img alt="" src=images/Path_DressupZCorrect.svg  style="width:32px;"> [Correction en Z](Path_DressupZCorrect/fr.md): corrige la profondeur en Z à l\'aide d\'une sonde.



### Commandes supplémentaires 

-   <img alt="" src=images/Path_Fixture.svg  style="width:32px;"> [Fixation](Path_Fixture/fr.md) : change la position de la fixation.

-   <img alt="" src=images/Path_Comment.svg  style="width:32px;"> [Commentaire](Path_Comment/fr.md) : insère un commentaire dans le G-code d\'un parcours d\'outil.

-   <img alt="" src=images/Path_Stop.svg  style="width:32px;"> [Arrêter](Path_Stop/fr.md) : insère un arrêt complet de la machine.

-   <img alt="" src=images/Path_Custom.svg  style="width:32px;"> [Personnaliser](Path_Custom/fr.md) : insère un G-code personnalisé.

-   <img alt="" src=images/Path_Probe.svg  style="width:32px;"> [Sonde](Path_Probe/fr.md) : crée une grille de sondage à partir d\'un brut.

-   <img alt="" src=images/Path_Shape.svg  style="width:32px;"> [Parcours à partir de formes](Path_Shape/fr.md) : crée un objet parcours d\'usinage à partir d\'un objet Part sélectionné. [**Fonctions expérimentales**](Path_experimental/fr.md). {{Version/fr|0.19}}



### Modification du parcours d\'usinage 

-   <img alt="" src=images/Path_Copy.svg  style="width:32px;"> [Copie opération](Path_Copy/fr.md) : crée une copie paramétrique d\'un objet parcours sélectionné.

-   <img alt="" src=images/Path_Array.svg  style="width:32px;"> [Réseau](Path_Array/fr.md) : crée une copie en réseau en dupliquant un parcours sélectionné.

-   <img alt="" src=images/Path_SimpleCopy.svg  style="width:32px;"> [Copie simple](Path_SimpleCopy/fr.md) : crée une copie non paramétrique d\'un objet parcours sélectionné.



### Opérations spécialisées 

-   <img alt="" src=images/Path_ThreadMilling.svg  style="width:32px;"> [Fraisage de filets](Path_ThreadMilling/fr.md): crée une opération de fraisage de filets de parcours à partir des fonctions d\'un objet de base. [**Expérimental**](Path_experimental/fr.md).



### Divers

-   <img alt="" src=images/Path_Area.svg  style="width:32px;"> [Surface](Path_Area/fr.md) : crée une zone d\'usinage à partir d\'objets sélectionnés. [**Fonctions expérimentales**](Path_experimental/fr.md).

-   <img alt="" src=images/Path_Area_Workplane.svg  style="width:32px;"> [Plan de travail](Path_Area_Workplane/fr.md) : crée une zone d\'usinage plane. [**Fonctions expérimentales**](Path_experimental/fr.md).



### Obsolète

-   <img alt="" src=images/Path_ToolLibraryEdit.svg  style="width:32px;"> [Gestionnaire d\'outils](Path_ToolLibraryEdit/fr.md) : modifier le gestionnaire d\'outils. Système d\'outils \"historiques\". {{VersionMinus/fr|0.18}}



## Architecture des outils coupants 

Gestion des outils, des forets et de la bibliothèque d\'outils. Basé sur l\'architecture des outils coupants.

-   [Path Outils](Path_Tools/fr.md)
-   [Path Forme de l\'outil](Path_ToolShape/fr.md)
-   [Path Outil coupant](Path_ToolBit/fr.md)
-   [Path Bibliothèque des outils coupants](Path_ToolBit_Library/fr.md)
-   [Path Contrôleur d\'outil](Path_ToolController/fr.md)



## Autre

-   [Path FAQ](Path_FAQ/fr.md) : l\'atelier Path partage de nombreux concepts avec d\'autres logiciels de FAO mais possède ses propres particularités. Si quelque chose ne va pas, c\'est un bon point de départ.
-   [Path Feuille de configuration](Path_SetupSheet/fr.md) : vous pouvez utiliser une Feuille de configuration pour personnaliser la façon dont les diverses valeurs de propriété pour les opérations sont calculées.
-   [Path Personnalisation du post-processeur](Path_Postprocessor_Customization/fr.md) : si vous avez une machine spéciale qui ne peut pas utiliser l\'un des post-processeurs disponibles, vous pouvez avoir besoin d\'écrire votre propre post-processeur.
-   [Path Quatrième axe](Path_fourth_axis/fr.md) : fraisage expérimental sur quatre axes.



## Préférences

-   <img alt="" src=images/Preferences-path.svg  style="width:32px;"> [Préférences\...](Path_Preferences/fr.md) : préférences disponibles dans l\'atelier Path.



## Script

Voir la page [Path Ecrire un script](Path_scripting/fr.md).



## Tutoriels

-   [Tutoriel Path, pas à pas pour l\'impatient](Path_Walkthrough_for_the_Impatient/fr.md) : un tutoriel rapide pour se familiariser avec Path.



## Vidéos

-   [FreeCAD Path : Custom paths with Python - Part 1 - 5](https://www.youtube.com/playlist?list=PLEuOia-QxyFKgzAeTyH62GKqWKVURiWJL) : une playlist avec une série de 5 vidéos en anglais par sliptonic. Cette série montre comment travailler avec l\'[atelier Path](Path_Workbench/fr.md).
-   [FreeCAD CAM Path Workbench](https://www.youtube.com/playlist?list=PLUrr_kHPp4vhGdLlj6IemtF-OPUlRvSTC) : une playlist avec une série de 7 vidéos en anglais par CAD CAM Lessons.
-   [FreeCAD CAM CNC](https://www.youtube.com/playlist?list=PLUrr_kHPp4vh2n6DcIlegK4dEKIFjmISJ) : une playlist avec une série de 8 vidéos en anglais par CAD CAM Lessons.



## Feuille de route 

-   [Path Plan de développement](Path_Development_Roadmap/fr.md) : lisez ceci si vous êtes un développeur et que vous souhaitez contribuer à Path.





{{Path_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Path Workbench/fr
