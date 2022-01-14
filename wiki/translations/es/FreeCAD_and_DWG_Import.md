# FreeCAD and DWG Import/es
{{TOCright}}


{{Fake heading|sub=4|< Back to [[FreeCAD Howto Import Export]]}}

## ¿Por qué es difícil soportar archivos DWG en FreeCAD? 


<div class="mw-translate-fuzzy">

El formato **DWG es un formato de archivo binario de código cerrado** que no es soportado directamente por FreeCAD. Requiere un conversor de archivos externo de terceros para convertirlo primero e importar la conversión a FreeCAD para su uso.


</div>


<div class="mw-translate-fuzzy">

## ¿Qué necesito para poder importar archivos DWG? 


</div>


<div class="mw-translate-fuzzy">

## FreeCAD v0.19 y LibreDWG 


</div>

-   página web: <https://www.gnu.org/software/libredwg/>
-   licencia: GPLv2-o posterior
-   opcional, se utiliza para permitir la importación y exportación de archivos DWG


<div class="mw-translate-fuzzy">

A partir de la versión 0.19, FreeCAD ya no necesita el convertidor ODA y puede utilizar libreDWG directamente. Ten en cuenta que, dado que libreDWG es un trabajo en curso, dependiendo de tu archivo, los resultados podrían no ser los mismos.


</div>

#### Installation Windows 


<div class="mw-translate-fuzzy">

### Windows

LibreDWG puede ser configurado para trabajar en Windows descargando y descomprimiendo el apropiado [binario precompilado para Windows](https://github.com/LibreDWG/libredwg/releases) y [añadiendo la carpeta a la ruta de su sistema de versiones de Windows](https://duckduckgo.com/?t=ffab&q=how+para+añadir+una+carpeta+a+su+ruta+de+sistema+de+Windows).


</div>

#### Installation Linux/Unix systems 


<div class="mw-translate-fuzzy">

### Linux/Unix systemas 

git clone [https://git.savannah.gnu.org/git/libredwg.git](https://git.savannah.gnu.org/git/libredwg.git)
cd libredwg
mkdir build
cd build
cmake ..
make
make install (o usa checkinstall, o simplemente localiza y copia la utilidad dwg2dxf en tu ruta de ejecutables, entonces será autodetectada por FreeCAD)


</div>

You need to set the path to the executable manually. See [Import Export Preferences](Import_Export_Preferences#DWG.md).


<div class="mw-translate-fuzzy">

### openSUSE


</div>


<div class="mw-translate-fuzzy">

Para evitar problemas de ejecución del programa debe utilizar el paquete LibreDWG compilado para la distribución de openSUSE OS instalada. LibreDWG se instala normalmente con **YAST** (abbr. Yet another Setup Tool) la herramienta de instalación y configuración del sistema operativo Linux.


</div>

El usuario más experimentado obtiene primero una visión general de los posibles paquetes proporcionados. **Nota:** openSUSE tiene varias opciones para elegir al descargar LibreDWG. Para ver estas opciones, visite [Survey of provided LibreDWG packages on openSUSE](https://software.opensuse.org/search?utf8=%E2%9C%93&baseproject=ALL&q=libredwg).


<div class="mw-translate-fuzzy">

Para, por ejemplo, ordenadores de sobremesa, portátiles y servidores de 64 bits de Intel o AMD, la versión (x86\_64) es la que hay que seleccionar. Por lo tanto, **libredwg0** y **libredwg-tools**\' son la opción correcta para instalar.


</div>

Se recomienda obtener los paquetes binarios directamente. A continuación, seleccione la distribución correcta para su sistema operativo openSUSE instalado.

En cualquier terminal/consola (se requieren derechos de root) la instalación se realizará con:


```python
zypper install libredwg0 libredwg-tools
```

You need to set the path to the executable manually. See [Import Export Preferences](Import_Export_Preferences#DWG.md).


<div class="mw-translate-fuzzy">

### Convertidor ODA (antes Convertidor Teigha) 


</div>

-   página web: <https://www.opendesign.com/guestfiles/oda_file_converter>
-   licencia: freeware
-   opcional, utilizado para permitir la importación y exportación de archivos DWG


<div class="mw-translate-fuzzy">

El ODA Conversor es una pequeña utilidad de libre acceso que permite convertir entre varias versiones de archivos DWG y DXF. FreeCAD puede utilizarlo para ofrecer importación y exportación de DWG, convirtiendo los archivos DWG al formato DXF bajo el capó, y luego utilizando su importador DXF estándar para importar el contenido del archivo. Se aplican las restricciones del [importador DXF](Draft_DXF/es.md).


</div>

#### Instalación


<div class="mw-translate-fuzzy">

En todas las plataformas, sólo instalando el paquete apropiado de <https://www.opendesign.com/guestfiles/oda_file_converter> . Después de la instalación, si la utilidad no es encontrada automáticamente por FreeCAD, puede que sea necesario establecer la ruta del ejecutable del convertidor manualmente. abrir Editar → Preferencias → Importación-Exportación → DWG y llenar \"Camino al convertidor de archivos de Teigha\" apropiadamente.


</div>

### QCAD pro 


<small>(v0.20)</small> 

-   homepage: <https://qcad.org/en/qcad-command-line-tools#dwg2dwg>
-   license: commercial
-   optional, used to enable import and export of DWG files

QCAD is a well-known open-source DXF-based 2D CAD platform. It also offers a paid pro version, which is basically the open-source version plus support for the DWG format. When buying the pro version, QCAD also includes a DWG to DXF conversion utility that can be used by FreeCAD.

#### Installation

You need to set the path to the executable manually. See [Import Export Preferences](Import_Export_Preferences#DWG.md).

### CADExchanger Ambiente de trabajo 

La instalación de CADExchanger Workbench permite trabajar con archivos DWG a través de la integración con el producto comercial de pago de conversión de archivos [CADExchanger](https://cadexchanger.com/). Sólo tienes que seguir las instrucciones en el [repositorio GitHub](https://github.com/yorikvanhavre/CADExchanger). Puedes discutir este ambiente de trabajo en [su hilo del foro](https://forum.freecadweb.org/viewtopic.php?f=9&t=22227&p=462421).

Por el momento, el modo CADExchanger es el único que permite trabajar con archivos DWG 3D, convirtiéndolos a otros formatos 3D.


<div class="mw-translate-fuzzy">

## ¿Cuáles son las alternativas? 


</div>

### DoubleCAD XT 

También existe DoubleCAD XT (https://www.turbocad.com/content/doublecad-xt-v5). El programa es gratuito para uso personal y comercial. Requiere un registro gratuito para recibir un código de activación por correo electrónico. Este programa es sólo para Windows. Nota: no parece haber sido actualizado desde hace años.

### NanoCAD 5.0 

También existe nanoCAD 5.0 (https://nanocad.com/products/nanoCAD/download/). El programa es gratuito para uso personal y comercial. Requiere un registro gratuito para recibir un código de activación por correo electrónico. Este programa es sólo para Windows.


<div class="mw-translate-fuzzy">

### Exportar sus archivos de AutoCAD en formato amigable 


</div>

Exportar tus archivos de AutoCAD en un formato más amigable para FreeCAD, como DXF R12 o R14, SVG, y si la versión lo soporta, IGES. Todos son mejores alternativas al formato DWG cuando se utiliza FreeCAD.


<div class="mw-translate-fuzzy">

Es importante saber que, contrariamente a la creencia popular, no hay ninguna diferencia entre el contenido de un archivo guardado en los formatos DWG o DXF, siempre que se trate de la misma versión (por ejemplo, DWG 2014 frente a DXF 2014). Ambos formatos son mantenidos por Autodesk, y ambos soportan exactamente las mismas características. La diferencia es que DWG es cerrado (codificado por máquina) mientras que DXF es abierto.


</div>


<div class="mw-translate-fuzzy">

## ¿Qué puedo hacer para ayudar? 


</div>

### Promover el uso de formatos alternativos 

En pocas palabras, deje de aceptar trabajos realizados en formato DWG. En la práctica, esto es a menudo más fácil de decir que de hacer. Aún así, no sería una mala práctica para los usuarios y partidarios de FreeCAD evitar y rechazar el formato DWG siempre que sea posible.

### Utilizar la biblioteca LibreDWG y presentar informes de errores 

En la versión de desarrollo, como se mencionó anteriormente, se puede cambiar del convertidor propietario ODA a la biblioteca de software libre LibreDWG para archivos DWG (y DXF). Por favor, hazlo e informa de cualquier problema que encuentres.


 

[<img src="images/Property.png" style="width:16px"> File\_Formats](Category_File_Formats.md) [<img src="images/Property.png" style="width:16px"> Common Questions](Category_Common_Questions.md)

---
[documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > FreeCAD and DWG Import/es
