# Manual:Import and export to other filetypes/zh-cn
{{Manual:TOC}}


<div class="mw-translate-fuzzy">

FreeCAD 可以导入和导出多种文件类型。以下是一些最重要的文件类型及其可用功能的简要描述：


</div>


<div class="mw-translate-fuzzy">

  格式    导入   导出   注释
     
  STEP    是     是     这是最可靠的导入/导出格式，因为它支持实体几何和 NURBS。只要可能，就使用它。
  IGES    是     是     一种较旧的实体格式，也得到了很好的支持。一些较旧的应用程序不支持 STEP，但支持 IGES。
  BREP    是     是     [OpenCasCade](https://en.wikipedia.org/wiki/Open_Cascade_Technology) 的本机格式，也是 FreeCAD 的几何内核。
  DXF     是     是     由 Autodesk 维护的开放格式。由于 DXF 文件中的 3D 数据以专有格式编码，FreeCAD 只能将 2D 数据导入/导出到该格式。
  DWG     是     是     DXF的专有版本。需要安装 [Teigha File Converter](https://www.opendesign.com/guestfiles) 实用程序。该格式受到与 DXF 相同的限制。
  OBJ     是     是     基于网格的格式。只能包含三角形网格。FreeCAD 的所有实体和基于 NURBS 的对象在导出时将转换为网格。Arch 工作台提供了另一种适合导出建筑模型的导出器。
  DAE     是     是     Sketchup 的主要导入/导出格式。只能包含三角形网格。FreeCAD 的所有实体和基于 NURBS 的对象在导出时将转换为网格。
  STL     是     是     基于网格的格式，常用于 3D 打印。只能包含三角形网格。FreeCAD 的所有实体和基于 NURBS 的对象在导出时将转换为网格。
  PLY     是     是     一种较旧的基于网格的格式。只能包含三角形网格。FreeCAD 的所有实体和基于 NURBS 的对象在导出时将转换为网格。
  IFC     是     是     [Industry Foundation Classes](https://en.wikipedia.org/wiki/Industry_Foundation_Classes)。需要安装 [IfcOpenShell-python](http://ifcopenshell.org/python)。IFC 格式及其与其他应用程序的兼容性是一项复杂的问题，请谨慎使用。
  SVG     是     是     一个出色而广泛使用的 2D 图形格式。
  VRML    是     是     一种相对较旧的基于网格的 Web 格式。
  GCODE   是     是     FreeCAD 已经可以导入和导出多种 GCode 格式，但目前只支持少数机器。
  CSG     是     否     OpenSCAD 的 [CSG](https://en.wikipedia.org/wiki/Constructive_solid_geometry)（构造实体几何）格式。


</div>

其中一些文件格式具有选项。这些选项可以从菜单**编辑→首选项→导入/导出：**进行配置。


<div class="mw-translate-fuzzy">

![](images/Import_preferences.jpg )


</div>

**延伸阅读**


<div class="mw-translate-fuzzy">

-   [FreeCAD 支持的所有文件格式](Import_Export.md)
-   [在 FreeCAD 中使用 DXF 文件](Draft_DXF.md):
-   [在 FreeCAD 中使用 SVG 文件](Draft_SVG.md)
-   [导入和导出到 IFC](Arch_IFC.md)
-   [OpenCasCade](http://www.opencascade.com)
-   [Teigha File Converter](https://www.opendesign.com/guestfiles)
-   [IFC 规范数据库](https://technical.buildingsmart.org/standards/ifc/ifc-schema-specifications/)
-   [IfcOpenShell](http://ifcopenshell.org/)


</div>



---
⏵ [documentation index](../README.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > [Tutorials](Category_Tutorials.md) > Manual:Import and export to other filetypes/zh-cn
