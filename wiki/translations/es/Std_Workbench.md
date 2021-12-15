---
- GuiCommand:/es
   Name:Std Workbench
   Name/es:Ambiente de Trabajo Std
   Empty:1
   MenuLocation:Vista → Ambiente de Trabajo
   Workbenches:[Ambiente de Trabajo](Workbenches/es.md)
---

# Std Workbench/es

## Descripción

El comando \'\'\'Ambiente de trabajo Std \'\'\' activa un [Ambiente de trabajo](Workbenches/es.md) seleccionado incluyendo su interfaz gráfica de usuario (GUI).

<img alt="" src=images/FreeCAD_interface_base_divisions.svg  style="width:800px;"> 
*La lista desplegable de Ambiente de trabajo indicada con el número 10 en la [interfaz](interface/es.md) estándar*

## Utilización

1.  Hay varias maneras de invocar el comando:
    -   Seleccionar un ambiente de trabajo en la lista desplegable **Ambiente de trabajo** de la barra de herramientas del ambiente de trabajo. Esta opción no está disponible si el ambiente de trabajo actual es `<none>` (sin ambiente de trabajo).
    -   Seleccione un ambiente de trabajo en el submenú **Vista → Ambiente de trabajo**.

## Notas


<div class="mw-translate-fuzzy">

-   Se pueden descargar _.


</div>

## Preferencias

-   El ambiente de trabajo de inicio se puede cambiar en las preferencias: **Edición → Preferencias... → General → General → Inicio**. Véase [Editor de preferencias](Preferences_Editor/es#General.md).

## Guionización


**Ver también:**

[Básicos de Guionización FreeCAD](FreeCAD_Scripting_Basics/es.md).

Para cambiar el ambiente de trabajo utiliza el método `activateWorkbench` del módulo FreeCADGui. Este método no está disponible si FreeCAD está en modo consola.


```python
import FreeCADGui

FreeCADGui.activateWorkbench("PartDesignWorkbench")
```





{{Std Base navi

}}  {{Interface navi}}

---
[documentation index](../README.md) > Std Workbench/es
