# Interface/es
## Introducción

La [interfaz](interface/es.md) de FreeCAD está basada en Qt, un conocido kit de herramientas de interfaz gráfica de usuario (GUI), particularmente utilizado en Linux, pero también disponible en Windows y MacOS.

<img alt="" src=images/FreeCAD_interface_base_divisions.svg  style="width:1024px;">



*Interfaz estándar en la v0.19.*

La ventana principal de la aplicación puede dividirse a grandes rasgos en 11 secciones:

1.  El [área de visualización principal](main_view_area/es.md), que puede contener diferentes ventanas con pestañas.
2.  La [vista 3D](3D_view/es.md), normalmente incrustada en el [área de visualización principal](main_view_area/es.md)
3.  La parte superior de la [vista combinada](combo_view/es.md), que incluye la [vista de árbol](tree_view/es.md) y el [panel de tareas](task_panel/es.md)
4.  La parte inferior de la [vista combinada](combo_view/es.md), que incluye el [editor de propiedades](property_editor/es.md)
5.  La [vista de selección](selection_view/es.md)
6.  La [vista de informe](report_view/es.md)
7.  La [consola de Python](Python_console/es.md)
8.  La [barra de estado](status_bar/es.md)
9.  El área de la barra de herramientas, ver la siguiente información sobre las barras de herramientas
10. El [selector de entornos de trabajo](Std_Workbench/es.md), que es una barra de herramientas
11. El [menú estándar](Standard_Menu/es.md)



## Componentes de la interfaz 

Como muchas piezas de software, FreeCAD incluye una barra de menú estándar, y luego una serie de barras de herramientas y paneles donde se encuentran las herramientas del usuario.



### Menús

Los [menús estándar](Standard_Menu/es.md) son: {{StdMenu|[**Archivo**](Std_File_Menu/es.md)}}, {{StdMenu|[**Editar**](Std_Edit_Menu/es.md)}}, {{StdMenu|[**Ver**](Std_View_Menu/es.md)}}, {{StdMenu|[**Herramientas**](Std_Tools_Menu/es.md)}}, {{StdMenu|[**Macro**](Std_Macro_Menu/es.md)}}, {{StdMenu|[**Windows**](Std_Windows_Menu/es.md)}}, {{StdMenu|[**Ayuda**](Std_Help_Menu/es.md)}}.



### Barras de herramientas 

Las barras de herramientas estándar que aparecen en la interfaz son:

-   Barra de herramientas de archivo: herramientas para trabajar con archivos, abrir documentos, copiar, pegar, deshacer y rehacer acciones.
-   [Barra herramientas de entorno de trabajo](Std_Workbench.md): contiene un único widget para seleccionar el [entorno de trabajo](workbenches/es.md) activo.
-   Barra de herramientas de Macros: herramientas para grabar, editar y ejecutar [macros](macros/es.md).
-   Barra de herramientas de vista: herramientas para controlar cómo aparecen los objetos en la [vista 3D](3D_view/es.md).
-   Barra de herramientas de extructura: herramientas para organizar objetos en el documento y crear enlaces a documentos adicionales.

Pueden activarse y desactivarse haciendo clic con el botón derecho del ratón en un espacio vacío de una de las barras de herramientas y eligiendo el elemento deseado, o desde el menú, **Vista → Barras de herramientas**.



### Paneles

Los principales paneles que permiten trabajar con objetos son:

-   [Vista 3D](3D_view/es.md): el área donde se dibuja la geometría 2D y 3D.
-   [Vista combinada](Combo_view/es.md): el panel que contiene al [vista de árbol](tree_view/es.md), el [ panel de tareas](task_panel/es.md), y el [editor de propiedades](property_editor/es.md).
-   [Vista de árbol](Tree_view/es.md): el elemento que muestra todos los objetos en el documento y su historial paramétrico.
-   [Panel de tareas](Task_panel/es.md): el panel que muestra diferentes acciones y opciones dependiendo de la herramienta de dibujo seleccionada.
-   [Editor de propiedades](Property_editor/es.md): el lugar donde se modifican las propiedades del objeto.
-   [Vista de selección](Selection_view/es.md): el panel que muestra los elementos que están actualmente seleccionados.
-   [Vista de informe](Report_view/es.md): el cuadro de texto que muestra diferentes mensajes de la aplicación y sus herramientas.
-   [Consola de Python](Python_console/es.md): el editor que permite ejecutar código [Python](Python/es.md) de forma interactiva para ver resultados en la [Vista 3D](3D_view/es.md).
-   [Barra de estado](Status_bar/es.md): la barra que muestra ciertos mensajes de la aplicación, y que tiene el selector de [navegación por ratón](Mouse_navigation/es.md).
-   [Vista DAG](DAG_view/es.md): una alternativa a la [vista de árbol](tree_view/es.md), que muestra las relaciones entre diferentes objetos a través de un gráfico.

A excepción de la vista 3D, todas pueden activarse y desactivarse haciendo clic con el botón derecho del ratón en un espacio vacío de una de las barras de herramientas superiores y eligiendo el elemento deseado, o desde el menú, **Vista → Paneles**.

Para activar y desactivar la barra de estado utilice el menú, **Vista → Barra de estado**.



### Otros

Otras interfaces y ventanas útiles son:

-   [Inspector de escenas](Std_SceneInspector/es.md): un panel que muestra los nodos Coin3D que componen la [escenografía](scenegraph/es.md). Para los usuarios avanzados y los desarrolladores, puede ser útil para solucionar las operaciones que manipulan la escena directamente, y los objetos creados en la [vista 3D](3D_view/es.md).
-   [Gráfico de dependencias](Std_DependencyGraph/es.md): una ventana que muestra el gráfico de dependencias de todos los objetos del documento, creado con el programa auxiliar [Graphviz](https://graphviz.org/). Es útil para reconocer problemas en la creación de objetos, como las dependencias circulares, que pueden no ser del todo evidentes desde la [vista de árbol](Tree_view/es.md) o la [vista de DAG](DAG_view/es.md).



### Personalización

Las barras de herramientas pueden tener más o menos botones, y se pueden crear barras de herramientas personalizadas con una mezcla de diferentes herramientas, y para almacenar macros desarrolladas.

Estas opciones se encuentran en el menú, **Herramientas → Personalizar**. Ver [personalización de la interfaz](Interface_Customization/es.md).


{{Interface navi

}}



---
⏵ [documentation index](../README.md) > Interface/es
