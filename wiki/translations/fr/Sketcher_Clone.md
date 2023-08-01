---
- GuiCommand:
   Name: Sketcher Clone
   Name/fr: Sketcher Clone
   MenuLocation: Esquisse - Outils d'esquisse - Clone
   Workbenches: [Sketcher](Sketcher_Workbench/fr.md)
   Shortcut: **Z** **L**
   Version: 0.16
   SeeAlso: [Sketcher Copie](Sketcher_Copy/fr.md), [Sketcher Déplacer](Sketcher_Move/fr.md)
---

# Sketcher Clone/fr

## Description

Clone les éléments d\'esquisse sélectionnés d\'un point à un autre en utilisant le dernier point sélectionné comme référence. Si des contraintes font partie des éléments source, les nouvelles contraintes sont liées aux contraintes source. si les contraintes du source sont modifiées, les contraintes du clone le sont également. Pour éviter ce lien, voir **[<img src=images/Sketcher_Copy.svg style="width:16px"> [Sketcher Copie](Sketcher_Copy/fr.md)**.

Notez qu\'un clone d\'un clone devient une copie de l\'esquisse. Si vous souhaitez créer des contraintes liées, clonez à nouveau les éléments source d\'origine.



## Utilisation

1.  Sélectionnez le ou les éléments de l\'esquisse pour l\'opération de clonage
2.  Cliquez sur **[<img src=images/Sketcher_Clone.svg style="width:16px"> [Clone](Sketcher_Clone/fr.md)** ou choisisser **Esquisse → Outils d'esquisse  → [<img src=images/Sketcher_Clone.svg style="width:16px"> Clone** dans le menu du haut.
3.  Déplacez la souris dans la [Vue 3D](3D_view/fr.md) à l\'emplacement souhaité pour le clone.En maintenant **Maj** enfoncé, l\'angle par rapport au point d\'emplacement peut être fixé par pas de 5°. {{Version/fr|0.20}}
4.  Cliquez avec le bouton gauche de la souris dans la vue 3D pour créer le clone.

Aucune contrainte supplémentaire n\'est ajoutée pour le clone.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Clone/fr
