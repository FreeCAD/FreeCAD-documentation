---
 GuiCommand:
   Name: Std ToggleNavigation
   Name/ru: Std ToggleNavigation
   MenuLocation: Вид , Навигация/редактирование
   Workbenches: All
   Shortcut: **Esc**
---

# Std ToggleNavigation/ru

## Описание

The **Std ToggleNavigation** command is intended for certain inspection operations and certain interactive mesh editing operations. These operations are quite \'expensive\' and therefore rely on an edit mode during which most navigation options are disabled. With this command it is possible to temporarily switch from edit mode to navigation mode, and, after changing the [3D view](3D_view.md), switch back to edit mode.

Не путайте эту команду с командой [\"Редактировать/закончить редактирование\"](Std_Edit/ru.md).

## Применение

*An example to demonstrate the command:*

1.  Switch to the <img alt="" src=images/Workbench_Mesh.svg  style="width:16px;"> [Mesh Workbench](Mesh_Workbench.md).
2.  Select the **Meshes → <img src="images/Mesh_BuildRegularSolid.svg" width=16px> Regular solid...** option from the menu.
3.  The Regular Solid dialog box opens.
4.  Choose **Ellipsoid** from the dropdown list.
5.  Press the **Create** button.
6.  Press the **Close** button to close the dialog box.
7.  Select the mesh object.
8.  Press the **<img src="images/Mesh_PolyCut.svg" width=16px> [Mesh PolyCut](Mesh_PolyCut.md)** button.
9.  Pick points in the 3D view to define a polygon that overlaps one half of the mesh.
10. Right-click and choose **Inner** from the context menu.
11. The result is an open mesh with a boundary.
12. Make sure the mesh is still selected.
13. Select the **Meshes → <img src="images/Mesh_AddFacet.svg" width=16px> Add triangle** option from the menu to invoke the [Mesh AddFacet](Mesh_AddFacet.md) command.
14. If you hover over a boundary point a yellow marker will appear and a left-click will select it.
15. Optionally select two more points and add a triangle to the mesh.
16. You are now in edit mode and it is impossible to rotate or pan the 3D view, although zooming still works.
17. Invoke the **Std ToggleNavigation** command to switch to navigation mode:
    -   Select the **View → <img src="images/Std_ToggleNavigation.svg" width=16px> Toggle navigation/Edit mode** option from the menu.
    -   Or use the keyboard shortcut: **Esc**.
18. Now you can rotate and pan the 3D view, but you cannot pick points to add triangles.
19. Invoke the **Std ToggleNavigation** command to switch back to edit mode:
    -   Select the **View → <img src="images/Std_ToggleNavigation.svg" width=16px> Toggle navigation/Edit mode** option from the menu.
    -   Or use the keyboard shortcut: **Esc**.
20. You can again pick points and add triangles.
21. Right-click in the 3D view and choose **Finish** from the context menu to end the [Mesh AddFacet](Mesh_AddFacet.md) command.





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ToggleNavigation/ru
