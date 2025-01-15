# Manual:Import and export to other filetypes/es
{{Manual:TOC}}


<div class="mw-translate-fuzzy">

FreeCAD puede importar y exportar a muchos tipos de archivos. Aquí hay una lista de los más importantes con una breve descripción de las características disponibles


</div>


<div class="mw-translate-fuzzy">

  Formato   Importar   Exportar   Notas
     
  STEP      Sí         Sí         Este es el formato de importación/exportación más fiel disponible, ya que soporta geometría sólida y NURBS. Utilícelo siempre que sea posible.
  IGES      Sí         Sí         Un formato sólido más antiguo, también muy bien soportado. Algunas aplicaciones antiguas no soportan STEP pero sí IGES.
  BREP      Sí         Sí         El formato nativo de [OpenCasCade](https://en.wikipedia.org/wiki/Open_Cascade_Technology), el núcleo de geometría de FreeCAD.
  DXF       Sí         Sí         Un formato abierto mantenido por Autodesk. Como los datos 3D dentro de un archivo DXF están codificados en un formato propietario, FreeCAD sólo puede importar/exportar datos 2D a/desde este formato.
  DWG       Sí         Sí         La versión propietaria de DXF. Requiere la instalación de la utilidad [Teigha File Converter](https://www.opendesign.com/guestfiles). Este formato sufre las mismas limitaciones que el DXF.
  OBJ       Sí         Sí         Un formato basado en mallas. Sólo puede contener mallas trianguladas. Todos los objetos sólidos y basados en NURBS de FreeCAD serán convertidos a malla en la exportación. El banco de trabajo Arch proporciona un exportador alternativo, más adecuado para la exportación de modelos arquitectónicos.
  DAE       Sí         Sí         El principal formato de importación/exportación de Sketchup. Sólo puede contener mallas trianguladas. Todos los objetos sólidos y basados en NURBS de FreeCAD se convertirán en mallas en la exportación.
  STL       Sí         Sí         Un formato basado en mallas, comúnmente utilizado para la impresión 3D. Sólo puede contener mallas trianguladas. Todos los objetos sólidos y basados en NURBS de FreeCAD serán convertidos a malla en la exportación.
  PLY       Sí         Sí         Un formato más antiguo basado en mallas. Sólo puede contener mallas trianguladas. Todos los objetos sólidos y basados en NURBS de FreeCAD serán convertidos a malla en la exportación.
  IFC       Sí         Sí         [Industry Foundation Classes](https://en.wikipedia.org/wiki/Industry_Foundation_Classes). Requiere la instalación de [IfcOpenShell-python](http://ifcopenshell.org/python). El formato IFC y su compatibilidad con otras aplicaciones es un asunto complejo, utilícelo con cuidado.
  SVG       Sí         Sí         Un excelente y extendido formato de gráficos 2D
  VRML      Sí         Sí         Un formato web bastante antiguo basado en mallas.
  GCODE     Sí         Sí         FreeCAD ya puede importar y exportar a/desde varios sabores de GCode, pero sólo un pequeño número de máquinas es soportado por el momento.
  CSG       Sí         No         El formato [CSG](https://en.wikipedia.org/wiki/Constructive_solid_geometry) (Constructive Solid Geometry) de OpenSCAD.


</div>

Algunos de estos formatos de archivo tienen opciones. Estas se pueden configurar desde el menú **Edición → Preferencias → Importar/exportar:**


<div class="mw-translate-fuzzy">

![](images/Import_preferences.jpg )


</div>

**Leer más**


<div class="mw-translate-fuzzy">

-   [Todos los formatos de archivo soportados por FreeCAD](Import_Export/es.md)
-   [Trabajar con archivos DXF en FreeCAD](Draft_DXF/es.md):
-   [Trabajar con archivos SVG en FreeCAD](Draft_SVG/es.md)
-   [Importar y exportar a IFC](Arch_IFC/es.md)
-   [OpenCasCade](http://www.opencascade.com)
-   [Teigha File Converter](https://www.opendesign.com/guestfiles)
-   [El formato IFC](http://www.buildingsmart-tech.org/ifc/IFC4/final/html/index.htm)
-   [IfcOpenShell](http://ifcopenshell.org/)


</div>



---
⏵ [documentation index](../README.md) > [Poweruser Documentation](Category_Poweruser%20Documentation.md) > [Tutorials](Category_Tutorials.md) > Manual:Import and export to other filetypes/es
