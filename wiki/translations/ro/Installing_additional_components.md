# Installing additional components/ro
<div class="mw-translate-fuzzy">





</div>


{{TOCright}}

# Introduction


<div class="mw-translate-fuzzy">

## Selectați sistemul de operare 

FreeCAD este cu adevarat o aplicație multi-platformă, dezvoltată folosind renumitul pachet [Qt](http://en.wikipedia.org/wiki/Qt_(framework)). Asta inseamna ca FreeCAD arata si se comporta la fel in Windows, Linux si Mac. Totusi, procedura de instalare difera usor pentru fiecare sistem de operare. Selectati mai jos sistemul de operare pentru mai multe detalii despre procedura de instalare.

    
   ![ alt=\'Windows\' \| link= Install on Windows/ro](images/Windows.png )   ![ alt=\'Linux\' \| link= Install on Unix/ro](images/Linux.png )   ![ alt=\'Mac\' \| link= Install on Mac/ro](images/Mac.png )
                              [Instalare in Windows](Install_on_Windows/ro.md)                                                  [ Instalare in Linux/Unix](Install_on_Unix/ro.md)                                             [Instalare in Mac](Install_on_Mac/ro.md)
    


</div>

# Help files 

See [Installing Helpfile](Installing_Helpfile.md).

# External workbenches 


<div class="mw-translate-fuzzy">

În afara de implicitul [workbenches](workbenches.md) împreună cu FreeCAD, există o colecție tot mai mare de ateliere suplimentare de lucru și module, create de membrii comunității, fiind disponibile pe web. Mai multe eforturi sunt în curs de desfășurare pentru a le aduna și a le pune la dispoziția dvs. într-un mod convenabil. Acestea sunt enumerate mai jos.


</div>


<div class="mw-translate-fuzzy">

## Software extern susținut de FreeCAD 

FreeCAD suportă o mulțime de pachete software externe din cutie. Aceasta înseamnă că trebuie să instalați software-ul și acesta va fi disponibil automat, data viitoare când îl porniți. Nu este nevoie să-l recompilați. Această secțiune își propune să furnizeze o listă a tuturor acestor pachete software, împreună cu unele informații despre locul în care este folosit în FreeCAD și unde le puteți lua.


</div>

FreeCAD supports several third party software packages out of the box. In many cases all you need to do is install the software, and when FreeCAD is restarted it will automatically find and be able to use it. This section aims to provide a list of such software packages, together with some information about where they are used in FreeCAD and where they can be downloaded.

## Support


<div class="mw-translate-fuzzy">

### GitPython

O bibliotecă python care este utilizată pentru a interacționa cu depozitele Git. Această funcție este în prezent în stare de dezvoltare în FreeCAD. Managerul [Addon Manager](Std_AddonMgr.md) poate folosi această bibliotecă pentru a importa add-on-uri dintr-un depozit Git. Proiectul este găzduit pe GitHub la adresa <https://github.com/gitpython-developers/GitPython>.


</div>

[GitPython](https://github.com/gitpython-developers/GitPython) is a library to interact with Git repositories. The [Addon Manager](Std_AddonMgr.md) can use this library. GitPython is included in the FreeCAD installers for Windows and Mac.


<div class="mw-translate-fuzzy">

### GraphViz

GraphViz este un software de vizualizare grafic open source. În FreeCAD este folosit pentru a genera grafice de dependență prin {{MenuCommand | Tools-> Dependency Graph ...}} Pagina principală este la <https://www.graphviz.org>


</div>

[GraphViz](https://www.graphviz.org) is an open source graph visualization software. It is used by the [Std DependencyGraph](Std_DependencyGraph.md) tool.


<div class="mw-translate-fuzzy">

### OpenCAMLib

Aceasta este o bibliotecă open source cu scopul de a oferi algoritmi de producție asistată de calculator (CAM). Este folosit în FreeCAD în [ workbench path](Path_Workbench.md). Pagina de pornire este la <http://www.anderswallin.net/CAM/>.


</div>

[OpenCAMLib](http://www.anderswallin.net/CAM) is an open source library of computer aided manufacturing (CAM) algorithms. It is used in the [Path Workbench](Path_Workbench.md). See the [OpenCamLib](OpenCamLib.md) page for installation instructions.


<div class="mw-translate-fuzzy">

### OpenSCAD

Programatorul Solid 3D CAD Modeller este un alt software CAD, bazat pe Geometrie Solidă Constructivă (CSG). Aceasta înseamnă că nu poate manipula ochiurile, dar acționează exclusiv pe o geometrie solidă. FreeCAD poate importa și exporta fișiere create de OpenSCAD prin meniurile {{MenuCommand | File-> Import}} și {{MenuCommand | File-> Export}} prin selectarea formatului {{MenuCommand | OpenSCAD CSG}} sau {{ MenuCommand \| format OpenSCAD}} tipuri de fișiere. Puteți obține OpenSCAD de la <https://www.openscad.org>.


</div>

[OpenSCAD](https://www.openscad.org) is a solid 3D modeller. The [OpenSCAD Workbench](OpenSCAD_Workbench.md) depends on this software and the [Mesh Workbench](Mesh_Workbench.md) uses it for its Boolean tools. It is also required for the import of SCAD files with the [Std Import](Std_Import.md) tool.

## File formats 

All software in this section will be used by the [Std Import](Std_Import.md) or [Std Export](Std_Export.md) tools.


<div class="mw-translate-fuzzy">

### CAD Exchanger 

O aplicație de tip proprietate, cu sursă închisă, pentru schimbarea diferitelor formate de fișiere folosite în CAD. Puteți să-l utilizați pentru a converti proprietăți, formate proprietar într-un format accesibil prin FreeCAD. Pagina de pornire se află la adresa <https://cadexchanger.com/> unde puteți descărca o versiune de evaluare sau puteți achiziționa o licență pentru aplicație.


</div>

[CADExchanger](https://cadexchanger.com) is a commercial application for exchanging various CAD file formats. There is an [external workbench](https://github.com/yorikvanhavre/CADExchanger) to use this application in FreeCAD.


<div class="mw-translate-fuzzy">

### Importator DXF 

FreeCAD are un importator și exportator nativ pentru fișierele DXF, programate în C ++. În prezent, acest importator nu implementează toate caracteristicile formatul DXF. Dacă vă bazați pe o caracteristică care nu este încă implementată, activați opțiunea {{MenuCommand | Edit-> Preferences-> Import-Export}} utilizând importatorul / exportatorul bazat pe python mai vechi. Apoi, puteți alege să lăsați FreeCAD să descarce automat fișierele necesare sau să le apucați de la <https://github.com/yorikvanhavre/Draft-dxf-importer>. Importatorul / exportatorul ales este folosit prin selectarea {{MenuCommand | File-> Import}} sau {{MenuCommand | File-> Export}} si alegerea formatului fisierului {{MenuCommand | AutoDesk DXF 2D}}.


</div>

FreeCAD has a native importer and exporter for DXF files, programmed in C++. Currently they do not implement all features of the DXF format. For those features the legacy Python importer and exporter are still available. These require the [Draft-dxf-importer](https://github.com/yorikvanhavre/Draft-dxf-importer) Python library. See the [FreeCAD and DXF Import](FreeCAD_and_DXF_Import.md) page for more information.

### DWG converters 

FreeCAD cannot directly read and write DWG files. To convert DXF files to DWG files, and vice-versa, FreeCAD relies on external converters. There is built-in support for the following DWG converters:

-   [LibreDWG](https://www.gnu.org/software/libredwg) (open-source, lacks support for some DWG entities).
-   [ODA File Converter](https://www.opendesign.com/guestfiles/oda_file_converter) (free, but not open-source).
-   [QCAD pro](https://qcad.org/en/qcad-command-line-tools#dwg2dwg) (commercial). <small>(v0.20)</small> 

See [Import Export Preferences](Import_Export_Preferences#DWG.md) and [FreeCAD and DWG Import](FreeCAD_and_DWG_Import.md) for more information.


<div class="mw-translate-fuzzy">

### ifcOpenShell

IfcOpenShell este o bibliotecă pentru a lucra cu formatul de fișiere Foundation Industry Classes (IFC) folosit în designul arhitectural. Acesta poate fi accesat din [arhivă de lucru](Arch_Workbench.md) prin {{MenuCommand | Arch-> Utilities-> Ifc Explorer}}. Pagina de pornire este la <http://ifcopenshell.org>


</div>

[IfcOpenShell](http://ifcopenshell.org) is a library for working with the Industry Foundation Classes (IFC) file format used in architectural design. The library is also used by the [Arch IfcExplorer](Arch_IfcExplorer.md) ({{VersionMinus|0.18}}) and [BIM IfcExplorer](BIM_IfcExplorer.md) tools. IfcOpenShell is included in the FreeCAD installers for Windows and Mac.

### IfcJson

[IfcJson](https://github.com/buildingSMART/ifcJSON) is a library required for exporting to the IFCJSON file format. IFCJSON is a new IFC format that is not yet supported by many applications.


<div class="mw-translate-fuzzy">

### pycollada

Pycollada aka python-collada este o bibliotecă python pentru citirea și scrierea documentelor COLLADA, un standard pentru schimbul de scene și elemente 3D. Dacă este instalat, puteți importa și exporta scenele din și din fișierele COLLADA prin comenzile {{MenuCommand | File-> Import}} și {{MenuCommand | File-> Export}} prin selectarea tipului de fișier COLLADA. Proiectul este găzduit de GitHub la adresa <https://pycollada.github.io/> și puteți descărca versiunile la <https://github.com/pycollada/pycollada/releases/>


</div>

[Pycollada](https://github.com/pycollada/pycollada/releases), also known as python-collada, is a Python library to read and write Collada (DAE) files. Pycollada is included in the FreeCAD installers for Windows and Mac.

## Rendering

### LuxCoreRender

[LuxCoreRender](https://www.luxcorerender.org) is a render engine, reboot of the [LuxRender](LuxRender.md) project. Officially it is not supported by the [Raytracing Workbench](Raytracing_Workbench.md), but it might be worth to give it a try. It is officially supported by the new [Render Workbench](https://github.com/FreeCAD/FreeCAD-render), intended as a future replacement of the Raytracing Workbench. See the [LuxCoreRender](LuxCoreRender.md) page for more information and installation instructions.

### LuxRender

[LuxRender](https://luxcorerender.org/history/) is one of the two render engines supported by the [Raytracing Workbench](Raytracing_Workbench.md). In 2013 the project has been rebooted becoming [LuxCoreRender](LuxCoreRender.md), with a major code rewriting and compatibility breaking changes. Officially the Raytracing Workbench only supports the abandoned [LuxRender](LuxRender.md) (latest version is 1.6, 2017-12-28), while the new [Render Workbench](https://github.com/FreeCAD/FreeCAD-render) (intended as a future replacement of the Raytracing Workbench) supports instead LuxCoreRender and has dropped the support for LuxRender. Anyway, even if officially not supported, [LuxCoreRender](LuxCoreRender.md) may work with the Raytracing Workbench, it might be worth to give it a try. See the [LuxRender](LuxRender.md) page for more information and installation instructions, and the [LuxCoreRender](LuxCoreRender.md) if you want to try a more modern software.


<div class="mw-translate-fuzzy">

### POVRay

POVRay este un cunoscut raytracer care poate face imagini fotorealiste. Acesta este unul dintre cei doi raytraceri susținut în prezent de FreeCAD în Atelierul de lucru raytracing. Utilizarea acestuia este descrisă în pagina [ raytracing workbench](Raytracing_Workbench.md). Puteți descărca POVRay de la <https://www.povray.org>.


</div>

[POV-Ray](https://www.povray.org) is a well-known ray-tracer which can render photo-realistic images. It is one of two render engines currently supported by the [Raytracing Workbench](Raytracing_Workbench.md). See the [POV-Ray](POV-Ray.md) page for more information and installation instructions.

## Finite element 


<div class="mw-translate-fuzzy">

### CalculiX

CalculiX este o suită de două pachete de elemente finite. One, CalculiX GraphiX sau calculix-cgx, este un interfață GUI pentru a afișa rezultatele celui de-al doilea pachet, CalculiX CrunchiX, sau calculix-ccx, un solver FEM. Numai acesta din urmă este susținut de FreeCAD. Acesta poate fi accesat din [FEM Workbench](FEM_Workbench.md) prin **Solve-> Solver CalculiX**. Există un solver standard și experimental susținut de FreeCAD. CalculiX poate fi descărcat de la <http://calculix.de>


</div>

[CalculiX](http://calculix.de) is a suite of two finite element packages: CalculiX CrunchiX, a FEM solver, and CalculiX GraphiX, a GUI frontend. Only the solver is supported by FreeCAD. It is used by the [Solver CalculiX](FEM_SolverCalculiX.md) tool.


<div class="mw-translate-fuzzy">

### Gmsh

Un generator automat 3D de elemente finite. Acesta poate fi folosit în FreeCAD din [FEM Workbench](FEM_Workbench.md) prin **Mesh-> FEM mesh form from gmsh**. Pagina de pornire a gmsh este la <http://www.geuz.org/gmsh>


</div>

[Gmsh](http://gmsh.info) is an automatic finite element mesh generator. it is used by the [FEM MeshGmshFromShape](FEM_MeshGmshFromShape.md) and [Mesh FromPartShape](Mesh_FromPartShape.md) tools.


<div class="mw-translate-fuzzy">

### Elmer

Elmer este un software de simulare multifizic, care a fost deschis din 2005. În FreeCAD, modulele Grid și Solver pot fi utilizate de către [FEM Workbench](FEM_Workbench.md) prin **Solve->Solver Elmer**. Pagina de start a proiectelor este la <https://www.elmerfem.org> și poate fi descărcată de la GitHub la <https://github.com/ElmerCSC/elmerfem/releases>.


</div>

[Elmer](https://www.csc.fi/web/elmer) is a multi-physics simulation software, which was open sourced in 2005. In FreeCAD its Grid and Solver modules are used by the [FEM SolverElmer](FEM_SolverElmer.md) tool.


<div class="mw-translate-fuzzy">

### FEniCS

FEniCS este o platformă de calcul pentru rezolvarea ecuațiilor diferențiale cu derivate parțiale (PDE), care sunt utilizate pe scară largă în rezolvarea problemelor FEM. Ca atare, acesta poate fi utilizat de [FEM Workbench](FEM_Workbench.md). FreeCAD poate importa și exporta rețelele FEniCS prin **File-> Import** și {{MenuCommand | File-> Export}} selectând formatul de fișier **FEM mesh fenics**. Pagina de pornire a FEniCS este la <https://fenicsproject.org>.


</div>

[FEniCS](https://fenicsproject.org) is a computing platform to solve partial differential equations (PDEs), which are widely used when solving FEM problems. It is used by the [FEM workbench](FEM_Workbench.md)


<div class="mw-translate-fuzzy">

### Z88

Z88 este un alt program FEM, care conține un mesher, solver și convertoare, care poate fi folosit de [FEM Workbench](FEM_Workbench.md) al FreeCAD. Acesta poate fi accesat prin **Solve-Solver Z88**. Z88 distribuie mai multe pachete, toate disponibile în mod liber, dar sunt surse închise. Cu toate acestea, Z88OS, publicat sub licență open source, este ceea ce este necesară în FreeCAD. Pagina principală este la <https://en.z88.de/>. Z88OS este, de asemenea, găzduit pe GitHub la <https://github.com/LSCAD/Z88OS> dacă doriți să îl compilați singur.


</div>

[Z88](https://en.z88.de) is another FEM program, containing a mesher, a solver and converters. It is used by the [FEM SolverZ88](FEM_SolverZ88.md) tool. FreeCAD requires the open source Z88OS package.


<div class="mw-translate-fuzzy">

O bibliotecă pentru exploatarea și manipularea câmpului (FOAM), care este necesară simulărilor de computational Fluid Dynamics (CFD). Ca atare, OpenFOAM este necesar de către [FEM Workbench](FEM_Workbench.md) al FreeCAD. Puteți accesa acest lucru prin intermediul submeniului **Model-> Fluid constraints**. Proiectul se află la <https://openfoam.org>.


</div>

[OpenFOAM](https://openfoam.org) is a large collection of libraries for computational fluid dynamics (CFD) simulations. OpenFOAM is used by the [Cfd](Cfd_Workbench.md) and [CfdOF](https://github.com/jaheyns/CfdOF) [external workbenches](external_workbenches.md).

# Related pages 

-   [Import Export](Import_Export.md)
-   [Import Export Preferences](Import_Export_Preferences.md)
-   [Third Party Libraries](Third_Party_Libraries.md)


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > Installing additional components/ro
