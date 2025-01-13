---
 GuiCommand:
   Name: CAM OpActiveToggle
   Name/fr: CAM Activer une opération
   MenuLocation: CAM , Activer/désactiver l'état actif de l'opération
   Workbenches: CAM_Workbench/fr
   Shortcut: **P** **X **
---

# CAM OpActiveToggle/fr

## Description

L\'outil <img alt="" src=images/CAM_OpActiveToggle.svg  style="width:24px;"> [Activer une opération](CAM_OpActiveToggle/fr.md) dans l\'[atelier CAM](CAM_Workbench/fr.md) est utilisé pour activer/désactiver l\'état actif d\'une opération d\'un parcours existante.

Cet outil ne peut être utilisé que si votre <img alt="" src=images/CAM_Job.svg  style="width:24px;"> [tâche](CAM_Job/fr.md) a au moins une opération de parcours.



## Utilisation

1.  Sélectionnez une opération dans le groupe **Opérations** appartenant à une tâche. Une opération désactivée est reconnaissable à son étiquette et à son icône grisées.
2.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/CAM_OpActiveToggle.svg" width=16px> [Activer/désactiver l'état actif de l'opération](CAM_OpActiveToggle/fr.md)**.
    -   Sélectionnez le bouton **CAM → <img src="images/CAM_OpActiveToggle.svg" width=16px> Activer/désactiver l'état actif de l'opération** du menu.
    -   Utilisez le raccourci clavier : **P** puis **X**.
3.  Le résultat dépend de l\'opération sélectionnée :
    -   Si vous avez sélectionné une opération active, la commande la désactive :
        -   L\'icône de l\'opération est remplacée par l\'icône de la commande : <img alt="" src=images/CAM_OpActiveToggle.svg  style="width:16px;">.
        -   L\'icône de l\'opération et le libellé sont grisés.
        -   Les chemins générés par l\'opération disparaissent de la [vue 3D](3D_view/fr.md).
        -   Lorsque vous utilisez l\'outil <img alt="" src=images/CAM_Inspect.svg  style="width:16px;"> [CAM Inspecter des commandes](CAM_Inspect/fr.md) ou de la commande <img alt="" src=images/CAM_Post.svg  style="width:16px;"> [CAM Post-traitement](CAM_Post/fr.md), le code G de l\'opération n\'est pas fourni.
    -   Si vous avez sélectionné une opération désactivée, la commande l\'active :
        -   L\'icône de l\'opération est remplacée par celle appartenant à l\'opération.
        -   L\'icône et le libellé de l\'opération ne sont plus grisés.
        -   Les trajectoires générées par l\'opération sont recalculées et affichées dans la [vue 3D](3D_view/fr.md).
        -   Lorsque vous utilisez l\'outil <img alt="" src=images/CAM_Inspect.svg  style="width:16px;"> [CAM Inspecter des commandes](CAM_Inspect/fr.md) ou de la commande <img alt="" src=images/CAM_Post.svg  style="width:16px;"> [CAM Post-traitement](CAM_Post/fr.md), le G-code de l\'opération est fourni.

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





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM OpActiveToggle/fr
