---
 GuiCommand:
   Name: Draft ToggleGrid
   Name/fr: Draft Basculer la grille
   Workbenches: Draft_Workbench/fr, Arch_Workbench/fr
   Shortcut: **G** **R**
   SeeAlso: Draft_Snap_Grid/fr, Draft_SelectPlane/fr
---

# Draft ToggleGrid/fr

## Description

La commande <img alt="" src=images/Draft_ToggleGrid.svg  style="width:24px;"> **Draft Basculer la grille** change la visibilité de la grille.


{{Version/fr|0.22}}

: chaque [vue 3D](3D_view/fr.md) possède sa propre grille qui peut être soit toujours visible, soit visible uniquement pendant les commandes, soit invisible. La visibilité initiale de la grille dans les nouvelles vues dépend des [préférences](#Préférences.md).



## Utilisation

1.  La commande peut être utilisée lorsqu\'une autre commande est active.
2.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Draft_ToggleGrid.svg" width=16px> [Basculer la grille](Draft_ToggleGrid/fr.md)** dans la barre d\'outils Draft Aimantation.
    -   Appuyez sur le le bouton **<img src="images/Draft_ToggleGrid.svg" width=16px> [Basculer la grille](Draft_ToggleGrid/fr.md)** du [Draft Widget aimantation](Draft_snap_widget/fr.md).
    -   Utilisez le raccourci clavier : **G** puis **R**. Ce raccourci ne peut pas être utilisé si une autre commande est active.
3.  La visibilité de la grille appartenant à la vue 3D courante a changé :
    -   Si aucune autre commande n\'est active :
        -   Si la grille était invisible, elle est maintenant toujours visible.
        -   Si la grille était visible, elle ne l\'est plus, mais la visibilité de la grille pendant les commandes reste inchangée.
    -   Si une autre commande est active :
        -   Si la grille était invisible, elle n\'est plus visible que pendant les commandes.
        -   Si la grille était visible, elle n\'est plus visible pendant les commandes et n\'est plus visible de mnaière permanente.



## Préférences

Voir aussi : [Réglage des préférences](Preferences_Editor/fr.md) et [Draft Préférences](Draft_Preferences/fr.md).

-   Plusieurs préférences de grille sont disponibles : **Édition → Préférences... → Draft → Grille et aimantation → Grille**.
-   Pour conserver la grille lorsque vous passez à d\'autres ateliers, voir [Réglage fin](Fine-tuning/fr#Atelier_Draft.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft ToggleGrid/fr
