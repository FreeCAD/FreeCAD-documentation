---
- GuiCommand:
   Name: Assembly3 LockMover
   Name/fr: Assembly3 Verrouiller le déplacement
   Icon: Assembly_LockMover.svg‎‎
   MenuLocation: Assembly3 -> Lock mover
   Workbenches: Assembly3_Workbench/fr
---

# Assembly3 LockMover/fr

## Description

La commande <img alt="" src=images/Assembly_LockMover.svg  style="width:24px;"> [Verrouiller le déplacement](Assembly3_LockMover/fr.md) est une commande qui empêche les pièces d\'être déplacées si elles sont fixées avec une contrainte de <img alt="" src=images/Assembly_ConstraintLock.svg  style="width:16px;"> [verrouillage](Assembly3_ConstraintLock/fr.md).

Lorsqu\'elle est activée, aucune des commandes de déplacement <img alt="" src=images/Assembly_Move.svg  style="width:16px;"> [Déplacer une pièce](Assembly3_MovePart/fr.md), <img alt="" src=images/Assembly_AxialMove.svg  style="width:16px;"> [Déplacement axial](Assembly3_AxialMove/fr.md), ou <img alt="" src=images/Assembly_QuickMove.svg  style="width:16px;"> [Déplacement rapide](Assembly3_QuickMove/fr.md) peuvent être sélectionnés tant que la sélection en cours contient un objet fixe. Cela ne semble pas s\'appliquer à la géométrie 2D (voir [Remarques](#Remarques.md)).

## Utilisation

1.  Activez la commande <img alt="" src=images/Assembly_LockMover.svg  style="width:16px;"> **Verrouiller le déplacement** en utilisant l\'un des moyens suivants :
    -   Le bouton **<img src="images/Assembly_LockMover.svg" width=16px> [Lock mover](Assembly3_LockMover/fr.md)**.
    -   L\'option de menu **Assembly3 → <img src="images/Assembly_LockMover.svg" width=16px> Lock mover**.

## Remarques

La **géométrie 2D** sélectionnée, telle que les Draft lignes, les arcs et les cercles, fixée par la contrainte Locked, ne désactive pas les outils de déplacement. Alors que les cercles et les arcs conservent leur position lorsqu\'un outil de déplacement leur est appliqué, les lignes peuvent être déplacées et inclinées.



---
⏵ [documentation index](../README.md) > Assembly3 LockMover/fr
