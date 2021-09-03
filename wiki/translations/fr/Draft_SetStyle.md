---
- GuiCommand:/fr
   Name:Draft SetStyle
   Name/fr:Draft Définir le style
   MenuLocation:Utilities → Définir le style
   Workbenches:[Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   Version:0.19
   SeeAlso:[Draft Éditeur de styles d'annotations](Draft_AnnotationStyleEditor/fr.md), [Draft Appliquer le style](Draft_ApplyStyle/fr.md)
---

## Description

La commande <img alt="" src=images/Draft_SetStyle.svg  style="width:24px;"> **Draft Définir le style** définit le style par défaut des nouveaux objets.

Cette commande est un travail en cours et la version V0.19 ainsi que la version V0.20 souffrent de plusieurs bogues.

![](images/Draft_SetStyle_taskpanel.png ) *Le panneau de tâches des paramètres de style*

## Utilisation

1.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton ![](images/Draft_tray_button_style.png ) de la [Draft Barre](Draft_Tray/fr.md). En fonction des paramètres de style en cours, ce bouton peut avoir un aspect différent.
    -   Sélectionnez l\'option {{MenuCommand|Utilitaires → <img src="images/Draft_SetStyle.svg" width=16px> Définir le style}} dans le menu.
2.  Le panneau de tâches {{MenuCommand|Paramètres de style}} s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
3.  Modifiez éventuellement un ou plusieurs paramètres.
4.  Appuyez sur le bouton **OK**.
5.  Le bouton de la [Draft Barre](Draft_Tray/fr.md) est mis à jour.

## Options

-   Dans la liste déroulante en haut du panneau des tâches, un style sortant peut être sélectionné. {{Version/fr|0.20}}
-   Appuyez sur le bouton {{button|<img src="images/Document-save.svg" width=16px> Enregistrer le style}} pour enregistrer les paramètres du style. {{Version/fr|0.20}}
-   Dans la section {{MenuCommand|Lignes et faces}}, les paramètres suivants peuvent être spécifiés :
    -   
        {{MenuCommand|Couleur de ligne}}
        
        . Utilisé aussi pour les [Draft Étiquettes](Draft_Label/fr.md) et pour la {{PropertyView/fr|Point Color}} des objets.

    -   
        {{MenuCommand|Largeur de ligne}}
        
        . Utilisé aussi pour les [Draft Étiquettes](Draft_Label/fr.md).

    -   
        {{MenuCommand|Style de représentation}}
        
        . Cette fonctionnalité ne fonctionne pas actuellement.

    -   
        {{MenuCommand|Mode d'affichage}}
        
        . Cette fonction ne fonctionne pas actuellement.

    -   
        {{MenuCommand|Couleur de la forme}}
        
        .

    -   
        {{MenuCommand|Transparence}}
        
        . Cette fonction ne fonctionne pas actuellement.
-   Dans la section {{MenuCommand|Annotations}}, les paramètres suivants peuvent être spécifiés :
    -   
        {{MenuCommand|Police de caractère}}
        
        .

    -   
        {{MenuCommand|Taille du texte}}
        
        . Il s\'agit en fait de la hauteur de la ligne, les lettres sont plus petites.

    -   
        {{MenuCommand|Espacement des caractères}}
        
        . Ceci est utilisé pour [Draft Dimensions](Draft_Dimension/fr.md). Il s\'agit de la distance entre le texte et la ligne de dimension. {{Version/fr|0.20}}

    -   
        {{MenuCommand|Couleur du texte}}
        
        . Utilisé aussi par {{MenuCommand|Couleur de ligne}} de [Draft Dimensions](Draft_Dimension/fr.md), qui définit la couleur de toute la dimension, y compris le texte.

    -   
        {{MenuCommand|Espacement des lignes}}
        
        . Ce facteur d\'échelle est appliqué à la hauteur de la ligne. Cette fonctionnalité ne fonctionne pas actuellement. {{Version/fr|0.20}}

    -   
        {{MenuCommand|Style de flèche}}
        
        .

    -   
        {{MenuCommand|Taille de la flèche}}
        
        .

    -   
        {{MenuCommand|Afficher les unités}}
        
        .

    -   
        {{MenuCommand|Substitution d'unité}}
        
        .
-   Appuyez sur le bouton {{button|<img src="images/Draft_SetStyle.svg" width=16px> Appliquer aux objets sélectionné}} pour appliquer les paramètres aux objets ou groupes sélectionnés. {{Version/fr|0.20}}
-   Appuyez sur le bouton {{button|<img src="images/Draft_Text.svg" width=16px> Textes/dimensions}} pour appliquer les paramètres à tous les [Draft Textes](Draft_Text.md) et [Draft Dimensions](Draft_Dimension/fr.md). {{Version/fr|0.20}}
-   Appuyez sur le bouton **Annuler** pour abandonner la commande.

## Remarques

-   Les paramètres {{MenuCommand|Couleur de ligne}}, {{MenuCommand|Largeur de ligne}} et {{MenuCommand|Couleur de la forme}} ne sont pas seulement utilisés pour les objets Draft, mais aussi pour les objets créés avec d\'autres ateliers.
-   Les styles sont enregistrés dans un fichier au nom fixe : {{FileName|StylePresets.json}} stocké dans le dossier utilisateur de FreeCAD {{FileName|Draft}} :
    -   Sous Linux, il s\'agit généralement de {{FileName|/home/<username>/.FreeCAD/Draft/}}.
    -   Sous Windows, il s\'agit du dossier {{FileName|%APPDATA%\FreeCAD\\Draft}}, qui est généralement sous {{FileName|C:\Users\<username>\Appdata\Roaming\FreeCAD\Draft}}.
    -   Sous macOS, il s\'agit généralement de {{FileName|/Users/<username>/Library/Preferences/FreeCAD/Draft/}}.

## Préférences

Voir aussi : [Réglage des préférences](Preferences_Editor/fr.md) et [Draft Préférences](Draft_Preferences/fr.md).

Les préférences suivantes sont en jeu :

-   Couleur de ligne : {{MenuCommand|Edition → Préférences... → Conception de pièces → Apparence de la forme → Propriétés par défaut de la vue de la forme → Couleur de la ligne}}.
-   Largeur de ligne : {{MenuCommand|Edition → Préférences... → Conception de pièces → Apparence de la forme → Propriétés par défaut de la vue de la forme → Largeur de ligne}}.
-   Style de dessin : {{MenuCommand|Outils → Editer paramètres... → BaseApp → Preferences → Mod → Draft → DefaultDrawStyle}}.
-   Mode d\'affichage : {{MenuCommand|Outils → Editer paramètres... → BaseApp → Preferences → Mod → Draft → DefaultDisplayMode}}.
-   Couleur de la forme : {{MenuCommand|Edition → Préférences... → Conception de pièces → Apparence de la forme → Propriétés d'affichage par défaut de la forme → Couleur de la forme}}.
-   Transparence : {{MenuCommand|Outils → Editer paramètres... → BaseApp → Preferences → Mod → Draft → DefaultTransparency}}.
-   Police du texte : {{MenuCommand|Edition → Préférences... → Draft → Textes et dimensions → Paramètres du texte → Famille de polices}}.
-   Taille du texte : {{MenuCommand|Edition → Préférences... → Draft → Textes et dimensions → Paramètres du texte → Taille de police}}.
-   Espacement du texte : {{MenuCommand|Edition → Préférences... → Draft → Textes et dimensions → Paramètres de cotation → Espacement du texte}}.
-   Couleur du texte : {{MenuCommand|Outils → Editer paramètres... → BaseApp → Preferences → Mod → Draft → DefaultTextColor}}.
-   Espacement des lignes : {{MenuCommand|Outils → Editer paramètres... → BaseApp → Preferences → Mod → Draft → LineSpacing}}.
-   Style de flèche : {{MenuCommand|Edition → Préférences... → Draft → Textes et dimensions → Paramètres de cotation → Style des flèches}}.
-   Taille de la flèche : {{MenuCommand|Edition → Préférences... → Draft → Textes et dimensions → Paramètres de cotation → Taille des flèches}}.
-   Afficher les unités : {{MenuCommand|Edition → Préférences... → Draft → Textes et dimensions → Paramètres de cotation → Afficher le suffixe de l'unité aux dimensions}}.
-   Remplacement de l\'unité : {{MenuCommand|Edition → Préférences... → Draft → Textes et dimensions → Paramètres de cotation → Remplacer l'unité}}.





 
