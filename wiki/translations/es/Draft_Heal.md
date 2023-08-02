---
- GuiCommand:
   Name: Draft Heal
   Name/es: Draft Heal
   Workbenches: Draft_Workbench, Arch_Workbench
   MenuLocation: Draft -> Utilities -> Heal
---

# Draft Heal/es


</div>

## Description


<div class="mw-translate-fuzzy">

## Descripción

Debido a la rápida evolución de FreeCAD, algunas definiciones de objetos pueden cambiar con el tiempo y entre versiones, lo que hace que algunos objetos de borrador encontrados en archivos anteriores no se carguen correctamente o contengan errores cuando se abren con una versión más reciente de FreeCAD. Este comando intenta reparar esos objetos defectuosos recreando uno nuevo desde cero, y luego copiando el contenido de las propiedades del anterior al nuevo. Puede ejecutarse con los objetos seleccionados, en cuyo caso solo mirará los objetos seleccionados o sin ningún objeto seleccionado. Todos los objetos del documento actual serán escaneados en busca de errores. Si no se encuentra ningún error, este comando no hará nada.


</div>

## Usage

1.  Optionally select one or more problematic objects. If no objects are selected the entire document will be processed.
2.  Select the **Utilities → <img src="images/Draft_Heal.svg" width=16px> Heal** option from the menu.
3.  If no errors are found the command will do nothing.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Heal/es
