---
- GuiCommand   *
   Name   *Path ToolLibraryEdit
   MenuLocation   *Path → Tool Manager
   Workbenches   *[Path](Path_Workbench.md)
   Shortcut   ***P** **T**
   SeeAlso   *
---

# Path ToolLibraryEdit/zh

## 描述


<div class="mw-translate-fuzzy">

刀具表编辑器用来编辑包含在[刀路作业中机加项目刀具表中不同的刀具](Path_Job.md). 该刀具表被包含在项目中于不同操作使用以获取当前刀具这一必要信息。


</div>

它也可以用来为你的作业选择刀具。

![](images/Path-Tooltable.png )


<div class="mw-translate-fuzzy">

操作非常直接   *

-   导入\...   * 从一个XML文件导入刀具表. {{Note|Warning|该功能当前有些问题，如果你从来没有在FreeCAD中使用过XML文件，该功能可能无法工作。}}
-   导出\...   * 以XML文件格式导出工具表。
-   新建刀具   * 打开一个可以输入你的刀具参数的对话框。详见新刀具
-   删除   * 删除当前所选行。{{Note|Warning|即便你取消会话刀具依旧会从你的刀具表中删除。}}
-   上移   * 你无法编辑刀具序号，但你可以将所选行上移来减少其刀具序号。。
-   下移   * 你也可以向下移动所选行来增大其刀具编号。


</div>

-   创建刀具控制器   * 如果你在刀具表左侧的复选框选择一个或多个 ，该按钮会被激活。如果你点击它，被选的刀具将被插入你当前的作业。

## 使用


<div class="mw-translate-fuzzy">

1.  选择一个[刀路作业](Path_Job.md)
2.  点击 **<img src="images/Path_ToolLibraryEdit.svg" width=16px> [刀具管理器](Path_ToolLibraryEdit/zh.md)** 按钮
3.  创建新刀具或者调整现有刀具属性。
    至少设置刀具直径, FreeCAD需要它来计算半径补偿。 截至版本0.17这是唯一需要的用于刀路创建的参数，然而如果你希望之后使用模拟刀具，你也可以增加切削刃角和切削刃高。
    ![](images/Path-ToolAdd.gif )


</div>

## 选项


<div class="mw-translate-fuzzy">

-   刀具可以使用上移/下移按钮重新排序。
-   完整的刀具表可以从XML文件导入(FreeCAD自有的工具表格式）或者HeeksCAD工具表导入。


</div>





{{Path_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path ToolLibraryEdit/zh
