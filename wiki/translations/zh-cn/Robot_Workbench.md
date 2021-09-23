# Robot Workbench/zh-cn






**The Robot Workbench is unmaintained. If you have experience with the topic and are interested in maintaining it, please state your intention in the developer's section of the [https://forum.freecadweb.org/index.php FreeCAD forum].

The reason this workbench is still in the master source code is because this workbench is programmed in C++. If this workbench could be programmed in Python, then it could be made an [external workbench](external_workbenches.md) and it could be moved to a separate repository.
**

## Introduction

<img alt="Robot workbench icon" src=images/Workbench_Robot.svg  style="width:128px;">


<div class="mw-translate-fuzzy">

机器人工作台是一个用于模仿工业 [Robot 6-Axis](Robot_6-Axis/cn.md) 的工具，就像 [Kuka](http://kuka.com/)。 用它可以完成以下任务：

-   用机器人和工件设立一个模拟环境
-   创建和填补轨迹
-   将一个 CAD 零件的特征分解为轨迹
-   模拟机器人的运动及其可达性
-   将轨迹导出为机器人程序文件


</div>

You can do the following tasks:

-   Set up a simulation environment with a robot and work pieces.
-   Create and fill up movement trajectories.
-   Decompose features of a CAD part to a trajectory.
-   Simulate the robot movement and reaching distance.
-   Export the trajectory to a robot program file.


<div class="mw-translate-fuzzy">

你可以从这儿找到例子： [Example files](http://www.freecad-project.de/svn/ExampleData/Examples/RobotSimulation/) 或者去参考 [Robot tutorial](Robot_tutorial.md).


</div>


{{TOCright}}

<img alt="" src=images/Robot_Workbench_example.jpg  style="width:500px;">

## 工具

这里提供了设置机器人的主要命令。

### 机器人

创建和管理六轴机器人的工具


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Robot_CreateRobot.png  style="width:30px;"> [创建机器人](Robot_CreateRobot.md): 在场景中插入一个新机器人
-   <img alt="" src=images/Robot_Simulate.png  style="width:30px;"> [模拟轨迹](Robot_Simulate.md): 打开模拟对话框并进行轨迹模拟
-   <img alt="" src=images/Robot_Export.png  style="width:30px;"> [导出轨迹](Robot_Export.md): 导出一个机器人程序文件
-   <img alt="" src=images/Robot_SetHomePos.png  style="width:30px;"> [设置起始位置](Robot_SetHomePos.md): 设置机器人的起始位置
-   <img alt="" src=images/Robot_RestoreHomePos.png  style="width:30px;"> [还原初始位置](Robot_RestoreHomePos.md): 将机器人移动到起始位置


</div>

### 轨迹

创建和操作轨迹的工具。分为两种：参数性的和非参数性的。


<div class="mw-translate-fuzzy">

#### 非参数性轨迹

-   <img alt="" src=images/Robot_CreateTrajectory.png  style="width:30px;"> [创建轨迹](Robot_CreateTrajectory.md): 在场景中插入一个新机器人
-   <img alt="" src=images/Robot_SetDefaultOrientation.png  style="width:30px;"> [设置默认方位](Robot_SetDefaultOrientation.md): 设置默认的方位航向点
-   <img alt="" src=images/Robot_SetDefaultValues.png  style="width:30px;"> [设置速度参数默认值](Robot_SetDefaultValues.md): 设置默认的航向点创建
-   <img alt="" src=images/Robot_InsertWaypoint.png  style="width:30px;"> [插入航向点](Robot_InsertWaypoint.md): 从当前机器人位置向轨迹中插入一个航向点
-   <img alt="" src=images/Robot_InsertWaypointPre.png  style="width:30px;"> [插入航向点](Robot_InsertWaypointPre.md): 从当前的鼠标位置向轨迹中插入一个航向点


</div>


<div class="mw-translate-fuzzy">

#### 参数性轨迹

-   <img alt="" src=images/Robot_Edge2Trac.png  style="width:30px;"> [由边创建轨迹](Robot_Edge2Trac.md): 插入一个新对象，该对象将边分解为轨迹
-   <img alt="" src=images/Robot_TrajectoryDressUp.png  style="width:30px;"> [修饰轨迹](Robot_TrajectoryDressUp.md): 覆盖轨迹的一个或多个属性
-   <img alt="" src=images/Robot_TrajectoryCompound.png  style="width:30px;"> [轨迹复合](Robot_TrajectoryCompound.md): 由多个单轨迹创建一个复合轨迹


</div>


<div class="mw-translate-fuzzy">

## 脚本编程

本节是由 <https://github.com/FreeCAD/FreeCAD_sf_master/blob/master/src/Mod/Robot/RobotExample.py> 产生出来的，你可以直接使用这个文件。


</div>

See the [Robot API example](Robot_API_example.md) for a description of the functions used to model the robot displacements.

## Tutorials

-   [Robot 6-Axis](Robot_6-Axis.md)
-   [VRML Preparation for Robot Simulation](VRML_Preparation_for_Robot_Simulation.md)


<div class="mw-translate-fuzzy">


{{docnav|FEM_Workbench|Standard Menu}}


</div>


{{Robot Tools navi

}} 

[Category:Workbenches](Category:Workbenches.md)
