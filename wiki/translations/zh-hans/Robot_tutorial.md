# Robot tutorial/zh-hans
---
 TutorialInfo:h-hans
   Topic:  Robot Workbench
   Level:  Beginner
   Time: 
   Author: r-frank
   FCVersion: 0.16.6703
   Files: 
}}


<div class="mw-translate-fuzzy">

本指南用于指导你如何使用机器人工作台来模拟一个机器人单元的设置。


</div>

! 
*Final result of this tutorial*

## 开始之前

本指南用于FreeCAD 0.16.6703及以上版本,如果你没有在你的电脑上安装FreeCAD，请前往 下载 页面并完成安装。


<div class="mw-translate-fuzzy">

本指南的目标是用于工业机器人，并不是用在移动或者服务机器人 现代机器人).


</div>

## Setting up the scene 

1.  Switch to the !{width="24"} Robot Workbench
2.  Create a new document by choosing **File** , ** New** from the top menu
3.  Insert a Kuka IR500 robot into the scene by choosing **Robot** , **Insert Robots** , **Kuka IR500** from the top menu
4.  Change to axonometric view by clicking on the !{width="24"} button
5.  Zoom to fit all by clicking on !{width="24"} FitAll button
6.  Save your file \...

## Setting up a trajectory 

1.  Switch to the !{width="24"} Robot Workbench
2.  Activate the model-tab in the tree view by clicking on it
3.  Create a new trajectory by clicking on the !{width="24"} Robot CreateTrajectory button
4.  Select the robot in the tree view
5.  Set home position for robot by clicking on !{width="24"} Robot_SetHomePos
6.  Switch to the Task Panel
7.  By using the sliders change robot position
8.  When robot and trajectory are selected in tree view clicking on !{width="24"} Robot InsertWaypoint will insert the way-point in the trajectory
9.  Each way-point is shown with a yellow cross, the waypoints are connected with orange lines
10. Define at least three different way points and insert them in the trajectory

## Simulating robot movement 

1.  Select robot and trajectory in tree view
2.  Select simulation by clicking on !{width="24"} Robot Simulate
3.  Click on Play ** &#9654;** button
4.  Watch simulation


{{Robot Tools navi

}} {{Userdocnavi
---



---
⏵ [documentation index](../README.md) > [Robot](Robot_Workbench.md) > Robot tutorial/zh-hans
