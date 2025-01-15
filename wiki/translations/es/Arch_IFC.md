# Arch IFC/es
<div class="mw-translate-fuzzy">





</div>






## Descripción


<div class="mw-translate-fuzzy">

El <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [Arquitectura](Arch_Workbench/es.md) y <img alt="" src=images/Workbench_BIM.svg  style="width:24px;"> [BIM Ambientes de trabajo](BIM_Workbench/es.md) cuentan con un importador y exportador de [Industry Foundation Classes (IFC)](https://es.wikipedia.org/wiki/Industry_Foundation_Classes). El formato IFC es un formato en continuo crecimiento para intercambiar datos entre aplicaciones [Modelado de información de construcción](https://es.wikipedia.org/wiki/Modelado_de_informaci%C3%B3n_de_construcci%C3%B3n), (Inglés: BIM, Building Information Modelling) utilizadas en arquitectura e ingeniería.


</div>

Read more about handling IFC files in FreeCAD on the [NativeIFC](NativeIFC.md) page.

#### IfcOpenShell


<div class="mw-translate-fuzzy">

Tanto el importador como el exportador dependen de la biblioteca [IfcOpenShell](IfcOpenShell/es.md), que se incluye en algunas distribuciones de FreeCAD. Una forma fácil de comprobar si IfcOpenShell está disponible es introducir lo siguiente en la [Consola de Python](Python_console/es.md):


</div>


```python
import ifcopenshell
```


<div class="mw-translate-fuzzy">

Si no aparece ningún mensaje de error, IfcOpenShell está instalado y puede proceder a [importar](Std_Import/es.md) IFC. De lo contrario, tendrá que instalar IfcOpenShell usted mismo; lea la página [IfcOpenShell](IfcOpenShell/es.md) para obtener más información sobre este proceso.


</div>


<div class="mw-translate-fuzzy">


**Nota:**

el **[<img src=images/BIM_Setup.svg style="width:16px"> [BIM Configuración](BIM_Setup/es.md)** buscará también IfcOpenShell y emitirá una notificación si no está instalado.


</div>




<div class="mw-translate-fuzzy">

## Importación


</div>

Starting from version 1.0, FreeCAD opens and imports IFC files natively. Read more on the [NativeIFC](NativeIFC.md) page.

### Older importers 

#### The Arch importer 

The original IFC importer from the Arch Workbench has been disabled in FreeCAD version 1.0, but is still available from Python:


```python
from importers import importIFC
importIFC.open("C:\\Path\\To\\My\\File.ifc")
```

Todas las entidades basadas en [IfcProduct](http://www.buildingsmart-tech.org/ifc/IFC4/Add1/html/schema/ifckernel/lexical/ifcproduct.htm) de los archivos IFC2x3 o IFC4 se importarán en el documento de FreeCAD. Los ajustes de las preferencias IFC permiten establecer cómo se importan los objetos IFC:

-   **objetos paramétricos completos de Arquitectura**, la geometría será, en la medida de lo posible, editable en FreeCAD
-   **objetos Arquitectura no paramétricos**, los objetos llevarán información y propiedades IFC pero no serán editables
-   **Formas de pieza no paramétricas**, la geometría se renderizará fielmente pero la información IFC se descartará
-   Una forma de pieza por planta, un objeto todo en uno, sólo como referencia.

Cada uno de estos tipos pierde algo de información respecto al anterior, pero es más ligero en recursos, lo que permite abrir archivos más grandes. Un último tipo permite descartar por completo la importación de objetos Arquitectura, lo que resulta útil para los modelos analíticos estructurales.

Normalmente, si intentas abrir un archivo grande y FreeCAD tarda demasiado en importarlo, prueba con un modo de importación inferior.


<div class="mw-translate-fuzzy">

IfcOpenShell soporta todas las entidades IFC2x3 e IFC4 (IFC4-add1 e IFC4-add2 están siendo implementadas en la v0.6 y podrían estar disponibles para cuando usted lea esto) pero no todas ellas pueden ser convertidas en objetos [Arquitectura](Arch_Workbench/es.md), las que no puedan serán importadas como simples formas [Piezas](Part_Workbench/es.md). El importador IFC comienza importando todas las entidades IFC derivadas de [IfcProduct](http://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifckernel/lexical/ifcproduct.htm), es decir, básicamente, todos los objetos que componen un edificio, como paredes o ventanas o tuberías. Todas las demás entidades que necesite uno de estos objetos, como los perfiles de extrusión o los componentes de las operaciones booleanas, se importarán según sea necesario.


</div>

Si se usa un modo de importación que utiliza objetos Arquitectura, sean paramétricos o no, todos los objetos llevarán el conjunto completo de [IfcPropiedades](http://www.buildingsmart-tech.org/ifc/IFC4/Add1/html/schema/ifcpropertyresource/lexical/ifcproperty.htm) adjunto a cada objeto, agrupado por Property Set.

Las estructuras de los edificios, tales como sitios, edificios y plantas, también se importan fielmente y la estructura se recrea correctamente en FreeCAD. Las estructuras de grupo (usando IfcGrupos) también se importan y se renderizan en FreeCAD, y pueden combinarse con estructuras de edificios, por ejemplo, teniendo grupos dentro de plantas o plantas dentro de grupos.

También se importan los objetos [IfcAnnotation](http://www.buildingsmart-tech.org/ifc/IFC4/Add1/html/schema/ifcproductextension/lexical/ifcannotation.htm), así como las entidades basadas en líneas y curvas [IfcStructuralItem](http://www.buildingsmart-tech.org/ifc/IFC4/Add1/html/schema/ifcstructuralanalysisdomain/lexical/ifcstructuralitem.htm).

Los magnitudes especificadas en el archivo IFC NO se importan. Sin embargo, como la geometría se recrea completamente en FreeCAD, la mayoría de las cantidades como la longitud, el área, etc. son fácilmente obtenibles para cada objeto.

Si se activa la opción **mostrar mensajes de depuración** en la configuración de las preferencias de IFC, se imprimirá un informe que indicará si algún objeto del archivo IFC ha fallado en la importación.

**Nota**: El ambiente de trabajo BIM cuenta con una herramienta [IFC explorer](BIM_IfcExplorer/es.md) que permite abrir un archivo IFC en modo rápido, de sólo texto, e importar sólo las partes que desee.

#### The legacy importer 


<div class="mw-translate-fuzzy">


**Nota 2:**

en el pasado (2013) el Ambiente de trabajo arquitectura solía contar con un importador IFC más simple que no dependía de IfcOpenShell. Este módulo heredado todavía se incluye en el código fuente, pero a partir de la v0.19 no se recomienda en absoluto; sólo será capaz de importar un subconjunto muy pequeño de objetos IFC, y debe considerarse completamente obsoleto.


</div>

The legacy importer can be used from Python:


```python
from importers import importIFClegacy
importIFClegacy.open("C:\\Path\\To\\My\\File.ifc")
```



## Exportación

La exportación a archivos IFC exportará todos los objetos seleccionados y sus descendientes. Todos los objetos de Arch/BIM son compatibles, así como otros objetos creados en otras mesas de trabajo. Los únicos objetos no totalmente soportados, por el momento, son **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Cuerpos](PartDesign_Body/es.md)**, **[<img src=images/Std_Part.svg style="width:16px"> [Piezas](Std_Part/es.md)**, y nuevas estructuras como **[<img src=images/Link.svg style="width:16px"> [App Enlaces](Std_LinkMake/es.md)** y **[<img src=images/LinkGroup.svg style="width:16px"> LinkGroups**, por lo que tendrás que hacer un poco de pruebas si los usas. [Arch Referencias](Arch_Reference/es.md) exportará actualmente como `IfcBuildingElementProxies`.

Para exportar todo un solar o edificio o toda una planta o un grupo que contenga otros objetos, sólo es necesario seleccionar ese edificio o planta o grupo. Los objetos del arco se exportarán con el tipo establecido en su propiedad \"Tipo IFC\". Sus [IfcProperties](http://www.buildingsmart-tech.org/ifc/IFC4/Add1/html/schema/ifcpropertyresource/lexical/ifcproperty.htm) también se exportan, y si estos objetos tienen un UID IFC de una importación anterior, el mismo UID se mantendrá en la exportación. Los objetos que no son objetos Arch se exportan como [IfcBuildingElementProxy](http://www.buildingsmart-tech.org/ifc/IFC4/Add1/html/schema/ifcsharedbldgelements/lexical/ifcbuildingelementproxy.htm).

Los archivos IFC se exportan como IFC2x3 o IFC4 dependiendo de su versión de IfcOpenShell, que puede compilarse con cualquiera de los esquemas IFC. Si utiliza IfcOpenShell v0.6 o superior, se utilizará la versión IFC especificada en las preferencias de Arch.

Si la forma de los objetos exportados se basa en una extrusión o en una operación booleana, la operación y los componentes se exportarán correctamente a IFC. En caso contrario, la forma del objeto se exportará como [IfcFacetedBrep](http://www.buildingsmart-tech.org/ifc/IFC4x1/html/schema/ifcgeometricmodelresource/lexical/ifcfacetedbrep.htm). Si la forma contiene curvas, éstas serán trianguladas. Sin embargo, IfcOpenShell v0.5 o superior cuenta con un serializador, que debe ser habilitado en las preferencias de Importación/Exportación → IFC. Si está habilitado, este serializador es capaz de exportar objetos curvos muy complejos, como los basados en NURBS, y así evitar las caras trianguladas. Sin embargo, en el momento de escribir este artículo, pocas aplicaciones BIM admiten objetos IFC NURBS, por lo que se aconseja hacer algunas pruebas.



## Más información 

-   [IfcOpenShell](IfcOpenShell/es.md), más información sobre la instalación de esta biblioteca.


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > Arch IFC/es
