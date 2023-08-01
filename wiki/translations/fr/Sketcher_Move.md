---
- GuiCommand:/fr
   Name:Sketcher Move
   Name/fr:Sketcher Déplacer
   MenuLocation:Esquisse → Outils d'esquisse → Déplacer
   Workbenches:[Sketcher](Sketcher_Workbench/fr.md)
   Shortcut:**Z** **M**
   Version:0.18
   SeeAlso:[Sketcher Clone](Sketcher_Clone/fr.md), [Sketcher Copie](Sketcher_Copy/fr.md)
---

# Sketcher Move/fr

## Description

Déplace les éléments d\'esquisse sélectionnés d\'un point à un autre, en utilisant le dernier point sélectionné comme référence.

![](images/sketcher_move.png‎ ) 
*La séquence de clics est indiquée par des flèches jaunes numérotées.<br>
Sélectionner l'élément '''A'''. Une ligne vectorielle indiquée par deux lignes rouges à partir du point pivot '''A''' pointant vers le numéro de la position de la souris en '''2''' apparait.<br>
Déplacer le pointeur de la souris sur l'emplacement de la cible '''3'''. L'élément en '''B''' est auto-contraint au point '''3'''.*



## Utilisation

1.  Sélectionnez les éléments d\'esquisse pour l\'opération de déplacement.
2.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **[<img src=images/Sketcher_Move.svg style="width:16px"> [Déplacer](Sketcher_Move/fr.md)** de la barre d\'outils
    -   Utilisez les raccourcis clavier **Z** puis **M**
    -   Utilisez l\'entrée **Esquisse → Outils d'esquisse → [<img src=images/Sketcher_Move.svg style="width:16px"> Déplacer** du menu
3.  Déplacez la souris dans la [Vue 3D](3D_view/fr.md) à l\'endroit souhaité.En maintenant **Ctrl** enfoncé (**Cmd** pour macOS), l\'angle par rapport à l\'emplacement peut être fixé par pas de 5°. {{Version/fr|0.20}}
4.  Cliquez avec le bouton gauche de la souris dans la vue 3D pour terminer le déplacement. Les contraintes existantes se déplacent également.
5.  Si vous voulez détacher un élément et le déplacer librement, supprimez ses contraintes de verrouillage et faites-le glisser avec la souris.





{{Sketcher_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Move/fr
