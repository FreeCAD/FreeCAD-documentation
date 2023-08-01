# Manual:The FreeCAD document/zh-cn
{{Manual:TOC/zh-cn}}

一个 FreeCAD 文档包含了场景中的所有对象。它可以包含分组和使用任何工作台创建的对象。因此，您可以在不同的工作台之间切换，仍然在同一个文档或文档中的对象上工作。文档是在保存工作时保存到磁盘的内容。在 FreeCAD 中，您还可以同时打开多个文档，并打开同一个文档的多个视图。

![](images/Freecad-document-01.jpg )

在文档中，对象可以被移动到分组中，并具有唯一的名称。管理分组、对象和对象名称主要是通过树视图进行的。在树视图中，您可以创建分组，将对象移动到分组中，删除对象或分组。通过在树视图或对象上右键单击，您可以重命名对象，更改它们的颜色，隐藏或显示它们，或者可能执行其他操作，这取决于当前的工作台。

![](images/Freecad-document-02.jpg )

FreeCAD 文档中的对象可以是不同类型的。每个工作台可以添加自己的对象类型，例如 [Mesh工作台添加了网格对象](Mesh_Workbench.md)，[Part 工作台添加了](Part_Workbench.md) Part 对象等等。

如果在 FreeCAD 中至少打开了一个文档，那么始终会有一个活动文档。活动文档是当前显示在 3D 视图中的文档，也是你当前正在操作的文档。如果切换到另一个文档的选项卡，那个文档将成为活动文档。大多数操作总是针对活动文档进行的。

FreeCAD 文档以 .FcStd 扩展名保存，它是一种基于 ZIP 的复合格式，类似于 LibreOffice。如果出现严重问题，通常可以解压缩文档并修复问题或恢复数据。

**延伸阅读**

-   [FreeCAD 文档结构](Document_structure.md)
-   [文件格式 FCStd](File_Format_FCStd.md)



---
⏵ [documentation index](../README.md) > Manual:The FreeCAD document/zh-cn
