---
- GuiCommand:/fr
   Name:Path OpActiveToggle
   Name/fr:Path Activation de l'opération
   MenuLocation:Path → Activer/désactiver l'état actif de l'opération
   Workbenches:[Path](Path_Workbench/fr.md)
   Shortcut:**P** **X **
---

# Path OpActiveToggle/fr

## Description

L\'outil **<img src="images/Path_OpActiveToggle.svg" width=24px> _ a au moins une opération de chemin, l\'icône passe colorée indiquant qu\'elle est disponible pour utilisation.

## Utilisation

1.  Sélectionnez une opération dans le groupe **Opérations** appartenant à un travail. Une opération désactivée est reconnaissable à son étiquette et à son icône grisées.
2.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Path_OpActiveToggle.svg" width=16px> [Activer/désactiver l'état actif de l'opération](Path_OpActiveToggle/fr.md)**.
    -   Sélectionnez le bouton **Path → <img src="images/Path_OpActiveToggle.svg" width=16px> Activer/désactiver l'état actif de l'opération** dans le menu.
    -   Utilisez le raccourci clavier : **P** puis **X**.
3.  Le résultat dépend de l\'opération sélectionnée :
    -   Si vous avez sélectionné une opération active, la commande la désactive :
        -   L\'icône de l\'opération est remplacée par l\'icône de la commande : <img alt="" src=images/Path_OpActiveToggle.svg  style="width:16px;">.
        -   L\'icône de l\'opération et le libellé sont grisés.
        -   Les chemins générés par l\'opération disparaissent de la [Vue 3D](3D_view/fr.md).
        -   Lorsque vous utilisez l\'outil <img alt="" src=images/Path_Inspect.svg  style="width:16px;"> _, le code G de l\'opération n\'est pas fourni.
    -   Si vous avez sélectionné une opération désactivée, la commande l\'active :
        -   L\'icône de l\'opération est remplacée par celle appartenant à l\'opération.
        -   L\'icône et le libellé de l\'opération ne sont plus grisés.
        -   Les trajectoires générées par l\'opération sont recalculées et affichées dans la [Vue 3D](3D_view/fr.md).
        -   Lorsque vous utilisez l\'outil <img alt="" src=images/Path_Inspect.svg  style="width:16px;"> _, le G-code de l\'opération est fourni.

## Options

Vide

## Propriétés

### Données

Vide

### Vue

Vide

## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Exemple :


```python
#Place code example here.
```





{{Path_Tools_navi

}}

---
[documentation index](../README.md) > [Path](Path_Workbench.md) > Path OpActiveToggle/fr
