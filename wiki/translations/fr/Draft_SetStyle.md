---
- GuiCommand   */fr
   Name   *Draft SetStyle
   Name/fr   *Draft Définir le style
   MenuLocation   *Utilities → Définir le style
   Workbenches   *[Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   Shortcut   ***S** **S**
   Version   *0.19
   SeeAlso   *[Draft Éditeur de styles d'annotations](Draft_AnnotationStyleEditor/fr.md), [Draft Appliquer le style](Draft_ApplyStyle/fr.md)
---

# Draft SetStyle/fr

## Description

La commande <img alt="" src=images/Draft_SetStyle.svg  style="width   *24px;"> **Draft Définir le style** définit le style par défaut des nouveaux objets.

Notez que plusieurs fonctionnalités ne fonctionnent pas dans la version V0.19 de cette commande.

![](images/Draft_SetStyle_taskpanel.png ) 
*Le panneau de tâches des paramètres de style*

## Utilisation

1.  Il y a plusieurs façons de lancer la commande    *
    -   Appuyez sur le bouton ![](images/Draft_tray_button_style.png ) de la [Draft Barre](Draft_Tray/fr.md). En fonction des paramètres de style en cours, ce bouton peut avoir un aspect différent.
    -   Sélectionnez l\'option **Utilitaires → <img src="images/Draft_SetStyle.svg" width=16px> Définir le style** dans le menu.
    -   Utilisez le raccourci clavier    * **S** puis **S**. {{Version/fr|0.20}}
2.  Le panneau de tâches **Paramètres de style** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
3.  Modifiez éventuellement un ou plusieurs paramètres.
4.  Appuyez sur le bouton **OK**.
5.  Le bouton de la [Draft Barre](Draft_Tray/fr.md) est mis à jour.

## Options

-   Dans la liste déroulante en haut du panneau des tâches, un style sortant peut être sélectionné. {{Version/fr|0.20}}
-   Appuyez sur le bouton **<img src="images/Document-save.svg" width=16px> Enregistrer le style** pour enregistrer les paramètres du style. {{Version/fr|0.20}}
-   Dans la section **Lignes et faces**, les paramètres suivants peuvent être spécifiés    *
    -   
        **Couleur de ligne**
        
        . Utilisé aussi pour les [Draft Étiquettes](Draft_Label/fr.md) et pour la **Point Color** des objets.

    -   
        **Largeur de ligne**
        
        . Utilisé aussi pour les [Draft Étiquettes](Draft_Label/fr.md).

    -   
        **Style de représentation**
        
        .

    -   
        **Mode d'affichage**
        
        .

    -   
        **Couleur de la forme**
        
        .

    -   
        **Transparence**
        
        .
-   Dans la section **Annotations**, les paramètres suivants peuvent être spécifiés    *
    -   
        **Police de caractère**
        
        .

    -   
        **Taille du texte**
        
        . Il s\'agit en fait de la hauteur de la ligne, les lettres sont plus petites.

    -   
        **Espacement des caractères**
        
        . Ceci est utilisé pour [Draft Dimensions](Draft_Dimension/fr.md). Il s\'agit de la distance entre le texte et la ligne de dimension. {{Version/fr|0.20}}

    -   
        **Couleur du texte**
        
        . Utilisé aussi par **Couleur de ligne** de [Draft Dimensions](Draft_Dimension/fr.md), qui définit la couleur de toute la dimension, y compris le texte.

    -   
        **Espacement des lignes**
        
        . Ce facteur d\'échelle est appliqué à la hauteur de la ligne. {{Version/fr|0.20}}

    -   
        **Style de flèche**
        
        .

    -   
        **Taille de la flèche**
        
        .

    -   
        **Afficher les unités**
        
        .

    -   
        **Substitution d'unité**
        
        .
-   Appuyez sur le bouton **<img src="images/Draft_SetStyle.svg" width=16px> Appliquer aux objets sélectionné** pour appliquer les paramètres aux objets ou groupes sélectionnés. {{Version/fr|0.20}}
-   Appuyez sur le bouton **<img src="images/Draft_Text.svg" width=16px> Textes/dimensions** pour appliquer les paramètres à tous les [Draft Textes](Draft_Text/fr.md) et [Draft Dimensions](Draft_Dimension/fr.md). {{Version/fr|0.20}}
-   Appuyez sur le bouton **Annuler** pour abandonner la commande.

## Remarques

-   Les paramètres **Couleur de ligne**, **Largeur de ligne** et **Couleur de la forme** ne sont pas seulement utilisés pour les objets Draft, mais aussi pour les objets créés avec d\'autres ateliers.
-   Les styles sont enregistrés dans un fichier au nom fixe    * **StylePresets.json** stocké dans le dossier utilisateur de FreeCAD **Draft**    *
    -   Sous Linux, il s\'agit généralement de **/home/<username>/.FreeCAD/Draft/**.
    -   Sous Windows, il s\'agit du dossier **%APPDATA%\FreeCAD\\Draft**, qui est généralement sous **C   *Users\<username>\Appdata\Roaming\FreeCAD\Draft**.
    -   Sous macOS, il s\'agit généralement de **/Users/<username>/Library/Preferences/FreeCAD/Draft/**.

## Préférences

Voir aussi    * [Réglage des préférences](Preferences_Editor/fr.md) et [Draft Préférences](Draft_Preferences/fr.md).

Les préférences suivantes sont en jeu    *

-   Couleur de ligne    * **Edition → Préférences... → Conception de pièces → Apparence de la forme → Propriétés par défaut de la vue de la forme → Couleur de la ligne**.
-   Largeur de ligne    * **Edition → Préférences... → Conception de pièces → Apparence de la forme → Propriétés par défaut de la vue de la forme → Largeur de ligne**.
-   Style de dessin    * **Outils → Editer paramètres... → BaseApp → Preferences → Mod → Draft → DefaultDrawStyle**.
-   Mode d\'affichage    * **Outils → Editer paramètres... → BaseApp → Preferences → Mod → Draft → DefaultDisplayMode**.
-   Couleur de la forme    * **Edition → Préférences... → Conception de pièces → Apparence de la forme → Propriétés d'affichage par défaut de la forme → Couleur de la forme**.
-   Transparence    * **Outils → Editer paramètres... → BaseApp → Preferences → Mod → Draft → DefaultTransparency**.
-   Police du texte    * **Edition → Préférences... → Draft → Textes et dimensions → Paramètres du texte → Famille de polices**.
-   Taille du texte    * **Edition → Préférences... → Draft → Textes et dimensions → Paramètres du texte → Taille de police**.
-   Espacement du texte    * **Edition → Préférences... → Draft → Textes et dimensions → Paramètres de cotation → Espacement du texte**.
-   Couleur du texte    * **Outils → Editer paramètres... → BaseApp → Preferences → Mod → Draft → DefaultTextColor**.
-   Espacement des lignes    * **Outils → Editer paramètres... → BaseApp → Preferences → Mod → Draft → LineSpacing**.
-   Style de flèche    * **Edition → Préférences... → Draft → Textes et dimensions → Paramètres de cotation → Style des flèches**.
-   Taille de la flèche    * **Edition → Préférences... → Draft → Textes et dimensions → Paramètres de cotation → Taille des flèches**.
-   Afficher les unités    * **Edition → Préférences... → Draft → Textes et dimensions → Paramètres de cotation → Afficher le suffixe de l'unité aux dimensions**.
-   Remplacement de l\'unité    * **Edition → Préférences... → Draft → Textes et dimensions → Paramètres de cotation → Remplacer l'unité**.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft SetStyle/fr
