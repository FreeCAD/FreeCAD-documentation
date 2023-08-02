---
- GuiCommand:
   Name: PartDesign_PolarPattern
   Name/fr: PartDesign Répétition circulaire
   MenuLocation: Part Design -> Appliquer une transformation -> Répétition circulaire
   Workbenches: PartDesign_Workbench/fr
   SeeAlso: PartDesign_MultiTransform/fr
---

# PartDesign PolarPattern/fr

## Description

L\'outil <img alt="" src=images/PartDesign_PolarPattern.svg  style="width:24px;"> **PartDesign Répétition circulaire** crée une transformation circulaire d\'une ou plusieurs fonctions.

![](images/PartDesign_PolarPattern_example.png ) 
*Une cavité de forme oblongue (B) réalisée sur une protrusion (A, également appelé support) est utilisée par une transformation circulaire. Le résultat (C) est illustré à droite.*



## Utilisation



### Créer

1.  Vous pouvez [activé](PartDesign_Body#Active_status.md) le bon corps.
2.  Sélectionnez au besoin une ou plusieurs fonctions dans la [Vue en arborescence](Tree_view/fr.md) ou la [Vue 3D](3D_view/fr.md).
3.  Il existe plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/PartDesign_PolarPattern.svg" width=16px> [Répétition circulaire](PartDesign_PolarPattern/fr.md)**.
    -   Sélectionnez l\'option **Part Design → Appliquer une transformation → <img src="images/PartDesign_PolarPattern.svg" width=16px> Répétition circulaire** dans le menu.
4.  S\'il n\'y a pas de corps actif, et qu\'il y a deux corps ou plus dans le document, la boîte de dialogue **Corps actif requis** s\'ouvrira et vous invitera à en activer un. S\'il y a un seul corps, il sera activé automatiquement.
5.  Si aucune fonction n\'a été sélectionnée, le [Panneau des tâches](Task_panel/fr.md) **Ajouter une fonction** s\'ouvre : sélectionnez-en une ou plusieurs (en maintenant la touche **Ctrl**) dans la liste et appuyez sur le bouton **OK**.
6.  Le [Panneau des tâches](Task_panel/fr.md) **Paramètres de la répétition circulaire** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
7.  Appuyez sur le bouton **OK** pour terminer.



### Modifier

1.  Faites l\'une des choses suivantes :
    -   Double-cliquez sur l\'objet PolarPattern dans la [vue en arborescence](Tree_view/fr.md).
    -   Cliquez avec le bouton droit de la souris sur l\'objet PolarPattern dans la [vue en arborescence](Tree_view/fr.md) et sélectionnez **Paramètres de la répétition circulaire** dans le menu contextuel.
2.  Le [panneau des tâches](Task_panel/fr.md) des **Paramètres de la répétition circulaire** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
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
-   S\'il y a plusieurs fonctions dans la transformation, leur ordre peut être important. Voir [Organiser les fonctions](#Organiser_les_fonctions.md).
-   Spécifiez la **Axe** de la transformation :
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
        
        : entrée séparée pour chaque ligne de construction dans l\'esquisse (idem).

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
        
        : sélectionnez une [PartDesign Ligne de référence](PartDesign_Line/fr.md) dans la [vue en arborescence](Tree_view/fr.md) ou une [PartDesign Ligne de référence](PartDesign_Line/fr.md) ou une arête dans la [vue 3D](3D_view/fr.md).
-   Cochez la case **Inverser la direction** pour inverser la transformation.
-   Spécifiez l\'**Angle** à couvrir par la transformation. Si l\'angle est inférieur à 360°, les instances sont réparties uniformément de 0° (première instance) à l\'angle donné (dernière instance). Si l\'angle est un cercle complet de 360°, les instances sont réparties uniformément autour du cercle. Cela signifie que pour n instances, un angle de 360° est équivalent à un angle de 360°\*(1-1/n).
-   Spécifiez le nombre d\'occurrences **Occurrences** (y compris la fonction d\'origine).
-   Si la case **Réactualiser la vue** est cochée, la vue sera mise à jour en temps réel.



## Organiser les fonctions 

Si certaines des fonctions sélectionnées sont additives et d\'autres soustractives, leur ordre peut avoir un impact sur le résultat final. Vous pouvez modifier l\'ordre en faisant glisser les fonctions individuellement dans la liste.

![](images/PartDesign_feature-order.gif ) 
*Effet de l'ordre des fonctionnalités*

## Limitations

-   Toute forme du modèle qui ne recouvre pas la fonction parent sera exclue. Cela garantit qu\'un corps PartDesign est toujours constitué d\'un solide unique et connecté.
-   Les transformations PartDesign ne sont pas encore aussi optimisées que leurs homologues de Draft. Ainsi, pour un grand nombre de pièces, vous devriez envisager d\'utiliser un [Draft Réseau polaire](Draft_PolarArray/fr.md) à la place, combiné à une opération booléenne Part. Cela peut nécessiter des modifications importantes de votre modèle car vous quittez PartDesign et ne pouvez donc pas simplement continuer avec d\'autres fonctions PartDesign dans le même corps. Un exemple est présenté dans [ce sujet du forum](https://forum.freecadweb.org/viewtopic.php?f=3&t=55192).
-   Un modèle ne peut pas être appliqué directement à un autre modèle, qu\'il soit circulaire, linéaire ou symétrique. Pour cela, vous avez besoin d\'une [PartDesign Transformation multiple](PartDesign_MultiTransform/fr.md).





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign PolarPattern/fr
