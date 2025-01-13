# FreeCADGui API/fr
**(octobre 2019) Ne pas éditer cette page. L'information est incomplète et obsolète. Pour la dernière API, voir la [https://www.freecadweb.org/api documentation de l'API générée automatiquement], ou générez la documentation vous-même, voir [Documentation du code source](Source_documentation/fr.md).**

Ce module est le pendant du module FreeCAD. Il contient tout ce qui touche à l\'interface utilisateur et les vues 3D. Exemple: 
```python
import FreeCAD as App
import FreeCADGui as Gui

# get the 3D model document
doc = App.ActiveDocument    

# get the visual representation model document
gui_doc = Gui.ActiveDocument

gui_doc.activateWorkbench("myWorkbench")
```


{{APIFunction | activate Workbench | chaîne | Active un atelier par nom | rien}}


{{APIFunction | activeDocument | | | le document actif ou None si rien n'existe}}


{{APIFunction | activeWorkbench | | | l'objet de l'atelier actif}}


{{APIFunction | addCommand | chaîne, object | Ajoute une commande FreeCAD. Chaîne est le nom de la commande et l'objet est un nom de classe définissant la commande |}}


{{APIFunction | AddIcon | chaîne, chaîne or liste | Ajoute une icône comme nom de fichier ou dans le format XPM du système |}}


{{APIFunction | addIconPath | chaîne | Ajouter un nouveau chemin d'accès au système où trouver les fichiers d'icônes |}}


{{APIFunction | addPreferencePage | chaîne, chaîne | Ajoute une forme d'interface utilisateur pour la boîte de dialogue des préférences. Le premier argument spécifie le nom du fichier et le second spécifie le nom du groupe |}}


{{APIFunction | addWorkbench | chaîne, object | Ajoute un atelier sous un nom défini. La chaîne est le nom de l'atelier et l'objet est un nom de classe définissant l'atelier |}}


{{APIFunction | createDialog | chaîne | Ouvre un fichier d'interface |}}


{{APIFunction | getDocument | chaîne | Obtient un document par son nom | le document}}


{{APIFunction | getWorkbench | chaîne | Obtient un atelier par son nom | l'atelier}}


{{APIFunction | Insert | chaîne | Ouvrir une macro, Inventor ou un fichier VRML | document}}


{{APIFunction | listWorkbenches | | Affiche une liste de toutes les ateliers | liste}}


{{APIFunction | open | chaîne | Ouvre une macro, Inventor ou un fichier VRML | le document ouvert}}


{{APIFunction | removeWorkbench | chaîne | Supprime un atelier par nom |}}


{{APIFunction | RunCommand | chaîne | Exécute une commande FreeCAD par nom |}}


{{APIFunction | updateGui | | Mise à jour de la fenêtre principale et toutes ses fenêtres |}}



---
⏵ [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > FreeCADGui API/fr
