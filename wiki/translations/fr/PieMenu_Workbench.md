# <img alt="Icône de l\'atelier PieMenu" src=images/PieMenuWorkbench.svg  style="width:64px;"> PieMenu Workbench/fr




## Introduction

L\'<img alt="" src=images/PieMenuWorkbench.svg  style="width:32px;"> **atelier PieMenu** est un [atelier externe](External_workbenches/fr.md) qui apporte un menu personnalisable fournissant un accès rapide aux outils FreeCAD via des raccourcis clavier. Vous pouvez choisir parmi de multiples formes, thèmes, personnaliser les outils et les raccourcis, et bien plus encore.

<img alt="" src=images/PieMenu_example.jpg  style="width:300px;">



*Exemple d'un PieMenu contenant 16 sections*

Dans l\'exemple ci-dessus, la première section correspond aux ateliers paramétriques, puis aux ateliers pour la conception et les dessins techniques, puis aux ateliers pour les assemblages, puis à quelques ateliers permettant à l\'auteur de tester de nouveaux outils et enfin à un raccourci vers les outils web.

## Installation

1.  Installez l\'atelier PieMenu via le <img alt="" src=images/AddonManager.svg  style="width:24px;"> [gestionnaire d\'extensions](Std_AddonMgr/fr.md). Pour une installation manuelle, voir [Installer des ateliers supplémentaires](Installing_more_workbenches/fr.md).
2.  Redémarrez FreeCAD.



## Définitions

-   **PieMenu** est un ensemble d\'outils regroupés dans un menu pour créer une barre de raccourcis accessible par un raccourci clavier.
-   **ToolBar** est un ensemble de raccourcis existants dans FreeCAD, contenant un ensemble d\'outils d\'un plan de travail.
-   **Context Mode** : un mode d\'activation spécial qui prend en compte la géométrie sélectionnée par l\'utilisateur pour déterminer quel PieMenu doit être activé en fonction des paramètres.
-   **Global shortcut** : raccourci général assigné au PieMenu pour ouvrir le PieMenu par défaut.
-   **Individual shortcut** : raccourci attribué à un PieMenu particulier.



## Utilisation

1.  Appuyer sur le raccourci global (par défaut la touche **Tab**) du clavier pour lancer le PieMenu.



### Premier lancement 

-   Il peut être nécessaire de redémarrer FreeCAD après l\'installation et après l\'activation initiale de PieMenu pour s\'assurer que la configuration est correcte.
-   Par défaut, le raccourci global pour activer PieMenu est la touche **Tab**. Toutefois, si cela ne fonctionne pas ou si vous souhaitez le modifier, vous pouvez accéder aux Préférences via le menu **Accessories → Pie menu settings** puis l\'onglet **Global settings**, puis **Global shortcut**.
-   Vous pouvez attribuer un raccourci simple (par exemple, une seule touche comme **A**), un raccourci composite (par exemple, **CTRL**+**Q**) ou un raccourci à plusieurs touches (par exemple, **F**, **F**).



### Créer/modifier un PieMenu 

Dans le cas d\'une nouvelle installation, PieMenu créera 3 PieMenus (**View**, **PartDesign** et **Sketcher**) avec quelques outils communs. Pour créer ou modifier d\'autres PieMenus, il suffit d\'aller dans les préférences (**QuickMenu → Preferences** ou **Accessories Menu → PieMenu Preferences**).

<img alt="" src=images/PieMenu_QuickMenu.png  style="width:300px;">



*QuickMenu*


**QuickMenu**

est le menu contextuel qui s\'affiche lorsqu\'on clique sur le bouton intégré dans le PieMenu, il permet d\'ajuster rapidement certains paramètres. Si le menu rapide n\'est pas visible, il doit être activé dans **Preferences** en activant l\'option **Show QuickMenu**.



## Préférences de PieMenu 

=

La fenêtre de préférences PieMenu contient 3 sections empilées verticalement.



### Section supérieure 

<img alt="" src=images/PieMenu_top_section.png  style="width:400px;">

La section supérieure contient une série de boutons qui vous permettent de :

1.  changer l\'icône de votre PieMenu.
2.  passer d\'un PieMenu à l\'autre.
3.  ajouter un nouveau PieMenu.
4.  supprimer un PieMenu.
5.  renommer un PieMenu.
6.  copier un PieMenu.
7.  créer un nouveau PieMenu à partir d\'une barre d\'outils existante.



### Section centrale 

La section centrale est à son tour divisée horizontalement en 3 sections qui peuvent être redimensionnées ou même cachées à l\'aide des séparateurs placés entre les sections. La première section comporte 4 onglets contenant chacun plusieurs paramètres/outils.



### Onglet PieMenu 

Créez un nouveau PieMenu en cliquant sur le bouton **+**, nommez-le et validez. Il sera alors visible dans la liste déroulante des PieMenus. Modifiez et ajustez les paramètres disponibles (les paramètres peuvent varier en fonction de la configuration du PieMenu) :

<img alt="" src=images/PieMenu_Tab_PieMenu.png  style="width:600px;">



*Fenêtre divisée en 3 sections montrant les paramètres de PieMenu, une liste d'actions PieMenu et l'aperçu du PieMenu utilisé*

.

-   **Menu size** : ajuste la taille du menu.
-   **Button size** : ajuste la taille des boutons (Note : la taille maximale dépend de la taille du menu).
-   **Shape** : plusieurs formes sont disponibles.
-   **Trigger Mode** : choisit le mode d\'activation : \'On press\' ou \'On hover\' de la souris pour ce PieMenu.
-   **Set the hover activation delay** : pour éviter un déclenchement trop rapide lors du passage de plusieurs commandes, il est nécessaire de définir un délai suffisant.
-   **Show command names** : certaines formes permettent d\'afficher les noms des commandes.
-   **Number of rows and columns** : pour les formes permettant une mise en page en lignes et/ou en colonnes.
-   **Icon spacing** : ajuste l\'espace entre les boutons.



### Onglet Tools 

<img alt="" src=images/PieMenu_Tab_Tools.png  style="width:600px;">



*Fenêtre divisée en 2 sections contenant les outils disponibles et l'aperçu du PieMenu utilisé*

-   Cochez les outils souhaités pour les ajouter à votre liste d\'outils PieMenu.
-   Vous pouvez déplacer ou supprimer des outils en utilisant les boutons situés sous la liste des outils.
-   **Astuce** : vous pouvez rechercher des outils par leur nom dans la barre de recherche.



### Onglet Context 

<img alt="" src=images/PieMenu_Tab_Context.png  style="width:600px;">



*Fenêtre divisée en 2 sections contenant les paramètres contextuels et la liste des actions du PieMenu.*

***(Attention, cette fonction n\'est pas entièrement opérationnelle, il peut y avoir des bogues)***

Context permet d\'activer un PieMenu spécifique en fonction de la géométrie sélectionnée par l\'utilisateur. Par exemple, lorsque l\'utilisateur sélectionne une face dans le modèle 3D, il peut souhaiter qu\'un menu Pie s\'ouvre pour créer une \"nouvelle esquisse\". C\'est possible avec le mode Context.



##### Comment utiliser le mode contextuel ? 

Dans le cadre d\'une utilisation normale, PieMenu s\'ouvre par défaut lorsque l\'on appuie sur le raccourci global, mais il arrive que l\'utilisateur ait besoin d\'outils spécifiques en fonction du type d\'objet 3D sélectionné.

Par exemple, prenons le cas *vous ne voulez que les outils qui sont utiles lorsqu\'une face d\'un objet 3D est sélectionnée dans PartDesign*. Vous pouvez créer un PieMenu contenant ces outils et définir les conditions d\'affichage de ce PieMenu dans l\'onglet Context comme suit :

-   Si vous sélectionnez une seule face (dans l\'atelier PartDesign) et que vous appuyez sur le raccourci global, ce PieMenu s\'affiche, donnant accès uniquement aux outils que l\'utilisateur a définis dans ce PieMenu. Si la case \"Immediate triggering when conditions are met\" est cochée, l\'affichage immédiat du menu PieMenu est déclenché sans qu\'il soit nécessaire d\'appuyer sur le raccourci global.

:   <img alt="" src=images/PieMenu_Context_1.png  style="width:600px;">

-   L\'avantage est que vous pouvez créer autant de PieMenus que nécessaire pour couvrir vos besoins actuels. Par exemple, vous pouvez avoir besoin d\'un PieMenu avec seulement les outils qui peuvent être utilisés dans PartDesign avec les arêtes :

:   <img alt="" src=images/PieMenu_Context_2.png  style="width:600px;">

-   En raison de l\'héritage du code des versions précédentes de PieMenu, pour que le mode contextuel fonctionne, il est nécessaire que le mode \"Global Context\" soit activé soit par le menu rapide, soit par les paramètres généraux.

:   <img alt="" src=images/PieMenu_Context_3.png  style="width:600px;">



### Onglet Global settings 

<img alt="" src=images/PieMenu_Tab_GlobalSettings.png  style="width:600px;">



*Fenêtre contenant les paramètres globaux qui s'appliquent à tous les PieMenus*

Ici, vous pouvez :

-   sélectionner le style du thème.
-   activer ou désactiver le menu rapide.
-   activer ou désactiver le mode contextuel (également disponible dans le menu rapide).
-   activer ou désactiver le mode bascule pour le raccourci global.
-   activer le clic droit long pour ouvrir la fonction PieMenu.
-   paramètres d\'importation et d\'exportation.
-   attribuer le raccourci global.



### Section inférieure 

<img alt="" src=images/PieMenu_bottom_section.png  style="width:400px;">

La section inférieure contient une série de boutons qui vous permettent :

1.  ouvrir la page **About**.
2.  ouvrir la documentation en utilisant le [module d\'aide](Help_Module/fr.md) de FreeCAD (vérifiez votre réglage dans **Édition → Préférences → Général → Aide → Affichage**).
3.  fermer la fenêtre des préférences.



## Références

-   Auteur : Grubuntu
-   Code source : <https://github.com/Grubuntu/PieMenu>
-   Rapports de bogues et demandes de fonctionnalités : <https://github.com/Grubuntu/PieMenu/issues>
-   Sujet du forum : <https://forum.freecad.org/viewtopic.php?t=84101>



## Liens

-   [CHANGELOG](https://github.com/Grubuntu/PieMenu/blob/master/CHANGELOG.md)



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > PieMenu Workbench/fr
