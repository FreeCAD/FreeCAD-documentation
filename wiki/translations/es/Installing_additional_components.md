# Installing additional components/es
{{TOCright}}

# Introducción


<div class="mw-translate-fuzzy">

Después de instalar FreeCAD para tu sistema operativo ([Windows](Installing_on_Windows/es.md), [Linux](Installing_on_Linux/es.md) o [Mac](Installing_on_Mac/es.md)), puedes considerar la instalación de uno o más de los siguientes componentes adicionales.


</div>

# Archivos de ayuda 

La documentación fuera de línea no se envía con todos los instaladores, pero está disponible como un paquete separado. Consulte la página [Instalación del archivo de ayuda](Installing_Helpfile/es.md) para obtener más información.

# Ambientes de trabajo externos 

Aparte de los [Ambientes de Trabajo](workbenches/es.md) por defecto incluidos en FreeCAD, hay una gran colección de útiles [Ambientes de trabajo externos](External_workbenches/es.md) hechos por miembros de la comunidad.

# Software de terceros 

FreeCAD apoya varios paquetes de software de terceros fuera de la caja. En muchos casos todo lo que necesitas hacer es instalar el software, y cuando FreeCAD se reinicie lo encontrará automáticamente y será capaz de utilizarlo. Esta sección tiene como objetivo proporcionar una lista de tales paquetes de software, junto con alguna información sobre dónde se utilizan en FreeCAD y dónde se pueden descargar.

## Apoyo

### GitPython

_ puede utilizar esta biblioteca. GitPython está incluido en los instaladores de FreeCAD para Windows y Mac.

### GraphViz

_.

### OpenCAMLib

_. Consulte la página [OpenCamLib](OpenCamLib/es.md) para obtener instrucciones de instalación.

### OpenSCAD

_ depende de este software y el [Ambiente de trabajo Malla](Mesh_Workbench/es.md) lo utiliza para sus herramientas booleanas. También es necesario para la importación de archivos SCAD con la herramienta [Std Importar](Std_Import/es.md).

## Formatos de archivo 

Todo el software de esta sección será utilizado por las herramientas [Std Importar](Std_Import/es.md) o [Std Exportar](Std_Export/es.md).

### CADExchanger

[CADExchanger](https://cadexchanger.com) es una aplicación comercial para intercambiar varios formatos de archivos CAD. Existe un [ambiente de trabajo externo](https://github.com/yorikvanhavre/CADExchanger) para utilizar esta aplicación en FreeCAD.

### DXF Importador 

FreeCAD tiene un importador y exportador nativo para archivos DXF, programado en C++. Actualmente no implementan todas las características del formato DXF. Para esas características el importador y el exportador heredados de Python están todavía disponibles. Estos requieren la biblioteca Python _ para más información.

### DWG converters 

FreeCAD cannot directly read and write DWG files. To convert DXF files to DWG files, and vice-versa, FreeCAD relies on external converters. There is built-in support for the following DWG converters:

-   [LibreDWG](https://www.gnu.org/software/libredwg) (open-source, lacks support for some DWG entities).
-   [ODA File Converter](https://www.opendesign.com/guestfiles/oda_file_converter) (free, but not open-source).
-   [QCAD pro](https://qcad.org/en/qcad-command-line-tools#dwg2dwg) (commercial). <small>(v0.20)</small> 

See [Import Export Preferences](Import_Export_Preferences#DWG.md) and [FreeCAD and DWG Import](FreeCAD_and_DWG_Import.md) for more information.

### IfcOpenShell

_ ({{VersionMinus/es|0.18}}) y [BIM IfcExplorer](BIM_IfcExplorer/es.md). IfcOpenShell está incluido en los instaladores de FreeCAD para Windows y Mac.

### IfcJson

[IfcJson](https://github.com/buildingSMART/ifcJSON) es una biblioteca necesaria para exportar al formato de archivo IFCJSON. IFCJSON es un nuevo formato IFC que aún no es soportado por muchas aplicaciones.

### Pycollada

[Pycollada](https://github.com/pycollada/pycollada/releases), también conocido como python-collada, es una biblioteca de Python para leer y escribir archivos Collada (DAE). Pycollada se incluye en los instaladores de FreeCAD para Windows y Mac.

## Renderización

### LuxCoreRender

_. Oficialmente no está soportado por el _ para más información e instrucciones de instalación.

### LuxRender

_. En 2013 el proyecto ha sido reiniciado convirtiéndose en _ puede funcionar con el Ambiente de trabajo Trazado de rayos, podría valer la pena probarlo. Mira la página de [LuxRender](LuxRender/es.md) para más información e instrucciones de instalación, y la de [LuxCoreRender](LuxCoreRender/es.md) si quieres probar un software más moderno.

### POVRay

_. Vea la página [POV-Ray](POV-Ray/es.md) para más información e instrucciones de instalación.

## Elemento Finito 

### CalculiX

_.

### Gmsh

_ y [Malla DesdePiezaForma](Mesh_FromPartShape/es.md).

### Elmer

_.

### FEniCS

_

### Z88

_. FreeCAD requiere el paquete Z88OS de código abierto.

### OpenFOAM

_ y _.

# Páginas relacionadas 

-   [Importación Exportación](Import_Export/es.md)
-   [Preferencias de importación y exportación](Import_Export_Preferences/es.md)
-   [ Bibliotecas de terceros](Third_Party_Libraries/es.md)




_

---
[documentation index](../README.md) > Installing additional components/es
