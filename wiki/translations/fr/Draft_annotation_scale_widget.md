# Draft annotation scale widget/fr
## Description

Le **Draft Widget d\'échelle d\'annotation** peut être utilisé pour spécifier la mise à l\'échelle des annotations de Draft. Cette échelle détermine le **Scale Multiplier** (facteur d\'échelle) des nouveaux [Draft Textes](Draft_Text/fr.md), [Draft Dimensions](Draft_Dimension/fr.md) et [Draft Étiquettes](Draft_Label/fr.md). Le widget est seulement disponible dans l\'<img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [atelier Draft](Draft_Workbench/fr.md). Il s\'agit d\'un élément de l\'interface graphique [optionnel](#Pr.C3.A9f.C3.A9rences.md) qui se trouve dans la [barre d\'état](Status_bar/fr.md).

![](images/Draft_annotation_scale_widget_button.png ) 
*Le widget d'échelle d'annotation de Draft*



## Utilisation

1.  Appuyez sur le bouton **x:x** dans la [barre d\'état](Status_bar/fr.md). Le bouton affiche l\'échelle d\'annotation actuelle.
2.  Le menu d\'échelle s\'ouvre.
3.  Effectuez l\'une des opérations suivantes :
    -   Sélectionnez l\'une des échelles standards.
    -   Sélectionnez l\'option **Personnalisé** :
        -   Dans la boîte de dialogue qui s\'ouvre, saisissez une échelle personnalisée en utilisant le format {{Value|x:x}} ou {{Value|x<nowiki>=</nowiki>x}}.
        -   Appuyez sur **Entrée** ou sur le bouton **OK**.

![](images/Draft_annotation_scale_widget_menu.png ) 
*Le menu du widget*



## Préférences

Voir aussi : [Réglage des préférences](Preferences_Editor/fr.md) et [Draft Préférences](Draft_Preferences/fr.md).

-   Le widget d\'échelle d\'annotation de Draft est facultatif : **Édition → Préférences... → Draft → Interface → Afficher le widget d'échelle d'annotation dans l'atelier Draft**.
-   Pour modifier l\'échelle d\'annotation sans le widget : **Outils → Éditeur de paramètres... → BaseApp → Preferences → Mod → Draft → DraftAnnotationScale**. L\'échelle est définie par un seul nombre. Pour une échelle de {{Value|1:50}}, entrez {{Value|0.02}}.



## Remarques

-   Voir aussi: [Draft Définir le style](Draft_SetStyle/fr.md) et [Draft Appliquer le style](Draft_ApplyStyle/fr.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft annotation scale widget/fr
