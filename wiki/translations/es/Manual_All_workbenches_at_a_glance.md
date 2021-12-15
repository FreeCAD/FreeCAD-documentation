# Manual:All workbenches at a glance/es
{{Manual:TOC/es}}

Una de las mayores dificultades para los nuevos usuarios de FreeCAD, es saber en qué ambiente de trabajo encontrar una herramienta específica. La siguiente tabla te dará una visión general de los ambientes de trabajo más importantes y sus herramientas. Consulta la página de cada [Ambiente de trabajo](Workbenches/es.md) en la documentación de FreeCAD para una lista más completa.

Cuatro ambientes de trabajo también están diseñados para trabajar en pareja, y uno de ellos está totalmente incluido en el otro: Arquitectura contiene todas las herramientas de Borrador, y DiseñoPieza todas las de Croquizador. Sin embargo, para mayor claridad, se separan a continuación.

### Pieza

El ambiente de trabajo de piezas proporciona herramientas básicas para trabajar con piezas sólidas: primitivas, como cubos y esferas, y operaciones geométricas simples y operaciones booleanas. Siendo el principal punto de anclaje con [OpenCasCade](https://en.wikipedia.org/wiki/Open_Cascade_Technology), el ambiente de trabajo de piezas proporciona la base del sistema de geometría de FreeCAD, y casi todos los demás ambientes de trabajo producen geometría basada en piezas.

  Tool                                                                                                               Description                                                         Tool                                                                                                                  Description
  ------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------
  <img alt="" src=images/Part_Box.svg  style="width:32px;"> _                                       Draws a cone
  <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> _                               Draws a sphere
  <img alt="" src=images/Part_Torus.svg  style="width:32px;"> _        Creates various other parametric geometric primitives
  <img alt="" src=images/Part_Builder.svg  style="width:32px;"> _                                      Fuses (unions) two objects
  <img alt="" src=images/Part_Common.svg  style="width:32px;"> _                                           Cuts (subtracts) one object from another
  <img alt="" src=images/Part_JoinConnect.svg  style="width:32px;"> _                   Embeds a walled object into another walled object
  <img alt="" src=images/Part_JoinCutout.svg  style="width:32px;"> _                           Extrudes planar faces of an object
  <img alt="" src=images/Part_Fillet.svg  style="width:32px;"> _                           Creates a solid by revolving another object (not solid) around an axis
  <img alt="" src=images/Part_Section.svg  style="width:32px;"> _   Creates multiple cross sections along an object
  <img alt="" src=images/Part_Chamfer.svg  style="width:32px;"> _                               Mirrors the selected object on a given mirror plane
  <img alt="" src=images/Part_RuledSurface.svg  style="width:32px;"> _                                   Sweeps one or more profiles along a path
  <img alt="" src=images/Part_Loft.svg  style="width:32px;"> _                               Creates a scaled copy of the original object
  <img alt="" src=images/Part_Thickness.svg  style="width:32px;"> [Thickness](Part_Thickness.md)                Assign a thickness to the faces of a shape                                                                                                                                                

### Borrador

The Draft Workbench provides tools to do basic 2D CAD drafting tasks: lines, circles, etc\... and a series of generic handy tools such as move, rotate or scale. It also provides several drawing aids, such as grid and snapping. It is principally meant to draw the guidelines for Arch objects, but also serves as FreeCAD\'s \"swiss knife\".

  Tool                                                                                                                    Description                                                    Tool                                                                                                               Description
  ----------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------
  <img alt="" src=images/Draft_Line.svg  style="width:32px;"> _                                 Draws a line made of multiple line segments (polyline)
  <img alt="" src=images/Draft_Circle.svg  style="width:32px;"> _                                     Draws an arc segment from center, radius, start angle and end angle
  <img alt="" src=images/Draft_Ellipse.svg  style="width:32px;">_                     Draws a regular polygon from a center and a radius
  <img alt="" src=images/Draft_Rectangle.svg  style="width:32px;"> _                                 Draws a multi-line text annotation
  <img alt="" src=images/Draft_Dimension.svg  style="width:32px;"> _                     Draws a B-Spline from a series of points
  <img alt="" src=images/Draft_Point.svg  style="width:32px;"> _     The ShapeString tool inserts a compound shape representing a text string at a given point in the current document
  <img alt="" src=images/Draft_Facebinder.svg  style="width:32px;"> _             Draws a Bezier curve from a series of points
  <img alt="" src=images/Draft_Move.svg  style="width:32px;"> _                         Rotates objects by a certain angle around a point
  <img alt="" src=images/Draft_Offset.svg  style="width:32px;"> _                         Trims, extends or extrudes an object
  <img alt="" src=images/Draft_Upgrade.svg  style="width:32px;"> _             Turns or separates objects into lower-level objects
  <img alt="" src=images/Draft_Scale.svg  style="width:32px;"> _   Creates a 2D object which is a flattened view of another object
  <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:32px;"> _              Creates a rectangular array from an object
  <img alt="" src=images/Draft_Clone.svg  style="width:32px;"> _                         Mirrors objects across a line

### Croquizador

The Sketcher Workbench contains tools to build and edit complex 2D objects, called sketches. The geometry inside these sketches can be precisely positioned and relationed by the use of constraints. They are primarily meant to be the building blocks of PartDesign geometry, but are useful everywhere in FreeCAD.

  Tool                                                                                                                                                            Description                                                                                                                                                 Tool                                                                                                                                                      Description
  --------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  <img alt="" src=images/Sketcher_CreatePoint.svg  style="width:32px;"> _                                                         Draws a line segment from 2 points
  <img alt="" src=images/Sketcher_Arc.svg  style="width:32px;"> _                      Draws an arc segment from two endpoints and another point on the circumference
  <img alt="" src=images/Sketcher_Circle.svg  style="width:32px;"> _         Draws a circle from three points on the circumference
  <img alt="" src=images/Sketcher_CreateEllipse.svg  style="width:32px;"> _   Draws an ellipse by major diameter (2 points) and minor radius point
  <img alt="" src=images/Sketcher_CreateArcOfEllipse.png  style="width:32px;"> _                             Draws a line made of multiple line segments. Several drawing modes available
  <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:32px;"> _                             Draws a regular triangle inscribed in a construction geometry circle
  <img alt="" src=images/Sketcher_CreateSquare.svg  style="width:32px;"> _                             Draws a regular pentagon inscribed in a construction geometry circle
  <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width:32px;"> _                             Draws a regular heptagon inscribed in a construction geometry circle
  <img alt="" src=images/Sketcher_CreateOctagon.svg  style="width:32px;"> _                                             Draws an oval by selecting the center of one semicircle and an endpoint of the other semicircle
  <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:32px;"> _                                               Trims a line, circle or arc with respect to a clicked point
  <img alt="" src=images/Sketcher_External.svg  style="width:32px;"> _        Toggles an element to/from construction mode. A construction object will not be used in a 3D geometry operation and is only visible while editing the Sketch that contains it
  <img alt="" src=images/Constraint_PointOnPoint.svg  style="width:32px;"> _            Affixes a point onto another object such as a line, arc, or axis.
  <img alt="" src=images/Constraint_Vertical.svg  style="width:32px;"> _                          Constrains the selected lines or polyline elements to a true horizontal orientation. More than one object can be selected before applying this constraint.
  <img alt="" src=images/Constraint_Parallel.png  style="width:32px;"> _              Constrains two lines perpendicular to one another, or constrains a line perpendicular to an arc endpoint.
  <img alt="" src=images/Constraint_Tangent.png  style="width:32px;"> _                           Constrains two selected entities equal to one another. If used on circles or arcs their radii will be set equal.
  <img alt="" src=images/Constraint_Symmetric.png  style="width:32px;"> _                                    Constrains the selected item by setting vertical and horizontal distances relative to the origin, thereby locking the location of that item
  <img alt="" src=images/Constraint_HorizontalDistance.svg  style="width:32px;"> _        Fixes the vertical distance between 2 points or line endpoints. If only one item is selected, the distance is set to the origin.
  <img alt="" src=images/Constraint_Length.png  style="width:32px;"> _                                          Defines the radius of a selected arc or circle by constraining the radius.
  <img alt="" src=images/Constraint_InternalAngle.png  style="width:32px;"> _                           Constrains two lines to obey a refraction law to simulate the light going through an interface
  <img alt="" src=images/Constraint_InternalAlignment.png  style="width:32px;"> _                                          Maps a sketch to the previously selected face of a solid
  <img alt="" src=images/Sketcher_MergeSketch.svg  style="width:32px;"> _                                     Mirrors selected elements of a sketch

### Diseño Piezas 

The Part Design Workbench contains advanced tools to build solid parts. It also contains all the tools from the sketcher. Since it can only produce solid shapes (the rule number one of Part Design), it is the main workbench to use when designing pieces (parts) to be manufactured or 3D-printed, as you will always obtain a printable object.

  Tool                                                                                                                                     Description                                                                         Tool                                                                                                                                        Description
  ---------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------
  <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> _                                   Creates a pocket from a selected sketch. The sketch must be mapped to an existing solid object\'s face
  <img alt="" src=images/PartDesign_Revolution.svg  style="width:32px;"> _                                   Creates a groove by revolving a sketch around an axis
  <img alt="" src=images/PartDesign_Fillet.svg  style="width:32px;"> _                               Chamfers edges of an object
  <img alt="" src=images/PartDesign_Draft.svg  style="width:32px;"> _                           Mirrors features on a plane or face
  <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:32px;"> _          Creates a polar pattern of features
  <img alt="" src=images/PartDesign_Scaled.png  style="width:32px;"> _   Allows creating a pattern with any combination of the other transformations
  <img alt="" src=images/PartDesign_WizardShaft.svg  style="width:32px;"> _   Allows you to create several types of gears

### Arquitectura

The Arch Workbench contains tools to work with [BIM](https://en.wikipedia.org/wiki/Building_information_modeling) projects (civil engineering and architecture). It also contains all the tools from the Draft workbench. The main use of the Arch Workbench is to create BIM objects or give BIM attributes to objects built with other workbenches, in order to export them to [IFC](https://en.wikipedia.org/wiki/Industry_Foundation_Classes).

  Tool                                                                                                  Description                                                        Tool                                                                                                               Description
  ----------------------------------------------------------------------------------------------------- ------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------
  <img alt="" src=images/Arch_Wall.svg  style="width:32px;"> _                Creates a structural element from scratch or using a selected object as a base
  <img alt="" src=images/Arch_Rebar.svg  style="width:32px;"> _                                Creates a floor including selected objects
  <img alt="" src=images/Arch_Building.svg  style="width:32px;"> _                                    Creates a site including selected objects
  <img alt="" src=images/Arch_Window.svg  style="width:32px;"> _   Adds a section plane object to the document
  <img alt="" src=images/Arch_Axis.svg  style="width:32px;"> _                                    Creates a sloped roof from a selected face
  <img alt="" src=images/Arch_Space.svg  style="width:32px;"> _                            Creates a stairs object in the document
  <img alt="" src=images/Arch_Panel.svg  style="width:32px;"> _                                Creates a frame object from a selected layout
  <img alt="" src=images/Arch_Equipment.svg  style="width:32px;"> _           Attributes a material to selected objects
  <img alt="" src=images/Arch_Schedule.svg  style="width:32px;"> _                   Cut an object according to a plan
  <img alt="" src=images/Arch_Add.svg  style="width:32px;"> _                            Subtracts or removes objects from a component
  <img alt="" src=images/Arch_Survey.svg  style="width:32px;"> [Survey](Arch_Survey.md)               Enters or leaves surveying mode                                                                                                                                                       

### Dibujo


**Development of the [Drawing Workbench](Drawing_Workbench.md) stopped in FreeCAD 0.16, and the new [TechDraw Workbench](TechDraw_Workbench.md) aiming to replace it was introduced in v0.17. The Drawing Workbench may be removed in future releases. Use the TechDraw Workbench instead.**

The Drawing Workbench handles the creation and manipulation of 2D drawing sheets, used for displaying views of your 3D work in 2D. These sheets can then be exported to 2D applications in SVG or DXF formats, to a PDF file or printed.

  Tool                                                                                                                    Description                                                                Tool                                                                                                                Description
  ----------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------
  <img alt="" src=images/Drawing_Landscape_A3.png  style="width:32px;"> _                            Inserts a view of the selected object in the active drawing sheet
  <img alt="" src=images/Drawing_Annotation.png  style="width:32px;"> _                            Adds a clip group to the current drawing sheet
  <img alt="" src=images/Drawing_Openbrowser.png  style="width:32px;"> _   Automatically creates orthographic views of an object on the current drawing sheet
  <img alt="" src=images/Drawing_Symbol.png  style="width:32px;"> _                   Inserts a special Draft view of the selected object in the current drawing sheet
  <img alt="" src=images/Drawing_Save.png  style="width:32px;"> [Save](Drawing_Save.md)                                Saves the current sheet as a SVG file                                                                                                                                                          

### Otros ambientes de trabajo incorporados 

Although the above summarizes the most important tools of FreeCAD, many more workbenches are available, among them:

-   The [Mesh Workbench](Mesh_Workbench.md) allows to work with [polygon meshes](https://en.wikipedia.org/wiki/Polygon_mesh). Although meshes are not the preferred type of geometry to work with in FreeCAD, because of their lack of precision and support for curves, meshes still have a lot of uses, and are fully supported in FreeCAD. The Mesh Workbench also offers a number of Part-to-Mesh and Mesh-to-Part tools.
-   The [Raytracing Workbench](Raytracing_Workbench.md) offers tools to interface with external renderers such as povray or luxrender. Right from inside FreeCAD, this workbench allows you to produce high-quality renderings from your models.
-   The [Spreadsheet Workbench](Spreadsheet_Workbench.md) permits the creation and manipulation of spreadsheet data, that can be extracted from FreeCAD models. Spreadsheet cells can also be referenced in many areas of FreeCAD, allowing to use them as master data structures.
-   The [FEM Workbench](FEM_Workbench.md) deals with [Finite Elements Analysis](https://en.wikipedia.org/wiki/Finite_element_method), and permits the performing of pre- and post-processing FEM calculations and to display the results graphically.

### Ambientes de trabajo externos 

A number of other very useful workbenches produced by FreeCAD community members also exist. Although they are not included in a standard FreeCAD installation,they are easy to install as plug-ins. They are all referenced in the [FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons) repository. Among the most developed are:

-   The [Drawing Dimensioning Workbench](https://github.com/hamish2014/FreeCAD_drawing_dimensioning) offers many new tools to work directly on Drawing Sheets and allow you to add dimensions, annotations and other technical symbols with great control over their aspect. **The Drawing Dimensioning Workbench is no longer maintained.**
-   The [Fasteners Workbench](https://github.com/shaise/FreeCAD_FastenersWB) offers a wide range of ready-to-insert fasteners objects like screws, bolts, rods, washers and nuts. Many options and settings are available.
-   The [A2plus](https://github.com/kbwbe/A2plus) workbench offers a series of tools to mount and work with [assemblies](https://en.wikipedia.org/wiki/Assembly_modelling).

**Leer más**

-   [La lista completa de ambientes de trabajo](Workbenches/es.md)
-   [El ambiente de trabajo de piezas](Part_Workbench/es.md)
-   [El ambiente de trabajo de bocetos](Draft_Workbench/es.md)
-   [El ambiente de trabajo de Croquizador y Diseño Piezas](PartDesign_Workbench/es.md)
-   [El ambiente de trabajo Arquitectura](Arch_Workbench/es.md)
-   [El ambiente de trabajo TechDraw](TechDraw_Workbench/es.md)
-   [El ambiente de trabajo MEF](FEM_Workbench/es.md)
-   [El repositorio de complementos de FreeCAD](https://github.com/FreeCAD/FreeCAD-addons)

---
[documentation index](../README.md) > Manual:All workbenches at a glance/es
