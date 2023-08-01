---
- GuiCommand:
   Name:Path Job
   Name/zh:刀路作业
   Workbenches:[Path](Path_Workbench.md)
   MenuLocation:Path → Job
   Shortcut:**P** **F**
   SeeAlso:
---

# Path Job/zh


</div>



## 描述


<div class="mw-translate-fuzzy">

作业工具在活动文档中创建一个新的作业对象。 作业对象包含以下信息：

1.  刀具控制器定义列表，指定刀路操作刀具的几何，给进量和速度。
2.  刀路操作的工作流程顺序列表。
3.  基础实体 - 用于偏移的克隆。
4.  库存，表示将在刀路工作台进行铣削的原材料。
5.  设定表，包含刀路运行使用的输入，包括静态值和公式。
6.  指定输出G代码作业的目标路径，文件名和扩展名，后处理器配置参数 - 用于为目标CNC控制器生成相应的指令，并自定义单位，刀具更改，停车等\...


</div>



## 使用


<div class="mw-translate-fuzzy">

1.  点击 **<img src="images/Path-Job.png" width=16px> [作业](Path_Job.md)** 按钮


</div>


<div class="mw-translate-fuzzy">

作业GUI有五个水平对齐的选项卡，常规、输出、设置、刀具和工作计划。 您可以确认或取消对话框。


</div>



## 总揽

![](images/Job_1.jpg )


<div class="mw-translate-fuzzy">

-   **标签**：树视图中显示的作业标签。
-   **模型**：基础对象，通过其形状定义作业的刀路。 如果它是零件设计对象，则通常情况下基础对象是您在此处选择的主体。 如果"之前"在设计结构树中选择了一个元素，则单击"添加作业"图标的时候，该元素已在被选中并显示在此处。 您可以通过从下拉菜单中选择其他元素来更改它。
-   **描述**：您可以在此处为作业添加一些注释。 注释仅供您参考，不会影响刀路。


</div>

## Output

![](images/Job_2.jpg )


<div class="mw-translate-fuzzy">

-   **输出文件**：设置G代码输出的名称，扩展名和文件路径。 您可以使用以下占位符：
    -   ％D活动文档的目录
    -   ％d活动文档的名称（不带扩展名）
    -   ％M用户文件宏目录
    -   ％j作业名称


</div>


<div class="mw-translate-fuzzy">

-   **处理程序**：为您的机器选择的后期处理。
-   **参数**：根据需要为后处理程序添加参数。


</div>



## 夹持

![](images/Job_3.jpg )

-   **储积**：设定原材料的大小和形状。
-   **方向**：选定的边或面用于相应地定位基础或储积。
-   **对齐**：选择顶点来设置原点或移动基础或储积



## 刀具

![](images/Job_4.jpg )


<div class="mw-translate-fuzzy">

从你的刀具列表中添加你在本作业运行所需要的刀具


</div>

添加刀具后，如果你在本作业中需要不同的给进速率的话，你可以选择/更改给进速率和旋转速度。 这里的更改不会改变存储在刀具列表中的参数。

如果你已经添加了自己的刀具，你可以删除默认刀具



## 工作计划

![](images/Job_5.jpg )

如果你的作业中包含不止一个刀路运行的化，你可以决定他们的运行顺序。 你可以选择一个运行后点击向上或者乡下按钮来改变其执行顺序。


<div class="mw-translate-fuzzy">





</div>


{{Path_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Job/zh
