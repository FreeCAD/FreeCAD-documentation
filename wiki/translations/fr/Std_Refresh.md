---
- GuiCommand:/fr
   Name:Std_Refresh
   Name/fr:Std Rafraîchir
   MenuLocation:Edition → Rafraîchir
   Workbenches:Tous
   Shortcut:**F5**
---

# Std Refresh/fr

## Description

La commande **Std Rafraîchir** recalcule le document actif. La commande est désactivée si le document ne nécessite pas de recalcul.



## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande Rafraîchir :
    -   Appuyez sur le bouton **<img src="images/Std_Refresh.svg" width=16px> [Rafraîchir](Std_Refresh/fr.md)** dans la barre d\'outils
    -   Sélectionnez l\'option **Edition → <img src="images/_Std_Refresh.svg" width=16px> Rafraîchir** dans le menu.
    -   Appuyer sur le raccourci clavier **F5**

## Options

-   Pour forcer un recalcul, sélectionnez le document ou un ou plusieurs objets dans la [vue en arborescence](Tree_view/fr.md), choisissez l\'option **<img src="images/Std_MarkToRecompute.svg" width=16px> Marquer pour recalculer** dans le menu contextuel et appelez la commande.
-   Pour les objets, mais pas pour les documents, vous pouvez également choisir **Marquer pour recalculer** dans le même menu contextuel.



## Remarques

-   Pour une macro qui recalculera le document actif, voir : [Macro ForceRecompute](Macro_ForceRecompute/fr.md).



## Script


**Voir aussi :**

[FreeCAD Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

Pour recalculer un document, utilisez la méthode `recompute` de l\'objet document.


```python
import FreeCAD

doc = FreeCAD.newDocument()
doc.recompute()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std Refresh/fr
