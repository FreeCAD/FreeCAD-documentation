---
- GuiCommand:
   Name:PartDesign_LinearPattern
   Name/fr:PartDesign Répétition linéaire
   MenuLocation:Part Design → Appliquer une transformation → Répétition linéaire
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   SeeAlso:[PartDesign Transformation multiple](PartDesign_MultiTransform/fr.md)
---

# PartDesign LinearPattern/fr

## Description

L\'outil <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:24px;"> **PartDesign Répétition linéaire** crée une transformation linéaire d\'une ou plusieurs fonctions.

![](images/PartDesign_LinearPattern_example.svg ) 
*Ci-dessus, une protrusion en forme de L (B) créée sur le dessus de la protrusion de base (A, aussi dénommée "support") est utilisée dans une répétition linéaire. Le résultat (C) est affiché à droite.*



## Utilisation



### Créer

1.  Vous pouvez [activé](PartDesign_Body#Active_status.md) le bon corps.
2.  Sélectionnez au besoin une ou plusieurs fonctions dans la [vue en arborescence](Tree_view/fr.md) ou la [vue 3D](3D_view/fr.md).
3.  Il existe plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/PartDesign_LinearPattern.svg" width=16px> [Répétition linéaire](PartDesign_LinearPattern/fr.md)**.
    -   Sélectionnez l\'option **Part Design → Appliquer une transformation → <img src="images/PartDesign_LinearPattern.svg" width=16px> Répétition linéaire** dans le menu.
4.  S\'il n\'y a pas de corps actif, et qu\'il y a deux corps ou plus dans le document, la boîte de dialogue **Corps actif requis** s\'ouvrira et vous invitera à en activer un. S\'il y a un seul corps, il sera activé automatiquement.
5.  Si aucune fonction n\'a été sélectionnée, le [panneau des tâches](Task_panel/fr.md) **Ajouter une fonction** s\'ouvre : sélectionnez-en une ou plusieurs (en maintenant la touche **Ctrl**) dans la liste et appuyez sur le bouton **OK**.
6.  Le [panneau des tâches](Task_panel/fr.md) **Paramètres de la répétition linéaire** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
7.  Appuyez sur le bouton **OK** pour terminer.



### Éditer

1.  Faites l\'une des choses suivantes :
    -   Double-cliquez sur l\'objet Draft dans la [vue en arborescence](Tree_view/fr.md).
    -   Cliquez avec le bouton droit de la souris sur l\'objet Draft dans la [vue en arborescence](Tree_view/fr.md) et sélectionnez **Paramètres de la répétition linéaire** dans le menu contextuel.
2.  Le [panneau des tâches](Task_panel/fr.md) des **Paramètres de la répétition linéaire** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
3.  Appuyez sur le bouton **OK** pour terminer.

## Options

-   Pour ajouter des fonctions :
    1.  Appuyez sur le bouton **Ajouter une fonction**.
    2.  Sélectionnez une fonction dans la [vue en arborescence](Tree_view/fr.md) ou la [vue 3D](3D_view/fr.md).
    3.  Répétez l\'opération pour ajouter d\'autres fonctions.
-   Pour supprimer des fonctions :
    1.  Appuyez sur le bouton **Supprimer une fonction**.
    2.  Effectuez l\'une des opérations suivantes :
        -   Sélectionnez une fonction dans la [vue en arborescence](Tree_view/fr.md) ou la [vue 3D](3D_view/fr.md).
        -   Sélectionnez une fonction dans la liste et appuyez sur la touche **Suppr**.
        -   Cliquez avec le bouton droit de la souris sur une fonction de la liste et sélectionnez **Enlever** dans le menu contextuel.
    3.  Répétez l\'opération pour supprimer d\'autres fonctions.
-   S\'il y a plusieurs fonctions dans le modèle, leur ordre peut être important. Voir [PartDesign Répétition circulaire](PartDesign_PolarPattern/fr#Organiser_les_fonctions.md).
-   Spécifiez la **Direction** de la transformation :
    -   
        **Axe normal à l'esquisse**
        
        : axe Z de l\'esquisse (disponible uniquement pour les fonctions basées sur l\'esquisse).

    -   
        **Axe d'esquisse vertical**
        
        : axe Y de l\'esquisse (idem).

    -   
        **Axe d'esquisse horizontal**
        
        : axe X de l\'esquisse (idem).

    -   
        **Ligne de construction #**
        
        : une entrée séparée pour chaque ligne de construction dans l\'esquisse (idem).

    -   
        **Axe X**
        
        : axe X du corps.

    -   
        **Axe Y**
        
        : axe Y du corps.

    -   
        **Axe Z**
        
        : axe Z du corps.

    -   
        **Sélectionnez une référence...**
        
        : sélectionnez une [PartDesign Ligne de référence](PartDesign_Line/fr.md) dans la [Vue en arborescence](Tree_view/fr.md) ou une [PartDesign Ligne de référence](PartDesign_Line/fr.md) ou une arête dans la [vue 3D](3D_view/fr.md).
-   Cochez la case **Inverser la direction** pour inverser la transformation.
-   Spécifiez la **Longueur** à couvrir par la transformation.
-   Spécifiez le nombre d\'occurrences **Occurrences** (y compris la fonction d\'origine).
-   Si la case **Réactualiser la vue** est cochée, la vue sera mise à jour en temps réel.

## Limitations

Voir [PartDesign Répétition circulaire](PartDesign_PolarPattern/fr#Limitations.md).





{{PartDesign Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign LinearPattern/fr
