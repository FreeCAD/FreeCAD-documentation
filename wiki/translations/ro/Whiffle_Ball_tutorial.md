---
- TutorialInfo:/ro
   Topic: Whiffle Ball (Part Module)
   Level: Beginner
   Time:
   Author:r-frank
   FCVersion:0.16.6703
   Files:[https://github.com/FreeCAD/Examples/blob/master/Whiffle_Ball_Tutorial_ExampleFiles/WhiffleBall_Tutorial_FCWiki.FCStd?raw=true] Whiffle Ball
---

# Whiffle Ball tutorial/ro




<div class="mw-translate-fuzzy">




</div>




<div class="mw-translate-fuzzy">

### Introducere

Acest tutorial este aici pentru a vă învăța cum se folosește Atelierul [Part Workbench](Part_Workbench.md). Veți exersa:

-   inserare primitive geometrice
-   schimbarea valorilor primitivelor
-   utilizarea plasamentului
-   realizarea de operații booleene


</div>

This tutorial was originally written by Roland Frank (†2017, r-frank), and it was rewritten and illustrated by vocx.

This tutorial is here to teach you how to use the [Part Workbench](Part_Workbench.md).

The Part Workbench was the first workbench developed. It provides the basic geometrical elements that can be used as building blocks for other workbenches. The Part Workbench is meant to be used in a traditional [constructive solid geometry](constructive_solid_geometry.md) (CSG) workflow. For a more modern workflow using sketches, pads, and features, use the [PartDesign Workbench](PartDesign_Workbench.md).

You will practice:

-   inserting primitives
-   changing parameters of those primitive objects
-   modifying their [placement](placement.md)
-   doing boolean operations

![](images/10_T03_Part_ball_fillet.png ) 
*Final model of the wiffle ball*




<div class="mw-translate-fuzzy">

### Setarea formelor elementare 

1.  Comuntați pe Modulul Piese [Part Workbench](Part_Workbench.md)
2.  Creați un nou document făcând click pe ** File** → ** New**
3.  Inserați o casetă făcând click pe <img alt="" src=images/Part_Box.png  style="width:32px;">
4.  Asigurați-vă că (\"cube\") este selectat în vederea arborescentă
5.  Change the dimensions of the box (see data-tab) to
    1.  Length= 90 mm
    2.  Width= 90 mm
    3.  Heigth= 90 mm
6.  Click into the value field of placement-row in data-tab so that ** ...** appears on right side
7.  Click on ** ...** to change the placement of the box
    1.  X: -45 mm
    2.  Y: -45 mm
    3.  Z: -45 mm
8.  Click on ** OK** to close dialog
9.  Insert box (\"cube001\") by clicking on <img alt="" src=images/Part_Box.png  style="width:32px;">
10. Make sure the box (\"cube001\") is selected in tree view
11. Change the dimensions of the box (\"cube001\") (see data-tab) to
    1.  Length= 80 mm
    2.  Width= 80 mm
    3.  Heigth= 80 mm
12. Change the placement of the box (\"cube001\") to
    1.  X: -40 mm
    2.  Y: -40 mm
    3.  Z: -40 mm
13. Click <img alt="" src=images/Part_Cylinder.png  style="width:32px;"> to insert a cylinder (\"cylinder\")
14. Make sure the cylinder (\"cylinder\") is selected in tree view
15. Change radius of cylinder to be 27,5 mm, change height to be 120 mm
16. Change placement values of \"cylinder\" to be
    1.  X: 0 mm
    2.  Y: 0 mm
    3.  Z: -60 mm
17. Click <img alt="" src=images/Part_Cylinder.png  style="width:32px;"> to insert a cylinder (\"cylinder001\")
18. Change radius of \"cylinder001\" to be 27,5 mm, change height to be 120 mm
19. Choose Edit \> Duplicate selection from the top menu to get another cylinder (\"cylinder002\")
20. Make sure \"cylinder001\" is selected in tree view
21. Change placement values of \"cylinder001\" to be
    1.  Y: 60 mm
    2.  Rotation axis with angle
    3.  Axis: X
    4.  Angle: 90°
22. Click on ** OK** to apply values and close dialog
23. Make sure \"cylinder002\" is selected in tree view
24. Change placement values of \"cylinder001\" to be
    1.  X: -60 mm
    2.  Rotation axis with angle
    3.  Axis: Y
    4.  Angle: 90°
25. Click on ** OK** to apply values and close dialog
26. Click on <img alt="" src=images/View-axometric.png  style="width:32px;"> to change to axometric view
27. Click on <img alt="" src=images/View-zoom-all.png  style="width:32px;"> to zoom to fit all
28. Select \"cube001\", \"cylinder\", \"cylinder001\" and \"cylinder002\" and fuse them by clicking <img alt="" src=images/Part_Fuse.png  style="width:32px;">
29. Select \"cube\" and \"fusion\", but make sure, that \"cube\" is selected FIRST
30. Apply a boolean cut by clicking <img alt="" src=images/Part_Cut.png  style="width:32px;">
31. Forma de bază finalizată ar trebui să arate astfel:


</div>


<div class="mw-translate-fuzzy">

**Tip:** Dacă ați selectat ceva greșit sau doriți doar să eliminați rapid totul,
doar faceți clic pe (OpenInventor Navigation-Style: CTRL-Click),


</div>

## Insert primitive cubes 

2\. Insert a primitive cube by clicking on **<img src="images/Part_Box.svg" width=16px> [Box](Part_Box.md)**.

:   2.1. Select `Cube` in the [tree view](tree_view.md).
:   2.2. Change the dimensions in the **Data** tab of the [property editor](property_editor.md).
:   2.3. Change **Length** to `90 mm`.
:   2.4. Change **Width** to `90 mm`.
:   2.5. Change **Height** to `90 mm`.

3\. In the **Data** tab of the [property editor](property_editor.md), click on the **Placement** value so the ellipsis button **...** appears on the right.

:   3.1. Press on the ellipsis to launch the [Placement](Std_Placement.md) dialog.
:   3.2. Change the **Translation** values.
:   3.3. Change **X** to `-45 mm`.
:   3.4. Change **Y** to `-45 mm`.
:   3.5. Change **Z** to `-45 mm`.
:   3.6. Press the **OK** button to close the dialog.

4\. Repeat the process, inserting a second, smaller cube by clicking on **<img src="images/Part_Box.svg" width=16px> [Box](Part_Box.md)**.

:   4.1. The second cube will be created with the same name, but with an additional number to distinguish the object.
:   4.2. Select `Cube001` in the [tree view](tree_view.md), and change the dimensions and placement like with the previous object.
:   4.3. Change **Length** to `80 mm`.
:   4.4. Change **Width** to `80 mm`.
:   4.5. Change **Height** to `80 mm`.
:   4.6. Open the [Placement](Std_Placement.md) dialog.
:   4.7. Change **X** to `-40 mm`.
:   4.8. Change **Y** to `-40 mm`.
:   4.9. Change **Z** to `-40 mm`.
:   4.10. Press the **OK** button to close the dialog.

## Change visual properties 

5\. The previous operations create a smaller cube inside a bigger cube. To visualize this, we can modify the **View** properties in the [property editor](property_editor.md).

:   5.1. Select `Cube001`, the smaller cube, in the [tree view](tree_view.md), and change the color. In the **View** tab, click on the **Shape Color** value to open the **Select color** dialog, then choose a green color; also change the value of **Line Width** to `2.0`.
:   5.2. Select `Cube`, the larger cube, in the [tree view](tree_view.md). In the **View** tab, change the value of **Transparency** to `70`.

![](images/01_T03_Part_cubes_visibility.png ) 
*Solid cube inside another solid cube*

## Insert primitive cylinders 

6\. Insert a primitive cylinder by clicking on **<img src="images/Part_Cylinder.svg" width=16px> [Cylinder](Part_Cylinder.md)**.

:   6.1. Select `Cylinder` in the [tree view](tree_view.md).
:   6.2. Change the dimensions in the **Data** tab of the [property editor](property_editor.md).
:   6.3. Change **Radius** to `27.5 mm`.
:   6.4. Change **Height** to `120 mm`.
:   6.5. Open the [Placement](Std_Placement.md) dialog.
:   6.6. Change **Z** to `-60 mm`.
:   6.7. Press the **OK** button to close the dialog.

7\. Repeat the process, inserting a second cylinder by clicking on **<img src="images/Part_Cylinder.svg" width=16px> [Cylinder](Part_Cylinder.md)**.

:   7.1. The second cylinder will be created with the same name, but with an additional number to distinguish the object.
:   7.2. Select `Cylinder001` in the [tree view](tree_view.md), and change the dimensions and placement like with the previous object.
:   7.3. Change **Radius** to `27.5 mm`.
:   7.4. Change **Height** to `120 mm`.
:   7.5. Open the [Placement](Std_Placement.md) dialog.
:   7.6. Change **Y** to `60 mm`.
:   7.7. Change the **Rotation** to `Rotation axis with angle`; **Axis** to `X` (by setting the `X`, `Y` and `Z` values of the axis inputboxes to `1`, `0` and `0` respectively), and **Angle** to `90 deg`.
:   7.8. Press the **OK** button to close the dialog.

8\. Insert another cylinder. This time create a duplicate so that the radius and height don\'t have to be changed, only its placement.

:   8.1. Select `Cylinder001` in the [tree view](tree_view.md), and go to the menu **Edit → [Duplicate selection](Std_DuplicateSelection.md)**. This will create `Cylinder002`.
:   8.2. Open the [Placement](Std_Placement.md) dialog.
:   8.3. Change **X** to `-60 mm`, and change **Y** back to `0 mm`.
:   8.4. Change the **Rotation** to `Rotation axis with angle`; **Axis** to `Y`, and **Angle** to `90 deg`.
:   8.5. Press the **OK** button to close the dialog.

## Change visual properties 

9\. The previous operations create three cylinders that intersect with each other, and also intersect the cubes. To visualize this better we can modify the **View** properties in the [property editor](property_editor.md).

:   9.1. Select `Cube001`, the smaller cube, in the [tree view](tree_view.md), and change the transparency. In the **View** tab, change the value of **Transparency** to `70`.
:   9.2. Select `Cylinder`, in the **View** tab, click on the **Shape Color** value to open the **Select color** dialog, then choose a red color.
:   9.3. Select `Cylinder001`, in the **View** tab, click on the **Shape Color** value to open the **Select color** dialog, then choose a blue color.
:   9.4. Select `Cylinder002`, in the **View** tab, click on the **Shape Color** value to open the **Select color** dialog, then choose a pink color.
:   9.5. Select the three cylinders, in the **View** tab also change the value of **Line Width** to `2.0`.

![](images/02_T03_Part_cylinders_visibility.png ) 
*Solid cylinders that intersect themselves and the solid cubes.*

## Fuse and cut 

10\. In the [tree view](tree_view.md), select `Cube001` (the inner, smaller cube), and the tree cylinders, then press **[<img src=images/Part_Fuse.svg style="width:16px"> [Fuse](Part_Fuse.md)**. This will create a `Fusion` object.

11\. Then perform a boolean cut of the `Cube` (larger cube) and the new `Fusion` object.

:   11.1. In the [tree view](tree_view.md) select `Cube` first, and then `Fusion`.
:   11.2. Then press **[<img src=images/Part_Cut.svg style="width:16px"> [Cut](Part_Cut.md)**. This will create a `Cut` object.
:   
    **Note:**the order in which you select the objects is important for the cut operation. The base object is selected first, and the subtracting object comes at the end.
:   11.3. If the colors look strange, select the new `Cut` object, go to the **View** tab, click on the **Shape Color** value to open the **Select color** dialog, then choose a gray color; also change the value of **Line Width** to `2.0`.

![](images/03_T03_Part_cube_cut.png ) 
*Hollow shape produced from cutting a cube and three cylinders from a bigger cube.*

## Insert primitive cubes to cut the corners of the partial solid 

Now we\'ll create more cubes that will be used as cutting tools to trim the corners of the previously obtained `Cut` object.

12\. Click on **<img src="images/Part_Box.svg" width=16px> [Box](Part_Box.md)**.

:   12.1. Select `Cube002` in the [tree view](tree_view.md), and change the dimensions and placement.
:   12.2. Change **Length** to `140 mm`.
:   12.3. Change **Width** to `112 mm`.
:   12.4. Change **Height** to `112 mm`.
:   12.5. Open the [Placement](Std_Placement.md) dialog.
:   12.6. Change **X** to `-70 mm`.
:   12.7. Change **Y** to `-56 mm`.
:   12.8. Change **Z** to `-56 mm`.
:   12.9. Press **OK**.

13\. Click on **<img src="images/Part_Box.svg" width=16px> [Box](Part_Box.md)**.

:   13.1. Select `Cube003` in the [tree view](tree_view.md), and change the dimensions and placement.
:   13.2. Change **Length** to `180 mm`.
:   13.3. Change **Width** to `180 mm`.
:   13.4. Change **Height** to `180 mm`.
:   13.5. Open the [Placement](Std_Placement.md) dialog.
:   13.6. Change **X** to `-90 mm`.
:   13.7. Change **Y** to `-90 mm`.
:   13.8. Change **Z** to `-90 mm`.
:   13.9. Press **OK**.

We\'ll duplicate the previous two objects again to use once more as cutting objects.

14\. Select only `Cube002` in the [tree view](tree_view.md), and go to **Edit → [Duplicate selection](Std_DuplicateSelection.md)**. This will create `Cube004`.

15\. Select only `Cube003` in the [tree view](tree_view.md), and go to **Edit → [Duplicate selection](Std_DuplicateSelection.md)**. This will create `Cube005`.

16\. To visualize this better we can modify the **View** properties in the [property editor](property_editor.md).

:   16.1. Select the `Cut` object, in the **View** tab, click on the **Shape Color** value to open the **Select color** dialog, then choose a blue color.
:   16.2. Select all new cubes, `Cube002`, `Cube003`, `Cube004`, and `Cube005`, in the **View** tab, change the value of **Transparency** to `80`.

![](images/04_T03_Part_cube_additional.png ) 
*Additional external cubes that will be used as cutting objects for the internal solid.*




<div class="mw-translate-fuzzy">

### Scurtături partea 1 

1.  Insert box (\"cube002\") by clicking on <img alt="" src=images/Part_Box.png  style="width:32px;">
2.  Change the dimensions of the box (\"cube002\") (see data-tab) to
    1.  Length= 140 mm
    2.  Width= 112 mm
    3.  Heigth= 112 mm
3.  Change the placement of the box (\"cube002\") to
    1.  X: -70 mm
    2.  Y: -56 mm
    3.  Z: -56 mm
4.  Insert box (\"cube003\") by clicking on <img alt="" src=images/Part_Box.png  style="width:32px;">
5.  Change the dimensions of the box (\"cube003\") (see data-tab) to
    1.  Length= 180 mm
    2.  Width= 180 mm
    3.  Heigth= 180 mm
6.  Change the placement of the box (\"cube003\") to
    1.  X: -90 mm
    2.  Y: -90 mm
    3.  Z: -90 mm
7.  Make sure \"cube002\" is selected in tree view, otherwise select it
8.  Choose Edit \> Duplicate selection from the top menu to get another box (\"cube004\")
9.  Make sure \"cube003\" is selected in tree view, otherwise select it
10. Choose Edit \> Duplicate selection from the top menu to get another box (\"cube005\")
11. Select \"cube003\" and \"cube002\", but make sure, that \"cube003\" is selected FIRST
12. Activate menu to change placement
13. Tick option \"Apply incremental changes to object placement\", notice that all values are reset \...
14. Choose \"Rotation: X-Axis\" and \"Angle: 45°\" and click on ** Apply**
15. Choose \"Rotation: Z-Axis\" and \"Angle: 45°\" and click on ** Apply**
16. Click on ** OK** to close the dialog
17. Apply a boolean cut by clicking <img alt="" src=images/Part_Cut.png  style="width:32px;">, the resulting object will be named \"cut001\"


</div>

17\. In the [tree view](tree_view.md) select `Cube002` and `Cube003`.

:   17.1. Open the [Placement](Std_Placement.md) dialog.
:   17.2. Tick the option **Apply incremental changes**; notice that all **Translation** values are reset to zeroes.
:   17.3. Change the **Rotation** to `Rotation axis with angle`; **Axis** to `X`, and **Angle** to `45 deg`, then click on **Apply**. This will apply a rotation around the X-axis, and will reset the **Angle** field to zero.
:   17.4. Change the **Rotation** again, now **Axis** to `Z`, and **Angle** to `45 deg`, then click on **Apply**. This will apply a rotation around the local Z-axis, and will reset the **Angle** field to zero.
:   17.5. Click on **OK** to close the dialog.

18\. In the [tree view](tree_view.md) de-select the objects; then select `Cube003` first, the bigger cube, and then `Cube002`, the smaller cube.

:   18.1. Then press **[<img src=images/Part_Cut.svg style="width:16px"> [Cut](Part_Cut.md)**. This will create `Cut001`. This is a hollowed body which intersects the initial `Cut` only at certain corners.

19\. To visualize this better we can modify the **View** properties in the [property editor](property_editor.md).

:   19.1. Select `Cube004` and `Cube005`, in the **View** tab, then change the value of **Visibility** to `false`, or press **Space** in the keyboard.
:   19.2. Select `Cut001`, click on the **Shape Color** value to open the **Select color** dialog, then choose a red color; also change the value of **Transparency** to `90`.

![](images/05_T03_Part_cube_additional_cut_1.png ) 
*A rotated, hollowed solid, which will be used as a cutting object for some corners of the internal solid.*




<div class="mw-translate-fuzzy">

### Scurtături partea 2 

1.  Selectați \"cube005\" and \"cube004\", dar asigurați-vă că \"cube005\" este PRIMUL selectat
2.  Activați meniul de schimbarea amplasament
3.  Bifați opțiunea \"Apply incremental changes to object placement\", notice that all values are resetted \...
4.  Alegeți \"Rotation: X-Axis\" și \"Angle: 45°\" apoi faceți clicl pe ** Apply**
5.  alegeți \"Rotation: Z-Axis\" și \"Angle: -45°\" și click pe ** Apply**
6.  Click pe ** OK** pentru a închide dialogul
7.  Apicați boolean cut făcând click <img alt="" src=images/Part_Cut.png  style="width:32px;">, obiectul rezultat va fi numit \"cut002\"
8.  Click pe <img alt="" src=images/View-axometric.png  style="width:32px;"> pentru a schimba vederea axonometrică
9.  Click pe <img alt="" src=images/View-zoom-all.png  style="width:32px;"> pentru a face prin zoom toate vizibile

Dacă totul a mers bine, modelul dvs. ar trebui să arate astfel:


</div>

20\. In the [tree view](tree_view.md) select `Cut001`, in the **View** tab, change the value of **Visibility** to `false`, or press **Space** in the keyboard.

21\. In the [tree view](tree_view.md) select `Cube004` and `Cube005`, in the **View** tab, change the value of **Visibility** to `true`, or press **Space** in the keyboard.

:   21.1. Open the [Placement](Std_Placement.md) dialog.
:   21.2. Tick the option **Apply incremental changes**; notice that all **Translation** values are reset to zeroes.
:   21.3. Change the **Rotation** to `Rotation axis with angle`; **Axis** to `X`, and **Angle** to `45 deg`, then click on **Apply**. This will apply a rotation around the X-axis, and will reset the `Angle` field to zero.
:   21.4. Change the **Rotation** again, now **Axis** to `Z`, and **Angle** to `-45 deg`, then click on **Apply**. This will apply a rotation around the local Z-axis, and will reset the **Angle** field to zero.
:   21.5. Click on **OK** to close the dialog.

22\. In the [tree view](tree_view.md) de-select the objects; then select `Cube005` first, the bigger cube, and then `Cube004`, the smaller cube.

:   22.1. Then press **[<img src=images/Part_Cut.svg style="width:16px"> [Cut](Part_Cut.md)**. This will create `Cut002`. This is a hollowed body which intersects the initial `Cut` only at certain corners.

23\. To visualize this better we can modify the **View** properties in the [property editor](property_editor.md).

:   23.1. Select `Cut002`, click on the **Shape Color** value to open the **Select color** dialog, then choose a pink color; also change the value of **Transparency** to `90`.

![](images/06_T03_Part_cube_additional_cut_2.png ) 
*A rotated, hollowed solid, which will be used as a cutting object for some corners of the internal solid.*




<div class="mw-translate-fuzzy">

### Finalizarea modelului 

1.  Selectați \"cut\" și \"cut001\", dar asigurați-vă că \"cut\" este selectat PRIMUL
2.  Apicați boolean cut făcând click pe <img alt="" src=images/Part_Cut.png  style="width:32px;">, obiectul rezultat va fi numit \"cut003\"
3.  Selectați \"cut003\" și \"cut002\", dar adigurați-vă, că \"cut003\" este ales primul
4.  Apicați boolean cut prin click pe <img alt="" src=images/Part_Cut.png  style="width:32px;">, obiectul rezultat fa fi numit \"cut004\"
5.  Click pe <img alt="" src=images/View-axometric.png  style="width:32px;"> pentru a schimba vederea axonometrică
6.  Click pe <img alt="" src=images/View-zoom-all.png  style="width:32px;"> pentru ca prin zoom să le cuprindeți prin toate
7.  Nu uitați să vă dalvați fișierul\...

Felicitări! Tocmai ați terminat cu succes acest tutorial!


</div>

24\. Make sure all objects are visible. In the [tree view](tree_view.md) select all objects, in the **View** tab, change the value of **Visibility** to `true`, or press **Space** in the keyboard.

![](images/07_T03_Part_ball_additional_both.png ) 
*The internal hollowed solid, together with the external objects which will be used to cut it.*

25\. In the [tree view](tree_view.md) de-select the objects; then select `Cut` first, and then `Cut001`.

:   25.1. Then press **[<img src=images/Part_Cut.svg style="width:16px"> [Cut](Part_Cut.md)**. This will create `Cut003`.

![](images/08_T03_Part_ball_cut_1.png ) 
*The internal hollowed solid, cut by `Cut001*.`

26\. In the [tree view](tree_view.md) de-select the objects; then select `Cut003` first, and then `Cut002`.

:   26.1. Then press **[<img src=images/Part_Cut.svg style="width:16px"> [Cut](Part_Cut.md)**. This will create `Cut004`. This is the final object.
:   26.2. Select `Cut004`, click on the **Shape Color** value to open the **Select color** dialog, then choose a green color; also change the value of **Line Width** to `2.0`.

![](images/09_T03_Part_ball_cut_2.png ) 
*The internal hollowed solid, cut by `Cut001* and {{incode|Cut002`. Final model.}}

27\. Real objects don\'t have perfectly sharp edges or corners, so applying a fillet to the edges can be done to refine the model.

:   27.1. In the [tree view](tree_view.md), select `Cut004` then press **[<img src=images/Part_Fillet.svg style="width:16px"> [Fillet](Part_Fillet.md)**.
:   27.2. In the **Fillet edges** [task panel](task_panel.md) go to **Selection**, choose **Select edges**, and then press **All**. As **Fillet type** choose `Constant radius`, then set **Radius** to `1 mm`.
:   24.3. Press **OK**. This will create a `Fillet` object.
:   27.4. In the **View** tab, change the value of **Line Width** to `2.0`.

![](images/10_T03_Part_ball_fillet.png ) 
*Final whiffle ball model with fillets applied to the edges.*



---
⏵ [documentation index](../README.md) > [Part](Category_Part.md) > Whiffle Ball tutorial/ro
