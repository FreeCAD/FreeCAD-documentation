# <img alt="Icône de l\'atelier CAM" src=images/Workbench_CAM.svg  style="width:64px;"> CAM Workbench/fr




## Introduction

L\'<img alt="" src=images/Workbench_CAM.svg  style="width:24px;"> [atelier CAM](CAM_Workbench/fr.md) est utilisé pour produire les instructions machine pour les [machines à commande numérique (CNC)](https://fr.wikipedia.org/wiki/Programmation_de_commande_numérique) à partir d\'un modèle 3D FreeCAD. Celui-ci produit des objets 3D réels sur des machines CNC telles que des fraiseuses, des tours, des découpeuses laser ou similaires. Généralement, les instructions sont en langage [G-code](https://fr.wikipedia.org/wiki/Programmation_de_commande_num%C3%A9rique#Fonctions_pr%C3%A9paratoires_G). Un [exemple général de simulation de séquence de parcours d\'outils CNC](https://www.ange-softs.com/SIMULCNCHTML/index.html) est présenté ici.

<img alt="" src=images/pathwb.png  style="width:600px;">

Le flux de travail de l\'atelier CAM de FreeCAD crée ces instructions machine comme suit :

-   Un modèle 3D est l\'objet de base, généralement créé à l\'aide d\'un ou plusieurs des ateliers <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/fr.md), <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/fr.md) ou <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft](Draft_Workbench/fr.md).
-   Une [CAM Tâche](CAM_Job/fr.md) est créée dans l\'atelier CAM. Celle-ci contient toutes les informations nécessaires pour générer le G-code nécessaire pour traiter l\'usinage sur une fraiseuse CNC : il y a le brut de matière (ou stock), le [gestionnaire d\'outils](CAM_ToolBitLibraryOpen/fr.md) et elle suit certaines commandes contrôlant la vitesse et les mouvements (généralement en G-code).
-   Les [CAM Outils](CAM_Tools/fr.md) sont sélectionnés comme requis par les opérations d\'usinage.
-   Les parcours de l\'outil de fraisage sont créés en utilisant par ex. des opérations de [Profilage](CAM_Profile/fr.md) et [Poche](CAM_Pocket_3D/fr.md). Ces objets CAM utilisent le langage G-code interne à FreeCAD, indépendant de la machine CNC.
-   Le travail est exporté en G-code, correspondant à votre machine. Cette étape s\'appelle *post-traitement*. Il y a différents post-processeurs disponibles.



## Concepts généraux 

L\'atelier CAM génère un G-Code définissant les parcours pour usiner le projet représenté par le modèle 3D sur la fraiseuse cible au [format G-code interne de FreeCAD](CAM_scripting/fr#Le_Format_G-code_interne_de_FreeCAD.md), qui est ensuite traduit dans le langage approprié pour le contrôleur CNC cible en sélectionnant le post-processeur approprié.

Le G-code est généré à partir des directives et des opérations contenues dans une tâche de CAM. Le flux des tâches les répertorie dans l\'ordre desquelles elles seront exécutées. La liste est complétée en ajoutant des opérations, des habillages des parcours, des commandes supplémentaires et des modifications à partir du menu CAM ou par les boutons de l\'interface graphique.

L\'atelier CAM fournit un gestionnaire d\'outils (bibliothèque, table d\'outils), un outil d\'inspection du G-code et de simulation. Il relie le post-processeur et permet d\'importer et d\'exporter des modèles de tâches.

L\'atelier CAM possède des dépendances externes, notamment :

1.  Les unités du modèle 3D FreeCAD sont définies dans les paramètres **Édition → Préférences → Général → Système d'unités par défaut**. La configuration du post-processeur définit les unités G-code finales.
2.  Le chemin du fichier Macro et les tolérances géométriques sont définis dans l\'onglet **Édition → Préférences → CAM → Préférences des tâches**.
3.  Les couleurs sont définies dans l\'onglet **Édition → Préférences → CAM → Couleurs de parcours**.
4.  Les paramètres des éléments de maintien sont définis dans l\'onglet **Édition → Préférences → CAM → Finitions**.
5.  Pour que la qualité du modèle 3D de base respecte les exigences de l\'atelier CAM, utilisez Vérifier la géométrie.

## Limitations

Certaines limitations actuelles dont vous devez être conscient :

-   La plupart des outils de CAM ne sont pas de véritables outils 3D mais uniquement compatibles 2.5D. Cela signifie qu\'ils prennent une forme 2D fixe et peuvent la découper à une profondeur donnée. Cependant, il existe deux outils qui produisent de véritables parcours 3D : **<img src="images/CAM_3DPocket.svg" width=24px> [Évidement 3D](CAM_Pocket_3D/fr.md)** et **<img src="images/CAM_Surface.svg" width=24px> [Surfaçage 3D](CAM_Surface/fr.md)** (qui est toujours une [fonction expérimentale](CAM_experimental/fr.md) en novembre 2020).
-   La plupart des ateliers CAM sont conçus pour une fraiseuse/routeur CNC standard à 3 axes (xyz) simple, mais les outils de tour sont en cours de développement dans la version 0.19_pre.
-   La plupart des opérations dans l\'atelier CAM renverront des parcours basés sur un outil/un trépan de fraise standard uniquement, quel que soit le type d\'outil/trépan affecté dans un contrôleur d\'outil donné, à l\'exception de **![](images/)_[Gravure](CAM_Engrave/fr.md)** et **<img src="images/CAM_Surface.svg" width=24px> [Surfaçage 3D](CAM_Surface/fr.md)**.
-   Les opérations effectuées dans l\'atelier CAM ne connaissent pas les mécanismes de serrage utilisés pour fixer le modèle à votre machine. Par conséquent, veuillez vérifier et simuler les parcours que vous générez avant d\'envoyer le code à votre machine. Si nécessaire, modélisez vos serrages dans FreeCAD afin de mieux inspecter les parcours générés. Recherchez les éventuelles collisions avec les fixations ou autres obstacles sur les parcours.



## Unités

La gestion des unités dans CAM peut prêter à confusion. Il y a plusieurs points à comprendre :

1.  Les unités de base FreeCAD pour la longueur et le temps sont respectivement \"mm\" et \"s\". La vélocité est donc \"mm/s\". C\'est ce que FreeCAD stocke en interne indépendamment de toute autre chose
2.  Le schéma d\'unité par défaut utilise les unités par défaut. Si vous utilisez le schéma par défaut et que vous entrez un taux d\'avance sans chaîne d\'unité, il sera saisi en tant que \"mm/s\"
3.  La plupart des machines à commande numérique attendent un débit d\'alimentation sous forme de \"mm/min\" ou \"in/min\". La plupart des post-processeurs convertissent automatiquement l\'unité lors de la génération de gcode.

Schémas :

1.  Changer le schéma dans les préférences change la chaîne d\'unité par défaut pour les champs d\'entrée. Si vous êtes un utilisateur CAM et que vous préférez concevoir en métrique, il est fortement recommandé d\'utiliser le schéma \"Metric Small Parts & CNC\". Si vous concevez en unités américaines, Imperial Decimal et Building US fonctionneront.
2.  Changer le schéma de votre unité préférée n\'aura aucun effet sur la sortie, mais aidera à éviter les erreurs de saisie.

Sortie :

1.  La génération de l\'unité correcte en sortie relève de la responsabilité du post-processeur et n\'est effectuée qu\'à ce moment-là.
2.  L\'unité de sortie de la machine n\'a aucun rapport avec le schéma d\'unités que vous avez choisi.
3.  Les post-processeurs produisent une sortie métrique (G21), une sortie impériale (G20) ou sont configurables.
4.  Les post-processeurs configurables produisent par défaut une sortie métrique (G21).
5.  Si vous souhaitez que votre post-processeur configurable produise du G-code impérial (G20), définissez l\'argument correct dans la configuration de sortie de votre tâche (par exemple \--inches pour linuxcnc). Ceci peut être stocké dans un modèle de tâche et défini comme modèle par défaut pour le rendre automatique pour tous les tâches futures.

CAM Inspection :

1.  Si vous utilisez l\'outil CAM Inspection pour inspecter le G-code, vous le verrez en \"mm/s\" car il n\'est pas post-traité.



## Hauteurs et profondeurs 

De nombreuses commandes ont différentes hauteurs et profondeurs :

<img alt="" src=images/Path-DepthsAndHeights.gif  style="width:500px;"> 
*Référence visuelle pour les propriétés de profondeur (paramètres)*



## Commandes

Certaines commandes sont expérimentales et ne sont pas disponibles par défaut. Pour les activer, voir [CAM Fonctions expérimentales](CAM_experimental/fr.md).



### Commandes du projet 

-   <img alt="" src=images/CAM_Job.svg  style="width:32px;"> [Tâche](CAM_Job/fr.md) : crée une nouvelle tâche CNC.

-   <img alt="" src=images/CAM_Post.svg  style="width:32px;"> [Post-traitement](CAM_Post/fr.md) : exporte un projet en G-code.

-   <img alt="" src=images/CAM_Sanity.svg  style="width:32px;"> [Chercher des erreurs](CAM_Sanity/fr.md) : vérifie les valeurs manquantes dans la tâche sélectionnée.

-   <img alt="" src=images/CAM_ExportTemplate.svg  style="width:32px;"> [Exporter un modèle](CAM_ExportTemplate/fr.md) : exporte la tâche en cours en tant que modèle.



### Commandes d\'outils 

-   <img alt="" src=images/CAM_Inspect.svg  style="width:32px;"> [Inspecter des commandes](CAM_Inspect/fr.md) : affiche le G-code pour vérification.

-   <img alt="" src=images/CAM_Simulator.svg  style="width:32px;"> [Simulateur de parcours](CAM_Simulator/fr.md) : montre l\'opération d\'usinage comme le ferait la machine.

-   <img alt="" src=images/CAM_SimulatorGL.svg  style="width:32px;"> [Simulateur GL](CAM_SimulatorGL/fr.md) : active le nouveau simulateur de CAM. {{Version/fr|1.0}}

-   <img alt="" src=images/CAM_SelectLoop.svg  style="width:32px;"> [Sélectionner une boucle](CAM_SelectLoop/fr.md) : permet de sélectionner une boucle d\'arêtes.

-   <img alt="" src=images/CAM_OpActiveToggle.svg  style="width:32px;"> [Activer une opération](CAM_OpActiveToggle/fr.md) : utilisé pour activer ou désactiver une opération d\'usinage.

-   <img alt="" src=images/CAM_ToolBitLibraryOpen.svg  style="width:32px;"> [Gestionnaire des outils coupants](CAM_ToolBitLibraryOpen/fr.md) : ouvre un éditeur pour gérer les bibliothèques des outils coupants.

-   <img alt="" src=images/CAM_ToolBitDock.svg  style="width:32px;"> [Sélecteur d\'outils coupants](CAM_ToolBitDock/fr.md) : active le menu du sélecteur des outils coupants.



### Opérations de base 

-   <img alt="" src=images/CAM_Profile.svg  style="width:32px;"> [Profilage](CAM_Profile/fr.md) : crée une opération de profilage de l\'ensemble du modèle ou à partir d\'une ou plusieurs faces ou arêtes sélectionnées.

-   <img alt="" src=images/CAM_Pocket_Shape.svg  style="width:32px;"> [Poche](CAM_Pocket_Shape/fr.md) : crée une opération de poche à partir d\'une ou de plusieurs poches sélectionnées.

-   <img alt="" src=images/CAM_Drilling.svg  style="width:32px;"> [Perçage](CAM_Drilling/fr.md) : effectue un cycle de perçage.

-   <img alt="" src=images/CAM_MillFace.svg  style="width:32px;"> [Surfaçage](CAM_MillFace/fr.md) : crée un parcours de surfaçage.

-   <img alt="" src=images/CAM_Helix.svg  style="width:32px;"> [Parcours hélicoïdal](CAM_Helix/fr.md) : crée un parcours hélicoïdal.

-   <img alt="" src=images/CAM_Adaptive.svg  style="width:32px;"> [Adaptatif](CAM_Adaptive/fr.md) : crée une opération adaptative de détourage et de contournage.

-   <img alt="" src=images/CAM_Slot.svg  style="width:32px;"> [Rainure](CAM_Slot/fr.md) : crée une opération de rainurage à partir d\'entités sélectionnées ou de points personnalisés. [**Fonctions expérimentales**](CAM_experimental/fr.md).

-   <img alt="" src=images/CAM_Engrave.svg  style="width:32px;"> [Gravure](CAM_Engrave/fr.md) : crée un parcours de gravure.

-   <img alt="" src=images/CAM_Deburr.svg  style="width:32px;"> [Ebavurage](CAM_Deburr/fr.md) : crée un parcours d\'ébavurage.

-   <img alt="" src=images/CAM_Vcarve.svg  style="width:32px;"> [Gravure en V](CAM_Vcarve/fr.md) : crée un parcours d\'usinage en utilisant une forme d\'outil en V.



### Opérations 3D 

-   <img alt="" src=images/CAM_Pocket_3D.svg  style="width:32px;"> [Évidement 3D](CAM_Pocket_3D/fr.md) : crée un parcours d\'usinage pour une poche 3D.

-   <img alt="" src=images/CAM_Surface.svg  style="width:32px;"> [Surfaçage 3D](CAM_Surface/fr.md) : crée un parcours d\'usinage pour une surface 3D. [**Fonctions expérimentales**](CAM_experimental/fr.md).

-   <img alt="" src=images/CAM_Waterline.svg  style="width:32px;"> [Contour par lignes de niveau](CAM_Waterline/fr.md) : crée un tracé défini par lignes de niveau pour une surface 3D. [**Fonctions expérimentales**](CAM_experimental/fr.md).



### Finitions du parcours 

-   <img alt="" src=images/CAM_DressupAxisMap.svg  style="width:32px;"> [Assigner un axe](CAM_DressupAxisMap/fr.md): assigne un axe par un autre.

-   <img alt="" src=images/CAM_DressupPathBoundary.svg  style="width:32px;"> [Limitation d\'une zone](CAM_DressupPathBoundary/fr.md) : ajoute une limite à un parcours d\'usinage sélectionné.

-   <img alt="" src=images/CAM_DressupDogbone.svg  style="width:32px;"> [Dégagement des angles](CAM_DressupDogbone/fr.md) : ajoute une finition pour l\'usinage des coins à un parcours d\'usinage sélectionné.

-   <img alt="" src=images/CAM_DressupDragKnife.svg  style="width:32px;"> [Lame rotative](CAM_DressupDragKnife/fr.md) : ajoute une finition pour lame rotative à un parcours d\'usinage sélectionné.

-   <img alt="" src=images/CAM_DressupLeadInOut.svg  style="width:32px;"> [Entrée/sortie](CAM_DressupLeadInOut/fr.md) : ajoute un point d\'entrée et/ou de sortie à un parcours d\'usinage sélectionné.

-   <img alt="" src=images/CAM_DressupRampEntry.svg  style="width:32px;"> [Rampe d\'entrée](CAM_DressupRampEntry/fr.md) : ajoute une finition de rampe d\'entrée d\'usinage à un parcours d\'usinage sélectionné.

-   <img alt="" src=images/CAM_DressupTag.svg  style="width:32px;"> [Attache](CAM_DressupTag/fr.md) : ajoute une modification à la finition de l\'attache de maintien d\'un parcours sélectionné.

-   <img alt="" src=images/CAM_DressupZCorrect.svg  style="width:32px;"> [Correction en Z](CAM_DressupZCorrect/fr.md): corrige la profondeur en Z à l\'aide d\'une sonde.



### Commandes supplémentaires 

-   <img alt="" src=images/CAM_Fixture.svg  style="width:32px;"> [Décaler l\'origine](CAM_Fixture/fr.md) : change la position de l\'origine.

-   <img alt="" src=images/CAM_Comment.svg  style="width:32px;"> [Commentaire](CAM_Comment/fr.md) : insère un commentaire dans le G-code d\'un parcours d\'outil.

-   <img alt="" src=images/CAM_Stop.svg  style="width:32px;"> [Arrêter](CAM_Stop/fr.md) : insère un arrêt complet de la machine.

-   <img alt="" src=images/CAM_Custom.svg  style="width:32px;"> [Personnaliser](CAM_Custom/fr.md) : insère un G-code personnalisé.

-   <img alt="" src=images/CAM_Probe.svg  style="width:32px;"> [Sonde](CAM_Probe/fr.md) : crée une grille de sondage à partir d\'un brut.

-   <img alt="" src=images/CAM_Shape.svg  style="width:32px;"> [Parcours à partir de formes](CAM_Shape/fr.md) : crée un objet parcours d\'usinage à partir d\'un objet Part sélectionné. [**Fonctions expérimentales**](CAM_experimental/fr.md). {{Version/fr|0.19}}



### Modifications du parcours 

-   <img alt="" src=images/CAM_Copy.svg  style="width:32px;"> [Copie opération](CAM_Copy/fr.md) : crée une copie paramétrique d\'un objet parcours sélectionné.

-   <img alt="" src=images/CAM_Array.svg  style="width:32px;"> [Réseau](CAM_Array/fr.md) : crée une copie en réseau en dupliquant un parcours sélectionné.

-   <img alt="" src=images/CAM_SimpleCopy.svg  style="width:32px;"> [Copie simple](CAM_SimpleCopy/fr.md) : crée une copie non paramétrique d\'un objet parcours sélectionné.



### Opérations spécialisées 

-   <img alt="" src=images/CAM_ThreadMilling.svg  style="width:32px;"> [Fraisage de filets](CAM_ThreadMilling/fr.md): crée une opération de fraisage de filets à partir des fonctions d\'un objet de base. [**Fonctions expérimentales**](CAM_experimental/fr.md).



### Divers

-   <img alt="" src=images/CAM_Area.svg  style="width:32px;"> [Surface](CAM_Area/fr.md) : crée une zone d\'usinage à partir d\'objets sélectionnés. [**Fonctions expérimentales**](CAM_experimental/fr.md).

-   <img alt="" src=images/CAM_Area_Workplane.svg  style="width:32px;"> [Zone du plan de travail](CAM_Area_Workplane/fr.md) : crée une zone plane d\'usinage. [**Fonctions expérimentales**](CAM_experimental/fr.md).



## Architecture des outils coupants 

Gestion des outils, des forets et de la bibliothèque d\'outils. Basé sur l\'architecture des outils coupants.

-   [CAM Outils](CAM_Tools/fr.md)
-   [CAM Forme de l\'outil](CAM_ToolShape/fr.md)
-   [CAM Outil coupant](CAM_ToolBit/fr.md)
-   [CAM Bibliothèque des outils coupants](CAM_ToolBit_Library/fr.md)
-   [CAM Contrôleur d\'outil](CAM_ToolController/fr.md)



## Autre

-   [CAM FAQ](CAM_FAQ/fr.md) : l\'atelier CAM partage de nombreux concepts avec d\'autres logiciels de FAO mais possède ses propres particularités. Si quelque chose ne va pas, c\'est un bon point de départ.
-   [CAM Feuille de configuration](CAM_SetupSheet/fr.md) : vous pouvez utiliser une Feuille de configuration pour personnaliser la façon dont les diverses valeurs de propriété pour les opérations sont calculées.
-   [CAM Personnaliser le post-processeur](CAM_Postprocessor_Customization/fr.md) : si vous avez une machine spéciale qui ne peut pas utiliser l\'un des post-processeurs disponibles, vous pouvez avoir besoin d\'écrire votre propre post-processeur.
-   [CAM Quatrième axe](CAM_fourth_axis/fr.md) : fraisage expérimental sur quatre axes.



## Préférences

-   <img alt="" src=images/Preferences-path.svg  style="width:32px;"> [Préférences\...](CAM_Preferences/fr.md) : préférences disponibles dans l\'atelier CAM.



## Script

Voir la page [CAM Ecrire un script](CAM_scripting/fr.md).



## Tutoriels

-   [Tutoriel CAM, pas à pas pour l\'impatient](CAM_Walkthrough_for_the_Impatient/fr.md) : un tutoriel rapide pour se familiariser avec CAM.



## Vidéos

-   [FreeCAD Path : Custom paths with Python - Part 1 - 5](https://www.youtube.com/playlist?list=PLEuOia-QxyFKgzAeTyH62GKqWKVURiWJL) : une playlist avec une série de 5 vidéos en anglais par sliptonic. Cette série montre comment travailler avec l\'[atelier Path](CAM_Workbench/fr.md).
-   [FreeCAD CAM Path Workbench](https://www.youtube.com/playlist?list=PLUrr_kHPp4vhGdLlj6IemtF-OPUlRvSTC) : une playlist avec une série de 7 vidéos en anglais par CAD CAM Lessons.
-   [FreeCAD CAM CNC](https://www.youtube.com/playlist?list=PLUrr_kHPp4vh2n6DcIlegK4dEKIFjmISJ) : une playlist avec une série de 8 vidéos en anglais par CAD CAM Lessons.
-   Voir aussi la section [Fabrication assistée par ordinateur (FAO)](Video_tutorials/fr#Fabrication_assistée_par_ordinateur_(FAO).md) de la page wiki [Tutoriels vidéo](Video_tutorials/fr.md).



## Feuille de route 

-   [CAM Plan de développement](CAM_Development_Roadmap.md) : lisez ceci si vous êtes un développeur et que vous souhaitez contribuer à CAM.





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > CAM Workbench/fr
