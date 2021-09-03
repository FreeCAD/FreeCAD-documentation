---
- GuiCommand:/fr
   Name:Path OpActiveToggle
   Name/fr:Path Activation de l'opération
   MenuLocation:Path → Activer/désactiver l'état actif de l'opération
   Workbenches:[Path](Path_Workbench/fr.md)
   Shortcut:**P** **X **
   SeeAlso:
---


</div>

## Description

L\'outil **<img src="images/Path_OpActiveToggle.svg" width=24px> [Path Activation de l'opération](Path_OpActiveToggle/fr.md)** dans l\'[Atelier Path](Path_Workbench/fr.md) est utilisé pour basculer l\'état actif d\'une opération de chemin existante. Cet outil n\'est pas disponible, icône gris clair, tant que vous n\'avez pas créé une ou plusieurs opérations de chemin. Une fois que votre <img alt="" src=images/Path_Job.svg  style="width:24px;"> [Path Tâche](Path_Job/fr.md) a au moins une opération de chemin, l\'icône passe colorée indiquant qu\'elle est disponible pour utilisation.

## Utilisation


<div class="mw-translate-fuzzy">

1.  Sélectionnez une opération dans le groupe \"Opérations\" d\'un travail.
2.  Cliquez sur l\'icône de la bascule **<img src="images/Path_OpActiveToggle.svg" width=16px> [Activer/désactiver l'état actif de l'opération](Path_OpActiveToggle/fr.md)**.
3.  Lorsque vous désactivez une opération, vous remarquerez:
    -   Le titre de l\'opération et l\'icône qui le précède deviennent gris clair.
    -   L\'icône devant l\'étiquette de l\'opération sera remplacée par celle de l\'icône <img alt="" src=images/Path_OpActiveToggle.svg  style="width:16px;"> Activation d\'opération.
    -   Les chemins générés à partir de l\'opération disparaîtront de la fenêtre.
    -   Lors de l\'utilisation de l\'outil **<img src="images/Path_Inspect.svg" width=16px> [Path Inspecte le G-Code...](Path_Inspect/fr.md)** ou **<img src="images/Path_PostProcess.svg" width=16px> [Path Post-traitement...](Path_Post/fr.md)**, aucun G-Code ne sera fourni à partir de l\'opération désactivée.


</div>


<div class="mw-translate-fuzzy">

## Options

Vide


</div>

Empty

## Propriétés


<div class="mw-translate-fuzzy">

### Données

Vide


</div>

Empty


<div class="mw-translate-fuzzy">

### Vue

Vide


</div>

Empty


<div class="mw-translate-fuzzy">

## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).


</div>


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).


<div class="mw-translate-fuzzy">

Exemple: 
```python#Place code example here.```


</div>


```python
#Place code example here.
```


<div class="mw-translate-fuzzy">





</div>


{{Path_Tools_navi

}} 
