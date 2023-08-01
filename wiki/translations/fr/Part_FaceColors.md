---
- GuiCommand:/fr
   Name:Part FaceColors
   Name/fr:Part Définir les couleurs
   MenuLocation:Menu contextuel → Définir les couleurs...
   Workbenches:[Part](Part_Workbench/fr.md), [PartDesign](PartDesign_Workbench/fr.md)
   SeeAlso:[Std Apparence](Std_SetAppearance/fr.md)
---

# Part FaceColors/fr

## Description

La fonction **Définir les couleurs** vous permet de définir une couleur pour chaque face ou surface d\'un objet. De cette façon, vous pouvez attribuer plusieurs couleurs à une pièce. Pour colorer des pièces entières, utilisez à la place la fonction *[Std Apparence](Std_SetAppearance/fr.md)*.

## Utilisation

Pour colorier les faces :

1.  Faites un clic droit sur un objet dans la [Vue en arborescence](Tree_view/fr.md). Si l\'objet supporte la fonctionnalité *FaceColors*, il y a une entrée de menu contextuel **Set colors\...** et vous pouvez cliquer dessus.
2.  Pour sélectionner une ou plusieurs faces :
    -   Pour une seule face, cliquez simplement dessus.
    -   Pour sélectionner plusieurs faces :
        -   Maintenez **Ctrl** enfoncé et cliquez sur plusieurs faces.
        -   Ou cliquez sur le bouton **Sélection par boîte** dans le panneau des tâches. Vous pouvez alors faire glisser un rectangle de sélection dans la [Vue 3D](3D_view/fr.md) avec la souris. Chaque face qui se trouve partiellement à l\'intérieur du rectangle sera sélectionnée.
3.  Choisissez une couleur pour les faces sélectionnées dans le panneau des tâches. {{Version/fr|0.20}} : la couleur peut également être rendue transparente en définissant le *Canal alpha*.
4.  Cliquez sur le bouton **OK** pour fermer le panneau des tâches et accepter les modifications.

Pour réinitialiser toutes les couleurs de la face :

1.  Cliquez sur **Définir par défaut**. Cela définit les couleurs de toutes les faces de la pièce à la couleur par défaut. Le bouton fonctionne instantanément, c\'est-à-dire que vous ne pouvez pas revenir en arrière avec le bouton **Annuler**.

![](images/Part_FaceColors-dialog.png ) 
*Le panneau des tâches Définir la couleur des faces*



---
![](images/Button_right.svg) [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > [Command_Reference](Category_Command_Reference.md) > [Part](Part_Workbench.md) > Part FaceColors/fr
