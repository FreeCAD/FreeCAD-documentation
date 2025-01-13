# Selection API/fr
**(octobre 2019) Ne pas éditer cette page. L'information est incomplète et obsolète. Pour la dernière API, voir la [https://www.freecadweb.org/api documentation de l'API générée automatiquement], ou générez la documentation vous-même, voir [Documentation du code source](Source_documentation/fr.md).**

Le sous-module de sélection fait partie du module FreeCADGui. Exemple: 
```python
import FreeCADGui
sel = FreeCADGui.Selection.getSelection()
```


{{APIFunction|addSelection|FreeCAD.Objet|Ajoute un objet à la sélection|}}


{{APIFunction|clearSelection|[chaîne]|Efface la sélection du nom de document donné. Si aucun document n'est donné la sélection complète est effacée|.}}


{{APIFunction|getSelection|[chaîne]|Renvoie une liste d'objets de documents sélectionnés pour un nom de document donné. Si aucun document n'est donné la sélection complète est retourné|. Une liste d'objets de documents dans l'ordre où ils ont été sélectionnés}}

. {{APIFunction|getSelectionEx|[chaîne]|Renvoie une liste de Sélection d'Objet pour un nom de document donné. Si aucun document n'est donné la sélection complète est retournée. Utilisé pour sélectionner les sous-objets (ex certaines arêtes d'une face)|. Une liste de Sélection d'Objets dans l'ordre où ils ont été sélectionnés}} {{APIFunction|isSelected|FreeCAD.Objet|Vérifie si un objet donné est sélectionné |}} {{APIFunction|removeSelection|FreeCAD.Objet|Supprime un objet de la sélection |}}



---
⏵ [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > Selection API/fr
