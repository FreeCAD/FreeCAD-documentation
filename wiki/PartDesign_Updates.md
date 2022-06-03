# PartDesign Updates
This page is dedicated to the Google Summer of Code project regarding the updates on the PartDesign workbench.

## Outline

FreeCAD as a modeling tool should have a focus on a streamlined and efficient workflow for part creation. For this reason, the PartDesign workbench was introduced which simplified many common tasks in the modeling process. Recently this workbench has seen substantial changes to further enhance the workflow and user friendlieness. However, due to the large changes, there are many open areas that need to be worked on. This GSoC project is focused on finishing the changes, updating the tools and further improvind the workflow. It will have high user impact as PartDesign is one of the most commonly used workbenches in FreeCAD.

## Details

1.  Port tools to the new body object, including full support for the origin planes/axes. This also includes updates to the GUI which need for example handle links dependend on the CoordinateSystem they are pointing to.
2.  Create UnitTests for the new tools functionality and fix bugs detected with the tests
    1.  The tests can be designed to reproduce already reported bugs and then be used as a way to debug and verify the solution.
    2.  All newly introduced or updated functionality should be tested with a unit test
3.  Enhance the tools functionality and improve the workflow.
    1.  Enhancement   * For example the new Pipe tool needs more features and robustness, Pad/Pocket can be enhanced with more functionality, etc. It is part of the students task to identify areas for improvement and introduce the code
    2.  Workflow updates   * The Attachment editor currently works well but has UI / workflow issues. The student can propose a new way of handling attachments in the GUI and introduce the code.
    3.  New tools   * There are a few tools missing that may be handy for the workflow, for example a splitting tool (Split faces by sketch). The studend can propose tools and introduce code.

## Expected Outcome 

1.  A more robust and streamlined PartDesign workbench
2.  Multiple unit tests ensuring the workbenchs functionality
3.  A more user friendly and efficient workflow

## Future Possibilities 

As this work touches the core of the FreeCAD code you will get a deep and full understanding of FreeCADs structure. With this you are equipped to work on any area you like. There are noumerus tools PartDesign can be further extended with after GSoC, which would also be worth annother project for the upcoming years.

## Project Properties 

### Skills

-   Programming language mainly C++, unit tests in python
-   Understand of APIs from FreeCAD and the OCC library required.
-   Experiance in using CAD software and knowing the benefits and problems of different mdoeling techniques is benefitial

### Difficulty

Medium

### Additional Information 

[Category   *Google Summer of Code](Category_Google_Summer_of_Code.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Updates
