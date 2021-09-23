# ViewObject API/de
**(Oktober 2019) Bearbeite diese Seiten nicht. Die Informationen sind unvollständig und veraltet. Die neueste API findest Du in der [https://www.freecadweb.org/api autogenerierten API-Dokumentation] oder generiere die Dokumentation selbst, siehe [Quelldokumentation](Source_documentation/de.md).**

Wenn die GUI aktiv ist, hat jedes Objekt im FreeCAD-Dokument ein zugeordnetes ViewObject, das sich im FreeCADGui-Dokument-Gegenstück befindet. Ein Ansicht-Objekt kann auf zwei Arten abgefragt werden. Beispiel: 
```python
myViewObj = FreeCAD.ActiveDocument.myObjectName.ViewObject
myViewObj = FreeCADGui.ActiveDocument.myObjectName
print myViewObj.IV
```


{{APIProperty|Annotation|the annotation node of a ViewObject}}


{{APIProperty|BoundingBox|the bounding box}}


{{APIProperty|Content|an XML representation of a ViewObject's properties}}


{{APIProperty|DisplayMode|the current display mode}}


{{APIProperty|IV|an Inventor representation of the ViewObject}}


{{APIProperty|Object|the associated FreeCAD Document Object of this ViewObject}}


{{APIProperty|PropertiesList|a list of properties of this ViewObject}}


{{APIProperty|RootNode|the Inventor node of this ViewObject (pivy.coin object)}}


{{APIProperty|Selectable|True if the object is selectable}}


{{APIProperty|Type|the type of this ViewObject}}


{{APIProperty|Visibility|True if the viewObject is visible}}


{{APIFunction|getAllDerivedFrom| | |all descentences of this object}}


{{APIFunction|getDocumentationOfProperty| | |the documentation string of the property of this class.}}


{{APIFunction|getGroupOfProperty| | |the name of the group which the property belongs to in this class. The properties sorted in differnt named groups for convenience.}}


{{APIFunction|getPropertyByName| | |the value of a named property.}}


{{APIFunction|getTypeOfProperty| | |the type of a named property. This can be (Hidden,ReadOnly,Output) or any combination.}}


{{APIFunction|hide| |Hides the object.| }}


{{APIFunction|isDerivedFrom|string|Checks if this object is derived from the given object type|True if given type is a father}}


{{APIFunction|isVisible| |Checks if the object is visible|a boolean}}


{{APIFunction|listDisplayModes| |Shows a list of all display modes|a list}}


{{APIFunction|setTransformation|coin.SoTransform|Sets a transformation on the Inventor node|nothing}}


{{APIFunction|show| |Shows the object if hidden|nothing}}


{{APIFunction|toString| | |a string representation of the Inventor node}}


{{APIFunction|update| |Updates the view representation of the object| }}


 

[Category:API](Category:API.md) [Category:Poweruser Documentation](Category:Poweruser_Documentation.md)

---
[documentation index](../README.md) > [API](Category:API.md) > ViewObject API/de
