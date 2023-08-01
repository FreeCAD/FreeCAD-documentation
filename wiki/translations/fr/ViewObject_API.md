# ViewObject API/fr
**(Octobre 2019) Ne modifiez pas cette page. L'information est incomplète et obsolète. Pour la dernière API, consultez la [https://www.freecadweb.org/api documentation de l'API générée automatiquement], ou générez la documentation vous-même, voir[Source documentation](Source_documentation/fr.md).**

Lorsque l\'interface graphique est en place, chaque objet dans le document FreeCAD a une ViewObject associé, qui réside dans le document homologue FreeCAD Gui. Un ViewObject peut être récupéré par deux moyens. Exemple: 
```python
myViewObj = FreeCAD.ActiveDocument.myObjectName.ViewObject
myViewObj = FreeCADGui.ActiveDocument.myObjectName
print myViewObj.IV
```


{{APIProperty | Annotation | le nœud d'annotation d'une vue Object}}


{{APIProperty | Boîte englobante | la boîte englobante}}


{{APIProperty | Contenu | une représentation XML des propriétés d'un ViewObject}}


{{APIProperty | DisplayMode | le mode d'affichage actuel}}


{{APIProperty | IV | une représentation Inventeur du ViewObject}}


{{APIProperty | objet | L'objet de ce ViewObject FreeCAD Document associé}}


{{APIProperty | PropertiesList | une liste de propriétés de ce ViewObject}}


{{APIProperty | RootNode | le nœud Inventeur de cette ViewObject (objet pivy.coin)}}


{{APIProperty | sélectionnable | True si l'objet est sélectionnable}}


{{APIProperty | Type | le type de cette ViewObject}}


{{APIProperty | Visibilité | Vrai si le ViewObject est visible}}


{{APIFunction | getAllDerivedFrom | | | toutes descentences de cet objet}}


{{APIFunction | getDocumentationOfProperty | | | la chaîne de documentation de la propriété de cette classe}}


{{APIFunction | getGroupOfProperty | | | le nom du groupe qui la propriété appartient à cette classe. Les biens immobiliers triés en groupes nommés differnt pour plus de commodité.}}


{{APIFunction | getPropertyByName | | |. La valeur d'une propriété nommée}}


{{APIFunction | getTypeOfProperty | | | le type d'une propriété nommée. Cela peut être (Hidden, ReadOnly, Output) ou toute combinaison.}}


{{APIFunction | hide | | Masque l'objet |.}}


{{APIFunction | isDerivedFrom | chaîne | Vérifie si cet objet est dérivé du type d'objet donné | vrai si le type donné est un père}}


{{APIFunction | isVisible | | Vérifie si l'objet est visible | un booléen}}


{{APIFunction | listDisplayModes | | Affiche une liste de tous les modes d'affichage | liste}}


{{APIFunction | setTransformation | coin.SoTransform | Définit une transformation sur le nœud Inventor | rien}}


{{APIFunction | spectacle | | Indique si l'objet est caché | rien}}


{{APIFunction | toString | | | une représentation de chaîne du nœud Inventor}}


{{APIFunction | Mise à jour | | Mise à jour de la  vue de représentation  de l'objet |}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > ViewObject API/fr
