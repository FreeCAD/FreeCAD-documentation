---
- GuiCommand:
   Name:Std ProjectUtil
   Name/es:Std ProjectoUtil
   MenuLocation:Hierramientas → Utilidad del proyecto...
   Workbenches:Todo
---

# Std ProjectUtil/es

## Descripción

Con el comando **Std ProjectoUtil** puedes extraer archivos de un archivo de proyecto de FreeCAD (***.FCStd**), que es de hecho un archivo [ZIP](https://en.wikipedia.org/wiki/Zip_(file_format)), y, después de ediciones manuales, crear un nuevo archivo de proyecto a partir de ellos.

![](images/Project_utility_en.png ) 
*El cuadro de diálogo de la utilidad del proyecto*

## Utilización

### Extraer proyecto 

1.  Seleccione la opción **Hierramientas → <img src="images/Std_ProjectUtil.svg" width=16px> Utilidad del proyecto...** en el menú.
2.  Se abre el cuadro de diálogo Utilidad del proyecto.
3.  Pulse el botón **...** a la derecha de **Extraer proyecto → Fuente**.
4.  Seleccione el archivo ***.FCStd** que desea editar.
5.  Pulse el botón **...** a la derecha de **Extraer proyecto → Destina**.
6.  Seleccione una carpeta en la que deba extraerse el archivo del proyecto. Es aconsejable seleccionar una carpeta vacía.
7.  Pulse el botón **Extracto**.
8.  Pulse el botón **Cerrar** para cerrar el cuadro de diálogo.

### Manual ediciones 


<div class="mw-translate-fuzzy">

Es importante darse cuenta de que los archivos dentro de un archivo de proyecto de FreeCAD están interconectados. La edición de un solo archivo suele dar lugar a errores. Para hacer ediciones consistentes a través de múltiples archivos utiliza un buen editor de código, como [Notepad++](http://notepad-plus-plus.org/) (para el SO Windows) y [Notepadqq](https://notepadqq.com/s/) (para los SO Linux).


</div>

### Crea projecto 

1.  Select the **Tools → <img src="images/Std_ProjectUtil.svg" width=16px> Project utility...** option from the menu.
2.  The Project utility dialog box opens.
3.  Press the **...** button to the right of **Create project → Source**.
4.  Select the **Document.xml** file. The command will be automatically find all linked files.
5.  Press the **...** button to the right of **Create project → Destination**.
6.  Select a folder where the new project file should be created.
7.  Press the **Create** button.
8.  A new project file with a fixed name, **project.fcstd**, is created in the selected folder. There is no warning if a file with that name already exists.
9.  Optionally check the {{CheckBox|TRUE|Load project file after creation}} checkbox.
10. Press the **Close** button to close the dialog box.

## Notas

-   For more information about the FreeCAD project file format see [File Format FCStd](File_Format_FCStd.md).





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std ProjectUtil/es
