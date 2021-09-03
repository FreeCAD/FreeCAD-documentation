





{{Manual:TOC/zh-cn}}

一份 FreeCAD 文件包含了场景中的所有对象。它可以包含任何工作台所创建的对象或它们的组合。因而你可以在工作台之间自由切换，但是仍在同一份 FreeCAD 文档上工作。当你保存你的工作成果时，这份 FreeCAD 文档便会被保存到磁盘中。可以在 FreeCAD 中同时打开多份文档，也可以为同一份文档开启多个视图。

![](images/Freecad-document-01.jpg )

在文档内部，对象可以移动到群组中，并具有唯一的名称。管理群组，对象和对象名称主要在树视图里完成。在那里，你可以创建群组，将对象移动到群组，删除对象或群组。通过右键单击树视图或对象，可以重命名对象，更改颜色，隐藏或显示它们，或者可能还有其他操作，具体取决于当前的工作台。

![](images/Freecad-document-02.jpg )


<div class="mw-translate-fuzzy">

FreeCAD 文档中的对象可以是不同类型的。每个工作台都可以添加自己的对象类型，例如[ Mesh Workbench](Mesh_Workbench.md) 添加网格对象，[Part Workbench](Part_Workbench.md) 添加 Part 对象，等等。


</div>

如果在 FreeCAD 中至少打开了一个文档，则有且只有一个活动文档，它就是当前 3D 视图中出现的文档，即您当前正在处理的文档。如果将选项卡切换到另一个文档，那么该文档将成为活动文档。大多数操作始终作用于活动文档。

FreeCAD 文档以 .FcStd 扩展名保存。这是一种基于 zip 的复合格式，类似于[LibreOffice](https://www.libreoffice.org)。如果出现什么问题，通常可以解压缩这个文档来解决问题或挽救数据。

**延伸阅读**

-   [FreeCAD 文档结构](Document_structure.md)
-   [文件格式 FCStd](File_Format_FCStd.md)




