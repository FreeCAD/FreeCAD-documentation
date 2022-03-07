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

La commande **Std Vers la console Python** crée des variables dans la [console Python](Python_console/fr.md) référençant un objet sélectionné et ses sous-formes sélectionnées, ainsi que d\'autres références utiles. Les variables et le code impliqué peuvent être utilisés dans le développement du code Python.

Les variables suivantes sont créées en fonction de l\'objet sélectionné et des sous-formes sélectionnées, le cas échéant :

+++
| Nom de la variable | Objet(s) référencé(s)                                                                                                                                     |
+====================+===========================================================================================================================================================+
|     | Le document contenant l\'objet sélectionné                                                                                                                |
| {{Incode|doc}}     |                                                                                                                                                           |
|                 |                                                                                                                                                           |
+++
|     | L\'objet Lien sélectionné (créé uniquement si l\'objet sélectionné est un Lien)                                                                           |
| {{Incode|lnk}}     |                                                                                                                                                           |
|                 |                                                                                                                                                           |
+++
|     | En fonction de l\'objet sélectionné :                                                                                                                     |
| {{Incode|obj}}     | L\'objet sélectionné lui-même (si l\'objet sélectionné n\'est pas un lien).                                                                               |
|                 | L\'objet lié (si l\'objet sélectionné est un lien)                                                                                                        |
+++
|     | Selon le type de {{Incode|obj}} :                                                                                                           |
| {{Incode|shp}}     | La propriété {{Incode|Shape}} de {{Incode|obj}} (pour les objets dérivés de la classe {{Incode|Part::Feature}}) |
|                 | La propriété {{Incode|Mesh}} de {{Incode|obj}} (pour les objets Mesh)                                                         |
|                    | La propriété {{Incode|Points}} de {{Incode|obj}} (pour les objets Points)                                                     |
+++
|     | La première sous-forme sélectionnée (créée uniquement si au moins une sous-forme est sélectionnée)                                                        |
| {{Incode|sub}}     |                                                                                                                                                           |
|                 |                                                                                                                                                           |
+++
|     | Une liste contenant toutes les formes secondaires (créée uniquement si deux formes secondaires ou plus sont sélectionnées)                                |
| {{Incode|subs}}    |                                                                                                                                                           |
|                 |                                                                                                                                                           |
+++

>>> ### Begin command Std_SendToPythonConsole
>>> try:
>>>     del(doc,lnk,obj,shp,sub,subs)
>>> except Exception:
>>>     pass
>>> 
>>> doc = App.getDocument("Unnamed")
>>> lnk = doc.getObject("Link")
>>> obj = lnk.getLinkedObject()
>>> shp = obj.Shape
>>> sub = obj.getSubObject("Edge10")
>>> subs = [obj.getSubObject("Edge10"),obj.getSubObject("Face3"),obj.getSubObject("Vertex5"),]
>>> ### End command Std_SendToPythonConsole



*Exemple de sortie : un bord, une face et un sommet d'un [Lien](Std_LinkMake/fr.md) vers un [Part Cube](Part_Box/fr.md) ont été sélectionnés*

## Utilisation

1.  Sélectionnez un seul objet ou une ou plusieurs sous-formes appartenant à un seul objet.
2.  Il existe plusieurs façons d\'appeler la commande :
    -   Sélectionnez l\'option **Édition → <img src="images/Std_SendToPythonConsole.svg" width=16px> Envoyer vers la console Python** dans le menu.
    -   Sélectionnez l\'option **<img src="images/Std_SendToPythonConsole.svg" width=16px> Envoyer vers la console Python** dans le menu contextuel de la [vue en arborescence](Tree_view/fr.md) ou le menu contextuel de la [vue 3D](3D_view/fr.md).
    -   Utilisez le raccourci clavier : **Ctrl**+**Shift**+**P**.
3.  Si nécessaire, la [console Python](Python_console/fr.md) s\'ouvre.
4.  La [console Python](Python_console/fr.md) reçoit le focus du clavier.

## Remarques

-   Toutes les variables précédemment créées sont supprimées à chaque fois que la commande est exécutée.





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std SendToPythonConsole/fr
