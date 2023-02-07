# Macros recipes
This page lists [macros](Macros.md) that can add functionality to a FreeCAD installation.

If you have written a macro and want to include it in one of the categories on this page, then go to [Macro documentation](Macro_documentation.md) to learn more about properly documenting a macro.

## Categories




<div class="toccolours mw-collapsible mw-collapsed">



### <img alt="" src=images/Part_CheckGeometry.svg  style="width:32px;"> 3D View operations 




<div class="mw-collapsible-content">
-    {{MacroLink|Icon=Macro_Align_Face_Object_to_View.png|Macro_Align_Face_Object_to_View|Macro Align Face Object to View}}: This macro aligns the current view to a selected face.

-    {{MacroLink|Icon=Macro_Align_View_to_Face.png|Macro_Align_View_to_Face|Macro Align View to Face}}: This macro aligns the current view to a selected face.

-    {{MacroLink|Icon=Macro_Copy3DViewToClipboard.png|Macro_Copy3DViewToClipboard|Macro Copy3DViewToClipboard}}: Copy contents of 3DView resized 640, 480 px to clipboard.

-    {{MacroLink|Icon=FCCamera_00.png|Macro_FCCamera|Macro FCCamera}}: This macro can rotate the screen in a defined angle and the defined axis and creates a plan to face the screen to create a form in the specified plan positions the selected face facing the screen, to detect the position of the camera.

-    {{MacroLink|Icon=Macro_Mouse_Cross.png|Macro_Mouse_Cross|Macro Mouse Cross}}: This small macro turns the arrow of the mouse in a precision cross.

-    {{MacroLink|Icon=Macro_Rotate_View_view_90_Degrees.png|Macro_Rotate_View|Macro Rotate View}}: This macro rotates the current view by 90° to the left. Only works if you are in ![Std_ViewTop\|16px\|link=Std_ViewTop](images/View-top.svg ) [XY (top)](Std_ViewTop.md) view.

-    {{MacroLink|Icon=Text_console_python.png|Macro_Rotate_View_Free|Macro Rotate View Free}}: This macro is used in the Python console and rotates the current view in the angle and plane given.

-    {{MacroLink|Icon=Macro_Rotate_View_with_Y_pointing_upwards_.png|Macro_Rotate_ViewAxonometric|Macro Rotate ViewAxonometric}}: This macro rotates the current view in View Axonometric.

-    {{MacroLink|Icon=Macro_Screen_Wiki.png|Macro_Screen_Wiki|Macro Screen Wiki}}: This macro allows to save the 3D view in the desired format. The 3D view or the full 3D window of FreeCAD takes the desired dimensions.

-    {{MacroLink|Icon=Snip.png|Macro_Snip|Macro Snip}}: Easily post screenshots to the FreeCAD forum.

-    {{MacroLink|Icon=Macro_View_Rotation.png|Macro_View_Rotation|Macro View Rotation}}: Provides a GUI to permit rotation of view by precise amounts in all three directions.

-    {{MacroLink|Icon=Zoom1_1.svg|Macro_Zoom1_1|Macro Zoom 1:1}}: 1:1 Zoom so objects appear their actual size on the screen.




</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">



### <img alt="" src=images/Draft_FlipDimension.svg  style="width:32px;"> Animation 




<div class="mw-collapsible-content">
-    {{MacroLink|Icon=Macro_Animated_Constrain.png|Macro_Animated_Constrain|Macro Animated Constrain}}: Animate angle constrain in sketcher.

-    {{MacroLink|Icon=Animator.svg|Macro_Animator|Macro Animator}}: Animate your model by animating its properties with this feature Python object.

-    {{MacroLink|Icon=Macro_Assemblage_Imprimante_3D.png|Macro_Assemblage_Imprimante_3D|Macro Assemblage Imprimante 3D}}: Simulation of movements of a 3D printer.

-    {{MacroLink|Icon=Macro_Assembly.png|Macro_Assembly|Macro Assembly}}: Assembly animate.

-    {{MacroLink|Icon=Macro_Constraint_Draft.png|Macro_Constraint_Draft|Macro Constraint Draft}}: Simple example animation Draft wires by use the Expressions for associate many wires and simulate or verify the movement. Here the circle rotation create the movement for all objects connected (This macro run with FreeCAD version 0.16).

-    {{MacroLink|Icon=Macro_crank_simul.png|Macro_crank_simul|Macro crank simul}}: Rotation rod and piston.

-    {{MacroLink|Icon=Macro_hinge.png|Macro_hinge|Macro hinge}}: Open and close hinge.

-    {{MacroLink|Icon=Macro_Spring.png|Macro_Spring|Macro Spring}}: Simulation of one spring.




</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">



### <img alt="" src=images/Applications-python.svg  style="width:32px;"> Code and scripting 




<div class="mw-collapsible-content">
-    {{MacroLink|Icon=Macro_Build_Utility.png|Macro_Build_Utility|Macro Build Utility}}: This macro provides a utility to assemble a project from sub-project files using the Merge Project facility.

-    {{MacroLink|Icon=Macro_clone_explicit.png|Macro_clone_explicit|Macro clone explicit}}: Creates a copy of each selected object and sets its properties to an expression linking to the original object, making it an explicit and editable clone.

-    {{MacroLink|Icon=Editor_Assistant_Icon.svg|Macro_Editor_Assistant|Macro Editor Assistant}}: Extends the capabilities of FreeCAD\'s integrated Python editor.

-    {{MacroLink|Icon=Macro_Global_Variable_Watcher.png|Macro_Global_Variable_Watcher|Macro Global Variable Watcher}}: This macro facilitates the user selecting global variables and monitoring their values.

-    {{MacroLink|Icon=Macro_MessageBox.png|Macro_MessageBox|Macro MessageBox}}: Shows how to give information to the user through the GUI.

-    {{MacroLink|Icon=Macro_Print_SceneGraph.png|Macro_Print_SceneGraph|Macro Print SceneGraph}}: Prints the SceneGraph.

-    {{MacroLink|Icon=Macro_Python_Assistant_Window.png|Macro_Python_Assistant_Window|Macro Python Assistant Window}}: This macro provides a cut/copy/paste workspace for Python code, it is segmented so different sections can be selected and it is persistent between FreeCAD sessions.
-    {{MacroLink|Icon=Macro_ZTest_Over_128.png|Macro_ZTest_Over_128|Macro ZTest Over 128}}: This macro is only used by programmers Test characters ASCII over 127.
-    {{MacroLink|Icon=MEPlan.png|Qt_Example|Qt Example}}: Example of using Qt commands, their connections, extraction and data assignment.

-   <img alt="" src=images/Text-x-python.png  style="width:24px;"> [scanObjects](https://github.com/dprojects/scanObjects): Inspection tool for FreeCAD macro development and project debug.

-    {{MacroLink|Icon=TNP_solution.png|Macro_TNP_Solution|Macro TNP Solution}}: A basic example of how the Topological Naming Problem can be solved. The macro is intended for programmers only.




</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">



### <img alt="" src=images/Arch_MeshToShape.svg  style="width:32px;"> Conversion 




<div class="mw-collapsible-content">
-    {{MacroLink|Icon=Applications-python.svg|Macro_3DXML_import|Macro 3DXML import}}: Imports a 3DXML-ascii file into FreeCAD, limited functionality.

-    {{MacroLink|Icon=Macro_Compound_Plus.png|Macro_Compound_Plus|Macro Compound Plus}}: Draft command set in a small macro for the 2D sketch example: work with the DXF files.

-    {{MacroLink|Icon=Macro_Creating_faces_from_a_DXF_file.png|Macro_Creating_faces_from_a_DXF_file|Macro Creating faces from a DXF file}}: This macro create face from a DXF file, the \"Layer\" are recognized separate and trained in groups.

-    {{MacroLink|Icon=Macro_DeepCopy.png|Macro_DeepCopy|Macro DeepCopy}}: Make a compound out of a part with a copy of all its shapes.

-    {{MacroLink|Icon=Macro_DXF_to_Face_and_Sketch.png|Macro_DXF_to_Face_and_Sketch|Macro DXF to Face and Sketch}}: This macro converts selected elements of imported DXF file to face and sketch.

-    {{MacroLink|Icon=Macro_Dxf_To_Shape.png|Macro_Dxf_To_Shape|Macro Dxf To Shape}}: Macro utility for create unique wire with many wires, the type wire created is selected to MakeWire, Bspline, BsplineCurve, BsplineCurve + Arc, Polygon, Bezier curve.

-    {{MacroLink|Icon=Macro_Extract_Wires_from_Mesh.png|Macro_Extract_Wires_from_Mesh|Macro Extract Wires from Mesh}}: Extracts boundary wires from selected meshes.

-    {{MacroLink|Icon=Macro_FaceToSketch.png|Macro_FaceToSketch|Macro FaceToSketch}}: Converts the selected Face to a single Sketch without constraints.

-    {{MacroLink|Icon=FCBmpImportLogo.svg|Macro_FCBmpImport|Macro FCBmpImport}}: Import Black and White BMP images into FreeCAD as sketch, wire, or solid or Grayscale BMP for lithophanes.

-    {{MacroLink|Icon=Macro_FCWire_To_Volume.png|Macro_FCWire_To_Volume|Macro FCWire To Volume}}: This macro create boolean operation with the objects selected just select the wires give the thickness and click \"Create\".

-    {{MacroLink|Icon=Applications-python.svg|Macro_Iges_PyImporter|Macro Iges PyImporter}}: Imports an iges file with entity 128, for example an iges-file from FreeShip, into FreeCAD.

-    {{MacroLink|Icon=Macro_MeshToPart.png|Macro_MeshToPart|Macro MeshToPart}}: Converts selected meshes to parts.

-    {{MacroLink|Icon=MultiCopy-reduced.png|Macro_MultiCopy|Macro MultiCopy}}: MultiCopy allows the duplication (copy and paste) of multiple FreeCAD objects that can be labelled sequentially and in a custom manner.

-    {{MacroLink|Icon=PartToVRML.png|Macro_PartToVRML|Macro PartToVRML}}: Converts selected parts to VRML meshes for small size and faster loading (VRML models Kicad and Blender compatible).




</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">



### <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> Draft Workbench and 2D 




<div class="mw-collapsible-content">
-    {{MacroLink|Icon=Macro_Align_Camera_to_Working_Plane.png|Macro_Align_Camera_to_Working_Plane|Macro Align Camera to Working Plane}}: This macro aligns the camera to the current [Draft Working Plane](Draft_SelectPlane.md).

-    {{MacroLink|Icon=Macro_Align_Working_Plane_to_Camera.png|Macro_Align_Working_Plane_to_Camera|Macro Align Working Plane to Camera}}: This macro moves the current [Draft Working Plane](Draft_SelectPlane.md) to the center of the current view.

-    {{MacroLink|Icon=Macro_Draft_Circle_3_Points.png|Macro_Draft_Circle_3_Points|Macro Draft Circle 3 Points}}: Creates a circle from 3 selected points 2D orthogonal.

-    {{MacroLink|Icon=Macro_Draft_Circle_3_Points.png|Macro_Draft_Circle_3_Points_3D|Macro Draft Circle 3 Points 3D}}: Creates a circle from 3 selected points in the space 3D.

-    {{MacroLink|Icon=Applications-python.svg|Macro_Draft_Circle_Tangent|Macro Draft Circle Tangent}}: Makes tangents to Draft circles.

-    {{MacroLink|Icon=Macro_EdgesToArc.png|Macro_EdgesToArc|Macro EdgesToArc}}: Converts the selected Edges to a circular Arc if possible. Useful for restoring discretized arcs.

-    {{MacroLink|Icon=Macro_Ellipse-Center%2B2Points.png|Macro_Ellipse-Center+2Points|Macro Ellipse-Center+2Points}}: Makes an ellipse by selecting three points (in this order): center, major radius and minor radius.

-    {{MacroLink|Icon=Macro_FCConvertLines.png|Macro_FCConvertLines|Macro FC Convert Lines}}: This macro convert the object line, wire in line Dash, DashDot, DashDotDot, ZigZag and Hand with the dimensions given.

-    {{MacroLink|Icon=Macro_Make_Arc_3_Points.png|Macro_Make_Arc_3_Points|Macro Make Arc 3 Points}}: Creates a arc from 3 selected points.

-    {{MacroLink|Icon=Macro_Draft_Circle_3_Points.png|Macro_Make_Circle_3_Points|Macro Make Circle 3 Points}}: Creates a circle from 3 selected points, the points can be objects.

-    {{MacroLink|Icon=Macro_Rectellipse.png|Macro_Rectellipse|Macro Rectellipse}}: Creates a parametric rectellipse.




</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">



### <img alt="" src=images/Drawing-orthoviews.svg  style="width:32px;"> Drawing Workbench 

The [Drawing Workbench](Drawing_Workbench.md) is obsolete since FreeCAD 0.17. Consider using the [TechDraw Workbench](TechDraw_Workbench.md) instead.




<div class="mw-collapsible-content">
-    {{MacroLink|Icon=Macro_Automatic_drawing.png|Macro_Automatic_drawing|Macro Automatic drawing}}: Allows the user to get the view of his object in a drawing with 4 different position (front,top,iso,right). Needs some modification to be perfectly effective.

-    {{MacroLink|Icon=Macro_CartoucheFC.png|Macro_CartoucheFC|Macro CartoucheFC}}: This GUI macro to fill simply all fields of the cartridge of the plan implementation worksheet FreeCAD, the format of the date and the symbol of the projection mode adapt to the EU region or US selected.

-    {{MacroLink|Icon=Macro_CartoucheFC_2.png|Macro_CartoucheFC_2|Macro CartoucheFC 2}}: This GUI macro to fill simply all fields of the cartridge **model 2** of the plan implementation worksheet FreeCAD.

-    {{MacroLink|Icon=Macro_CartoucheFC_Full.png|Macro_CartoucheFC_Full|Macro CartoucheFC Full}}: This GUI macro to fill simply all fields of the cartridge [Misc templates Full](Misc_templates_Full.md) of the plan implementation worksheet FreeCAD, the format of the date and the symbol of the projection mode adapt to the EU region or US selected.

-    {{MacroLink|Icon=Macro_Normal_Vector.png|Macro_Normal_Vector|Macro Normal Vector}}: Get the normal vector of a preselected face for creating a drawing view normal to that face.




</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">



### <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> Fem Workbench 




<div class="mw-collapsible-content">
-    {{MacroLink|Icon=Text-x-python.png|Macro_export_transient_FEM_results|Macro export transient FEM results}}: This macro exports multiple FEM result objects from a transient analysis to the VTK format and generates a PVU file which can be used to load the results directly into ParaView for post-processing.

-    {{MacroLink|Icon=Macro_GMSH.png|Macro_GMSH|Macro GMSH}}: Create FEM Meshes by GMSH Mesh Generator.




</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">



### <img alt="" src=images/Std_Windows.svg  style="width:32px;"> Gui 




<div class="mw-collapsible-content">
-    {{MacroLink|Icon=GuiResetToolbars.svg|Macro_GuiResetToolbars|Macro GuiResetToolbars}}: This macro resets the position of the toolbars.

-    {{MacroLink|Icon=Macro_MacroMenu.png|Macro_MacroMenu|Macro MacroMenu}}: Add the macros found in the macros folder to the Macros menu of FreeCAD.

-    {{MacroLink|Macro_SplitPropEditor|Macro SplitPropEditor}}: Temporarily split the property editor from the combo view to a separated dock widget.

-    {{MacroLink|Icon=Macro_Toggle_Views_Visibility.png|Macro_Toggle_Panels_Visibility|Macro Toggle Panels Visibility}}: This macro toggles the visibility of various supporting panels in FreeCAD, allowing the main window to be viewed with all available screen space.




</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">



### <img alt="" src=images/Part_Measure_Linear.svg  style="width:32px;"> Info and measurements 




<div class="mw-collapsible-content">
-    {{MacroLink|Icon=BoundBoxTracing.png|Macro_BoundingBox_Tracing|Macro BoundingBox Tracing}}: This macro red trace (editable) around the BoundingBox with 6 rectangles.

-    {{MacroLink|Icon=CenterFace.png|Macro_CenterFace|Macro CenterFace}}: This macro red trace (editable) the center face (mass) with 1 point and print the coordinates.

-    {{MacroLink|Icon=Macro_CenterOfMass.png|Macro_CenterOfMass|Macro CenterOfMass}}: Gives the total mass and the center of mass of multiple objects selected with the density chosen.

-    {{MacroLink|Icon=Macro_cross_section.png|Macro_cross_section|Macro cross section}}: Displays an interactively slidable cross-section.

-    {{MacroLink|Icon=Macro_Delta_xyz.png|Macro_Delta_xyz|Macro Delta xyz}}: Gives the Delta values and the distance between 2 points.

-    {{MacroLink|Icon=Macro_Dump_Objects.png|Macro_Dump_Objects|Macro Dump Objects}}: This macro generates a listing of all objects in the current document - the list can be in a window or on the Report view.

-    {{MacroLink|Icon=Macro_FC_element_selector.png|Macro_FC_element_selector|Macro FC element selector}}: This macro display all elements below cursor same \"Macro Mouse over cb\" with GUI (elements covered by other elements will also be displayed).

-    {{MacroLink|Icon=FCInfo.png|Macro_FCInfo|Macro FCInfo}}: Gives a series of information about the selected shape and can display a conversion of length, inclination (degrees, radian, grade) shape, surface, volume and the weight of the form in the density selected in various international and Anglo-Saxon units.

-    {{MacroLink|Icon=FCInfo.png|Macro_FCInfo_Alternate_Linux|Macro FCInfo Alternate Linux}}: Same as above, but for Linux (obsolete).

-    {{MacroLink|Icon=FCInfoToolBar.png|Macro_FCInfo_ToolBar|Macro FCInfo ToolBar}}: Gives a series of information about the selected shape as FCInfo in a mini ToolBar.

-    {{MacroLink|Icon=Macro_FCInfoGlass.png|Macro_FCInfoGlass|Macro FCInfoGlass}}: Gives a series of information about the selected shape and displayed in screen 3D.

-    {{MacroLink|Icon=FCInfoToMouse.png|Macro_FCInfoToMouse|Macro FCInfoToMouse}}: Provides informations coordinates, length and angles in real time on the mouse in a bubble annotation displayed in the 3D screen.

-    {{MacroLink|Icon=Macro_FCTreeView.png|Macro_FCTreeView|Macro FCTreeView}}: Macro for list all objects in the project in one list without hierarchy, options sort by name, label, visibility, group, by length option search by name, label\... without case sensitive or with case sensitive and select all objects displayed in the macro window.

-    {{MacroLink|Icon=Macro_HighlightCommon.png|Macro_HighlightCommon|Macro HighlightCommon}}: Highlight common parts.

-    {{MacroLink|Icon=HighlightDifference.png|Macro_HighlightDifference|Macro HighlightDifference}}: Compute the difference between two shapes.

-    {{MacroLink|Icon=Macro_MeasureCircle.png|Macro_MeasureCircle|Macro MeasureCircle}}: Compute the radius of a circle by 3 points or a circular edge.

-    {{MacroLink|Icon=Macro_Mouse_over_cb.png|Macro_Mouse_over_cb|Macro Mouse over cb}}: This macro display all elements below cursor (elements covered by other elements will also be displayed).

-    {{MacroLink|Icon=Macro_ObjectInfo.png|Macro_ObjectInfo|Macro ObjectInfo}}: User-friendly \"Info\" module created by a FreeCAD user.

-   <img alt="" src=images/Text-x-python.png  style="width:24px;"> [Macro showSpaceModel](https://github.com/dprojects/Woodworking/blob/master/Tools/showSpaceModel.py): Allows to calculate occupied space in 3D by the full model.

-   <img alt="" src=images/Text-x-python.png  style="width:24px;"> [Macro showSpaceSelected](https://github.com/dprojects/Woodworking/blob/master/Tools/showSpaceSelected.py): Allows to calculate occupied space in 3D by all selected elements.

-    {{MacroLink|Icon=Macro_SimpleProperties.png|Macro_SimpleProperties|Macro SimpleProperties}}: Display in a concise way basic physical properties of an object (volume, bound box dimensions, \...).




</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">



### <img alt="" src=images/Draft_VisGroup.svg  style="width:32px;"> Libraries 




<div class="mw-collapsible-content">
-    {{MacroLink|Icon=Macro_BOLTS.png|Macro_BOLTS|Macro BOLTS}}: The aim of BOLTS is to build a free and open-source standard parts library for CAD applications.

-    {{MacroLink|Icon=FreeCAD_Doc.png|Macro_PartsLibrary|Macro PartsLibrary}}: Starts the Parts library browser.

-    {{MacroLink|Icon=Macro_screw_maker1_2.png|Macro_screw_maker1_2|Macro screw maker1_2}}: This macro creates a screw with or without thread, according to ISO standards ([screw_maker1_6.py.zip with Pyside support](http://forum.freecadweb.org/viewtopic.php?f=22&t=6088#p48519)). [(Screw Maker 2.0 - new version!)](http://forum.freecadweb.org/viewtopic.php?f=22&t=6558&start=30#p95929)




</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">



### <img alt="" src=images/Bound-expression.svg  style="width:32px;"> Mathematical functions 




<div class="mw-collapsible-content">
-    {{MacroLink|Icon=Macro_3D_Parametric_Curve.png|Macro_3D_Parametric_Curve|Macro 3D Parametric Curve}}: Draw a function described by parametric equations x(t), y(t) and z(t).

-    {{MacroLink|Icon=Macro_Draw_2D_Function.png|Macro_Draw_2D_Function|Macro Draw 2D Function}}: Draws a function described by an equation z=F(x).

-    {{MacroLink|Icon=Macro_Draw_Parametric_2D_Function.png|Macro_Draw_Parametric_2D_Function|Macro Draw Parametric 2D Function}}: Based on the above macro, but for parametric and optionally polar.

-    {{MacroLink|Icon=Parametric_Curve_FP.svg|Macro_Parametric_Curve_FP|Macro Parametric Curve FP}}: Feature Python update of Macro 3D Parametric Curve.




</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">



### <img alt="" src=images/Part_Primitives.svg  style="width:32px;"> Object creation 




<div class="mw-collapsible-content">
-    {{MacroLink|Icon=AeroFoil.png|Macro_AeroFoil|Macro AeroFoil}}: AeroFoil creates airfoil curves and faces using pre-defined models, algebraic functions, and DAT or CSV Files.

-    {{MacroLink|Icon=Macro_Airfoil_Import_&_Scale.png|Macro_Airfoil_Import_&_Scale|Macro Airfoil Import & Scale}}: Imports and scales a .dat airfoil to desired chord length.

-    {{MacroLink|Icon=Part_Prism_Apothem.svg|Macro_Apothem_Based_Prism_GUI|Macro Apothem Based Prism GUI}}: A GUI dialog that creates an Apothem, (inradius) Based Prism from user input.

-    {{MacroLink|Icon=Applications-python.svg|Macro_BSurf_from_grid|Macro BSurf from grid}}: Makes a B-spline surface through a grid of points.

-    {{MacroLink|Icon=Macro_Circle.png|Macro_Circle|Macro Circle}}: Create a circle or arc giving radius, diameter, circumference, area, startangle, endangle, arc, anglecenter, cord, arrow, center (point) on choice (same above without GUI).

-    {{MacroLink|Icon=Macro_CirclePlus.png|Macro_CirclePlus|Macro CirclePlus}}: Create a circle or arc giving radius, diameter, circumference, area, startangle, endangle, arc, anglecenter, cord, arrow, center (point) on choice (same below but with GUI) plus create sector and face.

-    {{MacroLink|Icon=Macro_Cut_Circle.png|Macro_Cut_Circle|Macro Cut Circle}}: Cut a circle or arc and create x arcs, giving the number of cut.

-    {{MacroLink|Icon=Macro_Cut_Line.png|Macro_Cut_Line|Macro Cut Line}}: Cut a line and create x points, giving the number of points, create line or not, create points or not, create bicolor or not on choice.

-    {{MacroLink|Icon=Cam-groover-icon-32x32.png|Macro_FCCamGroover|Macro FCCamGroover}}: Creates grooved cylinder for cam.

-    {{MacroLink|Icon=FCCircularTextButtom.png|Macro_FCCircularText|Macro FCCircularText}}: This macro create a text around a cylinder.

-    {{MacroLink|Icon=FCHoneycombMakerIcon.png|Macro_FCHoneycombMaker|Macro FCHoneycombMaker}}: Creates parametric honeycomb grid.

-    {{MacroLink|Icon=FCSpring_Helix_Variable.png|Macro_FCSpring_Helix_Variable|Macro FCSpring Helix Variable}}: This macro creates one spring truncate, the troncature is adjustable on the all coil to choice.

-    {{MacroLink|Icon=FCSpring_On_Surface.png|Macro_FCSpring_On_Surface|Macro FCSpring On Surface}}: This macro creates one spring (helix) on the surface of the object (solide).

-    {{MacroLink|Icon=Macro_Geodesic_Dome.svg|Macro_Geodesic_Dome|Macro Geodesic Dome}}: This macro creates a geodesic dome shell.

-    {{MacroLink|Icon=Macro_Guitar_fretboard.png|Macro_Guitar_fretboard|Macro Guitar fretboard}}: Guitar Fretboard Maker.

-    {{MacroLink|Icon=Macro_Guitar_Nut.png|Macro_Guitar_Nut|Macro Guitar Nut}}: Guitar Nut Maker.

-    {{MacroLink|Icon=Macro_Half_turn_stairs.png|Macro_Half_turn_stairs|Macro Half turn stairs}}: Creates a half turn (left/right) stair from a Data-file.

-    {{MacroLink|Icon=Macro_Half_Hull_Model.png|Macro_Half-Hull_Model|Macro Half-Hull Model}}: This macro generates both three dimensional [half-hull](http://en.wikipedia.org/wiki/Half_hull_model_ship) and full-hull models from a series of 2D line drawings.

-    {{MacroLink|Icon=Hilbert_curve_icon.png|Macro_HilbertCurve|Macro HilbertCurve}}: Creates an Hilbert curve wire in 2 or 3 dimensions with many iterations.

-    {{MacroLink|Icon=Macro_Honeycomb.svg|Macro_Honeycomb|Macro Honeycomb}}: Creates a feature Python Honeycomb object compatible in and out of PartDesign.

-    {{MacroLink|Icon=ImportAirfoil.svg|Macro_ImportAirfoil|Macro ImportAirfoil}}: Airfoil coordinates import, then scale the airfoil, rotate, translate in the plane, translate along the span, select the plane and the main axis, and turn the geometry into a sketch.

-    {{MacroLink|Icon=Intersection_Icon.svg|Macro_Intersection|Macro Intersection}}: Finds the intersection between 2 or 3 selected edges/faces, works with Datum Planes and Datum Lines also. Creates a parametric feature Python object containing the shape of the intersection.

-    {{MacroLink|Icon=Macro_Line_Length.png|Macro_Line_Length|Macro Line Length}}: Create a line giving coordinate XYZ length and angle to plane X Y.

-    {{MacroLink|Icon=FCCreaLoft.png|Macro_Loft|Macro Loft}}: Create a loft with a list of wire (specially created for [Macro Texture](Macro_Texture.md)).

-    {{MacroLink|Icon=Macro_makeCube.png|Macro_Make_Cube|Macro Make Cube}}: Creates a [rectangular cuboid](http://en.wikipedia.org/wiki/Cuboid) from 4 points.

-    {{MacroLink|Icon=Applications-python.svg|Macro_Place_Image|Macro Place Image}}: Creates an [ImagePlane](Image_CreateImagePlane.md) and aligns it to an existing [Draft Rectangle](Draft_Rectangle.md).

-    {{MacroLink|Icon=Dodecahedron.svg|Macro_Polyhedrons|Macro Polyhedrons}}: This macro creates parametric polyhedrons (dodecahedron, icosahedron, tetrahedron, \...). Customizable via radius or side.

-    {{MacroLink|Icon=Pyramidicon.svg|Macro_Pyramid|Macro Pyramid}}: This macro creates a parametric pyramid. All parameters are customizable just like with Part Cone.

-    {{MacroLink|Icon=Macro_ReproWire.png|Macro_Repro_Wire|Macro Repro Wire}}: This macro reproduces all element selected subobject wire or face.

-    {{MacroLink|Icon=Macro_Site_From_Contours.png|Macro_Site_From_Contours|Macro Site From Contours}}: Creates an Arch Site from a series of contour lines.

-    {{MacroLink|Icon=Macro_Solid_Sweep.png|Macro_Solid_Sweep|Macro Solid Sweep}}: Creates a solid by sweeping a 2D profile along a trajectory previously selected in the 3D view. The 2D elements can be created through the regular tools in FreeCAD\'s GUI.

-    {{MacroLink|Icon=Macro_Stairs.png|Macro_Stairs|Macro Stairs}}: Create stair helix, create your stair nosing select and run the macro.

-    {{MacroLink|Icon=Macro_Triangle_AH.png|Macro_Triangle_AH|Macro Triangle AH}}: This macro creates a triangle by giving the head angle and the height of the triangle (the head of the triangle is positioned to the xyz coordinates 0.0).

-    {{MacroLink|Icon=Macro_WireXYZ.png|Macro_WireXYZ|Macro WireXYZ}}: This macro creates a Wire with the coordinates extracted from a file. The coordinates X Y Z are separated by a space.




</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">



### <img alt="" src=images/Std_TransformManip.svg  style="width:32px;"> Object transformation 




<div class="mw-collapsible-content">
-    {{MacroLink|Icon=Macro_Align_Object_to_View.png|Macro_Align_Object_to_View|Macro Align Object to View}}: This macro align the selected object to the current View and set the coordinates Placement of the camera.

-    {{MacroLink|Icon=Macro_ArrayCopy.png|Macro_ArrayCopy|Macro ArrayCopy}}: Copies the selected object several times, on an array grid.

-    {{MacroLink|Icon=Bevel.svg|Macro_Bevel|Macro Bevel}}: Bevels selected vertices, creates parametric feature Python object, compatible with all solids (except with round edges) including features in Part Design bodies.

-    {{MacroLink|Icon=Macro_Center_Align_Objects_with_Faces_or_Edges.png|Macro_Center_Align_Objects_with_Faces_or_Edges|Macro Center Align Objects with Faces or Edges}}: This macro covers the following constraints: Concentric constraint among non cylindrical parts; and Constraint on center Faces and/or Edges. It works also with the new Body and App::Part containers, as well as with STEP hierarchy.

-    {{MacroLink|Icon=Macro_CloneConvert‎.png|Macro_CloneConvert‎|Macro CloneConvert}}: Creates a clone of the object and the converted in the chosen position and size (inch, mm, m, µm\...). The base object is recognized in mm (FreeCAd base).

-    {{MacroLink|Icon=Macro_Connect_And_Sweep.png|Macro_Connect_And_Sweep|Macro Connect And Sweep}}: This macro easily creates a connection between two objects, an object and a point or between two points or the selected line, wire, edge (the center of the objects are the starting and ending points of the sweep) can be selected form a configurable ellipse polygon circle.

-    {{MacroLink|Icon=Macro_FlattenWire.png|Macro_FlattenWire|Macro FlattenWire}}: Flattens draft wires that are not planar to their median Z coordinate.

-    {{MacroLink|Icon=Macro_FlattenWire3Points.png|Macro_FlattenWire3Points|Macro FlattenWire3Points}}: Flattens draft wires that are not planar to a plane defined by 3 points.

-    {{MacroLink|Icon=Macro_HealArcs.png|Macro_HealArcs|Macro HealArcs}}: Sometimes arcs are transformed into BSplines, for example when scale operations have been applied to them. This macro recreates valid arcs from them. Useful before exporting to dxf.

-    {{MacroLink|Icon=Image_Scaling.svg|Macro_Image_Scaling|Macro Image Scaling}}: Macro for easy scaling drawings, graphics, diagram, blueprint and similar 2D images in Image workbench.

-    {{MacroLink|Icon=Macro_JointWire.png|Macro_JointWire|Macro JointWire}}: Allows to find and joint all non connected edge to the closest non connected one using a line.

-   <img alt="" src=images/Text-x-python.png  style="width:24px;"> [Macro magicAngle](https://github.com/dprojects/Woodworking/blob/master/Tools/magicAngle.py): Small GUI for the Draft.rotate function. Allows to rotate panels and even other more complicated objects, like construction profiles.

-    {{MacroLink|Icon=Macro_MatrixTransform.png|Macro_MatrixTransform|Macro MatrixTransform}}: Apply linear space transformations to distort shapes. E.g., non-uniform scaling, shearing, mirroring, axes swapping.

-    {{MacroLink|Icon=Centericon.png|Macro_MoveToOrigin|Macro Move to Origin}}: This macro translates the Placement of an object so that a selected location becomes its new origin.

-    {{MacroLink|Icon=multiCuts.png|Macro_MultiCuts|Macro MultiCuts}}: This macro improves boolean cut hierarchy by automatic labeling and using copies for cut.

-    {{MacroLink|Icon=Macro_Overlap.png|Macro_Overlap|Macro Overlap}}: Boolean operation. Similar to [Part Common](Part_Common.md), but with custom overlap count threshold (parametric).

-    {{MacroLink|Icon=parametric_defeaturing.svg|Macro_Parametric_Defeaturing|Macro Parametric Defeaturing}}: Macro that provides parametric defeaturing inside and outside the [PartDesign Workbench](PartDesign_Workbench.md).

-    {{MacroLink|Icon=Macro_Perpendicular_To_Wire.png|Macro_Perpendicular_To_Wire|Macro Perpendicular To Wire}}: This macro positions an object perpendicularl to a selected wire.

-    {{MacroLink|Icon=Macro_PlacementAbsolufy.png|Macro_PlacementAbsolufy|Macro PlacementAbsolufy}}: Reset Part containers to global origin while maintaining objects absolute position.

-    {{MacroLink|Icon=Macro_Remove_parametric_history.png|Macro_Remove_parametric_history|Macro Remove parametric history}}: Removes all parametric associativity from an object, leaving it as a \"dumb\" shape.

-    {{MacroLink|Icon=Macro_Rotate_To_Point.png|Macro_Rotate_To_Point|Macro Rotate To Point}}: Macro to rotate an object around the center of its boundbox, its center of mass, or the last clicked point.

-    {{MacroLink|Icon=Part_Section‎.png|Macro_Section|Macro Section}}: Alternative implementation of Part Section tool, more suitable for making sweep paths (parametric).

-    {{MacroLink|Icon=Macro_StraightenObject.png|Macro_StraightenObject|Macro StraightenObject}}: Re-align object(s) with FreeCAD coordinate system according reference face/edge.

-    {{MacroLink|Icon=Macro_SuperWire.png|Macro_SuperWire|Macro SuperWire}}: Forces the creation of a Wire from lines and arcs that don\'t necessarily touch each other. Use this if normal wire operation fails.

-    {{MacroLink|Icon=Wirefilter.svg|Macro_WireFilter|Macro WireFilter}}: Filter wires from a sketch to only use certain ones, also 2D offsets, scales, rearranges wire order.




</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">



### <img alt="" src=images/Part_FaceColors.svg  style="width:32px;"> Object visibility, view properties and textures 




<div class="mw-collapsible-content">
-   <img alt="" src=images/Text-x-python.png  style="width:24px;"> [colorManager](https://github.com/dprojects/Woodworking/blob/master/Tools/colorManager.py): Allows to set face colors for all objects from a spreadsheet. Also you can browse colors for a manually selected face or object and see the effect in the 3D model in real-time.

-    {{MacroLink|Icon=Workbench_Image.svg|Macro_Colorize|Macro Colorize}}: Easily set colors of faces, edges, and vertices, including individual transparency levels.

-    {{MacroLink|Icon=Macro_HiddenAlls.png|Macro_HiddenAlls|Macro Hidden Alls objects}}: This macro check hidden all object in the document (Visibility=False).

-    {{MacroLink|Icon=FCTexture.png|Macro_Texture|Macro Texture}}: Create a project from a bmp image to create a texture easily.

-    {{MacroLink|Icon=Macro_Texture_Objects.png|Macro_Texture_Objects|Macro Texture Objects}}: This macro allows you to temporarily put a texture image on the selected objects.

-    {{MacroLink|Icon=Macro_Toggle_Drawstyle.png|Macro_Toggle_Drawstyle|Macro Toggle Drawstyle}}: This macro toggles the Drawstyle of the selected object.

-    {{MacroLink|Icon=Macro_Toggle_Drawstyle_Optimized.png|Macro_Toggle_Drawstyle_Optimized|Macro Toggle Drawstyle Optimized}}: This macro toggles the Drawstyle of the selected object (same as Macro Toggle Drawstyle above but optimized for all languages).

-    {{MacroLink|Icon=Macro_SelectVisible.png|Macro_Toggle_Visibility|Macro Toggle Visibility}}: Set of three macro, macro **1:** hidden the objects not selected, macro **2:** displayed alls objects, macro **3:** hidden alls objects.

-    {{MacroLink|Icon=Macro_SelectVisible2.png|Macro_Toggle_Visibility2_1-2|Macro Toggle Visibility2 1-2}}: Set of two macro, macro **1:Macro_Toggle_Visibility2_1-2** hidden the objects not selected, macro **2:Macro_Toggle_Visibility2_2-2** displayed alls objects, macro with the original visibility.

-    {{MacroLink|Icon=Macro_VisibleAlls2.png|Macro_Toggle_Visibility2_2-2|Macro Toggle Visibility2 2-2}}: Set of two macro, macro **1:Macro_Toggle_Visibility2_1-2** hidden the objects not selected, macro **2:Macro_Toggle_Visibility2_2-2** displayed alls objects, macro with the original visibility.

-    {{MacroLink|Icon=Macro_VisibleAlls.png|Macro_VisibleAlls|Macro Visible Alls objects}}: This macro check visible all object in the document (Visibility=True).

-    {{MacroLink|Icon=Macro_Visibility_Manager.png|Macro_Visibility_Manager|Macro Visibility Manager}}: Manage visibility of document objects by type or individually.

-   <img alt="" src=images/Text-x-python.png  style="width:24px;"> [setTextures](https://github.com/dprojects/setTextures): Allows to permanently store the URL of textures in a FreeCAD project and load stored textures.




</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">



### <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> PartDesign Workbench 




<div class = "mw-collapsible-content">
-    {{MacroLink|Icon=Workbench_PartDesign.svg|Macro_PDWrapper|Macro PDWrapper}}: Encapsulates non-PartDesign solids for use in PartDesign Bodies, and more.




</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">



### <img alt="" src=images/View.svg  style="width:32px;"> Printer 3D 




<div class="mw-collapsible-content">
-    {{MacroLink|Icon=Macro_3d_Printer_Slicer.png|Macro_3d_Printer_Slicer|Macro 3d Printer Slicer}}: Exports current design to slicer software or CAM software.

-    {{MacroLink|Icon=Macro_3d_Printer_Slicer_Individual_Parts.svg|Macro_3d_Printer_Slicer_Individual_Parts|Macro 3d Printer Slicer Individual Parts}}: This code, when run, will export the visible bodies at the top level (bodies deeper in the tree will be ignored) of the currently open design to individual STL files, and open them it in the slicing software that you use. This macro will look for Cura as the default but you can change it to any other slicer by changing the SLICERAPP variable in the source code.

-    {{MacroLink|Icon=Macro_3D_Printer_Workflow.png|Macro_3D_Printer_Workflow|Macro 3D Printer Workflow}}: Macro that creates an stl file with perfect rounding, i.e. without visible facets, from selected objects. It also allows to launch programs of your choice. For example to automate the FreeCAD -\> Slicer -\> printing workflow.




</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">



### <img alt="" src=images/Preferences-raytracing.svg  style="width:32px;"> Raytracing 




<div class="mw-collapsible-content">
-    {{MacroLink|Icon=Macro_FreeCAD_to_Kerkythea.png|Macro_FreeCAD_to_Kerkythea|Macro FreeCAD to Kerkythea}}: Export from FreeCAD to Kerkythea.

-    {{MacroLink|Icon=Applications-python.svg|Macro_Z_Height_Map|Macro Z Height Map}}: Makes a grayscale heightmap in Z.




</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">



### <img alt="" src=images/Spreadsheet.svg  style="width:32px;"> Spreadsheet Workbench 




<div class="mw-collapsible-content">
-    {{MacroLink|Icon=aliasmanager_icon.png|Macro_Alias_Manager|Macro Alias Manager}}: Helps managing aliases inside FreeCAD Spreadsheet workbench. It is able to create, delete, move aliases and create a \'part family\' group of files.

-    {{MacroLink|Icon=easy-alias-icon.png|Macro_EasyAlias|Macro EasyAlias}}: Quickly create aliases in FreeCAD Spreadsheet workbench. It uses the labels from one column to create aliases for adjacent cells in the next column to the right, e.g. labels from Column A become aliases for the cells in Column B.

-    {{MacroLink|Icon=Macro_FCSpreadsheet_Extract.png|Macro_FCSpreadSheet_Extract|Macro FCSpreadSheet Extract}}: This macro save the data in a csv file with the formula or in a xml file.

-    {{MacroLink|Icon=Macro_SpreadsheetTools.png|Macro_SpreadsheetTools|Macro Spreadsheet Tools}}: This macro helps managing cells inside FreeCAD Spreadsheet workbench.

-    {{MacroLink|Icon=Applications-python.svg|Macro_Spreadsheet2html|Macro Spreadsheet2html}}: Exports a spreadsheet as styled html. Intended as support in transfering data to office suits.

-   <img alt="" src=images/Text-x-python.png  style="width:24px;"> [sheet2export](https://github.com/dprojects/sheet2export): Allows to export FreeCAD spreadsheet to file formats (.md, .html, .csv, .json).




</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">



### <img alt="" src=images/Arch_Survey.svg  style="width:32px;"> Utility 




<div class="mw-collapsible-content">
-    {{MacroLink|Icon=Macro_Arch_Axis_System_Repartition.png|Macro_Arch_Axis_System_Repartition|Macro Arch Axis System Repartition}}: This macro help you to create an Arch Axis System along a line with a set of parameters.

-    {{MacroLink|Icon=Macro_Duplicate_Selection.png|Macro_Duplicate_Selection|Macro Duplicate Selection}}: This macro testing if one selection are duplicate, select the object IN THE 3D VIEW the \"ForbiddenCursor\" stay if the or one selection is duplicate, the macro stay resident.

-    {{MacroLink|Icon=Macro_Easy_Cutouts_for_Enclosures.png|Macro_Easy_cutouts_for_Enclosure_Design|Macro Easy cutouts for Enclosure Design}}: This macro makes Cutouts for Enclosures in a very handy way.

-    {{MacroLink|Icon=Macro_ExpandTreeItem.png|Macro_ExpandTreeItem|Macro ExpandTreeItem}}: This macro expand selected items in the tree view. If not selection all item are expand/collapse.

-    {{MacroLink|Icon=Macro_findConfigFiles.png|Macro_findConfigFiles|Macro findConfigFiles}}: Finds user config files system.cfg and user.cfg, copies folder location to system clipboard, instructs user on renaming these files in order to reset FreeCAD settings, and opens folder with default file browser.

-    {{MacroLink|Icon=Force_Recompute.png|Macro_ForceRecompute|Macro ForceRecompute}}: Forces manual recompute of model.

-    {{MacroLink|Icon=Macro_If_Selected_Stay_If_Not_Then_Delete.png|Macro_If_Selected_Stay_If_Not_Then_Delete|Macro If Selected Stay If Not Then Delete}}: All object not selected are deleted!

-    {{MacroLink|Macro_ImperialScales|Macro ImperialScales}}: Shows a list of US Imperial Arch scales list with the corresponding factor to apply to TechDraw pages or views.

-    {{MacroLink|Icon=Macro_merge_duplicate_materials.png|Macro_merge_duplicate_materials|Macro merge duplicate materials}}: Merges materials that have the same base name (with different numeral endings like 001, 002,\...) into one.

-    {{MacroLink|Icon=Pcbway.png|Macro_PCBWay|Macro PCBWay}}: Sends a selected object to [PCBWay](https://pcbway.com) for manufacturing through CNC milling, laser cutting or 3D printing.

-    {{MacroLink|Icon=Pinger_Icon.svg|Macro_Pinger|Macro Pinger}}: Ping users on the forum with ease.

-    {{MacroLink|Icon=Macro_Recompute_Profiler.png|Macro_Recompute_Profiler|Macro Recompute Profiler}}: Measures time it takes to recompute each object in a project.

-    {{MacroLink|Icon=Replace_Part.png|Macro_Replace_Part_in_Assembly|Macro Replace Part in Assembly}}: Replaces a part (simple copy) in an \"Assembly\" with another Part (simple copy).

-    {{MacroLink|Icon=Macro_Select_Hovering.png|Macro_Select_Hovering|Macro Select Hovering}}: This macro select a choice Face, Edge, Vertex hovering by the mouse.

-    {{MacroLink|Icon=SelectVisible.png|Macro_SelectVisible|Macro SelectVisible}}: All visible objects in the tree will be selected.

-    {{MacroLink|Icon=Macro_Shake_Sketch.png|Macro_Shake_Sketch|Macro Shake Sketch}}: Shake a sketch in order to discover its unconstrained parts.

-    {{MacroLink|Icon=SketchUnmap.svg|Macro_SketchUnmap|Macro SketchUnmap}}: Unmap a sketch from its current support and makes its placement absolute, eventually creating a locating datum plane.

-    {{MacroLink|Macro_TreeToAscii|Macro TreeToAscii}}: Prints model tree as \"ASCII art\" with custom pattern & style, and export to clipboard, file or embedded document.

-    {{MacroLink|Icon=Macro_Unbind_Numpad_Shortcuts.png|Macro_Unbind_Numpad_Shortcuts|Macro Unbind Numpad Shortcuts}}: Rebinds standard view commands from digit keys to Ctrl+digit, so that they don\'t spin the view by accident when entering numbers.

-    {{MacroLink|Icon=WF_wf.png|Macro_WorkFeatures|Macro WorkFeatures}}: Tool utility to create points, axes, planes and many other useful features to facilitate the creation of your project.




</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">



### <img alt="" src=images/Bulb.svg  style="width:32px;"> Wizards 




<div class="mw-collapsible-content">
-    {{MacroLink|Icon=Macro_Corner_shapes_wizard.png|Macro_Corner_shapes_wizard/update|Macro Corner shapes wizard/update}}: Pops up a dialog asking for the dimensions of your corner piece, then creates the object in the document and creates a page view with top, front and lateral views of the piece.

-    {{MacroLink|Icon=Gearworkbech.png|Macro_FCGear|Macro FCGear}}: Additional Workbench to create different types of gears, involute gear, involute rack, cycloide gear, bevel gear.

-    {{MacroLink|Icon=Macro_Fonts_Win10_PYMP.png|Macro_Fonts_Win10_PYMP|Macro Fonts Win10 PYMP}}: This little macro is dedicate to users of Windows 10. The explorer fonts for use the [ShapeString](Draft_ShapeString.md) is empty and this little macro can help you see easily the font to use.

-    {{MacroLink|Icon=GenerateDrawing.svg|Macro_GenerateDrawing|Macro GenerateDrawing}}: Macro for automatic drawing generation with 3 normal projections and one isometric.

-    {{MacroLink|Icon=GenerateViews.svg|Macro_GenerateViews|Macro GenerateViews}}: Macro for automatic 2D views generation with 6 normal projections and one isometric.

-    {{MacroLink|Icon=GW_Dim.png|Macro_Geneva_Wheel|Macro Geneva Wheel}}: Allows the user to create a Geneva wheel mechanism from scratch. Must edit values within the Macro to alter the size of the object.

-    {{MacroLink|Icon=GW_Dim.png|Macro_Geneva_Wheel_GUI|Macro Geneva Wheel GUI}}: A GUI front end that allows the user to create a Geneva wheel mechanism from scratch.

-    {{MacroLink|Icon=Macro_Megaminx.png|Macro_Megaminx|Macro Megaminx}}: Display a Megaminx and interactively do slice rotations.

-    {{MacroLink|Icon=PropertyMemo.png|Macro_PropertyMemo|Macro PropertyMemo}}: This little macro create one Property additional (memo or other text) for you object (only Draft).

-    {{MacroLink|Icon=Macro_Rubik_Cube.png|Macro_Rubik_Cube|Macro Rubik Cube}}: Display a Rubik Cube and interactively do slice rotations.

-    {{MacroLink|Icon=Macro_Sheet_Metal_Unfolder.png|Macro_Sheet_Metal_Unfolder|Macro Sheet Metal Unfolder}}: Creates an unfolded part from a sheet-metal-part.

-    {{MacroLink|Icon=Macro_Unfold_Box.png|Macro_Unfold_Box|Macro Unfold Box}}: Allows to unfold the surfaces of a box of any shape and to draw them on a page.

-    {{MacroLink|Icon=Macro_Unroll_Ruled_Surface.png|Macro_Unroll_Ruled_Surface|Macro Unroll Ruled Surface}}: Allows to unroll ruled surfaces and to draw them on a page.




</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">



### <img alt="" src=images/Arch_Equipment.svg  style="width:32px;"> Woodworking 




<div class="mw-collapsible-content">
-   <img alt="" src=images/Text-x-python.png  style="width:24px;"> [getDimensions](https://github.com/dprojects/getDimensions): FreeCAD macro to get chipboards dimensions to cut (BOM, cutlist).

-    {{MacroLink|Icon=Macro_Cabinets32.png|Macro_Cabinets32|Macro Cabinets32}}: Creates side and top/bottom walls for a cabinet with drilled holes for connection parts of manufacturer Hettich.

-    {{MacroLink|Icon=Macro_Joint_Icon.svg|Macro_Joint|Macro Joint}}: Creates a variety of joints, such as mortise/tenon, box joints, dovetail joints, and snap joints.

-   <img alt="" src=images/Text-x-python.png  style="width:24px;"> [makeTransparent](https://github.com/dprojects/Woodworking/blob/master/Tools/makeTransparent.py): Switches all parts from non-transparent to transparent, and back, allowing you to preview pilot holes, countersinks and other joints.




</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">



### <img alt="" src=images/Std_FreeCADWebsite.svg  style="width:32px;"> Other interesting macros created by FreeCAD users 




<div class="mw-collapsible-content">
-   <img alt="" src=images/Text-x-python.png  style="width:24px;"> [By hamish2014](https://github.com/hamish2014?tab=repositories): FreeCAD_assembly2, FreeCAD_drawing_dimensioning, and more.

-   <img alt="" src=images/2364.png  style="width:24px;"> [By microelly2](https://github.com/microelly2?tab=repositories) : FreeCAD_macro, geodata, Animation, freecad-nurbs, PieMenu, and more.

-   <img alt="" src=images/Text-x-python.png  style="width:24px;"> [By oddtopus](https://github.com/oddtopus?tab=repositories): Flamingo (workbench for metal structures).

-   <img alt="" src=images/Text-x-python.png  style="width:24px;"> [By realthunder](https://github.com/realthunder/FreeCAD_assembly3#installation): Assembly3 Workbench, and more.

-   <img alt="" src=images/681.jpg  style="width:24px;"> [By rockn](https://github.com/j-wiedemann?tab=repositories): FreeCAD-Timber, FreeCAD-addons, FreeCAD-library, FreeCAD-StructuresBois, and more.

-   <img alt="" src=images/Text-x-python.png  style="width:24px;"> [By Siardeni](https://github.com/Siardeni/FreeCADTools): Workbench for create metal profiles, square tubing, z profile, palette, rotation, drawing, and more.

-   <img alt="" src=images/Text-x-python.png  style="width:24px;"> [By triplus](https://github.com/triplus?tab=repositories): IconThemes, ShortCuts, NavigationIndicator, TabBar, Launcher, PersistentToolbars, PieMenu, and more.




</div>


</div>



## Usage

See [how to install macros](how_to_install_macros.md) for a full description, and [customize toolbars](Customize_Toolbars.md) to add the macros to a toolbar for easy access.

Installing many macros is equivalent to installing a new workbench; see [how to install additional workbenches](How_to_install_additional_workbenches.md) for this information.

### Automatic installation 

Use the [Addon Manager](Std_AddonMgr.md) in **Tools → Addon manager** to install a macro that has been included in the [FreeCAD-macros](https://github.com/FreeCAD/FreeCAD-macros) repository. <small>(v0.17)</small> 

### Manual installation 

If the [Addon Manager](Std_AddonMgr.md) is not used, the macro can be installed manually.

-   Copy the [Python](Python.md) code from the corresponding macro page.
-   Open the macros menu **Macro → Macros**, press **Create**, and give it a name.
-   Paste the Python code that you copied.
-   Press the **Save** button, and restart FreeCAD.
-   To use it, open again the macros menu, select your new macro, and press **Execute**.

### Add a macro to a custom toolbar 

-   Go to **Tools → Customize**.
-   In the **Macros** tab, add a new macro name, and optionally define an icon and a keyboard shortcut.
-   In the **Toolbars** tab, create a new toolbar, and add your macro, taking it from the **Macros** category.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Macros](Category_Macros.md) > [Python Code](Category_Python Code.md) > Macros recipes
