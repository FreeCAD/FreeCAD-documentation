# Interface/es
{{TOCright}}

## Introducción

La [interfaz](interface/es.md) de FreeCAD está basada en Qt, un conocido kit de herramientas de interfaz gráfica de usuario (GUI), particularmente utilizado en Linux, pero también disponible en Windows y MacOS.

<img alt="" src=images/FreeCAD_interface_base_divisions.svg  style="width   *1024px;">



*Interfaz estándar en la v0.19.*

La ventana principal de la aplicación puede dividirse a grandes rasgos en 11 secciones   *

1.  El [área de vista principal](main_view_area/es.md), que puede contener diferentes ventanas con pestañas.
2.  La [vista 3D](3D_view/es.md), normalmente incrustada en el [área de vista principal](main_view_area/es.md)
3.  La parte superior de la [vista\_combo](combo_view/es.md), que incluye la [vista\_árbol](tree_view/es.md) y el [panel\_tarea](task_panel/es.md)
4.  La parte inferior de la [vista\_combo](combo_view/es.md), que incluye el [editor de propiedades](property_editor/es.md)
5.  La [vista de selección](selection_view/es.md)
6.  La [vista de informe](report_view/es.md)
7.  La [consola de Python](Python_console/es.md)
8.  La [barra\_de\_estado](status_bar/es.md)
9.  El área de la barra de herramientas, ver la siguiente información sobre las barras de herramientas
10. El [Selector de ambientes de trabajo](Std_Workbench/es.md), que es una barra de herramientas
11. El [menú estándar](Standard_Menu/es.md)

## Componentes de la interfaz 

Como muchas piezas de software, FreeCAD incluye una barra de menú estándar, y luego una serie de barras de herramientas y paneles donde se encuentran las herramientas del usuario.

### Menús

Los [menús estándar](Standard_Menu/es.md) son   * {{StdMenu|[**Archivo**](Std_File_Menu/es.md)}}, {{StdMenu|[**Editar**](Std_Edit_Menu/es.md)}}, {{StdMenu|[**Vista**](Std_View_Menu/es.md)}}, {{StdMenu|[**Herramientas**](Std_Tools_Menu/es.md)}}, {{StdMenu|[**Macro**](Std_Macro_Menu/es.md)}}, {{StdMenu|[**Windows**](Std_Windows_Menu/es.md)}}, {{StdMenu|[**Ayuda**](Std_Help_Menu/es.md)}}.

### Barras de herramientas 

The standard toolbars that appear in the interface are   *

-   File toolbar   * tools to work with files, open documents, copy, paste, undo and redo actions.
-   [Workbench toolbar](Std_Workbench.md)   * it contains a single widget to select the active [workbench](workbenches.md).
-   Macro toolbar   * tools to record, edit, and execute [macros](macros.md).
-   View toolbar   * tools to control how objects appear in the [3D view](3D_view.md).
-   Structure toolbar   * tools to organize objects in the document, and create links to additional documents.

Pueden activarse y desactivarse haciendo clic con el botón derecho del ratón en un espacio vacío de una de las barras de herramientas y eligiendo el elemento deseado, o desde el menú, **Vista → Barras de herramientas**.

### Paneles

The main panels that allow working with objects are   *

-   [3D view](3D_view.md)   * the area where 2D and 3D geometry is drawn.
-   [Combo view](Combo_view.md)   * the panel that contains the [tree view](tree_view.md), the [task panel](task_panel.md), and the [property editor](property_editor.md).
-   [Tree view](Tree_view.md)   * the element that shows all objects in the document and their parametric history.
-   [Task panel](Task_panel.md)   * the panel that shows different actions and options depending on the drawing tool selected.
-   [Property editor](Property_editor.md)   * the place where object properties are modified.
-   [Selection view](Selection_view.md)   * the panel that shows elements that are currently selected.
-   [Report view](Report_view.md)   * the text box that shows different messages from the application and its tools.
-   [Python console](Python_console.md)   * the editor that allows running [Python](Python.md) code interactively to see results in the [3D view](3D_view.md).
-   [Status bar](Status_bar.md)   * the bar that shows certain messages from the application, and that has the [mouse navigation](Mouse_navigation.md) selector.
-   [DAG view](DAG_view.md)   * an alternative to the [tree view](tree_view.md), which shows the relationships between different objects through a graph.

A excepción de la vista 3D, todas pueden activarse y desactivarse haciendo clic con el botón derecho del ratón en un espacio vacío de una de las barras de herramientas superiores y eligiendo el elemento deseado, o desde el menú, **Vista → Paneles**.

Para activar y desactivar la barra de estado utilice el menú, **Vista → Barra de estado**.

### Otros


<div class="mw-translate-fuzzy">

Otras interfaces y ventanas útiles son   *

-   [Inspector de escenas](Std_SceneInspector/es.md)   * un panel que muestra los nodos Coin3D que componen el [scenegraph](scenegraph/es.md). Para los usuarios avanzados y los desarrolladores, puede ser útil para solucionar las operaciones que manipulan la escena directamente, y los objetos creados en la [vista 3D](3D_view/es.md).
-   [Gráfico de dependencias](Std_DependencyGraph/es.md)   * una ventana que muestra el gráfico de dependencias de todos los objetos del documento, creado con el programa auxiliar [Graphviz](http   *//graphviz.org/). Es útil para reconocer problemas en la creación de objetos, como las dependencias circulares, que pueden no ser del todo evidentes desde la [vista de árbol](tree_view/es.md) o la [vista de DAG](DAG_view/es.md).


</div>

### Personalización

Las barras de herramientas pueden tener más o menos botones, y se pueden crear barras de herramientas personalizadas con una mezcla de diferentes herramientas, y para almacenar macros desarrolladas.

Estas opciones se encuentran en el menú, **Herramientas → Personalizar**. Ver [personalización de la interfaz](Interface_Customization/es.md).


{{Interface navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Interface/es
