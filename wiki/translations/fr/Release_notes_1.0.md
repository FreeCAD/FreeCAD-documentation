# Release notes 1.0/fr
**FreeCAD 1.0 est en cours de développement, il n'y a pas encore de date de sortie prévue.**


{{Message|
Des fonctionnalités sont-elles manquantes? Mentionnez-les dans les [https://forum.freecadweb.org/viewtopic.php?f&#61;10&t&#61;69438 Notes de publication pour v1.0] du fil du forum.

Voir [Contribuer à FreeCAD](Help_FreeCAD/fr.md) pour savoir comment contribuer à FreeCAD.
}}


{{Message|Toutes les images de cette page doivent utiliser le suffixe **_relnotes_1.0**}}


{{TOCright}}

**FreeCAD 1.0** a été publié le **JJ MM 2023**, téléchargez la depuis la page [Téléchargement](Download/fr.md). Cette page liste toutes les nouvelles fonctionnalités et les changements.

Les notes de versions plus anciennes de FreeCAD sont disponibles dans la [liste des notes de versions](Feature_list/fr#Notes_de_versions.md).

L\'endroit pour une image accrocheuse sélectionnée par les administrateurs sur le [forum des modèles des utilisateurs](https://forum.freecadweb.org/viewforum.php?f=24).



## Général



## Interface utilisateur 

   
  ![](images/Navi_Cube_relnotes_1.0.gif )   Les faces des coins du cube de navigation sont maintenant hexagonales et plus grandes, ce qui les rend plus faciles à cliquer. [Pull request #7876](https://github.com/FreeCAD/FreeCAD/pull/7876) et [Pull request #8266](https://github.com/FreeCAD/FreeCAD/pull/8266).
   

   
  <img alt="" src=images/Measurement-Part_relnotes_1.0.png  style="width:384px;">   Le style d\'affichage des résultats de [mesure](Part_Workbench/fr#Mesure.md) créés à l\'aide de l\'[atelier Part](Part_Workbench/fr.md) ou de l\'[atelier PartDesign](PartDesign_Workbench/fr.md) peut désormais être modifié dans les [Préférences](PartDesign_Preferences/fr#Mesure.md). [Pull request #7148](https://github.com/FreeCAD/FreeCAD/pull/7148)
   

   
  <img alt="" src=images/WbSelector_relnotes_1.0.png  style="width:300px;">   Le sélecteur d\'ateliers peut maintenant être placé de manière optionnelle dans la barre de menu au lieu de la zone de la barre d\'outils. [Pull request #7679](https://github.com/FreeCAD/FreeCAD/pull/7679)
   



### Autres améliorations de l\'interface utilisateur 

-   Le bouton pour <img alt="" src=images/Std_UserEditModeDefault.svg  style="width:24px;"> [Std Mode d\'édition](Std_UserEditMode/fr.md) a été supprimé de la barre d\'outils standard. Il peut être réintroduit en [personnalisant](Std_DlgCustomize/fr.md) votre barre d\'outils.[Pull request #7570](https://github.com/FreeCAD/FreeCAD/pull/7570)
-   Les boutons pour <img alt="" src=images/Std_Print.svg  style="width:24px;"> [Imprimer](Std_Print/fr.md), <img alt="" src=images/Std_Copy.svg  style="width:24px;"> [Copier](Std_Copy/fr.md), <img alt="" src=images/Std_Paste.svg  style="width:24px;"> [Coller](Std_Paste/fr.md) et <img alt="" src=images/Std_Cut.svg  style="width:24px;"> [Couper](Std_Cut/fr.md) ont été supprimés de la barre d\'outils standard. Ils peuvent être réintroduits en [personnalisant](Std_DlgCustomize/fr.md) votre barre d\'outils.[Pull request #7571](https://github.com/FreeCAD/FreeCAD/pull/7571) et [commit ea9a04e](https://github.com/FreeCAD/FreeCAD/commit/ea9a04e)
-   Des commandes pour [Std Stocker la vue de travail](Std_StoreWorkingView/fr.md) et [Std Rappel de la vue de travail](Std_RecallWorkingView/fr.md) temporaire ont été ajoutées. [Pull request #7525](https://github.com/FreeCAD/FreeCAD/pull/7525)
-   Les changements de valeur avec la molette de la souris dans les \"champs de saisie\" (type de widget utilisé pour entrer des valeurs dans les panneaux de tâches, par exemple par [Draft Ligne](Draft_Line/fr.md)) sont désactivés si le widget n\'a pas le focus et que [ComboBoxWheelEventFilter](Fine-tuning/fr#En_rapport_avec_la_souris.md) est activé. Cela permet d\'éviter les changements de valeur non désirés lors du défilement, comme c\'était déjà le cas pour les spin box et les combo box. [Pull request #7561](https://github.com/FreeCAD/FreeCAD/pull/7561)
-   Il est désormais possible de définir une transparence par défaut pour les nouveaux objets de [Part](Part_Module/fr.md) ou de [PartDesign](PartDesign_Workbench/fr.md) dans les [Préférences](PartDesign_Preferences/fr.md). [Pull request #7103](https://github.com/FreeCAD/FreeCAD/pull/7103)
-   Il y a le nouveau style d\'orbite **Vue en rotation**. Il peut être activé dans les [Réglages des préférences](Preferences_Editor/fr#Navigation.md) ou en appuyant sur le bouton **[<img src=images/NavigationCAD_dark.svg style="width:16px">** dans la [Barre d\'état](Status_bar/fr.md) et ensuite en utilisant le menu **Réglages → Style d'orbite**. [Pull Request #8048](https://github.com/FreeCAD/FreeCAD/pull/8048)
-   Le panneau de tâches [Std Apparence](Std_SetAppearance/fr.md) possède désormais également un bouton permettant de définir la propriété Couleur du point. [Pull request #7708](https://github.com/FreeCAD/FreeCAD/pull/7708)
-   Un bouton a été ajouté pour changer les couleurs du gradient d\'arrière-plan de la [vue 3D](3D_view/fr.md) dans l\'[éditeur de préférences](Preferences_Editor/fr#Couleurs.md). [Pull request #7155](https://github.com/FreeCAD/FreeCAD/pull/7155)
-   Tous les paramètres de transparence utilisent désormais le pas uniforme de 5% du bouton rotatif : un clic sur le bouton dans une boîte de dialogue ou dans l\'éditeur de propriétés modifie la transparence de 5%. Maintenez le bouton enfoncé pour modifier plusieurs pas de 5% à la fois. [Pull request #7723](https://github.com/FreeCAD/FreeCAD/pull/7723)
-   La fenêtre de sortie a été renommée en Vue rapport pour une uniformité avec l\'interface utilisateur. [Pull Request #7739](https://github.com/FreeCAD/FreeCAD/pull/7739)



## Noyau et API 



### Noyau

### API


<div class="mw-collapsible mw-collapsed toccolours">



#### Nouvelles API en Python 


<div class="mw-collapsible-content">

-   *BSplineSurfacePy::scaleKnotsToBounds* : met à l\'échelle les listes de nœuds U et V pour les adapter aux limites spécifiées. [Pull request #7258](https://github.com/FreeCAD/FreeCAD/pull/7258) et [Pull request #7385](https://github.com/FreeCAD/FreeCAD/pull/7385).
-   *BSplineCurvePy::scaleKnotsToBounds* : met à l\'échelle la liste des nœuds pour s\'adapter aux limites spécifiées. [Pull request #7385](https://github.com/FreeCAD/FreeCAD/pull/7385)

-   *ShapeFix_EdgeConnectPy* : classe racine pour les opérations de fixation. [commit 4d4adb93](https://github.com/FreeCAD/FreeCAD/commit/4d4adb93)
-   *ShapeFix_EdgePy* : correction d\'un bord invalide. [commit 4089cbfb](https://github.com/FreeCAD/FreeCAD/commit/4089cbfb)
-   *ShapeFix_FaceConnectPy* : Reconstruit la connectivité entre les faces dans le shell. [commit a0eb2e9d](https://github.com/FreeCAD/FreeCAD/commit/a0eb2e9d)
-   *ShapeFix_FacePy* : classe pour les opérations de fixation sur les faces. [commit b6cd635c](https://github.com/FreeCAD/FreeCAD/commit/b6cd635c)
-   *ShapeFix_FixSmallFacePy* : classe pour fixer les opérations sur les faces. [commit 4c2946c8](https://github.com/FreeCAD/FreeCAD/commit/4c2946c8)
-   *ShapeFix_FixSmallSolidPy* : correction des solides de petite taille. [commit b70d8d37](https://github.com/FreeCAD/FreeCAD/commit/b70d8d37)
-   *ShapeFix_FreeBoundsPy* : destinée à fournir les limites libres de la forme. [commit 1ee1aee1](https://github.com/FreeCAD/FreeCAD/commit/1ee1aee1)
-   *ShapeFix_RootPy* : classe racine pour les opérations de fixation. [commit f3e941a3](https://github.com/FreeCAD/FreeCAD/commit/f3e941a3)
-   *ShapeFix_ShapePy* : classe pour fixer les opérations sur les formes. [commit 87db9dcc](https://github.com/FreeCAD/FreeCAD/commit/87db9dcc)
-   *ShapeFix_ShapeTolerancePy* : modifie les tolérances des sous formes (sommets, arêtes, faces). [commit 125d5b63](https://github.com/FreeCAD/FreeCAD/commit/125d5b63)
-   *ShapeFix_ShellPy* : classe racine pour les opérations de fixation. [commit f3e941a3](https://github.com/FreeCAD/FreeCAD/commit/f3e941a3)
-   *ShapeFix_SolidPy* : classe racine pour les opérations de fixation. [commit 8d568793](https://github.com/FreeCAD/FreeCAD/commit/8d568793)
-   *ShapeFix_SplitCommonVertexPy* : classe pour les opérations de fixation sur les formes. [commit 4b44c54c](https://github.com/FreeCAD/FreeCAD/commit/4b44c54c)
-   *ShapeFix_SplitToolPy* : outil pour diviser et couper les bords. [commit bbecc3f2](https://github.com/FreeCAD/FreeCAD/commit/bbecc3f2)
-   *ShapeFix_WireframePy* : fournit des méthodes pour fixer le fil de fer d\'une forme. [commit 6843a461](https://github.com/FreeCAD/FreeCAD/commit/6843a461)
-   *ShapeFix_WirePy* : classe pour fixer les opérations sur les fils. [commit 94f6279a](https://github.com/FreeCAD/FreeCAD/commit/94f6279a)
-   *ShapeFix_WireVertexPy* : fixation des arêtes déconnectées dans le fil. [commit 8c6ffc99](https://github.com/FreeCAD/FreeCAD/commit/8c6ffc99)


</div>



#### Suppression d\'API Python 

-   *FreeCAD.EndingAdd* : remplacé par *FreeCAD.addImportType*. [Pull request #7167](https://github.com/FreeCAD/FreeCAD/pull/7167)
-   *FreeCAD.EndingGet* : remplacé par *FreeCAD.getImportType*. [Pull request #7167](https://github.com/FreeCAD/FreeCAD/pull/7167)


</div>



## Gestionnaire des extensions 



## Atelier Arch 

-   Plusieurs problèmes liés au mode d\'édition ont été corrigés et les menus contextuels de la [vue en arborescence](Tree_view.md) pour les objets Arch ont été améliorés. Les objets qui peuvent être édités ont maintenant une option **Editer** dans ce menu. L\'option **Définir les couleurs** a été supprimée pour les objets sans face ou qui ne peuvent avoir qu\'une seule face. [Pull request #8122](https://github.com/FreeCAD/FreeCAD/pull/8122)



### Autres améliorations de Arch 

-   Les objets [Profilé](Arch_Profile/fr.md) permettent désormais de modifier le type du Profilé après la création. [Pull request #7217](https://github.com/FreeCAD/FreeCAD/pull/7217)



## Atelier Draft 

-   Le manque de précision de [Draft Aimantation Le plus proche](Draft_Snap_Near/fr.md) lors de l\'aimantation à des courbes a été corrigé. De plus, [Draft Aimantation Perpendiculaire](Draft_Snap_Perpendicular/fr.md) peut maintenant aussi s\'accrocher à des faces et trouver des points multiples. Pour s\'accrocher à un sommet (par exemple un [Draft Point](Draft_Point/fr.md)) [Draft Aimantation Terminaison](Draft_Snap_Endpoint/fr.md) doit maintenant être utilisé au lieu de [Draft Aimantation Le plus proche](Draft_Snap_Near/fr.md). [Pull request #7132](https://github.com/FreeCAD/FreeCAD/pull/7132)
-   Pour faciliter le travail avec des [calques](Draft_Layer/fr.md), leur comportement de glisser-déposer a été modifié. Si vous déposez un objet d\'un [Std Groupe](Std_Group/fr.md), ou un objet de type groupe tel qu\'un [Arch Partie de bâtiment](Arch_BuildingPart/fr.md), sur un calque, il n\'est plus retiré du groupe, et vice versa. Cela fonctionne sans maintenir la touche **Ctrl** enfoncée. [Pull request #7462](https://github.com/FreeCAD/FreeCAD/pull/7462)
-   La commande [Draft Réseau de points](Draft_PointArray/fr.md) prend désormais en charge davantage de types d\'objets Points. Tout objet ayant une forme et des sommets, ainsi qu\'un [maillage](Mesh_Workbench/fr.md) et un [nuage de points](Points_Workbench/fr.md) peuvent être utilisés. [Pull request #7597](https://github.com/FreeCAD/FreeCAD/pull/7597)
-   Les menus contextuels de la [vue en arborescence](Tree_view/fr.md) pour les objets Draft ont été améliorés. Les objets qui peuvent être édités avec la commande [Draft Editer](Draft_Edit/fr.md) ou qui ont une solution d\'édition dédiée, ont maintenant une option **Editer** dans ce menu. L\'option **Définir les couleurs** a été supprimée pour les objets sans face ou qui ne peuvent avoir qu\'une seule face. [Pull request #7970](https://github.com/FreeCAD/FreeCAD/pull/7970)
-   Les propriétés des objets d\'annotation Draft ont été unifiées. Les objets [Draft Texte](Draft_Text/fr.md), [Draft Dimension](Draft_Dimension/fr.md) et [Draft Etiquette](Draft_Label/fr.md) ont maintenant tous un nom de police, une taille de police et une couleur de texte. Les options de mode d\'affichage ont également été harmonisées et sont désormais les suivantes : Screen et World. [Issue #7861](https://github.com/FreeCAD/FreeCAD/issues/7861) et [Pull request #8081](https://github.com/FreeCAD/FreeCAD/pull/8081)



### Autres améliorations de Draft 

-   Plusieurs problèmes liés à [Draft Réseau selon une courbe](Draft_PathArray.md) ont été corrigés. [Pull request #7506](https://github.com/FreeCAD/FreeCAD/pull/7506) et [Pull request #7662](https://github.com/FreeCAD/FreeCAD/pull/7662)
-   La commande [Draft Edition](Draft_Edit/fr.md) a reçu plusieurs améliorations. Pour les [Polylignes](Draft_Wire/fr.md), les [B-splines](Draft_BSpline/fr.md) et les [Courbes de Bézier](Draft_BezCurve/fr.md), une option Fermer/Ouvrir a été ajoutée au menu contextuel des bords. Pour les B-splines et les courbes de Bézier, une option Inverser a également été ajoutée au même menu. Les panneaux de tâches ont été améliorés. [Pull request #7527](https://github.com/FreeCAD/FreeCAD/pull/7527) et [Pull request #7541](https://github.com/FreeCAD/FreeCAD/pull/7541)
-   La barre d\'outils [Draft Aimantation](Draft_Snap/fr.md) a été transformée en une barre d\'outils standard. Les raccourcis clavier peuvent maintenant être assignés aux aimantations. Mais leur utilisation au cours d\'une commande ne fonctionne que si aucune des boîtes de saisie du panneau des tâches n\'a le focus, car elles \"captent\" les raccourcis dits en commande. [Pull request #7656](https://github.com/FreeCAD/FreeCAD/pull/7656)
-   Dans le panneau des tâches de la commande [Draft Définir le style](Draft_SetStyle/fr.md), le bouton \"Textes/dimensions\" a été remplacé par le bouton \"Annotations\". En appuyant sur ce bouton, toutes les annotations seront traitées, y compris [Draft Etiquette](Draft_Label/fr.md). Plusieurs problèmes mineurs supplémentaires ont également été corrigés. [Pull request #8190](https://github.com/FreeCAD/FreeCAD/pull/8190), [Pull request #8195](https://github.com/FreeCAD/FreeCAD/pull/8195) and [Pull request #8196](https://github.com/FreeCAD/FreeCAD/pull/8196)



## Atelier FEM 

   
  <img alt="" src=images/FEM_Elmer-Multithread_relnotes_1.0.png  style="width:384px;">   Résultat de simulation où 8 régions maillées sont visibles (une pour chaque cœur de CPU utilisé). Il est maintenant possible d\'exécuter le solveur [Elmer](FEM_SolverElmer/fr.md) en utilisant plusieurs cœurs de CPU. Pour plus d\'informations sur les avertissements, voir [ce post du forum](https://forum.freecadweb.org/viewtopic.php?p=610617#p610617) [Pull request #7159](https://github.com/FreeCAD/FreeCAD/pull/7159)
   



### Autres améliorations de FEM 

-   Il existe maintenant une <img alt="" src=images/FEM_ConstraintInitialPressure.svg  style="width:24px;"> [contrainte de pression initiale](FEM_ConstraintInitialPressure/fr.md) pour définir la pression interne initiale des fluides. [Pull request #7364](https://github.com/FreeCAD/FreeCAD/pull/7364)
-   La <img alt="" src=images/FEM_ConstraintBodyHeatSource.svg  style="width:24px;"> [contrainte source thermique](FEM_ConstraintBodyHeatSource/fr.md) a maintenant un panneau de tâches et il est possible de définir la chaleur pour plusieurs corps ou d\'utiliser plusieurs contraintes pour différents corps dans une analyse. [Pull request #7367](https://github.com/FreeCAD/FreeCAD/pull/7367)
-   Il est maintenant possible d\'ouvrir (et ainsi de visualiser) des fichiers \*.pvtu (données de grille non structurées VTK partitionnées). Un fichier \*.pvtu est également le résultat d\'une simulation par [Elmer](FEM_SolverElmer/fr.md), lorsque plus d\'un coeur de CPU a été utilisé. [Pull request #7159](https://github.com/FreeCAD/FreeCAD/pull/7159)
-   Le rapport de déformation critique a été ajouté au pipeline de résultats de VTK. Il donne une indication de la rupture ductile pour les matériaux avec un objet \"MaterialMechanicalNonlinear\" (Matériau mécanique non linéaire). [Pull request #7467](https://github.com/FreeCAD/FreeCAD/pull/7467)
-   <img alt="" src=images/FEM_FemMesh2Mesh.svg  style="width:24px;"> [Maillage FEM à maillage](FEM_FemMesh2Mesh/fr.md) permet de définir l\'échelle du maillage déformé en utilisant Python. [Fil du forum](https://forum.freecadweb.org/viewtopic.php?f=18&t=71936) et [Pull request #7715](https://github.com/FreeCAD/FreeCAD/pull/7715)



## Exportation

## Mesh



### Autres améliorations de Mesh 

-   Permet d\'ajouter des transparences à un maillage. [Fil de discussion du forum](https://forum.freecadweb.org/viewtopic.php?f=22&t=72531) et [Commit f88305e](https://github.com/FreeCAD/FreeCAD/commit/f88305e).



## Atelier OpenSCAD 



## Atelier Part 



### Autres améliorations de Part 



## Atelier PartDesign 

   
  <img alt="" src=images/PD_Counterdrill_relnotes_1.0.png  style="width:384px;">Un trou de contre-perçage.   La boîte de dialogue de [Perçage](PartDesign_Hole/fr.md) prend en charge le type de tête de vis *Contre-perçage*. [Pull request #7562](https://github.com/FreeCAD/FreeCAD/pull/7562)
                                                                                                                                  
   



### Autres améliorations de PartDesign 

-   Dans la boîte de dialogue de [Perçage](PartDesign_Hole/fr.md), les types de têtes de vis obsolètes (vis à tête métrique, vis à tête cylindrique, etc.) ont été supprimés. Ils étaient abandonnés depuis FreeCAD 0.19. Les perçages utilisant ces types sont transformés en fraisages/alésages personnalisés avec le diamètre et la profondeur utilisés par les types. [Pull request #7654](https://github.com/FreeCAD/FreeCAD/pull/7654)
-   La commande [Valider l\'esquisse](Sketcher_ValidateSketch/fr.md) a été ajoutée à la barre d\'outils des aides. [Pull request #7700](https://github.com/FreeCAD/FreeCAD/pull/7700)
-   Les commandes inutilisables [Quitter l\'esquisse](Sketcher_LeaveSketch/fr.md) et [Vue de l\'esquisse](Sketcher_ViewSketch/fr.md) ont été supprimées du menu. Les commandes [Modifier l\'esquisse](Sketcher_EditSketch/fr.md), [Fusionner les esquisses](Sketcher_MergeSketches/fr.md) et [Esquisse miroir](Sketcher_MirrorSketch/fr.md) ont été ajoutées au menu. [Pull request #7700](https://github.com/FreeCAD/FreeCAD/pull/7700)
-   Le [profil d\'engrenage à développante](PartDesign_InvoluteGear/fr.md) a de nouvelles propriétés permettant de modifier la longueur des dents. Cela permet maintenant d\'ajuster certains types de contacts et d\'utiliser le profil pour créer également des [involute splines (en)](https://en.wikipedia.org/wiki/Spline_(mechanical)) (arbre avec canelure?). [Pull request #8184](https://github.com/FreeCAD/FreeCAD/pull/8184)



## Atelier Path 

-   Intégration de Camotics. Si Camotics (version 1.2.2 ou ultérieure) est installé, une nouvelle icône sera ajoutée à la barre d\'outils Path. Sélectionnez une Path Tâche et appuyez sur le bouton pour ouvrir la boîte de dialogue Camotics. Faites ensuite glisser le curseur pour générer un solide simulé en tout point du travail. Vous pouvez également lancer l\'application Camotics complète pour exécuter la simulation animée. Cela entraîne un post-traitement silencieux de la tâche et la création d\'un fichier de projet camotics. [Pull request #6637](https://github.com/FreeCAD/FreeCAD/pull/6637)

-   Des chaînes de substitution supplémentaires pour le nommage automatique des sorties. Si la sortie est divisée en plusieurs fichiers, les noms de fichiers peuvent automatiquement substituer le label du contrôleur d\'outil, WCS, ou le label de l\'opération. Ceci s\'ajoute aux autres chaînes de substitution existantes comme la date, le nom du travail, etc.

-   Implémentation de l\'option de brise-copeaux (Chipbreaking) pour les cycles de perçage de type débourrage. Le brise-copeaux émet un cycle G73 qui amène la commande à effectuer un très petit mouvement de rétraction pour casser le copeau sans rétracter complètement la mèche du trou. G73 est supporté nativement par LinuxCNC. D\'autres postprocesseurs devront interpréter le G73 et émettre les codes de contrôle appropriés ou décomposer la rétraction en mouvements G1/G0. Le support des postprocesseurs pour la décomposition G73 a été ajouté aux postprocesseurs \"refactorisés\". [Pull request #7469](https://github.com/FreeCAD/FreeCAD/pull/7469).



## Module Plot 



## Atelier Sketcher 

   
  <img alt="" src=images/Constrain_B-spline_knots_relnotes_1.0.gif  style="width:384px;">Déplacement des nœuds d\'une B-spline.Cliquez sur l\'image pour voir l\'animation.   Les nœuds des B-splines peuvent maintenant être déplacés et contraints comme tout autre point de l\'esquisse. [Pull request #7484](https://github.com/FreeCAD/FreeCAD/pull/7484)
                                                                                                                                                                                                                          
   

   
  <img alt="" src=images/sketcher-move-piece_relnotes_1.0.gif  style="width:384px;">Déplacement d\'une B-spline.Cliquez sur l\'image si l\'animation ne démarre pas.   Le déplacement d\'une B-spline ne déplace plus que la partie entre les nœuds. [Pull request #7110](https://github.com/FreeCAD/FreeCAD/pull/7110)
                                                                                                                                                                                                              
   

   
  <img alt="" src=images/Sketcher_BackEdit_relnotes_1.0.gif  style="width:384px;">Cliquez sur l\'image pour voir l\'animation.   Possibilité d\'éditer de manière transparente les esquisses depuis l\'avant ou l\'arrière. Lorsque vous travaillez depuis l\'arrière, les sommets (et toutes les géométries et contraintes) sont également sélectionnables et la vue en coupe est automatiquement basculée. [Pull request #7417](https://github.com/FreeCAD/FreeCAD/pull/7417)
                                                                                                                                                        
   

   
  <img alt="" src=images/Sketcher_Element_Widget_relnotes_1.0.gif  style="width:384px;">Cliquez sur l\'image pour voir l\'animation.   Le widget Eléments a été retravaillé pour simplifier l\'interface utilisateur et permettre une sélection plus simple des différentes parties de chaque géométrie : arête, point de départ, point d\'arrivée et point central. [Pull request #7567](https://github.com/FreeCAD/FreeCAD/pull/7567)
                                                                                                                                                                    
   

   
  <img alt="" src=images/Sketcher_Join_Curves_relnotes_1.0.gif  style="width:384px;">Cliquez sur l\'image pour voir l\'animation.   L\'outil [Joindre des courbes](Sketcher_JoinCurves/fr.md) a été ajouté. Il permet de combiner plusieurs courbes en une seule B-spline. [Pull request #6507](https://github.com/FreeCAD/FreeCAD/pull/6507)
                                                                                                                                                              
   



### Autres améliorations de Sketcher 

-   Le bouton de la barre d\'outils pour [Contrainte de réfraction (loi de Snell)](Sketcher_ConstrainSnellsLaw/fr.md) a été supprimé. [Commit ef62fc3](https://github.com/FreeCAD/FreeCAD/commit/ef62fc3)
-   Les [Contraintes dimensionnelles](Sketcher_Workbench/fr#Contraintes_dimensionnelles.md) et les boîtes de sélection numérique prennent en charge maintenant les mêmes fonctions mathématiques que les [expressions](Expressions/fr.md) (évaluées sur place). [Pull Request #7124](https://github.com/FreeCAD/FreeCAD/pull/7124)
-   Les boutons de la barre d\'outils pour [Sélection contraintes redondantes](Sketcher_SelectRedundantConstraints/fr.md) et [Sélection des contraintes conflictuelles](Sketcher_SelectConflictingConstraints/fr.md) ont été supprimés. [Pull request #7568](https://github.com/FreeCAD/FreeCAD/pull/7568)
-   Le bouton de la barre d\'outils pour [Arrêt de l\'opération](Sketcher_StopOperation/fr.md) a été supprimé. [Pull request #7569](https://github.com/FreeCAD/FreeCAD/pull/7569)
-   La section \"Modifier les contrôles\" de la boîte de dialogue de Sketcher a été rendue optionnelle. [Pull request #7572](https://github.com/FreeCAD/FreeCAD/pull/7572)
-   Le bouton [Sélecteur des degrés de liberté non contraints](Sketcher_SelectElementsWithDoFs/fr.md) de la barre d\'outils a été supprimé. [Pull request #7603](https://github.com/FreeCAD/FreeCAD/pull/7603)
-   La barre d\'outils de Sketcher a été divisée en deux : \"Sketcher-edit-mode\" et \"Sketcher\" (c\'est-à-dire \"pas en mode édition\"). Les barres d\'outils de Sketcher qui ne sont destinées qu\'au mode d\'édition sont masquées en mode de non-édition, et celles qui ne sont destinées qu\'au mode de non-édition sont masquées en mode d\'édition. La barre d\'outils Structure est également masquée dans Sketcher. [Pull request #7655](https://github.com/FreeCAD/FreeCAD/pull/7655)
-   [Contrainte de coïncidence](Sketcher_ConstrainCoincident/fr.md) peut désormais agir comme une contrainte concentrique lors de la sélection de 2 ou plusieurs cercles, arcs, ellipses ou arcs d\'ellipses. [Pull request #7703](https://github.com/FreeCAD/FreeCAD/pull/7703)
-   [Copie carbone](Sketcher_CarbonCopy/fr.md) utilise désormais, si possible, les noms des contraintes dans les expressions qu\'il crée au lieu d\'une référence basée sur un index, ce qui le rend plus fiable. [Pull request #7688](https://github.com/FreeCAD/FreeCAD/pull/7688)



## Atelier Spreadsheet 



### Autres améliorations de Spreadsheet 



## Atelier TechDraw 

   
  <img alt="" src=images/TechDraw_SurfaceFinishExample_relnotes_1.0.png  style="width:250px;">   L\'outil [Symbole d\'état de surface](TechDraw_SurfaceFinishSymbol/fr.md) a été ajouté pour permettre la création de symboles de finition de surface décrivant la rugosité, la disposition et l\'ondulation, mais aussi le type de traitement de surface. Il prend en charge les styles ISO et ASME. Comme le montre l\'image, l\'outil existant [Ligne de référence](TechDraw_LeaderLine/fr.md) peut être utilisé pour référencer correctement les symboles orientés vers les bords d\'un objet. [Pull request #7227](https://github.com/FreeCAD/FreeCAD/pull/7227)
  <img alt="" src=images/TechDraw_ComplexSection_relnotes_1.0.png  style="width:250px;">               L\'outil [Vue en coupe complexe](TechDraw_ComplexSection/fr.md) a été ajouté. [Pull request #7658](https://github.com/FreeCAD/FreeCAD/pull/7658)
                                                                                                                      
   



### Autres améliorations de TechDraw 

-   Les modes de navigation ont été mis à jour pour correspondre à ceux utilisés dans la vue 3D. [Pull request #7081](https://github.com/FreeCAD/FreeCAD/pull/7081) et [Pull request #7107](https://github.com/FreeCAD/FreeCAD/pull/7107)
-   Les hachures des bitmaps ont été corrigées. [Issue #6582](https://github.com/FreeCAD/FreeCAD/issues/6582) et [Pull request #7121](https://github.com/FreeCAD/FreeCAD/pull/7121)
-   La prise en charge des espaces ajustables pour les lignes d\'extension des [cotes](TechDraw_Preferences/fr#Dimensions.md) a été ajoutée. [Pull request #7133](https://github.com/FreeCAD/FreeCAD/pull/7133)
-   Le multithreading a été introduit pour la suppression des lignes cachées et la recherche des faces. [Pull request #7377](https://github.com/FreeCAD/FreeCAD/pull/7377)
-   L\'algorithme de détection des faces a été amélioré. [Pull request #7448](https://github.com/FreeCAD/FreeCAD/pull/7448)
-   L\'outil [Tout imprimer](TechDraw_PrintAll/fr.md) a été ajouté. [Pull request #7460](https://github.com/FreeCAD/FreeCAD/pull/7460)
-   [Quatre outils](TechDraw_Workbench/fr#Empilement.md) permettant de contrôler l\'ordre d\'empilement des vues ont été ajoutés. [Issue #6012](https://github.com/FreeCAD/FreeCAD/issues/6012) et [Pull request #7460](https://github.com/FreeCAD/FreeCAD/pull/7460)
-   La [vue active](TechDraw_ActiveView/fr.md) crée maintenant une capture d\'écran au lieu d\'une image SVG. [Pull request #7471](https://github.com/FreeCAD/FreeCAD/pull/7471)
-   Tous les modèles d\'écriture latine ont été convertis en \"plain svg\". [Pull request #7472](https://github.com/FreeCAD/FreeCAD/pull/7472)
-   Un aperçu a été ajouté au panneau des tâches de l\'outil [Vue en coupe](TechDraw_SectionView/fr.md). [Pull request #7658](https://github.com/FreeCAD/FreeCAD/pull/7658)
-   Suppression des fonctions obsolètes : DrawViewPart::replaceCenterLine, DrawViewPart::replaceCosmeticEdge, DrawViewPart::replaceCosmeticVertex et DrawViewPart::replaceGeomFormat.

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

Les systèmes d\'exploitation pris en charge sont :

-   Windows 7, 8, 10 et 11
-   Linux Ubuntu Focal Fossa (20.04) et plus récent
-   MacOS : 10.12 Sierra ou plus récent



## Limitations connues 



### Windows 32 bits 

Depuis FreeCAD 0.19, nous ne supportons plus officiellement Windows 32 bits. FreeCAD pourrait fonctionner sur ces systèmes, mais aucun support n\'est donné.



### Bureau distant sous Windows 

Selon les capacités graphiques OpenGL d\'un ordinateur, il se peut que l\'on rencontre un plantage lors de l\'exécution de FreeCAD via le bureau à distance. Pour résoudre ce problème, mettez à jour votre pilote OpenGL. Si cela ne vous aide pas :

-   Téléchargez [cette bibliothèque OpenGL](https://downloads.fdossena.com/geth.php?r=mesa64-latest) pour Windows 64 bits et extrayez-la.
-   Renommez le fichier DLL en *opengl32sw.dll* et copiez-le dans le sous-dossier *bin* du dossier d\'installation de FreeCAD (écrasez la DLL existante).



### MacOS : l\'atelier Start affiche une page blanche 

Si l\'[atelier Start](Start_Workbench/fr.md) n\'affiche qu\'une page blanche, vous devez activer l\'option **Utiliser le logiciel OpenGL** dans le menu **Edition → Préférences → Affichage**.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 1.0/fr
