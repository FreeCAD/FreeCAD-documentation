# UTF Project
**
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
**

 

This is the project plan for the FreeCAD part of the [Development roadmap](Development_roadmap.md).

## Purpose and principles 

To improve multi-language capabilities in FreeCAD by implementing support for UTF characters within the Coin3D interface.

Despite Coin3D now moving to a more open development platform, it\'s still very difficult to contribute back into the project.

(mrlukeparry) I have yet to receive a response on contributing back and for now it seems more appropriate to keep this within the FreeCAD project and would mean we can let users test without requiring development versions of Coin3D. I would aim to achieve this by 0.14 considering it\'s a big priority for increasing accessibility of FreeCAD to non-english users.

## Organizing

-   Provide a basic UTF string handling functionality that is independent of major libraries except STL.
-   Implement the Coin3D fields and 3D text nodes for handling the new UTF data storage.
-   Migrate modules over to use the new textual nodes.
-   Rigorous testing

## Next actions 

-   Implement the UTF String Handling Class **(WIP)**
-   Handling of fonts and glyphs.
-   Implement Coin3D text fields and nodes for use in project
-   Migrate modules using SoText2 and SoText3 to utilise new nodes



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Roadmap](Category_Roadmap.md) > UTF Project
