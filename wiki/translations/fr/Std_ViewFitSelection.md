---
- GuiCommand:
   Name: Std ViewFitSelection
   Name/fr: Std Affiche la sélection
   MenuLocation: Affichage ->  Vues standards -> Affiche la sélection
   Workbenches: Tous
   Shortcut: **V** **S**
   SeeAlso: Std_ViewFitAll/fr
---

# Std ViewFitSelection/fr



## Description

La commande **Std Affiche la sélection** effectue un zoom et un panoramique sur la vue de sorte que tous les objets sélectionnés tiennent à l\'intérieur de la [vue 3D](3D_view/fr.md) active. Cette commande est utile dans les cas où, pour une raison quelconque, les objets se trouvent au-delà des limites de la vue 3D en cours ou ne peuvent pas être facilement trouvés à l\'aide de la [navigation 3D](Mouse_navigation/fr.md).



## Utilisation

1.  Sélectionnez un ou plusieurs objets.
2.  Il existe plusieurs façons d\'appeler la commande :
    -   Appuyez sur le bouton **<img src="images/Std_ViewFitSelection.svg" width=16px> [Affiche la sélection](Std_ViewFitSelection/fr.md)**.
    -   Sélectionnez l\'option **Affichage →  Vues standards → <img src="images/Std_ViewFitSelection.svg" width=16px> Affiche la sélection** du menu.
    -   Sélectionnez l\'option **<img src="images/Std_ViewFitSelection.svg" width=16px> Affiche la sélection** dans le menu contextuel de la [vue 3D](3D_view/fr.md).
    -   Utilisez le raccourci clavier : **V** then **S**.



## Script


**Voir aussi :**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour changer la vue en \"Afficher la sélection\", la méthode `SendMsgToActiveView` de l\'objet FreeCADGui peut être utilisée. Cette méthode n\'est pas disponible si FreeCAD est en mode console.


```python
import FreeCADGui

FreeCADGui.SendMsgToActiveView('ViewSelection')
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ViewFitSelection/fr
