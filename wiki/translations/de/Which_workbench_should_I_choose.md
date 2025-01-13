# Which workbench should I choose/de
Wenn du neu im Umgang mit FreeCAD bist, ist es wahrscheinlich, dass du dich fragst, mit welchem [Arbeitsbereich](Workbenches/de.md) du deine Arbeit beginnen solltest. Diese Seite hilft dir auszuwählen, womit du startest.

Arbeitsbereiche sind Zusammenstellungen von gruppierten Werkzeugen, Schaltflächen und anderen Schnittstellenelementen. Man kann sie sich als Anwendung innerhalb einer Anwendung vorstellen. In FreeCAD sind Arbeitsbereiche normalerweise eine Zusammenstellung von Werkzeugen, die einem bestimmten Zweck dienen wie z.B. 2D-Zeichnungserstellung, 3D-Objekte erstellen, Boote konstruieren, Roboter-Bewegungsbahnen erstellen, Gebäude entwerfen und vieles mehr.

FreeCAD enthält einige eingebaute [ Arbeitsbereiche](Workbenches/de.md), aber viele weitere [externe Arbeitsbereiche](External_workbenches/de.md) können einfach mit dem [Addon-Manager](Std_AddonMgr/de.md) installiert werden.


<div lang="en" dir="ltr" class="mw-content-ltr">

New FreeCAD users generally start using and learning one or two specific workbenches, then explore other areas of FreeCAD and add the tools they find interesting there to their skills set. Before diving into specific workbenches, though, make sure you read the [Getting started](Getting_started.md) and [Navigating in the 3D space](Manual_Navigating_in_the_3D_view.md) pages, as they provide generic knowledge you\'ll need everywhere in FreeCAD. The [FreeCAD manual](Manual_Introduction.md) is another good way to discover FreeCAD step by step, in a linear way.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The first workbench you should use depends on what you intent to do with FreeCAD. We usually see new users coming with one of the following requirements:


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## I have no previous CAD experience, and I want to design and 3D print an object 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

That is probably the most common use case among new FreeCAD users, and what FreeCAD is best at. It features a specific workbench for that: the [PartDesign Workbench](PartDesign_Workbench.md). PartDesign also contains all the tools from the [Sketcher Workbench](Sketcher_Workbench.md), so you will learn and use two workbenches in one.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

When starting a new model with PartDesign, you will usually first be required to create a [body](PartDesign_Body.md). A body is at the same time a container for subshapes, and the result, your final object. Think of it as one object = one body. The body, although it can be composed of several parts, should always represent a single assembled object, with no loose parts. Most operations you perform on or inside a body will prevent you from creating loose parts.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Most often, what you will do inside a body is the following sequence of operations:


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

1.  [Draw a closed 2D shape](Sketcher_NewSketch.md) (also called [sketches](Sketcher_Workbench.md)) on some plane in the 3D space (for example, on the ground (XY) plane, or on a face of an existing part). Sketches are a very powerful feature of FreeCAD. They can contain linear or curved segments, but also complex elements such as constraints or construction geometry.
2.  [Extrude that shape](PartDesign_Pad.md) so it forms a solid
3.  Use that solid either as an [addition](PartDesign_Pad.md) or [subtraction](PartDesign_Pocket.md) of another solid
4.  Optionally, apply some finishes such as [rounding](PartDesign_Fillet.md) on some faces


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

And repeat this process until you get to your finished object. See the list of tutorials below for more in-depth information and examples of typical modelling processes. When you have finished modeling your object, it is time to send it to the 3D printer. This usually means:


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

1.  Make sure you have your 3D printer set up, and a slicing application ready (an application responsible for turning a 3D object into commands for the printer, such as [slic3r](https://slic3r.org/) or [cura](https://ultimaker.com/software/ultimaker-cura))
2.  Select your body (your final object)
3.  Navigate to menu File -\> Export and export your object to a format supported by your slicer application, usually the STL format
4.  Open the STL file in the slicer, set the correct parameters for your printer, and press the \"print\" button


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

There are many other places in this documentation to learn more about the PartDesign workflow and how to use the Sketcher:


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   Read more on the [PartDesign Workbench](PartDesign_Workbench.md)
-   Read more on the [Sketcher Workbench](Sketcher_Workbench.md)
-   Tutorial: [Creating a simple part with PartDesign](Creating_a_simple_part_with_PartDesign.md)
-   Tutorial: [Basic Part Design Tutorial](Basic_Part_Design_Tutorial.md)
-   Tutorial: [Modeling for product design](Manual_Modeling_for_product_design.md)
-   Tutorial: [Export to STL or OBJ](Export_to_STL_or_OBJ.md)


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## I have some experience with SolidWorks or something similar. I want to do product design and assemblies 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The first part of your use case is pretty similar to the one above. You would typically use the [PartDesign Workbench](PartDesign_Workbench.md), which also contains all the tools of the [Sketcher Workbench](Sketcher_Workbench.md). You will typically design one body for each individual part of your assembly.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Once you have your different parts, you\'ll need to assemble them together. FreeCAD does not at the moment feature a default, unique assembly workbench. Rather, there are several assembly add-ons that you can easily install via the [Addons manager](Std_AddonMgr.md):


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   The [A2plus Workbench](A2plus_Workbench.md) provides tools to create multi-part assemblies. It is the oldest that we have in FreeCAD. It was born before advanced features like App Link objects were available in FreeCAD, so it is more basic and simpler, which can be a problem or an advantage.
-   The [Assembly3 Workbench](Assembly3_Workbench.md) is used to perform assembly of different bodies contained in a single file or in multiple documents. It was a testbed for the App Link object that was eventually included in the master code. It is the most complex solution and supports things like interactive kinematics.
-   The [Assembly4 Workbench](Assembly4_Workbench.md) is a solution based on the enhanced expression engine and the App Link object developed in the branch of Assembly3. Assembly4 does not work with a proper constraint solver, instead it uses the expression engine to position bodies with respect to Local Coordinate Systems (LCS).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The one best for you to choose depends on your requirements, and it\'s not easy to tell beforehand.We suggest you try Assembly4 first, then try Assembly3 if you need something more complex, or A2Plus if it is too complex for your needs.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## I have some experience with AutoCAD or something similar. I want to do 2D drawing 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Although FreeCAD is primarily a 3D application, it has all the tools to fully draw and annotate complex 2D designs such as house plans, and to either print them, export them as PDF documents, or export them to other formats supported by other traditional 2D CAD applications, such as DXF or DWG.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The workbench of choice for 2D Drafting is the [Draft Workbench](Draft_Workbench.md). Draft features all the tools commonly found in traditional CAD applications, such as lines, rectangles, arcs, splines, hatch fillings, texts or dimensions, and tools to modify objects, such as move, rotate, extend, scale, offset and so on.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The objects you draw can be grouped together using groups or layers, and the drawings you create can be exported as DXF/DWG files, or placed at a certain scale on a sheet that represents a sheet of paper. This sheet can then be printed or exported as a PDF file.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Differently to traditional 2D CAD applications, though, FreeCAD is primarily a 3D CAD application. So a first step you will need to do when starting to work with Draft tools is to choose in which plane of the 3D space you will want to draw your design. Traditionally, this is done in the XY plane, which would be a horizontal plane laying on the ground, at altitude zero.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

In Draft, you do that by setting your [working plane](Draft_SelectPlane.md). The working plane is where next drawing operations (line, rectangle, etc) will be done. You can change the working plane anytime, but you also can set FreeCAD up so it always starts with the working plane set to the ground XY plane, and never worry about this anymore.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Make sure you read how to [navigate in the 3D space](Manual_Navigating_in_the_3D_view.md), so you know how to set your viewpoint to look directly at your working plane from above, and get back to that viewpoint if you move away from it. This will ensure you a comfortable working space, similar to the application you know.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Once your working plane is set, all you need to do is start drawing. Explore the [list of available Draft tools](Draft_Workbench.md) to know what is there, but they will basically behave similarly to other 2D CAD applications. For example, draw lines that represent the boundary of a terrain, or a rectangle that represents a house.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

When working with Draft, you usually draw in real size. One meter is one meter. Make sure you set up your [working units](Units.md) to your liking. Also, make use of the [snapping tools](Draft_Snap.md) to position your points precisely.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Grouping your objects can be done using [groups](Std_Group.md) or [layers](Draft_Layer.md). Layers are simply groups that can control the color and other aspects of the objects placed inside them.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

When your drawing is ready to be exported, simply select everything you want to export (or the groups/layers containing them), and use menu File -\> Export, and choose the DXF or DWG format. Note that DWG capabilities of FreeCAD depend on [external software](Draft_DXF#DWG.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

To print or export your drawing as a PDF file, you make use of the [TechDraw Workbench](TechDraw_Workbench.md). TechDraw is used to create printable sheets, place on them templates and other page graphical elements, and views of your 2D or 3D models. A typical workflow with Draft and TechDraw includes:


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

1.  Set your working plane as the XY (top) plane
2.  Creating your drawing using Draft tools
3.  Make sure to group all the components of your drawing into groups or layers, and have one root group or layer container that contains all the layers or subgroups of your drawing. This makes it easier to place it in one go on a sheet. You would typically create a different group for each separate drawing, so you can control their positions and scales independently on the sheet.
4.  Switch to the TechDraw workbench
5.  Create a new page
6.  Set or adjust its template
7.  For each of your Draft drawings, use the [Draft view](TechDraw_DraftView.md) tool to create a view of it on the sheet
8.  Adjust the scale and position of each view
9.  Print or save he sheet as a PDF file from the TechDraw menu


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Here is more material about Draft and 2D drawing in FreeCAD:


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   All the [Draft Workbench](Draft_Workbench.md) tools
-   Tutorial: [Traditional 2D drafting](Manual_Traditional_2D_drafting.md)
-   Tutorial: [Draft tutorial](Draft_tutorial.md)
-   Tutorial: [Basic Sketcher Tutorial](Basic_Sketcher_Tutorial.md). The sketcher can be used to create much more complex and advanced 2D elements than you can do in Draft


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## I have some experience with Revit or ArchiCAD or another BIM application. I want to do BIM modelling 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Your workbench of choice is the [BIM Workbench](BIM_Workbench.md). The BIM workbench contains all the tools usually found in BIM applications to model building components, such as wall, window, door, etc. It also contains most of the [Draft tools](Draft_Workbench.md), and uses the same [working plane](Draft_SelectPlane.md) concept, where your next objects will lie on the current working plane.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

There is no mandatory building structure organization (ex. floors) in FreeCAD. You can choose to group your BIM objects into [groups](Std_Group.md) or [layers](Draft_Layer.md), similarly to Draft, but you can also make use of the [Building Part](Arch_BuildingPart.md) object to represent levels or buildings, and achieve a similar organization as usually found in other BIM applications.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Most BIM tools such as walls and windows will create an object on their own, by selecting options in the task panel and clicking points in the 3D view, but they can also all work by selecting other objects before. For example, you can draw a wall by selecting the wall tool and then clicking two points, but you can also draw a line or polyline first, then, with that object selected, press the Wall button. A wall will be built on top of that polyline, and use it as its baseline. If you modify the polyline, the wall will change accordingly.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The different BIM tools such as wall, window, column, etc\... will produce a corresponding wall, window or column object. However, the type of the produced object is defined by and only by its **IFC type** property, which can be changed anytime. So you can use the wall tool to model a beam for example. You only have to change its IFC type from \"wall\" to \"beam\" afterwards.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Similarly, any object created with another workbench or even another application can become a BIM object. Using the [Create component](Arch_Component.md) tool, you can add BIM properties (included the IFC Type property) to any other object.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

After creating a BIM model, which is nothing else than a 3D model where all objects have defined BIM/IFC properties, you can do several operations such as:


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   Exporting it to the [IFC formatby](Arch_IFC.md) selecting your model root container (group or building part) and hitting menu File -\> Export and selecting IFC. The IFC format is the standard exchange format for BIM models and is supported by all BIM applications
-   Extract 2D drawings such as floor plans, sections or elevations. This is done by placing [section planes](Arch_SectionPlane.md) in your model
-   Create drawings from these section planes. This is done either (and preferably) as an intermediary step, using the [Draft Shape2DView](Draft_Shape2DView.md) tool, which can then be further annotated with Draft tools, or directly placed on a TechDraw sheet using the [TechDraw ArchView](TechDraw_ArchView.md) tool
-   Create schedules or quantities tables using the [Arch Schedule](Arch_Schedule.md) tool and the [Spreadsheet Workbench](Spreadsheet_Workbench.md)
-   Export your model to another application to create 3D renderings, such as [Blender](https://blender.org). This is usually done by selecting the objects you wish to export, and use menu File -\> Export and choose a format well supported by these applications, such as OBJ or DAE. Note that there is a [FreeCAD importer](https://gist.github.com/yorikvanhavre/e873d51c8f0e307e333fe595c429ba87) available for Blender, which enables it to open FreeCAD files directly.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Here is more material to learn about BIM modeling in FreeCAD:


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   The [BIM Workbench](BIM_Workbench.md) tools
-   Tutorials: [Architecture and BIM](Tutorials#Architecture_and_BIM.md)


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## I have no clear idea what I want to do. I just want to explore FreeCAD 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The best way to go is probably to browse through the [FreeCAD manual](Manual_Introduction.md). The manual is designed as a flowing, printable sequence of chapters that will gently guide you through everything there is to know about FreeCAD.


</div>



---
⏵ [documentation index](../README.md) > Which workbench should I choose/de
