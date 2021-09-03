


{{TOCright}}

Cette page contient différents réglages et paramètres que vous pouvez utiliser pour affiner votre installation FreeCAD ou pour résoudre certains problèmes.

## Option paramètres 

L\'[Editeur de préférences](Preferences_Editor/fr.md) FreeCAD du menu **Édition → Préférences** est couramment utilisé pour définir et manipuler le tableau des paramètres de FreeCAD.

Cependant, il est également possible d\'accéder, de modifier et de créer des paramètres manuellement, à l\'aide du [Editeur de paramètres](Std_DlgParameter/fr.md) situé dans le menu **Outils → Editer paramètres...**.

La liste ci-dessous répertorie les paramètres qui ne sont pas accessibles via l'éditeur de préférences mais que vous pouvez définir manuellement (situé dans **BaseApp/Preferences**)

-   **Bitmaps/Theme/ThemeSearchPaths** (booléen) : Défini à `False` pour que FreeCAD utilise ses icônes incluses au lieu du thème des icônes du système sous Linux.
-   **DockWindows/DAGView/Enabled** (booléen) : Défini à `True` pour activer un widget dockable beta de la [Vue DAG](DAG_view/fr.md). Après avoir changé la valeur du paramètre, un redémarrage de FreeCAD est nécessaire pour que le widget soit disponible dans la liste des vues/panneaux.
-   **DockWindows/PropertyView/Enabled** (booléen) : Défini à `True` pour activer un widget ancrable de l\'[Éditeur de propriétés](Property_editor/fr.md) indépendant de la vue combinée. Après avoir changé la valeur du paramètre, un redémarrage de FreeCAD est nécessaire pour que le widget soit disponible dans la liste des vues/panneaux.
-   **DockWindows/TreeView/Enabled** (booléen) : Défini à `True` pour activer un widget ancrable de la [vue en arborescence](Document_structure/fr.md) indépendant de la vue combinée. Après avoir changé la valeur du paramètre, un redémarrage de FreeCAD est nécessaire pour que le widget soit disponible dans la liste des vues/panneaux.
-   **Document/ChangeViewProviderTouchDocument** (booléen) : Défini à `False` pour que les changements de visibilité des éléments ne marquent pas le document comme modifié.
-   **Document/SaveThumbnailFix** (booléen) : Défini à `True` pour corriger un problème avec Qt5 qui empêche la génération de miniatures de fichiers `.FCStd`.
-   **General/RecentIncludesExported** (booléen) : Défini à `True` pour inclure les fichiers exportés dans la liste des fichiers récents. La valeur par défaut est `False`.
-   **General/RecentIncludesImported** (booléen) : Donnez la valeur `False` pour exclure les fichiers importés de la liste des fichiers récents. La valeur par défaut est `True`.
-   **Mod/Draft/defaultCameraHeight** (entier) : Définit la hauteur de la caméra lorsque Draft démarre dans un document vide. 0 désactive, la valeur par défaut de FreeCAD est 5, bon quand on travaille en millimètres, une bonne hauteur pour le travail en arc est 4500.
-   **Mod/Part/ParametricRefine** (booléen) : Défini à `False` pour que [Part RefineShape](Part_RefineShape.md) crée une copie indépendante plutôt qu\'une copie liée. La valeur par défaut est `True`.
-   **Mod/PartDesign/AdditiveHelixPreview** (booléen) : Défini à `True` pour s\'assurer qu\'une hélice additive qui n\'intersecte pas le corps est visible dans l\'aperçu. La valeur par défaut est `False`.
-   **Mod/PartDesign/SubtractiveHelixPreview** (booléen) : Défini à `True` pour qu\'une hélice soustractive qui n\'intersecte pas le corps soit visible dans l\'aperçu. La valeur par défaut est `True`.
-   **Mod/PartDesign/SwitchToTask** (booléen) : Défini à `False` pour empêcher l\'[atelier PartDesign](PartDesign_Workbench/fr.md) de passer au panneau Tâche au démarrage. La valeur par défaut est `True`.
-   **Mod/PartDesign/SwitchToWB** (booléen) : Définissez-le sur `False` pour empêcher l\'appel automatique de l\'[atelier PartDesign](PartDesign_Workbench/fr.md) lorsqu\'un [PartDesign Corps](PartDesign_Body/fr.md) est activé. La valeur par défaut est `True`.
-   **PropertyView/AutoTransactionView** (booléen) : Défini à `True` pour que les modifications des propriétés de l\'onglet View soient ajoutées à la pile d\'annulation (et donc annulables). La valeur par défaut est `False`.
-   **View/NavigationDebug** (booléen) : active la sortie de débogage des styles de navigation (à partir de la v0.19, seul le style de navigation Gesture a quelque chose à dire).
-   **View/SavePicture** (chaîne) : Défini à **FramebufferObject**, **PixelBuffer** ou **CoinOffscreenRenderer** pour différentes méthodes de production d\'images à partir de la vue 3D.

### Exportation du nom de fichier par défaut 

-   **General/ExportDefaultFilenameMultiple** (chaîne de caractères): définit le nom de fichier par défaut à utiliser lors de l\'exportation d\'objets multiples. La valeur par défaut est \"%F\".
-   **General/ExportDefaultFilenameSingle** (chaîne de caractères): définit le nom de fichier par défaut à utiliser lors de l\'exportation d\'un objet unique. La valeur par défaut est \"%F-%P-\".

Ces deux options permettent l\'insertion automatique de diverses informations dans le nom du fichier, en utilisant les caractères de format suivants :

-   %F - le nom du fichier .FCStd (ou l\'étiquette, si elle n\'est pas encore enregistrée)
-   %Lx - l\'étiquette du ou des objets sélectionnés, séparés par le caractère \'x\'.
-   %Px - l\'étiquette du ou des objets sélectionnés et de leur premier parent, séparés par le caractère \'x\'.
-   %U - la date et l\'heure, en UTC, [ISO 8601](https://fr.wikipedia.org/wiki/ISO_8601)
-   %D - la date et l\'heure, dans le fuseau horaire local, [ISO 8601](https://fr.wikipedia.org/wiki/ISO_8601)

Tous les autres caractères sont traités littéralement. Si le nom de fichier résultant est illégal, il sera modifié lors de la sauvegarde, les caractères illégaux étant remplacés par le trait de soulignement (\_).

## En rapport avec la souris 

-   **General/ComboBoxWheelEventFilter** (booléen) : sur `True` pour que les widgets ne captent pas l\'événement de la molette de la souris et empêchent le défilement des zones défilantes.
-   **View/GestureRollFwdCommand**, **View/GestureRollBackCommand** (chaîne): commandes à exécuter par des gestes de roulis de bouton de la souris de style de navigation Gesture.
-   **View/GestureMoveThreshold** (entier): le curseur de la souris à distance (px) doit se déplacer pour entrer dans les modes de rotation ou de panoramique du style de navigation Gesture. La valeur par défaut est 5.
-   **View/GestureTapHoldTimeout** (entier): définit le temps d\'attente (en millisecondes) pour passer en mode panoramique dans le style de navigation Gesture. Il peut être utile de l\'augmenter s\'il est difficile de faire glisser la géométrie dans l\'esquisse. La valeur par défaut est 700.

### Raccourci clavier 

### Touche Echap 

-   **General/TasksKeyEsc** (booléen): Créez et mettez à `False` pour désactiver la touche **Echap** sortant du [Panneau des tâches](Task_panel/fr.md) dans tous les ateliers (c\'est-à-dire si le panneau des tâches a le focus). **Remarque:** remplacé par [Sketcher Préférences](Sketcher_Preferences/fr#G.C3.A9n.C3.A9ral.md).
-   **Mod/Sketcher/ViewKeyEsc** (booléen): Créez et mettez à `False` pour désactiver les problèmes de la touche **Echap** en appuyant une à plusieurs fois, lors de l\'échappement de la création de géométrie/contraintes mode continue. (voir [fil de discussion](https://forum.freecadweb.org/viewtopic.php?f=3&t=42207&start=60#p367584))

## Ateliers particuliers 

-   L\'<img alt="" src=images/Workbench_TechDraw.svg  style="width:16px;"> [atelier TechDraw](TechDraw_Workbench/fr.md) dispose de plusieurs options masquées décrits dans [TechDraw Préférences](TechDraw_Preferences/fr#Paramètres_cachés.md).
-   L\'<img alt="" src=images/Workbench_Path.svg  style="width:16px;"> [atelier Path](Path_Workbench/fr.md) a une option pour activer les fonctionnalités expérimentales documentées dans [Path Fonctions expérimentales](Path_experimental/fr.md).
-   L\'<img alt="" src=images/Workbench_BIM.svg  style="width:16px;"> [atelier BIM](BIM_Workbench/fr.md):
    -   **Mod/BIM/DefaultPageScale** (flottant): mise à l\'échelle par défaut pour les nouvelles pages TechDraw créées à partir de l\'atelier BIM, au cas où le modèle ne contiendrait pas de champ de texte modifiable (insensible au texte) \"Échelle\" ou \"Mise à l\'échelle\".

## En relation 

-   [Editeur des paramètres](Std_DlgParameter/fr.md)
-   [Réglage des préférences](Preferences_Editor/fr.md)




[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md)
