# Object API/fr
**(Octobre 2019) Ne modifiez pas cette page. L'information est incomplète et obsolète. Pour la dernière API, consultez la [https://www.freecadweb.org/api documentation de l'API générée automatiquement], ou générez la documentation vous-même, voir [Source documentation](Source_documentation/fr.md).**

Êtant paramétrique, les Objets Documents dans FreeCAD peuvent avoir beaucoup de propriétés supplémentaires, mais ce sont celles de base, présentes dans chaque Objet Document FreeCAD document. Les objets peuvent être récupérés tout simplement par leur nom. Exemple: 
```python
myObj = FreeCAD.ActiveDocument.myObjectName
print myObj.PropertiesList
```


{{APIProperty | Contenu |. Une représentation XML des propriétés d'un objet}}


{{APIProperty| Label | Obtient/définit l'étiquette des objets. La chaîne peut être unicode.}}


{{APIProperty|Nom | Le nom unique d'un objet.}}


{{APIProperty | Placement | Obtient/définit le placement d'un objet. Un placement définit une orientation (rotation) et une position (de base) dans l'espace 3D. Il est utilisé lorsque aucune mise à l'échelle ou autre distorsion n'est nécessaire.}}


{{APIProperty | PropertiesList | Une liste des propriétés d'un objet}}


{{APIProperty | État | L'état FreeCAD d'un objet (.-À-dire se il doit être recalculé)}}


{{APIProperty | Type | Une chaîne décrivant le type d'un objet}}


{{APIProperty | ViewObject | The View fournisseur associé (objet FreeCADGUI) d'un objet}}


{{APIFunction | getAllDerivedFrom | | | Tous les descendants de cet objet}}


{{APIFunction | GetDocumentation propriété | | |. La chaîne de documentation de la propriété de cette classe}}


{{APIFunction | getGroupOfProperty | | | Le nom du groupe auquel la propriété appartient dans cette classe. Les propriétés sont classées dans différents groupes nommés pour plus de commodité.}}


{{APIFunction | getPropertyByName | | |. La valeur d'une propriété nommée}}


{{APIFunction | getTypeOfProperty | | | Le type d'une propriété nommée. Cela peut être (Hidden, ReadOnly,Output) ou toute combinaison.}}


{{APIFunction | isDerivedFrom | | | Vrai si le type donné est un père}}


{{APIFunction | purgeTouched | | Marque l'objet comme inchangé |}}


{{APIFunction | contact | | Marque l'objet comme modifié (touché) |}}


 

[Category:API](Category:API.md) [Category:Poweruser Documentation](Category:Poweruser_Documentation.md)

---
[documentation index](../README.md) > [API](Category:API.md) > Object API/fr
