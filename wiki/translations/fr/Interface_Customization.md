# Interface Customization/fr
{{TOCright}}

## Introduction

L\'interface FreeCAD est basée sur la boîte à outils [Qt](https   *//fr.wikipedia.org/wiki/Qt) et possède une organisation de pointe. Certains aspects de l\'interface peuvent être personnalisés. Vous pouvez, par exemple, ajouter des barres d\'outils personnalisées avec des outils de plusieurs ateliers ou des outils définis dans des macros et vous pouvez créer vos propres raccourcis clavier. Mais les menus et barres d\'outils par défaut fournis avec FreeCAD et ses ateliers ne peuvent pas être modifiés.

![](images/Std_DlgCustomize_tab_Toolbars.png ) 
*La boite de dialogue de personnalisation de l'interface*

## Utilisation

1.  Les commandes disponibles dans la boite de dialogue de personnalisation d\'interface dépendent des ateliers qui ont été chargés dans la session FreeCAD en cours. Vous devez donc d\'abord charger tous les établis dont vous souhaitez avoir accès aux commandes.
2.  Il existe plusieurs façons d\'appeler la commande <img alt="" src=images/Std_DlgCustomize.svg  style="width   *16px;"> [Std Personnalisation](Std_DlgCustomize/fr.md)   *
    -   Sélectionnez l\'option **Outils → <img src="images/Std_DlgCustomize.svg" width=16px> Personnaliser...** dans le menu.
    -   Cliquez avec le bouton droit sur une zone de barre d\'outils et choisissez **<img src="images/Std_DlgCustomize.svg" width=16px> Personnaliser...** dans le menu contextuel.
3.  La boîte de dialogue Personnaliser s\'ouvre. Pour plus d\'informations, voir [Options](#Options.md).
4.  Le bouton **Aide** ne fonctionne pas pour le moment.
5.  Appuyez sur le bouton **Fermer** pour fermer la boîte de dialogue.

## Options

Dans la boîte de dialogue Personnaliser, les onglets suivants sont disponibles   *

### Commandes

![](images/Std_DlgCustomize_tab_Commands.png ) 
*L'onglet Commandes*

Avec cet onglet, vous pouvez parcourir les commandes disponibles.

#### Parcourir les commandes 

1.  Sélectionnez une catégorie de commandes dans le panneau **Catégorie** à gauche. Certaines catégories correspondent aux entrées de menu.
2.  Les outils disponibles dans la catégorie sélectionnée sont affichés dans le panneau de droite.
3.  Survolez une commande   * son infobulle apparaît.
4.  Sélectionnez une commande   * son texte dans la barre d\'état s\'affiche sous les deux panneaux.


{{Top}}

### Clavier

![](images/Std_DlgCustomize_tab_Keyboard.png ) 
*L'onglet Clavier*

Dans cet onglet, des raccourcis clavier personnalisés peuvent être définis. Les raccourcis des macro-commandes peuvent être définis dans l\'onglet [Macros](#Macros.md).

#### Ajouter un raccourci personnalisé 

1.  Sélectionnez une catégorie de commandes dans la liste déroulante **Catégorie**.
2.  Sélectionnez une commande dans le panneau **Commandes**.
3.  La case **Raccourci actuel** affiche le raccourci actuel, si disponible.
4.  Entrez un nouveau raccourci dans la zone de saisie **Appuyez sur nouveau raccourci**. Les raccourcis peuvent comporter jusqu\'à 4 entrées. Chaque entrée est soit un seul caractère, une combinaison d\'une ou plusieurs touches spéciales ou une combinaison d\'une ou plusieurs touches spéciales et un caractère. Utilisez **Retour Arrière** pour corriger les erreurs.
5.  Si le raccourci est déjà utilisé, une boîte de dialogue vous demandera si vous souhaitez le remplacer, et la commande à laquelle le raccourci est affecté apparaîtra dans le panneau **Actuellement assigné à**.
6.  Appuyez sur le bouton **Attribuer** pour attribuer le nouveau raccourci.
7.  Appuyez sur le bouton **Effacer** pour supprimer le raccourci entré. Cela supprimera également le contenu de la boîte **Raccourci actuel**. Notez que les raccourcis par défaut ne sont pas supprimés définitivement. Ils seront restaurés au redémarrage de FreeCAD.

#### Supprimer un raccourci personnalisé 

1.  Sélectionnez une catégorie de commandes dans la liste déroulante **Catégorie**.
2.  Sélectionnez une commande dans le panneau **Commandes**.
3.  Appuyez sur le bouton **Réinitialiser**.

#### Supprimer tous les raccourcis personnalisés 

1.  Appuyez sur le bouton **Tout réinitialiser**.

#### Remarques (clavier) 

-   Les raccourcis ne fonctionnent que si leurs commandes apparaissent dans le menu standard ou dans le menu d\'un plan de travail qui a été chargé dans la session FreeCAD en cours, ou si leurs commandes apparaissent sur une barre d\'outils *visible* .

-   Dans V0.19 il y a un problème avec certaines commandes Draft. Leurs raccourcis par défaut ne fonctionnent pas et/ou des raccourcis personnalisés ne peuvent pas leur être attribués.
-   Pour réaffecter un raccourci par défaut, un nouveau raccourci doit d\'abord être affecté à sa commande d\'origine.


{{Top}}

### Ateliers

![](images/Std_DlgCustomize_tab_Workbenches.png ) 
*L'onglet Ateliers*

Dans cet onglet, la liste des [Ateliers](Std_Workbench/fr.md) peut être modifiée. La liste **Ateliers activés** affiche les Ateliers tels qu\'ils apparaîtront dans le sélecteur d\'Ateliers.

#### Désactiver un atelier 

1.  Sélectionnez un établi dans la liste des **ateliers activés**.
2.  Appuyez sur le bouton **<img src="images/Button_left.svg" width=16px>**.
3.  L\'atelier sera déplacé vers la liste des **ateliers désactivés**

#### Réactiver un atelier 

1.  Sélectionnez un établi dans la liste des **ateliers désactivés**.
2.  Appuyez sur le bouton **<img src="images/Button_right.svg" width=16px>**.
3.  L\'atelier sera déplacé vers la liste des **ateliers désactivés**.

#### Réactiver tous les ateliers 

1.  Appuyez sur le bouton **<img src="images/Button_add_all.svg" width=16px>**.

#### Modifier une position d\'un atelier 

1.  Sélectionnez un établi dans la liste des **Ateliers activés**.
2.  Appuyez sur le bouton **<img src="images/Button_up.svg" width=16px>** ou sur le bouton **<img src="images/Button_down.svg" width=16px>**.
3.  Répétez éventuellement cette opération jusqu\'à ce que l\'atelier soit à la bonne position.

#### Trier les ateliers par ordre alphabétique 

1.  Appuyez sur le bouton **<img src="images/Button_sort.svg" width=16px>**.


{{Top}}

### Barre d\'outils 

![](images/Std_DlgCustomize_tab_Toolbars.png ) 
*L'onglet Barres d'outils*

Dans cet onglet, des barres d\'outils personnalisées peuvent être créées et modifiées.

#### Sélectionnez l\'atelier 

1.  Dans la liste déroulante à droite, sélectionnez l\'atelier dont vous souhaitez modifier les barres d\'outils personnalisées. L\'option {{Value|Global}} est disponible pour les barres d\'outils personnalisées qui devraient être disponibles dans tous les ateliers.

#### Créer une barre d\'outils 

1.  Appuyez sur le bouton **Nouveau...**.
2.  Saisissez un nom dans la boîte de dialogue qui s\'ouvre.
3.  Appuyez sur le bouton **OK**.
4.  La nouvelle barre d\'outils apparaîtra dans le panneau de droite.

#### Renommer une barre d\'outils 

1.  Sélectionnez une barre d\'outils dans le panneau de droite.
2.  Appuyez sur le bouton **Renommer...**.
3.  Saisissez un nouveau nom dans la boîte de dialogue qui s\'ouvre.
4.  Appuyez sur le bouton **OK**.

#### Supprimer une barre d\'outils 

1.  Sélectionnez une barre d\'outils dans le panneau de droite.
2.  Appuyez sur le bouton **Supprimer**.

#### Désactiver une barre d\'outils 

1.  Décochez la case devant le nom de la barre d\'outils dans le panneau de droite.
2.  Une barre d\'outils désactivée sera invisible dans l\'interface FreeCAD.

#### Ajouter une commande 

1.  Il faut au moins une barre d\'outils personnalisée. Voir [Créer une barre d\'outils](#Cr.C3.A9er_une_barre_d.27outils.md).
2.  Sélectionnez la barre d\'outils appropriée dans le panneau de droite. Si aucune barre d\'outils n\'est sélectionnée, la commande sera ajoutée à la première barre d\'outils de la liste.
3.  Sélectionnez une catégorie dans la liste déroulante de gauche. Les macros commandes qui ont été configurées dans l\'onglet [Macros](#Macros.md) apparaissent dans la catégorie \'Macros\'.
4.  Sélectionnez une commande dans le panneau de gauche.
5.  Ou sélectionnez \'\' pour ajouter un séparateur (une ligne entre deux boutons de la barre d\'outils).
6.  Appuyez sur le bouton **<img src="images/Button_right.svg" width=16px>**.

#### Supprimer une commande 

1.  Si nécessaire, développez la barre d\'outils dans le panneau de droite.
2.  Sélectionnez une commande.
3.  Appuyez sur le bouton **<img src="images/Button_left.svg" width=16px>**.

#### Modifier une position de commande 

1.  Si nécessaire, développez la barre d\'outils dans le panneau de droite.
2.  Sélectionnez une commande.
3.  Appuyez sur le bouton **<img src="images/Button_up.svg" width=16px>** ou sur le bouton **<img src="images/Button_down.svg" width=16px>**.
4.  Répétez éventuellement cette opération jusqu\'à ce que la commande soit dans la bonne position.

#### Remarques (Barres d\'outils) 

-   Les barres d\'outils appartenant à l\'atelier en cours sont mises à jour immédiatement, mais après avoir désactivé/réactivé une barre d\'outils, un changement d\'atelier est requis (basculer vers un atelier puis revenir en arrière).
-   Pour mettre à jour les barres d\'outils globales, un changement d\'atelier (si des commandes ont été ajoutées ou supprimées) ou un redémarrage (si l\'ordre d\'une barre d\'outils a changé ou une barre d\'outils a été renommée) est requis.

-   Dans V0.19 il y a un problème avec certaines commandes Draft. Après les avoir ajoutés à une barre d\'outils personnalisée et quitté l\'application FreeCAD, le fichier **user.cfg** doit être modifié manuellement pour ces commandes. Recherchez le nom de la barre d\'outils personnalisée et dans cette section, changez le contenu des éléments `FCText` qui commencent par `gui_` en `DraftTools`.


{{Top}}

### Macros

![](images/Std_DlgCustomize_tab_Macros.png ) 
*L'onglet Macros*

Avec cet onglet, les commandes de macro utilisateur peuvent être configurées. Une fois configurés, ils peuvent être ajoutés à des barres d\'outils personnalisées. FreeCAD utilise un dossier dédié pour les macros dutilisateurs et seules les macros de ce dossier peuvent être configurées. Utilisez la commande <img alt="" src=images/Std_DlgMacroExecute.svg  style="width   *16px;"> [Std Lancer la macro](Std_DlgMacroExecute/fr.md) pour rechercher ce dossier sur votre système.

Si vous téléchargez une macro avec le <img alt="" src=images/Std_AddonMgr.svg  style="width   *16px;"> [Gestionnaire d\'extensions](Std_AddonMgr/fr.md), assurez-vous de télécharger également son fichier image d\'icône. La plupart des macros ont un lien d\'image sur la page d\'informations qui apparaît dans le gestionnaire d\'extensions. Vous pouvez par exemple placer ce fichier image dans le dossier des macros utilisateur.

Si vous souhaitez utiliser une macro téléchargée à partir d\'une autre source, vous devrez l\'installer manuellement. Voir [Comment installer les macros](How_to_install_macros/fr.md) pour plus d\'informations.

#### Ajouter une commande macro 

1.  Dans la liste déroulante **Macro**, sélectionnez une macro.
2.  Saisissez un **Texte de menu**. Ce sera le nom utilisé pour identifier la macro-commande et apparaîtra également dans la barre d\'outils s\'il n\'y a pas d\'icône.
3.  Vous pouvez également saisir une **Infobulle**. Ce texte apparaîtra près de l\'emplacement de la souris lorsque vous survolez l\'icône de la barre d\'outils.
4.  Vous pouvez également saisir un **Texte d\'état**. Ce texte apparaîtra dans la [barre d\'état](Status_bar/fr.md) lorsque vous survolez l\'icône de la barre d\'outils.
5.  Facultativement, entrez la page wiki de la macro, si elle est disponible, dans la zone de saisie **Qu\'est-ce que c\'est**. Saisissez le nom de la page, pas l\'URL complète.
6.  Vous pouvez également saisir un raccourci dans la zone de saisie **Accélérateur**. Voir [Clavier](#Clavier.md) pour plus d\'informations.
7.  Pour ajouter une icône   *
    1.  Appuyez sur le bouton **Pixmap** **...**.
    2.  La boîte de dialogue Choisir une icône s\'ouvre.
    3.  Si nécessaire, appuyez sur le bouton **Dossiers d'icônes...** pour ajouter un dossier d\'icônes.
    4.  Sélectionnez une icône dans le panneau. La boîte de dialogue Choisir une icône se ferme automatiquement.
8.  Appuyez sur le bouton **Ajouter**.
9.  La macro-commande apparaît dans le panneau de gauche.
10. La macro-commande peut maintenant être sélectionnée dans l\'onglet [Barre d\'outils](#Barre_d'outils.md).

#### Supprimer une commande macro 

1.  Sélectionnez une commande macro dans le panneau de gauche.
2.  Appuyez sur le bouton **Supprimer**.

#### Modifier une commande macro 

1.  Double-cliquez sur la commande macro dans le panneau de gauche.
2.  Apportez les modifications requises. Notez que vous ne pouvez pas supprimer l\'icône, vous pouvez uniquement la remplacer.
3.  Appuyez sur le bouton **Remplacer**.


{{Top}}

### Mouvement de la Spaceball 

Cet onglet est vide si aucune souris 3D n\'est détecté. Voir   * [Périphériques d\'entrée de connexion 3D](3Dconnexion_input_devices/fr.md). {{Top}}

### Boutons de la souris 3D 

Cet onglet est vide si aucune souris 3D n\'est détecté. Voir   * [Périphériques d\'entrée de connexion 3D](3Dconnexion_input_devices/fr.md). {{Top}}

## Thèmes

FreeCAD prend en charge la thématisation complète de l\'interface, via des feuilles de style .qss. Le [format qss](https   *//doc.qt.io/qt-5/stylesheet-syntax.html) est très similaire au [format css](https   *//en.wikipedia.org/wiki/CSS) utilisé dans les pages Web. Il ajoute essentiellement plus de méthodes pour référencer les différents widgets et éléments de l\'interface Qt. Vous pouvez modifier le thème par défaut (qui reprend simplement le style défini par votre système de bureau) en sélectionnant une **feuille de style** dans les [Préférences FreeCAD](Preferences_Editor/fr#G.C3.A9n.C3.A9ral.md).

Vous pouvez également créer votre propre thème si vous n\'êtes pas satisfait des thèmes fournis avec FreeCAD, par exemple en modifiant une [feuille de style existante](https   *//github.com/FreeCAD/FreeCAD/tree/master/src/Gui/Stylesheets). Votre nouveau style doit être placé dans un dossier spécifique pour qu\'il soit trouvé par FreeCAD    *

-    **%APPDATA%/FreeCAD/Gui/Stylesheets**(sous Windows). Le dossier **%APPDATA%** peut être retrouvé en entrant {{Incode|App.getUserAppDataDir()}} dans la [console Python](Python_console/fr.md).

-    **$HOME/.FreeCAD/Gui/Stylesheets**(sous Linux).

-    **$HOME/Library/Preferences/FreeCAD/Gui/Stylesheets**(sous MacOS).


{{Top}}

## Addons

Les modules complémentaires offrent une autre façon de personnaliser l\'interface d\'utilisation. Vous trouverez ci-dessous quelques addons créés par les utilisateurs de la communauté FreeCAD. Ils peuvent être téléchargés via le <img alt="" src=images/Std_AddonMgr.svg  style="width   *16px;"> [gestionnaire d\'Addons](Std_AddonMgr/fr.md) (remarque   * ils sont répertoriés dans l\'onglet Ateliers).

### Menu Cube 

-   Dépôt Github   * <https   *//github.com/triplus/CubeMenu>

### Transparence

-   Dépôt Github   * <https   *//github.com/triplus/Glass>.

### Thèmes des icônes 

-   Dépôt Github   * <https   *//github.com/triplus/IconThemes>

### Lanceur

-   Dépôt Github   * <https   *//github.com/triplus/Launcher>

### Menu Camembert 

-   Dépôt Github   * <https   *//github.com/triplus/PieMenu>

### RemBench

-   Dépôt Github   * <https   *//github.com/triplus/RemBench>

### Raccourci

-   Dépôt Github   * <https   *//github.com/triplus/ShortCuts>


{{Top}}





{{Std Base navi

}} {{Interface navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Interface Customization/fr
