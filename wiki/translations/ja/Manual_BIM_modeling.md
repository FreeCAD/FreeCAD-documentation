# Manual:BIM modeling/ja
{{Manual:TOC}}


<div class="mw-translate-fuzzy">

BIMは[Building Information Modeling](https://ja.wikipedia.org/wiki/BIM)の略です。万人に認められた正確な定義はないですが、単純には今日における建築物や、橋梁・隧道（トンネル）等といった大型構造物のモデル化のされ方ということができます。BIMモデルは大抵3Dモデルに基づいており、更に素材の情報、他のオブジェクトやモデルとの関係性、施工や保全のための特別指示といった一連の付加的な情報を含んでいます。そしてこの付加情報により、構造耐力や原価、工期見積り、エネルギー消費の計算といったモデルの詳細分析が可能であるようなものです。


</div>


<div class="mw-translate-fuzzy">

FreeCADの[Archワークベンチは](Arch_Workbench.md)、BIMモデリングのための一連のツールや機能を実装しており、FreeCADの他の機能とも、目的こそ違えども緊密に統合され動作するようになっています: 実際他のワークベンチにおいて作成された如何なるオブジェクトもArchオブジェクトにすることができ、或はArchオブジェクトを生成するための元とすることができます。


</div>


<div class="mw-translate-fuzzy">

[PartDesign Workbenchにおけるのと](PartDesign_Workbench.md)同様、Archワークベンチにおいて作られるオブジェクトは実世界にて建てられることを意図しているため、**ソリッド**である必要があります。この点は通常Archのツールが自動的に実現し、またオブジェクトの妥当性を確認する機能をも提供しています。


</div>

本章では、この小さな建築物がどのようにモデル化されるかを見ていきましょう。

![](images/FreeCAD_BIMHouse.png )

-   Create a new document, and switch to the <img alt="" src=images/Workbench_BIM.svg  style="width:16px;"> [BIM Workbench](BIM_Workbench.md).
-   Open menu **Edit → Preferences → Draft → Grid and Snapping** and set:
    -   **Main lines every** `10`.
    -   **Grid spacing** `1000mm` to have a one meter-based grid, which is convenient for the size of our building.
    -   **Grid size** `100 lines`.
-   On the **snapping toolbar** make sure the <img alt="" src=images/Draft_Snap_Grid.svg  style="width:16px;"> [Snap grid](Draft_Snap_Grid.md) button is enabled, so we can use the grid as much as possible.
-   If you do not see the axes then click the <img alt="" src=images/Draft_ToggleGrid.svg  style="width:16px;"> [Toggle grid](Draft_ToggleGrid.md) button.
-   Set the [Working Plane](Draft_SelectPlane.md) to **XY** plane
-   Draw four lines with the <img alt="" src=images/Draft_Line.svg  style="width:16px;"> [Draft Line](Draft_Line.md) tool. You can enter coordinates manually, or simply pick the points on the grid with the mouse. We will be using meters for our dimensions:
    -   From point (0,0) to point (0,3)
    -   From point (0,3) to point (4,3)
    -   From point (4,3) to point (4,0)
    -   From point (4,0) to point (0,0)

![](images/Exercise_arch_03.jpg )

Notice that we consistently drew the lines in the same direction (clockwise). While this isn't required, it helps ensure that the walls we will build next have consistent left and right orientations. You might wonder why we didn't just draw a rectangle, which would have been simpler. However, using four separate lines gives us the opportunity to showcase additional BIM functionalities, such as how to combine multiple objects into one, which is an essential part of the workflow.

-   Once you have created the lines check their start and end points and adjust if necessary to get them exactly correct.

![](images/Manual-BIM_Modeling_-_Adjusting_Lines.png )

-   Select all four lines, then press the <img alt="" src=images/Arch_Wall.svg  style="width:16px;"> [Wall](Arch_Wall.md) button.
-   Set the walls\' **Height** to 3m (default).
-   Set **Alignment** property to **left**. Setting the Alignment property to the left ensures that the walls you create will be positioned to the left side of the lines you drew. In FreeCAD's BIM Workbench, walls are typically generated based on a reference line, and the left or right alignment dictates which side of the line the wall will be placed.

If you didn't draw the lines in the same order as instructed (clockwise), the orientation of some walls may be flipped, meaning they could be positioned on the opposite side of the line (to the right instead of the left). In that case, you would need to adjust the alignment to the right for those specific walls to ensure they all align consistently. Once this is set correctly, you\'ll have four walls that intersect at the corners, positioned on the inside of the baseline, forming the desired layout.

![](images/Exercise_arch_04.jpg )

After creating walls, the next step is to join them so they intersect properly. This is necessary when walls don\'t connect cleanly at their intersections. To do this, you select one wall as the \"host\" and add the other walls as \"additions\", merging their geometry with the host. All objects in the BIM Workbench can have multiple additions (which add geometry) or subtractions (which remove geometry). These relationships can be managed anytime by double-clicking the object in the tree, allowing for flexible adjustments to ensure the walls and other architectural elements integrate smoothly.

-   Select the four walls with **Ctrl** pressed, the last one being the wall that you chose to become the host
-   Press the <img alt="" src=images/Arch_Add.svg  style="width:16px;"> [Add](Arch_Add.md) button. The four walls have now been turned into one:

![](images/Exercise_arch_05.jpg )

The individual walls are however still accessible, by expanding the wall in the tree view.

-   Let\'s now place a door by pressing on the <img alt="" src=images/BIM_Door.svg  style="width:16px;"> [Door](BIM_Door.md) tool.
-   Begin by selecting the wall. While this step isn\'t required, it\'s a useful habit to develop. If an object is selected before starting an operation, the operation will automatically apply to that entity by default.
-   Set the <img alt="" src=images/View-axonometric.svg  style="width:16px;"> [Working Plane](Draft_SelectPlane.md) to **auto** so we are not restricted to the ground plane
-   Press the <img alt="" src=images/BIM_Door.svg  style="width:16px;"> [Door](BIM_Door.md) button.
-   In the door creation panel, select the **Glass door** preset, and set its **Width** to 1 m and its **Height** to 2.1m. You will notice that you can choose between various door types and set up their parameters as you wish. In FreeCAD a door is derived by an [window](Arch_Window.md) operation.
-   Make sure the <img alt="" src=images/Draft_Snap_Near.svg  style="width:16px;"> [Snap near](Draft_Snap_Near.md) option is turned on, so we can snap on faces
-   Place your door roughly on the middle of the front face of the wall:

![](images/FreeCAD_BIMDoor.png )

-   We can now set the precise location by expanding the wall and the window objects in the tree view and changing the **Placement** property of the base sketch of our door. Set its position to **x = 0.5 m, y = 0, z = 0**. Our door is now exactly where we want it:

![](images/FreeCAD_BIMDoorPos.png )

-   Let\'s place a window next to our door. Select the wall, press the <img alt="" src=images/Arch_Window.svg  style="width:16px;"> [Window](Arch_Window.md) tool, select the **Open 2-pane** preset, and place a **1m x 1m** window in the same face as the door. Set the placement of the underlying sketch to position **x = 0, y = 0, z = 1.1m**, so the upper line of the window is aligned to the top of the door.

![](images/FreeCAD_BIMWindow.png )

Windows are always based on sketches. You can easily create custom windows by first drawing a sketch on a face, then turning that sketch into a window by selecting it and clicking the window button. Afterward, you can define the window\'s parameters---such as which parts of the sketch should be extruded and by how much---by double-clicking the window in the tree view. Now, let\'s move on to creating a slab:

-   Set the [Working Plane](Draft_SelectPlane.md) to **XY** plane
-   Create a <img alt="" src=images/Draft_Rectangle.svg  style="width:16px;"> [rectangle](Draft_Rectangle.md) with a **length** of 5m, a height of **4m**, and place it at position x:-0.5m, y:-0.7m, z:0.
-   Select the rectangle
-   Click the <img alt="" src=images/BIM_Slab.svg  style="width:16px;"> [Slab](BIM_Slab.md) tool to create a slab from the rectangle
-   Keep the default values of 0.2m for the **height** property and set the normal **direction** to (0,0,-1), so the extrusion goes downward. While we could have moved the object 0.2m downward instead, it\'s a good practice to keep extruded objects aligned with their base profile to maintain consistency and accuracy in the model.
-   Set the **Ifc Type** property of the slab to **slab**. This is not necessary in FreeCAD, but is important for IFC export, as it will ensure that the object is exported with the correct IFC type.

![](images/FreeCAD_BIMSlab.png )

-   Let\'s put a roof over our heads now. We can easily do it by using the <img alt="" src=images/Arch_Roof.svg  style="width:16px;"> [Roof](Arch_Roof.md) tool.
-   Press the <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:16px;"> [Snap working plane](Draft_Snap_WorkingPlane.md) option to enable the drafting on all planes.
-   By choosing one of the top faces of our house press the <img alt="" src=images/Draft_SelectPlane.svg  style="width:16px;"> [Select plane](Draft_SelectPlane.md) button. The working plane is now set to that face.
-   Create a <img alt="" src=images/Draft_Rectangle.svg  style="width:16px;"> [rectangle](Draft_Rectangle.md), snapping to two opposite points of the walls:
-   On the **data** tab of the roof set the **Runs** parameter to 1600.
-   If you wish to change the color of the roof you can do so on the view tab

![](images/FreeCAD_BIMHouseg.png )

With that, our model is now complete. The next step is to organize it properly to ensure it exports correctly to the IFC format. IFC files require all building elements to be grouped within a **building** object, and optionally, within a specific **story**. Additionally, all buildings must be located on a **site**. However, FreeCAD\'s IFC exporter will automatically generate a default site if one isn\'t present, so we don\'t need to add it manually. It\'s important to properly structure the model to comply with IFC standards, ensuring smooth collaboration and compatibility with other BIM software. Proper organization will also help avoid any data loss or errors during the export process.

-   Select the walls, the slab, and the roof.
-   Press the <img alt="" src=images/Arch_Floor.svg  style="width:16px;"> [Floor](Arch_Floor.md) button
-   Select the floor we just created
-   Press the <img alt="" src=images/Arch_Building.svg  style="width:16px;"> [Building](Arch_Building.md) button

Our model is now ready to export:

![](images/FreeCAD_BIMExport.png )

The [IFC format](https://en.wikipedia.org/wiki/Industry_Foundation_Classes) is one of the most precious assets in a free BIM world, because it allows the exchange of data between any application and actor of the construction world, in an open manner (the format is open, free and maintained by an independent consortium). Exporting your BIM models as IFC ensures that anyone can see and analyze them, no matter the application used.

-   Select the top object you want to export, that is, the Building object.
-   Select menu **File -\> Export -\> Industry Foundation Classes** and save your file.
-   The resulting IFC file can now be opened in a wide range of applications and viewers (the image below shows the file opened in the free [IfcPlusPlus](http://www.ifcquery.com/) viewer). Checking the exported file in such a viewer application before distributing it to other people is important to check that all the data contained in the file is correct. FreeCAD itself can also be used to re-open the resulting IFC file.

![](images/FreeCAD_BIMIFC.png )

We can use the <img alt="" src=images/Workbench_TechDraw.svg  style="width:16px;"> [TechDraw Workbench](TechDraw_Workbench.md) to create a drawing of our building. The process is similar to what was shown in the previous section, so we won\'t go into too much detail here. Simply create a new view by using the <img alt="" src=images/TechDraw_PageDefault.svg  style="width:16px;"> [insert Default Page](TechDraw_PageDefault.md) option, then select the view you want to display in the drawing and add dimensions where necessary. This will allow us to create a professional 2D representation of the 3D model for documentation or presentation purposes.

![](images/FreeCAD_BIMHouseDrawing.png )

Our page is now ready, and we can export it to SVG or DXF formats, or print it. The SVG format allows you to open the file using illustration applications such as [Inkscape](http://www.inkscape.org), with which you can quickly enhance technical drawings and turn them into much nicer presentation drawings. It offers many more possibilities than the DXF format.

## Downloads

-   The file produced during this exercise: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/house.FCStd>
-   The IFC file exported from the above file: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/house.ifc>
-   The SVG file exported from the above file: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/house.svg>

## Related

-   [BIM Workbench](BIM_Workbench.md)
-   [The Arch Workbench](Arch_Workbench.md)
-   [The Draft working plane](Draft_SelectPlane.md)
-   [The Draft snapping settings](Draft_Snap.md)
-   [The expressions system](Expressions.md)
-   [The IFC format](https://en.wikipedia.org/wiki/Industry_Foundation_Classes)
-   [IfcOpenShell](http://ifcopenshell.org)
-   [IfcPlusPlus](http://www.ifcquery.com)
-   [Inkscape](http://www.inkscape.org)





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Manual:BIM modeling/ja
