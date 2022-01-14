# OpenGL on MacOS
## Known Issue: Rendering problems on MacOS 

Qt 4, the [ GUI](wikipedia_Graphical_User_Interface.md) software library used by FreeCAD, has a known limitation that can result in some odd-looking behaviour on modern versions of MacOS when windows within FreeCAD overlap.

This issue has been resolved by moving FreeCAD\'s Qt OpenGL usage to new classes introduced with Qt 5, as of the FreeCAD 0.17 development version in late March 2017.

See [issue 1401](http://freecadweb.org/tracker/view.php?id=1401).

[<img src="images/Property.png" style="width:16px"> Developer Documentation](Category_Developer_Documentation.md)

---
[documentation index](../README.md) > OpenGL on MacOS
