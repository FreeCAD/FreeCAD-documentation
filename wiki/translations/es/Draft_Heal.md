---
- GuiCommand:/es
   Name:Draft Heal
   Name/es:Draft Heal
   Workbenches:[Draft](Draft_Workbench.md), [Arch](Arch_Workbench.md)
   MenuLocation:Draft → Utilities → Heal
---


</div>

## Description


<div class="mw-translate-fuzzy">

## Descripción

Debido a la rápida evolución de FreeCAD, algunas definiciones de objetos pueden cambiar con el tiempo y entre versiones, lo que hace que algunos objetos de borrador encontrados en archivos anteriores no se carguen correctamente o contengan errores cuando se abren con una versión más reciente de FreeCAD. Este comando intenta reparar esos objetos defectuosos recreando uno nuevo desde cero, y luego copiando el contenido de las propiedades del anterior al nuevo. Puede ejecutarse con los objetos seleccionados, en cuyo caso solo mirará los objetos seleccionados o sin ningún objeto seleccionado. Todos los objetos del documento actual serán escaneados en busca de errores. Si no se encuentra ningún error, este comando no hará nada.


</div>

## Usage

1.  Optionally select one or more problematic objects. If no objects are selected the entire document will be processed.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Heal.svg" width=16px> [Draft Heal](Draft_Heal.md)** button.
    -   Select the {{MenuCommand|Utilities → <img src="images/Draft_Heal.svg" width=16px> Heal}} option from the menu.
3.  If no errors are found the command will do nothing.





 
