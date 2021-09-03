---
- GuiCommand:/fr
   Name:Draft ToggleConstructionMode
   Name/fr:Draft Basculer en mode construction
   MenuLocation:Utilitaires → Basculer en mode construction
   Workbenches:[Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   Shortcut:**C** **M**
   SeeAlso:[Draft Ajouter au groupe de construction](Draft_AddConstruction/fr.md), [Draft Groupe automatique](Draft_AutoGroup/fr.md)
---

## Description

La commande <img alt="" src=images/Draft_ToggleConstructionMode.svg  style="width:24px;"> **Draft Basculer en mode construction** active ou désactive le mode de construction de Draft. Si le mode construction est activé, les nouveaux objets [Draft](Draft_Workbench/fr.md), à l\'exception des [Draft Points](Draft_Point/fr.md), sont placés dans un groupe dédié et reçoivent une couleur prédéfinie. Cette fonctionnalité est destinée à la géométrie de construction, souvent temporaire, utilisée pour fournir de nouveaux [points d\'accrochage](Draft_Snap/fr.md) pour la création d\'autres objets. Lorsque la géométrie de construction n\'est plus nécessaire, le groupe de construction peut facilement être [caché](Std_HideSelection/fr.md) ou [effacé](Std_Delete/fr.md).

<img alt="" src=images/Draft_construction_mode_example.jpg  style="width:400px;"> 
*Géométrie de construction, en bleu, utilisée pour déterminer le centre et le rayon d'un cercle*

## Bug dans la version 0.19 {#bug_dans_la_version_0.19}

Dans la version 0.19 de FreeCAD, cette commande et la commande [Draft Ajouter au groupe de construction](Draft_AddConstruction/fr.md) utilisent généralement des groupes différents. Pour éviter cela, changez {{MenuCommand|Construction group name}} dans les préférences en {{Value|Draft_Construction}} : {{MenuCommand|Edition → Préférences... → Draft → Paramètres généraux → Géométrie de construction → Nom du groupe de construction}}. Dans la version 0.20, {{MenuCommand|Construction group name}} est utilisé pour le libellé du groupe de construction, le nom du groupe est toujours {{Value|Draft_Construction}}.

## Utilisation

1.  Il y a plusieurs façons d\'invoquer la commande :
    -   Appuyez sur le bouton **<img src="images/Draft_ToggleConstructionMode.svg" width=16px> [Basculer en mode construction](Draft_ToggleConstructionMode/fr.md)** de [Draft La barre](Draft_Tray/fr.md). Ce bouton est enfoncé si le mode de construction Draft est activé.
    -   Sélectionnez l\'option {{MenuCommand|Utilitaires → <img src="images/Draft_ToggleConstructionMode.svg" width=16px> Basculer en mode construction}} dans le menu.
    -   Utilisez le raccourci clavier : **C** puis **M**.
2.  Le bouton de [Draft La barre](Draft_Tray/fr.md) est mis à jour.

## Remarques

-   Si le mode de construction Draft est activé, le [calque](Draft_Layer/fr.md) actif est ignoré.

## Préférences

-   Pour modifier l\'étiquette ({{Version/fr|0.20}}) du groupe de construction : {{MenuCommand|Edition → Préférences... → Draft → Paramètres généraux → Géométrie de construction → Nom du groupe de construction}}.
-   Pour modifier la couleur utilisée : {{MenuCommand|Edition → Préférences... → Draft → Paramètres généraux → Géométrie de construction → Couleur de la géométrie de construction}}.





 
