---
 GuiCommand:
   Name: Std ToggleClipPlane
   Name/fr: Std Couper selon des plans
   MenuLocation: Affichage , Couper selon des plans
   Workbenches: Tous
   SeeAlso: Part_SectionCut/fr
---

# Std ToggleClipPlane/fr

## Description

La commande **Std Couper selon des plans** permet de masquer temporairement les objets et leurs parties sur un côté d\'un maximum de trois plans virtuels dans la [vue 3D](3D_view/fr.md) active.

![](images/Std_ToggleClipPlane_example.png ) 
*Un objet creux coupé*

![](images/Std_ToggleClipPlane_Dialog.png ) 
*La boite de dialogue Couper selon des plans*



## Utilisation

1.  Sélectionnez l\'option **Affichage → <img src="images/Std_ToggleClipPlane.svg" width=16px> Couper selon des plans** du menu.
2.  Dans La boite de dialogue Découpage, effectuez l\'une des opérations suivantes :
    -   Cochez une ou plusieurs des cases {{CheckBox|TRUE|Découpage suivant X}} à {{CheckBox|TRUE|Couper suivant Z}}.
        -   Vous pouvez modifier la ou les distances de décalage.
        -   Vous pouvez modifier appuyer sur le bouton **Retourner** pour changer le côté du plan de découpe où les objets sont masqués.
    -   Cochez la case {{CheckBox|TRUE|Couper suivant une direction personnalisée}}.
        -   Vous pouvez modifier la distance de décalage.
        -   Effectuez l\'une des actions suivantes :
            -   Appuyez sur le bouton **Vue** pour utiliser la direction de la vue en cours.
            -   Cochez la case {{CheckBox|TRUE|Ajuster la direction de la vue}} pour une direction qui s\'adapte dynamiquement et afficher les changements.
            -   Spécifiez la direction en entrant les coordonnées X, Y et Z d\'un vecteur normal.
3.  Vous pouvez modifier la vue pour inspecter le modèle.
4.  Appuyez sur le bouton **Fermer** pour fermer le panneau des tâches et terminer la commande.



## Remarques

-   Pour distinguer clairement l\'intérieur des objets partiellement coupés, changez leur propriété **Lighting** en \"One side\". La couleur du côté intérieur de leurs surfaces dépendra alors des paramètres de rétroclairage : **Édition → Préférences... → Affichage → Vue 3D → Couleur du rétroéclairage - Intensité**. Voir [Éditeur de préférences](Preferences_Editor/fr#Vue_3D.md).





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std ToggleClipPlane/fr
