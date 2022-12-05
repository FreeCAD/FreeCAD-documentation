---
- GuiCommand:/fr
   Name:Path ToolLibraryEdit
   Name/fr:Path Gestionnaire du magasin d'outils
   MenuLocation:Path → Tool Manager
   Workbenches:[Path](Path_Workbench/fr.md)
   Shortcut:**P** **T**
   SeeAlso:
---

# Path ToolLibraryEdit/fr

## Description

Le **<img src="images/Path_ToolLibraryEdit.svg" width=16px> [gestionnaire du magasin d'outils](Path_ToolLibraryEdit/fr.md)** permet d\'éditer les différents outils de la collection contenue dans l\'objet machine d\'une **<img src="images/Path_Job.svg" width=16px> [Tâche](Path_Job/fr.md)**. Ce magasin d\'outils est utilisé par les différentes opérations contenues dans le projet pour obtenir les informations nécessaires sur l\'outil actuel.

Il sert également à la sélection d\'un outil que vous souhaitez utiliser dans votre travail.

![](images/Path-Tooltable.png )

La manipulation est simple:

-   Import\...: importe une collection d\'outils à partir d\'un fichier XML. {{Note|Warning|Ceci est actuellement en partie cassé et ne fonctionne pas si vous n'avez jamais eu de fichier xml auparavant.}}
-   Export\...: exporte la collection vers un fichier XML.
-   New Tool: ouvre une boîte de dialogue dans laquelle vous pouvez entrer les paramètres de votre outil.
-   Delete: supprime les lignes actuellement sélectionnées. {{Note|Avertissement|Les outils sont supprimés de votre collection même si vous annulez la boîte de dialogue}}
-   Move up: vous ne pouvez pas modifier le numéro d\'outil, vous pouvez déplacer la ligne sélectionnée pour diminuer son numéro d\'outil
-   Move down: vous pouvez déplacer la ligne sélectionnée vers le bas pour augmenter son numéro d\'outil

-   Crée un ou des contrôleurs d\'outils: Si vous cochez une ou plusieurs cases à gauche de la liste d\'outils, ce bouton devient actif. Si vous cliquez dessus, les outils sélectionnés seront insérés dans votre travail actuel.

## Utilisation

1.  Sélectionnez un **<img src="images/Path_Job.svg" width=16px> [Path Tâche](Path_Job/fr.md)
**
2.  Lancez le gestionnaire d\'outils en utilisant plusieurs méthodes :
    -   Appuyez sur le bouton **<img src="images/Path_ToolLibraryEdit.svg" width=16px> [Tool Manager](Path_ToolLibraryEdit/fr.md)** dans la barre d\'outils.
    -   En utilisant le raccourci clavier **P** puis **T**.
    -   En utilisant l\'entrée **Path → Tool Manager** du menu supérieur.
3.  Créez de nouveaux outils ou ajustez les propriétés des outils existants.
    Définissez au moins le diamètre, FreeCAD en a besoin pour calculer la compensation de rayon. Depuis {{VersionPlus/fr|0.17}}, c\'est la seule valeur utilisée pour la création de parcours d\'usinage. Cependant, si vous souhaitez utiliser l\'outil de simulation plus tard, ajoutez également l\'angle de coupe et la hauteur du tranchant.
    ![](images/Path-ToolAdd.gif )

## Options

-   Les outils peuvent être réorganisés en utilisant les boutons de déplacement vers le haut / vers le bas
-   Des tables à outils complètes peuvent être importées à partir de fichiers XML (format de table à outils propre à FreeCAD) ou de tables à outils HeeksCAD





{{Path_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path ToolLibraryEdit/fr
