# Fine-tuning/fr
## Introduction

L\'[Editeur de préférences](Preferences_Editor/fr.md) de FreeCAD du menu **Édition → Préférences** est généralement utilisé pour définir et manipuler la table des paramètres de FreeCAD.

Cependant, il est également possible d\'accéder, de modifier et de créer des paramètres manuellement, à l\'aide de l\'[Éditeur de paramètres](Std_DlgParameter/fr.md) du menu **Outils → Éditer les paramètres...**.

Cette page liste les paramètres qui ne sont pas accessibles via l\'éditeur de préférences, mais que vous pouvez régler manuellement pour affiner votre installation de FreeCAD ou résoudre des problèmes. Tous les paramètres sont situés dans **BaseApp/Préférences/**.



## Général

-   **Addons/developerMode** (booléen) : défini sur `True` pour activer le mode développeur du [Gestionnaire des extensions](Std_AddonMgr/fr.md). Voir [Métadonnées du package](Package_Metadata/fr#Validation.md).

-   **Bitmaps/Theme/ThemeSearchPaths** (booléen) : défini sur `False` pour que FreeCAD utilise ses icônes incluses au lieu du thème des icônes du système sous Linux.

-   **Dialog/DontUseNativeColorDialog** (booléen) : paramètre de la boîte de dialogue du sélecteur de couleur. Définir à `False` si vous voulez que FreeCAD utilise la boîte de dialogue de couleur natif de votre système plutôt que la boîte de dialogue de couleur Qt. La valeur par défaut est `True`.

-   **Dialog/DontUseNativeDialog**\' (booléen) : paramètre de dialogue de fichier. Définir à `False` si vous voulez utiliser la boîte de dialogue native de fichier lors de l\'ouverture de fichiers ou à `True` pour utiliser la boîte de dialogue File Picker de Qt. La valeur par défaut dépend d\'un paramètre de compilation : #define (USE_QT_FILEDIALOG).

-   **Dialog/DontUseNativeFontDialog** (booléen) : utilisé par la commande [Draft Forme à partir d\'un texte](Draft_ShapeString/fr.md). Définir à `False` pour utiliser la boîte de dialogue de la police native. La valeur par défaut est `True`.

-   **DockWindows/DAGView/Enabled** (booléen) : défini sur `True` pour activer un widget dockable beta de la [Vue DAG](DAG_view/fr.md). Après avoir changé la valeur du paramètre, un redémarrage de FreeCAD est nécessaire pour que le widget soit disponible dans la liste des vues/panneaux.

-   **DockWindows/PropertyView/Enabled** (booléen) : défini sur `True` pour activer un widget ancrable de l\'[Éditeur de propriétés](Property_editor/fr.md) indépendant de la vue combinée. Après avoir changé la valeur du paramètre, un redémarrage de FreeCAD est nécessaire pour que le widget soit disponible dans la liste des vues/panneaux.

-   **Document/AutoNameDynamicProperty** (booléen) : défini sur `True` pour que FreeCAD renomme automatiquement les propriétés dynamiques avec un nom spécifié invalide au lieu de lancer une exception. Notez que le code Python n\'aura pas accès au nouveau nom.

-   **DockWindows/TreeView/Enabled** (booléen) : défini sur `True` pour activer un widget ancrable de la [vue en arborescence](Document_structure/fr.md) indépendant de la vue combinée. Après avoir changé la valeur du paramètre, un redémarrage de FreeCAD est nécessaire pour que le widget soit disponible dans la liste des vues/panneaux.

-   **Document/ChangeViewProviderTouchDocument** (booléen) : défini sur `False` pour que les changements de visibilité des éléments ne marquent pas le document comme modifié.

-   **Document/SaveThumbnailFix** (booléen) : défini sur `True` pour corriger un problème avec Qt5 qui empêche la génération de miniatures de fichiers `.FCStd`.

-   **General/LockToolBars** (booléen) : défini sur `True` pour empêcher les barres d\'outils d\'être déplaçables et pour cacher les petites poignées de déplacement. Surtout utilisé en conjonction avec des feuilles de style qui rendent les barres d\'outils verticales.

-   **General/RecentIncludesExported** (booléen) : défini sur `True` pour inclure les fichiers exportés dans la liste des fichiers récents. La valeur par défaut est `False`.

-   **General/RecentIncludesImported** (booléen) : défini sur `False` pour exclure les fichiers importés de la liste des fichiers récents. La valeur par défaut est `True`.

-   **General/ShowSplasherMessages** (booléen) : défini sur `False` pour ne pas afficher les messages sur l\'écran de démarrage. Cela peut réduire le temps de démarrage de FreeCAD. La valeur par défaut est `True`.

-   **Macro/DuplicateFrom001** : (booléen) : défini sur `True` pour toujours commencer à chercher le nom de fichier de macro dupliqué suggéré avec \@001 au lieu du \@NNN en cours, le cas échéant. La valeur par défaut est `False`.

-   **Macro/DuplicateIgnoreExtraNote** (booléen) : défini sur `True` pour ignorer la note supplémentaire lors de la suggestion d\'un nom de fichier de macro dupliqué. La note supplémentaire est le texte du nom de fichier qui suit \"@NNN\" et précède \".FCMacro\". Exemple : \"my_macro@005.my_note.FCMacro\". Si `True`, le nom de fichier suivant suggéré est \"my_macro@006.FCMacro\". S\'il est défini sur `False`, le prochain nom de fichier suggéré est \"my_macro@006.my_note.FCMacro\". Pour être reconnu comme une note supplémentaire, le texte doit commencer par un point (\".\") après le \"@NNN\". Sinon, par exemple, \"my_macro@006_my_note.FCMacro\" se voit suggérer \"my_macro@006_my_note@001.FCMacro\" comme nouveau nom de fichier, ce qui peut être souhaitable dans certains cas. La valeur par défaut est `False`.

-   **Macro/ReplaceSpaces** (booléen) : défini sur `False` si vous ne voulez pas que les espaces dans vos noms de fichiers soient automatiquement convertis en caractères de soulignement lorsque vous créez, renommez ou dupliquez une macro. Cela n\'affecte pas les fichiers existants, mais uniquement lors de la création d\'un nouveau fichier ou du renommage ou de la duplication d\'un fichier existant. La valeur par défaut est `True`.

-   **MainWindow/ClearMenuBar** (booléen) : défini sur `True` pour effacer la barre de menu lors du changement d\'atelier, utile lors de l\'utilisation d\'un menu global, car elle peut ne pas être mise à jour lors du changement d\'atelier et peut être rapidement encombrée par les entrées de menu de chaque atelier. La valeur par défaut est `False`. Sous macOS, elle est effacée dans les deux sens pour contourner un bogue de Qt.

-   *MainWindow/ToolBarNameAsToolTip* (booléen) : défini sur `False` pour ne pas obtenir le nom de la barre d\'outils comme infobulle. La valeur par défaut est `True`.

-   **PropertyView/AutoTransactionView** (booléen) : défini sur `True` pour que les modifications des propriétés de l\'onglet View soient ajoutées à la pile d\'annulation (et donc annulables). La valeur par défaut est `False`.

-   **Selection/AutoShowSelectionView** (booléen) : défini sur `True` pour que le volet de la vue de sélection s\'affiche automatiquement lorsque vous sélectionnez quelque chose. La valeur par défaut est `False`.

-   **Selection/singleClickFeatureSelect** (booléen) : défini sur `False` pour désactiver la sélection en un seul clic d\'une fonction dans PartDesign. La valeur par défaut est `True`.

-   **TreeView/TreeViewStretchDescription** (booléen) : défini sur `True` pour étirer la colonne \'Description\' dans la [Vue en arborescence](Tree_view/fr.md) vers le bord droit du volet. La valeur par défaut est `False`.

-   **TreeView/HideColumn** (booléen) : défini sur {{True}} pour cacher la colonne \"Description\" dans la [Vue en arborescence](Tree_view/fr.md). La valeur par défaut est `False`.

-    {{VersionMinus/fr|0.20}}**View/Dimensions3dColor** (chaîne) : définit une valeur de couleur au format hexa `#RRGGBB` pour modifier la couleur d\'affichage des dimensions directes dans [Part Mesure linéaire](Part_Measure_Linear/fr.md). Pour {{VersionPlus/fr|0.21}}, voir [PartDesign Préférences](PartDesign_Preferences/fr#Mesure.md).

-    {{VersionMinus/fr|0.20}}**View/DimensionsAngularColor** (chaîne) : définit une valeur de couleur au format hexa `#RRGGBB` pour modifier la couleur d\'affichage de la dimension angulaire dans [Part Mesure angulaire](Part_Measure_Angular/fr.md). Pour {{VersionPlus/fr|0.21}}, voir [PartDesign Préférences](PartDesign_Preferences/fr#Mesure.md).

-    {{VersionMinus/fr|0.20}}**View/DimensionsDeltaColor** (chaîne) : définit une valeur de couleur au format hexa `#RRGGBB` pour modifier la couleur d\'affichage des dimensions orthogonales dans [Part Mesure linéaire](Part_Measure_Linear/fr.md). Pour {{VersionPlus/fr|0.21}}, voir [PartDesign Préférences](PartDesign_Preferences/fr#Mesure.md).

-   **View/NavigationDebug** (booléen) : active la sortie de débogage des styles de navigation (à partir de la v0.19, seul le style de navigation Gesture a quelque chose à dire).

-   **View/SavePicture** (chaîne) : défini sur **FramebufferObject**, **PixelBuffer** ou **CoinOffscreenRenderer** pour différentes méthodes de production d\'images à partir de la vue 3D.



## Nom des fichiers d\'exportation par défaut 

-   **General/ExportDefaultFilenameMultiple** (chaîne de caractères) : définit le nom de fichier par défaut à utiliser lors de l\'exportation d\'objets multiples. La valeur par défaut est \"%F\".
-   **General/ExportDefaultFilenameSingle** (chaîne de caractères) : définit le nom de fichier par défaut à utiliser lors de l\'exportation d\'un objet unique. La valeur par défaut est \"%F-%P-\".

Ces deux options permettent l\'insertion automatique de diverses informations dans le nom du fichier, en utilisant les caractères de format suivants :

-   %F - le nom du fichier .FCStd (ou l\'étiquette, si elle n\'est pas encore enregistrée)
-   %Lx - l\'étiquette du ou des objets sélectionnés, séparés par le caractère \'x\'.
-   %Px - l\'étiquette du ou des objets sélectionnés et de leur premier parent, séparés par le caractère \'x\'.
-   %U - la date et l\'heure, en UTC, [ISO 8601](https://fr.wikipedia.org/wiki/ISO_8601)
-   %D - la date et l\'heure, dans le fuseau horaire local, [ISO 8601](https://fr.wikipedia.org/wiki/ISO_8601)

Tous les autres caractères sont traités littéralement. Si le nom de fichier résultant est illégal, il sera modifié lors de la sauvegarde, les caractères illégaux étant remplacés par le trait de soulignement (\_).



## En rapport avec la souris 

-   **General/ComboBoxWheelEventFilter** (booléen) : défini sur `True` pour que les widgets ne captent pas l\'événement de la molette de la souris et empêchent le défilement des zones défilantes. Nécessite le redémarrage de FreeCAD pour être pris en compte.
-   **View/GestureMoveThreshold** (entier) : le curseur de la souris à distance (px) doit se déplacer pour entrer dans les modes de rotation ou de panoramique du style de navigation Gesture. La valeur par défaut est 5.
-   **View/GestureRollFwdCommand**, **View/GestureRollBackCommand** (chaîne) : commandes à exécuter par des gestes de roulis de bouton de la souris de style de navigation Gesture.
-   **View/GestureTapHoldTimeout** (entier) : définit le temps d\'attente (en millisecondes) pour passer en mode panoramique dans le style de navigation Gesture. Il peut être utile de l\'augmenter s\'il est difficile de faire glisser la géométrie dans l\'esquisse. La valeur par défaut est 700.



## Raccourcis clavier 



### Touche Echap 

-   **General/TasksKeyEsc** (booléen) : défini sur `False` pour désactiver la touche **Echap** sortant du [Panneau des tâches](Task_panel/fr.md) dans tous les ateliers (c\'est-à-dire si le panneau des tâches a le focus).



## Cube de navigation 

Voir [Cube de navigation](Navigation_Cube/fr#Paramètres_avancés.md).



## Ateliers particuliers 



### <img alt="" src=images/Workbench_BIM.svg  style="width:24px;"> [Atelier BIM](BIM_Workbench/fr.md) 

-   **Mod/BIM/DefaultPageScale** (flottant) : échelle par défaut pour les nouvelles pages de TechDraw créées à partir de l\'atelier BIM, dans le cas où le modèle ne contient pas de champ de texte éditable \"Scale\" ou \"Scaling\" (insensible à la casse).



### <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Atelier Draft](Draft_Workbench/fr.md) 

-   **Mod/Draft/DefaultAnnoDisplayMode** (entier) : réglé sur {{Value|1}} pour créer des annotations Draft ([textes](Draft_Text/fr.md), [dimensions](Draft_Dimension/fr.md) et [étiquettes](Draft_Label/fr.md)) avec leur **Mode d'affichage** réglé sur {{Value|Écran}}. Réglé sur {{Value|0}} pour les nouvelles annotations avec cette propriété définie sur {{Value|Monde}}. Par défaut, c\'est {{Value|0}}. {{Version/fr|0.22}}
-   **Mod/Draft/GridHideInOtherWorkbenches** (booléen) : défini sur `False` pour conserver la [Draft grille](Draft_ToggleGrid/fr.md) lors du passage à des ateliers autres que [Arch](Arch_Workbench/fr.md), [BIM](BIM_Workbench/fr.md) ou [Draft](Draft_Workbench/fr.md). La valeur par défaut est `True`. {{Version/fr|0.22}}
-   **Mod/Draft/useSupport** (booléen) : défini sur `True` pour que la propriété **Support** des objets Draft créés sur une face d\'un objet de base existant soit attribuée à cet objet de base. C\'était le comportement standard avant la version 0.19 de FreeCAD. Notez que ce paramètre peut ne pas être pris en charge dans les versions futures. La valeur par défaut est `False`.



### <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Atelier Part](Part_Workbench/fr.md) 

-   **Mod/Part/ParametricRefine** (booléen) : défini sur `False` pour que [Part Affiner la forme](Part_RefineShape/fr.md) crée une copie indépendante plutôt qu\'une copie liée. La valeur par défaut est `True`.



### <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Atelier PartDesign](PartDesign_Workbench/fr.md) 

-   **Mod/PartDesign/AdditiveHelixPreview** (booléen) : défini sur `True` pour s\'assurer qu\'une hélice additive qui n\'intersecte pas le corps est visible dans l\'aperçu. La valeur par défaut est `False`.
-   **Mod/PartDesign/SubtractiveHelixPreview** (booléen) : défini sur `True` pour qu\'une hélice soustractive qui n\'intersecte pas le corps soit visible dans l\'aperçu. La valeur par défaut est `True`.
-   **Mod/PartDesign/SwitchToTask** (booléen) : défini sur `False` pour empêcher l\'[atelier PartDesign](PartDesign_Workbench/fr.md) de passer au panneau Tâche au démarrage. La valeur par défaut est `True`.
-   **Mod/PartDesign/SwitchToWB** (booléen) : défini sur `False` pour empêcher l\'appel automatique de l\'[atelier PartDesign](PartDesign_Workbench/fr.md) lorsqu\'un [PartDesign Corps](PartDesign_Body/fr.md) est activé. La valeur par défaut est `True`.



### <img alt="" src=images/Workbench_Path.svg  style="width:24px;"> [Atelier Path](Path_Workbench/fr.md) 

-   L\'[atelier Path](Path_Workbench/fr.md) dispose de deux options pour activer les fonctions expérimentales documentées sur la page [Path Fonctions expérimentales](Path_experimental/fr.md).



### <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Atelier Sketcher](Sketcher_Workbench/fr.md) 

-   **Mod/Sketcher/RadiusDiameterConstraintDisplayAngleRandomness** (flottant) : définit un angle aléatoire sur la valeur supérieure. La valeur est la plage de l\'angle aléatoire, centrée sur l\'angle de base. La valeur par défaut est 0 degré.
-   **Mod/Sketcher/RadiusDiameterConstraintDisplayBaseAngle** (flottant) : définit l\'angle (par rapport à l\'horizontale) utilisé pour afficher les contraintes de rayon/diamètre dans Sketcher au moment de la création. La valeur par défaut est de 15 degrés (si aucune valeur n\'est définie).
-   **Mod/Sketcher/RoundRectangleSuggConstraints** (booléen) : défini sur `False` pour désactiver l\'ajout de deux points de construction supplémentaires lors de la création d\'un rectangle arrondi. {{Version/fr|0.21}}



#### Couleurs des étiquettes de contraintes 

L\'étiquette dans Sketcher qui affiche l\'état en cours des contraintes (par exemple, \"Underconstrained\", \"Fully Constrained\", etc\...) peut être stylisée sur une base par état, soit à l\'aide de la feuille de style Qt, soit via les préférences de l\'utilisateur. Les préférences de l\'utilisateur sont prioritaires si elles ont été définies (dans **Mod/Sketcher/General**) :

-   **EmptySketchMessageColor** - Valeur par défaut à 50% d\'opacité noire.
-   **UnderconstrainedMessageColor** - Noir par défaut
-   **MalformedConstraintMessageColor** - Rouge par défaut
-   **ConflictingConstraintMessageColor** - Rouge par défaut
-   **RedundantConstraintMessageColor** - Rouge orangé par défaut
-   **PartiallyRedundantConstraintMessageColor** - Bleu royal par défaut
-   **SolverFailedMessageColor** - Rouge par défaut
-   **FullyConstrainedMessageColor** - Vert par défaut



### <img alt="" src=images/Workbench_Start.svg  style="width:24px;"> [Atelier Start](Start_Workbench/fr.md) 

-   **Mod/Start/DefaultImportXXX** (chaîne) : où XXX est une extension de fichier en minuscules. Par exemple DefaultImportifc pour les fichiers .IFC. Permet de définir un module d\'importation par défaut à utiliser lorsque l\'on clique sur une icône de la page de démarrage, lorsque plusieurs importateurs sont disponibles. Par exemple, en définissant DefaultImportifc = ifc_import, l\'importateur NativeIFC sera utilisé s\'il est disponible. {{Version/fr|0.21}}
-   **Mod/Start/TimeFormat** (chaîne) : chaîne de format temporel telle que {{Value|%m/%d/%Y %H:%M:%S}} utilisée pour la date dans l\'infobulle affichée lorsqu\'un élément de la page de démarrage est survolé.



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Fine-tuning/fr
