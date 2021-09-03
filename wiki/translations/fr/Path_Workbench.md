




<img alt="Icône de l\'Atelier Path" src=images/Workbench_Path.svg  style="width:128px;">


{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

L\'<img alt="" src=images/Workbench_Path.svg  style="width:24px;"> [atelier Path](Path_Workbench/fr.md) est utilisé pour produire les instructions machine pour les machines CNC [à commande numérique](https://fr.wikipedia.org/wiki/Programmation_de_commande_numérique) à partir d\'un modèle 3D FreeCAD. Celui-ci produit des objets 3D réels sur des machines CNC telles que des fraiseuses, des tours, des découpeuses laser ou similaires. Généralement, les instructions sont en langage [G-Code](https://fr.wikipedia.org/wiki/Programmation_de_commande_num%C3%A9rique).


</div>

<img alt="" src=images/pathwb.png  style="width:600px;">


<div class="mw-translate-fuzzy">

Le flux de travail de l\'atelier Path FreeCAD crée ces instructions machine comme suit :

-   Un modèle 3D est l\'objet de base, généralement créé à l\'aide d\'un ou plusieurs des ateliers [Part Design](PartDesign_Workbench/fr.md), [Part](Part_Workbench/fr.md) ou [Draft](Draft_Module/fr.md).
-   Un [Travail (Tâche)](Path_Job/fr.md) est créé dans l\'atelier Path. Celui-ci contient toutes les informations nécessaires pour générer le G-Code nécessaire pour traiter l\'usinage sur une fraiseuse CNC : il y a le brut de matière (le stock), le [magasin d\'outils](Path_ToolLibraryEdit/fr.md) et il suit certaines commandes contrôlant la vitesse et les mouvements (généralement en G-Code).
-   Les outils sont sélectionnés comme requis par les opérations d\'usinage.
-   Les parcours de l\'outil de fraisage sont créés en utilisant par ex. des opérations de [Contournage](Path_Profile/fr.md) et [Poche](Path_Pocket_3D/fr.md). Ces [objets Parcours d\'usinage](Path_objects/fr.md) utilisent le langage G-Code interne à FreeCAD, indépendant de la machine CNC.
-   Le travail est exporté en G-Code, correspondant à votre machine. Cette étape s\'appelle *post-traitement*. Il y a différents post-processeurs disponibles.


</div>

## General concepts 


<div class="mw-translate-fuzzy">

## Concepts généraux 

L\'atelier Path génère le G-Code définissant les parcours d\'outils requis pour fabriquer le projet représenté par le modèle 3D sur la fraiseuse cible en [Format G-Code interne de FreeCAD](Path_scripting/fr#Le_Format_G-Code_interne_de_FreeCAD.md), qui est ensuite traduit dans le langage approprié pour le contrôleur CNC cible en sélectionnant le Post processeur approprié.

Le G-Code est généré à partir des directives et des opérations contenues dans un Travail (Tâche) Path. Le Flux de travail des tâches les répertorie dans l\'ordre dans lequel elles seront exécutées. La liste est remplie en ajoutant des opérations Path, des optimisations Path, des commandes partielles Path, et des modifications Path à partir du menu Path, ou des boutons d\'interface graphique.


</div>

The G-code is generated from directives and Operations contained in a Path Job. The Job Workflow lists these in the order they will be executed. The list is populated by adding Path Operations, Path Dressups, Path Supplemental Commands, and Path Modifications from the Path Menu, or GUI buttons.


<div class="mw-translate-fuzzy">

L\'atelier Path fournit des outils de gestion (bibliothèque, table d\'outils), d\'inspection de G-Code et de simulation. Il relie le Post processeur et permet d\'importer et d\'exporter des modèles de Tâches.


</div>


<div class="mw-translate-fuzzy">

L\'atelier Path possède des dépendances externes, notamment :

1.  Les unités du modèle 3D FreeCAD sont définies dans les paramètres **Édition → Préférences → Général → Onglet Unités Réglage des unités**. La configuration du Post processeur définit les unités G-Code finales.
2.  Le chemin du fichier Macro et les tolérances géométriques sont définis dans l\'onglet **Édition → Préférences → Path → Job Préférences**.
3.  Les couleurs sont définies dans l\'onglet **Édition → Préférences → Path → Couleurs de chemin**.
4.  Les paramètres des éléments de maintien sont définis dans l\'onglet **Édition → Préférences → Path → Trajectoires additionnelles (Dressups)**.
5.  Pour que la qualité du modèle 3D de base respecte les exigences de l\'atelier Path, utilisez Vérifier la géométrie.


</div>

## Limitations

Certaines limitations actuelles dont vous devez être conscient :

-   La plupart des outils de Path ne sont pas de véritables outils 3D mais uniquement compatibles 2.5D. Cela signifie qu\'ils prennent une forme 2D fixe et peuvent la découper à une profondeur donnée. Cependant, il existe deux outils qui produisent de véritables chemins 3D: **<img src="images/Path_3DPocket.svg" width=24px> [Poche 3D](Path_Pocket_3D/fr.md)** et **<img src="images/Path_3DSurface.svg" width=24px> [Surface 3D](Path_3DSurface/fr.md)** (qui est toujours une [fonction expérimentale](Path_experimental/fr.md) en novembre 2020).
-   La plupart des ateliers Path sont conçus pour une fraiseuse/routeur CNC standard à 3 axes (xyz) simple, mais les outils de tour sont en cours de développement dans la version 0.19\_pre.
-   La plupart des opérations dans l\'atelier Path renverront des chemins basés sur un outil/un trépan de fraise standard uniquement, quel que soit le type d\'outil/trépan affecté dans un contrôleur d\'outil donné, à l\'exception de **<img src="images/_Path_Engrave.svg" width=24px ]] [Gravure](Path_Engrave/fr.md)** et **![](images/)**.
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
5.  Si vous voulez que votre post-processeur configurable produise un gcode impérial (G20), placez l\'argument correct dans votre config de sortie de travail (ie \--inches pour [linuxcnc](http://linuxcnc.org/)). Cela peut être stocké dans un modèle de travail et défini comme modèle par défaut pour le rendre automatique pour tous les travaux futurs

Path Inspection :

1.  Si vous utilisez l\'outil Path Inspect pour regarder le g-code, vous le verrez en \'mm/s\' car il n\'est pas post-traité

## Heights and depths 


<div class="mw-translate-fuzzy">

## Commandes Path 

De nombreuses commandes ont différentes hauteurs et profondeurs : <img alt="" src=images/Path-DepthsAndHeights.gif  style="width:500px;"> 
*Référence visuelle pour les propriétés de profondeur (paramètres)*


</div>

<img alt="" src=images/Path-DepthsAndHeights.gif  style="width:500px;"> 
*Visual reference for Depth properties (settings)*

## Commands

Some commands are experimental and not available by default. To enable them see [Path experimental](Path_experimental.md).

### Project Commands 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Job.svg  style="width:32px;"> [Tâche](Path_Job/fr.md) : Crée une nouvelle tâche CNC


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_PostProcess.svg  style="width:32px;"> [Post Processeur](Path_Post/fr.md) : Exporte un projet en G-code


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Sanity.svg  style="width:32px;"> [Rechercher les erreurs](Path_Sanity/fr.md) : Vérifie le travail sélectionné pour les valeurs manquantes.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_ExportTemplate.svg  style="width:32px;"> [Exporte comme Modèle](Path_ExportTemplate/fr.md) : Exportez le travail en cours en tant que modèle


</div>

### Tool Commands 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Inspect.svg  style="width:32px;"> [Inspecteur de G-Code ](Path_Inspect/fr.md): Affiche le G-Code pour vérification


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Simulator.svg  style="width:32px;"> [Simulateur d\'usinage](Path_Simulator/fr.md) : Montre l\'opération de fraisage comme sur la machine


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_SelectLoop.svg  style="width:32px;"> [Terminer une boucle](Path_SelectLoop/fr.md) : Complète une boucle à partir de deux arêtes sélectionnées


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_OpActiveToggle.svg  style="width:32px;"> [Activation d\'opération](Path_OpActiveToggle/fr.md) : Utilisé pour activer ou désactiver une opération d\'usinage


</div>

-   <img alt="" src=images/Path_ToolBitLibraryOpen.svg  style="width:32px;"> [ToolBit Library editor](Path_ToolBitLibraryOpen.md): Opens an editor to manage ToolBit libraries. <small>(v0.19)</small> 

-   <img alt="" src=images/Path_ToolBitDock.svg  style="width:32px;"> [ToolBit Dock](Path_ToolBitDock.md): Toggles the ToolBit Dock. <small>(v0.19)</small> 


<div class="mw-translate-fuzzy">

### Opérations de base de Path 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Profile.svg  style="width:32px;"> [Profile](Path_Profile/fr.md) (Nouveau dans la version 0.19) : crée une opération de profil de l\'ensemble du modèle, ou à partir d\'une ou plusieurs faces ou arêtes sélectionnées. Cette opération a combiné les opérations Contour, Faces de profil et Arêtes de profil préexistantes.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Pocket.svg  style="width:32px;"> [Poche](Path_Pocket_Shape/fr.md) : Crée une opération de poche à partir d\'une ou de plusieurs poches sélectionnées


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Drilling.svg  style="width:32px;"> [Perçage](Path_Drilling/fr.md) : Effectue un cycle de perçage


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Face.svg  style="width:32px;"> [Surfaçage](Path_MillFace/fr.md) : Crée un parcours de surfaçage


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Helix.svg  style="width:32px;"> [Helix](Path_Helix/fr.md) : Crée un parcours hélicoïdal


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Adaptive.svg  style="width:32px;"> [Adaptation](Path_Adaptive/fr.md) : Crée une opération adaptative de compensation et de profilage


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Slot.svg  style="width:32px;"> [Rainure](Path_Slot/fr.md) (Nouveau dans la version 0.19) : crée une opération de rainurage à partir d\'entités sélectionnées ou de points personnalisés.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Engrave.svg  style="width:32px;"> [Gravure](Path_Engrave/fr.md) : Crée un parcours de gravure


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Vcarve.svg  style="width:32px;"> [Vcarve](Path_Vcarve/fr.md) : Crée un parcours d\'usinage pour une poche 3D


</div>

### 3D Operations 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_3DPocket.svg  style="width:32px;"> [Poche 3D](Path_Pocket_3D/fr.md) : Crée un parcours d\'usinage pour une poche 3D


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_3DSurface.svg  style="width:32px;"> [Surface 3D](Path_3DSurface/fr.md) : Crée un parcours d\'usinage pour une surface 3D (expérimental, 0.19).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Waterline.svg  style="width:32px;"> [Contour par lignes de niveau](Path_Waterline/fr.md) : Crée un tracé défini par lignes de niveau pour une surface 3D (experimental, 0.19)


</div>


<div class="mw-translate-fuzzy">

### Habillage Path 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_DressupPathBoundary.svg  style="width:32px;"> [Habillage des limites](Path_DressupPathBoundary/fr.md) : Ajoute une modification d\'habillage des limites à un chemin sélectionné


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_DressupDogbone.svg  style="width:32px;"> [Usinage des coins](Path_DressupDogbone/fr.md) : Ajoute une modification pour l\'usinage des coins à un parcours d\'usinage sélectionné


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_DressupDragKnife.svg  style="width:32px;"> [Parcours de couteau](Path_DressupDragKnife/fr.md) : Ajoute une modification de parcours de couteau à un parcours d\'usinage sélectionné


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_DressupLeadInOut.svg  style="width:32px;"> [Point d\'entrée/sortie](Path_DressupLeadInOut/fr.md) : Ajoute un point d\'entrée et/ou de sortie à un parcours d\'usinage sélectionné


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_DressupRampEntry.svg  style="width:32px;"> [Rampe d\'entrée](Path_DressupRampEntry/fr.md) : Ajoute une rampe d\'entrée d\'usinage à un parcours d\'usinage sélectionné


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_DressupTag.svg  style="width:32px;"> [Balise d\'attache](Path_DressupTag/fr.md) : Ajoute une balise pour une attache de maintien à un parcours d\'usinage sélectionné


</div>


<div class="mw-translate-fuzzy">

### Commandes particulières 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Fixture.svg  style="width:32px;"> [Point de fixation](Path_Fixture/fr.md) : Change la position du point de fixation


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Comment.svg  style="width:32px;"> [Commentaire](Path_Comment/fr.md) : Insère un commentaire dans le G-code d\'un parcours d\'outil


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Stop.svg  style="width:32px;"> [Stop](Path_Stop/fr.md) : Insère un arrêt complet de la machine


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Custom.svg  style="width:32px;"> [Personnaliser](Path_Custom/fr.md) : Insère un G-code personnalisé


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Shape.svg  style="width:32px;"> [G-code à partir d\'une forme](Path_Shape/fr.md) : Crée un objet parcours d\'usinage à partir d\'un objet Pièce sélectionné


</div>


<div class="mw-translate-fuzzy">

### Modification du parcours d\'usinage 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Copy.svg  style="width:32px;"> [Copier](Path_Copy/fr.md) : Crée une copie paramétrique d\'un objet parcours sélectionné


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Array.svg  style="width:32px;"> [Copie en réseau](Path_Array/fr.md) : Crée une copie en réseau en dupliquant un parcours sélectionné


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_SimpleCopy.svg  style="width:32px;"> [Copie Simple](Path_SimpleCopy/fr.md) : Crée une copie non paramétrique d\'un objet parcours sélectionné


</div>

### Miscellaneous


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Area.svg  style="width:32px;"> [Zone d\'usinage](Path_Area/fr.md) : Crée une zone d\'usinage à partir d\'objets sélectionnés. En cours.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Area_Workplane.svg  style="width:32px;"> [Zone de travail plane](Path_Area_Workplane/fr.md) : Crée une zone d\'usinage plane. En cours.


</div>

### Obsolete


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_ToolLibraryEdit.svg  style="width:32px;"> [Gestionnaire d\'outils](Path_ToolLibraryEdit/fr.md) : Modifier le gestionnaire d\'outils


</div>

## ToolBit architecture 

Manage tools, bits, and the Tool Library. Based on the ToolBit architecture. <small>(v0.19)</small> 

-   [Path Tools](Path_Tools.md)
-   [Path ToolShape](Path_ToolShape.md)
-   [Path ToolBit](Path_ToolBit.md)
-   [Path ToolBit Library](Path_ToolBit_Library.md)
-   [Path ToolController](Path_ToolController.md)

## Other


<div class="mw-translate-fuzzy">

L\'atelier Path partage de nombreux concepts avec d\'autres progiciels de FAO, mais possède ses propres particularités. Si quelque chose ne va pas, c\'est peut-être un bon point de départ.


</div>


<div class="mw-translate-fuzzy">

### Préférences


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Std_DlgPreferences.svg  style="width:32px;"> [Préférences\...](Draft_Preferences/fr.md): Préférences disponibles dans Path Outils.


</div>

## Script


<div class="mw-translate-fuzzy">

Voir la page [Path Ecrire un script](Path_scripting/fr.md).


</div>

## Tutorials

-   [Path Walkthrough for the Impatient](Path_Walkthrough_for_the_Impatient.md): a quick tutorial to get familiar with Path.

## Videos

-   [FreeCAD Path: Custom paths with Python - Part 1 - 5](https://www.youtube.com/playlist?list=PLEuOia-QxyFKgzAeTyH62GKqWKVURiWJL): a playlist with a series of 5 videos in English by sliptonic. This series shows how to work with the [Path Workbench](Path_Workbench.md).
-   [FreeCAD CAM Path Workbench](https://www.youtube.com/playlist?list=PLUrr_kHPp4vhGdLlj6IemtF-OPUlRvSTC): a playlist with a series of 7 videos in English by CAD CAM Lessons.
-   [FreeCAD CAM CNC](https://www.youtube.com/playlist?list=PLUrr_kHPp4vh2n6DcIlegK4dEKIFjmISJ) a playlist with a series of 8 videos in English by CAD CAM Lessons.





{{Path_Tools_navi

}} 

[Category:Workbenches{{\#translation:}}](Category:Workbenches.md)
