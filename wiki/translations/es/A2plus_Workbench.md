# <img alt="El icono del Ambiente de trabajo A2plus" src=images/A2p_workbench.svg  style="width   *64px;"> A2plus Workbench/es

## Introducción


{{TOCright}}

El ambiente de trabajo A2plus es un [Ambiente de trabajo externo](External_workbenches/es.md) para [ensamble](Assembly/es.md) diferentes piezas en FreeCAD.


<div class="mw-translate-fuzzy">

Esta documentación describe la versión de A2plus **0.4.47 o más reciente**.


</div>

## Instalación

El ambiente de trabajo A2plus es un complemento de FreeCAD. Se puede instalar fácilmente a través del <img alt="" src=images/AddonManager.svg  style="width   *24px;"> de FreeCAD [Administrador de complementos](Std_AddonMgr/es.md) desde el menú **Herramientas → Administrador de complementos**. A2plus está en desarrollo activo y obtendrá nuevas características con frecuencia. Por lo tanto, debería actualizarlo regularmente utilizando también el menú **Herramientas → [Administrador de complementos](Std_AddonMgr/es.md)**. El código de A2plus está alojado y desarrollado [en GitHub](https   *//github.com/kbwbe/A2plus) y también puede ser instalado manualmente copiándolo en el directorio **Mod** de FreeCAD.

## Cómo empezar 

Primero cambia a la barra de herramientas A2plus en FreeCAD. Para crear un ensamblaje crea un nuevo archivo en FreeCAD. Al principio este archivo necesita ser guardado. Se recomienda (pero no es necesario) guardarlo en la misma carpeta de las piezas que quieres ensamblar.

Ahora se pueden añadir piezas al ensamblaje utilizando el botón de la barra de herramientas <img alt="" src=images/A2p_ImportPart.svg  style="width   *24px;"> o <img alt="" src=images/A2p_ShapeReference.svg  style="width   *24px;">. El botón <img alt="" src=images/A2p_ImportPart.svg  style="width   *24px;"> añade todos los cuerpos del archivo seleccionado como una sola pieza. Cuando se utiliza el botón <img alt="" src=images/A2p_ShapeReference.svg  style="width   *24px;"> se puede elegir qué parte de un archivo debe ser importada como parte. De esta forma se puede, por ejemplo, importar sólo un boceto para ensamblar otras piezas utilizando el boceto para determinar las posiciones de las piezas.

La primera parte añadida obtiene una posición fija por defecto. (Puede cambiar esto más tarde a través de la propiedad de la parte **Posición fija**.)

Parts that are already in the assembly can be cloned with the toolbar button <img alt="" src=images/A2p_DuplicatePart.svg  style="width   *24px;">.

To edit a part from the assembly, select it in the model tree and use the toolbar button <img alt="" src=images/A2p_EditPart.svg  style="width   *24px;">. This will open the part into a new tab in FreeCAD or switch to its tab if the file is already opened.

To update changed parts in assemblies click on the toolbar button <img alt="" src=images/A2p_ImportPart_Update.svg  style="width   *24px;">. The toolbar button <img alt="" src=images/A2p_RecursiveUpdate.svg  style="width   *24px;"> imports parts too but recursively over possible [subassemblies](#Subassemblies.md). If you select one or some parts in FreeCAD\'s the tree view, A2plus will ask you to only update the selected parts.

Imported parts will keep their external dependencies and can be edited. For well-defined parts like screws it is however useful that their shape cannot be edited. This can be achieved with the toolbar button <img alt="" src=images/A2p_ConvertPart.svg  style="width   *24px;"> that converts the selected part to a static copy of the original part.

To save the assembly and close it afterwards, the toolbar button <img alt="" src=images/A2p_Save_and_exit.svg  style="width   *24px;"> can be used.

## Ensamblaje

Assembling parts is done by adding constraints between parts. After a constraint A2plus will move the parts according to the constraint if possible.

To create a constraint between parts, keep the **Ctrl** key pressed and select each an edge or face of two parts. Then click the toolbar button of the desired constraint. A dialog will pop up that is descried in section [Constraints](#Constraints.md). The constraint will be added in the model tree attached to the affected parts.

For complex constraints between parts A2plus might fail to solve the constraints. Therefore also have a look at section [Troubleshooting](#Troubleshooting.md) for strategies to resolve such cases.

### Mantenga el vista general 

The more parts you add, the more important it is to keep track. A2plus therefore offers these tools to move and view parts   *

-   To move a part around in the assembly, select it in the model tree and use the toolbar button <img alt="" src=images/A2p_MovePart.svg  style="width   *24px;">. When you placed the part where you like it, left-click with the mouse. If the moved part already has constraints it will be placed accordingly by pressing the toolbar button <img alt="" src=images/A2p_solver.svg  style="width   *24px;"> because this triggers to resolve all constraints of the assembly.
-   To show a constraint select it in the model tree and use the toolbar button <img alt="" src=images/A2p_ViewConnection.svg  style="width   *24px;">. This will make the whole assembly transparent and highlight the two objects that are connected via the constraint. To go back to the normal view, left-click into the assembly.
-   To show only certain parts in the assembly, select these parts in the model tree and use the toolbar button <img alt="" src=images/A2p_Isolate_Element.svg  style="width   *24px;">. Alternatively you can hide a certain part by selecting it in the model tree and pressing **Space** to toggle its visibility.
-   To toggle the transparency view of the whole assembly you can use the toolbar button <img alt="" src=images/A2p_ToggleTransparency.svg  style="width   *24px;">.
-   Every part can be made transparent using the normal FreeCAD editing. However sometimes the transparency setting for parts is lost when reopening the assembly due to a bug in FreeCAD. As workaround you can use the toolbar button <img alt="" src=images/A2p_Restore_Transparency.svg  style="width   *24px;"> to restore the transparency settings.

## Restricciones

When creating a constraint such a dialog will be displayed after you pressed a constraint toolbar button   *

![](images/A2p_ConstraintPropertiesDialog.png ) 
*Above   * The A2plus Constraint Properties Dialog*

For certain constraints it allows you to modify the constraint direction. With the button **<img src="images/A2p_solver.svg" width=24px> Solve** you can check beforehand if this new constraint can be solved by A2plus. If not, have a look at section [Troubleshooting](#Troubleshooting.md).

Constraints can be disabled by changing its [visibility](Std_ToggleVisibility.md). This is done by selecting the constraint in the tree view and pressing **Space**. This toggles the property **Suppressed**. A suppressed constraint is not taken into account when the assembly is solved.

A2plus provides the following constraints   *

#### Point on Point 

Select either a [vertex](Glossary#Vertex.md) (point), circle or sphere on each part. If a circle or sphere was selected, its center point will be used for the constraint. The toolbar button <img alt="" src=images/A2p_PointIdentity.svg  style="width   *24px;"> adds the constraint {{Variable|pointIdentity}} that make the vertices coincident.

#### Punto en la línea 

Select a [vertex](Glossary#Vertex.md) (point), or circular [edge](Glossary#Edge.md) (will select its center point), or a spherical [face](Glossary#Face.md) (will also select its center point) on one part and an [edge](Glossary#Edge.md) on the other part. The toolbar button <img alt="" src=images/A2p_PointOnLineConstraint.svg  style="width   *24px;"> adds the constraint {{Variable|pointOnLine}}. It will put the vertex on the edge.

#### Punto en el plano 

Select a [vertex](Glossary#Vertex.md) (point), or circular [edge](Glossary#Edge.md) (will select its center point), or a spherical [face](Glossary#Face.md) (will also select its center point) on one part and a plane on the other part. The toolbar button <img alt="" src=images/A2p_PointOnPlaneConstraint.svg  style="width   *24px;"> adds the constraint {{Variable|pointOnPlane}}. The constraint dialog allows you to specify an offset between the point and the plane. This offset can also be flipped between both sides of the plane. If the offset is zero, the constraint will put the vertex on the plane.

#### Esfera sobre Esfera 

Select either a spherical [face](Glossary#Face.md) or a [vertex](Glossary#Vertex.md) (point) on both parts. The toolbar button <img alt="" src=images/A2p_SphericalSurfaceConstraint.svg  style="width   *24px;"> adds the constraint {{Variable|sphereCenterIdent}}. It will either make the center of the spheres, the center of the sphere and the vertex, or the vertices coincident.

#### Circular Edge on Circular Edge 

Select a circular [edge](Glossary#Edge.md) on both parts. The toolbar button <img alt="" src=images/A2p_CircularEdgeConstraint.svg  style="width   *24px;"> adds the constraint {{Variable|circularEdge}}. The constraint dialog allows you to specify an offset between the edges. This offset can also be flipped. You can furthermore set the constraint direction and lock the rotation of the parts. If the offset is zero, the constraint will put the edges concentric in the same plane.

#### Axis Coincident 

Select either a cylindrical [face](Glossary#Face.md) or a linear [edge](Glossary#Edge.md) on both parts. The toolbar button <img alt="" src=images/A2p_AxialConstraint.svg  style="width   *24px;"> adds the constraint {{Variable|axisCoincident}}. The constraint dialog allows you to specify the axis direction. The dialog allows you furthermore to lock the rotation of the parts. The constraint will make the axes or lines coincident.

#### Axis Parallel 

Select either a cylindrical [face](Glossary#Face.md) or a linear [edge](Glossary#Edge.md) on both parts. The toolbar button <img alt="" src=images/A2p_AxisParallelConstraint.svg  style="width   *24px;"> adds the constraint {{Variable|axisParallel}}. The constraint dialog allows you to specify the axis direction. The constraint will make the axes or lines parallel.

#### Axis on Plane parallel 

Select either a cylindrical [face](Glossary#Face.md) or a linear [edge](Glossary#Edge.md) on one part and a plane on the other part. The toolbar button <img alt="" src=images/A2p_AxisPlaneParallelConstraint.svg  style="width   *24px;"> adds the constraint {{Variable|axisPlaneParallel}}. The constraint will make the axis or line parallel to the plane.

#### Axis on Plane normal 

Select either a cylindrical [face](Glossary#Face.md) or a linear [edge](Glossary#Edge.md) on one part and a plane on the other part. The toolbar button <img alt="" src=images/A2p_AxisPlaneNormalConstraint.svg  style="width   *24px;"> adds the constraint {{Variable|axisPlaneNormal}}. The constraint will make the axis or line normal to the plane.

#### Axis on Plane angle 

Select either a cylindrical [face](Glossary#Face.md) or a linear [edge](Glossary#Edge.md) on one part and a plane on the other part. The toolbar button <img alt="" src=images/A2p_AxisPlaneAngleConstraint.svg  style="width   *24px;"> adds the constraint {{Variable|axisPlaneAngle}}. The constraint will at first make the axis parallel to the plane. Then you can adjust the angle for the axis in the appearing constraint settings dialog.

#### Plane Parallel 

Select a plane on both parts. The toolbar button <img alt="" src=images/A2p_PlanesParallelConstraint.svg  style="width   *24px;"> adds the constraint {{Variable|planesParallel}}. The constraint dialog allows you to specify the constraint direction. The constraint will make the planes parallel.

#### Plane on Plane 

Select a plane on both parts. The toolbar button <img alt="" src=images/A2p_PlaneCoincidentConstraint.svg  style="width   *24px;"> adds the constraint {{Variable|planeCoincident}}. The constraint dialog allows you to specify a constraint direction and an offset between the planes. This offset can also be flipped. If the offset is zero, the constraint will make the planes coincident.

#### Plane Angular 

Select a plane on both parts. The toolbar button <img alt="" src=images/A2p_AngleConstraint.svg  style="width   *24px;"> adds the constraint {{Variable|angledPlanes}}. The constraint dialog allows you to specify an angle between the planes. The constraint will make the planes at first parallel and the set the specified angle.

#### Coincidence at Center of Mass 

Select either a closed [edge](Glossary#Edge.md) or a plane on both parts. The toolbar button <img alt="" src=images/A2p_CenterOfMassConstraint.svg  style="width   *24px;"> adds the constraint {{Variable|centerOfMass}}. The constraint dialog allows you to specify an offset between the edges or planes. This offset can also be flipped. You can furthermore set the constraint direction and lock the rotation of the parts. If the offset is zero, the constraint will put the edges or planes into the same plane.

### Subassemblies

An assembly can contain other assemblies. They are added like parts by pressing the toolbar button <img alt="" src=images/A2p_ImportPart.svg  style="width   *24px;"> and selecting a ***.FCStd** file containing an assembly. Such subassemblies can also be edited like parts using the toolbar button <img alt="" src=images/A2p_EditPart.svg  style="width   *24px;">. Please make sure for higher assembly stages that you update the assembly recursively via the toolbar button <img alt="" src=images/A2p_RecursiveUpdate.svg  style="width   *24px;"> when there were changes.

## Constraint Handling 

Possible constraints for a selection are displayed in the toolbar and the *Constraint Tools* dialog by enabling the corresponding buttons. The *Constraint Tools* dialog is opened via the toolbar button <img alt="" src=images/A2p_DefineConstraints.svg  style="width   *24px;">. It is intended to stay open to be able to add quickly several constraints to the assembly.

Existing constraints can be edited by selecting them in the model tree and then either double-clicking on it or using the toolbar button <img alt="" src=images/A2p_EditConstraint.svg  style="width   *24px;">. This opens the *Constraint Properties* dialog.

Constraints can be temporarily suppressed by selecting them in the model tree and changing the tree element property **Suppressed**.

Constraints can be deleted either by selecting them in the model tree and pressing **Del** or by selecting a part with constraints in the model tree and using the toolbar button <img alt="" src=images/A2p_DeleteConnections.svg  style="width   *24px;">.

All constraints can be resolved at any time with the toolbar button <img alt="" src=images/A2p_solver.svg  style="width   *24px;">. If the toolbar button <img alt="" src=images/A2p_ToggleAutoSolve.svg  style="width   *24px;"> is turned on a resolve is automatically done after every edit of a constraint.

The toolbar button <img alt="" src=images/A2p_FlipConstraint.svg  style="width   *24px;"> affects the constraint that was added most recently. It flips the constraint direction.

## Part Lists 

To create part lists of assemblies, the different parts of the assembly must get part info that can be read by A2plus. This is done by editing the part using the toolbar button <img alt="" src=images/A2p_EditPart.svg  style="width   *24px;">. In the opened part press the toolbar button <img alt="" src=images/A2p_PartsInfo.svg  style="width   *24px;"> and a [spreadsheet](Spreadsheet_Workbench.md) with the name *\#PARTINFO\#* is created.

The structure of the spreadsheet is like this   *

![](images/A2p_PartinfoTable.png )

Fill out the grey fields with info you have and want to have in the final parts list.

In the assembly or subassembly use the toolbar button <img alt="" src=images/A2p_PartsList.svg  style="width   *24px;">. It will ask you if you want to iterate recursively over all subassemblies. Click on *Yes*. This creates a new spreadsheet with the name *\#PARTSLIST\#*. It contains the info from the different *\#PARTSINFO\#* spreadsheets of the parts in a list like this   *

![](images/A2p_PartslistTable.png )

The position (POS) is automatically set according to the appearance of the parts in the model tree. The top level part will get POS 1.

The quantity (QTY) is automatically calculated from the assembly. If a parts is twice in the assembly it will get QTY 2.

If you have updated a part info you can refresh the parts list by pressing the toolbar button <img alt="" src=images/A2p_PartsList.svg  style="width   *24px;"> again.

For subassemblies you can also create an info spreadsheet using the toolbar button <img alt="" src=images/A2p_PartsInfo.svg  style="width   *24px;">. When you create or update the parts list of the main assembly this info will be used if you click on *No* for the question if you want to iterate recursively over all subassemblies. Then the different parts are not in the parts list but only the subassemblies.

## Special Features 

### Assembly Structure 

The toolbar button <img alt="" src=images/A2p_Treeview.svg  style="width   *24px;"> creates an HTML file with the structure of your assembly. The file will by default be created in the folder of your assembly file. The structure looks like this   *

   *   ![](images/A2p_Dependency-Tree.jpg )

### Degrees of Freedom 

The button <img alt="" src=images/A2p_DOFs.svg  style="width   *24px;"> labels every part of the assembly with its degrees of freedom. Furthermore it outputs a list with all parts and their dependencies. The list is output into FreeCAD\'s widget *Report view*. If this widget is currently not visible, it can either be shown by right-clicking into an empty part of the FreeCAD toolbar area and then choosing it in the appearing context menu or with the menu **View → Panels → [Report view](Report_view.md)**.

The degrees of freedom labels can be removed by clicking the button <img alt="" src=images/A2p_DOFs.svg  style="width   *24px;"> again.

### Part Labels 

The button <img alt="" src=images/A2p_PartLabel.svg  style="width   *24px;"> labels every part of the assembly in the 3D view with its name. The part labels can be removed by clicking the button <img alt="" src=images/A2p_PartLabel.svg  style="width   *24px;"> again

### Shape of whole Assembly 

Sometimes it is necessary to have the whole assembly combined as one shape. This shape can then for example be used for 3D printing in the [Mesh workbench](Mesh_Workbench.md) or for drawings in the [TechDraw workbench](TechDraw_Workbench.md). It is created using the toolbar button <img alt="" src=images/A2p_SimpleAssemblyShape.svg  style="width   *24px;">. The shape is by default not made visible. Use the same toolbar button to update the shape in case of changes in the assembly.

### Convert absolute Paths to relative Ones 

With the menu **A2plus → Misc → [<img src=images/A2p_SetRelativePathes.svg style="width   *24px"> Convert absolute paths of imported parts to relative ones** you can convert absolute paths of imported parts to relative ones.

## Preferences

The a2plus preferences can be accessed via FreeCAD\'s menu **Edit → [Preferences](Preferences_Editor.md)** and there in the section *A2plus*. You can set the following options   *

### Default solving method 

Use solving of partial systems    * The solver begins with a part that has the property **fixed Position** set to *true* and a part constrained to it. All other parts are not calculated. If a solution could be found, the next constrained part is added to the calculation and so on.
Use \"magnetic\" solver, solving all parts at once    * The solver tries to move all parts at once in direction to a part that has the property **fixed Position** set to *true*. Note that this will in most cases take more time for the calculation of a solution.
Force fixed position    * This sets the property **fixed Position** to *true* for all parts in the assembly. Then no calculation is actually performed since all parts will always be fixed to the positions where they were created.

### Default solver behaviour 

Solve automatically if a constraint property is changed    * The solver will automatically be started. The same as turning on the toolbar button <img alt="" src=images/A2p_ToggleAutoSolve.svg  style="width   *24px;">.

### Behaviour when updating imported parts 

Recalculate imported parts before updating them    * All parts of the assembly, including subassemblies, will be opened in FreeCAD to be reconstructed using values from spreadsheets.
This feature is designed to construct fully parametrically. **Note   *** This feature is very experimental and not recommended for important projects.
Known problems   *

-   The assembly can be destroyed because of wrong references to topological names in parts
-   Master spreadsheets can get broken when they are edited while a referenced part file is already closed. This can crash FreeCAD.

Enable recursive update of imported parts    * Opens all subassemblies recursively to update them.





Use experimental topological naming    * While importing parts to the assembly an algorithm generates topological names for each subelement of the imported shape. The topological names are written into the **mux Info**. When an imported part needs to be updated, these topological names are used to update the subelements of the constraints. So assemblies get more robust against volatile subelement numbers of FreeCAD.
**Note   *** This increases file sizes and calculation time during import of parts. If topological naming should be used it has to be activated before the assembly is created.





Inherit per face transparency from parts and subassemblies    * Use colour and transparency settings from imported parts.
**Note   *** This feature is very experimental and not recommended for important projects.





Do not import invisible shapes    * This will hide invisible datum/construction shapes. **Note   *** No constraints must be connected to datum/construction shapes in higher or other subassemblies. Otherwise you can break the assembly.





Use solid union for importing parts and subassemblies    * All imported parts will directly be put together as union.
This feature is useful for [FEM](FEM_Workbench.md) simulations or [3D-printing](Manual_Preparing_models_for_3D_printing.md) if only one solid is allowed. The alternative is to create a [shape of the whole assembly](#Shape_of_whole_Assembly.md) later on.

### User interface settings 

Show constraints in toolbar    * If this option is not used, the toolbar buttons for the different constraints are not visible to save space in the toolbar. New constraints can still be set using the *Constraint Tools* dialog (toolbar button <img alt="" src=images/A2p_DefineConstraints.svg  style="width   *24px;">).
Use native file manager of your OS    * If this option is used, you get the file dialog of your OS when selecting files for assemblies.

### Storage of files 

Use relative paths for imported parts    * Uses relative file paths to the part files.
Use absolute paths for imported parts    * Uses absolute file paths to the part files.
All files are in this project folder    * All project files have to be in the specified folder. It doesn\'t matter if they are in subfolders of this folder. **Note   *** No file is allowed to exist several times in the folder (e.g. in different subfolders).
This option is helpful to work on different machines because then one only has to copy the project folder.

## Troubleshooting

Sooner or later you will get the problem that A2plus cannot solve the constraints you set. To overcome this, there are different strategies   *

### Using the Conflict Finder Tool 

This is the safest method when you have several constraints because this tool attempts to solve one constraint after another until it finds the conflicting constraint. Then you can go on with the other strategies to resolve the identified constraint. The tool is called using the toolbar button <img alt="" src=images/A2p_SearchConstraintConflicts.svg  style="width   *24px;">.

### Checking Constraint Direction 

Sometimes constraints seem to be consistently defined but they can nevertheless not be solved. An example   * Assume you have a {{Variable|[planesParallel](#Plane_Parallel.md)}} constraint set for two planes. Now you want to set for the same planes the {{Variable|[planeCoincident](#Plane_on_Plane.md)}} constraint and A2plus cannot solve this. Then the constraint directions of {{Variable|planesParallel}} and {{Variable|planeCoincident}} are different. Use the same direction for both constraints to fix this.

A2plus offers to automatically check the right direction for **all** constraints of the assembly using the toolbar button <img alt="" src=images/A2p_ReAdjustConstraints.svg  style="width   *24px;">.

### Deleting Constraints 

Most cases of unsolvable constraints occur directly when adding a new constraint. The solution is then to delete the constraint you added last. A2plus will propose this, too.

Sometimes the deletion strategy is the only one, for example when you edited a part in FreeCAD so that faces or edges connected to constraints are missing. You should then delete one constraint that is connected to the changed part at a time. Use the toolbar button <img alt="" src=images/A2p_solver.svg  style="width   *24px;"> after every deletion to see if you reached a solvable state.

When you got an assembly that can be solved, add step by step the constraints you need.

### Moving Parts 

In some cases the solver only needs better start values to solve the constraints. Take for example the case that you have an axle part and a wheel part. You add a {{Variable|axisCoincident }} constraint and get no info that the solver failed but the parts are not moved accordingly and in the *Report view* widget of FreeCAD you see \"*REACHED POS-ACCURACY    *0.0*\". A solution for this is to move the parts closer to that position you like to get by the constraint.

**Note   *** Assure that at least one part of the constraint has the property **fixed Position** set to *false*.

### Setting the Tip Property 

If you miss some features of your part after the import to an A2plus assembly, check the property **[Tip](PartDesign_MoveTip.md)**.

A2plus imports bodies of parts with all their features up to the tip feature. This is sensible because setting the tip to a certain feature means that all features behind the tip should not appear in the final part. So if you miss a part feature in A2plus, open the part via the toolbar button <img alt="" src=images/A2p_EditPart.svg  style="width   *24px;">, then select a body and look at its property **Tip**. If the tip is not at the feature where you want it, right-click on the feature where the tip should be and choose **[<img src=images/PartDesign_MoveTip.svg style="width   *24px"> Set tip**. Finally save the part and reload the assembly using the toolbar button <img alt="" src=images/A2p_ImportPart_Update.svg  style="width   *24px;">.

### Repairing Assembly Tree 

If you cannot see a clear reason why some constraints cannot be resolved, you can try to use the toolbar button <img alt="" src=images/A2p_RepairTree.svg  style="width   *24px;">. This will resolve all constraints and re-group then again under the different parts.

### Migrating old A2plus assemblies 

Assemblies created with A2plus older than March 2019 do not show the correct icons for imported parts and have obsolete properties. These assemblies can be migrated to A2plus version 0.4.35 and newer using the menu **A2plus → Misc → [<img src=images/A2p_Upgrade.svg style="width   *24px"> Migrate proxies of imported parts**. After doing this, you must save and reopen your assembly file.

### Avoiding Accented Characters 

**This strategy is not necessary for Windows.**

On some operating systems you can get problems if the file names or the file paths of parts or the assembly contain accented characters. Therefore avoid such characters and also special characters in general.

### Fixing Position 

**This strategy is no longer necessary for assemblies created with A2plus 0.3.11 or newer because A2plus issues now a warning for missing fixed positions.**

When you set a constraint between two parts and no part has the property **fixed Position** set to *true* or is connected by a constraint to a part with **fixed Position** set to *true*, the constraint cannot be solved. The same happens if both parts of the constraint have **fixed Position** set to *true*.

Then A2plus outputs the info about the failed solution, but sometimes you only see that the parts are not moved accordingly and in the *Report view* widget of FreeCAD you see \"*REACHED POS-ACCURACY    *0.0*\". This means the solver finished without errors but it could actually not solve the constraints.

Therefore check that at least one of your parts in the assembly has **fixed Position** set to *true*. Then assure that you only set constraints to a part which is somehow connected to the fixed part. To visualise these dependencies, see section [Assembly Structure](#Assembly_Structure.md).

### Rotating Parts 

**This strategy is no longer necessary for assemblies created with A2plus 0.4.0 or newer because A2plus rotates the parts now automatically a bit in the background to get a sufficient start angle for the solver.**

The solver often fails for the constraint {{Variable|angledPlanes}} if the two selected planes have currently an angle of 0° or 180°. (The parts are not moved accordingly and in the *Report view* widget of FreeCAD you see \"*REACHED POS-ACCURACY    *0.0*\".) A solution for this is to rotate one part by a few degrees using FreeCAD\'s transform feature (right-click on the part in the model tree and select in the context menu **Transform**).

**Note   *** Assure that at least one part of the constraint has the property **fixed Position** set to *false*.

## Animation

A2plus offers animations via dragging and via Python scripts.

### Dragging

Dragging animations are interactive since you trigger it by dragging a part of the assembly. To get these kind of animations   *

1.  Fully constrain the part whose movement or rotation should be animated
2.  Click on the toolbar button <img alt="" src=images/A2p_MovePartUnderConstraints.svg  style="width   *24px;">. This enables the dragging mode.
3.  Click on the desired part in the assembly.
4.  Now you can move the mouse and the part will follow the movement of the mouse within the defined constraints.
5.  To end the dragging mode, left click in the assembly or press ESC.

Here is an example assembly to try out the dragging animation   * [A2p\_example-for-dragging-animation.FCStd](https   *//forum.freecadweb.org/download/file.php?id=99204)

![](images/A2p_dragging-animation-result.gif )



*Above   * The dragging animation using the example assembly*

### Scripting

Despite the dragging mode offers nice interactive animations, they are sometimes not precise enough for screencasts or videos. Scripted animations have the advantage that they animate movements and rotations in a defined way. You can for example rotate a part by exactly 10° back and forth. The following examples use an assembly where a part should be rotated. If you try to animate this using the dragging mode, you will see how hard it is to get a back and forth rotation that you can e.g. show your boss in a presentation. With the interactive example script, however, this is an easy task.

A scripted animation works usually this way   *

1.  The assembly is fully constrained
2.  The script changes a parameter, for example the position or rotation angle of a part
3.  After the parameter change, the assembly constraints are solved
4.  Step 2. and 3. are repeated to get the animation

It is also possible to change instead of a placement parameter a constraint, for example the distance between 2 planes.

#### Simple Script Example 

The simplest way to script an animation is a non-interactive animation that follows a defined movement. Here is an example   * First download this assembly file   * [A2p\_animated-example.FCStd](https   *//forum.freecadweb.org/download/file.php?id=97554) and also this Python script   * [A2p\_animation-example-script.py](https   *//forum.freecadweb.org/download/file.php?id=97981).


<div class="mw-collapsible mw-collapsed toccolours">

This is the content of the script and the lines beginning with a \'\#\' describe what the different script lines do   *


<div class="mw-collapsible-content">


```python
# import libraries
import time, math, PySide
import A2plus.a2p_solversystem as a2p_solver

# we use steps of 1 degree
step = 1
# wait 1 ms between every step
timeout = 0.001
# initial angle is 0 degree
angle = 0
# we take the currently opened document
document = FreeCAD.activeDocument()
# we want later change the rotation angle of the part "star_wheel_001"
starWheel = document.getObject("star_wheel_001")
# define a progress dialog running from 0 to 360
progressDialog = PySide.QtGui.QProgressDialog(u"Animation progress", u"Stop", 0, 360)

# the while block is the main loop to change the angle and solve
# the assembly constraints subsequently
while angle < 360   * # run this loop until we have one full turn (360 degrees)
    # increase the rotation angle
    angle += step
    # set the new angle to the progress dialog
    progressDialog.setValue(angle)
    # change the rotation angle of the part "star_wheel_001"
    starWheel.Placement.Rotation.Angle = math.radians(angle)
    # solve the constraints 
    a2p_solver.solveConstraints(document, useTransaction=True)
    # update the view after the solving ('Gui' stands for 'graphical user interface')
    FreeCADGui.updateGui()
    # bring the progress dialog to front
    PySide.QtGui.QWidget.raise_(progressDialog)
    # if 'Stop' was pressed in the dialog, exit the loop
    if progressDialog.wasCanceled()   *
        angle = 360
    # wait some time before performing the next step
    time.sleep(timeout)
```


</div>


</div>

To use the script to perform the animation, we must

1.  Open the assembly file in FreeCAD.
2.  Open the script file in FreeCAD.
3.  Click on the toolbar button <img alt="" src=images/Menu_Std_DlgMacroExecute_fr_02.png  style="width   *24px;"> to execute the script (also called macro).
4.  Change to the tab of the assembly to see the rotation.

To practice, just change something in the script and execute it afterwards. For example increase *step* to *5*.

This is the result of the example animation   *

![](images/A2p_animated-example-result.gif )

#### Interactive Script Example 

The first script example demonstrated how to create an animation without any user feedback. For most applications you need to interact with the animation. For example the interesting issue in the example is to see how the driving pins cross the center groove of the wheel. To have a closer look you might present this detail to your colleagues or boss. Therefore you need an interactive solution.

This can be done by using a custom animation dialog with a slider. By moving the slider you can set the rotation angle and therefore rotate back and forth at interesting position.

We use the same assembly file   * [A2p\_animated-example.FCStd](https   *//forum.freecadweb.org/download/file.php?id=97554) and this Python script   * [A2p\_animation-example-script.py](https   *//forum.freecadweb.org/download/file.php?id=97982).


<div class="mw-collapsible mw-collapsed toccolours">

This is the content of the script to get the interactive animation dialog   *


<div class="mw-collapsible-content">


```python
# import libraries
import time, math, PySide, sys
import FreeCAD.A2plus.a2p_solversystem as a2p_solver
from FreeCAD import Units
from PySide import QtCore, QtGui

# wait 1 ms after every calculation
timeout = 0.001
# we take the currently opened document
document = FreeCAD.activeDocument()
# we want later change the rotation angle of the part "star_wheel_001"
starWheel = document.getObject("star_wheel_001")

class AnimationDlg(QtGui.QWidget)   * # the animation dialog

    def __init__(self)   * # to initialize the dialog
        super(AnimationDlg, self).__init__()
        self.initUI()

    def initUI(self)   * # the definition of the dialog components
        self.setMinimumSize(self.minimumSizeHint()) # set the minimal dialog size to minimum
        self.setWindowTitle('Animation Dialog')
        # use a grid layout for the whole form
        self.mainLayout = QtGui.QGridLayout()
        self.lineNo = 0 # first dialog grid line
        # add description label
        DescriptionLabel = QtGui.QLabel(self)
        DescriptionLabel.setText("Change slider to change rotation angle")
        self.mainLayout.addWidget(DescriptionLabel,self.lineNo,0,1,4)
         # next dialog grid line
        self.lineNo += 1
        # add a label; there is no need for the "self." prefix because we don't want to change the label later
        LabelMin = QtGui.QLabel(self)
        LabelMin.setText("Min")
        LabelMin.setFixedHeight(32)
        self.mainLayout.addWidget(LabelMin,self.lineNo,0)
        # add a spin edit to define the slider minimum
        self.MinEdit = QtGui.QSpinBox(self)
        # get the angle unit as string
        self.MinEdit.setSuffix(" " + str(FreeCAD.Units.Quantity(1, FreeCAD.Units.Angle))[2   *])
        self.MinEdit.setMaximum(999)
        self.MinEdit.setMinimum(0)
        self.MinEdit.setSingleStep(10)
        self.MinEdit.setValue(0)
        self.MinEdit.setFixedHeight(32)
        self.MinEdit.setToolTip("Minimal angle for the slider")
        QtCore.QObject.connect(self.MinEdit, QtCore.SIGNAL("valueChanged(int)"), self.setMinEdit)
        self.mainLayout.addWidget(self.MinEdit,self.lineNo,1)
        # add the slider
        self.slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        self.slider.setRange(0, 360)
        self.slider.setValue(0)
        self.slider.setFixedHeight(32)
        self.slider.setToolTip("Move the slider to change the rotation angle")
        QtCore.QObject.connect(self.slider, QtCore.SIGNAL("sliderMoved(int)"), self.handleSliderValue)
        self.mainLayout.addWidget(self.slider,self.lineNo,2)
        # add a label
        LabelMax = QtGui.QLabel(self)
        LabelMax.setText("Max")
        LabelMax.setFixedHeight(32)
        self.mainLayout.addWidget(LabelMax,self.lineNo,3)
        # add a spin edit to define the slider maximum
        self.MaxEdit = QtGui.QSpinBox(self)
        # get the angle unit as string
        self.MaxEdit.setSuffix(" " + str(FreeCAD.Units.Quantity(1, FreeCAD.Units.Angle))[2   *])
        self.MaxEdit.setMaximum(999)
        self.MaxEdit.setMinimum(1)
        self.MaxEdit.setSingleStep(10)
        self.MaxEdit.setValue(360)
        self.MaxEdit.setFixedHeight(32)
        self.MaxEdit.setToolTip("Maximal angle for the slider")
        QtCore.QObject.connect(self.MaxEdit, QtCore.SIGNAL("valueChanged(int)"), self.setMaxEdit)
        self.mainLayout.addWidget(self.MaxEdit,self.lineNo,4)
         # next dialog grid line
        self.lineNo += 1
        # add a spacer
        self.mainLayout.addItem(QtGui.QSpacerItem(10,10), 0, 0)
        # add a label
        LabelCurrent = QtGui.QLabel(self)
        LabelCurrent.setText("Current angle   *")
        LabelCurrent.setFixedHeight(32)
        self.mainLayout.addWidget(LabelCurrent,self.lineNo,1)
        # output the current angle
        self.CurrentAngle = QtGui.QLineEdit(self)
        self.CurrentAngle.setText(str(0))
        self.CurrentAngle.setFixedHeight(32)
        self.CurrentAngle.setToolTip("Current rotation angle")
        self.CurrentAngle.isReadOnly()
        self.mainLayout.addWidget(self.CurrentAngle,self.lineNo,2)
        # add label for the unit
        LabelUnit = QtGui.QLabel(self)
        LabelUnit.setText("deg")
        LabelUnit.setFixedHeight(32)
        self.mainLayout.addWidget(LabelUnit,self.lineNo,3)
        # button to close the dialog
        self.Close = QtGui.QPushButton(self)
        self.Close.setText("Close")
        self.Close.setFixedHeight(32)
        self.Close.setToolTip("Closes the dialog")
        QtCore.QObject.connect(self.Close, QtCore.SIGNAL("clicked()"), self.CloseClicked)
        self.mainLayout.addWidget(self.Close,self.lineNo,4)
        # place the defined grid layout to the dialog
        self.setLayout(self.mainLayout)
        self.update()

    def handleSliderValue(self)   *
        # set slider value as angle
        starWheel.Placement.Rotation.Angle = math.radians(self.slider.value())
        # output current angle
        self.CurrentAngle.setText(str(self.slider.value()))
        # solve the constraints 
        a2p_solver.solveConstraints(document)
        # update the view after the solving ('Gui' stands for 'graphical user interface')
        FreeCADGui.updateGui()
        # wait some time, important to give time to perform calculations
        time.sleep(timeout)

    def setMinEdit(self)   *
        # assure that the minimum is samller than the maximum
        if self.MinEdit.value() >=  self.MaxEdit.value()   *
            self.MaxEdit.setValue(self.MinEdit.value() + 1)
        self.slider.setRange(self.MinEdit.value(), self.MaxEdit.value())

    def setMaxEdit(self)   *
        # assure that the minimum is samller than the maximum
        if self.MinEdit.value() >=  self.MaxEdit.value()   *
            self.MinEdit.setValue(self.MaxEdit.value() - 1)
        self.slider.setRange(self.MinEdit.value(), self.MaxEdit.value())

    def CloseClicked(self)   *
        AnimationDialog.close()

# create and show the defined dialog
AnimationDialog = AnimationDlg()
AnimationDialog.show()

# run this loop when the dialog is visible
while AnimationDialog.isVisible()   *
    # update the view; important to give the OS feedback the dialog is alive
    FreeCADGui.updateGui()
    # bring the dialog to front, so that the dialog is always visible
    QtGui.QWidget.raise_(AnimationDialog)
    # output slider value here too because during the calculation the slider might have been moved
    AnimationDialog.CurrentAngle.setText(str(AnimationDialog.slider.value()))
```


</div>


</div>

The dialog defined in the script looks like this   *

![](images/A2p_AnimationDialog.png )

### Script Commands 

To understand the script syntax better, here is some command info   * 
```python starWheel.Placement.Rotation.Angle = math.radians(angle)```

Here we change the placement property `Rotation.Angle` of the part get got previously as `starWheel`. This property gets the angle as [radian](https   *//en.wikipedia.org/wiki/Radian). The function `radians()` from the library `math` converts the angle from degree to radian.

The property `Rotation.Angle` uses the current placement axis of the part (in our example the X-axis). To rotate the part e.g. around the Z-axis one can set the rotation axis (before calling the rotation command) using the command   * 
```python starWheel.Placement.Rotation.Axis = FreeCAD.Vector(0,0,1)``` Instead of rotating, parts can also be moved. To change for example the placement in Y-direction of the wheel, the command would be   * 
```python starWheel.Placement.Base.y = PositionShift``` In this case we would not define the variable `angle` but `PositionShift` that we change on every loop run.

There are different ways to set the placement of a part. Some are [ documented here](Placement.md). Unfortunately there is no list (yet) with all possible placement commands. 
```pythona2p_solver.solveConstraints(document, useTransaction=False/True)```

This is an A2plus-specific command. It solves the assembly constraints of the assembly we previously got as `document`. The option `useTransaction` specifies if FreeCAD should store every change in the undo/redo stack. For large animations you might therefore set it to `False`.




[Category   *Addons](Category_Addons.md) [Category   *External Workbenches](Category_External_Workbenches.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > A2plus Workbench/es
