


{{VeryImportantMessage|
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
}}


{{TOCright}}

This project is toward the implementation of a decent Units system in FreeCAD. It follows the rules of the \[<http://en.wikipedia.org/wiki/GTD#GTD_methodology>\| Getting things done\] process. The projects are collected in the [Development roadmap](Development_roadmap.md).

## Purpose and principles 

This is a software development project aimed to implement a Unit-system framework into FreeCAD.

The development steps are planed here (Next actions) and tracked in the Issue tracking system to get a well formed change log: [Issue tracker](http://apps.sourceforge.net/mantisbt/free-cad/my_view_page.php)

## Outcome

It will enable FreeCAD to handle wired measurement systems, like the imperial system, and complex compound [SI](http://en.wikipedia.org/wiki/International_System_of_Units) units. Also handle the import/export formats which are able to transport Units (like STEP). And allow scaling based on assumptions of Units (mm-\>m, m-\>in).

## Brainstorming

Lots of discussion was done here: <http://forum.freecadweb.org/viewtopic.php?f=10&t=1616>

And lot of information you\'ll find in the [Units](Units.md) article.

## Organizing

### Upgrading units parser 

Upgrading the parser to handle and generate signatures as discussed in the [Units](Units.md) article.

### Properties

Changing the properties form e.g. PropertyLength to PropertyUntit with a unit signature.

Eventually a property editor for the PropertyUntit.

### Workbenches

-   Upgrading workbenches to use the Units framework. I would start with Sketcher and PartDesign and go subsequently further\...
-   Documenting that upgrade process so other people can do the same with other workbenches \--[Yorikvanhavre](User:Yorikvanhavre.md) 13:13, 28 November 2011 (UTC)

## Next actions 

-   Upgrading units parser (jriegel)



[Category:Roadmap{{\#translation:}}](Category:Roadmap.md)
