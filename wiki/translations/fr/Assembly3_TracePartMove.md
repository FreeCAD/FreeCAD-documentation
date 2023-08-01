---
- GuiCommand:
   Name: Assembly3 TracePartMove
   Name/fr: Assembly3 Tracé du déplacement d'une pièce
   Icon: Assembly_Trace.svg‎‎
   MenuLocation: Assembly3 - Trace part move
   Workbenches: [Assembly3](Assembly3_Workbench/fr.md)
---

# Assembly3 TracePartMove/fr

## Description

La commande <img alt="" src=images/Assembly_Trace.svg  style="width:24px;"> [Tracé du déplacement d\'une pièce](Assembly3_TracePartMove/fr.md) trace un seul point d\'un assemblage cinématique, lorsqu\'un des objets assemblés est déplacé avec l\'outil <img alt="" src=images/Assembly_Move.svg  style="width:16px;"> [Move part](Assembly3_MovePart/fr.md) ou l\'outil <img alt="" src=images/Assembly_AxialMove.svg  style="width:16px;"> [Axial move](Assembly3_AxialMove/fr.md).

## Utilisation

1.  Sélectionnez un objet filaire :
    -   Un point pour se tracer lui-même.
    -   Une arête ou une face pour tracer le point central de sa forme.
2.  Activez la commande <img alt="" src=images/Assembly_Trace.svg  style="width:16px;"> **Trace part move** en utilisant l\'une des méthodes suivantes :
    -   Le bouton **<img src="images/Assembly_Trace.svg" width=16px> [Trace part move](Assembly3_TracePartMove/fr.md)**.
    -   L\'option de menu **Assembly3 → <img src="images/Assembly_Trace.svg" width=16px> Trace part move**.
3.  Sélectionnez un objet de l\'assemblage et déplacez-le en utilisant l\'une des méthodes suivantes :
    -   L\'outil <img alt="" src=images/Assembly_Move.svg  style="width:16px;"> [Move part](Assembly3_MovePart/fr.md).
    -   L\'outil <img alt="" src=images/Assembly_AxialMove.svg  style="width:16px;"> [Axial move](Assembly3_AxialMove/fr.md).
4.  Appuyez sur la touche **Echap** ou sur le bouton **OK** (déplacement axial uniquement) pour terminer le traçage.
5.  Trouvez un objet AsmTrace dans la [Vue en arborescence](Tree_view/fr.md).

## Remarques

-   Si vous ne sélectionnez aucune forme dans la première étape, vous tracerez la forme qui a été sélectionnée dans la troisième étape.
-   Pour changer l\'élément à tracer, vous devez désactiver cet outil avant de sélectionner un nouvel élément et de le réactiver.
-   Si vous contrôlez le mouvement avec un autre outil tel que ce [contrôleur cinématique](Tutorial_KinematicController/fr.md) qui permet d\'utiliser un outil de déplacement en parallèle, vous pouvez utiliser cet outil pour modifier l\'assemblage étape par étape et utiliser l\'outil de déplacement pour ajouter un point et une ligne de connexion à chaque étape. Il est possible d\'utiliser l\'outil de déplacement comme déclencheur en prenant et en faisant glisser l\'une des flèches - juste un tout petit peu jusqu\'à ce que le point et la ligne suivants apparaissent (utilisez la transparence si nécessaire).

:   (J\'espère qu\'il y aura une méthode plus élégante à l\'avenir).



---
⏵ [documentation index](../README.md) > Assembly3 TracePartMove/fr
