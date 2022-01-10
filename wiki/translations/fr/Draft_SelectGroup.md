---
- GuiCommand:/fr
   Name:Draft SelectGroup
   Name/fr:Draft Sélection groupée
   MenuLocation:Utilitaires → Sélectionner le groupe
   Workbenches:[Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   SeeAlso:[Std Créer un groupe](Std_Group/fr.md), [Draft Ajouter au groupe](Draft_AddToGroup/fr.md), [Draft Ajouter au groupe de construction](Draft_AddConstruction/fr.md), [Draft Groupement automatique](Draft_AutoGroup/fr.md)
---

# Draft SelectGroup/fr

## Description


<div class="mw-translate-fuzzy">

La commande <img alt="" src=images/Draft_SelectGroup.svg  style="width:24px;"> **Draft Sélection groupée** sélectionne le contenu des objets [Draft Calques](Draft_Layer/fr.md), [Std Groupes](Std_Group/fr.md) ou des objets de type groupe [Arch](Arch_Workbench/fr.md).


</div>

The command was revised in FreeCAD version 0.20 and this page describes that version.

## Utilisation


<div class="mw-translate-fuzzy">

1.  Pour utiliser cette commande, au moins un groupe ou un calque doit exister.
2.  Sélectionnez un ou plusieurs objets, la sélection peut inclure des groupes sélectionnés dans la [Vue en arborescence](Tree_view/fr.md).
3.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Draft_SelectGroup.svg" width=16px> [Draft Si la sélection est un groupe...](Draft_SelectGroup/fr.md)**.
    -   Sélectionnez l\'option **Utilitaires → <img src="images/Draft_SelectGroup.svg" width=16px> Sélectionner le groupe ** dans le menu.
    -   Sélectionnez l\'option **Utilitaires → <img src="images/Draft_SelectGroup.svg" width=16px> Sélectionner un groupe** dans le menu contextuel de la [Vue en arborescence](Tree_view/fr.md) ou de la [Vue 3D](3D_view/fr.md).
4.  Les résultats de la commande dépendent de la sélection fournie :
    -   Pour un objet imbriqué simple, le groupe ou le calque dans lequel se trouve l\'objet, et son autre contenu, les objets apparentés de l\'objet donné, sont sélectionnés. Les objets apparentés peuvent inclure des groupes, mais le contenu de ces groupes imbriqués n\'est pas sélectionné.
    -   Pour un groupe donné, le groupe lui-même, le contenu du groupe et le contenu de tous les groupes imbriqués, quel que soit leur niveau d\'imbrication, sont sélectionnés, mais les groupes imbriqués eux-mêmes ne le sont pas.


</div>

## Remarques

-   Pour plus d\'informations sur l\'organisation de votre modèle, voir [Structure du document](Document_structure/fr.md) et [Tutoriel Arch](Arch_tutorial/fr#Organiser_votre_mod.C3.A8le.md).

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft SelectGroup/fr
