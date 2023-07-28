---
- GuiCommand:/zh-cn
   Name:校验草图…
   MenuLocation:Sketch → Validate sketch…
   Workbenches:[Sketcher](Sketcher_Workbench/zh-cn.md), [PartDesign](PartDesign_Workbench/zh-cn.md)
   SeeAlso:[重合约束](Sketcher_ConstrainCoincident/zh-cn.md), [Topological naming problem](Topological_naming_problem/zh-cn.md)
---

# Sketcher ValidateSketch/zh-cn



## 描述


<div class="mw-translate-fuzzy">

**草图验证（Validate sketch）**工具可用于修复不可编辑的草图、存在无效约束的草图，以及添加有缺失的[重合约束的根据DXF等文件中导入的几何图形所创建的草图](Sketcher_ConstrainCoincident.md)。此工具也可有效的定位本地草图中缺失的重合约束，这个问题将导致在您试图运用一个PartDesign特征时生成一个\"can\'t validate broken face\"错误。


</div>

![](images/Sketcher_ValidateSketch_taskpanel.png ) 
*The Sketcher validation task panel*



## 用法


<div class="mw-translate-fuzzy">

1.  选择待验证的草图，可以从模型树或通过单击3D视图中目标对象的一条边进行选择。**请注意：** 草图一定不能处于编辑模式中。如果您正处于草图编辑模式，需要[退出草图编辑模式](Sketcher_LeaveSketch.md)。
2.  从Sketch菜单或Part Design菜单中打开草图验证工具。
3.  执行的具体操作请参考下列[选项部分](#选项.md)。
4.  完成验证后点击**Close**按钮。


</div>



## 选项



### 缺失重合约束

找出有重合关系却缺失重合约束的顶点，并为之添加重合约束。按下**Find**按钮；程序会弹出一个对话框来报告找到了多少缺失的重合约束； 并在3D视图中以黄色小十字符号表示出来。按下**OK**来关闭此对话框，再按**Fix**按钮来添加缺失的重合约束。

如有需要，可在下拉字段中定义一个更大的公差值。

Press **Highlight troublesome vertexes** to highlight vertexes that are outside this tolerance.

This tolerance is also used by the **Find**/**Fix** process.

通过选择\"Ignore construction geometry\"复选框在分析过程中忽略造型几何图形。

### Invalid constraints 


<div class="mw-translate-fuzzy">

### 无效约束


</div>

For example, if there is a Circle-Line-Tangent constraint, but it references two lines, it is considered invalid.

(This sometimes happens due to the [Topological naming problem](Topological_naming_problem.md), i.e. the external geometry changes type).

It also does other checks, such as for empty links.

### Degenerated geometry 

Degenerated geometry can result from solver actions in a sketch.

For instance, if a line is forced to shorten to become almost a point.

Other examples: a zero length line or zero radius circle/arc.

### Reversed external geometry 


<div class="mw-translate-fuzzy">

### 逆向外部几何图形


</div>

This process might be helpful if sketches with external-geometry fail to solve because of these changes.

### Constraint orientation locking 


<div class="mw-translate-fuzzy">

### 约束方向锁定


</div>

Internally they work by constraining the angle between tangent vectors. With tangent constraint for example, the angle can be 0 or 180 degrees (co-directed or opposed vectors). The actual angle is remembered in the constraint data (\"constraint orientation is locked\"), it guards against flipping. But the angle can be erased (\"constraint orientation unlock\") or updated; these tools do exactly that.

The locking mechanism typically works well and this tool should not be needed. **It should only used after making a backup of the open document.**





{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ValidateSketch/zh-cn
