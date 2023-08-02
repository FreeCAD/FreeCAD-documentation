---
- GuiCommand:
   Name: Std Workbench
   Name/fr: Std Atelier
   Empty: 1
   MenuLocation: Affichage -> Atelier
   Workbenches: Workbenches/fr
---

# Std Workbench/fr

## Description

La commande **Std Atelier** active l\'un des [ateliers](Workbenches/fr.md) sélectionné y compris son interface utilisateur graphique (GUI).

<img alt="" src=images/FreeCAD_interface_base_divisions.svg  style="width:800px;"> 
*La liste déroulante d'atelier indiqué par le numéro 10 dans l'[interface](interface/fr.md) standard*



## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande :
    -   Sélectionnez un plan de travail dans la liste déroulante d**\'Ateliers** de la barre d\'outils du plan de travail. Cette option n\'est pas disponible si le plan de travail actuel est `<none>` (pas d\'atelier).
    -   Sélectionnez un atelier dans le sous-menu {{MenuCommand |Affichage → Atelier}}.



## Remarques

-   Des [ateliers externes](External_workbenches/fr.md) supplémentaires peuvent être téléchargés à l\'aide du <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestionnaire des extensions](Std_AddonMgr/fr.md).



## Préférences

-   L\'atelier de démarrage peut être modifié dans les préférences : **Édition → Préférences... → Général → Général → Démarrage**. Voir [Réglage des préférences](Preferences_Editor/fr#G.C3.A9n.C3.A9ral.md).



## Script


**Voir aussi :**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour changer d\'atelier, utilisez la méthode `activateWorkbench` du module FreeCADGui. Cette méthode n\'est pas disponible si FreeCAD est en mode console.


```python
import FreeCADGui

FreeCADGui.activateWorkbench("PartDesignWorkbench")
```





{{Std Base navi

}}  {{Interface navi}}



---
⏵ [documentation index](../README.md) > Std Workbench/fr
