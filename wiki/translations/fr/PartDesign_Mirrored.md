---
- GuiCommand:
   Name: PartDesign_Mirrored
   Name/fr: PartDesign Symétrie
   MenuLocation: Part Design -> Appliquer une transformation -> Symétrie
   Workbenches: PartDesign_Workbench/fr
   SeeAlso: PartDesign_MultiTransform/fr
---

# PartDesign Mirrored/fr

## Description

L\'outil <img alt="" src=images/PartDesign_Mirrored.svg  style="width:24px;"> **PartDesign Symétrie** reflète une ou plusieurs fonctions.

![](images/PartDesign_Mirrored_example.svg ) 
*Une fonction poche créée à partir d'une esquisse contenant un cercle (A) est utilisée pour créer une fonction symétrie. L'axe vertical de l'esquisse (B) est utilisé pour définir le plan symétrique. Le résultat (C) est illustré à droite.*

## Utilisation

### Créer

1.  Vous pouvez [activé](PartDesign_Body#Active_status.md) le bon corps.
2.  Sélectionnez au besoin une ou plusieurs fonctions dans la [Vue en arborescence](Tree_view/fr.md) ou la [Vue 3D](3D_view/fr.md).
3.  Il existe plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/PartDesign_Mirrored.svg" width=16px> [Symétrie](PartDesign_Mirrored/fr.md)**.
    -   Sélectionnez l\'option **Part Design → Appliquer une transformation → <img src="images/PartDesign_Mirrored.svg" width=16px> Symétrie** dans le menu.
4.  S\'il n\'y a pas de corps actif, et qu\'il y a deux corps ou plus dans le document, la boîte de dialogue **Corps actif requis** s\'ouvrira et vous invitera à en activer un. S\'il y a un seul corps, il sera activé automatiquement.
5.  Si aucune fonction n\'a été sélectionnée, le [Panneau des tâches](Task_panel/fr.md) **Ajouter une fonction** s\'ouvre : sélectionnez-en une ou plusieurs (en maintenant la touche **Ctrl**) dans la liste et appuyez sur le bouton **OK**.
6.  Le [Panneau des tâches](Task_panel/fr.md) **Paramètres de la symétrie** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
7.  Appuyez sur le bouton **OK** pour terminer.

### Éditer

1.  Effectuez l\'une des opérations suivantes :
    -   Double-cliquez sur l\'objet Mirrored dans la [Vue en arborescence](Tree_view/fr.md).
    -   Cliquez avec le bouton droit de la souris sur l\'objet Mirrored dans la [Vue en arborescence](Tree_view/fr.md) et sélectionnez **Modifier la symétrie** dans le menu contextuel.
2.  Le [Panneau des tâches](Task_panel/fr.md) des **Paramètres de la symétrie** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
3.  Appuyez sur le bouton **OK** pour terminer.

## Options

-   Pour ajouter des fonctions :
    1.  Appuyez sur le bouton **Ajouter une fonction**.
    2.  Sélectionnez une fonction dans la [Vue en arborescence](Tree_view/fr.md) ou la [Vue 3D](3D_view/fr.md).
    3.  Répétez l\'opération pour ajouter d\'autres fonctions.
-   Pour supprimer des fonctions :
    1.  Appuyez sur le bouton **Supprimer une fonction**.
    2.  Effectuez l\'une des opérations suivantes :
        -   Sélectionnez une fonction dans la [Vue en arborescence](Tree_view/fr.md) ou la [Vue 3D](3D_view/fr.md).
        -   Sélectionnez une fonction dans la liste et appuyez sur la touche **Suppr**.
        -   Cliquez avec le bouton droit de la souris sur une fonction de la liste et sélectionnez **Enlever** dans le menu contextuel.
    3.  Répétez l\'opération pour supprimer d\'autres fonctions.
-   S\'il y a plusieurs fonctions dans la transformation, leur ordre peut être important. Voir [Organiser les fonctions](#Organiser_les_fonctions.md).
-   Spécifiez le **Plan** de la symétrie :
    -   
        **Axe normal à l'esquisse**
        
        : L\'axe Z de l\'esquisse (disponible uniquement pour les fonctions basées sur l\'esquisse).

    -   
        **Axe d'esquisse vertical**
        
        : L\'axe Y de l\'esquisse (idem).

    -   
        **Axe d'esquisse horizontal**
        
        : L\'axe X de l\'esquisse (idem).

    -   
        **Ligne de construction #**
        
        : Une entrée séparée pour chaque ligne de construction dans l\'esquisse (idem).

    -   
        **Axe X**
        
        : L\'axe X du corps.

    -   
        **Axe Y**
        
        : L\'axe Y du corps.

    -   
        **Axe Z**
        
        : L\'axe Z du corps.

    -   
        **Sélectionnez une référence...**
        
        : Sélectionnez une face planaire dans la [Vue 3D](3D_view/fr.md).
-   Cochez la case **Inverser la direction** pour inverser la transformation.
-   Si la case **Réactualiser la vue** est cochée, la vue sera mise à jour en temps réel.

## Limitations

Voir [PartDesign Répétition circulaire](PartDesign_PolarPattern/fr#Limitations.md).





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Mirrored/fr
