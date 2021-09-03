


{{TutorialInfo
|Topic=Modeling
|Level=Intermediate
|Author=[Yorik](User:Yorik.md)
|FCVersion=0.14
}}

![](images/Arch_tutorial_00.jpg )

## Introduction

This tutorial aims at giving you the basics to work with the [Arch Workbench](Arch_Workbench.md). I will try to make it simple enough so you don\'t need any previous experience with FreeCAD, but having some experience with 3D or [BIM](http://en.wikipedia.org/wiki/Building_Information_Modeling) applications will be useful. In any case, you should be prepared to look for yourself for further information about how FreeCAD works on the [FreeCAD documentation wiki](Main_Page.md). The [Getting started](Getting_started.md) page is a must read, if you have no previous experience with FreeCAD. Also check our [tutorials](tutorials.md) section, and on [youtube](http://www.youtube.com/results?search_query=freecad) you will also find a lot more of FreeCAD tutorials.

The purpose of the [Arch Workbench](Arch_Workbench.md) is to offer a complete [BIM](http://en.wikipedia.org/wiki/Building_Information_Modeling) workflow inside FreeCAD. As it is still under development, don\'t expect to find here the same tools and level of completion as grown-up commercial alternatives such as [Revit](http://en.wikipedia.org/wiki/Revit) or [ArchiCAD](http://en.wikipedia.org/wiki/Archicad), but on the other hand, FreeCAD being used in a much bigger scope than these applications, the [Arch Workbench](Arch_Workbench.md) greatly benefits from the other disciplines FreeCAD caters to, and offers some features rarely seen in traditional BIM applications.

Here are, for example, a couple of interesting features of FreeCAD\'s [Arch Workbench](Arch_Workbench.md) that you\'ll hardly find in other BIM apps:

-   Architectural objects are always solids. From FreeCAD\'s strong mechanical background, we learned the importance of always working with solid objects. This ensures a much more error-free workflow, and very reliable boolean operations. Since cutting through 3D objects with a 2D plane, in order to extract sections, is also a boolean operation, you can immediately see the importance of this point.

-   Architectural objects can always have any shape. No restrictions. Walls don\'t need to be vertical, slabs don\'t need to look like slabs. Any solid object can always become any architectural object. Very complex things, usually hard to define in other BIM applications, like a floor slab curving up and becoming a wall (yes Zaha Hadid, it\'s you we\'re talking about), present no particular problem at all in FreeCAD.

-   The whole power of FreeCAD is at your fingertips. You can design architectural objects with any other tool of FreeCAD, such as the [PartDesign Workbench](PartDesign_Workbench.md), and when they are ready, convert them to architectural objects. They will still retain their full modeling history, and continue being totally editable. The [Arch Workbench](Arch_Workbench.md) also inherits much of the [Draft Workbench](Draft_Workbench.md) functionality, such as [snapping](Draft_Snap.md) and [working planes](Draft_SelectPlane.md).

-   The [Arch Workbench](Arch_Workbench.md) is very [mesh](Mesh_Workbench.md)-friendly. You can easily design an architectural model in a mesh-based application such as [Blender](http://en.wikipedia.org/wiki/Blender_%28software%29) or [SketchUp](http://en.wikipedia.org/wiki/Sketchup) and import it in FreeCAD. If you took care of the quality of your model and its objects are manifold solid shapes, turning them into architectural objects only requires the press of a button.

At the time I\'m writing this, though, the [Arch Workbench](Arch_Workbench.md), as the rest of FreeCAD, suffers some limitations. Most are being worked on, though, and will disappear in the future.

-   FreeCAD is no 2D application. It is made for 3D. There is a reasonable set of tools for drawing and editing 2D objects with the [Draft Workbench](Draft_Workbench.md) and [Sketcher Workbench](Sketcher_Workbench.md), but it is not made for handling very large (and sometimes badly drawn) 2D CAD files. You can usually successfully import 2D files, but don\'t expect very high performance if you want to keep working on them in 2D. You have been warned.

-   No materials support. FreeCAD will have a complete [Material](Material.md) system, able to define very complex materials, with all the goodies you can expect (custom properties, material families, rendering and visual aspect properties, etc), and the [Arch Workbench](Arch_Workbench.md) will of course use it when it is ready.

-   Very preliminary [IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes) support. You can already [import IFC files](Arch_IFC.md), quite reliably, provided [IfcOpenShell](http://ifcopenshell.org) is installed on your system, but exporting is still not officially supported. This is worked on both by the FreeCAD and IfcOpenShell developers, and in the future we can expect full-powered IFC support.

-   Most Arch tools are still in development. That means that automatic \"wizard\" tools that create complex geometry automatically, such as [Arch Roof](Arch_Roof.md) or [Arch Stairs](Arch_Stairs.md) can only produce certain types of objects, and other tools that have presets, such as [Arch Structure](Arch_Structure.md) or [Arch Window](Arch_Window.md) only have a couple of basic presets. This will of course grow over time.

-   [Relations between objects](Assembly_project.md) in FreeCAD are still not officially available. These, for example the relation between a window and its host wall, are currently implemented in the [Arch Workbench](Arch_Workbench.md) with temporary (and therefore somewhat limited) methods. Many new possibilities will arise when this feature will be fully available.

-   [Units](Units.md) are being implemented in FreeCAD, which will allow you to work with any unit you wish (even imperial units, you guys from the USA can be eternally grateful for this to Jürgen, FreeCAD\'s godfather and dictator). But at the moment the implementation is not complete, and the Arch workbench still doesn\'t support them. You must consider it \"unit-less\".


{{Note|FreeCAD version 0.14 required|This tutorial was written using [FreeCAD version 0.14](Release_notes_0.14.md). You will need at least this version number in order to follow it. Earlier versions might not contain all the needed tools, or they could lack options presented here.}}

## Typical workflows 

The [Arch Workbench](Arch_Workbench.md) is mainly made for two kinds of workflows:

-   Build your model with a faster, mesh-based application such as [Blender](http://en.wikipedia.org/wiki/Blender_%28software%29) or [SketchUp](http://en.wikipedia.org/wiki/Sketchup), and import them in FreeCAD in order to extract plans and section views. FreeCAD being made for precision modeling, at a much higher level than what we usually need in architectural modeling, building your models directly in FreeCAD can be heavy and slow. For this reason, such a workflow has big advantages. I described it in [this article](http://yorik.uncreated.net/guestblog.php?2012=180) on my blog. If you care to model correctly and precisely (clean, solid, non-manifold meshes), this workflow gives you the same performance and precision level as the other.

-   Build your model directly in FreeCAD. That is what I will showcase in this tutorial. We will use mostly three workbenches: [Arch](Arch_Workbench.md), of course, but also [Draft](Draft_Workbench.md), whose tools are all included in Arch, so there is no need to switch workbenches, and [Sketcher](Sketcher_Workbench.md). Conveniently, you can do as I usually do, which is to create a custom toolbar in your Arch workbench, with Tools → Customize, and add the tools from the sketcher that you use often. This is my \"customized\" Arch workbench:

![](images/Arch_tutorial_01.jpg )

In this tutorial, we will model the house in 3D, based on the 2D drawings we\'ll download from the net, and extract from it 2D documents, such as plans, elevations and sections.

## Preparation

Instead of creating a project from scratch, let\'s take an example project to model, it will save us time. I chose this wonderful house by the famous architect [Vilanova Artigas](http://en.wikipedia.org/wiki/Jo%C3%A3o_Batista_Vilanova_Artigas) (see a series of [pictures](http://www.leonardofinotti.com/projects/architects-second-house/image/40409-130405-010d) by Leonardo Finotti), because it is close to where I live, it is simple, it\'s a wonderful example of the amazing modernist architecture of São Paulo, and DWG drawings are [easily available](http://www.bibliocad.com/library/second-house-vilanova-artigas_72926#).

We will use the 2D DWG drawings obtained from the link above (you need to register on the above site to download, but it\'s free, or grab directly a DXF version [here](http://yorik.uncreated.net/archive/scripts/artigas.dxf)) as a base to build our model. So the first thing you\'ll want to do is to download the file, unzip it, and open the DWG file inside with a DWG application such as [DraftSight](http://www.3ds.com/products-services/draftsight/overview/). Alternatively, you can convert it to DXF with a free utility such as the [ODA File Converter](https://www.opendesign.com/guestfiles/oda_file_converter). If you have the ODA converter installed (and its path set in the Arch preferences settings), FreeCAD is also [able to import DWG files directly](Draft_DXF.md). But since these files can sometimes be of bad quality and very heavy, it\'s usually better to open it first with a 2D CAD application and do some cleaning.

Here, I removed all the detail drawings, all the titleblocks and page layouts, did a \"clean\" (\"purge\" in AutoCAD slang) to remove all unused entities, reorganized the sections at a logical location in relation to the plan view, and moved everything to the (0,0) point. After that, our file can be opened quite efficiently in FreeCAD. Check the different options available in Edit → Preferences → Draft → Import/Export, they can affect how (and how quickly) DXF/DWG files are imported.

This is how the file looks after being opened in FreeCAD. I also changed the thickness of the walls (the contents of the \"muros\" group), and flipped a couple of doors that were imported with wrong X scale, with the [Draft Scale](Draft_Scale.md) tool:

![](images/Arch_tutorial_02.jpg )

The [DXF importer](Draft_DXF.md) (which also takes care of DWG files, since when importing DWG files, they are simply converted to DXF first), groups the imported objects by layer. There is no layer in FreeCAD, but there are [groups](Std_Group.md). [Groups](Std_Group.md) offer a similar way to organize the objects of your files, but don\'t have specific properties, like AutoCAD layers, that apply to their contents. But they can be placed inside other groups, which is very handy. The first thing we might want to do here, is to create a new [group](Std_Group.md) in the [tree view](Document_structure.md), right-click on the document icon, add a group, right click on it to rename it as \"base 2D plans\", and drag and drop all the other objects into it.

## Building the walls 

Like most [Arch](Arch_Workbench.md) objects, [walls](Arch_Wall.md) can be built upon a big variety of other objects: [lines](Draft_Line.md), [wires](Draft_Wire.md) (polylines), [sketches](Sketcher_Workbench.md), faces or solid (or even on nothing at all, in which case they are defined by height, width and length). The resulting geometry of the wall depends on that base geometry, and the properties you fill in, such as width and height. As you might guess, a wall based on a line will use that line as its alignment line, while a wall based on a face will use that face as its base footprint, and a wall based on a solid will simply adopt the shape of that solid. This allows about any shape imaginable to become a wall.

There are different possible strategies to build walls in FreeCAD. One might want to build a complete \"floor plan\" with the [sketcher](Sketcher_Workbench.md), and build one, big, wall object from it. This technique works, but you can only give one thickness for all the walls of the project. Or, you can build each piece of wall from separate line segments. Or, this is what we will do here, a mix of both: We will build a couple of [wires](Draft_Wire.md) on top of the imported plan, one for each type of wall:

![](images/Arch_tutorial_03.jpg )

As you see, I\'ve drawn in red the lines that will become concrete walls (a [pictures search](http://www.google.com/search?tbm=isch&q=casa+artigas+brooklin) of the house can help you to see the different wall types), the green ones are the exterior brick walls, and the blue ones will become the inner walls. I passed the lines through the doors, because doors will be inserted in the walls later, and will create their openings automatically. Walls can also be aligned left, right or centrally on their baseline, so it doesn\'t matter which side you draw the baseline. I also took care on avoiding intersections as much as I could, because our model will be cleaner that way. But we\'ll take care of intersections later.

When this is done, place all those lines in a new [group](Std_Group.md) if you want, select each line one by one, and press the [Arch Wall](Arch_Wall.md) tool to build a wall from each of them. You can also select several lines at once. After doing that, and correcting widths (exterior walls are 25cm wide, inner walls are 15cm wide) and some alignments, we have our walls ready:

![](images/Arch_tutorial_04.jpg )

We could also have built our walls from scratch. If you press the [Arch Wall](Arch_Wall.md) button with no object selected, you will be able to click two points on the screen to draw a wall. But under the hood, the wall tool will actually draw a line and build a wall on it. In this case, I found it more didactic to show you how things work.

Did you notice that I took great care not to cross the walls? This will save us some headache later, for example if we export our work to other applications, that might not like it. I have only one intersection, where I was too lazy to draw two small line segments, and drew one big wire crossing another. This must be fixed. Fortunately, all Arch objects have a great feature: you can add one to another. Doing that will unite their geometries, but they are still editable independently after. To add one of our crossing walls to the other, just select one, CTRL + select the other, and press the [Arch Add](Arch_Add.md) tool:

![](images/Arch_tutorial_05.jpg )

On the left are the two intersecting walls, on the right the result after adding one to the other.


{{Note|An important note about parametric objects|Something is important to consider already. As you can see, in FreeCAD, everything is parametric: Our new "united" wall is made from two walls, each based on a baseline. When you expand them in the [tree view](Document_structure.md), you can see all that chain of dependencies. As you can imagine, this little game can quickly become very complex. Furthermore, if you already know how to work with the [sketcher](Sketcher_Workbench.md), you might have wanted to draw the baselines with constrained sketches. This whole complexity has a cost: it raises exponentially the number of calculations that FreeCAD has to perform to keep your model geometry up to date. So, think about it, don't add unnecessary complexity when you don't need it. Keep a good balance between simple and complex objects, and keep these for the cases where you really need them.}}

For example, I could have drawn all my baselines above without caring about what crosses what, and fix things with the [Arch Add](Arch_Add.md) tool later. But I would have raised much the complexity of my model, for no gain at all. Better make them correct right from the start, and keeping them as very simple pieces of geometry.

Now that our walls are okay, we need to raise their height, until they intersect the roof. Then, since the wall object still cannot be cut automatically by roofs (this will happen some day, though), we will build a \"dummy\" object, that follows the shape of the roof, to be subtracted from our walls.

First, by looking at our 2D drawings, we can see that the highest point of the roof is 5.6m above the ground. So let\'s give all our walls a height of 6m, so we make sure they will be cut by our dummy roof volume. Why 6m and not 5.6m? You may ask. Well, if you already worked with boolean operations (additions, subtractions, intersections), you must already know that these operations usually don\'t like much \"face-on-face\" situations. They prefer clearly, frankly intersecting objects. So by doing this, we keep on the safe side.

To raise the height of our walls, simply select all of them (don\'t forget the one we added to the other) in the tree view, and change the value of their \"height\" property.

Before making our roof and cutting the walls, let\'s make the remaining objects that will need to be cut: The walls of the above studio, and the columns. The walls of the studio are made the same way as we did, on the superior floor plan, but they will be raised up to level 2.6m. So we will give them the needed height so their top is at 6m too, that is, 3.4m. Once this is done, let\'s move our walls up by 2.6m: Select them both, put yourself in frontal view (View → Standard Views → Front), press the [Draft Move](Draft_Move.md) button, select a first point, then enter 0, 2.6, 0 as coordinates, and press enter. Your objects now have jumped 2.6m high:

![](images/Arch_tutorial_06.jpg )


{{Note|About coordinates|The [Draft](Draft_Workbench.md) objects, and most [Arch](Arch_Workbench.md) objects too, obey to a Draft system called [working planes](Draft_SelectPlane.md). This system defines a 2D plane where next operations will take place. If you don't specify any, that working plane adapts itself to the current view. This is why we switched to frontal view, and you see that we indicated a movement in X of 0 and in Y of 2.6. We could also have forced the working plane to stay on the ground, by using the [Draft SelectPlane](Draft_SelectPlane.md) tool. Then, we would have entered a movement of X of 0, Y of 0 and Z of 2.6. }}

Now let\'s move our walls horizontally, to their correct location. Since we have points to snap to, this is easier: Select both walls, press the [Draft Move](Draft_Move.md) tool, and move them from one point to the other:

![](images/Arch_tutorial_07.jpg )

Finally, I changed the color of some walls to a brick-like color (so it\'s easier to differentiate), and made a small correction: Some walls don\'t go up to the roof, but stop at a height of 2.60m. I corrected the height of those walls.

## Raising the structure 

Now, since we\'ll have to cut our walls with a subtraction volume, we might as well see if there aren\'t other objects that will need to be cut that way. There are, some of the columns. This is a good opportunity to introduce a second arch object: the [Arch Structure](Arch_Structure.md). Structure objects behave more or less like walls, but they aren\'t made to follow a baseline. Rather, they prefer to work from a profile, that gets extruded (along a profile line or not). Any flat object can be a profile for a structure, with only one requirement: they must form a closed shape.

For our columns, we will use another strategy than with the walls. Instead of \"drawing\" on top of the 2D plans, we will directly use objects from it: the circles that represent the columns in the plan view. In theory, we could just select one of them, and press the [Arch Structure](Arch_Structure.md) button. However, if we do that, we produce an \"empty\" structural object. This is because you can never be too sure at how well objects were drawn in the DWG file, and often they are not closed shapes. So, before turning them into actual columns, let\'s turn them into faces, by using the [Draft Upgrade](Draft_Upgrade.md) tool twice on them. The first time to convert them into closed wires (polylines), the second time to convert those wires into faces. That second step is not mandatory, but, if you have a face, you are 100% sure that it is closed (otherwise a face cannot be made).

After we have converted all our columns to faces, we can use the [Arch Structure](Arch_Structure.md) tool on them, and adjust the height (some have 6m, other only 2.25m height):

![](images/Arch_tutorial_08.jpg )

On the image above, you can see two columns that are still as they were in the DWG file, two that were upgraded to faces, and two that were turned into structural objects, and their height set to 6m and 2.25m.

Note that those different Arch objects (walls, structures, and all the others we\'ll discover) all share a lot of things between them (for example all can be added one to another, like we already saw with walls, and any of them can be converted to another). So it\'s more a matter of taste, we could have made our columns with the wall tool too, and converted them if needed. In fact, some of our walls are concrete walls, we might want to convert them to structures later.

## Subtractions

Now it is time to build our subtraction volume. The easiest way will be to draw its profile on top of the section view. Then, we will rotate it and place it at its correct position. See why I placed the sections and elevations like that before beginning? It will be very handy for drawing stuff there, then moving it to its correct position on the model.

Let\'s draw a volume, bigger than the roof, that will be subtracted from our walls. To do that, I drew two lines on top of the base of the roof, then extended them a bit further with the [Draft Trimex](Draft_Trimex.md) tool. Then, I drew a [wire](Draft_Wire.md), snapping on these lines, and going well above our 6 meters. I also drew a blue line on the ground level (0.00), that will be our rotation axis.

<img alt="" src=images/Arch_tutorial_09.jpg  style="width:1024px;">

Now is the tricky part: We will use the [Draft Rotate](Draft_Rotate.md) tool to rotate our profile 90 degrees up, in the right position to be extruded. To do that, we must first change the [working plane](Draft_SelectPlane.md) to the YZ plane. Once this is done, the rotation will happen in that plane. But if we do like we did a bit earlier, and set our view to side view, it will be hard to see and select our profile, and to know where is the basepoint around which it must rotate, right? Then we must set the working plane manually: Press the [Draft SelectPlane](Draft_SelectPlane.md) button (it is in the \"tasks\" tab of the tree view), and set it to YZ (which is the \"side\" plane). Once you set the working plane manually, like that, it won\'t change depending on your view. You can now rotate your view until you have a good view of all the things you must select. To switch the working plane back to \"automatic\" mode later, press the [Draft SelectPlane](Draft_SelectPlane.md) button again and set it to \"None\".

Now the rotation will be easy to do: Select the profile, press the [Draft Rotate](Draft_Rotate.md) button, click on a point of the blue line, enter 0 as start angle, and 90 as rotation:

<img alt="" src=images/Arch_tutorial_10.jpg  style="width:1024px;">

Now all we need to do it to move the profile a bit closer to the model (set the working plane to XY if needed), and extrude it. This can be done either with the [Part Extrude](Part_Extrude.md) tool, or [Draft Trimex](Draft_Trimex.md), which also has the special hidden power to extrude faces. Make sure your extrusion is larger than all the walls it will be subtracted from, to avoid face-on-face situations:

<img alt="" src=images/Arch_tutorial_11.jpg  style="width:1024px;">

Now, here comes into action the contrary of the [Arch Add](Arch_Add.md) tool: [Arch Remove](Arch_Remove.md). As you might have guessed, it also makes an object a child of another, but its shape is subtracted from the host object, instead of being united. So now things are simple: Select the volume to subtract (I renamed it as \"Roof volume to subtract\" in the tree view so it is easy to spot), CTRL + select a wall, and press the [Arch Remove](Arch_Remove.md) button. You\'ll see that, after the subtraction happened, the volume to subtract disappeared from both the 3D view and the tree view. That is because it has been marked as child of the wall, and \"swallowed\" by that wall. Select the wall, expand it in the tree view, there is our volume.

Now, select the volume in the tree vieew, CTRL + select the next wall, press [Arch Remove](Arch_Remove.md). Repeat for the next walls until you have everything properly cut:

<img alt="" src=images/Arch_tutorial_12.jpg  style="width:1024px;">

Remember that for both [Arch Add](Arch_Add.md) and [Arch Remove](Arch_Remove.md), the order you select the objects is important. The host is always the last one, like in \"Remove X from Y\" or \"Add X to Y\"


{{Note|A note about additions and subtractions|Arch objects that support such additions and subtractions (all of them except the "visual" helper objects such as the axes) keep track of such objects by having two properties, respectively "Additions" and "Subtractions", that contain a list of links to other objects to be subtracted or added. A same object can be in the lists of several other objects, as it is the case of our subtraction volume here. Each of the fathers will want to swallow it in the tree view, though, so it will usually "live" in the last one. But you can always edit those lists for any object, by double-clicking it in the tree view, which in FreeCAD enters edit mode. Pressing the escape key exits edit mode.}}

## Making the roofs 

Now, all we have to do to complete the structure, is to make the roof and the smaller inner slabs. Again, the easiest way is to draw their profiles on top of the section, with the [Draft Wire](Draft_Wire.md) tool. Here I drew 3 profiles on top of each other (I moved them apart in the image below so you see better). The green one will be used for the lateral borders of the roof slab, then the blue one for the side parts, and the red ones for the central part, that sits above the bathroom block:

<img alt="" src=images/Arch_tutorial_13.jpg  style="width:1024px;">

Then, we must repeat the rotation operation above, to rotate the objects in a vertical position, then move them at their correct places, and copy some of them that will need to be extruded twice, with the \[\[Draft Move\|\]Draft Move\] tool, with the ALT key pressed, which creates copies instead of moving the current object. I also added two more profiles for the side walls of the bathroom opening.

<img alt="" src=images/Arch_tutorial_14.jpg  style="width:1024px;">

When everything is in place, it\'s just a matter of using the [Draft Trimex](Draft_Trimex.md) tool to extrude, then convert them to [Arch Structure](Arch_Structure.md) objects.

<img alt="" src=images/Arch_tutorial_15.jpg  style="width:1024px;">

After that, we can see some problems arising: two of the columns on the right are too short (they should go up to the roof), and there is a gap between the slab and the walls of the studio on the far right (the 2.60 level symbol on the section view was obviously wrong). Thanks to the parametric objects, all this is very easy to solve: For the columns, just change their height to 6m, fish your roof subtraction volume from the tree view, and subtract it to the columns. For the walls, it\'s even easier: move them a bit down. Since the subtraction volume remains at the same place, the wall geometry will adapt automatically.

Now one last thing must be fixed, there is a small slab in the bathroom, that intersects some walls. Let\'s fix that by creating a new subtraction volume, and subtract it from those walls. Another feature of the [Draft Trimex](Draft_Trimex.md) tool, that we use to extrude stuff, is that it can also extrude one single face of an existing object. This creates a new, separate object, so there is no risk to \"harm\" the other object. So we can select the base face of the small slab (look at it from beneath the model, you\'ll see it), then press the [Draft Trimex](Draft_Trimex.md) button, and extrude it up to well above the roofs. Then, subtract it from the two inner bathroom walls with the [Arch Remove](Arch_Remove.md) tool:

<img alt="" src=images/Arch_tutorial_16.jpg  style="width:1024px;">

## Floors, stairs and chimney 

Now, our structure is complete, we just have a couple of smaller objects to do.

### The chimney 

Let\'s start with the chimney. Now you already know how it works, right? Draw a couple of closed [wires](Draft_Wire.md), move them up at their correct height with the [Draft Move](Draft_Move.md) tool, extrude them with the [Draft Trimex](Draft_Trimex.md) tool, turn the bigger one into a [structure](Arch_Structure.md), and subtract the smaller ones. Notice how the chimney tube wasn\'t drawn on the plan view, but I found its position by dragging blue lines from the section views.

<img alt="" src=images/Arch_tutorial_17.jpg  style="width:1024px;">

### The floors 

The floors are not well represented in the base drawings. When looking at the sections, you cannot know where and how thick the floor slabs are. So I will suppose that the walls are sitting on top of foundation blocks, at level 0.00, and that there are floor slabs, also sitting on those blocks, 15cm thick. So the floor slabs don\'t run under the walls, but around them. We could do that by creating a big rectangular slab then subtracting the walls, but remember, subtraction operations cost us. Better do it in smaller pieces, it will be \"cheaper\" in terms of calculation, and also if we do it intelligently, room by room, these will also be useful to calculate floor areas later:

<img alt="" src=images/Arch_tutorial_18.jpg  style="width:1024px;">

Once the wires are drawn, just turn them into [structures](Arch_Structure.md), and give them a height of 0.15:

<img alt="" src=images/Arch_tutorial_19.jpg  style="width:1024px;">

### The stairs 

Now the stairs. Meet the next of the Arch tools, the [Arch Stairs](Arch_Stairs.md). This tool is still in a very early stage of development, at the time I\'m writing, so don\'t expect too much of it. But it is already pretty useful to make simple, straight stairs. One concept is important to know, the stairs tool is thought to build stairs from a flat floor up to a wall. In other words, when viewed from the top, the stairs object occupies exactly the space that it occupies on the plan view, so the last riser is not drawn (but it is of course taken into account when calculating heights).

In this case, I preferred to build the stairs on the section view, because we\'ll need many measurements that are easier to get from that view. Here, I drew a couple of red guidelines, then two blue lines that will be the base of our two pieces of stairs, and two green closed wires, that will form the missing parts. Now select the first blue line, press the [Arch Stairs](Arch_Stairs.md) tool, set the number of steps to 5, the height to 0.875, the width to 1.30, the structure type to \"massive\" and the structure thickness to 0.12. Repeat for the other piece.

Then, extrude both green wires by 1.30, and rotate and move them to the right position:

<img alt="" src=images/Arch_tutorial_20.jpg  style="width:1024px;">

On the elevation view, draw (then rotate) the border:

<img alt="" src=images/Arch_tutorial_21.jpg  style="width:1024px;">

Then move everything into place:

<img alt="" src=images/Arch_tutorial_22.jpg  style="width:1024px;">

Don\'t forget also to cut the column that crosses the stairs, because in BIM it\'s always bad to have intersecting objects. We are building like in the real world, remember, where solid objects cannot intersect. Here, I didn\'t want to subtract the column directly from the stairs (otherwise the column object would be swallowed by the stairs object in the tree view, and I didn\'t like that), so I took the face on which the column was built, and extruded it again. This new extrusion was then subtracted from the stairs.

Right! All the hard work is now done, let\'s go on with the very hard work!

## Doors and windows 

[Arch Windows](Arch_Window.md) are pretty complex objects. They are used to make all kinds of \"inserted\" objects, such as windows or doors. Yes, in FreeCAD, doors are just a special kind of window. In real life too, if you think of it, no? The [Arch Window](Arch_Window.md) tool can still be a bit hard to use today, but consider this as a tradeoff, as it was built for maximum power. Almost any kind of window your imagination can produce can be done with it. But as the tool will gain more presets, this situation will certainly become better in the future.

The [Arch Window](Arch_Window.md) object works like this: It is based on a 2D layout, any 2D object, but preferably a [sketch](Sketcher_Workbench.md), that contains closed wires (polylines). These wires define the different parts of the window: outer frames, inner frames, glass panels, solid panels, etc. The window objects then has a property that stores what to do with each of these wires: extrude it, place it at a certain offset, etc. Finally, a window can be inserted into a host object such as a wall or structure, and it will automatically create a hole in it. That hole will be calculated by extruding the biggest wire found in the 2D layout.

There are two ways to create such objects in FreeCAD: By using a preset, or drawing the window layout from scratch. We\'ll look at both methods here. But remember that the preset method does nothing else than creating the layout object and defining the necessary extrusions for you.

### Using presets 

When pressing the [Arch Window](Arch_Window.md) tool with no object selected, you are invited either to pick a 2D layout, or to use one of the presets. Let\'s use the \"Simple Door\" preset to place the main entrance door of our model. Give it a width of 1m, a height of 2.45m, a W1 size of 0.15m, and leave the other parameters to 0.05m. Then click the lower left corner of the wall, and your new door is created:

<img alt="" src=images/Arch_tutorial_23.jpg  style="width:1024px;">

You will notice that your new door won\'t appear in the tree view. That is because, by snapping to a wall, we indicated that wall as its host object. Consequently, it has been \"swallowed\" by the wall. But a right click on it → Go to selection will find it in the tree.

In this case, as our window is not inserted in any wall (the opening was there already), we might as well detach our window from its host wall. This is done by double-clicking the host wall in the tree view to enter its edit mode. There, you will see the window in its \"Subtractions\" group. Simply select the window there, press the \"remove element\" button, then \"OK\". Our window has now been removed from its host wall, and lies at the bottom of the tree view.

We have a second door, exactly the same as this one, a bit on the left. Instead of creating a new door from scratch, we have two ways to make a copy of the previous one: By using the [Draft Move](Draft_Move.md) tool, with the ALT key pressed, which, as you already know, copies an object instead of moving it. Or, even better, we can use the [Draft Clone](Draft_Clone.md) tool. The clone tool produces a \"clone\" of a selected object, that you can move around, but that retains the shape of the original object. If the original object changes, the clone changes too.

So all we need to do now is select the door, press the [Draft Clone](Draft_Clone.md) tool, then move the clone to its correct position with the [Draft Move](Draft_Move.md) tool.

### Organizing your model 

<img alt="" src=images/Arch_tutorial_24.jpg  style="width:400px;">

Now would be a good time to do a bit of housecleaning. Since we already have two windows, it is a good moment to do some cleaning in the tree view: Create a new [group](Std_Group.md), rename it to \"windows\", and drop the 2 windows in it. I also recommend you to separate other elements that way, such as the walls and structures. Since you can also create [groups](Std_Group.md) inside groups, you can organize further, for example by placing all elements that form the roof into a separate group, so it is easy to turn on and off (turning a group visible or invisible does the same with all objects inside).

The [Arch Workbench](Arch_Workbench.md) has some additional tools to organize your model: the [Arch Site](Arch_Site.md), [Arch Building](Arch_Building.md) and [Arch Floor](Arch_Floor.md). Those 3 objects are based on the standard FreeCAD group, so they behave exactly like groups, but they have a couple of additional properties. For example, [floors](Arch_Floor.md) have the ability to set and manage the height of the contained walls and structure, and when they are moved, all their contents are moved too.

But here, since we have only one building with only one (and a half) floor, there is no real need to use such objects, so let\'s stick with simple groups.




Now, let\'s get back to work. Turn off the roof group, so we can see better inside, and switch the Display Mode of the floor objects to Wireframe (or use the [Draft ToggleDisplayMode](Draft_ToggleDisplayMode.md) tool) so we can still snap to them, but we can see the plan view underneath. But you can also turn off the floors completely, then place your doors at level 0, then raise them of 15cm with the [Draft Move](Draft_Move.md) tool.

Let\'s place the interior doors. Use the \"Simple Door\" preset again, make doors of 1.00m and 0.70m wide x 2.10m high, with W1 size of 0.1m. Make sure you snap to the correct wall when you place them, so they automatically create a hole in that wall. If it is hard to place them correctly, you can place them at an easier location, at the corner of the wall, for example, then move them. The \"hole\" will move together.

If by mistake you hosted a window in the wrong wall, it is easy to fix: Remove the window from the \"Subtraction\" group of the host wall in edit mode, as we saw above, then add it to the \"Subtraction\" group of the correct wall, by the same method, or, simply, using the [Arch Remove](Arch_Remove.md) tool.

A little work later, all our doors are there:

<img alt="" src=images/Arch_tutorial_25.jpg  style="width:1024px;">

After a closer look at the elevation view, I now detected another error: The top of the brick walls is not as 2.60m, but 17.5cm lower, that is, 2.425m. Fortunately, windows based on presets have a facility: You can alter their general dimensions (width and height) from their properties. So let\'s change their height to 2.425 - 0.15, that is, 2.275. The second window, as it is a clone of the first one, will adapt too. This is basically where the true magic of parametric design appears.

Now we can look at the really interesting stuff: How to design your own custom windows.

### Creating custom windows 

As I explained above, [Arch Window](Arch_Window.md) objects are created from 2D layouts, made of closed elements (wires (polylines), circles, rectangles, anything). Since [Draft](Draft_Workbench.md) objects cannot hold more than one of these elements, the preferred tool to draw window layouts is the [Sketcher](Sketcher_Workbench.md). Unfortunately, with the sketcher, it is not possible to snap to external objects like with the Draft workbench, which would be useful here, since our elevations are drawn already. Fortunately, a tool exists to convert Draft objects to a sketch: The [Draft To Sketch](Draft_Draft2Sketch.md) tool.

So, let\'s start by building our first window layout. I drew it on the elevation, using several [rectangles](Draft_Rectangle.md): One for the outer line, and 4 for the inner lines. I stopped before the door, because, remember, our door already has a frame there:

<img alt="" src=images/Arch_tutorial_26.jpg  style="width:1024px;">

Then, select all the rectangles, and press the [Draft To Sketch](Draft_Draft2Sketch.md) button (and delete the rectangles, because this tool doesn\'t delete the original objects, in case something goes wrong). Then, with the new sketch selected, press the [Arch Window](Arch_Window.md) tool:

<img alt="" src=images/Arch_tutorial_27.jpg  style="width:1024px;">

The tool will detect that the layout has one outer wire and several inner wires, and automatically proposes you a default configuration: One frame, made by subtracting the inner wires from the outer one, extruded by 1m. Let\'s change that, by entering the window\'s edit mode, by double-clicking on it in the tree view:

You will see a \"Default\" component, that has been created automatically by the Window tool, that uses the 5 wires (always subtracting the other ones from the biggest one), and has an extrusion value of 1. Let\'s change its extrusion value to 0.1, to match what we used in the doors.

Then, let\'s add 4 new glass panels, each using a single wire, and give them an extrusion of 0.01, and an offset of 0.05, so they are placed at the middle of the frame. This will be how your window looks like when you are finished:

<img alt="" src=images/Arch_tutorial_28.jpg  style="width:1024px;">

I suppose now you must have understood the power of this system: Any combination of frames and panels of any shape is possible. If you can draw it in 2D, it can exist as a full valid 3D object.

Now, let\'s draw the other pieces, then we\'ll move everything into place together. But first. we\'ll need to do some corrections to the base 2D drawing, because some lines are clearly missing, where the windows meet the stairs. We can fix that by offsetting the stairs line by 2.5cm with the [Draft Offset](Draft_Offset.md) tool (with ALT pressed of course, to copy our lines instead of moving them). Now we can draw our layout, with [wires](Draft_Wire.md), then convert them to a sketch, then making a window of it.

After doing that a couple of times (I made it in 4 separate pieces, but it\'s up to you to decide), we have our facade complete:

<img alt="" src=images/Arch_tutorial_29.jpg  style="width:1024px;">

Now, as before, it\'s just a matter of rotating the pieces, and moving them to their correct position:

<img alt="" src=images/Arch_tutorial_30.jpg  style="width:1024px;">

Last missing piece, there is a segment of wall that didn\'t appear on the plan view, that we need to add. We have several options for that, I chose to draw a line on the ground plane, then move it up to the correct height, then create a wall from it. Then, we also need to fish up our roof subtraction volume (it must have stayed in the last column), then subtract it. Now this side of the building is ready:

<img alt="" src=images/Arch_tutorial_31.jpg  style="width:1024px;">

Ready? Not quite. Look at the image above, we did our doors with a 5cm frame, remember (it was the default from the preset). But the other windows have 2.5cm frames. This needs to be fixed.

### Editing windows 

We already saw how to build and update window components, via the window\'s edit mode, but we can also edit the underlying sketch. Preset windows are not different than custom windows, the [Arch Window](Arch_Window.md) tool only created the underlying sketch fo you. Select our door object (the original, not the copy, remember, we made a clone), and expand it in the tree view. There is our sketch. Double-click it to enter edit mode.

the [Sketcher Workbench](Sketcher_Workbench.md) is an extremely powerful tool. It doesn\'t have some of the [Draft](Draft_Workbench.md) conveniences, such as snapping or working planes, but it has many other advantages. In FreeCAD you will frequently use one or another depending on the need. The most important feature of the sketcher is constraints. Constraints allow you to automatically fix the position of some elements relative to others. For example, you can force a segment to always be vertical, or to always be at a certain distance to another.

When we edit our door sketch, we can see that it is made on a fully constrained sketch:

<img alt="" src=images/Arch_tutorial_32.jpg  style="width:1024px;">

Now all we need to do is edit the 5cm distances between the outer line and the inner line, by double-clicking them, and changing their value to 2.5cm (Remember, the units are still not fully functional at the time I\'m writing this). After clicking the \"OK\" button, our door (and its clone) have been updated.

## Working without 2D support 

Until now our work has been relatively easy, because we had the underlying 2D drawings to base our work upon. But now, we must do the opposite facade and the glass atrium, and things are getting more complicated: The opposite facade drawing has a lot of wrong things, doesn\'t represent the atrium at all, and we have simply no drawing for the inner walls of the atrium. So we will need to invent a couple of things ourselves. Be sure to have a look at [reference pictures](http://www.pedrokok.com.br/2010/02/residencia-artigas-sao-paulo-sp/img_8265-533px/) to figure out how things are made. Or do it as you wish!

One thing we can already do: duplicate the complicated stairs window with the [Draft Move](Draft_Move.md) tool, because it is equal on both sides:

<img alt="" src=images/Arch_tutorial_33.jpg  style="width:1024px;">

Note that here, I preferred to duplicate with the [Draft Move](Draft_Move.md) tool instead of using a [clone](Draft_Clone.md), because the clone currently doesn\'t support different colors inside objects. The difference is that the clone is a copy of the final shape of the original object, while if you copy an object, you create a new object and give it all the same properties as the original one (therefore, also its base sketch and its window components definition, which are both stored as properties).

Now we must attack the parts that are not drawn anywhere. Let\'s start with the glass wall between the sitting room and the atrium. It\'ll be easier to draw it on the elevation view, because we\'ll get the correct height of the roof. Once you are in plan view, you can rotate the view from the menu View → Standard Views → Rotate left or right, until you get a comfortable view to work, like this:

<img alt="" src=images/Arch_tutorial_34.jpg  style="width:1024px;">

Note how on the image above, I made a line from the model to the left section, to get the exact width of the window. Then, I reproduced that width on the elevation view and divided it into 4 pieces. Then I built one main window piece, plus 4 additional windows for the sliding doors. The sketcher sometimes has difficulties with overlapping wires, that\'s why I preferred to keep them separated like this:

<img alt="" src=images/Arch_tutorial_35.jpg  style="width:1024px;">

After the necessary rotations, everything clicks perfectly into place:

<img alt="" src=images/Arch_tutorial_36.jpg  style="width:1024px;">

We still need some corner piece there. A little useful trick with the [Draft SelectPlane](Draft_SelectPlane.md) tool, if you have a face selected when you press the button, the working plane matches this face (at least its position, and if the face is rectangular, it also tries to match its axes). This is useful to draw 2D objects directly on the model, such as here, we can draw a rectangle to be extruded directly at its correct position:

<img alt="" src=images/Arch_tutorial_37.jpg  style="width:1024px;">

Then let\'s do the two remaining pieces. One is easy, it is a copy of what\'s on the other side, so we can simply use the 2D drawing:

<img alt="" src=images/Arch_tutorial_38.jpg  style="width:1024px;">

The other one is a bit tricky, by looking at the pictures, we see that it has many vertical divisions, like the stairs windows. By chance (or very good design from Vilanova Artigas), the width of our window, of 4.50m, is exactly the same as the stairs window, so we can use the exact same division: 15 pieces of 30cm. Here I used the [Draft OrthoArray](Draft_OrthoArray.md) tool to copy over the two lines 15 times,and drew rectangles on top of them:

<img alt="" src=images/Arch_tutorial_39.jpg  style="width:1024px;">

Once this is done, we can create our window with the same method we already know. Another small useful trick, in case you haven\'t found it yourself already: When editing a window, if you change the name of a component, it actually creates a duplicate of it. So to create the 15 inner glass panels, instead of clicking 15 times the \"add\" button and fill 15 times the data, you can just keep editing one, and change its name and wire, it will create a copy each time.

After the window is rotated and moved into place, the atrium is complete:

<img alt="" src=images/Arch_tutorial_40.jpg  style="width:1024px;">

## Edits and fixes 

Now when we look at our back elevation, and compare it with the plan, we see that there are some differences that need to be fixed. Namely, the bedroom windows are smaller than I first thought, and we\'ll need to add some more walls. In order to do that properly, some floors need to be cut:

<img alt="" src=images/Arch_tutorial_41.jpg  style="width:1024px;">

We have of course several ways to do that, making a subtraction volume would be an easy way, but it would add unnecessary complexity to the model. Better to edit the base wire of each floors. This is where the [Draft Edit](Draft_Edit.md) mode comes into action. By expanding these floors in the tree view, then making their base wire visible, we can then double-click them to enter edit mode. There, we can move their points, or add or remove points. With this,editing our floor plates becomes easy.

<img alt="" src=images/Arch_tutorial_42.jpg  style="width:1024px;">

After some more sweat (the person who made those drawings obviously became pretty lazy when did this last elevation, much is drawn wrong), we finally have our complete house:

<img alt="" src=images/Arch_tutorial_43.jpg  style="width:1024px;">

Note the chimney tube, which is made from a circle I used to make a hole in the chimney block, that I extruded, then converted into a tube with the [Part Offset](Part_Offset.md) tool.


{{Note|Problems in objects|Sometimes an object you made can have problems. For example, the object it was based onto has been deleted, and the object can therefore not recalculate its shape. These are usually shown to you by a little red sign on their icon, and/or a warning in the output window. There is no generic recipe to fix these problems, because they can have many origins. But, the easiest way to solve them is often to delete them, and, if you didn't delete their base objects, recreate them.}}

## Output

Now, after all the hard work we passed through to build this model, comes the reward: What can we do with it? Basically, this is the big advantage of working with BIM, all our traditional architectural needs, such as 2d drawings (plans, sections, etc), renderings, and calculations (bills of quantities, etc) can all be extracted from the model. And, even better, regenerated every time the model changes. I\'ll show you here how to obtain these different documents.

### Preparations

Before starting to export stuff, one consideration is interesting to do: As you saw, our model is becoming increasingly complex, with a lot of relationships between objects. This can make subsequent calculation operations, such as cutting through the model, heavy. One quick way to magically \"simplify\" drastically your model, is to remove all of this complexity, by exporting it to the [STEP](http://en.wikipedia.org/wiki/ISO_10303-21) format. That format will preserve all your geometry, but will discard all the relationships and parametric constructions, keeping only the final shape. When reimporting that STEP file into FreeCAD, you will get a model that has no relationship, and a much smaller file size. Think of it as an \"output\" file, that you can regenerate anytime from your \"master\" file:

<img alt="" src=images/Arch_tutorial_44.jpg  style="width:1024px;">

### Exporting to IFC and other applications 

<img alt="" src=images/Arch_tutorial_45.jpg  style="width:400px;">

One of the very fundamental things you need when working with BIM is to be able to import and export [IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes) files. This is still a work in progress in FreeCAD. [IFC](Arch_IFC.md) format is already supported, and importing IFC files into FreeCAD is already pretty reliable. Exporting is still experimental, though, and has currently many limitations. However, things are bettering and we should get proper IFC export very soon.

[IFC export](Arch_IFC.md) requires very little setup, once the necessary software libraries are installed. You only need to recreate the building structure, which is needed in all IFC files, by adding an [Arch Building](Arch_Building.md) to your file, then an [Arch Floor](Arch_Floor.md), then moving all the groups of objects that compose your model in it. Make sure you leave your construction geometry (all the 2D stuff we\'ve been drawing) out of it to avoid making your IFC file unnecessarily heavy.

Another thing to set, is to check the \"Role\" property of structural elements. Since IFC has no \"generic\" structural element, like FreeCAD, we need to assign them roles (column, beam, etc\...) so the exporter knows what element to create in the IFC file.

In this case, we need our whole architectural system, so the IFC exporter can know if an object must be exported as a wall or a column, so we are using our \"master\" model, not our \"output\" model.

Once this is done, simply select your building object, and choose the \"Industry Foundation Classes\" format. Exporting to non-BIM applications, such as [Sketchup](http://www.sketchup.com/) is also easy, you have several export formats at your disposal, such as [Collada](Arch_DAE.md), STEP, IGES or OBJ.




### Rendering

FreeCAD also features a rendering module, the [Raytracing Workbench](Raytracing_Workbench.md). That workbench currently supports two render engines, [PovRay](http://www.povray.org/) and [LuxRender](http://www.luxrender.net). Since FreeCAD is not designed for image rendering, the features that the Raytracing workbench offer to you are somewhat limited. The best course of action when you want to do proper rendering, is to export your model to a mesh-based format such as OBJ or STL, and open it in an application more suited to rendering, such as [blender](http://www.blender.org). The image below has been rendered with blender\'s cycles engine:

<img alt="" src=images/Arch_tutorial_47.jpg  style="width:1024px;">

But, for a quick rendering, the Raytracing workbench can already do a good job, with the advantage of being very easy to setup, thanks to its templates system. This is a rendering of our model fully made within FreeCAD, with the Luxrender engine, using the \"indoor\" template.

<img alt="" src=images/Arch_tutorial_48.jpg  style="width:1024px;">

The Raytracing workbench still offers you very limited control over materials, but lighting and environments are defined in templates, so they can be fully customized.

### 2D drawings 

Certainly the most important use of BIM is to produce 2D drawings automatically. This is done in FreeCAD with the [Arch SectionPlane](Arch_SectionPlane.md) tool. This tool allows you to place a section plane object in the 3D view, that you can orient to produce plans, sections and elevations. Section planes must know what objects they must consider, so once you have created one, you must add objects to it with the [Arch Add](Arch_Add.md) tool. You can add individual objects, or, more conveniently, a group, a floor or a whole building. This allows you to easily change the scope of a certain section plane later, by adding or removing objects to/from that group. Any change to these objects gets reflected in the views produced by the section plane.

The section plane automatically produces cut views of the objects it intersects. In other words, to produce views instead of sections, you just need to place the section plane outside of your objects.

<img alt="" src=images/Arch_tutorial_49.jpg  style="width:1024px;">

The section planes can produce two different outputs: [shape](Part_Workbench.md) objects, that live in the same document as your 3D model, or [drawing views](Drawing_Workbench.md), that are made to use on a drawing sheet produced by the [Drawing workbench](Drawing_Workbench.md). Each of these behave differently, and has its own advantages.

**Shape views**

This output is produced by using the [Draft Shape2DView](Draft_Shape2DView.md) tool with a section plane selected. You produce a 2D view of the model directly in the 3D space, like on the image above. The main advantage here is that you can work on them using the [Draft](Draft_Workbench.md) tools (or any other standard tool of FreeCAD), so you can add texts, dimensions, symbols, etc:

<img alt="" src=images/Arch_tutorial_50.jpg  style="width:1024px;">

On the image above, two [Shape2D views](Draft_Shape2DView.md) have been produced for each section, one showing everything, the other showing only the cut lines. This allows us to give it a different line weight, and turn hatching on. Then, dimensions, texts and symbols have been added, and a couple of DXF blocks have been imported to represent the furniture. These views are then easy to export to DXF or DWG, and open in your favorite 2D CAD application, such as [LibreCAD](http://www.librecad.org) or [DraftSight](http://www.3ds.com/products-services/draftsight/overview/), where you can work further on them:

<img alt="" src=images/Arch_tutorial_51.jpg  style="width:1024px;">

Note that some features are still not supported by the [DXF/DWG exporter](Draft_DXF.md) so the result in your 2D application might differ a bit. For example, in the image above, I had to redo the hatching, and correct the position of some dimension texts. If you place your objects in different groups in FreeCAD, these become layers in your 2D CAD application.

**Drawing views**

The other kind of output that can be produced from [section planes](Arch_SectionPlane.md) is a [Drawing view](Drawing_Workbench.md). These are produced by using the [Draft Drawing](Draft_Drawing.md) tool with a section plane selected. This method has one big limitation compared to the previous one: you have limited possibilities to edit the results, and at the moment, things like dimensioning or hatching are still not natively supported.

On the other hand, the final output being easier to manipulate, and the graphical possibilities of the SVG format being huge, in the future, undoubtedly this will be the preferred method. At the moment, though, you\'ll get better results using the previous one.

<img alt="" src=images/Arch_tutorial_52.jpg  style="width:1024px;">

On the image above, the geometry is the direct output of the section plane, but some other Draft objects have been added, such as dimensions and hatched polygons, and another view object with same scale and offset values has been produced from them with the [Draft Drawing](Draft_Drawing.md) tool. In the future, such operations will be done directly on the Drawing page, leaving your model totally clean.

### Quantities extraction 

This is another very important task to be performed on BIM models. In FreeCAD, things look good right from the start, since the OpenCasCade kernel of FreeCAD already takes care of calculating lengths, areas and volumes for all the shapes it produces. Since all [Arch](Arch_Workbench.md) objects are solids, you are always guaranteed to be able to obtain a volume from them.

**Using spreadsheets**

To populate a spreadsheet with values extracted from the model the Arch\_Schedule tool can be used.

![](images/Arch_schedule_example03.jpg )

**The survey mode**

Another way to survey your model and extract values, is to use the [Arch Survey](Arch_Survey.md) mode. In this mode, you can click on points, edges, faces or double-click to select whole objects, and you get altitude, length, area or volume values, shown on the model, printed on the FreeCAD output window, and copied to the clipboard, so you can easily pick and paste values in another opened application

<img alt="" src=images/Arch_tutorial_54.jpg  style="width:1024px;">

## Conclusion

I hope this gives you a good overview of the available tools, be sure to refer to the [Arch Workbench](Arch_Workbench.md) and [Draft Workbench](Draft_Workbench.md) documentation for more (there are more tools that I didn\'t mention here), and, more generally, to the rest of the [FreeCAD documentation](Main_Page.md). Pay a visit to the [forum](http://forum.freecadweb.org) too, many problems can usually be solved there in no time, and follow my [blog](http://yorik.uncreated.net/guestblog.php?tag=freecad) for news about he Arch workbench development.

The file created during this tutorial can be found [here](http://yorik.uncreated.net/archive/projects/casa_artigas.fcstd)


{{Tutorials navi

}}  
