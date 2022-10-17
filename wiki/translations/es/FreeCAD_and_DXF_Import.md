# FreeCAD and DXF Import/es
{{TOCright}}

## Fondo

DXF es un formato de datos CAD propietario para dibujos 2D que se originó con AutoCAD. Se pueden encontrar más detalles en la página wiki [DXF](DXF/es.md).

## Introducción

Desde la versión 0.18 de FreeCAD hay un nuevo importador DXF en C++, y desde la versión 0.19 también un nuevo exportador DXF en C++. Estos nuevos componentes se instalan con FreeCAD.

Para utilizar el importador y exportador DXF más antiguo, heredado, es necesario instalar varios archivos. Estos archivos no se pueden incluir con FreeCAD ya que utilizan bibliotecas publicadas bajo una licencia que no es compatible con FreeCAD.

## Cómo instalar el importador y exportador DXF heredado 

### Automáticamente

Si los archivos no están ya instalados, ve al menú **Edición → Preferencias → Importar-Exportar → DXF** y activa la opción **Permitir a FreeCAD descargar y actualizar automáticamente las bibliotecas DXF** para que FreeCAD las descargue e instale automáticamente.

Para FreeCAD 0.14 o anterior hay que instalarlo manualmente   *

### Manualmente

1.  Go to [Yorik\'s Github account](https   *//github.com/yorikvanhavre/Draft-dxf-importer) and download these files (on the right side you can choose \"download as ZIP\").
2.  Put the files in your macro folder.
3.  If you are unsure where this folder is, go to **Edit → Preferences → General → Macro** and check the field named **Macro Path**.

-   In Ubuntu your macro folder is normally (the folder is hidden, you may need to unhide it)   *

/home/your_user_name/.FreeCAD 

-   In Windows your macro folder is normally   *

C   *Users\your_user_name\AppData\Roaming\FreeCAD

Ver también   * [Instalación del Importador Dxf](Dxf_Importer_Install/es.md)

## Consejos y trucos 

A veces los archivos DXF no se importan aunque se abren en otros programas CAD sin problemas.

You can try   *

1.  Go to **Edit → Preferences → Import-Export → DXF** and untick the option **Join geometry** and try again.
2.  Remember that maybe now you won\'t have coincident endpoints. You will have to make them coincident yourself.
3.  You can do this with the [Sketcher CloseShape](Sketcher_CloseShape.md) command <small>(v0.15)</small>  or you can apply the constraints manually.

You can also try   *

1.  Go to **Edit → Preferences → Draft → General settings** and adjust the value of **Tolerance** (default   * 0,05) and try again.

Para ver un resumen de todas las preferencias relacionadas con DXF, consulte [Preferencias de importación y exportación](Import_Export_Preferences/es#DXF.md).

[Category   *User_Documentation](Category_User_Documentation.md) [Category   *File_Formats](Category_File_Formats.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [User_Documentation](Category_User_Documentation.md) > [File_Formats](Category_File_Formats.md) > FreeCAD and DXF Import/es
