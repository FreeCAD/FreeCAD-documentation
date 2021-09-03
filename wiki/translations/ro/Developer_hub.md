

![150](images/Crystal_Clear_app_tutorials.png )

Acesta este locul unde veți veni dacă doriți să contribuiți la dezvoltarea software-ului FreeCAD.

Aceste pagini sunt în stadiu incipient de dezvoltare. Dacă nu găsiți informațiile pe care le căutați, sau aveți invormații utile undeva unde nu am făcut link-ul, atunci vă rog lăsați un comentariu pe [forum](http://forum.freecadweb.org/index.php?sid=5f84150e79db8842e277b042077097ff) și cineva se va uita acole la el (sau, dacă te simți îndrăzneț, de ce să nu editezi direct această pagină!).

## Developer Documentation {#developer_documentation}


<div class="mw-translate-fuzzy">

## Documentație Dezvoltatori {#documentație_dezvoltatori}

Documentația dezvoltatorului a inclus următoarele secțiuni:


</div>

### Compiling FreeCAD {#compiling_freecad}


<div class="mw-translate-fuzzy">

### Fă-o singur: Compilare FreeCAD {#fă_o_singur_compilare_freecad}

-   [Source code management](Source_code_management.md)
-   [Find assistance](Tracker.md) când aveți o problemă sau credeți că poate ați găsit un bug
-   [Compiling on Windows](CompileOnWindows.md)
-   [Compiling on Unix](CompileOnUnix.md)
-   [Compiling on Mac OS X](CompileOnMac.md)
-   [Licence details](Licence.md) despre licența FreeCAD
-   [Third Party Libraries](Third_Party_Libraries.md)
-   [Third Party Tools](Third_Party_Tools.md)
-   [Start up and Configuration](Start_up_and_Configuration.md)
-   [Source documentation](Source_documentation.md)


</div>

### Packaging

[Packaging](Packaging.md) consists in taking the compiled binaries and Python source files of FreeCAD, and distributing them for use in a particular system.

-   [Linux packaging](Linux_packaging.md)
    -   [Debian development](Debian_development.md)
    -   [Debian Unstable](Debian_Unstable.md)
    -   [Git buildpackage](Git_buildpackage.md)
-   [Windows packaging](Windows_packaging.md)
-   [MacOS packaging](MacOS_packaging.md)

### Build Support Tools {#build_support_tools}


<div class="mw-translate-fuzzy">

### Construiți instrumente de sprijin {#construiți_instrumente_de_sprijin}

-   The [FreeCAD Build Tool](FreeCAD_Build_Tool.md)
    -   [Adding an application module](Module_Creation.md) to FreeCAD
-   [Debugging](Debugging.md) FreeCAD
-   [Testing](Testing.md) FreeCAD
-   [Compiling (Speeding up)](Compiling_(Speeding_up).md) FreeCAD
-   [Continuous Integration](Continuous_Integration.md)


</div>

### Modifying FreeCAD {#modifying_freecad}


<div class="mw-translate-fuzzy">

### Modificarea FreeCAD {#modificarea_freecad}

-   Înțelegerea codului sursă [The FreeCAD source code](The_FreeCAD_source_code.md)
-   Adaugă caracteristici GUI [Features](Gui_Command.md) la FreeCAD sau Ateliere
-   [Branding](Branding.md) sau \'\'cum să-i dați un aspect unic la FreeCAD \'\'
-   [Artwork](Artwork.md) ce am făcut pentru FreeCAD ca să-l puteți reutiliza în mod liber
-   [Artwork\_Guidelines](Artwork_Guidelines.md) standarde pentru iconițe
-   [Translating FreeCAD](Localisation.md)
-   [Extra python modules](Extra_python_modules.md), sau *cum să extindeți funcționalitatea Python în interiorul FreeCAD*
-   [Google Summer of Code](Google_Summer_of_Code.md) implicați-vă prin intermediul programului Google de asistență pentru studenți


</div>

-   [Translating an external workbench](Translating_an_external_workbench.md)

### Module developer\'s guide {#module_developers_guide}


<div class="mw-translate-fuzzy">

### Ghidul deszvoltatorului de Module {#ghidul_deszvoltatorului_de_module}

[FreeCAD Mod Dev Guide](https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide): Aceasta este o carte electronică scrisă pe github. \"Este un proiect colaborativ și sunteți binevenit să adăugați îmbunătățiri\" Vă rugăm să ne trimiteți cererea dvs. de a vă aduce contribuția.


</div>

Capitole:

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

Cel mai recent preview pdf poate fi descărcat din depozitul: git[pdf folder](https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide/tree/master/pdf)

### Internals


<div class="mw-translate-fuzzy">

### Documentație OpenCascade {#documentație_opencascade}

-   [Roman Lygin\'s tutorials](http://opencascade.wikidot.com/romansarticles)
-   [Full Online Documentation](https://dev.opencascade.org/doc/overview/html/index.html)
-   [Reference Manual](https://dev.opencascade.org/doc/refman/html/index.html)
-   [The openCascade wiki](http://opencascade.wikidot.com)


</div>

OpenCascade is a software development platform for 3D surface and solid modeling, CAD data exchange, and visualization, mostly in the form of C++ libraries.

-   [Roman Lygin\'s tutorials](http://opencascade.wikidot.com/romansarticles)
-   [Full Online Documentation](https://dev.opencascade.org/cdoc/overview/html/index.html)
-   [Reference Manual](https://dev.opencascade.org/doc/refman/html/index.html)
-   [The openCascade wiki](http://opencascade.wikidot.com) (currently containing ?? Chinese spam)

#### File format {#file_format}

[File Format FCStd](File_Format_FCStd.md). The files created with FreeCAD are `.zip` files that include the [BREP](https://en.wikipedia.org/wiki/Boundary_representation) geometry, as well as XML data that describes the document.

#### Sketcher solver {#sketcher_solver}

-   [Sketcher Solver Architecture Booklet](https://forum.freecadweb.org/viewtopic.php?f=10&t=36355) (forum thread), [source](https://github.com/abdullahtahiriyo/FreeCADBooks/tree/master/FreeCAD_Solver_Architecture) in GitHub.
-   [PlaneGCS solver](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Sketcher/App/planegcs/) in the FreeCAD source code; important files are [GCS.cpp](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Sketcher/App/planegcs/GCS.cpp) and [SubSystem.cpp](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Sketcher/App/planegcs/SubSystem.cpp).
-   [Recent Several Sketcher improvements](https://forum.freecadweb.org/viewtopic.php?f=9&t=29192).

The sketcher solver isn\'t perfect, as there are some issues with numerical precision when using large values, see [Adventure of fixing sketcher solver for large sketches](https://forum.freecadweb.org/viewtopic.php?f=10&t=40502).

The development of a new solver architecture could improve the way the solver is used both in the [Sketcher Workbench](Sketcher_Workbench.md), and for assembly of 3D bodies. See [Reimplementing constraint solver](https://forum.freecadweb.org/viewtopic.php?f=20&t=40525).

## Roadmap


<div class="mw-translate-fuzzy">

## Foaie de parcurs {#foaie_de_parcurs}

FreeCAD, deși utilizabilă în anumite domenii, este la începutul unei lungi drumuri în marele curent CAD. Mai sunt încă multe de făcut pentru a ajunge la o stare în care putem concura cu software comercial.


</div>

[0.20 Development Cycle](0.20_Development_Cycle.md)

## Community

-   [IRC channel](irc://chat.freenode.net/freecad) ,synchronized with [gitter channel](https://gitter.im/FreeCAD/FreeCAD)
-   [Development forum](https://forum.freecadweb.org/viewforum.php?f=6)


<div class="mw-translate-fuzzy">

-   [Development roadmap](Development_roadmap.md)


</div>


<div class="mw-translate-fuzzy">

## Credits

[Contributors](Contributors.md)


</div>




[Category:Hubs{{\#translation:}}](Category:Hubs.md) [Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md)
