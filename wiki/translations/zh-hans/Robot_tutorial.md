# Robot tutorial/zh-hans
{{TutorialInfo/zh-hans
|Topic= Robot Workbench
|Level= Beginner
|Time=
|Author=r-frank
|FCVersion=0.16.6703
|Files=
}}


<div class="mw-translate-fuzzy">

本指南用于指导你如何使用[机器人工作台来模拟一个机器人单元的设置](机器人工作台.md)。


</div>

![](images/Robot_Tutorial_RobotSimulation.gif ) 
*Final result of this tutorial*

## 开始之前

本指南用于FreeCAD 0.16.6703及以上版本,如果你没有在你的电脑上安装FreeCAD，请前往 [下载](下载.md) 页面并完成安装。


<div class="mw-translate-fuzzy">

本指南的目标是用于[工业机器人](http://en.wikipedia.org/wiki/Industrial_robot)，并不是用在移动或者服务机器人(详见 [1](http://en.wikipedia.org/wiki/Robot#Modern_robots) 现代机器人).


</div>

## Setting up the scene 

1.  Switch to the <img alt="" src=images/Workbench_Robot.svg  style="width:24px;"> [Robot Workbench](Robot_Workbench.md)
2.  Create a new document by choosing **File** → ** New** from the top menu
3.  Insert a Kuka IR500 robot into the scene by choosing **Robot** → **Insert Robots** → **Kuka IR500** from the top menu
4.  Change to axonometric view by clicking on the <img alt="" src=images/View-axometric.svg  style="width:24px;"> button
5.  Zoom to fit all by clicking on <img alt="" src=images/Std_ViewFitAll.svg  style="width:24px;"> [FitAll](Std_ViewFitAll.md) button
6.  Save your file \...

## Setting up a trajectory 

1.  Switch to the <img alt="" src=images/Workbench_Robot.svg  style="width:24px;"> [Robot Workbench](Robot_Workbench.md)
2.  Activate the model-tab in the [tree view](tree_view.md) by clicking on it
3.  Create a new trajectory by clicking on the <img alt="" src=images/Robot_CreateTrajectory.svg  style="width:24px;"> [Robot CreateTrajectory](Robot_CreateTrajectory.md) button
4.  Select the robot in the [tree view](tree_view.md)
5.  Set home position for robot by clicking on <img alt="" src=images/Robot_SetHomePos.svg  style="width:24px;"> [Robot\_SetHomePos](Robot_SetHomePos.md)
6.  Switch to the [Task Panel](Task_Panel.md)
7.  By using the sliders change robot position
8.  When robot and trajectory are selected in _ will insert the way-point in the trajectory
9.  Each way-point is shown with a yellow cross, the waypoints are connected with orange lines
10. Define at least three different way points and insert them in the trajectory

## Simulating robot movement 

1.  Select robot and trajectory in [tree view](tree_view.md)
2.  Select simulation by clicking on <img alt="" src=images/Robot_Simulate.svg  style="width:24px;"> [Robot Simulate](Robot_Simulate.md)
3.  Click on Play ** &#9654;** button
4.  Watch simulation


{{Tutorials navi

}} {{Robot Tools navi}}

---
[documentation index](../README.md) > [Robot](Robot_Workbench.md) > Robot tutorial/zh-hans
