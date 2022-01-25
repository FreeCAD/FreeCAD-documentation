# <img alt="" src=images/Crystal_Clear_app_tutorials.png  style="width:64px;"> Developer hub/pl





This is the place to come if you want to contribute to the development of the FreeCAD software.

These pages are in the early stage of development. If you can\'t find the information you are looking for, or have found useful information somewhere we have not linked to, then please leave a comment on the [forum](http://forum.freecadweb.org/index.php?sid=5f84150e79db8842e277b042077097ff) and someone will look into it (or, if you are feeling bold, why not edit this page directly!).

## Developer Documentation 

The developer documentation comprises the following sections:

### Compiling FreeCAD 

-   [Github repo](https://github.com/FreeCAD/FreeCAD). If you are new to git, read [Source code management](Source_code_management.md)
-   [Compile with Docker](Compile_on_Docker.md)
-   [Compiling on Windows](Compile_on_Windows.md)
-   [Compiling on Linux](Compile_on_Linux.md)
-   [Compiling on MacOS](Compile_on_MacOS.md)
-   [Licence details](Licence.md) about the FreeCAD licences
-   [Third Party Libraries](Third_Party_Libraries.md)
-   [Third Party Tools](Third_Party_Tools.md)
-   [Start up and Configuration](Start_up_and_Configuration.md)
-   [Source documentation](Source_documentation.md)
-   Use the [bug tracker](Tracker.md) when you have a problem or think you may have found a bug

### Packaging

[Packaging](Packaging.md) consists in taking the compiled binaries and Python source files of FreeCAD, and distributing them for use in a particular system.

-   [Linux packaging](Linux_packaging.md)
    -   [Debian development](Debian_development.md)
    -   [Debian Unstable](Debian_Unstable.md)
    -   [Git buildpackage](Git_buildpackage.md)
-   [Windows packaging](Windows_packaging.md)
-   [MacOS packaging](MacOS_packaging.md)

### Build Support Tools 

-   The [FreeCAD Build Tool](FreeCAD_Build_Tool.md)
    -   [Adding an application module](Workbench_creation.md) to FreeCAD
-   [Debugging](Debugging.md) FreeCAD
-   [Testing](Testing.md) FreeCAD
-   [Compiling (Speeding up)](Compiling_(Speeding_up).md) FreeCAD
-   [Continuous Integration](Continuous_Integration.md)

### Modifying FreeCAD 

-   Understanding [The FreeCAD source code](The_FreeCAD_source_code.md)
-   [Submitting patches](Tracker#Submitting_patches.md)
-   Add [Features](Gui_Command.md) to FreeCAD or a Workbench
-   [Branding](Branding.md) or *how to give FreeCAD a unique look*
-   [Artwork](Artwork.md) we made for FreeCAD, that you can freely reuse
-   [Artwork guidelines](Artwork_Guidelines.md) standards for icons
-   [Translating FreeCAD](Localisation.md)
-   [Extra python modules](Extra_python_modules.md), or *how to extend python functionality within FreeCAD*
-   [Google Summer of Code](Google_Summer_of_Code.md) get involved via Google\'s student support program
-   [Fine-tuning](Fine-tuning.md) shows different options and parameter switches that can overcome problems
-   [Wrapping a C++ class in Python](Wrapping_a_Cplusplus_class_in_Python.md) shows how to create the Python wrapper for a C++ class

-   [Translating an external workbench](Translating_an_external_workbench.md)

### Module developer\'s guide 

[FreeCAD Mod Dev Guide](https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide): This is an ebook under writing on github, please fork and send pull request to contribute.

Chapters:

-   Overview and Software Architecture
-   Source code structure
-   Base and App module
-   Gui module
-   Python wrapping
-   Modular design
-   Fem module source analysis (mixed C++ and Python)
-   Development of CFD Module (pure Python)
-   Module testing and debugging
-   Contribute code with git

Latest pdf preview can be downoaded from [pdf folder](https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide/tree/master/pdf) of this git repo

### Internals

#### OpenCascade Documentation 

OpenCascade is a software development platform for 3D surface and solid modeling, CAD data exchange, and visualization, mostly in the form of C++ libraries.

-   [Roman Lygin\'s tutorials](http://opencascade.wikidot.com/romansarticles)
-   [Full Online Documentation](https://dev.opencascade.org/cdoc/overview/html/index.html)
-   [Reference Manual](https://dev.opencascade.org/doc/refman/html/index.html)
-   [The openCascade wiki](http://opencascade.wikidot.com) (currently containing ?? Chinese spam)

#### File format 

[File Format FCStd](File_Format_FCStd.md). The files created with FreeCAD are `.zip` files that include the [BREP](https://en.wikipedia.org/wiki/Boundary_representation) geometry, as well as XML data that describes the document.

#### Sketcher solver 

-   [Sketcher Solver Architecture Booklet](https://forum.freecadweb.org/viewtopic.php?f=10&t=36355) (forum thread), [source](https://github.com/abdullahtahiriyo/FreeCADBooks/tree/master/FreeCAD_Solver_Architecture) in GitHub.
-   [PlaneGCS solver](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Sketcher/App/planegcs/) in the FreeCAD source code; important files are [GCS.cpp](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Sketcher/App/planegcs/GCS.cpp) and [SubSystem.cpp](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Sketcher/App/planegcs/SubSystem.cpp).
-   [Recent Several Sketcher improvements](https://forum.freecadweb.org/viewtopic.php?f=9&t=29192).

The sketcher solver isn\'t perfect, as there are some issues with numerical precision when using large values, see [Adventure of fixing sketcher solver for large sketches](https://forum.freecadweb.org/viewtopic.php?f=10&t=40502).

The development of a new solver architecture could improve the way the solver is used both in the [Sketcher Workbench](Sketcher_Workbench.md), and for assembly of 3D bodies. See [Reimplementing constraint solver](https://forum.freecadweb.org/viewtopic.php?f=20&t=40525).

## Roadmap

FreeCAD, though usable in certain areas, is at the beginning of a long way into the CAD mainstream. There is still a lot to do to reach a state where we can compete with commercial software.

[0.20 Development Cycle](0.20_Development_Cycle.md)

## Community

-   [IRC channel](irc://chat.freenode.net/freecad) ,synchronized with [gitter channel](https://gitter.im/FreeCAD/FreeCAD)
-   [Development forum](https://forum.freecadweb.org/viewforum.php?f=6)

-   [Development roadmap](Development_roadmap.md)

## Credits

[Contributors](Contributors.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Hubs](Category_Hubs.md) > [Developer Documentation](Category_Developer Documentation.md) > Developer hub/pl
