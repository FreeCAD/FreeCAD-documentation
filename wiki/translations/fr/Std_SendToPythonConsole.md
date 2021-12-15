---
- GuiCommand:/fr
   Name:Std SendToPythonConsole
   Name/fr:Std Vers la console Python
   MenuLocation:Édition → Envoyer vers la console Python
   Workbenches:Tous
   Shortcut:**Ctrl**+**Shift**+**P**
   Version:0.19
---

# Std SendToPythonConsole/fr

## Description

La commande **Std Vers la console Python** crée une variable dans la [console Python](Python_console/fr.md) référençant un objet sélectionné. Si une sous-forme de l\'objet est sélectionnée, deux variables supplémentaires sont créées, l\'une faisant référence à la forme de l\'objet et l\'autre faisant référence à la sous-forme elle-même. Les variables et le code impliqués peuvent être utilisés pour développer du code Python.

>>> ### Begin command Std_SendToPythonConsole
>>> obj = App.getDocument("Unnamed").getObject("Box")
>>> shp = App.getDocument("Unnamed").getObject("Box").Shape
>>> elt = App.getDocument("Unnamed").getObject("Box").Shape.Edge8
>>> ### End command Std_SendToPythonConsole



*Exemple de sortie : un bord de [Part Cube](Part_Box/fr.md) a été sélectionné*

## Utilisation


<div class="mw-translate-fuzzy">

1.  Sélectionnez un seul objet.
2.  Il existe plusieurs façons d\'appeler la commande :
    -   Sélectionnez l\'option **Édition → <img src="images/Std_SendToPythonConsole.svg" width=16px> Envoyer vers la console Python** dans le menu.
    -   Sélectionnez l\'option **<img src="images/Std_SendToPythonConsole.svg" width=16px> Envoyer vers la console Python** dans le menu contextuel de la [vue en arborescence](Tree_view/fr.md) ou le menu contextuel de la [vue 3D](3D_view/fr.md).
    -   Utilisez le raccourci clavier : **Ctrl**+**Shift**+**P**.


</div>





{{Std Base navi

}}

---
[documentation index](../README.md) > Std SendToPythonConsole/fr
