---
- GuiCommand:
   Name: Draft SetStyle
   Name/fr: Draft Définir le style
   MenuLocation: Utilitaires - Définir le style
   Workbenches: [Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   Shortcut: **S** **S**
   Version: 0.19
   SeeAlso: [Draft Éditeur de styles d'annotations](Draft_AnnotationStyleEditor/fr.md), [Draft Appliquer le style](Draft_ApplyStyle/fr.md)
---

# Draft SetStyle/fr

## Description

La commande <img alt="" src=images/Draft_SetStyle.svg  style="width:24px;"> **Draft Définir le style** définit le style par défaut des nouveaux objets.

<img alt="" src=images/Draft_SetStyle_Taskpanel.png  style="width:" height="550px;"> 
*Le panneau de tâches des paramètres de style*



## Utilisation

1.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton ![](images/Draft_tray_button_style.png ) de la [Draft Barre](Draft_Tray/fr.md). En fonction des paramètres de style en cours, ce bouton peut avoir un aspect différent.
    -   Sélectionnez l\'option **Utilitaires → <img src="images/Draft_SetStyle.svg" width=16px> Définir le style** dans le menu.
    -   Utilisez le raccourci clavier : **S** puis **S**. {{Version/fr|0.20}}
2.  Le panneau de tâches **Paramètres de style** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
3.  Modifiez éventuellement un ou plusieurs paramètres.
4.  Appuyez sur le bouton **OK** pour enregistrer les paramètres.
5.  Le bouton de la [Draft Barre](Draft_Tray/fr.md) est mis à jour.

## Options

-   Dans la liste déroulante en haut du panneau des tâches, un style sortant peut être sélectionné. {{Version/fr|0.20}}
-   Appuyez sur le bouton **<img src="images/Document-save.svg" width=16px> Enregistrer le style** pour enregistrer les paramètres du style. {{Version/fr|0.20}}
-   Dans la section **Lignes et faces**, les paramètres suivants peuvent être spécifiés :
    -   
        **Couleur de la ligne**
        
        . Elle est également utilisée pour les annotations ({{Version/fr|0.21}}) et pour la **Point Color** des objets.

    -   
        **Epaisseur de la ligne**
        
        . Ce paramètre est également utilisé pour les annotations ({{Version/fr|0.21}}) et pour l\'affichage des propriétés des objets (**Point Size**).

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
-   Les paramètres de la section **Annotations** s\'appliquent aux [Draft Textes](Draft_Text/fr.md), [Draft Dimensions](Draft_Dimension/fr.md) et [Draft Etiquettes](Draft_Label/fr.md). Les paramètres suivants peuvent être spécifiés (voir [Draft Texte](Draft_Text/fr#Vue.md) pour plus de détails) :
    -   
        **Police de caractère**
        
        .

    -   
        **Taille du texte**
        
        . Il s\'agit en fait de la hauteur de la ligne, les lettres sont plus petites.

    -   
        **Couleur du texte**
        
        . Utilisé aussi par **Couleur de ligne** de [Draft Dimensions](Draft_Dimension/fr.md), qui définit la couleur de toute la dimension, y compris le texte.

    -   
        **Espacement des lignes**
        
        . Non utilisé pour les dimensions. {{Version/fr|0.20}}
-   Dans la section **Dimensions**, les paramètres suivants peuvent être spécifiés (voir [Draft Dimension](Draft_Dimension/fr#Vue.md) pour plus de détails) :
    -   
        **Style de flèche**
        
        .

    -   
        **Taille de la flèche**
        
        .

    -   
        **Dépassement des lignes de dimension**
        
        . {{Version/fr|0.21}}

    -   
        **Lignes d'extension**
        
        . {{Version/fr|0.21}}

    -   
        **Dépassement des lignes d'extension**
        
        . {{Version/fr|0.21}}

    -   
        **Espacement du texte**
        
        . {{Version/fr|0.20}}

    -   
        **Afficher les unités**
        
        .

    -   
        **Substitution d'unité**
        
        .
-   Appuyez sur le bouton **<img src="images/Draft_SetStyle.svg" width=16px> Sélectionné** pour appliquer les paramètres aux objets ou groupes sélectionnés. Les objets peuvent être sélectionnés lorsque le panneau des tâches est ouvert. {{Version/fr|0.20}}
-   Appuyez sur le bouton **<img src="images/Draft_Text.svg" width=16px> Annotations** pour appliquer les paramètres à tous les [Draft Textes](Draft_Text/fr.md), [Draft Dimensions](Draft_Dimension/fr.md) et [Draft Étiquettes](Draft_Label/fr.md) du document en cours. {{Version/fr|0.21}}
-   Appuyez sur le bouton **Annuler** pour terminer la commande sans enregistrer les paramètres.



## Remarques

-   Les paramètres **Couleur de ligne**, **Largeur de ligne**, **Couleur de la forme** et **Transparence** ne sont pas seulement utilisés pour les objets Draft, mais aussi pour les objets créés avec d\'autres ateliers.
-   Les styles sont enregistrés dans un fichier au nom fixe : **StylePresets.json** stocké dans le dossier utilisateur de FreeCAD **Draft** :
    -   Sous Linux, il s\'agit généralement de **/home/<username>/.local/share/FreeCAD/Mod/** ({{VersionPlus/fr|0.20}}) ou **/home/<username>/.FreeCAD/Mod/** ({{VersionMinus/fr|0.19}}).
    -   Sous Windows, il s\'agit du dossier **%APPDATA%\FreeCAD\\Draft**, qui est généralement sous **C:\Users\<username>\Appdata\Roaming\FreeCAD\Draft**.
    -   Sous macOS, il s\'agit généralement de **/Users/<username>/Library/Preferences/FreeCAD/Draft/**.



## Préférences

Voir aussi : [Réglage des préférences](Preferences_Editor/fr.md) et [Draft Préférences](Draft_Preferences/fr.md).

Les préférences suivantes sont en jeu :

-   Couleur de ligne : **Edition → Préférences... → Part/Part Design → Apparence de la forme → Propriétés par défaut de la vue de la forme → Couleur de la ligne** et **Couleur des points**.
-   Largeur de ligne : **Edition → Préférences... → Part/Part Design → Apparence de la forme → Propriétés par défaut de la vue de la forme → Largeur de ligne** et **Taille des points**.
-   Style de dessin : **Outils → Editer paramètres... → BaseApp → Preferences → Mod → Draft → DefaultDrawStyle**.
-   Mode d\'affichage : **Outils → Editer paramètres... → BaseApp → Preferences → Mod → Draft → DefaultDisplayMode**.
-   Couleur de la forme : **Edition → Préférences... → Part/Part Design → Apparence de la forme → Propriétés d'affichage par défaut de la forme → Couleur de la forme**.
-   Transparence : **Edition → Préférences... → Part/Part Design → Apparence de la forme → Transparence de la forme**.
-   Police du texte : **Edition → Préférences... → Draft → Textes et cotes → Paramètres pour le texte → Famille de polices**.
-   Taille du texte : **Edition → Préférences... → Draft → Textes et cotes → Paramètres pour le texte → Taille de police**.
-   Couleur du texte : **Outils → Editer paramètres... → BaseApp → Preferences → Mod → Draft → DefaultTextColor**.
-   Espacement des lignes : **Outils → Editer paramètres... → BaseApp → Preferences → Mod → Draft → LineSpacing**.
-   Style de flèche : **Edition → Préférences... → Draft → Textes et cotes → Paramètres pour les dimensions → Style des flèches**.
-   Taille de la flèche : **Edition → Préférences... → Draft → Textes et cotes → Paramètres pour les dimensions → Taille des flèches**.
-   Dépassement des lignes de dimension : **Edition → Préférences... → Draft → Textes et cotes → Paramètres pour les dimensions → Dépassement des lignes de dimension**.
-   Lignes d\'extension : **Edition → Préférences... → Draft → Textes et cotes → Paramètres pour les dimensions → Lignes d'extension**.
-   Dépassement des lignes d\'extension : Lignes d\'extension : **Edition → Préférences... → Draft → Textes et cotes → Paramètres pour les dimensions → Dépassement des lignes d'extension**.
-   Espacement du texte : **Edition → Préférences... → Draft → Textes et cotes → Paramètres pour les cotations → Espacement du texte**.
-   Afficher les unités : **Edition → Préférences... → Draft → Textes et cotes → Paramètres pour les cotations → Afficher le suffixe de l'unité aux dimensions**.
-   Remplacement de l\'unité : **Edition → Préférences... → Draft → Textes et cotes → Paramètres pour les cotations → Remplacer l'unité**.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft SetStyle/fr
