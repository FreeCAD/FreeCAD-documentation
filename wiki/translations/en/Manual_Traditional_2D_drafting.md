# Manual:Traditional 2D drafting/en
{{Manual:TOC}}

You might be interested by FreeCAD because you already have some technical drawing experience, for example with software like [AutoCAD](https://en.wikipedia.org/wiki/AutoCAD). Or you already know something about design, or you prefer to draw things before building them. In any case, FreeCAD features a more traditional workbench, with tools found in most 2D CAD applications: The [Draft Workbench](Draft_Workbench.md).

The Draft Workbench, although it adopts ways of working inherited from the traditional 2D CAD world, is not limited at all to the 2D realm. All its tools work in the whole 3D space and many of the Draft tools, for example <img alt="" src=images/Draft_Move.svg  style="width:16px;"> [Move](Draft_Move.md) or <img alt="" src=images/Draft_Rotate.svg  style="width:16px;"> [Rotate](Draft_Rotate.md), are commonly used all over FreeCAD because they are often more intuitive than changing placement parameters manually.

Among the tools offered by the Draft Workbench, you will find traditional drawing tools like <img alt="" src=images/Draft_Line.svg  style="width:16px;"> [Line](Draft_Line.md), <img alt="" src=images/Draft_Circle.svg  style="width:16px;"> [Circle](Draft_Circle.md), or <img alt="" src=images/Draft_Wire.svg  style="width:16px;"> [Wire](Draft_Wire.md) (polyline), modification tools like <img alt="" src=images/Draft_Move.svg  style="width:16px;"> [Move](Draft_Move.md), <img alt="" src=images/Draft_Rotate.svg  style="width:16px;"> [Rotate](Draft_Rotate.md) or <img alt="" src=images/Draft_Offset.svg  style="width:16px;"> [Offset](Draft_Offset.md), a [working plane/grid system](Draft_SelectPlane.md) that allows you to define precisely in which plane you are working, and a complete [snapping system](Draft_Snap.md) that makes it very easy to draw and position elements precisely in relation to each other.

To showcase the workflow and possibilities of the Draft Workbench, we will walk through a simple exercise, the result of which will be this little drawing, showing the floor plan of a small house that contains only a kitchen top (A pretty absurd floor plan, but we can do what we want here, can\'t we?):

![](images/Exercise_cabin_01.jpg )

-   Switch to the **Draft Workbench**
-   As in all technical drawing applications, it is wise to set up your environment correctly, it will save you a lot of time. Configure the [grid and working plane](Draft_SelectPlane.md), [Text](Draft_Text.md) and [Dimension](Draft_Dimension.md) settings to your liking in menu **Edit → Preferences → Draft**. In this exercise, however, we will act as if these settings were left at their default values.

![](images/Freecad_draft_options_01.jpg )

-   One option might need your attention, though: the \"**Fill objects with faces whenever possible**\" option. If this is marked, closed objects like rectangles or circles will be filled with a face by default, which can make snapping to underlying objects difficult. You can either turn this option off now, or, later on, turn the \"**Make Face**\" property of each individual object off, to prevent them from creating a face.

-   The Draft Workbench also has two special toolbars: One with **visual settings**, where you can change the current working plane, turn [construction mode](Draft_ToggleConstructionMode.md) on/off, set the line color, face color, line weight and text size to be used for new objects, and another one with **snap locations**. There, you can turn the grid on/off and set/unset individual [Snap locations](Draft_Snap.md):

![](images/Draft_toolbars.jpg )

-   Turning on all the snap buttons is convenient, but also makes drawing slower, as more calculation needs to be done when you move the mouse cursor. It is often better to keep only the ones you will actually use.

-   Let\'s start by turning **construction mode** on, which will allow us to draw some guidelines on which we will draw our final geometry.
-   If you wish, set the **working plane** to **XY**. If you do this, the working plane won\'t change, no matter the current view. If not, the working plane will adapt automatically to the current view, and you should take care of staying in top view whenever you want to draw on the XY (ground) plane.
-   Then, select the <img alt="" src=images/Draft_Rectangle.svg  style="width:16px;"> [Rectangle](Draft_Rectangle.md) tool and draw a rectangle, starting at point (0,0,0), of 2 meters by 2 meters (leave the Z at zero). Note that most of the Draft commands can be fully performed from the keyboard, without touching the mouse, using their two-letter shortcut. Our first 2x2m rectangle can be done like this: re 0 **Enter** 0 **Enter** 0 **Enter** 2m **Enter** 2m **Enter** 0 **Enter**.
-   Duplicate that rectangle by 15cm inside, using the <img alt="" src=images/Draft_Offset.svg  style="width:16px;"> [Offset](Draft_Offset.md) tool, turning its Copy mode on, and giving it a distance of 15cm:

![](images/Exercise_cabin_02.jpg )

-   We can then draw a couple of vertical lines to define where our doors and windows will be placed, using the <img alt="" src=images/Draft_Line.svg  style="width:16px;"> [Line](Draft_Line.md) tool (note that the \"relative\" mode box should be unchecked for this step). The crossing of these lines with our two rectangles will give us useful intersections to snap our walls to. Draw the first line from point (15cm, 1m, 0) to point (15cm, 3m, 0).
-   Duplicate that line 5 times, using the <img alt="" src=images/Draft_Move.svg  style="width:16px;"> [Move](Draft_Move.md) tool with Copy mode turned on. Turn also the Relative mode on, which will allow us to define movements in relative distances, which is easier than calculating the exact position of each line. Perform each move operation in sequence on the line that was created immediately prior. Give each new copy any start point, you can leave it at (0,0,0) for example, and the following relative endpoints:
    -   line001: x: 10cm
    -   line002: x: 120cm
    -   line003: x: -55cm, y: -2m
    -   line004: x: 80cm
    -   line005: x: 15cm

![](images/Exercise_cabin_03.jpg )

-   That is all we need now, so we can switch construction mode off. Check that all the construction geometry has been placed into a \"Construction\" group, which makes it easy to hide it all at once or even delete it completely later on.
-   Now let\'s draw our two wall pieces using the <img alt="" src=images/Draft_Wire.svg  style="width:16px;"> [Wire](Draft_Wire.md) tool. Make sure the <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:16px;"> [intersection snap](Draft_Snap.md) is turned on, as we will need to snap to the intersections of our lines and rectangles. Draw two wires as follows, by clicking all the points of their contours. To close them, either click on the first point again, or press the **Close** button:

![](images/Exercise_cabin_04.jpg )

-   We can change their default grey color to a nice hatch pattern, by selecting both walls, then setting their **Pattern** property to **Simple**, and their **Pattern size** to your liking, for example **0.005**.

![](images/Exercise_cabin_05.jpg )

-   We can now hide the construction geometry by right-clicking the Construction group and choose **Hide Selection**.
-   Let\'s now draw the windows and doors. Make sure the <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:16px;"> [midpoint snap](Draft_Snap.md) is turned on, and draw six lines as follow:

![](images/Exercise_cabin_06.jpg )

-   We will now change the door line to create an opened door symbol. Start by rotating the line using the <img alt="" src=images/Draft_Rotate.svg  style="width:16px;"> [Rotate](Draft_Rotate.md) tool. Click the endpoint of the line as rotation center, give it a start angle of **0**, and an end angle of **-90**.
-   Then create the opening arc with the <img alt="" src=images/Draft_Arc.svg  style="width:16px;"> [Arc](Draft_Arc.md) tool. Pick the same point as the rotation center we used in the previous step as center, click the other point of the line to give the radius, then the start and end points as follow:

![](images/Exercise_cabin_07.jpg )

-   We can now start placing some furniture. To begin with, let\'s place a counter by drawing a rectangle from the upper left inner corner, and giving it a width of 170cm and a height of -60cm. In the image below, the **Transparency** property of the rectangle is set to 80%, to give it a nice furniture look.
-   Then let\'s add a sink and a cookertop. Drawing these kinds of symbols by hand can be very tedious, and they are usually easy to find on the internet, for example on <http://www.cad-blocks.net> . In the **Downloads** section below, for convenience, we separated a sink and a cookertop from this project, and saved them as DXF files.You can download these two files by visiting the links below, and right-clicking the **Raw** button, then choosing **save as**.
-   Inserting a DXF file into an opened FreeCAD document can be done either by choosing the **File → Import** menu option, or by dragging and dropping the DXF file from your file explorer into the FreeCAD window. The contents of the DXF files might not appear right on the center of your current view, depending on where they were in the DXF file. You can use menu **View → Standard views → Fit all** to zoom out and find the imported objects. Insert the two DXF files, and move them to a suitable location on the tabletop:

![](images/Exercise_cabin_08.jpg )

-   We can now place a couple of dimensions using the <img alt="" src=images/Draft_Dimension.svg  style="width:16px;"> [Dimension](Draft_Dimension.md) tool. Dimensions are drawn by clicking 3 points: the start point, an end point, and a third point to place the dimension line. To make horizontal or vertical dimensions, even if the two first points are not aligned, press **Shift** while clicking the second point.
-   You can change the position of a dimension text by double-clicking the dimension in the tree view. A control point will allow you to move the text graphically. In our exercise, the \"0.15\" texts have been moved away for better clarity.
-   You can change the contents of the dimension text by editing their **Override** property. In our example, the texts of the door and window dimensions have been edited to indicate their heights:

![](images/Exercise_cabin_09.jpg )

-   Let\'s add some description texts using the <img alt="" src=images/Draft_Text.svg  style="width:16px;"> [Text](Draft_Text.md) tool. Click a point to position the text, then enter the lines of text, pressing Enter after each line. To finish, press Enter twice.
-   The indication lines (also called \"leaders\") that link the texts to the item they are describing are simply done with the Wire tool. Draw wires, starting from the text position, to the place being described. Once that is done, you can add a bullet or arrow at the end of the wires by setting their **End Arrow** property to **`True`**

![](images/Exercise_cabin_10.jpg )

-   Our drawing is now complete! Since there are quite a number of objects there, it would be wise do some cleaning and restructure everything into nice groups, to make the file easier to understand for other people:

![](images/Exercise_cabin_11.jpg )

-   We can now print our work by placing it on a Drawing sheet, which we will show later in this manual, or directly export our drawing to other CAD applications, by exporting it to a DXF file. Simply select our \"Floor plan\" group, select menu **File → Export**, and select the Autodesk DXF format. The file can then be opened in any other 2D CAD application such as [LibreCAD](http://www.librecad.org). You might notice some differences, depending on the configurations of each application.

![](images/Exercise_cabin_12.jpg )

-   The most important thing about the Draft Workbench, however, is that the geometry you create with it can be used as a base or easily extruded into 3D objects, simply by using the <img alt="" src=images/Part_Extrude.svg  style="width:16px;"> [Part_Extrude](Part_Extrude.md) tool from the [Part Workbench](Part_Workbench.md), or, to stay in Draft, the <img alt="" src=images/Draft_Trimex.svg  style="width:16px;"> [Trimex](Draft_Trimex.md) (Trim/Extend/Extrude) tool, which under the hood performs a Part Extrusion, but does it \"the Draft way\", that is, allows you to indicate and snap the extrusion length graphically. Experiment extruding our walls as shown below.
-   By pressing the <img alt="" src=images/Draft_SelectPlane.svg  style="width:16px;"> [working plane](Draft_SelectPlane.md) button after selecting a face of an object, you are also able to place the working plane anywhere, and therefore draw Draft objects in different planes, for example on top of the walls. These can then be extruded to form other 3D solids. Experiment setting the working plane on one of the top faces of the walls, then draw some rectangles up there.

![](images/Exercise_cabin_13.jpg )

-   All kinds of openings can also be done as easily by drawing Draft objects on the faces of walls, then extruding them, then using the boolean tools from the Part Workbench to subtract them from another solid, as we saw in the previous chapter.

Fundamentally, what the Draft Workbench does is to provide graphical ways to create basic Part operations. While in Part you will usually position objects by setting their placement parameter, in Draft you can do it on-screen. There are times when one is better, other times when the other is preferable. Don\'t forget, you can create [custom toolbars](Interface_Customization.md) in one of these workbenches, add the tools from the other, and get the best of both worlds.

## Downloads

-   The file created during this exercise: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/cabin.FCStd>
-   The sink DXF file: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/sink.dxf>
-   The cookertop DXF file: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/cooktop.dxf>
-   The final DXF file produced during this exercise: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/cabin.dxf>

## Related

-   [The Draft Workbench](Draft_Workbench.md)
-   [Snapping](Draft_Snap.md)
-   [The Draft working plane](Draft_SelectPlane.md)



---
![](images/Button_right.svg) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [Draft](Category_Draft.md) > Manual:Traditional 2D drafting/en
