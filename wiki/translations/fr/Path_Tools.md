# Path Tools/fr
{{TOCright}}

## Description

Cette page décrit l\'architecture ToolBit (Outil coupant) utilisée dans l\'[atelier Path](Path_Workbench/fr.md) qui est devenu le système par défaut de FreeCAD v 0.19. Pour l\'ancien système d\'outils voir [Path Gestionnaire d\'outils](Path_ToolLibraryEdit/fr.md). Les outils de l\'atelier Path sont gérés différemment de ceux des autres logiciels de FAO.

Il y a plusieurs concepts que l\'utilisateur doit comprendre :

-   [Path Forme d\'outil](Path_ToolShape/fr.md) : sont des modèles pour créer des outils. Les Formes d\'outil sont des documents FreeCAD qui modélisent l\'outil en utilisant des contraintes nommées. La forme d\'outil est un modèle d\'outil *abstrait* à partir duquel sont créées les instances d\'outils (appelées toolbits ou outils coupants). Par exemple, toutes les fraises partageront le même fichier Forme d\'outil.

-   [Path Outil coupant](Path_ToolBit/fr.md) : sont des instances d\'une forme d\'outil. Un outil coupant aura des valeurs *spécifiques* pour chacune des contraintes nommées dans la forme de l\'outil. Un outil coupant est utilisé dans un travail de trajectoire par le biais d\'un contrôleur d\'outils (Tool Controller). Le même outil coupant peut exister dans plusieurs bibliothèques.

-   [Path Bibliothèque des outils](Path_ToolBit_Library/fr.md) : contient une collection arbitraire d\'outils coupants . Les outils spécifiques d\'une bibliothèque sont entièrement laissés à la discrétion de l\'utilisateur. Cas d\'utilisation possibles pour les bibliothèques :
    -   Un utilisateur amateur peut n\'avoir qu\'une seule bibliothèque pour tous les outils qu\'il possède.
    -   Une bibliothèque peut contenir tous les outils utilisés pour un matériau spécifique comme l\'aluminium ou le bois.
    -   Une bibliothèque peut contenir des outils pour travailler sur un matériau spécifique.
    -   Une bibliothèque peut contenir des outils d\'un fournisseur spécifique.
    -   Une bibliothèque peut correspondre à la disposition d\'un changeur automatique d\'outils.

Un [Contrôleur d\'outil](Path_ToolController/fr.md) contrôle la façon dont un outil est utilisé dans une tâche de trajectoire. Un contrôleur combine l\'outil coupant avec les propriétés de la vitesse de la broche, de la direction et des taux d\'avance horizontaux et verticaux.

## Dialogues

L\'utilisateur interagit avec le système de gestion des outils par le biais d\'un menu de cheminement dans deux flux de travail différents. Chaque flux de travail a des éléments d\'interface graphique dédiés.

-   Le fenêtre **<img src="images/Path_ToolBitLibraryOpen.svg" width=24px> [Sélecteur d'outil coupant](Path_ToolBitDock/fr.md)** pour utiliser les outils dans une tâche de trajectoire en créant des contrôleurs d\'outils.

-    **<img src="images/Path_ToolBitDock.svg" width=24px> [Gestionnaire des outils coupants](Path_ToolBitLibraryOpen/fr.md)**pour gérer les outils de l\'utilisateur avec les boutons *Create Toolbit*, *Add Existing* et *Remove*.

## Organisation

Lorsque FreeCAD est installé, un exemple de hiérarchie de bibliothèques d\'outils et d\'outils coupants est créé dans le répertoire d\'installation à :

-   Sous Linux, il s\'agit généralement de {{FileName|/usr/lib64/FreeCAD/Mod/Path/Tools}}.
-   Sous Windows, il s\'agit généralement de {{FileName|C:\Program Files\FreeCAD\Mod\Path\Tools}}.
-   Sous macOS, il s\'agit généralement de {{FileName|/Applications/FreeCAD/Mod/Path/Tools}} {{ColoredText||Red|--> doit être révisé}}.




    Tools
      + Bit
      + Library
      + Shape

Il est toujours recommandé de stocker les outils coupants et les bibliothèques nouvellement créés dans un endroit sûr pour éviter qu\'ils ne soient écrasés lors d\'une mise à jour du programme. Même les formes d\'outils personnalisées peuvent être stockées dans des emplacements arbitraires où elles peuvent être sauvegardées. L\'utilisateur est toutefois encouragé à utiliser une structure logique comparable à celle illustrée ci-dessus pour que les boîtes à outils et les bibliothèques soient bien organisées. Lorsque le Tool library Manager est ouvert, Path vérifie l\'emplacement du répertoire de travail. Si l\'emplacement n\'est pas accessible en écriture ou est identique à l\'emplacement par exemple/par défaut, Path invite l\'utilisateur à sélectionner ou à créer un nouveau répertoire de travail.

## Options

Les références aux outils coupants et à leurs formes peuvent être stockées soit avec un chemin absolu, soit avec un chemin relatif au chemin de recherche. En général, il est recommandé d\'utiliser des chemins relatifs en raison de leur flexibilité et de leur robustesse face aux changements de mise en page. Si plusieurs outils ou formes d\'outils portant le même nom existent dans différents répertoires, il peut être nécessaire d\'utiliser des chemins absolus.

Voir [Path Préférences](Path_Preferences/fr.md) pour choisir si des chemins absolus ou relatifs sont utilisés.

## Migration à partir des outils existants 

Si vous utilisez l\'atelier FreeCAD Path depuis un certain temps, vous devrez peut-être ajuster vos préférences avant de pouvoir utiliser le système d\'outil coupant. Si en appuyant sur le bouton Bibliothèque d\'outils de la barre d\'outils, la boîte de dialogue des outils historiques s\'affiche, allez à la page ci-dessous dans les [Path Préférences](Path_Preferences/fr.md) et désactivez les outils historiques.
Vous devez redémarrer FreeCAD pour que la modification soit valide.

![Désactivation des outils historiques](images/Preferences.png )

## Démarrer avec les outils dans FC 0.19 

Lisez la section \Migration à partir des outils existants\ ci-dessus. Les étapes ci-dessous vous guideront dans le processus d\'obtention d\'un outil coupant dans votre **<img src="images/Path_Job.svg" width=16px> [Path Tâche](Path_Job/fr.md)** particulière.

En bref, le processus commence par un fichier forme d\'outil (profil) qui ne contient qu\'une esquisse FreeCAD de la moitié de la forme physique de l\'outil (profil). Ce fichier de la forme de l\'outil est ensuite utilisé comme base pour créer un fichier ToolBit contenant la représentation 3D de l\'outil coupant ou du couteau. Un ou plusieurs outils coupants sont affectés à un nombre quelconque de bibliothèques d\'outils, selon les besoins de l\'utilisateur. Cette structure et ce flux de travail permettent de partager des formes d\'outils, des outils coupants et des bibliothèques d\'outils entières, ce qui représente un grand pas en avant par rapport au système de gestion d\'outils existant avant la version 0.19.

### Vérification ou création une forme d\'outil 

L\'intégration d\'un outil de coupe ou d\'un outil dans une Path Tâche en vue de son utilisation dans des opérations commence par une [Forme d\'outil](Path_ToolShape/fr.md). Cette étape de vérification ou de création d\'une forme d\'outil n\'est pas nécessaire si vous disposez déjà d\'un outil coupant existant.

#### Vérification que la forme de l\'outil souhaitée existe 

-   FreeCAD inclut un ensemble de formes d\'outils communes avec chaque distribution. Visitez la page [Path Forme d\'outil](Path_ToolShape/fr.md) pour voir la liste des formes d\'outils communes incluses.
-   Vous pouvez disposer de fichiers de formes d\'outils supplémentaires dans vos fichiers personnels.
-   Soyez attentif à l\'[organisation](Path_Tools/fr#Organisation.md) du système Outils coupants dans son ensemble, comme mentionné ci-dessus.

#### Création une nouvelle forme d\'outil 

:   Suivez les instructions décrites dans la section [Utilisation](Path_ToolShape/fr#Utilisation.md) de la page [Path Forme d\'outil](Path_ToolShape/fr.md) pour créer une forme d\'outil personnalisée.

### Chargement ou création d\'un outil coupant 

Une fois que la forme de l\'outil (profil) souhaitée existe, vous devez créer un [outil coupant](Path_ToolBit/fr.md) en utilisant la forme d\'outil (profil).

1.  Dans l\'<img alt="" src=images/Workbench_Path.svg  style="width:24px;"> [atelier Path](Path_Workbench/fr.md), faites **Path → Create Tool**.
2.  Dans le panneau de tâches de création d\'[outil coupant](Path_ToolBit/fr.md) qui s\'affiche, donnez un nom au nouvel outil et sélectionnez le fichier de forme d\'outil correspondant comme base de ce nouvel outil.
3.  Une vignette de la forme d\'outil sélectionnée devrait apparaître avec une liste de paramètres.
4.  Réglez les paramètres de l\'embout comme vous le souhaitez.
5.  Cliquez sur **OK** pour enregistrer le nouvel outil coupant.
6.  Le nouvel outil apparaît dans l\'arbre d\'objets de FreeCAD.

### Sauvegarder le nouvel outil coupant 

1.  Localisez et sélectionnez le nouvel outil dans l\'arbre des objets de la fenêtre principale de FreeCAD.
2.  Dans la barre de menu de l\'<img alt="" src=images/Workbench_Path.svg  style="width:24px;"> [atelier Path](Path_Workbench/fr.md), sélectionnez **Path → Save Tool as...**.
3.  Une fenêtre contextuelle s\'affiche.
4.  Allez jusqu\'au dossier dans lequel vous souhaitez enregistrer le nouveau fichier de l\'outil coupant.
5.  Saisissez un nom de fichier pour l\'outil coupant.
6.  Cliquez sur le bouton **Save**.

### Enregistrement de l\'outil coupant dans une bibliothèque d\'outils 

1.  Dans l\'<img alt="" src=images/Workbench_Path.svg  style="width:24px;"> [atelier Path](Path_Workbench/fr.md), faites **Path → Open ToolBit Library editor**.
2.  La fenêtre [Gestionnaire d\'outils](Path_ToolBitLibraryOpen/fr.md) s\'ouvre.
3.  En haut de cette fenêtre, vérifiez ou définissez le chemin d\'accès au dossier contenant vos bibliothèques d\'outils existantes, ou l\'emplacement où vous souhaitez stocker vos bibliothèques d\'outils.
4.  Sous le chemin d\'accès, à gauche, se trouve la zone de liste des bibliothèques d\'outils. Cliquez sur une bibliothèque d\'outils existante que vous souhaitez utiliser comme destination pour votre nouvel outil coupant ou cliquez sur l\'icône verte plus pour créer une nouvelle bibliothèque d\'outils dans le dossier identifié ci-dessus.
5.  Sur le côté droit de la fenêtre de l\'éditeur de bibliothèque d\'outils se trouve la liste des outils coupants et les boutons d\'action pour la bibliothèque d\'outils actuellement sélectionnée. Cliquez sur l\'icône **Add ToolBit**.
6.  Dans la fenêtre de navigation de fichier qui s\'ouvre, naviguez jusqu\'à votre nouvel élément, sélectionnez-le et cliquez sur le bouton **Open**. Le nouvel outil coupant sera ajouté à la bibliothèque d\'outils active.
7.  N\'oubliez pas de cliquer sur le bouton **Save Table** au bas de la fenêtre de la bibliothèque d\'outils afin d\'enregistrer les modifications.
8.  Laissez cette fenêtre de bibliothèque d\'outils ouverte pour l\'étape suivante.
9.  Une fois que vos outils coupants sont créés et enregistrés dans une bibliothèque d\'outils coupants, vous pouvez les réutiliser.

### Ajout d\'un outil coupant à une tâche 

1.  Dans la fenêtre de la bibliothèque d\'outils ouverte, localisez et activez la bibliothèque d\'outils souhaitée.
2.  Sélectionnez le(s) outil(s) à ajouter à la tâche. Sélectionnez en plusieurs en maintenant la touche CTRL enfoncée lors de la sélection.
3.  Cliquez sur le bouton **Add Tool Controller(s) to Job**.
4.  Fermez le gestionnaire d\'outils.

## En relation 

-   [Path Outil coupant](Path_ToolBit/fr.md)
-   [Path Gestionnaire des outils](Path_ToolBitLibraryOpen/fr.md)





{{Path_Tools_navi

}}

---
[documentation index](../README.md) > [Path](Path_Workbench.md) > Path Tools/fr
