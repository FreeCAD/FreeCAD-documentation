---
- GuiCommand:
   Name: Path OpActiveToggle
   Name/fr: Path Activer une opération
   MenuLocation: Path -> Activer/désactiver l'état actif de l'opération
   Workbenches: Path_Workbench/fr
   Shortcut: **P** **X **
---

# Path OpActiveToggle/fr

## Description

L\'outil <img alt="" src=images/Path_OpActiveToggle.svg  style="width:24px;"> [Activer une opération](Path_OpActiveToggle/fr.md) dans l\'[atelier Path](Path_Workbench/fr.md) est utilisé pour basculer l\'état actif d\'une opération d\'un parcours existante. Cet outil n\'est pas disponible, indiqué par une version gris clair de l\'icône, tant que vous n\'avez pas créé une ou plusieurs opérations de parcours. Une fois que votre <img alt="" src=images/Path_Job.svg  style="width:24px;"> [tâche](Path_Job/fr.md) a au moins une opération de parcours, l\'icône sera entièrement colorée, indiquant qu\'elle est disponible.



## Utilisation

1.  Sélectionnez une opération dans le groupe **Opérations** appartenant à une tâche. Une opération désactivée est reconnaissable à son étiquette et à son icône grisées.
2.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Path_OpActiveToggle.svg" width=16px> [Activer/désactiver l'état actif de l'opération](Path_OpActiveToggle/fr.md)**.
    -   Sélectionnez le bouton **Path → <img src="images/Path_OpActiveToggle.svg" width=16px> Activer/désactiver l'état actif de l'opération** dans le menu.
    -   Utilisez le raccourci clavier : **P** puis **X**.
3.  Le résultat dépend de l\'opération sélectionnée :
    -   Si vous avez sélectionné une opération active, la commande la désactive :
        -   L\'icône de l\'opération est remplacée par l\'icône de la commande : <img alt="" src=images/Path_OpActiveToggle.svg  style="width:16px;">.
        -   L\'icône de l\'opération et le libellé sont grisés.
        -   Les chemins générés par l\'opération disparaissent de la [vue 3D](3D_view/fr.md).
        -   Lorsque vous utilisez l\'outil <img alt="" src=images/Path_Inspect.svg  style="width:16px;"> [Path Inspecter des commandes](Path_Inspect/fr.md) ou de la commande <img alt="" src=images/Path_Post.svg  style="width:16px;"> [Path Post-traitement](Path_Post/fr.md), le code G de l\'opération n\'est pas fourni.
    -   Si vous avez sélectionné une opération désactivée, la commande l\'active :
        -   L\'icône de l\'opération est remplacée par celle appartenant à l\'opération.
        -   L\'icône et le libellé de l\'opération ne sont plus grisés.
        -   Les trajectoires générées par l\'opération sont recalculées et affichées dans la [vue 3D](3D_view/fr.md).
        -   Lorsque vous utilisez l\'outil <img alt="" src=images/Path_Inspect.svg  style="width:16px;"> [Path Inspecter des commandes](Path_Inspect/fr.md) ou de la commande <img alt="" src=images/Path_Post.svg  style="width:16px;"> [Path Post-traitement](Path_Post/fr.md), le G-code de l\'opération est fourni.

## Options

Vide



## Propriétés

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
⏵ [documentation index](../README.md) > [Path](Path_Workbench.md) > Path OpActiveToggle/fr
