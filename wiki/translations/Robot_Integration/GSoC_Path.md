# GSoC Path/Robot Integration
This page describes the Google Summer of Code project idea regarding integration between the Path(CNC) and Robot workbenches.

This project may not be fully achievable in the time frame allowed. A proposal that moves this project toward completion without achieving all expected outcomes described below is acceptable. However, your proposal should include specific goal that you intend to achieve in the time permitted.

## Outline

FreeCAD aims to provide general engineering functionality beyond CAD. One of the more recent workbenches added to FreeCAD is Path which provides CNC/CAM (Computer Numerical Control/ Computer Aided Machining) capability. Path makes it possible for the user to start with a model of a part and generate the machine control code (gcode) to drive a CNC machine to manufacture the physical part. It provides tools to generate, organize, sequence, and visualize the paths that a cutter will follow to cut a part from the stock material. Path is still in early development but already provides many tools to manufacture parts including Drilling, Engraving, Pocketing, Profiling, Contour, and Surface operations. One area where Path lags commercial applications is in visualizing and simulating the actual machining process. It is possible to see a backplot of where the tool will move, but it is not possible to animate the process or visualize how the physical machine will move. Nor is it possible to simulate the material removal to see how the manufactured part might differ from the model.

Robot Workbench has been part of FreeCAD for many years but has received very little development attention recently. It aims to allow the simulation of industrial robots and the trajectory planning to \'program\' them for specific tasks. Robot workbench has the ability to visualize and simulate a robot\'s movements and follow a pre-planned trajectory. Currently Robot is limited to the URDF (Universal Robot Descriptor Files) provided with the workbench. These are limited to a handful of Kuka robots.

This GSoC project idea aims to add specific functionality to take advantage of Robot\'s simulation capability to satisfy Path\'s need for simulation. It will also make it easier to design new robots and drive them with Path generated trajectories.

## Details

1.  Learn the Path workbench, meet the developers, and get familiar with the development process and conventions.
2.  Explore the robot workbench and its limitations. Research and become familiar with the URDF format. Understand what work has already been done by the community in this area
3.  Build a URDF generation tool that can allow a user to model a robot in FreeCAD and generate a URDF file.
4.  Extend the Path \'Command\' and \'Path\' objects to provide a robot trajectory interface. In other words, make it possible for Robot simulations to run from Path commands.
5.  Build User interface components to allow users to access these tools
6.  Build unit tests to exercise core functionality.
7.  Write documentation for the new features.

## Expected Outcome 

1.  Allow a user to model his CNC machine.
2.  Allow a user to click a simulate button and see the simulated machine animated to follow the Path as accurately as possible.

## Future Possibilities 

1.  Simulation could be extended to visualize material removal from a simulated stock object.

## Project Properties 

### Skills

-   Programming language Python and C++
-   Familiarity with CNC/CAM concepts
-   Familiarity with FreeCAD modeling techniqes.

### Difficulty

Medium

### Additional Information 

_ _ _

---
[documentation index](../README.md) > GSoC Path/Robot Integration
