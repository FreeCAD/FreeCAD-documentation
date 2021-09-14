# Interface/pt-br

 {{TOCright}}

## Introdução

The FreeCAD [interface](interface.md) is based on Qt, a well known graphical user interface (GUI) toolkit, particularly used in Linux, but also available in Windows and MacOS.

<img alt="" src=images/FreeCAD_interface_base_divisions.svg  style="width:1024px;">


*Standard interface in v0.19.*

The main window of the application can be roughly divided into 11 sections:

1.  The [main view area](main_view_area.md), which can contain different tabbed windows
2.  The [3D view](3D_view.md), normally embedded in the [main view area](main_view_area.md)
3.  The upper part of the [combo view](combo_view.md), which includes the [tree view](tree_view.md) and [task panel](task_panel.md)
4.  The lower part of the [combo view](combo_view.md), which includes the [property editor](property_editor.md)
5.  The [selection view](selection_view.md)
6.  The [report view](report_view.md)
7.  The [Python console](Python_console.md)
8.  The [status bar](status_bar.md)
9.  The toolbar area, see the following information on the toolbars
10. The [Workbench selector](Std_Workbench.md), which itself is a toolbar
11. The [standard menu](Standard_Menu.md)

## Components of the interface 

Like many pieces of software, FreeCAD includes a standard menu bar, and then a series of toolbars and panels where the user tools are found.

### Menus

The [standard menus](Standard_Menu.md) are: {{StdMenu|[**File**](Std_File_Menu.md)}}, {{StdMenu|[**Edit**](Std_Edit_Menu.md)}}, {{StdMenu|[**View**](Std_View_Menu.md)}}, {{StdMenu|[**Tools**](Std_Tools_Menu.md)}}, {{StdMenu|[**Macro**](Std_Macro_Menu.md)}}, {{StdMenu|[**Windows**](Std_Windows_Menu.md)}}, {{StdMenu|[**Help**](Std_Help_Menu.md)}}.

### Toolbars

The standard toolbars that appear in the interface are:

-   File toolbar: tools to work with files, open documents, copy, paste, undo and redo actions.
-   [Workbench toolbar](Std_Workbench.md): it contains a single widget to select the active [workbench](workbenches.md).
-   Macro toolbar: tools to record, edit, and execute [macros](macros.md).
-   View toolbar: tools to control how objects appear in the [3D view](3D_view.md).
-   Structure toolbar: tools to organize objects in the document, and create links to additional documents.

These can be turned on and off by right clicking on an empty space on one of the toolbars and choosing the desired element, or from the menu, **View → Toolbars**.

### Panels

The main panels that allow working with objects are:

-   [3D view](3D_view.md): the area where 2D and 3D geometry is drawn.
-   [Combo view](Combo_view.md): the panel that contains the [tree view](tree_view.md), the [task panel](task_panel.md), and the [property editor](property_editor.md).
-   [Tree view](Tree_view.md): the element that shows all objects in the document and their parametric history.
-   [Task panel](Task_panel.md): the panel that shows different actions and options depending on the drawing tool selected.
-   [Property editor](Property_editor.md): the place where object properties are modified.
-   [Selection view](Selection_view.md): the panel that shows elements that are currently selected.
-   [Report view](Report_view.md): the text box that shows different messages from the application and its tools.
-   [Python console](Python_console.md): the editor that allows running [Python](Python.md) code interactively to see results in the [3D view](3D_view.md).
-   [Status bar](Status_bar.md): the bar that shows certain messages from the application, and that has the [mouse navigation](Mouse_navigation.md) selector.
-   [DAG view](DAG_view.md): an alternative to the [tree view](tree_view.md), which shows the relationships between different objects through a graph.

With the exception of the 3D view, all can be turned on and off by right clicking on an empty space on one of the top toolbars and choosing the desired element, or from the menu, **View → Panels**.

To activate and deactivate the status bar use the menu, **View → Status bar**.

### Other

Other useful interfaces and windows include:

-   [Scene inspector](Std_SceneInspector.md): a panel that shows the Coin3D nodes that make up the [scenegraph](scenegraph.md). For power users and developers, it may be useful to troubleshoot operations that manipulate the scene directly, and the objects created in the [3D view](3D_view.md).
-   [Dependency graph](Std_DependencyGraph.md): a window showing the dependency graph of all the objects in the document, created with the auxiliary program [Graphviz](Graphviz.md). It is helpful to recognize problems in the creation of objects, such as circular dependencies, which may not be entirely evident from the [tree view](tree_view.md) or the [DAG view](DAG_view.md).

### Customization

Toolbars can have more or fewer buttons, and custom toolbars can be created with a mix of different tools, and to store developed macros.

These options are in the menu, **Tools → Customize**. See [interface customization](Interface_Customization.md).


{{Interface navi

}} 
