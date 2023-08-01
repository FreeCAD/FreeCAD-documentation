# FreeCAD API/fr
**(Octobre 2019) Ne modifiez pas cette page. L'information est incomplète et obsolète. Pour la dernière API, consultez la [https://www.freecadweb.org/api documentation de l'API générée automatiquement], ou générez la documentation vous-même, voir [Source documentation](Source_documentation/fr.md).**

C\'est le module principal (root) de FreeCAD. Il peut également être appelé par \"App\" de l\'interprète FreeCAD. Il contient tout ce qui est nécessaire pour manipuler des documents et leur contenu (objets)

Exemple: 
```python
import FreeCAD
print FreeCAD.listDocuments()
mydoc = FreeCAD.activeDocument()
```


{{APIFunction|ConfigDump| |Imprime un dictionnaire contenant tout l'environnement de configuration FreeCAD.| }}


{{APIFunction|ConfigGet|[string]|Renvoie la valeur de la clé donnée. Si aucune clé n'est fournie, la configuration complète est renvoyée|Une chaîne.}}


{{APIFunction|ConfigSet|string, string|Définit la clé donnée (première chaîne) sur la valeur donnée (deuxième chaîne).| }}


{{APIFunction|Version| |Imprime la version FreeCAD.| }}


{{APIFunction|activeDocument| |Renvoie le document actif ou Aucun s'il n'y a pas de document actif.|Un document FreeCAD.}}


{{APIFunction|addExportType|string, string|Ajoute un nouveau type de fichier d'exportation à FreeCAD. La première chaîne doit être formatée comme cet exemple: "Document Word (*.doc)". La deuxième chaîne est le nom d'un script/module python contenant une fonction export().| }}


{{APIFunction|addImportType|string, string|Ajoute un nouveau type de fichier d'importation à FreeCAD, fonctionne de la même manière que addExportType, le module de gestion python doit contenir une fonction open() et/ou import().| }}


{{APIFunction|closeDocument|Nom du document|Ferme le document donné| }}


{{APIFunction|getDocument|Nom du document|Renvoie un document ou déclenche une exception s'il n'y a pas de document avec le nom donné.| }}


{{APIFunction|getExportType|string|Renvoie le nom du module qui peut exporter le type de fichier spécifié.|Une chaîne.}}


{{APIFunction|getImportType|string|Renvoie le nom du module qui peut importer le type de fichier spécifié.|Une chaîne.}}


{{APIFunction|listDocuments| |Renvoie un dictionnaire de noms et de pointeurs d'objet de tous les documents.|Un dictionnaire de noms et de pointeurs d'objet.}}


{{APIFunction|newDocument|[string], [hidden<nowiki>=</nowiki>False]|Crée et renvoie un nouveau document avec un nom donné. Le nom du document doit être unique, ce qui est vérifié automatiquement. Si aucun nom n'est fourni, le document sera nommé "Sans titre". Si <tt>hidden<nowiki>=</nowiki>True</tt> est passé, FreeCAD en mode GUI n'affichera pas le document et n'affichera pas d'onglet pour le document; cela permet d'effectuer des opérations automatiques sur un document temporaire (ou de créer un document et de l'enregistrer) sans perturber l'interface utilisateur.|Le document nouvellement créé.}}


{{APIFunction|open|string|Voir openDocument| }}


{{APIFunction|openDocument|filepath, [hidden]|Crée et renvoie un document et charge un fichier projet dans le document. L'argument chaîne doit pointer vers un fichier existant. Si le fichier n'existe pas ou si le fichier ne peut pas être chargé, une exception d'E / S est levée. Dans ce cas, le document créé est conservé, mais sera vide. Si <tt>hidden<nowiki>=</nowiki>True</tt> est passé, FreeCAD en mode GUI n'affichera pas le document et n'affichera pas d'onglet pour le document; cela permet d'effectuer des opérations automatiques sur un document et de le fermer sans perturber l'interface utilisateur.|Le document FreeCAD ouvert.}}


{{APIFunction|setActiveDocument|Nom du document|Définit le document actif par son nom.| }}



---
⏵ [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > FreeCAD API/fr
