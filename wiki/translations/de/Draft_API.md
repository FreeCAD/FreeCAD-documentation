# Draft API/de
**(November 2018) Diese Information kann unvollständig und veraltet sein. Für die letzte API siehe die (engl.) [https://www.freecadweb.org/api autogenerierte API-Dokumentation].**

Diese Funktionen sind Teil des [Draft-Arbeitsbereichs](Draft_Workbench/de.md) und können in [Makros](macros/de.md) oder mit dem [Phyton](Python/de.md)-Interpreter verwendet werden, sobald der `Draft`-Arbeitsbereich importiert wurde.

Beispiel: 
```python
import FreeCAD, Draft

myrect = Draft.makeRectangle(4, 3)
mydistance = FreeCAD.Vector(2, 2, 0)
Draft.move(myrect, mydistance)
```


{{APIFunction|cut|FreeCAD.Object, FreeCAD.Object|Returns a cut object made from the difference of the 2 given objects. The original objects get hidden.|The newly created object}}


{{APIFunction|extrude|FreeCAD.Object, Vector|Extrudes the given object in the direction given by the vector. The original object gets hidden.|The newly created object}}


{{APIFunction|formatObject|FreeCAD.Object, [FreeCAD.Object]|This function applies to the given target object the current properties set on the Draft toolbar (line color and line width), or copies the properties of a second object if provided. It also places the object in construction group if the construction button is pressed.|Nothing}}


{{APIFunction|fuse|FreeCAD.Object, FreeCAD.Object|Returns an object made from the union of the 2 given objects. If the objects are coplanar, a special Draft Wire is used, otherwise the final object is a standard Part fuse.|The newly created object}}


{{APIFunction|getDraftPath|[string]|Returns the user or system path where the Draft module is running from. If a subpath or a filename is supplied, the full path to the subpath inside the Draft module is returned.|A file path}}


{{APIFunction|getGroupContents|list|Scans recursively the given list for groups. If groups are encountered, their contents are appended to the list.|A list of FreeCAD Objects}}


{{APIFunction|getRealName|string|Strips the trailing numbers from an object name.|The stripped object name}}


{{APIFunction|getSelection| |Returns the current FreeCAD selection.|The current FreeCAD selection.}}


{{APIFunction|makeCircle|radius, [placement], [facemode], [startangle], [endangle]|Creates a circle object with given radius. If a placement is given, it is used. If facemode is False, the circle is shown as a wireframe, otherwise as a face. If startangle AND endangle are given (in degrees), they are used and the object appears as an arc.|The newly created object.}}


{{APIFunction|makeDimension|Vector, Vector, [Vector] or FreeCAD.Object, int, int, [Vector]|Creates a Dimension object measuring distance between first and second vectors, with the dimension line passign through the third vector if provided. The current line width and color from the Draft toolbar will be used. Instead of 2 vectors, you can also pass a FreeCAD object, and two integers (and optionally a vector where the dimension line must pass). In that case, the dimension will be associated with the object, and measure two of its vertices, indicated by the two given indice numbers.|The newly created object.}}


{{APIFunction|makeLine|Vector, Vector|Creates a line between the two given vectors. The current line width and color from the Draft toolbar will be used.|The newly created object.}}


{{APIFunction|makeRectangle|length, width, [placement], [facemode]|Creates a Rectangle object with length in X direction and height in Y direction. If a placement is given, it is used. If facemode is False, the rectangle is shown as a wireframe, otherwise as a face. The current line width and color from the Draft toolbar will be used.|The newly created object.}}


{{APIFunction|makeText|string or list, [Vector], [screenmode]|Creates a Text object, at the given point if a vector is provided, containing the string or the strings given in the list, one string by line. The current color from the Draft toolbar and the text height and font specified in preferences are used. If screenmode is True, the text always faces the view direction, otherwise it lies on the XY plane.|The newly created object.}}


{{APIFunction|makeWire|list or Part.Wire, [closed], [placement], [facemode]|Creates a DWire object from the given list of vectors or from the given Wire. If closed is True or if first and last points are identical, the wire is closed. If facemode is True (and wire is closed), the wire will appear filled. The current line width and color from the Draft toolbar will be used.|A new Draft DWire (not a Part Wire).}}


{{APIFunction|move|FreeCAD.Object or list, Vector, [copymode]|Moves the given object or the objects contained in the given list in the direction and distance indicated by the given vector. If copymode is True, the actual objects are not moved, but copies are created instead.|The object(s) (or their copies if copymode was True).}}


{{APIFunction|precision| |Returns the precision value from Draft user settings.|An integer.}}


{{APIFunction|rotate|FreeCAD.Object or list, angle, [center], [axis] ,[copymode]|Rotates the given object or the objects contained in the given list with the given angle around the given center if provided, using axis as a rotation axis. If axis is omitted, the rotation will be around the vertical Z axis. If copymode is True, the actual objects are not moved, but copies are created instead.|The objects (or their copies).}}


{{APIFunction|scale|FreeCAD.Object or list, vector, [center], [copymode]|Scales the given object or the objects contained in the given list with a scale factors defined by the given vector (in X, Y and Z directions) around the given center if provided. If copymode is True, the actual objects are not moved, but copies are created instead.|The objects (or their copies).}}


{{APIFunction|select|FreeCAD.Object|Deselects everything and selects only the passed object|Nothing.}}


{{APIFunction|shapify|FreeCAD.Object|Transforms a parametric shape object into non-parametric.|The new object.}}


{{APIFunction|draftify|FreeCAD.Object or list|Turns the given object or each object of the given list into Draft parametric wires.|Nothing.}}


{{APIFunction|getSVG|FreeCAD.Object, [linemodifier], [textmodifier], [(u,v)]|Creates a SVG representation of the given object. The linemodifier attribute is a scale factor (in percents) for line width, and textmodifier for text size. You can also optionally provide a tuple of vectors to define a projection plane, otherwise the geometry will be projected on the XY plane.|a string containing a SVG representation of the given object.}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > [Draft](Draft_Workbench.md) > Draft API/de
