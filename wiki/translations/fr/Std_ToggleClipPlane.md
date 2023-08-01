---
- GuiCommand:
   Name:Std ToggleClipPlane
   Name/fr:Std Basculer le plan de coupe
   MenuLocation:Affichage → Plan de coupe
   Workbenches:Tous
   SeeAlso:[Part Coupe persistante](Part_SectionCut/fr.md)
---

# Std ToggleClipPlane/fr

## Description

La commande **Std Basculer le plan de coupe** permet de masquer temporairement les objets et leurs parties sur un côté d\'un maximum de trois plans virtuels dans la [vue 3D](3D_view/fr.md) active.

![](images/Std_ToggleClipPlane_example.png ) 
*Un objet creux coupé*

![](images/Std_ToggleClipPlane_Dialog.png ) 
*La boite de dialogue Découpage*



## Utilisation

1.  Sélectionnez l\'option **Affichage → <img src="images/Std_ToggleClipPlane.svg" width=16px> Plan de coupe** dans le menu.
2.  Dans La boite de dialogue Découpage, effectuez l\'une des opérations suivantes :
    -   Cochez une ou plusieurs des cases {{CheckBox|TRUE|Découpage suivant X}} à {{CheckBox|TRUE|Découpage suivant Z}}.
        -   Modifiez éventuellement la ou les distances de décalage.
        -   Appuyez éventuellement sur le bouton **Retourner** pour changer le côté du plan de détourage où les objets sont masqués.
    -   Cochez la case {{CheckBox|TRUE|Découpage suivant une direction personnalisée}}.
        -   Modifiez éventuellement la distance de décalage.
        -   Effectuez l\'une des actions suivantes :
            -   Appuyez sur le bouton **Vue** pour utiliser la direction de la vue en cours.
            -   Cochez la case {{CheckBox|TRUE|Ajuster la direction de la vue}} pour une direction qui s\'adapte dynamiquement et afficher les changements.
            -   Spécifiez la direction en entrant les coordonnées X, Y et Z d\'un vecteur normal.
3.  Modifiez éventuellement la vue pour inspecter le modèle.
4.  Appuyez sur le bouton **Fermer** pour fermer le panneau des tâches et terminer la commande.



## Remarques

-   Pour distinguer clairement l\'intérieur des objets partiellement coupés, changez leur propriété **Lighting** en \"One side\". La couleur du côté intérieur de leurs surfaces dépendra alors des paramètres de rétroclairage : **Édition → Préférences... → Affichage → Vue 3D → Couleur du rétroéclairage - Intensité**. Voir [Éditeur de préférences](Preferences_Editor/fr#Vue_3D.md).





{{Std_Base_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std ToggleClipPlane/fr
