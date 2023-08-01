# Release notes 0.21/fr
**FreeCAD 0.21 est en cours de développement, il n'y a pas encore de date de sortie prévue.**


{{Message|
Des fonctionnalités sont-elles manquantes ? Mentionnez-les dans les [https://forum.freecadweb.org/viewtopic.php?f&#61;10&t&#61;69438 Notes de publication pour v0.21] du fil du forum.

Voir [Contribuer à FreeCAD](Help_FreeCAD/fr.md) pour savoir comment contribuer à FreeCAD.
}}


{{Message|Toutes les images de cette page doivent utiliser le suffixe **_relnotes_0.21**}}




**FreeCAD 0.21** a été publié le **JJ MM 2023**, téléchargez la depuis la page [Téléchargement](Download/fr.md). Cette page liste toutes les nouvelles fonctionnalités et les changements.

Les notes de versions plus anciennes de FreeCAD sont disponibles dans la [liste des notes de versions](Feature_list/fr#Notes_de_versions.md).

L\'endroit pour une image accrocheuse sélectionnée par les administrateurs sur le [forum des modèles des utilisateurs](https://forum.freecadweb.org/viewforum.php?f=24).



## Général



## Interface utilisateur 

   
  ![](images/Navi_Cube_relnotes_0.21.png )   Le [Cube de navigation](Navigation_Cube/fr.md) a été mis à jour. Le cube n\'est plus affiché en perspective si la [vue 3D](3D_view/fr.md) est en mode orthographique. Les faces des coins ont été rendues hexagonales et plus grandes afin qu\'elles soient plus faciles à cliquer. Des bordures ont été ajoutées autour des boutons. La sélection et la taille des polices par défaut ont été améliorées. Le menu Mini-cube comprend maintenant une case à cocher pour activer la mobilité du cube. Plusieurs nouveaux paramètres ont été ajoutés, voir la page [Cube de navigation](Navigation_Cube/fr.md) pour plus d\'informations.Les pages suivantes ont été ajoutées : [Pull request #7876](https://github.com/FreeCAD/FreeCAD/pull/7876), [Pull request #8266](https://github.com/FreeCAD/FreeCAD/pull/8266), [Pull request #8646](https://github.com/FreeCAD/FreeCAD/pull/8646) et [Pull request #9356](https://github.com/FreeCAD/FreeCAD/pull/9356).
   

+++
| <img alt="" src=images/Part_SectionCut_example_relnotes_0.21.gif  style="width:384px;">Coupe persistante d\'objets se croisant.Cliquez sur l\'image pour voir l\'animation. | L\'outil [Coupe persistante](Part_SectionCut/fr.md) permet maintenant de couper des objets qui s\'entrecroisent. Ceci est utile pour les assemblages où les intersections d\'objets s\'intersectant ne peuvent parfois pas être évitées en raison de problèmes numériques. |
|                                                                                                                                                                                                                         | [Pull request #8252](https://github.com/FreeCAD/FreeCAD/pull/8252).                                                                                                                                                                                                                |
+++

   
  <img alt="" src=images/Measurement-Part_relnotes_0.21.png  style="width:384px;">   Le style d\'affichage des résultats de [mesure](Part_Workbench/fr#Mesure.md) créés à l\'aide de l\'[atelier Part](Part_Workbench/fr.md) ou de l\'[atelier PartDesign](PartDesign_Workbench/fr.md) peut désormais être modifié dans les [Préférences](PartDesign_Preferences/fr#Mesure.md). [Pull request #7148](https://github.com/FreeCAD/FreeCAD/pull/7148)
   

   
  <img alt="" src=images/WbSelector_relnotes_0.21.png  style="width:384px;">   Le sélecteur d\'ateliers peut maintenant être placé de manière optionnelle dans la barre de menu au lieu de la zone de la barre d\'outils. [Pull request #7679](https://github.com/FreeCAD/FreeCAD/pull/7679)
   



### Autres améliorations de l\'interface utilisateur 

-   Les boutons pour <img alt="" src=images/Std_Print.svg  style="width:24px;"> [Imprimer](Std_Print/fr.md) et <img alt="" src=images/Std_UserEditModeDefault.svg  style="width:24px;"> [Mode d\'édition](Std_UserEditMode/fr.md) ont été supprimées de la barre d\'outils Fichier. Ils peuvent être réajoutés en [personnalisant](Std_DlgCustomize/fr.md) votre barre d\'outils. [Pull request #7570](https://github.com/FreeCAD/FreeCAD/pull/7570) et [commit ea9a04e](https://github.com/FreeCAD/FreeCAD/commit/ea9a04e)
-   La barre d\'outils Fichier a été divisée. Les boutons pour <img alt="" src=images/Std_Undo.svg  style="width:24px;"> [Annuler](Std_Undo/fr.md), <img alt="" src=images/Std_Redo.svg  style="width:24px;"> [Rétablir](Std_Redo/fr.md) et <img alt="" src=images/Std_Refresh.svg  style="width:24px;"> [Rafraîchir](Std_Refresh/fr.md) ont été déplacés vers la nouvelle barre d\'outils Edition. Les boutons pour <img alt="" src=images/Std_Cut.svg  style="width:24px;"> [Couper](Std_Cut/fr.md), <img alt="" src=images/Std_Copy.svg  style="width:24px;"> [Copier](Std_Copy/fr.md) et <img alt="" src=images/Std_Paste.svg  style="width:24px;"> [Coller](Std_Paste/fr.md) ont été déplacés vers la nouvelle barre d\'outils Presse-papiers. Le bouton pour <img alt="" src=images/Std_WhatsThis.svg  style="width:24px;">[Qu\'est-ce que c\'est ?](Std_WhatsThis/fr.md) a été déplacé vers la nouvelle barre d\'outils Aide. [Pull request #7620](https://github.com/FreeCAD/FreeCAD/pull/7620)
-   Les commandes [Stocker la vue de travail](Std_StoreWorkingView/fr.md) et [Rappel de la vue de travail](Std_RecallWorkingView/fr.md) temporaire ont été ajoutées. [Pull request #7525](https://github.com/FreeCAD/FreeCAD/pull/7525)
-   Les changements de valeur avec la molette de la souris dans les \"champs de saisie\" (un type de widget utilisé pour entrer des valeurs dans les panneaux de tâches, par exemple par [Draft Ligne](Draft_Line/fr.md)) sont désactivés si le widget n\'a pas le focus et que [ComboBoxWheelEventFilter](Fine-tuning/fr#En_rapport_avec_la_souris.md) est activé. Cela permet d\'éviter les changements de valeur non désirés lors du défilement, comme c\'était déjà le cas pour les spin box et les combo box. [Pull request #7561](https://github.com/FreeCAD/FreeCAD/pull/7561)
-   Il est désormais possible de définir une transparence par défaut pour les nouveaux objets de [Part](Part_Module/fr.md) ou [PartDesign](PartDesign_Workbench/fr.md) dans les [Préférences](PartDesign_Preferences/fr.md). [Pull request #7103](https://github.com/FreeCAD/FreeCAD/pull/7103)
-   Il y a le nouveau style d\'orbite **Vue en rotation**. Il peut être activé dans les [Réglages des préférences](Preferences_Editor/fr#Navigation.md) ou en appuyant sur le bouton **[<img src=images/NavigationCAD_dark.svg style="width:16px">** dans la [Barre d\'état](Status_bar/fr.md) puis en utilisant le menu **Réglages → Style d'orbite**). [Pull Request #8048](https://github.com/FreeCAD/FreeCAD/pull/8048)
-   Le panneau de tâches [Std Apparence](Std_SetAppearance/fr.md) possède désormais également un bouton permettant de définir la propriété Couleur du point. [Pull request #7708](https://github.com/FreeCAD/FreeCAD/pull/7708)
-   Un bouton a été ajouté pour changer les couleurs du gradient d\'arrière-plan de la [vue 3D](3D_view/fr.md) dans l\'[éditeur de préférences](Preferences_Editor/fr#Couleurs.md). [Pull request #7155](https://github.com/FreeCAD/FreeCAD/pull/7155)
-   Tous les paramètres de transparence utilisent désormais le pas uniforme de 5 % du bouton rotatif : un clic sur le bouton dans une boîte de dialogue ou dans l\'éditeur de propriétés modifie la transparence de 5 %. Maintenez le bouton enfoncé pour modifier plusieurs pas de 5 % à la fois. [Pull request #7723](https://github.com/FreeCAD/FreeCAD/pull/7723)
-   La fenêtre de sortie a été renommée en Vue rapport pour l\'uniformité avec l\'interface utilisateur. [Pull Request #7739](https://github.com/FreeCAD/FreeCAD/pull/7739)
-   L\'atelier Image a été supprimé. Pour insérer un plan d\'image, la commande [Std Importer](Std_Import/fr.md) peut désormais être utilisée. Double-cliquez sur un plan d\'image pour modifier son orientation et son échelle. La nouvelle commande [Std Charger une image](Std_ViewLoadImage/fr.md) remplace la commande Ouvrir Image. [Pull Request #8955](https://github.com/FreeCAD/FreeCAD/pull/8955)
-   L\'atelier Raytracing, obsolète, a été supprimé. L\'[atelier Render](https://github.com/FreeCAD/FreeCAD-render) externe doit être utilisé à la place. [Pull Request #9420](https://github.com/FreeCAD/FreeCAD/pull/9420)



## Noyau et API 



### Noyau

-   La fonction **cbrt(x)** pour les racines cubiques a été ajoutée pour être utilisée dans les [expressions](Expressions/fr#Fonctions_exponentielles_et_logarithmiques.md). [Pull request #8629](https://github.com/FreeCAD/FreeCAD/pull/8629)
-   De nombreuses nouvelles [propriétés](Property/fr#Tous_les_types_de_propriétés.md) sont disponibles pour les scripts. [Pull request #6717](https://github.com/FreeCAD/FreeCAD/pull/6717)
-   Ajout des fonctions de création d\'objets {{Incode|vector}}, {{Incode|matrix}}, {{Incode|rotation}}, {{Incode|placement}} ainsi que des fonctions matricielles {{Incode|mrotate}}, {{Incode|mrotatex}}, {{Incode|mrotatey}}, {{Incode|mrotatez}}, {{Incode|mtranslate}} pour une utilisation dans les [Expressions](Expressions/fr.md). [Pull request #8603](https://github.com/FreeCAD/FreeCAD/pull/8603)

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

-   Plusieurs catégories de [Arch Profilé](Arch_Profile/fr.md) ont été ajoutées : IS RHS, IS SHS, IS Angle et IS Tee. [Pull request #7181](https://github.com/FreeCAD/FreeCAD/pull/7181) et [Pull request #7217](https://github.com/FreeCAD/FreeCAD/pull/7217)
-   Les objets [Arch Profilé](Arch_Profile/fr.md) supportent désormais la modification du type de profil après la création. [Pull request #7217](https://github.com/FreeCAD/FreeCAD/pull/7217)
-   Plusieurs problèmes liés au mode d\'édition ont été corrigés et les menus contextuels de la [vue en arborescence](Tree_view.md) pour les objets Arch ont été améliorés. Les objets qui peuvent être édités ont maintenant une option **Éditer** dans ce menu. L\'option **Définir les couleurs** a été supprimée pour les objets sans face ou qui ne peuvent avoir qu\'une seule face. [Pull request #8122](https://github.com/FreeCAD/FreeCAD/pull/8122)
-   Les objets [Arch Plan de coupe](Arch_SectionPlane/fr.md) gèrent maintenant les objets non solides de la même manière que les objets solides. [Pull request #8688](https://github.com/FreeCAD/FreeCAD/pull/8688)



### Autres améliorations de Arch 

-   L\'outil **Inverser la position de la charnière** a été amélioré. Pour toutes les polylignes rectangulaires, l\'arête opposée est maintenant correctement détectée. [Pull request #8199](https://github.com/FreeCAD/FreeCAD/pull/8199)
-   Le terrain d\'un [Arch Site](Arch_Site/fr.md) peut désormais être un solide. [Pull request #8409](https://github.com/FreeCAD/FreeCAD/pull/8409)
-   Un [Arch Site](Arch_Site/fr.md) n\'affiche plus une représentation fantôme des objets de son groupe. [Pull request #8409](https://github.com/FreeCAD/FreeCAD/pull/8409)



## Atelier Draft 

-   Le manque de précision de [Draft Aimantation Le plus proche](Draft_Snap_Near/fr.md) lors de l\'aimantation à des courbes a été corrigé. De plus, [Draft Aimantation Perpendiculaire](Draft_Snap_Perpendicular/fr.md) peut maintenant aussi s\'accrocher à des faces et trouver des points multiples. Pour s\'accrocher à un sommet (par exemple un [Draft Point](Draft_Point/fr.md)) [Draft Aimantation Terminaison](Draft_Snap_Endpoint/fr.md) doit maintenant être utilisé au lieu de [Draft Aimantation Le plus proche](Draft_Snap_Near/fr.md). [Pull request #7132](https://github.com/FreeCAD/FreeCAD/pull/7132)
-   Pour faciliter le travail avec des [calques](Draft_Layer/fr.md), leur comportement de glisser-déposer a été modifié. Si vous déposez un objet d\'un [Std Groupe](Std_Group/fr.md), ou un objet de type groupe tel qu\'un [Arch Partie de bâtiment](Arch_BuildingPart/fr.md), sur un calque, il n\'est plus retiré du groupe, et vice versa. Cela fonctionne sans maintenir la touche **Ctrl** enfoncée. [Pull request #7462](https://github.com/FreeCAD/FreeCAD/pull/7462)
-   La commande [Draft Réseau de points](Draft_PointArray/fr.md) prend désormais en charge davantage de types d\'objets Points. Tout objet ayant une forme et des sommets, ainsi qu\'un [maillage](Mesh_Workbench/fr.md) et un [nuage de points](Points_Workbench/fr.md) peuvent être utilisés. [Pull request #7597](https://github.com/FreeCAD/FreeCAD/pull/7597)
-   Les menus contextuels de la [vue en arborescence](Tree_view/fr.md) pour les objets Draft ont été améliorés. Les objets qui peuvent être édités avec la commande [Draft Éditer](Draft_Edit/fr.md) ou qui ont une solution d\'édition dédiée, ont maintenant une option **Éditer** dans ce menu. L\'option **Définir les couleurs** a été supprimée pour les objets sans face ou qui ne peuvent avoir qu\'une seule face. [Pull request #7970](https://github.com/FreeCAD/FreeCAD/pull/7970)
-   Les propriétés des objets d\'annotation Draft ont été unifiées. Les objets [Draft Texte](Draft_Text/fr.md), [Draft Dimension](Draft_Dimension/fr.md) et [Draft Étiquette](Draft_Label/fr.md) ont maintenant tous un nom de police, une taille de police et une couleur de texte. Les options de mode d\'affichage ont également été harmonisées et sont désormais les suivantes : Screen et World. [Issue #7861](https://github.com/FreeCAD/FreeCAD/issues/7861) et [Pull request #8081](https://github.com/FreeCAD/FreeCAD/pull/8081)
-   Dans le panneau des tâches de la commande [Draft Définir le style](Draft_SetStyle/fr.md), le bouton **Textes/dimensions** a été remplacé par le bouton **Annotations**. En appuyant sur ce bouton, toutes les annotations seront traitées, y compris les [Draft Étiquettes](Draft_Label/fr.md). Les paramètres **Dépassement des lignes de dimension**, **Lignes d'extension** et **Dépassement des lignes d'extension** ont été ajoutés. Plusieurs problèmes mineurs ont également été corrigés. [Pull request #8190](https://github.com/FreeCAD/FreeCAD/pull/8190), [Pull request #8195](https://github.com/FreeCAD/FreeCAD/pull/8195), [Pull request #8196](https://github.com/FreeCAD/FreeCAD/pull/8196) et [Pull request #9514](https://github.com/FreeCAD/FreeCAD/pull/9514).
-   Annuler/Rétablir ne fonctionnait pas correctement pour les commandes Draft de modification sous Windows. [Pull request #8267](https://github.com/FreeCAD/FreeCAD/pull/8267)
-   La commande [Gestionnaire de calques](Draft_LayerManager/fr.md) a été migrée de l\'atelier BIM vers l\'atelier Draft. [Pull request #8795](https://github.com/FreeCAD/FreeCAD/pull/8795)



### Autres améliorations de Draft 

-   Lors de l\'alignement du plan de travail avec une face, il n\'était orienté pour correspondre aux axes globaux que si la face était un quadrilatère. [Pull request #7249](https://github.com/FreeCAD/FreeCAD/pull/7249)
-   Plusieurs problèmes liés au [Draft Réseau selon une courbe](Draft_PathArray/fr.md) ont été corrigés. [Pull request #7506](https://github.com/FreeCAD/FreeCAD/pull/7506) et [Pull request #7662](https://github.com/FreeCAD/FreeCAD/pull/7662)
-   La commande [Draft Edition](Draft_Edit/fr.md) a reçu plusieurs améliorations. Pour les [Polylignes](Draft_Wire/fr.md), les [B-splines](Draft_BSpline/fr.md) et les [Courbes de Bézier](Draft_BezCurve/fr.md), une option Fermer/Ouvrir a été ajoutée au menu contextuel des bords. Pour les B-splines et les courbes de Bézier, une option Inverser a également été ajoutée au même menu. Les panneaux de tâches ont été améliorés. [Pull request #7527](https://github.com/FreeCAD/FreeCAD/pull/7527) et [Pull request #7541](https://github.com/FreeCAD/FreeCAD/pull/7541)
-   L\'utilisation d\'Echap pour quitter une commande ne désactive plus le mode continu. [Pull request #7611](https://github.com/FreeCAD/FreeCAD/pull/7611)
-   La barre d\'outils [Draft Aimantation](Draft_Snap/fr.md) a été transformée en une barre d\'outils standard. Les raccourcis clavier peuvent maintenant être assignés aux aimantations. Mais leur utilisation au cours d\'une commande ne fonctionne que si aucune des boîtes de saisie du panneau des tâches n\'a le focus, car elles \"captent\" les raccourcis dits en commande. [Pull request #7656](https://github.com/FreeCAD/FreeCAD/pull/7656)
-   Plusieurs bogues de [Draft Éditeur de styles d\'annotations](Draft_AnnotationStyleEditor/fr.md) ont été corrigés. Les paramètres **Couleur du texte** et **Espacement du texte** ont été ajoutés. [Pull request #8207](https://github.com/FreeCAD/FreeCAD/pull/8207) et [Pull request #9702](https://github.com/FreeCAD/FreeCAD/pull/9702)
-   Les propriétés Start et End Offset ont été ajoutées aux objets [Draft Réseau selon une courbe](Draft_PathArray/fr.md). [Pull request #8295](https://github.com/FreeCAD/FreeCAD/pull/8295)
-   Une propriété Count a été ajoutée aux réseaux qui n\'en disposaient pas : les versions non liées de [Draft Réseau orthogonal](Draft_OrthoArray/fr.md), [Draft Réseau polaire](Draft_PolarArray/fr.md) et [Draft Réseau circulaire](Draft_CircularArray/fr.md). [Pull request #8433](https://github.com/FreeCAD/FreeCAD/pull/8433)
-   Le comportement actif/non actif de la [grille](Draft_Snap_Grid/fr.md) a été corrigé. [Pull request #8818](https://github.com/FreeCAD/FreeCAD/pull/8818)
-   La gestion des convertisseurs DWG a été améliorée. [Pull request #9444](https://github.com/FreeCAD/FreeCAD/pull/9444) et [Pull request #9830](https://github.com/FreeCAD/FreeCAD/pull/9830)



## Atelier FEM 

   
  <img alt="" src=images/FEM_PostFilterContours_relnotes_0.21.png  style="width:384px;">Iso-contours décrivant la composante y de l\'induction magnétiqueabsolue dans et autour d\'un fil de cuivre traversé par un courantélectrique à une fréquence de 100 kHz.Pour plus d\'informations sur ce modèle, voir la section 14 des [tutoriels d\'Elmer (en)](https://www.nic.funet.fi/index/elmer/doc/ElmerTutorials.pdf).   Il existe le nouveau modèle <img alt="" src=images/FEM_PostFilterContours.svg  style="width:24px;"> [Filtre par contours](FEM_PostFilterContours/fr.md) qui permet de dessiner des iso-lignes ou des iso-contours. Les iso-contours sont des nœuds de maillage connectés qui ont la même valeur de champ de résultat. Les lignes de champ électrique en sont un exemple typique. [Pull request #8462](https://github.com/FreeCAD/FreeCAD/pull/8462)
   

   
  <img alt="" src=images/FEM_Elmer-Multithread_relnotes_0.21.png  style="width:384px;">Résultat de la simulation (de l\'eau courante chauffée) avec 8régions de maillage visibles (une pour chaque cœur de CPU utilisé).   Il est maintenant possible d\'exécuter le solveur [Elmer](FEM_SolverElmer/fr.md) en utilisant plusieurs cœurs de CPU. Pour plus d\'informations sur les avertissements, voir [ce post du forum](https://forum.freecadweb.org/viewtopic.php?p=610617#p610617) [Pull request #7159](https://github.com/FreeCAD/FreeCAD/pull/7159)
   

   
  <img alt="" src=images/FEM_EquationMagnetodynamic2D_relnotes_0.21.png  style="width:300px;">Résultat de la simulation de la partie imaginairede la densité de courant dans un creuset chaufféélectriquement par une bobine l\'encerclant.Ce modèle est disponible dans les [FEM Exemples](FEM_Examples/fr.md).Pour plus d\'informations sur ce modèle, voir la section 16 des [tutoriels d\'Elmer](https://www.nic.funet.fi/index/elmer/doc/ElmerTutorials.pdf).   L\'<img alt="" src=images/FEM_EquationMagnetodynamic2D.svg  style="width:24px;"> [Équation magnétodynamique 2D](FEM_EquationMagnetodynamic2D/fr.md) a été ajoutée. Avec cela, il est possible de réaliser des simulations électromagnétiques en 2D. [Pull request #8355](https://github.com/FreeCAD/FreeCAD/pull/8355)
   

   
  <img alt="" src=images/FEM_EquationMagnetodynamic_relnotes_0.21.png  style="width:384px;">Résultat de la simulation de la partie imaginaire de l\'inductionmagnétique dans et autour d\'un fil de cuivre traversé par uncourant électrique à une fréquence de 100 kHz. Ce modèle est disponible dans les [FEM Exemples](FEM_Examples/fr.md). Pour plusd\'informations sur ce modèle, voir la section 14 des [tutoriels d\'Elmer](https://www.nic.funet.fi/index/elmer/doc/ElmerTutorials.pdf).   L\'<img alt="" src=images/FEM_EquationMagnetodynamic.svg  style="width:24px;"> [Équation magnétodynamique](FEM_EquationMagnetodynamic/fr.md) a été ajoutée. Avec cela, il est possible de réaliser des simulations électromagnétiques. [Pull request #8380](https://github.com/FreeCAD/FreeCAD/pull/8380)
   

   
  <img alt="" src=images/FEM_EquationDeformation_relnotes_0.21.png  style="width:384px;">Résultat de la simulation d\'un fil de fer en U qui est déforméen pressant les extrémités du U l\'une contre l\'autre.Pour plus d\'informations sur ce modèle, voir la section 8 des [tutoriels d\'Elmer](https://www.nic.funet.fi/index/elmer/doc/ElmerTutorials.pdf).   L\'<img alt="" src=images/FEM_EquationDeformation.svg  style="width:24px;"> [Équation de déformation](FEM_EquationDeformation.md) a été ajoutée. Elle permet d\'effectuer des analyses d\'élasticité non linéaire (déformation). [Pull request #8981](https://github.com/FreeCAD/FreeCAD/pull/8981)
   



### Autres améliorations de FEM 

-   Lors de l\'exécution d\'analyses à l\'aide du <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;"> [solveur CalculiX](FEM_SolverCalculixCxxtools/fr.md), un [pipeline de resultats](FEM_PostPipelineFromResult/fr.md) est désormais créé pour visualiser les résultats. [Pull request #8525](https://github.com/FreeCAD/FreeCAD/pull/8525) et [Pull request #8903](https://github.com/FreeCAD/FreeCAD/pull/8903)
-   Il est maintenant possible d\'effectuer [analyses transitoires](FEM_SolverElmer_SolverSettings/fr#Pas_de_temps_(analyses_transitoires).md) lors de l\'utilisation du <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [solveur Elmer](FEM_SolverElmer/fr.md). [Pull request #9056](https://github.com/FreeCAD/FreeCAD/pull/9056)
-   La <img alt="" src=images/FEM_ConstraintInitialPressure.svg  style="width:24px;"> [contrainte de pression initiale](FEM_ConstraintInitialPressure/fr.md) a été ajoutée pour définir la pression interne initiale des fluides. [Pull request #7364](https://github.com/FreeCAD/FreeCAD/pull/7364)
-   La <img alt="" src=images/FEM_ConstraintCurrentDensity.svg  style="width:24px;"> [contrainte de densité de courant](FEM_ConstraintCurrentDensity/fr.md) a été ajoutée pour définir les densités de courant des corps et des faces. [Pull request #8348](https://github.com/FreeCAD/FreeCAD/pull/8348)
-   La <img alt="" src=images/FEM_ConstraintMagnetization.svg  style="width:24px;"> [contrainte de magnétisation](FEM_ConstraintMagnetization.md) a été ajoutée pour définir les magnétisations des corps et des faces. [Pull request #8393](https://github.com/FreeCAD/FreeCAD/pull/8393)
-   La <img alt="" src=images/FEM_ConstraintFlowVelocity.svg  style="width:24px;"> [contrainte de vitesse d\'écoulement](FEM_ConstraintFlowVelocity/fr.md) et <img alt="" src=images/FEM_ConstraintInitialFlowVelocity.svg  style="width:24px;"> [contrainte de vitesse d\'écoulement initiale](FEM_ConstraintInitialFlowVelocity/fr.md) ont été complètement réécrites. Il est maintenant également possible de spécifier une vitesse via une formule mathématique (pour définir un profil de vitesse). [Pull request #8963](https://github.com/FreeCAD/FreeCAD/pull/8963) et [Pull request #8964](https://github.com/FreeCAD/FreeCAD/pull/8964)**Remarque :** il s\'agit d\'un changement majeur. Les analyses avec des contraintes de vitesse d\'écoulement et de vitesse d\'écoulement initiale existantes ne fonctionneront plus. Vous devez créer de nouvelles contraintes de vitesse d\'écoulement dans l\'analyse pour que les analyses existantes fonctionnent. [Pull request #8963](https://github.com/FreeCAD/FreeCAD/pull/8963) et [Pull request #8964](https://github.com/FreeCAD/FreeCAD/pull/8964)**Remarque bis :** jusqu\'à FreeCAD 0.21, les résultats du solveur d\'écoulement étaient erronés (la densité et la viscosité du fluide étaient trop élevées d\'un facteur 1000). Par conséquent, la refonte de la contrainte de vitesse garantit également que les résultats seront corrects.
-   Il est maintenant possible de définir dans la <img alt="" src=images/FEM_ConstraintDisplacement.svg  style="width:24px;"> [contrainte de déplacement](FEM_ConstraintDisplacement/fr.md) des déplacements définis par des équations (déplacement en fonction du temps du solveur utlisé).
-   La <img alt="" src=images/FEM_ConstraintBodyHeatSource.svg  style="width:24px;"> [contrainte source thermique](FEM_ConstraintBodyHeatSource/fr.md) a maintenant un panneau de tâches et il est possible de définir la chaleur pour plusieurs corps ou d\'utiliser plusieurs contraintes pour différents corps dans une analyse. [Pull request #7367](https://github.com/FreeCAD/FreeCAD/pull/7367)
-   La <img alt="" src=images/FEM_ConstraintSpring.svg  style="width:24px;"> [contrainte de ressort](FEM_ConstraintSpring/fr.md) n\'était utilisée par aucun solveur. Elle peut maintenant être utilisée par le solveur [Elmer](FEM_SolverElmer/fr.md) via les équations de [déformation](FEM_EquationDeformation/fr.md) et d\'[élasticité](FEM_EquationElasticity/fr.md). [Pull request #9005](https://github.com/FreeCAD/FreeCAD/pull/9005)
-   La fonction de découpage du maillage résultant <img alt="" src=images/FEM_PostCreateFunctionCylinder.svg  style="width:24px;"> [Filtre fonction cylindre](FEM_PostCreateFunctionCylinder/fr.md) a été ajoutée. [Pull request #8735](https://github.com/FreeCAD/FreeCAD/pull/8735)
-   La fonction de découpage du maillage résultant <img alt="" src=images/FEM_PostCreateFunctionBox.svg  style="width:24px;"> [Filtre fonction boîte](FEM_PostCreateFunctionBox/fr.md) a été ajoutée. [Pull request #8825](https://github.com/FreeCAD/FreeCAD/pull/8825)
-   Il est maintenant possible d\'ouvrir (et ainsi de visualiser) des fichiers \*.pvtu (données de grille non structurées VTK partitionnées). Un fichier \*.pvtu est également le résultat d\'une simulation par [Elmer](FEM_SolverElmer/fr.md), lorsque plus d\'un cœur de CPU est utilisé pour les calculs. [Pull request #7159](https://github.com/FreeCAD/FreeCAD/pull/7159)
-   Le rapport de déformation critique a été ajouté au pipeline de résultats de VTK. Il donne une indication de la rupture ductile pour les matériaux avec un objet \"MaterialMechanicalNonlinear\" (Matériau mécanique non linéaire). [Pull request #7467](https://github.com/FreeCAD/FreeCAD/pull/7467)
-   <img alt="" src=images/FEM_FemMesh2Mesh.svg  style="width:24px;"> [Maillage FEM à maillage](FEM_FemMesh2Mesh/fr.md) a le nouveau paramètre *scale* pour définir l\'échelle du maillage déformé en utilisant Python. [Fil du forum](https://forum.freecadweb.org/viewtopic.php?f=18&t=71936) et [Pull request #7715](https://github.com/FreeCAD/FreeCAD/pull/7715)
-   Les [préférences](FEM_Preferences/fr.md) ont une nouvelle option pour définir quel solveur doit être automatiquement ajouté lors de la création d\'une nouvelle analyse.
-   Amélioration de l\'ergonomie :
    -   Si vous vous trouvez dans l\'atelier FEM lorsque vous chargez un fichier FreeCAD contenant une analyse, l\'analyse est activée automatiquement (vous avez immédiatement accès à tous les boutons de la barre d\'outils FEM).
    -   La barre d\'outils ne contient que des boutons pour les solveurs installés sur votre système. Les solveurs non disponibles ne sont plus affichés.
-   De nouveaux fichiers d\'exemples pour les équations suivantes sont disponibles dans les [FEM Exemples](FEM_Examples/fr.md) : [déformation](FEM_EquationDeformation/fr.md), [écoulement](FEM_EquationFlow/fr.md), [flux](FEM_EquationFlux/fr.md), [chaleur](FEM_EquationHeat/fr.md), [magnétodynamique](FEM_EquationMagnetodynamic/fr.md) et [magnétodynamique 2D](FEM_EquationMagnetodynamic2D/fr.md). [#8550](https://github.com/FreeCAD/FreeCAD/pull/8550), [Pull request #8569](https://github.com/FreeCAD/FreeCAD/pull/8569), [Pull request #8579](https://github.com/FreeCAD/FreeCAD/pull/8579), [Pull request #8597](https://github.com/FreeCAD/FreeCAD/pull/8597), [Pull request #8630](https://github.com/FreeCAD/FreeCAD/pull/8630) et [#9004](https://github.com/FreeCAD/FreeCAD/pull/9004).
-   Nouvelle carte de matériau pour le dioxyde de carbone et un alliage de titane. [Pull request #8332](https://github.com/FreeCAD/FreeCAD/pull/8332) et [Pull request #8636](https://github.com/FreeCAD/FreeCAD/pull/8636)



## Exportation



## Mesh (Maillage) 



### Autres améliorations de Mesh 

-   Permet d\'ajouter des transparences à un maillage. [Fil de discussion du forum](https://forum.freecadweb.org/viewtopic.php?f=22&t=72531) et [Commit f88305e](https://github.com/FreeCAD/FreeCAD/commit/f88305e).



## Atelier OpenSCAD 



## Atelier Part 



### Autres améliorations de Part 

-   La commande [Part Points à partir de maillage](Part_PointsFromMesh/fr.md) a été étendue pour accepter n\'importe quel objet géométrique. [Pull request #8730](https://github.com/FreeCAD/FreeCAD/pull/8730)



## Atelier PartDesign 

   
  <img alt="" src=images/PD_Counterdrill_relnotes_0.21.png  style="width:384px;">Un trou de contre-perçage.   La boîte de dialogue de [Perçage](PartDesign_Hole/fr.md) prend en charge le type de tête de vis *Contre-perçage*. [Pull request #7562](https://github.com/FreeCAD/FreeCAD/pull/7562)
                                                                                                                                    
   

   
  <img alt="" src=images/PartDesign_task_dialog_relnotes_0.21.png  style="width:384px;">   L\'interface utilisateur de plusieurs boîtes de dialogue de tâches de PartDesign pour la sélection de géométries a été améliorée, ne nécessitant plus l\'utilisation de boutons séparés pour l\'ajout ou la suppression de géométries dans la sélection. [Pull request #8990](https://github.com/FreeCAD/FreeCAD/pull/8990)
                                                                                                          
   



### Autres améliorations de PartDesign 

-   Dans la boîte de dialogue de [Perçage](PartDesign_Hole/fr.md), les types de têtes de vis obsolètes (vis à tête métrique, vis à tête cylindrique, etc.) ont été supprimés. Ils étaient abandonnés depuis FreeCAD 0.19. Les perçages utilisant ces types sont transformés en fraisages/alésages personnalisés avec le diamètre et la profondeur utilisés par les types. [Pull request #7654](https://github.com/FreeCAD/FreeCAD/pull/7654)
-   Dans les boîtes de dialogue de [Lissage additif](PartDesign_AdditiveLoft/fr.md) et de [Lissage soustractif](PartDesign_SubtractiveLoft/fr.md), l\'option **Fermé**, auparavant non fonctionnelle, crée désormais un lissage fermé (comme un anneau). [Pull request #8748](https://github.com/FreeCAD/FreeCAD/pull/8748)
-   La commande [Valider l\'esquisse](Sketcher_ValidateSketch/fr.md) a été ajoutée à la barre d\'outils des aides. [Pull request #7700](https://github.com/FreeCAD/FreeCAD/pull/7700)
-   Les commandes inutilisables [Quitter l\'esquisse](Sketcher_LeaveSketch/fr.md) et [Vue de l\'esquisse](Sketcher_ViewSketch/fr.md) ont été supprimées du menu. Les commandes [Modifier l\'esquisse](Sketcher_EditSketch/fr.md), [Fusionner les esquisses](Sketcher_MergeSketches/fr.md) et [Esquisse miroir](Sketcher_MirrorSketch/fr.md) ont été ajoutées au menu. [Pull request #7700](https://github.com/FreeCAD/FreeCAD/pull/7700)
-   L\'[Engrenage à développante](PartDesign_InvoluteGear/fr.md) a de nouvelles propriétés permettant de modifier la longueur des dents. Cela permet maintenant d\'ajuster certains types de contacts et d\'utiliser le profil pour créer également des [involute splines (en)](https://en.wikipedia.org/wiki/Spline_(mechanical)) (arbre avec canelure ?). [Pull request #8184](https://github.com/FreeCAD/FreeCAD/pull/8184)
-   L\'[Engrenage à développante](PartDesign_InvoluteGear/fr.md) permet désormais de changer de profil. [Issue #5618](https://github.com/FreeCAD/FreeCAD/issues/5618) et [Pull request #8934](https://github.com/FreeCAD/FreeCAD/pull/8934)
-   Lors de la création d\'un [Clone](PartDesign_Clone/fr.md), celui-ci hérite désormais des couleurs de l\'objet cloné. [Pull request #9547](https://github.com/FreeCAD/FreeCAD/pull/9547)



## Atelier Path 

-   Intégration de Camotics. Si Camotics (version 1.2.2 ou ultérieure) est installé, une nouvelle icône sera ajoutée à la barre d\'outils Path. Sélectionnez une Path Tâche et appuyez sur le bouton pour ouvrir la boîte de dialogue Camotics. Faites ensuite glisser le curseur pour générer un solide simulé en tout point du travail. Vous pouvez également lancer l\'application Camotics complète pour exécuter la simulation animée. Cela entraîne un post-traitement silencieux de la tâche et la création d\'un fichier de projet camotics. [Pull request #6637](https://github.com/FreeCAD/FreeCAD/pull/6637)

-   Des chaînes de substitution supplémentaires pour le nommage automatique des sorties. Si la sortie est divisée en plusieurs fichiers, les noms de fichiers peuvent automatiquement substituer le label du contrôleur d\'outil, Systèmes de coordonnées de pièce (Work Coordinate Systems = WCS), ou le label de l\'opération. Ceci s\'ajoute aux autres chaînes de substitution existantes comme la date, le nom du travail, etc.

-   Implémentation de l\'option de brise-copeaux (Chipbreaking) pour les cycles de perçage de type débourrage. Le brise-copeaux émet un cycle G73 qui amène la commande à effectuer un très petit mouvement de rétraction pour casser le copeau sans rétracter complètement la mèche du trou. G73 est supporté nativement par LinuxCNC. D\'autres postprocesseurs devront interpréter le G73 et émettre les codes de contrôle appropriés ou décomposer la rétraction en mouvements G1/G0. Le support des postprocesseurs pour la décomposition G73 a été ajouté aux postprocesseurs \"refactorisés\". [Pull request #7469](https://github.com/FreeCAD/FreeCAD/pull/7469).



## Module Plot 



## Atelier Sketcher 

   
  <img alt="" src=images/Constrain_B-spline_knots_relnotes_0.21.gif  style="width:384px;">Déplacement des nœuds d\'une B-spline.Cliquez sur l\'image pour voir l\'animation.   Les nœuds des B-splines peuvent maintenant être déplacés et contraints comme tout autre point de l\'esquisse. [Pull request #7484](https://github.com/FreeCAD/FreeCAD/pull/7484)
                                                                                                                                                                                                                            
   

   
  <img alt="" src=images/sketcher-move-piece_relnotes_0.21.gif  style="width:384px;">Déplacement d\'une B-spline.Cliquez sur l\'image si l\'animation ne démarre pas.   Le déplacement d\'une B-spline ne déplace plus que la partie entre les nœuds. [Pull request #7110](https://github.com/FreeCAD/FreeCAD/pull/7110)
                                                                                                                                                                                                                
   

   
  <img alt="" src=images/Sketcher_Join_Curves_relnotes_0.21.gif  style="width:384px;">Cliquez sur l\'image pour voir l\'animation.   L\'outil [Joindre des courbes](Sketcher_JoinCurves/fr.md) a été ajouté. Il permet de combiner deux courbes en une seule B-spline. [Pull request #6507](https://github.com/FreeCAD/FreeCAD/pull/6507)
                                                                                                                                                                
   

   
  <img alt="" src=images/Sketcher_BackEdit_relnotes_0.21.gif  style="width:384px;">Cliquez sur l\'image pour voir l\'animation.   Les esquisses peuvent désormais être éditées de manière transparente à partir de l\'avant ou de l\'arrière. Lorsque vous travaillez de l\'arrière, les sommets (et toutes les géométries et contraintes) peuvent être sélectionnés de la même manière et la vue de la section est commutée automatiquement. [Pull request #7417](https://github.com/FreeCAD/FreeCAD/pull/7417)
                                                                                                                                                          
   

   
  <img alt="" src=images/Sketcher_Grid_Rework_relnotes_0.21.png  style="width:384px;">   La grille de Sketcher a été retravaillée. L\'outil [Grille](Sketcher_Grid/fr.md) a été ajouté. L\'option de mise à l\'échelle automatique de la grille a été ajoutée. [Pull request #8473](https://github.com/FreeCAD/FreeCAD/pull/8473)
                                                                                                      
   

   
  <img alt="" src=images/Sketcher_Constraint_Widget_relnotes_0.21.png  style="width:384px;">   Le widget Contrainte de Sketcher a été retravaillé pour simplifier l\'interface utilisateur. [Pull request #7566](https://github.com/FreeCAD/FreeCAD/pull/7566)
                                                                                                                  
   

   
  <img alt="" src=images/Sketcher_Element_Widget_relnotes_0.21.gif  style="width:384px;">Cliquez sur l\'image pour voir l\'animation.   Le widget Eléments a été retravaillé pour simplifier l\'interface utilisateur et permettre une sélection plus simple des différentes parties de chaque géométrie : arête, point de départ, point d\'arrivée et point central. [Pull request #7567](https://github.com/FreeCAD/FreeCAD/pull/7567)
                                                                                                                                                                      
   

   
  <img alt="" src=images/Sketcher_Grid_relnotes_0.21.gif  style="width:384px;">   Une fonction permettant de redimensionner automatiquement la grille en fonction du niveau de zoom et d\'autres améliorations ont été introduites. [Pull request #8473](https://github.com/FreeCAD/FreeCAD/pull/8473)
                                                                                        
   

   
  <img alt="" src=images/Sketcher_layers_relnotes_0.21.gif  style="width:384px;">   La fonctionnalité de base des calques visuels a été introduite. Pour l\'instant, seuls 3 calques codés en dur sont pris en charge. D\'autres améliorations sont attendues dans le futur. Ce PR supprime également le widget \"Edit controls\" du panneau des tâches car tout son contenu a été déplacé vers d\'autres endroits ou supprimé. Les options d\'ordre de rendu ont été déplacées dans la barre d\'outils d\'édition du Sketcher. [Pull request #8716](https://github.com/FreeCAD/FreeCAD/pull/8716) et [Pull request #9590](https://github.com/FreeCAD/FreeCAD/pull/9590)
                                                                                            
   

   
  <img alt="" src=images/Sketcher_Circle2CircleConstraint_relnotes_0.21.png  style="width:384px;">   La [contrainte dimensionnelle](Sketcher_ConstrainDistance/fr.md) de cercle à cercle a été introduite. [Pull request #8896](https://github.com/FreeCAD/FreeCAD/pull/8896)
                                                                                                                              
   

   
  <img alt="" src=images/Sketcher_Circle2LineConstraint_relnotes_0.21.png  style="width:384px;">   La [contrainte dimensionnelle](Sketcher_ConstrainDistance/fr.md) de cercle à ligne a été introduite. [Pull request #9044](https://github.com/FreeCAD/FreeCAD/pull/9044)
                                                                                                                          
   

   
  <img alt="" src=images/Sketcher-snap2_relnotes_0.21.gif  style="width:384px;">Cliquez sur l\'image de gauche pour voir l\'animation.   Le gestionnaire d\'aimantation, l\'aimantation à l\'angle et l\'aimantation au point milieu ont été ajoutés. [Pull request #8387](https://github.com/FreeCAD/FreeCAD/pull/8387)
                                                                                                                                                              
   

   
  <img alt="" src=images/Sketcher-concentric_relnotes_0.21.gif  style="width:384px;">   [Contrainte de coïncidence](Sketcher_ConstrainCoincident/fr.md) peut désormais agir comme une contrainte concentrique lors de la sélection de 2 ou plusieurs cercles, arcs, ellipses ou arcs d\'ellipses. [Pull request #7703](https://github.com/FreeCAD/FreeCAD/pull/7703)
                                                                                                    
   

   
  <img alt="" src=images/Sketcher-B-spline_by_knots_v2_relnotes_0.21.gif  style="width:384px;">   L\'outil [B-spline par des nœuds](Sketcher_CreateBSplineByInterpolation/fr.md) a été ajouté. [Pull request #8530](https://github.com/FreeCAD/FreeCAD/pull/8530)
                                                                                                                        
   

   
  <img alt="" src=images/Sketcher-periodic_B-spline_by_knots_v2_relnotes_0.21.gif  style="width:384px;">   L\'outil [B-spline périodique par des nœuds](Sketcher_CreatePeriodicBSplineByInterpolation/fr.md) a été ajouté. [Pull request #8530](https://github.com/FreeCAD/FreeCAD/pull/8530)
                                                                                                                                          
   



### Autres améliorations de Sketcher 

-   Le bouton de la barre d\'outils pour [Contrainte de réfraction (loi de Snell)](Sketcher_ConstrainSnellsLaw/fr.md) a été supprimé. [Commit ef62fc3](https://github.com/FreeCAD/FreeCAD/commit/ef62fc3)
-   [Diviser](Sketcher_Split/fr.md) prend maintenant en charge plus de courbes (ellipses, paraboles, hyperboles et B-splines). [Pull request #6971](https://github.com/FreeCAD/FreeCAD/pull/6971)
-   Les [Contraintes dimensionnelles](Sketcher_Workbench/fr#Contraintes_dimensionnelles.md) et les boîtes de sélection numérique prennent en charge maintenant les mêmes fonctions mathématiques que les [expressions](Expressions/fr.md) (évaluées sur place). [Pull Request #7124](https://github.com/FreeCAD/FreeCAD/pull/7124)
-   Les boutons de la barre d\'outils pour [Sélection contraintes redondantes](Sketcher_SelectRedundantConstraints/fr.md) et [Sélection des contraintes conflictuelles](Sketcher_SelectConflictingConstraints/fr.md) ont été supprimés. [Pull request #7568](https://github.com/FreeCAD/FreeCAD/pull/7568)
-   Le bouton de la barre d\'outils pour [Arrêt de l\'opération](Sketcher_StopOperation/fr.md) a été supprimé. [Pull request #7569](https://github.com/FreeCAD/FreeCAD/pull/7569)
-   Le bouton [Sélecteur des degrés de liberté non contraints](Sketcher_SelectElementsWithDoFs/fr.md) de la barre d\'outils a été supprimé. [Pull request #7603](https://github.com/FreeCAD/FreeCAD/pull/7603)
-   La barre d\'outils de Sketcher a été divisée en deux : \"Sketcher-edit-mode\" et \"Sketcher\" (c\'est-à-dire \"pas en mode édition\"). Les barres d\'outils de Sketcher qui ne sont destinées qu\'au mode d\'édition sont masquées en mode de non-édition, et celles qui ne sont destinées qu\'au mode de non-édition sont masquées en mode d\'édition. La barre d\'outils Structure est également masquée dans Sketcher. [Pull request #7655](https://github.com/FreeCAD/FreeCAD/pull/7655)
-   [Copie carbone](Sketcher_CarbonCopy/fr.md) utilise désormais, si possible, les noms des contraintes dans les expressions qu\'elle crée au lieu d\'une référence basée sur un index, ce qui la rend plus fiable. [Pull request #7688](https://github.com/FreeCAD/FreeCAD/pull/7688)
-   L\'outil Contraindre l\'alignement interne a été supprimé. Il était obsolète depuis l\'introduction de l\'outil [Basculer la géométrie interne](Sketcher_RestoreInternalAlignmentGeometry/fr.md). [Pull request #8863](https://github.com/FreeCAD/FreeCAD/pull/8863)
-   La boîte de tâches \"Message du solveur\" de Sketcher a été simplifiée. La case à cocher \"suppression automatique de la redondance\" a été déplacée dans le menu du bouton de réglage de la boîte à tâches \"Contrainte\". La case à cocher de mise à jour automatique a été déplacée dans le menu du bouton de mise à jour. [Pull request #8864](https://github.com/FreeCAD/FreeCAD/pull/8864)



## Atelier Spreadsheet 



### Autres améliorations de Spreadsheet 



## Atelier Surface 

   
  <img alt="" src=images/Surface_BlendCurve_relnotes_0.21.png  style="width:250px;">   L\'outil [Fusion de courbes](Surface_BlendCurve/fr.md) a été ajouté. [Pull request #7339](https://github.com/FreeCAD/FreeCAD/pull/7339)
                                                                                                  
   



## Atelier TechDraw 

   
  <img alt="" src=images/TechDraw_SurfaceFinishExample_relnotes_0.21.png  style="width:250px;">             L\'outil [Symbole d\'état de surface](TechDraw_SurfaceFinishSymbol/fr.md) a été ajouté pour permettre la création de symboles de finition de surface décrivant la rugosité, la disposition et l\'ondulation, mais aussi le type de traitement de surface. Il prend en charge les styles ISO et ASME. Comme le montre l\'image, l\'outil existant [Ligne de référence](TechDraw_LeaderLine/fr.md) peut être utilisé pour référencer correctement les symboles orientés vers les bords d\'un objet. [Pull request #7227](https://github.com/FreeCAD/FreeCAD/pull/7227)
  <img alt="" src=images/TechDraw_ComplexSection_relnotes_0.21.png  style="width:250px;">                         L\'outil [Vue en coupe complexe](TechDraw_ComplexSection/fr.md) a été ajouté pour permettre la création de demi-sections, de sections décalées et de sections alignées. [Pull request #7658](https://github.com/FreeCAD/FreeCAD/pull/7658)
  <img alt="" src=images/TechDraw_HoleShaftFitExample_relnotes_0.21.png  style="width:250px;">               L\'outil [Tolérance de trou/d\'arbre](TechDraw_HoleShaftFit/fr.md) a été ajouté. [Pull request #8455](https://github.com/FreeCAD/FreeCAD/pull/8455)
  <img alt="" src=images/TechDraw_AxoLengthDimensionExample_relnotes_0.21.png  style="width:250px;">   L\'outil [Cote axonométrique](TechDraw_AxoLengthDimension/fr.md) a été ajouté. [Pull request #8359](https://github.com/FreeCAD/FreeCAD/pull/8359)
                                                                                                                                  
   



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
-   Les fonctions DrawViewPart obsolètes ont été supprimées : replaceCenterLine, replaceCosmeticEdge, replaceCosmeticVertex et replaceGeomFormat.
-   Les cotes 3D peuvent désormais être créées de la même manière que les cotes 2D (à l\'exception du fait que la géométrie doit être sélectionnée dans une vue 3D). Il n\'est donc plus nécessaire de les lier manuellement à la géométrie 3D. [Pull request #8141](https://github.com/FreeCAD/FreeCAD/pull/8141)
-   L\'outil [Réparation des cotes](TechDraw_DimensionRepair/fr.md) a été ajouté. [Pull request #8141](https://github.com/FreeCAD/FreeCAD/pull/8141)
-   Une fonction pour supprimer les bords qui se chevauchent renvoyés par l\'algorithme de suppression des lignes cachées a été ajoutée plus un nouveau paramètre (dans les préférences avancées) pour le nombre de passages de cette fonction. [Pull request #9280](https://github.com/FreeCAD/FreeCAD/pull/9280)

## Web



## Ateliers externes 

### A2plus

### Assembly3

### Assembly4

### FCGear

### Ship

## Compilation

Depuis cette version, FreeCAD ne peut être compilé qu\'avec Qt 5.x et Python 3.x. La version la plus basse de Qt supportée est la 5.12, la version la plus basse de Python supportée est la 3.8.

Pour compiler FreeCAD, voir les instructions pour [Windows](Compile_on_Windows/fr.md), [Linux](Compile_on_Linux/fr.md) et [macOS](Compile_on_MacOS/fr.md).

Les systèmes d\'exploitation pris en charge sont :

-   Windows 7, 8, 10 et 11
-   Linux Ubuntu Focal Fossa (20.04) et plus récent
-   macOS : 10.12 Sierra ou plus récent



## Limitations connues 



### Windows 32 bits 

Depuis FreeCAD 0.19, nous ne supportons plus officiellement Windows 32 bits. FreeCAD pourrait fonctionner sur ces systèmes, mais aucun support n\'est donné.



### Bureau distant sous Windows 

Selon les capacités graphiques OpenGL d\'un ordinateur, il se peut que l\'on rencontre un plantage lors de l\'exécution de FreeCAD via le bureau à distance. Pour résoudre ce problème, mettez à jour votre pilote OpenGL. Si cela ne vous aide pas :

-   Téléchargez [cette bibliothèque OpenGL](https://downloads.fdossena.com/geth.php?r=mesa64-latest) pour Windows 64 bits et extrayez-la.
-   Renommez le fichier DLL en *opengl32sw.dll* et copiez-le dans le sous-dossier *bin* du dossier d\'installation de FreeCAD (écrasez la DLL existante).



### macOS : l\'atelier Start affiche une page blanche 

Si l\'[atelier Start](Start_Workbench/fr.md) n\'affiche qu\'une page blanche, vous devez activer l\'option **Utiliser le logiciel OpenGL** dans le menu **FreeCAD-0.21 → Préférences → Affichage**.



---
⏵ [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 0.21/fr
