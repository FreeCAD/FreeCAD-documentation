---
- GuiCommand:
   Name:Sketcher MapSketch
   MenuLocation:Part Design/Sketch → Map sketch to face...
   Workbenches:[Sketcher](Sketcher_Workbench.md), [PartDesign](PartDesign_Workbench.md)
   SeeAlso:[Sketcher New sketch](Sketcher_NewSketch.md)
---

## 描述

此工具会将一个存在的草图映射至一个几何图形的面上。以此草图创建的PartDesign特征可针对相加特征（如两种挤出成型方式Pad与evolution）与基础实体融合，或针对相减特征（如两种挖槽方式Pocket与Groove）与基础实体相减。

请注意，此工具不能用于创建新的草图。仅限于进行草图映射，或将存在的草图重新映射至实体面或PartDesign特征。典型的使用场景：

-   草图被创建在一个标准的平面上(XY, XZ, YZ)，而您却想将其映射至一个实体面上，从而进一步在此构建一个特征。
-   草图被映射至实体的某个特定面上，而您却需要把它映射至另一个不同的面上。
-   修复一个坏掉的模型。

<img alt="" src=images/Sketcher_MapSketch_00.png  style="width:480px;">

## Usage

## 如何使用

-   选择一个PartDesign特征上的面或一个实体上的面。
-   点击工具栏中的**![](images/)_[Map_sketch_to_face](Sketcher_MapSketch.md)**图标（或前往当前所用工作台中的PartDesign或Sketch菜单找此工具）。
-   在打开的**Select sketch**对话窗口中的列表里选择待映射至面上的草图，并点击OK。
-   草图将自动在编辑模式下打开。

## 在修复一个损坏的模型时使用草图映射工具

草图工作台中的草图映射工具（MapSketch）常用于修复损坏的模型。


<div class="mw-translate-fuzzy">

一个常见的用例是所依赖的关系图（graph）有所损坏。（您可以通过**Tools → Dependency graph**来查阅依赖关系图。）从模型树中间删除某个特征可能是造成这个问题的罪魁祸首。在以下示例中，我们将实际破坏并修复一个模型。


</div>

这是一个基础模型。其中有一个凸垫，一个凹槽，以及一个凹槽中凸垫。请注意，此模型的依赖图是线性的。

![](images/JschremppFCADEdit1.png )

我们现在已删除了凹槽以及凹槽所创建的草图（即Pocket与Sketch001）。注意到，依赖图一分为二，坏掉了。为了修复此模型，我们希望将Sketch002附于Pad的顶面上。在此模型的视图中，您将发现很容易选错面。

![](images/JschremppFCADEdit2.png )

为了修复此模型，我们首先改变此实体的可见性。即隐藏Pad001并令Pad可见。

![](images/JschremppFCADEdit3.png )

我们现在选择Pad的顶面，再选择草图映射工具。在弹出的对话框中选中Sketch002。此时，我们的模型就修复好了。在模型视图中，我们令Pad001可见，并隐藏Pad，即可看到正确的模型。

![](images/JschremppFCADEdit4.png )





{{Sketcher Tools navi

}}  
