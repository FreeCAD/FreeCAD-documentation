---
 GuiCommand:
   Name: Part ColorPerFace
   Name/fr: Part Couleur par face
   MenuLocation: Affichage , Couleur par face
   Workbenches: Part_Workbench/fr, PartDesign_Workbench/fr
   SeeAlso: Std_SetAppearance/fr
---

# Part ColorPerFace/fr

## Description

La commande **Part Couleur par face** définit les propriétés d\'affichage des faces sélectionnées. Pour modifier un objet entier, utilisez plutôt la commande [Std Apparence](Std_SetAppearance/fr.md).

Cette page a été mise à jour pour la version 1.0.

![](images/Part_ColorPerFace_Taskpanel.png ) 
*Le panneau Définir l'apparence par face*



## Utilisation

1.  Sélectionnez un seul objet.
2.  Il y a plusieurs façons de lancer la commande :
    -   Si l\'[atelier Part](Part_Workbench/fr.md) est actif : appuyez sur le bouton **<img src="images/Part_ColorPerFace.svg" width=16px> [Couleur par face](Part_ColorPerFace/fr.md)**.
    -   Sélectionnez l\'option **Affichage → <img src="images/Part_ColorPerFace.svg" width=16px> Couleur par face** du menu.
    -   Sélectionnez l\'option **<img src="images/Part_ColorPerFace.svg" width=16px> Définir l'apparence par face...** dans le menu contextuel de la [vue en arborescence](Tree_view/fr.md).
3.  Le panneau de tâches **Définir l\'apparence par face** s\'ouvre.
4.  Sélectionnez une ou plusieurs faces :
    -   Maintenez la touche **Ctrl** enfoncée pour sélectionner plusieurs faces.
    -   En option, vous pouvez appuyrz sur le bouton **Sélection par une boîte**. Cliquez dans une zone vide et faites glisser un rectangle pour sélectionner toutes les faces appartenant à l\'objet qui se trouvent (partiellement) à l\'intérieur du rectangle. Il est possible de spécifier plusieurs sélections de boîtes.
5.  Effectuez l\'une des opérations suivantes :
    -   Sélectionnez un matériau dans la liste.
        1.  Vous pouvez appuyer sur le bouton **Lancer l'éditeur** pour lancer l\'[éditeur de matériaux](Materials_Edit/fr.md).

        -   Spécifiez une **apparence personnalisée** :

        1.  Appuyez sur le bouton **...**.
        2.  La boîte de dialogue **Propriétés du matériau** s\'ouvre :
            ![](images/Material_Properties_Dialog.png )
        3.  Ces propriétés peuvent être modifiées :
            -   **Couleur ambiante** : couleur des ombres sur l\'objet.
            -   **Couleur diffuse** : couleur réelle/de base de l\'objet.
            -   **Couleur émissive** : couleur de la lumière rayonnant de l\'objet.
            -   **Couleur spéculaire** : couleur du reflet sur une surface brillante de l\'objet.
            -   **Brillance**\'
            -   **Transparence**
        4.  Il est possible d\'appuyer sur le bouton **Réinitialiser** pour modifier l\'apparence et la rendre conforme à celle définie par le matériau.
        5.  Vous pouvez également appuyer sur le bouton **Par défaut** pour modifier l\'apparence afin qu\'elle corresponde aux [préférences](PartDesign_Preferences/fr#Aspect_de_la_forme.md) en cours.
        6.  Appuyez sur le bouton **Fermer** lorsque vous avez terminé.
    -   Appuyez sur le bouton **Définir par défaut** pour modifier l\'apparence en fonction de celle définie par le matériau.
6.  Vous pouvez sélectionner une ou plusieurs nouvelles faces dont vous souhaitez modifier les propriétés.
7.  Appuyez sur le bouton **OK** pour fermer le panneau des tâches et terminer la commande.





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part ColorPerFace/fr
