---
- GuiCommand:/fr
   Name:Mesh AddFacet
   Name/fr:Mesh Ajouter un triangle
   MenuLocation:Maillages → Ajouter un triangle
   Workbenches:[Mesh](Mesh_Workbench/fr.md)
   SeeAlso:[Mesh Remplir les trous](Mesh_FillupHoles/fr.md), [Mesh Boucher un trou](Mesh_FillInteractiveHole/fr.md)
---

## Description

La commande **Mesh Ajouter un triangle** ajoute des faces le long d\'une limite d\'un objet maillé ouvert. Elle peut être utilisée pour remplir des trous.

## Utilisation

1.  Pendant la commande, le mode d\'édition sera actif. Dans ce mode, il est impossible de faire pivoter ou de faire un panoramique de la [vue 3D](3D_view.md) bien que le zoom fonctionne toujours. Mais vous pouvez temporairement sortir du mode d\'édition avec la commande [Std Bascule en mode navigation](Std_ToggleNavigation/fr.md) si vous avez besoin de changer la vue.
2.  Sélectionnez un seul objet maillé ouvert.
3.  Il existe plusieurs façons d\'appeler la commande:
    -   Appuyez sur le bouton **<img src="images/Mesh_AddFacet.svg" width=16px> [Ajouter manuellement un triangle à une face](Mesh_AddFacet/fr.md)**.
    -   Sélectionnez l\'option {{MenuCommand|Maillages → <img src="images/Mesh_AddFacet.svg" width=16px> Ajouter un triangle}} dans le menu.
4.  Si vous survolez un sommet le long d\'une limite du maillage, un marqueur jaune apparaîtra et un clic gauche le sélectionnera.
5.  Sélectionnez deux points supplémentaires pour définir une face triangulaire. L\'ordre des trois points, dans le sens horaire ou antihoraire, détermine la direction de la normale du visage.
6.  Un menu apparaît avec les options suivantes:
    -   
        {{MenuCommand|Add triangle}}
        
        : ajoute la face au maillage.

    -   
        {{MenuCommand|Flip normal}}
        
        : inverse la normale de la face. Après avoir sélectionné cette option, un clic gauche affichera à nouveau le menu.

    -   
        {{MenuCommand|Clear}}
        
        : supprime les points sélectionnés.
7.  Ajoutez éventuellement plus de faces.
8.  Choisissez {{MenuCommand|Finish}} dans le menu contextuel de la vue 3D pour terminer la commande.

## Remarques

Pour une indication plus précise de l\'orientation des faces des objets maillés, assurez-vous que la propriété **Lighting** des objets mesh est définie sur {{Value|One side}}. La couleur de l\'arrière de leurs faces dépendra alors des paramètres de rétroéclairage: {{MenuCommand|Edition → Préférences... → Affichage → Vue 3D → Backlight color - Intensity}}. Voir [Editeur de préférences](Preferences_Editor/fr#Vue_3D.md).





{{Mesh Tools navi

}}  
