 {{TOCright}}


{{Fake heading|sub=4|< Back to [[FreeCAD Howto Import Export]]}}

## ¿Por qué es difícil soportar archivos DWG en FreeCAD? {#por_qué_es_difícil_soportar_archivos_dwg_en_freecad}

El formato **DWG es un formato de archivo binario de código cerrado** que no es soportado directamente por FreeCAD. Requiere un conversor de archivos externo de terceros para convertirlo primero e importar la conversión a FreeCAD para su uso.

Ten en cuenta que en este momento no es posible importar DWG 3D en FreeCAD. Los datos 3D están incrustados como datos binarios .SAT (ACIS), un formato propietario y no documentado.

## ¿Qué necesito para poder importar archivos DWG? {#qué_necesito_para_poder_importar_archivos_dwg}

### Convertidor ODA (antes Convertidor Teigha) {#convertidor_oda_antes_convertidor_teigha}

-   página web: <https://www.opendesign.com/guestfiles/oda_file_converter>
-   licencia: freeware
-   opcional, utilizado para permitir la importación y exportación de archivos DWG

El ODA Conversor es una pequeña utilidad de libre acceso que permite convertir entre varias versiones de archivos DWG y DXF. FreeCAD puede utilizarlo para ofrecer importación y exportación de DWG, convirtiendo los archivos DWG al formato DXF bajo el capó, y luego utilizando su importador DXF estándar para importar el contenido del archivo. Se aplican las restricciones del [importador DXF](Draft_DXF/es.md).

#### Instalación

En todas las plataformas, sólo instalando el paquete apropiado de <https://www.opendesign.com/guestfiles/oda_file_converter> . Después de la instalación, si la utilidad no es encontrada automáticamente por FreeCAD, puede que sea necesario establecer la ruta del ejecutable del convertidor manualmente. abrir Editar → Preferencias → Importación-Exportación → DWG y llenar \"Camino al convertidor de archivos de Teigha\" apropiadamente.

Para obtener instrucciones más detalladas, consulte \[<https://wiki.freecadweb.org/Dxf_Importer_Install/es#Tercer_paso>: este tutorial\].

#### Utilización

El programa puede utilizarse con la interfaz de línea de comandos o con la interfaz gráfica. Asegúrese de convertir los archivos DWG a un formato ASCII.

El formato de la línea de comandos es:

1.  Carpeta de entrada citada
2.  Carpeta de salida citada
3.  Versión\_de\_salida {\"ACAD9\", \"ACAD10\", \"ACAD12\", \"ACAD13\", \"ACAD14\", \"ACAD2000\", \"ACAD2004\", \"ACAD2007\", \"ACAD2010\"}
4.  Tipo de archivo de salida {\"DWG\", \"DXF\", \"DXB\"}
5.  Recurrir a la carpeta de entrada {\"0\", \"1\"}
6.  Auditar cada archivo {\"0\", \"1\"}
7.  Filtro de archivos de entrada \[opcional\] (por defecto: \"\*.DWG;\*.DXF\")

**Ejemplo para Linux**
ODAFileConverter \"/home/dwg-data\" \"/home/dxf-data\" \"ACAD2010\" \"DXF\" \"0\" \"1\" \"test.dwg\" El segundo número (auditoría) tiene que ser 1, de lo contrario falla

**Ejemplo para Windows**
\"C:\\NArchivos de Programa\\NODA\\NTeigha File Converter 3.08.2\\NTeighaFileConverter.exe\" \"Ruta-Del-Directorio-de-entrada\" \"Ruta-Del-Directorio-de-salida\" \"ACAD2010\" \"DXF\" \"0\" \"1\" \"Nombre-De-un-Archivo-de-Prueba.dwg\"

### CADExchanger Ambiente de trabajo {#cadexchanger_ambiente_de_trabajo}

La instalación de CADExchanger Workbench permite trabajar con archivos DWG a través de la integración con el producto comercial de pago de conversión de archivos [CADExchanger](https://cadexchanger.com/). Sólo tienes que seguir las instrucciones en el [repositorio GitHub](https://github.com/yorikvanhavre/CADExchanger). Puedes discutir este ambiente de trabajo en [su hilo del foro](https://forum.freecadweb.org/viewtopic.php?f=9&t=22227&p=462421).

Por el momento, el modo CADExchanger es el único que permite trabajar con archivos DWG 3D, convirtiéndolos a otros formatos 3D.

## FreeCAD v0.19 y LibreDWG {#freecad_v0.19_y_libredwg}

A partir de la versión 0.19, FreeCAD ya no necesita el convertidor ODA y puede utilizar libreDWG directamente. Ten en cuenta que, dado que libreDWG es un trabajo en curso, dependiendo de tu archivo, los resultados podrían no ser los mismos.

-   página web: <https://www.gnu.org/software/libredwg/>
-   licencia: GPLv2-o posterior
-   opcional, se utiliza para permitir la importación y exportación de archivos DWG

GNU LibreDWG es una biblioteca libre en C para manejar archivos DWG. Pretende ser un sustituto libre de las bibliotecas del SDK de Open Design Alliance Drawings.

## Instalación {#instalación_1}


<div class="mw-translate-fuzzy">

### .AppImage lanzamientos {#appimage_lanzamientos}

LibreDWG se incluye en v 0.19\_pre appimages[1](https://forum.freecadweb.org/viewtopic.php?f=8&t=39827&start=20#p372933)


</div>

### Windows

LibreDWG puede ser configurado para trabajar en Windows descargando y descomprimiendo el apropiado [binario precompilado para Windows](https://github.com/LibreDWG/libredwg/releases) y [añadiendo la carpeta a la ruta de su sistema de versiones de Windows](https://duckduckgo.com/?t=ffab&q=how+para+añadir+una+carpeta+a+su+ruta+de+sistema+de+Windows).

### Linux/Unix systemas {#linuxunix_systemas}

git clone [https://git.savannah.gnu.org/git/libredwg.git](https://git.savannah.gnu.org/git/libredwg.git)
cd libredwg
mkdir build
cd build
cmake ..
make
make install (o usa checkinstall, o simplemente localiza y copia la utilidad dwg2dxf en tu ruta de ejecutables, entonces será autodetectada por FreeCAD)

### openSUSE


<div class="mw-translate-fuzzy">

Para evitar problemas de ejecución del programa debe utilizar el paquete LibreDWG compilado para la distribución de openSUSE OS instalada. LibreDWG se instala normalmente con **YAST** (abbr. Yet another Setup Tool) la herramienta de instalación y configuración del sistema operativo Linux.


</div>

El usuario más experimentado obtiene primero una visión general de los posibles paquetes proporcionados. **Nota:** openSUSE tiene varias opciones para elegir al descargar LibreDWG. Para ver estas opciones, visite [Survey of provided LibreDWG packages on openSUSE](https://software.opensuse.org/search?utf8=%E2%9C%93&baseproject=ALL&q=libredwg).

Para, por ejemplo, ordenadores de sobremesa, portátiles y servidores de 64 bits de Intel o AMD, la versión (x86\_64) es la que hay que seleccionar. Por lo tanto, **libredwg0** y **libredwg-tools**\' son la opción correcta para instalar.

Se recomienda obtener los paquetes binarios directamente. A continuación, seleccione la distribución correcta para su sistema operativo openSUSE instalado.

En cualquier terminal/consola (se requieren derechos de root) la instalación se realizará con:

:   
    
```python
    zypper install libredwg0 libredwg-tools
    
```
    

Después, toda importación de archivos \*.dwg debería funcionar correctamente.

## ¿Cuáles son las alternativas? {#cuáles_son_las_alternativas}

### DoubleCAD XT {#doublecad_xt}

También existe DoubleCAD XT (https://www.turbocad.com/content/doublecad-xt-v5). El programa es gratuito para uso personal y comercial. Requiere un registro gratuito para recibir un código de activación por correo electrónico. Este programa es sólo para Windows. Nota: no parece haber sido actualizado desde hace años.

### NanoCAD 5.0 {#nanocad_5.0}

También existe nanoCAD 5.0 (https://nanocad.com/products/nanoCAD/download/). El programa es gratuito para uso personal y comercial. Requiere un registro gratuito para recibir un código de activación por correo electrónico. Este programa es sólo para Windows.

### Exportar sus archivos de AutoCAD en formato amigable {#exportar_sus_archivos_de_autocad_en_formato_amigable}

Exportar tus archivos de AutoCAD en un formato más amigable para FreeCAD, como DXF R12 o R14, SVG, y si la versión lo soporta, IGES. Todos son mejores alternativas al formato DWG cuando se utiliza FreeCAD.

Es importante saber que, contrariamente a la creencia popular, no hay ninguna diferencia entre el contenido de un archivo guardado en los formatos DWG o DXF, siempre que se trate de la misma versión (por ejemplo, DWG 2014 frente a DXF 2014). Ambos formatos son mantenidos por Autodesk, y ambos soportan exactamente las mismas características. La diferencia es que DWG es cerrado (codificado por máquina) mientras que DXF es abierto.

## ¿Qué puedo hacer para ayudar? {#qué_puedo_hacer_para_ayudar}

### Promover el uso de formatos alternativos {#promover_el_uso_de_formatos_alternativos}

En pocas palabras, deje de aceptar trabajos realizados en formato DWG. En la práctica, esto es a menudo más fácil de decir que de hacer. Aún así, no sería una mala práctica para los usuarios y partidarios de FreeCAD evitar y rechazar el formato DWG siempre que sea posible.

### Utilizar la biblioteca LibreDWG y presentar informes de errores {#utilizar_la_biblioteca_libredwg_y_presentar_informes_de_errores}

En la versión de desarrollo, como se mencionó anteriormente, se puede cambiar del convertidor propietario ODA a la biblioteca de software libre LibreDWG para archivos DWG (y DXF). Por favor, hazlo e informa de cualquier problema que encuentres.


 

[Category:File\_Formats{{\#translation:}}](Category:File_Formats.md) [Category:Common Questions{{\#translation:}}](Category:Common_Questions.md)
