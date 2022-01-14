# Manual:Import and export to other filetypes/zh-cn
{{Manual:TOC/zh-cn}}

FreeCAD 可以导入和导出多种类型的文件。下表列出了最重要的几种文件类型，并简要介绍了可用的功能。


<div class="mw-translate-fuzzy">

  格式    导入   导出   说明
  ------- ------ ------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  STEP    是     是     这是最忠实的导入/导出格式，因为它支持实体几何和 NURBS。只要可以，最好用它。
  IGES    是     是     这是较旧的实体几何格式，但也得到了很好的支持。一些较旧的应用程序不支持 STEP，但有IGES。
  BREP    是     是     这是 [OpenCasCade](https://en.wikipedia.org/wiki/Open_Cascade_Technology) 的原生格式，是 FreeCAD 的几何内核。
  DXF     是     是     这是由 Autodesk 公司维护的开放格式。因为 DXF 文件中的 3D 数据是以专有格式编码的，所以 FreeCAD 只能导入/导出此格式的 2D 数据。
  DWG     是     是     这是 DXF 的专有版本。需要安装 [Teigha 文件转换器](https://www.opendesign.com/guestfiles)程序。这种格式受到的限制与 DXF 相同。
  OBJ     是     是     这是基于网格的格式，只包含三角网格。导出时，FreeCAD 的所有实体和基于 NURBS 的对象都将转换为网格。Arch 工作台提供了另一种导出工具，更适合导出建筑模型。
  DAE     是     是     这是 Sketchup 的主要导入/导出格式，只包含三角网格。导出时，FreeCAD 的所有实体和基于 NURBS 的对象都将转换为网格。
  STL     是     是     这是基于网格的格式，通常用于 3D 打印，只包含三角网格。导出时，FreeCAD 的所有实体和基于 NURBS 的对象都将转换为网格。
  PLY     是     是     这是较旧的基于网格的格式，只包含三角网格。导出时，FreeCAD 的所有实体和基于 NURBS 的对象都将转换为网格。
  IFC     是     是     这是[工业基础类](https://en.wikipedia.org/wiki/Industry_Foundation_Classes)，需要安装 [IfcOpenShell-python](http://ifcopenshell.org/python.html)。IFC 格式本身，还有与其他应用程序的兼容性，都挺复杂，使用需谨慎。
  SVG     是     是     这是一个优秀的，使用广泛的 2D 图形格式。
  VRML    是     是     这是一种相当古老的基于网格的 Web 格式。
  GCODE   是     是     FreeCAD 已经可以导入和导出多种 GCode，但目前只支持少量机器。
  CSG     Yes    No     这是 OpenSCAD 的 [CSG](https://en.wikipedia.org/wiki/Constructive_solid_geometry) （构造实体几何）格式。


</div>


<div class="mw-translate-fuzzy">

其中一些文件格式有可选项，可以在菜单**编辑 -\> 首选项 -\> 导入/导出**里配置。


</div>

![](images/Import_preferences.jpg )

**延伸阅读**


<div class="mw-translate-fuzzy">

-   [FreeCAD 支持的所有文件格式](Import_Export.md)
-   [在 FreeCAD 中使用 DXF 文件](Draft_DXF.md)
-   [启用支持 DXF 和 DWG 格式](Dxf_Importer_Install.md)
-   [在 FreeCAD 中使用 SVG 文件](Draft_SVG.md)
-   [导入和导出到 IFC](Arch_IFC.md)
-   [OpenCasCade](http://www.opencascade.com)
-   [Teigha 文件转换器](https://www.opendesign.com/guestfiles)
-   [IFC格式](http://www.buildingsmart-tech.org/ifc/IFC4/final/html/index.htm)
-   [IfcOpenShell](http://ifcopenshell.org/)


</div>




[<img src="images/Property.png" style="width:16px"> Poweruser Documentation](Category_Poweruser_Documentation.md) [<img src="images/Property.png" style="width:16px"> Tutorials](Category_Tutorials.md)

---
[documentation index](../README.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > Manual:Import and export to other filetypes/zh-cn
