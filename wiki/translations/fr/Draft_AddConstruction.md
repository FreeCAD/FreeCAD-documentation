---
- GuiCommand:/fr
   Name:Draft AddConstruction
   Name/fr:Draft Ajouter au groupe de construction
   MenuLocation:Utilitaires → Ajouter au groupe de construction
   Workbenches:[Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   Version:0.17
   SeeAlso:[Draft Basculer en mode construction](Draft_ToggleConstructionMode/fr.md), [Draft Ajouter au groupe](Draft_AddToGroup/fr.md)
---

## Description

La commande <img alt="" src=images/Draft_AddConstruction.svg  style="width:24px;"> **Draft Ajouter au groupe de construction** déplace les objets vers le [Draft Groupe de construction](Draft_ToggleConstructionMode/fr.md). Elle applique également la [couleur de la géométrie de la construction](Draft_ToggleConstructionMode/fr#Pr.C3.A9f.C3.A9rences.md) aux objets.

## Bug dans la version 0.19 {#bug_dans_la_version_0.19}

Dans la version 0.19 de FreeCAD, cette commande et la commande [Draft Basculer en mode construction](Draft_ToggleConstructionMode/fr.md) utilisent généralement des groupes différents. Pour éviter cela, changez {{MenuCommand|Construction group name}} dans les préférences en {{Value|Draft_Construction}} : {{MenuCommand|Edition → Préférences... → Draft → Paramètres généraux → Géométrie de construction → Nom du groupe de construction}}. Dans la version 0.20, {{MenuCommand|Construction group name}} est utilisé pour le libellé du groupe de construction, le nom du groupe est toujours {{Value|Draft_Construction}}.

## Utilisation

1.  Sélectionner un ou plusieurs objets.
2.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le **<img src="images/Draft_AddConstruction.svg" width=16px> [Draft Ajoute les objets sélectionnées au groupe de construction...](Draft_AddConstruction/fr.md)**.
    -   Sélectionnez l\'option {{MenuCommand|Utilitaires → <img src="images/Draft_AddConstruction.svg" width=16px> Ajouter au groupe de construction }} dans le menu.
3.  S\'il n\'existe pas, le groupe de construction doit être créé en premier.
4.  Les objets sont déplacés vers le groupe de construction et leurs propriétés de couleur sont modifiées.

## Remarques

-   Les objets peuvent également être déplacés vers le groupe de construction en les glissant et en les déposant sur le groupe dans la [Vue en arborescence](Tree_view/fr.md) ou en utilisant la commande [Draft Ajouter au groupe de construction](Draft_AddToGroup/fr.md). Dans les deux cas, la [Couleur de la géométrie de construction](Draft_ToggleConstructionMode/fr#Pr.C3.A9f.C3.A9rences.md) n\'est pas appliquée.
-   Pour plus d\'informations sur l\'organisation de votre modèle, voir [Structure du document](Document_structure/fr.md) et [Tutoriel Arch](Arch_tutorial/fr#Organiser_votre_mod.C3.A8le.md)





 
