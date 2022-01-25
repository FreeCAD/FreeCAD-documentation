# Object API/de
**(Oktober 2019) Bearbeite diese Seiten nicht. Die Informationen sind unvollständig und veraltet. Die neueste API findest Du in der [https://www.freecadweb.org/api autogenerierten API-Dokumentation] oder generiere die Dokumentation selbst, siehe [Quelldokumentation](Source_documentation/de.md).**

Being parametric, document objects in FreeCAD can have a lot of additional properties, but these are the basic ones, present in every FreeCAD Document Object. Objects can be retrieved simply by their name. Example: 
```python
myObj = FreeCAD.ActiveDocument.myObjectName
print myObj.PropertiesList
```


{{APIProperty|Content|An XML representation of the properties of an object.}}


{{APIProperty|Label|Gets/sets the objects label. The string can be unicode.}}


{{APIProperty|Name|The unique name of an object.}}


{{APIProperty|Placement|Gets/sets the Placement of an object. A placement defines an orientation (rotation) and a position (base) in 3D space. It is used when no scaling or other distortion is needed.}}


{{APIProperty|PropertiesList|A list of the properties of an object}}


{{APIProperty|State|The FreeCAD state of an object (ie. if it needs to be recomputed)}}


{{APIProperty|Type|A string describing the type of an object}}


{{APIProperty|ViewObject|The associated View Provider (FreeCADGUI object) of an object}}


{{APIFunction|getAllDerivedFrom| | |All descendants of this object}}


{{APIFunction|getDocumentationOfProperty| | |The documentation string of the property of this class.}}


{{APIFunction|getGroupOfProperty| | |The name of the group which the property belongs to in this class. The properties are sorted in different named groups for convenience.}}


{{APIFunction|getPropertyByName| | |The value of a named property.}}


{{APIFunction|getTypeOfProperty| | |The type of a named property. This can be (Hidden,ReadOnly,Output) or any combination.}}


{{APIFunction|isDerivedFrom| | |True if given type is a father}}


{{APIFunction|purgeTouched| |Marks the object as unchanged| }}


{{APIFunction|touch| |Marks the object as changed (touched)| }}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > Object API/de
