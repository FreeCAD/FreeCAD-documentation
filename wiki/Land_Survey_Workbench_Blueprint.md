 


{{VeryImportantMessage|
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
}}


{{VeryImportantMessage|Important note: The Land Survey Workbench has been abandoned. If there are interested developers who want to spearhead it, please let us know on the forum}}

 

This page lists the requirements and implementation for a new workbench usable in the field of [Land Survey](http://en.wikipedia.org/wiki/Land_survey). The page is a bit outdated. Find the latest informations for FreeCAD in this regard on a HUGE forum thread: <http://forum.freecadweb.org/viewtopic.php?f=8&t=6973>

## Rectangle selection 

> A new mouse mode may be required:
>
> -   left-click on an object selects the object
> -   left-click in empty space - begin selection action; click again - end selection action, add to selection set
>     -   CTRL - exclude from already selected set
> -   press and hold middle button to pan
> -   contextual menu on right click
> -   wheel up/down - zoom

## Layers

-   Object properties such as color, line weight, visibility, print-ability can be set on a per-object basis or may be inherited from the parent layer.
-   Each object has a parent layer / an object may be part of a layer or not.

## Blocks

Blocks are objects that behave in most circumstances as a single object. The objects do not loose their individuality inside the block.

> Since there is a Upgrade/Downgrade, this functionality may already be present.

### Dynamic attributes 

Variables. Components of the block that may be changed without changing the definition of the block. Position inside the block is one such attribute.

> This feature will integrate well if expressed as properties.

## Points

In land survey the points are usually associated with numbers, description and other characteristics.

> The blocks with dynamic properties should do it.

## Querry tools for 2 and a half system 

The planar position is usually decoupled (especially in cadastre applications) from the height. When you want to know the distance between two points you actually want to know the distance in horizontal projection. The horizontal plane is XY, with Y pointing toward north. Z points upward (positive altitude).

## Rich text; Tables 

General support for rich text.

Note: the information in this page is based on a shallow understanding of FreeCAD\'s internals. Once it deepens the requirements and implementation may be adjusted. Contributions are welcomed! \--[Xtnickx](User:Xtnickx.md) 11:00, 26 January 2013 (UTC)

 

[Category:Roadmap{{\#translation:}}](Category:Roadmap.md) [Category:Developer{{\#translation:}}](Category:Developer.md)
