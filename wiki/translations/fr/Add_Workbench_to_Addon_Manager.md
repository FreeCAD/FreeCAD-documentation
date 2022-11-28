# Add Workbench to Addon Manager/fr
{{TOCright}}

## Introduction

Ces instructions expliquent, étape par étape, comment ajouter un atelier Python au [Gestionnaire des extensions](Std_AddonMgr/fr.md).

Conditions requises    *

-   Un dépôt git local.
-   Un dépôt git distant. Les hôtes git pris en charge sont [GitHub](https   *//github.com), [GitLab](https   *//about.gitlab.com/), [Framagit](https   *//framagit.org/public/projects) et [Debian Salsa](https   *//salsa.debian.org/public).
-   Git doit être installé.

## Activer le mode développeur 

1.  Ouvrez l\'[Éditeur de préférences](Preferences_Editor/fr.md)    * sélectionnez l\'option **Édition → <img src="images/Std_DlgPreferences.svg" width=16px> Préférences...** dans le menu.
2.  Sélectionnez l\'option **<img src="images/Std_AddonMgr.svg" width=16px> Gestionnaire des extensions** dans la barre de gauche.
3.  Dans l\'onglet **Options du gestionnaire des extensions**, cochez la case **Activer le mode développeur des extensions**. Cela activera le bouton **Outils du développeur...** dans le gestionnaire des extensions.
4.  Appuyez sur le bouton **OK** pour fermer l\'éditeur de préférences.

## Créer le fichier package.xml 

1.  Ouvrez le [Gestionnaire des extensions](Std_AddonMgr/fr.md)    * sélectionnez l\'option **Outils → <img src="images/Std_AddonMgr.svg" width=16px> Gestionnaire des extensions** dans le menu.
2.  Appuyez sur le bouton **Outils du développeur...**.
3.  La boîte de dialogue **Outils pour le développeur d'extensions** s\'ouvre.
    <img alt="" src=images/Addon_Manager_Addon_Developer_Tools_Dialog.png  style="width   *350px;">
4.  Saisissez les éléments suivants    *
    -   
        **Chemin vers l'extension**
        
           * chemin vers le dépôt git local.

    -   
        **Nom de l’extension**
        
           * ce nom apparaîtra dans les listes du gestionnaire des extensions.

    -   
        **Description**
        
           * idem.

    -   
        **Version**
        
           * idem.

    -   
        **URL du dépôt**
        
           * idem.

    -   
        **Branche principale**
        
           * idem.

    -   
        **URL du README**
        
           * recommandé.

    -   
        **Icône**
        
           * l\'icône doit faire partie du dépôt.
5.  Appuyez sur le bouton **<img src="images/List-add.svg" width=16px>** au bas de la boîte de dialogue.
6.  La boîte de dialogue **Élément de contenu** s\'ouvre.
    <img alt="" src=images/Addon_Manager_Content_Item_Dialog.png  style="width   *350px;">
7.  Le **Type de contenu** doit être défini sur {{Value|Atelier}}.
8.  Cochez la case **C'est le seul élément de l'extension**.
9.  Saisissez le nom de la classe **Atelier**. Il s\'agit du nom de classe spécifié dans le fichier **InitGui.py**.
10. Pour le **Sous-répertoire**, entrez {{Value|./}}.
11. Appuyez sur le bouton **OK** pour fermer le dialogue.
12. Appuyez sur le bouton **Enregistrer** pour fermer la boîte de dialogue **Outils pour le développeur d'extensions** et enregistrer le fichier **package.xml**.
13. Appuyez sur le bouton **<img src="images/Process-stop.svg" width=16px> Fermer** pour fermer le gestionnaire des extensions.
14. Poussez le fichier créé vers votre dépôt distant.

## Ajouter l\'atelier au fichier .gitmodules 

1.  Faites un fork <https   *//github.com/FreeCAD/FreeCAD-addons>.
2.  Créez une nouvelle branche.
3.  Modifiez le fichier **.gitmodules** pour inclure votre nouvelle extension, par ordre alphabétique.
4.  Poussez la nouvelle branche vers GitHub.
5.  Soumettez une Pull Request au dépôt FreeCAD-Addons avec le nouveau fichier **.gitmodules**.

## Voir aussi 

-   [Création d\'atelier](Workbench_creation/fr.md)
-   [Métadonnées du package](Package_Metadata.md)    * informations détaillées sur le fichier **package.xml**.

[Category   *Addons](Category_Addons.md) [Category   *Developer Documentation](Category_Developer_Documentation.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > [Developer Documentation](Category_Developer Documentation.md) > Add Workbench to Addon Manager/fr
