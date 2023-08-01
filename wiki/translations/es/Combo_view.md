# Combo view/es
## Introducción

El [Combo view](combo_view/es.md) es uno de los paneles principales del FreeCAD [interfaz](interface/es.md). Se encuentra en el lado izquierdo de la pantalla por defecto. Está *compuesto por dos secciones*, la:

-   [Sección superior](#Upper_section/es.md) que contiene dos pestañas: la pestaña **Modelo** y la pestaña **Tareas**
-   [Sección inferior](#Lower_section/es.md) muestra el [Editorial de propiedades](property_editor/es.md). Contiene dos pestañas: las propiedades **Ver** y **Datos**. El [Editor de propiedades](property_editor/es.md) sólo se muestra cuando la pestaña **Modelo** está *activa*, es decir, cuando la [vista de árbol](tree_view/es.md) es visible.


**Note:**

originalmente la parte superior ([vista de árbol](tree_view/es.md)) estaba separada de la parte inferior ([editor de propiedades](property_editor/es.md)) pero luego se combinaron, y así se creó la vista \"combo\".

## Sección superior 

La pestaña **Modelo** muestra la [ vista de árbol](tree_view/es.md), que es una representación del contenido del documento, incluyendo la geometría 2D y 3D con su historial paramétrico, pero también apoyando los objetos que contienen datos guardados en el documento.

La pestaña **Tareas** muestra el [panel de tareas](task_panel/es.md), que mostrará diferentes acciones dependiendo del banco de trabajo activo, y la herramienta activa.

<img alt="" src=images/FreeCAD_Combo_view_Tree_View_properties.png  style="width:" height="600px;"> <img alt="" src=images/FreeCAD_Combo_view_Task_panel.png  style="width:" height="600px;">



*La vista combinada tiene dos pestañas: la pestaña Modelo que controla la visualización de la [ vista de árbol](tree_view/es.md) y el [editor de propiedades](property_editor/es.md), y la pestaña Tareas que controla la visualización del [ panel de tareas](task_panel/es.md).*

## Sección inferior 

La parte inferior de la vista combinada muestra el [editor de propiedades](property_editor/es.md), que muestra dos pestañas para las propiedades **Vista** y **Datos**. El editor de propiedades sólo se muestra cuando la pestaña **Modelo** está activa, es decir, cuando la [ vista de árbol](tree_view/es.md) está visible.

-   La pestaña **Vista** muestra las propiedades de visualización de los objetos, que sólo afectan a su apariencia en la [Vista 3D](3D_view/es.md).

-   La pestaña **Datos** muestra las propiedades paramétricas de los objetos, que determinan cómo se definen realmente las formas geométricas.

<img alt="" src=images/FreeCAD_Combo_view_Tree_View_properties.png  style="width:" height="600px;"> <img alt="" src=images/FreeCAD_Combo_view_Tree_Data_properties.png  style="width:" height="600px;">



*La parte inferior de la vista combinada es el editor de propiedades, que muestra las propiedades de la Vista y los Datos.*

## Desactivando la vista Combo 

Para usar estas vistas por sí mismas, use el [editor de parámetros](Std_DlgParameter/es.md). Cree los siguientes subgrupos si no existen

-    `BaseApp/Preferences/DockWindows/TreeView`
    

-    `BaseApp/Preferences/DockWindows/PropertyView`
    

luego agregue el parámetro `Habilitado` de tipo `Booleano`, y póngalo en `True`.

Entonces activa la vista usando el menú, **Vista → Paneles → Vista de árbol** o **→ Vista de propiedades**.


{{Std Base navi

}} {{Interface navi}}



---
⏵ [documentation index](../README.md) > Combo view/es
