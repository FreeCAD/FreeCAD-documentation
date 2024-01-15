---
 GuiCommand:
   Name: Sketcher Clone
   Name/fr: Sketcher Cloner
   MenuLocation: Esquisse , Outils d'esquisse , Cloner
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **Z** **L**
   Version: 0.16
   SeeAlso: Sketcher_Copy/fr, Sketcher_Move/fr
---

# Sketcher Clone/fr

## Description

Clone les éléments d\'esquisse sélectionnés d\'un point à un autre en utilisant le dernier point sélectionné comme référence. Si des contraintes font partie des éléments source, les nouvelles contraintes sont liées aux contraintes source. si les contraintes du source sont modifiées, les contraintes du clone le sont également. Pour éviter ce lien, voir **[<img src=images/Sketcher_Copy.svg style="width:16px"> [Sketcher Copier](Sketcher_Copy/fr.md)**.

Notez qu\'un clone d\'un clone devient une copie de l\'esquisse. Si vous souhaitez créer des contraintes liées, clonez à nouveau les éléments source d\'origine.



## Utilisation

1.  Sélectionner le ou les éléments de l\'esquisse à cloner
2.  Cliquer sur **[<img src=images/Sketcher_Clone.svg style="width:16px"> [Cloner](Sketcher_Clone/fr.md)** ou choisir **Esquisse → Outils d'esquisse  → [<img src=images/Sketcher_Clone.svg style="width:16px"> Cloner** du menu supérieur.
3.  Déplacer la souris dans la [vue 3D](3D_view/fr.md) à l\'emplacement souhaité pour le clone.En maintenant **Maj** enfoncé, l\'angle par rapport au point d\'emplacement peut être fixé par pas de 5°. {{Version/fr|0.20}}
4.  Cliquer avec le bouton gauche de la souris dans la vue 3D pour créer le clone.

Aucune contrainte supplémentaire n\'est ajoutée pour le clone.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Clone/fr
