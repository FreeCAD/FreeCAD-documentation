---
- GuiCommand:/fr
   Name:Std TextDocument
   Name/fr:Std Ajouter un document texte
   MenuLocation:Outils → Ajouter un document texte
   Workbenches:Tous
   Version:0.19
   SeeAlso:[Draft Formes à partir de texte](Draft_ShapeString/fr.md), [Draft Texte](Draft_Text.md)
---

# Std TextDocument/fr

## Description

La commande **Std Ajouter un document texte** crée un objet capable de contenir du texte arbitraire. Cet élément peut être utilisé pour écrire des informations générales ou de la documentation sur le modèle.

## Utilisation

1.  Sélectionnez l\'option {{StdMenu|Outils → Ajouter un document texte}} dans le menu
2.  Double-cliquez sur l\'objet nouvellement créé dans la [vue en arborescence](tree_view/fr.md) pour ouvrir un onglet dans lequel écrire du texte.
3.  Ajouter du texte.
4.  Fermez l\'onglet et enregistrez le fichier lorsque vous y êtes invité.

## Propriétés

### Vue


{{TitleProperty|Editor}}

-    {{PropertyView/fr|Font Name|Font}}: un nom de police, par exemple, {{Value|Ubuntu Mono}}.

-    {{PropertyView/fr|Font Size|Float}}: une taille de police en points, par exemple, {{Value|11}}.

-    {{PropertyView/fr|Read Only|Bool}}: par défaut `False`. Mis à `True`, le texte ne peut pas être modifié tant que cette propriété n\'est pas définie sur `False`.

-    {{PropertyView/fr|Syntax Highlighter|Enumeration}}: il est par défaut {{Value|None}}. S\'il est défini sur {{Value|Python}}, il mettra en surbrillance le texte comme la [console Python](Python_console/fr.md).

## Script


**Voir aussi :**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md) et [objet scripté](scripted_objects/fr.md).

Voir [Part Feature](Part_Feature/fr.md) pour les informations générales sur l\'ajout d\'objets au document.

Un objet `App::TextDocument` est créé avec la méthode `addObject()` du document. Une fois qu\'un TextDocument existe, ses informations textuelles sont stockées dans son attribut `Text`. Cet attribut peut être utilisé dans d\'autres objets, par exemple, comme chaîne dans une **<img src="images/Draft_ShapeString.svg" width=16px> [Draft Formes à partir de texte](Draft_ShapeString/fr.md)**.


```python
import FreeCAD as App
import Draft

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::TextDocument", "Text_document")
obj.Text = "textual information"
App.ActiveDocument.recompute()

obj2 = Draft.makeShapeString(obj.Text, "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)
App.ActiveDocument.recompute()
```





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std TextDocument/fr
