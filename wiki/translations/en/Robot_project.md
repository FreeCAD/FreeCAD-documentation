# Robot project/en



**
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
**


{{TOCright}}

This is [the project article](project.md) for the Robot project. It follows the rules of the \[<http://en.wikipedia.org/wiki/Getting_Things_Done#GTD_methodology>\| Getting things done\] process. The projects are collected in the [Development roadmap](Development_roadmap.md).

## Purpose and principles 

This project should lay down the principal technologies for a realistic robot simulation in FreeCAD. In the first step it targets the standard 6-axis industrial robot.

## Outcome

Robot simulation

![](images/Robot.jpg )

## Brainstorming

### Libs in field 

-   [OROCOS](http://www.orocos.org/) portable C++ libraries for advanced machine and robot control
-   [ROBOOP](http://roboop.sourceforge.net/) A robotics object oriented package in C++
-   [Beremiz](http://www.beremiz.org/) an OpenSource PLC.

### Standards for communication 

-   [OPC UA](http://en.wikipedia.org/wiki/OPC_Unified_Architecture) a machine to machine communication protocol for industrial automation (PLC)
-   [1](https://www.ipk.fraunhofer.de/de/referenzen/realistic-robot-simulation.html) German initiative to improve the accuracy of robot controllers and optimize offline robot programming
-   [Realistic Robot Simulation (RRS)](http://www.realistic-robot-simulation.org/) RRS-2, Virtual Robot Controller (VRC) Interface

### Middleware for comunication 

-   [D-Bus](http://en.wikipedia.org/wiki/D-Bus) a software bus, an inter-process communication (IPC), and a remote procedure call (RPC) mechanism that allows communication between multiple computer programs
-   [CORBA](http://en.wikipedia.org/wiki/Common_Object_Request_Broker_Architecture) enables collaboration between systems on different operating systems, programming languages, and computing hardware

### Commercial products in that field 

-   [Visual Components](http://www.visualcomponents.com/Solutions/Robot-Simulation)
-   [Delmia](http://www.3ds.com/products/delmia/welcome/)
-   [KUKA Sim](http://www.kuka-robotics.com/germany/en/products/software/kuka_sim/start.htm)

### Knowledge

-   [Kinematic definition](http://prt.fernuni-hagen.de/lehre/KURSE/PRT001/course_main/node15.html) \--\> link outdated!!!
-   [Denavit--Hartenberg parameters](https://en.wikipedia.org/wiki/Denavit%E2%80%93Hartenberg_parameters) parameters associated with a particular convention for attaching reference frames to the links of robot manipulator
-   [Roboter VRML modele](http://www.iha.tut.fi/education/IHA-3500/robotlib/) \--\> link outdated!!!

## Organizing

-   Visual representation of 6-Axis robots (done)
-   Forward and inverse kinematic calculation of arbitrary robots (done)
-   RobotLib, dynamic readably robot types (work in progress)
-   Trajectory simulation (work in progress)
    -   collision simulation
    -   detection of configuration changes and singularities
    -   time estimation
    -   used volume (planed)
-   Post processor for Kuka robots (work in progress)
-   Process and work cell control (planed)
-   Movie making out of simulation (planed)

## Next actions 

-   Trajectory and Waypoint management.



[Category:Roadmap](Category:Roadmap.md)
