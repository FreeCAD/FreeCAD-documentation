---
- GuiCommand:
   Name: Draft SubelementHighlight
   Name/fr: Draft Surbrillance des sous éléments
   MenuLocation: Modification -> Surbrillance des sous éléments
   Workbenches: Draft_Workbench/fr, Arch_Workbench/fr
   Shortcut: **H** **S**
   Version: 0.19
   SeeAlso: Draft_Move/fr, Draft_Rotate/fr, Draft_Scale/fr
---

# Draft SubelementHighlight/fr

## Description

La commande <img alt="" src=images/Draft_SubelementHighlight.svg  style="width:24px;"> **Draft Surligner les sous éléments** met temporairement en évidence les objets sélectionnés ou les objets de base des objets sélectionnés. Elle est destinée à être utilisée en conjonction avec le mode sous-élément de la commande [Draft Déplacer](Draft_Move/fr.md), la commande [Draft Rotation](Draft_Rotate/fr.md) ou la commande [Draft Scale](Draft_Scale/fr.md). Actuellement, le mode sous-élément ne fonctionne correctement que pour les [Draft Lignes](Draft_Line/fr.md) et les [Draft Polylignes](Draft_Wire/fr.md).

![](images/Draft_SubelementHighlight_example.png ) 
*Un Arch mur dont la base, une Draft Polyligne, a été mise en surbrillance.*

## Utilisation

1.  Sélectionnez éventuellement une ou plusieurs [Draft Lignes](Draft_Line/fr.md) ou [Draft Polylignes](Draft_Wire/fr.md), ou des objets dont les objets **Base** sont des [Draft Lignes](Draft_Line/fr.md) ou des [Draft Polylignes](Draft_Wire/fr.md).
2.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Draft_SubelementHighlight.svg" width=16px> [Surbrillance des sous éléments](Draft_SubelementHighlight/fr.md)**.
    -   Sélectionnez l\'option **Modification → <img src="images/Draft_SubelementHighlight.svg" width=16px> Surbrillance des sous-éléments** dans le menu.
    -   Utilisez le raccourci clavier : **H** puis **S**.
3.  Si vous n\'avez pas encore sélectionné d\'objet : sélectionnez un objet dans la [Vue 3D](3D_view/fr.md).
4.  Les objets sélectionnés sont rendus visibles (si nécessaire), leur **Line Color** et **Point Color** deviennent rouges et leur **Point Size** devient {{Value|10}}.
5.  Il est conseillé de désélectionner maintenant la sélection existante, par exemple en cliquant sur un point aléatoire dans la [Vue 3D](3D_view/fr.md).
6.  Sélectionnez un ou plusieurs sous-éléments, arêtes ou points, des objets qui ont été marqués en rouge.
7.  Invoquez [Draft Déplacer](Draft_Move/fr.md), [Draft Rotation](Draft_Rotate/fr.md) ou [Draft Échelle](Draft_Scale/fr.md).
8.  Basculez le mode sous-élément dans le panneau des tâches de cette commande en cochant la case **Modifier les sous-éléments**.
9.  Modifiez les sous-éléments sélectionnés et terminez la commande Draft modify.
10. Appuyez sur **Echap** pour annuler les modifications visuelles temporaires des objets.

## Remarques

-   Si des objets ont été mis en évidence avec cette commande, les modifications visuelles temporaires doivent être annulées avant d\'enregistrer et de rouvrir le fichier.
-   Les objets surlignés ne doivent pas être copiés si le mode sous-élément est désactivé. Les modifications visuelles temporaires ne peuvent pas être annulées pour les copies créées de cette manière.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft SubelementHighlight/fr
