---
- GuiCommand   */fr
   Name   *Draft AddToGroup
   Name/fr   *Draft Déplacer vers un groupe
   MenuLocation   *Utilitaires → Déplacer vers le groupe...
   Workbenches   *[Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   SeeAlso   *[Std Créer un groupe](Std_Group/fr.md), [Draft Nommer un groupe](Draft_AddNamedGroup/fr.md), [Draft Ajouter au groupe de construction](Draft_AddConstruction/fr.md), [Draft Groupement automatique](Draft_AutoGroup/fr.md)
---

# Draft AddToGroup/fr

## Description

La commande <img alt="" src=images/Draft_AddToGroup.svg  style="width   *24px;"> **Draft Déplacer vers le groupe** déplace les objets vers un [Std Groupe](Std_Group/fr.md). Elle peut aussi dégrouper des objets.

Dans la version 0.20 de FreeCAD, la commande peut également gérer les objets de type groupe [Arch](Arch_Workbench/fr.md).

## Utilisation

1.  Sélectionnez un ou plusieurs objets.
2.  Il existe plusieurs façons de lancer la commande    *
    -   Appuyez sur le bouton **<img src="images/Draft_AddToGroup.svg" width=16px> [Déplacer vers le groupe...](Draft_AddToGroup/fr.md)**.
    -   Sélectionnez le bouton **Utilitaires → <img src="images/Draft_AddToGroup.svg" width=16px> [Déplacer vers le groupe...](Draft_AddToGroup/fr.md)** dans le menu.
    -   Sélectionnez l\'option **Utilitaires → <img src="images/Draft_AddToGroup.svg" width=16px> Déplacer vers le groupe... ** dans le menu contextuel de la [Vue en arborescence](Tree_view/fr.md) ou de la [Vue 3D](3D_view/fr.md).
3.  Un menu s\'affiche près du curseur. Effectuez l\'une des opérations suivantes    *
    -   Sélectionnez **Dégrouper** pour déplacer les objets hors du ou des groupes dans lesquels ils se trouvent.
    -   Sélectionnez le groupe vers lequel vous voulez déplacer les objets.
    -   Sélectionnez **+ Ajouter un nouveau groupe** pour déplacer les objets vers un nouveau groupe    * {{Version/fr|0.20}}
        1.  Le panneau de tâches **Ajouter un groupe** s\'ouvre.
        2.  Saisissez un **Nom du groupe**.
        3.  Appuyez sur le bouton **OK**.

## Remarques

-   Les objets peuvent également être déplacés vers un groupe en les glissant et en les déposant sur le groupe dans la [Vue en arborescence](Tree_view/fr.md).
-   Cette commande peut être utilisée pour déplacer des objets vers le [Groupe de construction](Draft_ToggleConstructionMode/fr.md), mais, contrairement à la commande [Draft Déplacer vers un groupe](Draft_AddConstruction/fr.md), elle n\'applique pas la [couleur de la géométrie de la construction](Draft_ToggleConstructionMode/fr#Pr.C3.A9f.C3.A9rences.md).
-   Pour plus d\'informations sur l\'organisation de votre modèle, voir [Structure du document](Document_structure/fr.md) et [Arch Tutoriel](Arch_tutorial/fr#Organiser_votre_mod.C3.A8le.md).



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft AddToGroup/fr
