---
 GuiCommand:
   Name: Draft SetStyle
   Name/fr: Draft Définir le style
   MenuLocation: Utilitaires , Définir le style
   Workbenches: Draft_Workbench/fr, BIM_Workbench/fr
   Shortcut: Draft : **S** **S**
   Version: 0.19
   SeeAlso: Draft_AnnotationStyleEditor/fr, Draft_ApplyStyle/fr
---

# Draft SetStyle/fr

## Description

La commande <img alt="" src=images/Draft_SetStyle.svg  style="width:24px;"> **Draft Définir le style** définit le style par défaut des nouveaux objets.

<img alt="" src=images/Draft_SetStyle_Taskpanel_Tab_Shape.png  style="width:" height="500px;"> <img alt="" src=images/Draft_SetStyle_Taskpanel_Tab_Annotation.png  style="width:" height="500px;"> 
*Les deux onglets du panneau de tâches des paramètres de style ({{Version/fr|1.0*)}}



## Utilisation

1.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton ![](images/Draft_tray_button_style.png ) de la [Draft Barre](Draft_Tray/fr.md). En fonction des paramètres de style en cours, ce bouton peut avoir un aspect différent.
    -   [Draft](Draft_Workbench/fr.md): sélectionnez l\'option **Utilitaires → <img src="images/Draft_SetStyle.svg" width=16px> Définir le style** du menu ou dans le menu contextuel de la [vue en arborescence](Tree_view/fr.md) ou de la [vue 3D](3D_view/fr.md).
    -   Draft : utilisez le raccourci clavier : **S** puis **S**.
2.  Le panneau de tâches **Paramètres de style** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
3.  Modifiez éventuellement un ou plusieurs paramètres.
4.  Appuyez sur le bouton **OK** pour enregistrer les paramètres.
5.  Le bouton de [Draft La barre](Draft_Tray/fr.md) est mis à jour.

## Options

-   Dans la liste déroulante située en haut du panneau des tâches, il est possible de sélectionner un préréglage de style existant.
-   Cliquez sur le bouton **<img src="images/Document-save.svg" width=16px>** pour enregistrer les paramètres de style en cours en tant que préréglage.
-   Dans l\'onglet **Forme**, les paramètres suivants peuvent être spécifiés :
    -   
        **Apparence des formes**
        
        -   
            **Couleur des formes**
            
            .

        -   
            **Couleur autour des formes**
            
            . {{Version/fr|1.0}}

        -   
            **Couleur émissive des formes**
            
            . {{Version/fr|1.0}}

        -   
            **Couleur spéculaire des formes**
            
            . {{Version/fr|1.0}}

        -   
            **Transparence des formes**
            
            .

        -   
            **Brillance des formes**
            
            . {{Version/fr|1.0}}

    -   
        **Autre**
        
        -   
            **Couleur des lignes**
            
            .

        -   
            **Largeur des lignes**
            
            .

        -   
            **Couleur des points**
            
            . {{Version/fr|1.0}}

        -   
            **Taille des points**
            
            . {{Version/fr|1.0}}

        -   
            **Style de trait**
            
            .

        -   
            **Mode d'affichage**
            
            .
-   Les paramètres de l\'onglet **Annotation** s\'appliquent à [Draft Textes](Draft_Text/fr.md), [Draft Dimensions](Draft_Dimension/fr.md) et [Draft Étiquettes](Draft_Label/fr.md). Les paramètres suivants peuvent être spécifiés (voir [Draft Texte](Draft_Text/fr#Vue.md) et [Draft Dimension](Draft_Dimension/fr#Vue.md) pour plus de détails) :
    -   
        **Textes**
        
        -   
            **Nom de la police**
            
            .

        -   
            **Taille de la police**
            
            . Il s\'agit en fait de la hauteur de ligne par défaut, les lettres sont plus petites.

        -   
            **Espace interlignes**
            
            . Non utilisé pour les dimensions.

        -   
            **Multiplicateur d'échelle**
            
            . C\'est l\'inverse de l\'échelle définie dans le [Widget d\'échelle d\'annotation](Draft_annotation_scale_widget/fr.md). Si l\'échelle est {{value|1:100}}, le multiplicateur est {{value|100}}. {{Version/fr|1.0}}

        -   
            **Couleur des textes**
            
            .

    -   
        **Lignes et flèches**
        
        -   
            **Largeur des lignes**
            
            . {{Version/fr|1.0}}

        -   
            **Type des flèches**
            
            .

        -   
            **Taille des flèches**
            
            .

        -   
            **Couleur des lignes et flèches**
            
            . {{Version/fr|1.0}}

    -   
        **Dimensions**
        
        -   
            **Afficher l'unité**
            
            .

        -   
            **Substitution d’unité**
            
            .

        -   
            **Dépassement des lignes de dimension**
            
            . {{Version/fr|0.21}}

        -   
            **Longueur des lignes d'extension**
            
            . {{Version/fr|0.21}}

        -   
            **Dépassement des lignes d'extension**
            
            . {{Version/fr|0.21}}

        -   
            **Espacement du texte**
            
            .
-   Appuyez sur le bouton **<img src="images/Draft_SetStyle.svg" width=16px> Sélectionné** pour appliquer les paramètres aux objets ou groupes sélectionnés. Les objets peuvent être sélectionnés lorsque le panneau des tâches est ouvert.
-   Cliquez sur le bouton **<img src="images/Draft_Text.svg" width=16px> Annotations** pour appliquer les paramètres aux [Draft Textes](Draft_Text/fr.md), [Draft Dimensions](Draft_Dimension/fr.md) et [Draft Étiquettes](Draft_Label/fr.md) dans le document en cours. <small>(v0.21)</small> 
-   Appuyez sur le bouton **Annuler** pour terminer la commande sans enregistrer les paramètres.



## Remarques

-   Les paramètres de l\'onglet **Forme**, à l\'exception de **Style de trait** et **Mode d'affichage**, sont utilisés non seulement pour les objets Draft, mais aussi pour les objets créés avec d\'autres ateliers.
-   Tous les paramètres, à l\'exception de **Style de trait** et **Mode d'affichage**, peuvent également être modifiés dans les préférences. Voir [PartDesign Préférences](PartDesign_Preferences/fr#Aspect_de_la_forme.md) et [raft Préférences](Draft_Preferences/fr#Textes_et_dimensions.md).
-   Les styles sont enregistrés dans un fichier au nom fixe : **StylePresets.json** stocké dans le dossier utilisateur de FreeCAD **Draft** :
    -   Sous Linux, il s\'agit généralement de **/home/<username>/.local/share/FreeCAD/Draft/**.
    -   Sous Windows, il s\'agit du dossier **%APPDATA%\FreeCAD\\Draft**, qui est généralement sous **C:\Users\<username>\Appdata\Roaming\FreeCAD\Draft**.
    -   Sous macOS, il s\'agit généralement de **/Users/<username>/Library/Preferences/FreeCAD/Draft/**.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft SetStyle/fr
