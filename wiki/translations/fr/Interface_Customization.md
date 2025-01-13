# Interface Customization/fr
## Introduction

L\'interface FreeCAD est basée sur la boîte à outils [Qt](https://fr.wikipedia.org/wiki/Qt) et possède une bonne organisation. Certains aspects de l\'interface peuvent être personnalisés. Vous pouvez, par exemple, ajouter des barres d\'outils personnalisées avec des outils de plusieurs ateliers ou des outils définis dans des macros et vous pouvez créer vos propres raccourcis clavier. Mais les menus et barres d\'outils par défaut fournis avec FreeCAD et ses ateliers ne peuvent pas être modifiés.

![](images/Std_DlgCustomize_tab_Toolbars.png ) 
*La boite de dialogue de personnalisation de l'interface*



## Utilisation

1.  Les commandes disponibles dans la boite de dialogue de personnalisation d\'interface dépendent des ateliers qui ont été chargés dans la session FreeCAD en cours. Vous devez donc d\'abord charger tous les établis dont vous souhaitez avoir accès aux commandes.
2.  Il existe plusieurs façons de lancer la commande <img alt="" src=images/Std_DlgCustomize.svg  style="width:16px;"> [Std Personnaliser](Std_DlgCustomize/fr.md) :
    -   Sélectionnez l\'option **Outils → <img src="images/Std_DlgCustomize.svg" width=16px> Personnaliser...** du menu.
    -   Cliquez avec le bouton droit sur une zone de barre d\'outils et choisissez **<img src="images/Std_DlgCustomize.svg" width=16px> Personnaliser...** dans le menu contextuel.
3.  La boîte de dialogue **Personnaliser** s\'ouvre. Pour plus d\'informations, voir [Options](#Options.md).
4.  Le bouton **Aide** ne fonctionne pas pour le moment.
5.  Appuyez sur le bouton **Fermer** pour fermer la boîte de dialogue.



## Options

Dans la fenêtre de dialogue Personnaliser, les onglets suivants sont disponibles :



### Clavier

![](images/Std_DlgCustomize_tab_Keyboard.png ) 
*L'onglet Clavier*

Dans cet onglet, des raccourcis clavier personnalisés peuvent être définis. Les raccourcis des macro-commandes peuvent être définis dans l\'onglet [Macros](#Macros.md).



#### Recherche

Vous pouvez rechercher des commandes en saisissant au moins 3 caractères de leur texte de menu ou de leur nom dans le champ de recherche. La recherche est insensible à la casse.

Il est également possible de rechercher des raccourcis :

-   Dans le champ de recherche, les touches spéciales des raccourcis doivent être saisies sous forme de chaînes. Par exemple, pour rechercher des commandes qui utilisent **Ctrl** dans leur raccourci, entrez {{Value|ctrl}} (4 lettres).
-   Ajoutez des parenthèses pour rechercher des raccourcis à un seul caractère, par exemple : {{Value|(c)}}.
-   Ajoutez une virgule et un espace entre les caractères des raccourcis multi-caractères, par exemple : {{Value|g, b, b}}.



#### Ajouter un raccourci 

1.  Sélectionnez une catégorie de commande dans la liste déroulante **Catégorie**.
2.  Sélectionnez une commande dans le panneau **Commandes**.
    -   Cliquez sur les en-têtes de colonne {{Value|Commande}}, {{Value|Raccourci}} ou {{Value|Défaut}} pour réorganiser la liste.
    -   Vous pouvez également faire glisser le séparateur à droite du panneau pour le redimensionner.
3.  La case **Raccourci actuel** affiche le raccourci actuel, s\'il est disponible.
4.  Entrez un nouveau raccourci dans la zone de saisie **Nouveau raccourci**. Les raccourcis peuvent comporter jusqu\'à 4 entrées. Chaque entrée est soit un caractère unique, soit une combinaison d\'une ou plusieurs touches spéciales, soit une combinaison d\'une ou plusieurs touches spéciales et d\'un caractère. Utilisez **Retour** pour corriger les erreurs.
5.  Les autres commandes actives (voir [Remarques](#Remarques.md)) qui utilisent déjà le raccourci seront listées dans la **Liste de priorité des raccourcis**.
6.  Appuyez sur le bouton **Attribuer** pour attribuer le nouveau raccourci.
7.  Si la **Liste de priorité des raccourcis** contient plus d\'une commande, vous pouvez modifier son ordre en sélectionnant les commandes individuelles et en appuyant sur le bouton **Haut** ou sur le bouton **Bas**. Si des commandes actives partagent le même raccourci, le raccourci déclenchera celle qui est la plus haute dans la liste.



#### Supprimer un raccourci 

1.  Sélectionnez une catégorie de commande dans la liste déroulante **Catégorie**.
2.  Sélectionnez une commande dans le panneau **Commandes**.
3.  Appuyez sur le bouton **Clear**.



#### Restaurer un raccourci par défaut 

1.  Sélectionnez une catégorie de commandes dans la liste déroulante **Catégorie**.
2.  Sélectionnez une commande dans le panneau **Commandes**.
3.  Appuyez sur le bouton **Réinitialiser**.



#### Restaurer tous les raccourcis par défaut 

1.  Appuyez sur le bouton **Tout réinitialiser**.



#### Remarques

-   Les raccourcis ne fonctionnent que pour les commandes actives. Les commandes actives sont des commandes qui apparaissent dans le menu standard, ou dans le menu de l\'atelier actif, ou des commandes qui apparaissent dans une barre d\'outils \"visible\".


{{Top}}



### Barre d\'outils 

![](images/Std_DlgCustomize_tab_Toolbars.png ) 
*L'onglet Barres d'outils*

Dans cet onglet, des barres d\'outils personnalisées peuvent être créées et modifiées.



#### Recherche 

Voir [Clavier](#Recherche.md).



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
3.  Sélectionnez une catégorie de commande dans la liste déroulante **Catégorie**. Les macro-commandes qui ont été configurées dans l\'onglet [Macros](#Macros.md) apparaissent dans la catégorie {{Value|Macros}}.
4.  Sélectionnez une commande dans le panneau **Commandes** ou sélectionnez {{Value|<Séparateur>}} pour ajouter un séparateur (une ligne entre deux boutons de la barre d\'outils).
    -   Vous pouvez également faire glisser le séparateur à droite du panneau pour le redimensionner.
5.  Appuyez sur le bouton **<img src="images/Button_right.svg" width=16px>**.



#### Supprimer une commande 

1.  Si nécessaire, développez la barre d\'outils dans le panneau de droite.
2.  Sélectionnez une commande.
3.  Appuyez sur le bouton **<img src="images/Button_left.svg" width=16px>**.



#### Modifier une position de commande 

1.  Si nécessaire, développez la barre d\'outils dans le panneau de droite.
2.  Sélectionnez une commande.
3.  Appuyez sur le bouton **<img src="images/Button_up.svg" width=16px>** ou sur le bouton **<img src="images/Button_down.svg" width=16px>**.
4.  Répétez éventuellement cette opération jusqu\'à ce que la commande soit dans la bonne position.



#### Remarques 

-   Les barres d\'outils appartenant à l\'atelier en cours sont mises à jour immédiatement, mais après avoir désactivé/réactivé une barre d\'outils, un changement d\'atelier est requis (basculer vers un atelier puis revenir en arrière).
-   Pour mettre à jour les barres d\'outils globales, un changement d\'atelier (si des commandes ont été ajoutées ou supprimées) ou un redémarrage (si l\'ordre d\'une barre d\'outils a changé ou une barre d\'outils a été renommée) est requis.


{{Top}}

### Macros

![](images/Std_DlgCustomize_tab_Macros.png ) 
*L'onglet Macros*

Cet onglet permet de définir des commandes de macro. Une fois configurées, elles peuvent être ajoutées à des barres d\'outils personnalisées. Les macros installées avec le <img alt="" src=images/Std_AddonMgr.svg  style="width:16px;"> [gestionnaire des extensions](Std_AddonMgr/fr.md) sont configurées automatiquement et ajoutées à une barre d\'outils {{Value|Globale}} (voir [Barre d\'outils](#Barre_d'outils.md)), si vous confirmez le popup **Ajouter un bouton** pendant le processus d\'installation.

Si vous souhaitez utiliser une macro téléchargée à partir d\'une autre source, vous devrez l\'installer manuellement. Voir [Comment installer des macros](How_to_install_macros/fr.md) pour plus d\'informations. Notez que FreeCAD utilise un dossier dédié aux macros et que seules les macros de ce dossier peuvent être configurées. Utilisez la <img alt="" src=images/Std_DlgMacroExecute.svg  style="width:16px;"> [Std Exécuter une macro](Std_DlgMacroExecute/fr.md) pour trouver ce dossier sur votre système.



#### Ajouter une commande macro 

1.  Dans la liste déroulante **Macro**, sélectionnez une macro.
2.  Saisissez un **Texte du menu**. Ce sera le nom utilisé pour identifier la macro-commande et apparaîtra également dans la barre d\'outils s\'il n\'y a pas d\'icône.
3.  Vous pouvez également saisir une **Infobulle**. Ce texte apparaîtra près de l\'emplacement de la souris lorsque vous survolez l\'icône de la barre d\'outils.
4.  Vous pouvez également saisir un **Texte d\'état**. Ce texte apparaîtra dans la [barre d\'état](Status_bar/fr.md) lorsque vous survolez l\'icône de la barre d\'outils.
5.  Vous pouvez entrer la page wiki de la macro, si elle est disponible, dans la zone de saisie **Qu\'est-ce que c\'est**. Saisissez le nom de la page, pas l\'URL complète.
6.  Vous pouvez également saisir un raccourci dans la zone de saisie **Créer un raccourci**. Voir [Clavier](#Clavier.md) pour plus d\'informations.
7.  Pour ajouter une icône :
    1.  Appuyez sur le bouton **Icône** **...**.
    2.  La fenêtre de dialogue **Choisir une icône** s\'ouvre.
    3.  Si nécessaire, appuyez sur le bouton **Dossiers d'icônes...** pour ajouter un dossier d\'icônes.
    4.  Sélectionnez une icône dans le panneau. La fenêtre de dialogue **Choisir une icône** se ferme automatiquement.
8.  Appuyez sur le bouton **Ajouter**.
9.  La commande de la macro apparaît dans le panneau de gauche.
10. La commande de la macro peut maintenant être sélectionnée dans l\'onglet [Barre d\'outils](#Barre_d'outils.md).



#### Supprimer une commande de macro 

1.  Sélectionnez la commande de la macro dans le panneau de gauche.
2.  Appuyez sur le bouton **Supprimer**.



#### Modifier une commande de macro 

1.  Double-cliquez sur la commande de la macro dans le panneau de gauche.
2.  Apportez les modifications requises. Notez que vous ne pouvez pas supprimer l\'icône, vous pouvez uniquement la remplacer.
3.  Appuyez sur le bouton **Remplacer**.


{{Top}}



### Mouvement de la Spaceball 

Cet onglet est vide si aucune souris 3D n\'est détecté. Voir : [Périphériques d\'entrée de connexion 3D](3Dconnexion_input_devices/fr.md). 

### Boutons de la souris 3D 

Cet onglet est vide si aucune souris 3D n\'est détecté. Voir : [Périphériques d\'entrée de connexion 3D](3Dconnexion_input_devices/fr.md). 

## Thèmes

FreeCAD prend en charge la thématisation complète de l\'interface, via des feuilles de style .qss. Le [format qss](https://doc.qt.io/qt-5/stylesheet-syntax.html) est très similaire au [format css](https://en.wikipedia.org/wiki/CSS) utilisé dans les pages Web. Il ajoute essentiellement plus de méthodes pour référencer les différents widgets et éléments de l\'interface Qt. Vous pouvez modifier le thème par défaut (qui reprend simplement le style défini par votre système de bureau) en sélectionnant une **feuille de style** dans les [Préférences FreeCAD](Preferences_Editor/fr#G.C3.A9n.C3.A9ral.md).

Vous pouvez également créer votre propre thème si vous n\'êtes pas satisfait des thèmes fournis avec FreeCAD, par exemple en modifiant une [feuille de style existante](https://github.com/FreeCAD/FreeCAD/tree/master/src/Gui/Stylesheets). Votre nouveau style doit être placé dans un dossier spécifique pour qu\'il soit trouvé par FreeCAD :

-    **%APPDATA%/FreeCAD/Gui/Stylesheets**(sous Windows). Le dossier **%APPDATA%** peut être retrouvé en entrant {{Incode|App.getUserAppDataDir()}} dans la [console Python](Python_console/fr.md).

-    **$HOME/.FreeCAD/Gui/Stylesheets**(sous Linux).

-    **$HOME/Library/Application Support/FreeCAD/Gui/Stylesheets**(sous macOS).


{{Top}}



## Extensions

Les extensions du <img alt="" src=images/Std_AddonMgr.svg  style="width:16px;"> [gestionnaire des extensions](Std_AddonMgr/fr.md) offrent un autre moyen de personnaliser l\'interface utilisateur. Plusieurs [ateliers externes](External_workbenches/fr.md) et [kits de preférences](Preference_Packs/fr.md) sont disponibles. {{Top}}





{{Std Base navi

}} {{Interface navi}}



---
⏵ [documentation index](../README.md) > Interface Customization/fr
