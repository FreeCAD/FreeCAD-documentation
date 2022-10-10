# Release notes 1.0/fr
**FreeCAD 1.0 est en cours de développement, il n'y a pas encore de date de sortie prévue.**


{{Message|
Des fonctionnalités sont-elles manquantes? Mentionnez-les dans les [https   *//forum.freecadweb.org/viewtopic.php?f&#61;10&t&#61;69438 Notes de publication pour v1.0] du fil du forum.

Voir [Contribuer à FreeCAD](Help_FreeCAD/fr.md) pour savoir comment contribuer à FreeCAD.
}}


{{Message|Toutes les images de cette page doivent utiliser le suffixe **_relnotes_1.0**}}


{{TOCright}}

**FreeCAD 1.0** a été publié le **JJ MM 2023**, téléchargez la depuis la page [Téléchargement](Download/fr.md). Cette page liste toutes les nouvelles fonctionnalités et les changements.

Les notes de versions plus anciennes de FreeCAD sont disponibles dans la [liste des notes de versions](Feature_list/fr#Notes_de_versions.md).

L\'endroit pour une image accrocheuse sélectionnée par les administrateurs sur le [forum des modèles des utilisateurs](https   *//forum.freecadweb.org/viewforum.php?f=24).

## Général

## Interface utilisateur 

   
  <img alt="" src=images/Measurement-Part_relnotes_1.0.png  style="width   *384px;">   Le style d\'affichage des résultats de [mesure](Part_Workbench/fr#Mesure.md) créés à l\'aide de l\'[atelier Part](Part_Workbench/fr.md) ou de l\'[atelier PartDesign](PartDesign_Workbench/fr.md) peut désormais être modifié dans les [Préférences](PartDesign_Preferences/fr#Mesure.md). [Pull request #7148](https   *//github.com/FreeCAD/FreeCAD/pull/7148)
   

### Autres améliorations de l\'interface utilisateur 

-   Il est désormais possible de définir une transparence par défaut pour les nouveaux objets de [Part](Part_Module/fr.md) ou [PartDesign](PartDesign_Workbench/fr.md) dans les [Préférences](PartDesign_Preferences/fr.md). [Pull request #7103](https   *//github.com/FreeCAD/FreeCAD/pull/7103)
-   Un bouton a été ajouté pour changer les couleurs du dégradé de fond de la [Vue 3D](3D_view/fr.md) dans les [Réglages des préférences](Preferences_Editor/fr#Couleurs.md). [Pull request #7155](https   *//github.com/FreeCAD/FreeCAD/pull/7155)
-   Des commandes pour [enregistrer](Std_StoreWorkingView/fr.md) et [rappeler](Std_RecallWorkingView/fr.md) une vue de travail temporaire ont été ajoutées. [Pull request #7525](https   *//github.com/FreeCAD/FreeCAD/pull/7525)
-   Les changements de valeur avec la molette de la souris dans les \"champs de saisie\" (un type de widget utilisé pour entrer des valeurs dans les panneaux de tâches, par exemple par [Draft Ligne](Draft_Line/fr.md)) sont désactivés si le widget n\'a pas le focus et si [ComboBoxWheelEventFilter](Fine-tuning/fr.md) est activé. Cela permet d\'éviter les changements de valeur indésirables lors du défilement, comme c\'était déjà le cas pour les boîtes d\'incrémentx et les boîtes combo. [request #7561](https   *//github.com/FreeCAD/FreeCAD/pull/7561%7CPull)

## Noyau et API 

### Noyau

### API


<div class="mw-collapsible mw-collapsed toccolours">

#### Nouvelles API en Python 


<div class="mw-collapsible-content">

-   *BSplineSurfacePy   *   *scaleKnotsToBounds*    * met à l\'échelle les listes de nœuds U et V pour les adapter aux limites spécifiées. [Pull request #7258](https   *//github.com/FreeCAD/FreeCAD/pull/7258) et [Pull request #7385](https   *//github.com/FreeCAD/FreeCAD/pull/7385).
-   *BSplineCurvePy   *   *scaleKnotsToBounds*    * met à l\'échelle la liste des nœuds pour s\'adapter aux limites spécifiées. [Pull request #7385](https   *//github.com/FreeCAD/FreeCAD/pull/7385)

-   *ShapeFix_EdgeConnectPy*    * classe racine pour les opérations de fixation. [commit 4d4adb93](https   *//github.com/FreeCAD/FreeCAD/commit/4d4adb93)
-   *ShapeFix_EdgePy*    * correction d\'un bord invalide. [commit 4089cbfb](https   *//github.com/FreeCAD/FreeCAD/commit/4089cbfb)
-   *ShapeFix_FaceConnectPy*    * Reconstruit la connectivité entre les faces dans le shell. [commit a0eb2e9d](https   *//github.com/FreeCAD/FreeCAD/commit/a0eb2e9d)
-   *ShapeFix_FacePy*    * classe pour les opérations de fixation sur les faces. [commit b6cd635c](https   *//github.com/FreeCAD/FreeCAD/commit/b6cd635c)
-   *ShapeFix_FixSmallFacePy*    * classe pour fixer les opérations sur les faces. [commit 4c2946c8](https   *//github.com/FreeCAD/FreeCAD/commit/4c2946c8)
-   *ShapeFix_FixSmallSolidPy*    * correction des solides de petite taille. [commit b70d8d37](https   *//github.com/FreeCAD/FreeCAD/commit/b70d8d37)
-   *ShapeFix_FreeBoundsPy*    * destinée à fournir les limites libres de la forme. [commit 1ee1aee1](https   *//github.com/FreeCAD/FreeCAD/commit/1ee1aee1)
-   *ShapeFix_RootPy*    * classe racine pour les opérations de fixation. [commit f3e941a3](https   *//github.com/FreeCAD/FreeCAD/commit/f3e941a3)
-   *ShapeFix_ShapePy*    * classe pour fixer les opérations sur les formes. [commit 87db9dcc](https   *//github.com/FreeCAD/FreeCAD/commit/87db9dcc)
-   *ShapeFix_ShapeTolerancePy*    * modifie les tolérances des sous formes (sommets, arêtes, faces). [commit 125d5b63](https   *//github.com/FreeCAD/FreeCAD/commit/125d5b63)
-   *ShapeFix_ShellPy*    * classe racine pour les opérations de fixation. [commit f3e941a3](https   *//github.com/FreeCAD/FreeCAD/commit/f3e941a3)
-   *ShapeFix_SolidPy*    * classe racine pour les opérations de fixation. [commit 8d568793](https   *//github.com/FreeCAD/FreeCAD/commit/8d568793)
-   *ShapeFix_SplitCommonVertexPy*    * classe pour les opérations de fixation sur les formes. [commit 4b44c54c](https   *//github.com/FreeCAD/FreeCAD/commit/4b44c54c)
-   *ShapeFix_SplitToolPy*    * outil pour diviser et couper les bords. [commit bbecc3f2](https   *//github.com/FreeCAD/FreeCAD/commit/bbecc3f2)
-   *ShapeFix_WireframePy*    * fournit des méthodes pour fixer le fil de fer d\'une forme. [commit 6843a461](https   *//github.com/FreeCAD/FreeCAD/commit/6843a461)
-   *ShapeFix_WirePy*    * classe pour fixer les opérations sur les fils. [commit 94f6279a](https   *//github.com/FreeCAD/FreeCAD/commit/94f6279a)
-   *ShapeFix_WireVertexPy*    * fixation des arêtes déconnectées dans le fil. [commit 8c6ffc99](https   *//github.com/FreeCAD/FreeCAD/commit/8c6ffc99)


</div>

#### Suppression d\'API Python 

-   *FreeCAD.EndingAdd*    * remplacé par *FreeCAD.addImportType*. [Pull request #7167](https   *//github.com/FreeCAD/FreeCAD/pull/7167)
-   *FreeCAD.EndingGet*    * remplacé par *FreeCAD.getImportType*. [Pull request #7167](https   *//github.com/FreeCAD/FreeCAD/pull/7167)


</div>

## Gestionnaire d\'Addon 

## Atelier Arch 

### Autres améliorations de Arch 

-   Les objets [Profilé](Arch_Profile/fr.md) permettent désormais de modifier le type du Profilé après la création. [Pull request #7217](https   *//github.com/FreeCAD/FreeCAD/pull/7217)

## Atelier Draft 

-   Le manque de précision de [Draft Aimantation Le plus proche](Draft_Snap_Near/fr.md) lors de l\'aimantation à des courbes a été corrigé. De plus, [Draft Aimantation Perpendiculaire](Draft_Snap_Perpendicular/fr.md) peut maintenant aussi s\'accrocher à des faces et trouver des points multiples. Pour s\'accrocher à un sommet (par exemple un [Draft Point](Draft_Point/fr.md)) [Draft Aimantation Terminaison](Draft_Snap_Endpoint/fr.md) doit maintenant être utilisé au lieu de [Draft Aimantation Le plus proche](Draft_Snap_Near/fr.md). [Pull request #7132](https   *//github.com/FreeCAD/FreeCAD/pull/7132)
-   Pour faciliter le travail avec des [calques](Draft_Layer/fr.md), leur comportement de glisser-déposer a été modifié. Si vous déposez un objet d\'un [Std Groupe](Std_Group/fr.md), ou un objet de type groupe tel qu\'un [Arch Partie de bâtiment](Arch_BuildingPart/fr.md), sur un calque, il n\'est plus retiré du groupe, et vice versa. Cela fonctionne sans maintenir la touche **Ctrl** enfoncée. [Pull request #7462](https   *//github.com/FreeCAD/FreeCAD/pull/7462)

### Autres améliorations de Draft 

## Atelier FEM 

   
  <img alt="" src=images/FEM_Elmer-Multithread_relnotes_1.0.png  style="width   *384px;">   Résultat de simulation où 8 régions maillées sont visibles (une pour chaque cœur de CPU utilisé). Il est maintenant possible d\'exécuter le solveur [Elmer](FEM_SolverElmer/fr.md) en utilisant plusieurs cœurs de CPU. Pour plus d\'informations sur les avertissements, voir [ce post du forum](https   *//forum.freecadweb.org/viewtopic.php?p=610617#p610617) [Pull request #7159](https   *//github.com/FreeCAD/FreeCAD/pull/7159)
   

### Autres améliorations de FEM 

-   Il existe maintenant une <img alt="" src=images/FEM_ConstraintInitialPressure.svg  style="width   *32px;"> [contrainte de pression initiale](FEM_ConstraintInitialPressure/fr.md) pour définir la pression interne initiale des fluides. [Pull request #7364](https   *//github.com/FreeCAD/FreeCAD/pull/7364)
-   La <img alt="" src=images/FEM_ConstraintBodyHeatSource.svg  style="width   *32px;"> [Contrainte source thermique](FEM_ConstraintBodyHeatSource/fr.md) a maintenant un panneau de tâches et il est possible de définir la chaleur pour plusieurs corps ou d\'utiliser plusieurs contraintes pour différents corps dans une analyse. [Pull request #7367](https   *//github.com/FreeCAD/FreeCAD/pull/7367)
-   Il est maintenant possible d\'ouvrir (et ainsi de visualiser) des fichiers \*.pvtu (données de grille non structurées VTK partitionnées). Un fichier \*.pvtu est également le résultat d\'une simulation par [Elmer](FEM_SolverElmer/fr.md), lorsque plus d\'un coeur de CPU a été utilisé. [Pull request #7159](https   *//github.com/FreeCAD/FreeCAD/pull/7159)
-   Le rapport de déformation critique a été ajouté au pipeline de résultats de VTK. Il donne une indication de la rupture ductile pour les matériaux avec un objet \"MaterialMechanicalNonlinear\" (Matériau mécanique non linéaire). [Pull request #7467](https   *//github.com/FreeCAD/FreeCAD/pull/7467)

## Exportation

## Mesh

### Autres améliorations de Mesh 

## Atelier OpenSCAD 

## Atelier Part 

### Autres améliorations de Part 

## Atelier PartDesign 

### Autres améliorations de PartDesign 

## Atelier Path 

-   Intégration de Camotics. Si Camotics (version 1.2.2 ou ultérieure) est installé, une nouvelle icône sera ajoutée à la barre d\'outils Path. Sélectionnez une Path Tâche et appuyez sur le bouton pour ouvrir la boîte de dialogue Camotics. Faites ensuite glisser le curseur pour générer un solide simulé en tout point du travail. Vous pouvez également lancer l\'application Camotics complète pour exécuter la simulation animée. Cela entraîne un post-traitement silencieux de la tâche et la création d\'un fichier de projet camotics. [Pull request #6637](https   *//github.com/FreeCAD/FreeCAD/pull/6637)

-   Des chaînes de substitution supplémentaires pour le nommage automatique des sorties. Si la sortie est divisée en plusieurs fichiers, les noms de fichiers peuvent automatiquement substituer le label du contrôleur d\'outil, WCS, ou le label de l\'opération. Ceci s\'ajoute aux autres chaînes de substitution existantes comme la date, le nom du travail, etc.

-   Implémentation de l\'option de brise-copeaux (Chipbreaking) pour les cycles de perçage de type débourrage. Le brise-copeaux émet un cycle G73 qui amène la commande à effectuer un très petit mouvement de rétraction pour casser le copeau sans rétracter complètement la mèche du trou. G73 est supporté nativement par LinuxCNC. D\'autres postprocesseurs devront interpréter le G73 et émettre les codes de contrôle appropriés ou décomposer la rétraction en mouvements G1/G0. Le support des postprocesseurs pour la décomposition G73 a été ajouté aux postprocesseurs \"refactorisés\". [Pull request #7469](https   *//github.com/FreeCAD/FreeCAD/pull/7469).

## Module Plot 

## Atelier Sketcher 

   
  ![](images/sketcher-move-piece_relnotes_1.0.gif )   Faire glisser un B-spline ne déplace plus que la pièce entre les noeuds. [Pull request #7110](https   *//github.com/FreeCAD/FreeCAD/pull/7110)
                                                                                     
   

   
  ![](images/Sketcher_BackEdit_relnotes_1.0.gif )   Possibilité d\'éditer de manière transparente les esquisses depuis l\'avant ou l\'arrière. Lorsque vous travaillez depuis l\'arrière, les sommets (et toutes les géométries et contraintes) sont également sélectionnables et la vue en coupe est automatiquement basculée. [Pull request #7417](https   *//github.com/FreeCAD/FreeCAD/pull/7417)
                                                                                 
   

### Autres améliorations de Sketcher 

## Atelier Spreadsheet 

### Autres améliorations de Spreadsheet 

## Atelier TechDraw 

   
  <img alt="" src=images/TechDraw_SurfaceFinishExample_relnotes_1.0.png  style="width   *384px;">   Un nouvel outil [Symbole d\'état de surface](TechDraw_SurfaceFinishSymbol/fr.md) a été ajouté pour permettre la création de symboles de finition de surface décrivant la rugosité, la disposition et l\'ondulation, mais aussi le type de traitement de surface. Il prend en charge les styles ISO et ASME. Comme le montre l\'image, l\'outil existant [Ligne de référence](TechDraw_LeaderLine/fr.md) peut être utilisé pour référencer correctement les symboles orientés vers les bords d\'un objet. [Pull request #7227](https   *//github.com/FreeCAD/FreeCAD/pull/7227)
   

### Autres améliorations de TechDraw 

-   La prise en charge des espaces ajustables pour les lignes d\'extension des [dimensions](TechDraw_Preferences/fr#Dimensions.md) a été ajoutée. [Pull request #7133](https   *//github.com/FreeCAD/FreeCAD/pull/7133)
-   Suppression des fonctions obsolètes    * DrawViewPart   *   *replaceCenterLine, DrawViewPart   *   *replaceCosmeticEdge, DrawViewPart   *   *replaceCosmeticVertex et DrawViewPart   *   *replaceGeomFormat.

## Web

## Ateliers externes 

### A2plus

### Assembly3

### Assembly4

### FCGear

### Ship

## Compilation

Depuis cette version, FreeCAD ne peut être compilé qu\'avec Qt 5.x et Python 3.x. La version la plus basse de Python supportée est la 3.8 selon le [Cycle de développement de FreeCAD 1.0](FreeCAD_1.0_Development_Cycle/fr.md).

Pour compiler FreeCAD voir les instructions pour [Windows](Compile_on_Windows/fr.md), [Linux](Compile_on_Linux/fr.md) et [MacOS](Compile_on_MacOS/fr.md).

Les systèmes d\'exploitation pris en charge sont    *

-   Windows 7, 8, 10 et 11
-   Linux Ubuntu Focal Fossa (20.04) et plus récent
-   MacOS    * 10.12 Sierra ou plus récent

## Limitations connues 

### Windows 32 bits 

Depuis FreeCAD 0.19, nous ne supportons plus officiellement Windows 32 bits. FreeCAD pourrait fonctionner sur ces systèmes, mais aucun support n\'est donné.

### Bureau distant sous Windows 

Selon les capacités graphiques OpenGL d\'un ordinateur, il se peut que l\'on rencontre un plantage lors de l\'exécution de FreeCAD via le bureau à distance. Pour résoudre ce problème, mettez à jour votre pilote OpenGL. Si cela ne vous aide pas    *

-   Téléchargez [cette bibliothèque OpenGL](https   *//downloads.fdossena.com/geth.php?r=mesa64-latest) pour Windows 64 bits et extrayez-la.
-   Renommez le fichier DLL en *opengl32sw.dll* et copiez-le dans le sous-dossier *bin* du dossier d\'installation de FreeCAD (écrasez la DLL existante).

### MacOS    * l\'atelier Start affiche une page blanche 

Si l\'[atelier Start](Start_Workbench/fr.md) n\'affiche qu\'une page blanche, vous devez activer l\'option **Utiliser le logiciel OpenGL** dans le menu **Edition → Préférences → Affichage**.

[Category   *News](Category_News.md) [Category   *Documentation](Category_Documentation.md) [Category   *Releases](Category_Releases.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 1.0/fr
