# Google Summer of Code 2017
This is the **2017** GSoC page.

**The 2018 Google Summer of Code page is located [here](Google_Summer_of_Code_2018.md).**

FreeCAD started participating to the Googles student coding program ([GSoC](https://summerofcode.withgoogle.com/)) in 2016. As we are only a small team we got involved in a [combined effort](http://brlcad.org/w/index.php?title=Google_Summer_of_Code/Project_Ideas#FreeCAD_Projects) of many CAx organisations. Due to the [combined application](http://brlcad.org/w/index.php?title=Google_Summer_of_Code/Project_Ideas#FreeCAD_Projects) at GSoC many links will lead from here to the [BRLcad wiki](http://brlcad.org/wiki/Google_Summer_of_Code), which is used as single place for everything.

## How it works 

-   The student writes a project proposal for FreeCAD.
    -   Sometimes their project idea caters to something that the open source organization suggests and sometimes it\'s an idea entirely of the student\'s conception.
-   Proposals are reviewed, evaluated, and ranked by the open source organization\'s mentors.
-   Google allocates a certain number of slots to each participating organization
    -   That, in turn, determines how many student developers work with that organization.

If you want to get involved have a look at the [getting started checklist](http://brlcad.org/wiki/Summer_of_Code/Checklist). Whether you\'re applying or accepted, we\'ve itemized everything you need to do in this list. We\'re here to help you become new open source developers, so don\'t be shy if you have any questions.

### The Selection Process 

GSoC is about getting people involved and contributing to open source over the long-term. As such, we heavily weight our application selection process towards students that are interested in remaining involved in FreeCAD and open source software development long after GSoC has ended. GSoC is not a job. If you think this is just a summer job, then GSoC is probably not for you. It\'s only like a job in terms of planning your time commitment over the summer.

Additionally, submissions are graded based on perception of the submitter\'s abilities to complete the task within the program timeframe, general consensus on the technical approach being proposed, and overall interest in having such modifications made to FreeCAD. Particular notice is made of students that are responsive to questions and readily interactive in the IRC channel or on the forum. Communication is a great thing.

Just about every GSoC organization receives considerably more project proposals than can be accepted. Every application gets read multiple times and reviewed in detail. Of those applications, only a small subset are selected so keep in mind that the selection process is rather competitive and difficult.

Whether or not you are accepted, contributing to open source outside of GSoC is one of the main goals of the program and is the best way to be noticed and get your proposal accepted. Keep that in mind. Thanks for your interest and we look forward to working with new FreeCAD developers!

### Available Slots 

As FreeCAD is new in GSoC our slots will be limited to a maximum of two. Hence it will be hard for gathering one of those slots with your application. Try to increase your chance by getting to know us early and start fixing bugs before GSoC starts, this always helps to build trust and will convince us of your dedication.

## Possible Mentors 

[Ickby](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=686), [Bernd](https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=2069), [Yorik](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=68) : You can reach us all in the forum and in the IRC channel.

## Implementation Ideas 

The ideas listed here have a high chance of being accepted as project proposal. Note that for students already longer involved in FreeCAD, and which already contributed code, own ideas in their line of work are also welcome. Feel free to contact us on IRC, the forum or the mailing list for further discussions about the listed projects. The topics priority shows you how important the work on the ideas is for the mentors, and hence choosing a high priority topic will give you an advantage if there are more applications than slots for FreeCAD.

++++++
| Topic                                                                                                                                                                                                                                                                                                             | Language                | Difficulty  | Priority | Contact                                                                                                                                                    |
+===================================================================================================================================================================================================================================================================================================================+=========================+=============+==========+============================================================================================================================================================+
| [Advanced FreeCAD test system](Advanced_FreeCAD_test_system.md): Create a framework for result file based comparisons and workbench specific comparators. Also creation of test cases should be simplified by a GUI or wizard.                                                                            | Python/C++              | Medium      | Low      | [Ickby](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=686)                                                                                 |
++++++
| [Topological Naming Project](Topological_Naming_Project.md): Implementation of subshape identifiers based on creation history and update of topology class to work with those identifiers                                                                                                                 | C++                     | Hard        | High     | [Ickby](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=686)                                                                                 |
++++++
| [Direct modeling tools](Direct_modeling_tools.md): Create a new layer of tools and objects, that work on top of existing Part-based 3D objects, that allow a user to graphically modify their geometry.                                                                                                   | Python/C++              | Medium      | Low      | [Yorik](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=68)                                                                                  |
++++++
| [FEM Post Processing based on VTK](FEM_Post_Processing_based_on_VTK.md): Base the existing FEM VTK post processing on the updated SMESH data structure and design a python interface for it. Also improve integration into the workbench.                                                                 | C++                     | Medium      | Medium   | [Ickby](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=686)                                                                                 |
++++++
| [IPython notebook integration](IPython_notebook_integration.md): Create a way to export the open inventor scenegraph as a JavaScript file and add functions for seamless interaction with the IPython display system                                                                                      | C++, JavaScript, Python | Easy        | Low      | [Ickby](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=686)                                                                                 |
++++++
| [Integrate Cycles renderer](Integrate_Cycles_renderer.md): Add Blender\'s new Cycles renderer as a new render engine to the Raytracing Workbench                                                                                                                                                          | C++                     | Medium      | Low      | [Yorik](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=68)                                                                                  |
++++++
| Stepwise integration of ElmerFem into FreeCAD should be done in three phases: Phase 1 - [New solver object for handling ElmerFEM execution in FEM-workbench](New_solver_object_for_handling_ElmerFEM_execution_in_FEM-workbench.md)                                                                       | Python, C++             | Medium-Hard | High     | [Bernd](https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=2069), [HoWil](https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=6222) |
| Phase 2 - [Mapping of main ElmerSolver setting for mechanical simulations](Mapping_of_main_ElmerSolver_setting_for_mechanical_simulations.md)                                                                                                                                                             |                         |             |          |                                                                                                                                                            |
| Phase 3 - [Give graphical access to a wide range of available ElmerSolver setting from within FreeCAD](Give_graphical_access_to_a_wide_range_of_available_ElmerSolver_setting_from_within_FreeCAD.md)                                                                                                     |                         |             |          |                                                                                                                                                            |
++++++
| [PartDesign Updates](PartDesign_Updates.md): Finish PartDesign port to new Body object, simplify the workflows and extend tools while making them more robust.                                                                                                                                            | C++, Python             | Medium      | High     | [Ickby](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=686)                                                                                 |
++++++
| [GSoC FEM Solver Z88](GSoC_FEM_Solver_Z88.md): Extend the capabilities of FEM solver Z88OS in FreeCAD FEM workbench.                                                                                                                                                                                      | Python                  | Easy-Medium | Low      | [Bernd](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=686)                                                                                 |
++++++
| [GSoC FEM Unit Tests](GSoC_FEM_Unit_Tests.md): Extend the unit tests of FreeCAD FEM workbench.                                                                                                                                                                                                            | Python                  | Easy-Medium | Low      | [Bernd](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=686)                                                                                 |
++++++
| [GSoC Path/Robot Integration](GSoC_Path/Robot_Integration.md): Path is the CNC/CAM workbench. It currently lacks any simulation capability. Robot workbench is a tool for simulating industrial robots. Extend Path and Robot workbenches to support simulation of CNC operations in the Robot workbench. | C++, Python             | Easy-Medium | Medium   | [Yorik](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=68), [sliptonic](https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=708) |
++++++



---
⏵ [documentation index](../README.md) > Google Summer of Code 2017
