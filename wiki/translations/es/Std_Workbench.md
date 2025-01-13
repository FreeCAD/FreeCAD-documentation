---
 GuiCommand:
   Name: Std Workbench
   Name/es: Ambiente de Trabajo Std
   Empty: 1
   MenuLocation: Vista , Ambiente de Trabajo
   Workbenches: Workbenches/es
---

# Std Workbench/es


</div>



## Descripción


<div class="mw-translate-fuzzy">

El comando **Ambiente de trabajo Std** activa un [Ambiente de trabajo](Workbenches/es.md) seleccionado incluyendo su interfaz gráfica de usuario (GUI).


</div>

![](images/Std_Workbench_ComboBox_Icons_And_Text.png ) 
*The default ComboBox Workbench selector type*

![](images/Std_Workbench_TabBar_Icons_Only.png ) 
*The optional TabBar Workbench selector type (here displayed with icons only) <small>(v1.0*)</small> 



## Utilización


<div class="mw-translate-fuzzy">

1.  Hay varias maneras de invocar el comando:
    -   Seleccionar un ambiente de trabajo en la lista desplegable **Ambiente de trabajo** de la barra de herramientas del ambiente de trabajo. Esta opción no está disponible si el ambiente de trabajo actual es `<none>` (sin ambiente de trabajo).
    -   Seleccione un ambiente de trabajo en el submenú **Vista → Ambiente de trabajo**.


</div>



## Notas


<div class="mw-translate-fuzzy">

-   Se pueden descargar [Ambientes de trabajo externos](External_workbenches/es.md) adicionales con el <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestor de Complementos](Std_AddonMgr/es.md).


</div>



## Preferencias

See also: [Preferences Editor](Preferences_Editor.md).


<div class="mw-translate-fuzzy">

-   El ambiente de trabajo de inicio se puede cambiar en las preferencias: **Edición → Preferencias... → General → General → Inicio**. Véase [Editor de preferencias](Preferences_Editor/es#General.md).


</div>



## Guionización


<div class="mw-translate-fuzzy">


**Ver también:**

[Básicos de Guionización FreeCAD](FreeCAD_Scripting_Basics/es.md).


</div>


<div class="mw-translate-fuzzy">

Para cambiar el ambiente de trabajo utiliza el método `activateWorkbench` del módulo FreeCADGui. Este método no está disponible si FreeCAD está en modo consola.


</div>


```python
import FreeCADGui

FreeCADGui.activateWorkbench("PartDesignWorkbench")
```


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}  {{Interface navi}}



---
⏵ [documentation index](../README.md) > Std Workbench/es
