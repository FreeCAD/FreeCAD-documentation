





{{VeryImportantMessage|The Robot Workbench is unmaintained. If you have experience with the topic and are interested in maintaining it, please state your intention in the developer's section of the [https://forum.freecadweb.org/index.php FreeCAD forum].

The reason this workbench is still in the master source code is because this workbench is programmed in C++. If this workbench could be programmed in Python, then it could be made an [external workbench](external_workbenches.md) and it could be moved to a separate repository.
}}

## Introduction

<img alt="Robot workbench icon" src=images/Workbench_Robot.svg  style="width:128px;">


<div class="mw-translate-fuzzy">

The robot workbench is a tool to simulate industrial grade [Robot 6-Axis](Robot_6-Axis/cs.md), like e.g. [Kuka](http://kuka.com/). You can do the following tasks:

-   set up a simulation environment with a robot and work pieces
-   create and fill up trajectories
-   decompose features of an CAD part to a trajectory
-   simulate the robot movement and reachability
-   export the trajectory to a robot program file


</div>

You can do the following tasks:

-   Set up a simulation environment with a robot and work pieces.
-   Create and fill up movement trajectories.
-   Decompose features of a CAD part to a trajectory.
-   Simulate the robot movement and reaching distance.
-   Export the trajectory to a robot program file.

To get started try the [Robot tutorial](Robot_tutorial.md), and see the programming interface in the [RobotExample.py](https://github.com/FreeCAD/FreeCAD_sf_master/blob/master/src/Mod/Robot/RobotExample.py) example file.


{{TOCright}}

<img alt="" src=images/Robot_Workbench_example.jpg  style="width:500px;">

## Tools

Here the principal commands you can use to create a robot set-up.

### Robots

The tools to create and manage the 6-Axis robots

-   <img alt="" src=images/Robot_CreateRobot.svg  style="width:30px;"> [Create a robot](Robot_CreateRobot.md): Insert a new robot into the scene
-   <img alt="" src=images/Robot_Simulate.svg  style="width:30px;"> [Simulate a trajectory](Robot_Simulate.md): Opens the simulation dialog and lets you simulate
-   <img alt="" src=images/Robot_Export.svg  style="width:30px;"> [Export a trajectory](Robot_Export.md): Export a robot program file
-   <img alt="" src=images/Robot_SetHomePos.svg  style="width:30px;"> [Set home position](Robot_SetHomePos.md): Set the home position of a robot
-   <img alt="" src=images/Robot_RestoreHomePos.svg  style="width:30px;"> [Restore home position](Robot_RestoreHomePos.md): move the robot to its home position

### Trajectories

Tools to create and manipulate trajectories. There are two kinds, the parametric and non parametric ones.

#### Non parametric trajectories 

-   <img alt="" src=images/Robot_CreateTrajectory.svg  style="width:30px;"> [Create a trajectory](Robot_CreateTrajectory.md): Inserts a new empty trajectory-object into the scene
-   <img alt="" src=images/Robot_SetDefaultOrientation.svg  style="width:30px;"> [Set the default orientation](Robot_SetDefaultOrientation.md): Set the orientation way-points gets created by default
-   <img alt="" src=images/Robot_SetDefaultValues.svg  style="width:30px;"> [Set the default speed parameter](Robot_SetDefaultValues.md): Set the default values for way-point creation
-   <img alt="" src=images/Robot_InsertWaypoint.svg  style="width:30px;"> [Insert a waypoint](Robot_InsertWaypoint.md): Insert a way-point from the current robot position into a trajectory
-   <img alt="" src=images/Robot_InsertWaypointPre.svg  style="width:30px;"> [Insert a waypoint preselected](Robot_InsertWaypointPre.md): Insert a way-point from the current mouse position into a trajectory

#### Parametric trajectories 

-   <img alt="" src=images/Robot_Edge2Trac.svg  style="width:30px;"> [Create a trajectory out of edges](Robot_Edge2Trac.md): Insert a new object which decompose edges to a trajectory
-   <img alt="" src=images/Robot_TrajectoryDressUp.svg  style="width:30px;"> [Dress-up a trajectory](Robot_TrajectoryDressUp.md): Lets you override one or more properties of a trajectory
-   <img alt="" src=images/Robot_TrajectoryCompound.svg  style="width:30px;"> [Trajectory compound](Robot_TrajectoryCompound.md): Create a compound out of some single trajectories

## Scripting

See the [Robot API example](Robot_API_example.md) for a description of the functions used to model the robot displacements.

## Tutorials

-   [6-Axis Robot](Robot_6-Axis/cs.md)
-   [VRML Preparation for Robot Simulation](VRML_Preparation_for_Robot_Simulation/cs.md)


<div class="mw-translate-fuzzy">


{{docnav/cs|Arch_Workbench/cs|Macros/cs}}


</div>


{{Robot Tools navi

}} 

[Category:Workbenches{{\#translation:}}](Category:Workbenches.md)
