---
- GuiCommand:/fr
   Name:Path ToolBitLibraryOpen
   Name/fr:Path Gestionnaire d'outils
   MenuLocation:Path → ToolBit Library editor
   Workbenches:[Path](Path_Workbench/fr.md)
   Version:0.19
   SeeAlso:[Path Sélecteur d'outil](Path_ToolBitDock/fr.md), [Path Outils](Path_Tools/fr.md), [Path ToolBit](Path_ToolBit/fr.md)
---

## Description

Le **<img src="images/Path_ToolBitLibraryOpen.svg" width=16px> [Tool xxxxx](Path_ToolBitLibraryOpen.md)
**

![](images/Toolbitmanager.png )

Le gestionnaire de bibliothèque (illustré ci-dessus) est la boîte de dialogue permettant de créer, de gérer et d\'organiser les boîtes à outils. En lançant le gestionnaire de bibliothèque à partir du menu Chemin ou du bouton \'gestionnaire\' dans le dock, le gestionnaire s\'affiche sous forme de boîte de dialogue modale.

A partir de là, l\'utilisateur peut effectuer toutes les tâches liées à la gestion du toolbit :

-   Sélection d\'une bibliothèque par défaut.
-   Créer/modifier/supprimer des boîtes à outils.
-   Créer des bibliothèques.
-   Modifier les bibliothèques en ajoutant et en supprimant des boîtes à outils.
-   Sauvegarder une bibliothèque sous un nouveau nom.
-   Exporter une bibliothèque au format de table d\'outils LinuxCNC (.tbl).

Seule la création de nouvelles formes d\'outils ne peut être effectuée à partir du gestionnaire de bibliothèque de toolbits. Il s\'agit d\'un sujet avancé. (voir [Path Création de formes d\'outils](Path_ToolShape/fr.md))

Le volet à gauche (1) affiche une liste de toutes les bibliothèques du répertoire de travail en cours. La bibliothèque en cours est mise en évidence.

Le chemin du répertoire de travail en cours est affiché dans la barre de titre de la fenêtre (2). Un sélecteur de fichiers (3) peut être utilisé pour sélectionner un autre répertoire de travail.

Le volet de droite (4) montre tous les toolbits de la bibliothèque sélectionnée. En double-cliquant dans la colonne de gauche, vous pouvez modifier le numéro d\'outil par défaut pour ce toolbit. Le numéro d\'outil sera utilisé lors de la création d\'un contrôleur d\'outil. Le numéro est un attribut de la bibliothèque. Cela signifie que le même toolbit peut exister dans plusieurs bibliothèques d\'outils et avoir des numéros d\'outils par défaut différents dans chacune d\'elles.

Les outils situés en haut (5) sont utilisés pour créer/additionner/supprimer des toolbits de la bibliothèque actuelle.

Le bouton Enregistrer sous (6) permet d\'écrire la bibliothèque dans un nouveau fichier ou de l\'exporter vers un format de table d\'outils valide. Actuellement, seul le format LinuxCNC est supporté.

Le gestionnaire se souviendra de la dernière bibliothèque d\'outils active et du dernier répertoire de travail entre deux utilisations.

Le bouton de fermeture (7) en bas à droite permet de quitter le gestionnaire de bibliothèque d\'outils. Toutes les modifications apportées à la bibliothèque en cours sont conservées sur le disque. Si vous appuyez sur la touche Echap, le gestionnaire est désactivé mais aucune modification n\'est apportée à la bibliothèque en cours. La bibliothèque sélectionnée lors de la fermeture du gestionnaire deviendra la nouvelle bibliothèque par défaut et sera affichée dans la fenêtre des Toolbits.

## Utilisation

### Gestion des outils 

1.  Il existe plusieurs façons d\'ouvrir le gestionnaire de bibliothèque de Toolbits :
    -   Sélectionnez l\'option **Path → <img src="images/Path_ToolBitLibraryOpen.svg" width=16px> Éditeur de bibliothèque ToolBit** dans le menu.
    -   Ouvrez le dock Toolbit comme décrit ci-dessus et appuyez sur le bouton **<img src="images/Path_ToolBitLibraryOpen.svg" width=16px>** pour ouvrir le gestionnaire de bibliothèque.
2.  Sélectionnez une bibliothèque dans la liste.
3.  Créez/Ajoutez/Supprimez des toolbits de la bibliothèque.
4.  Double-cliquez sur une ligne pour éditer le toolbit.
5.  Fermez le gestionnaire.
6.  La bibliothèque sélectionnée devient la bibliothèque par défaut du dock.

## Modification des Toolbits 

Il existe plusieurs façons d\'éditer les toolbits et la bibliothèque :

A. En cliquant sur les en-têtes de colonne de la bibliothèque, vous pouvez trier la bibliothèque des toolbits. La bibliothèque conservera le tri et l\'utilisera dans le dock.

:   ![](images/Librarysort.png )
:   
    *Tri de la bibliothèque toolbit via les en-têtes de colonne*
    

B. En double-cliquant dans la première colonne, vous pouvez modifier le numéro du toolbit. Ce sera le numéro d\'outil par défaut utilisé lors de la création d\'un nouveau contrôleur d\'outils. Il est possible d\'utiliser le même numéro pour plusieurs toolbits.

:   ![](images/Edittoolnumber.png )
:   
    *Double-cliquez sur la première colonne pour modifier le numéro d'outil*.

C. Double-cliquez n\'importe où ailleurs dans la ligne pour ouvrir le panneau d\'édition du toolbit. A partir de là, vous pouvez modifier d\'autres propriétés du toolbit.

:   ![](images/Editingpanel.png )
:   : *Ouverture du panneau d'édition du toolbit en cliquant n'importe où ailleurs dans la rangée.*

## En relation 

-   [Path Outils](Path_Tools/fr.md)
-   [Path ToolBit](Path_ToolBit/fr.md)





{{Path_Tools_navi

}} 
