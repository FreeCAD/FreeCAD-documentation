---
 GuiCommand:
   Name: Draft ToggleConstructionMode
   Name/fr: Draft Basculer en mode construction
   MenuLocation: Utilitaires , Basculer en mode construction
   Workbenches: Draft_Workbench/fr, BIM_Workbench/fr
   Shortcut: Draft : **C** **M**
   SeeAlso: Draft_AddConstruction/fr, Draft_AutoGroup/fr
---

# Draft ToggleConstructionMode/fr

## Description

La commande <img alt="" src=images/Draft_ToggleConstructionMode.svg  style="width:24px;"> **Draft Basculer en mode construction** active ou désactive le mode de construction de Draft. Si le mode construction est activé, les nouveaux objets [Draft](Draft_Workbench/fr.md) sont placés dans un groupe dédié et reçoivent une couleur prédéfinie. Cette fonction est destinée à la géométrie de construction, souvent temporaire, utilisée pour fournir de nouveaux [points d\'aimantation](Draft_Snap/fr.md) pour la création d\'autres objets. Lorsque la géométrie de construction n\'est plus nécessaire, le groupe de construction peut facilement être [caché](Std_HideSelection/fr.md) ou [effacé](Std_Delete/fr.md).

<img alt="" src=images/Draft_construction_mode_example.jpg  style="width:400px;"> 
*Géométrie de construction, en bleu, utilisée pour déterminer le centre et le rayon d'un cercle*



## Utilisation

1.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton ![](images/Draft_tray_button_construction.png ) de la [Draft Barre](Draft_Tray/fr.md). Ce bouton est activé si le mode de construction Draft est en cours.
    -   [Draft](Draft_Workbench/fr.md) : sélectionnez l\'option **Utilitaires → <img src="images/Draft_ToggleConstructionMode.svg" width=16px> Basculer en mode construction** du menu ou dans le menu contextuel de la [vue en arborescence](Tree_view/fr.md) ou de la [vue 3D](3D_view/fr.md).
    -   Draft: utilisez le raccourci clavier : **C** puis **M**.
2.  Le bouton de la [Draft Barre](Draft_Tray/fr.md) est mis à jour.



## Remarques

-   Si le mode de construction Draft est activé, le [calque](Draft_Layer/fr.md) actif est ignoré.



## Préférences

-   Pour modifier l\'étiquette du groupe de construction : **Édition → Préférences... → Draft → Général → Étiquette du groupe de construction**.
-   Pour modifier la couleur utilisée : **Édition → Préférences... → Draft → Général → Couleur de la géométrie de construction**.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft ToggleConstructionMode/fr
