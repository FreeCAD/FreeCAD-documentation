---
 GuiCommand:
   Name: Sketcher ToggleActiveConstraint
   Name/fr: Sketcher Activer les contraintes
   Workbenches: Sketcher_Workbench/fr
   MenuLocation: Esquisse , Contraintes d'esquisse , Activer/désactiver la contrainte
   Shortcut: **K** **Z**
   Version: 0.19
   SeeAlso: Sketcher_ToggleDrivingConstraint/fr
---

# Sketcher ToggleActiveConstraint/fr

## Description

L\'outil <img alt="" src=images/Sketcher_ToggleActiveConstraint.svg  style="width:24px;"> [Sketcher Activer les contraintes](Sketcher_ToggleActiveConstraint/fr.md) active ou désactive les contraintes sélectionnées. La désactivation des contraintes vous permet de tester d\'autres arrangements géométriques sans supprimer les contraintes.

Cet outil est similaire à [Sketcher Contraintes pilotantes](Sketcher_ToggleDrivingConstraint/fr.md), mais contrairement à celui-ci, il fonctionne également pour les contraintes géométriques, et les valeurs des contraintes désactivées de dimension sont préservées.



## Utilisation

1.  Sélectionner une ou plusieurs contraintes.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **[<img src=images/Sketcher_ToggleActiveConstraint.svg style="width:16px"> [Activer/désactiver la contrainte](Sketcher_ToggleActiveConstraint/fr.md)**.

    -   Sélectionnez l\'option **Esquisse → Contraintes d'esquisse → <img src="images/Sketcher_ToggleActiveConstraint.svg" width=16px> Activer/désactiver la contrainte** du menu.

    -   
        {{Version/fr|1.0}}
        
        : cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **<img src="images/Sketcher_ToggleActiveConstraint.svg" width=16px> Activer/désactiver la contrainte** du menu contextuel.

    -   Dans la section **Contraintes** de la [fenêtre de dialogue de l\'esquisse](Sketcher_Dialog/fr.md), sélectionnez l\'option **Activer** ou **Désactiver** du menu contextuel. L\'option proposée dépend de l\'état de la contrainte sous le curseur.

    -   Utiliser le raccourci clavier : **K** puis **Z**.
3.  Les contraintes sélectionnées actives sont désactivées et deviennent grises ([couleur](Sketcher_Preferences/fr#Apparence.md) par défaut), tandis que les contraintes sélectionnées désactivées sont activées et redeviennent rouges (couleur par défaut).



## Exemple

<img alt="" src=images/Sketcher_ToggleActiveConstraint_example_active.png  style="width:400px;"> 
*Une esquisse complètement contrainte.‎*

<img alt="" src=images/Sketcher_ToggleActiveConstraint_example_disabled_1.png  style="width:400px;"> 
*L'une des contraintes angulaires a été désactivée, l'esquisse n'est plus entièrement contrainte.*

<img alt="" src=images/Sketcher_ToggleActiveConstraint_example_disabled_2.png  style="width:400px;"> 
*La géométrie non contrainte peut être déplacée. La contrainte désactivée est toujours disponible et peut être réactivée pour revenir à l'esquisse entièrement contrainte.*



## Script


**Voir aussi :**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Le statut actif d\'une contrainte peut être contrôlé par des [macros](Macros/fr.md) et depuis la [console Python](Python_console/fr.md). 
```python
SketchObject.toggleActive(index)
```

Utilisez la méthode `toggleActive` d\'un [Sketcher SketchObject](Sketcher_SketchObject/fr.md) et `index` de la contrainte pour l\'activer ou la désactiver. L\'index commence de `0` jusqu\'à `N-1`, où `N` est le nombre total de contraintes.

Exemple : 
```python
import FreeCAD as App

sketch = App.ActiveDocument.Sketch
sketch.toggleActive(3)
```





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ToggleActiveConstraint/fr
