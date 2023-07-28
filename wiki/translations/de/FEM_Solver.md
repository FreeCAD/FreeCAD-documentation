# FEM Solver/de
{{TOCright}}



## Vorwort

Diese Seite sammelt Informationen über die vom Arbeitsbereich [FEM](FEM_Workbench/de.md) verwendeten Finite-Elemente-Löser. Die Schnittstelle zwischen einem Löser und FreeCAD sowohl in der Vor- als auch in der Nachbearbeitung erfolgt über Textdateien. Das bedeutet, dass theoretisch jeder Löser, der über Textdateien konfiguriert und gesteuert werden kann, mit FreeCAD zusammenarbeiten kann; für diese Kommunikation muss ein geeigneter Parser und Schreiber von Ein- und Ausgabedateien programmiert werden. Im Forum findet sich ein Thema mit Diskussionen und Ankündigungen zu den verschiedenen Lösern:[General FEM solvers discussion topic](https://forum.freecadweb.org/viewtopic.php?f=18&t=26326).

Wikipedia [listet viele Finite Elemente Softwarepakete auf](https://en.wikipedia.org/wiki/List_of_finite_element_software_packages). Einen Vergleich findest du auf [feacompare.com](https://feacompare.com/).



### Verfügbare Löser in verschiedenen Linux Distributionen 

Das [FreeCAD-Abhängigkeiten](https://github.com/luzpaz/FreeCAD-dependencies) Repositorium verfolgt die Abhängigkeiten von FreeCAD über viele Linux Distributionen hinweg. Die [FEM.md](https://github.com/luzpaz/FreeCAD-dependencies/blob/master/FC-Workbenches/FEM.md) Seite betrachtet verfügbare quelloffene FEA Löser, die mit der [FEM_Workbench/de](FEM_Workbench/de.md) verwendet werden können. Die Seite zeigt die Version eines bestimmten Lösers im Repositorium einer bestimmten Linux Distribution. Diese Information ist nützlich, um zu wissen, ob ein Löser aktuell oder veraltet ist und aktualisiert werden muss.

Die Informationen werden auch im Forum diskutiert: [unterstützter und nicht unterstützter Löser](https://forum.freecadweb.org/viewtopic.php?f=18&t=26326&start=10#p270325).



## Löser mit einer Schnittstelle in FreeCAD 

Diese Löser sind gut in FreeCAD integriert, was bedeutet, dass es möglich ist, ein Simulationsprojekt von der grafischen Oberfläche und den Schaltflächen im FEM Arbeitsbereich aus zu erstellen und auszuführen.



### CalculiX

Dies ist der erste Löser, der für die Arbeit mit dem FEM Arbeitsbereich integriert wurde. CalculiX ist vor allem für statische, thermo-mechanische und modale Analysen konzipiert. Weitere Informationen über diesen Löser findet man unter [FEM CalculiX](FEM_CalculiX/de.md).

### Elmer

Der Elmer-Multiphysics-Löser wurde als [Google-Summer-of-Code-2017](Google_Summer_of_Code_2017.md)-Projekt in FreeCAD integriert: [Hauptwebsite](https://www.csc.fi/web/elmer), [Gemeinschaftsportal](http://www.elmerfem.org./), [Code Repositorium](https://github.com/ElmerCSC/elmerfem), [Elmer Integration (GSoC) - Aktivitätsprotokoll](https://forum.freecadweb.org/viewtopic.php?f=18&t=22576) ( Forumsthema).



### Mystran

Mystran is a structural analysis program which uses Nastran input file format. It is released under MIT license. Which means it seems OpenSource. See [main website](https://www.mystran.com/), [code repository](https://github.com/dr-bill-c/MYSTRAN) and [Mystran-FreeCAD-forum (forum topic)](https://forum.freecadweb.org/viewtopic.php?t=46171).

### Z88

Der Löser Z88 ist für lineare statische Simulationen mit dem Schwerpunkt auf der Vermittlung der Finite-Elemente-Methode konzipiert. Er war der zweite Solver, der [in FreeCAD integriert](https://forum.freecadweb.org/viewtopic.php?f=18&t=15568) wurde. Danach wurde die Integration als Projekt des [Google Summer of Code 2017](Google_Summer_of_Code_2017.md) verbessert.

Siehe die Informationen:

-   [Hauptwebsite](https://en.z88.de/z88os/), [Downloadseite](https://en.z88.de/download-z88os/), [Quelltext Repositorium](https://github.com/LSCAD/Z88OS) (und vorkompilierte Binärdateien).
-   Versionshinweise: [Z88os V15 veröffentlicht am 17.07.2017](https://forum.z88.de/viewtopic.php?f=18&t=885), [Z88os V13 veröffentlicht am 20.05.2009](https://forum.z88.de/viewtopic.php?t=90) (Version in Debian Jessie 8, Stretch 9, Buster 10).
-   [Wie man Z88 in FEM? benutzt](https://forum.freecadweb.org/viewtopic.php?t=23318) (Forumsthema).

Es gibt zwei Versionen, Z88OS ist die quelloffene Version, während Z88Aurora Freeware ist und eine grafische Oberfläche und zusätzliche Lösungsmethoden enthält.



## Löser als externe Arbeitsbereiche implementiert 

Diese Löser sind nicht in den Arbeitsbereich [FEM](FEM_Workbench/de.md) integriert, d.h. sie benötigen eine separate Schnittstelle, um ein Simulationsprojekt zu erstellen. Dies wird durch [Makros](Macros/de.md) oder [externe Arbeitsbereiche](External_workbenches/de.md) erreicht.

### DualSPHysics

[DualSPHysics](https://dual.sphysics.org/) ist ein Satz von C++ , CUDA und Java Bibliotheken, die die [geglättete Teilchen Hydrodynamik](https://en.wikipedia.org/wiki/Smoothed-particle_hydrodynamics) verwenden. (SPH) Modell namens [SPHysics](https://wiki.manchester.ac.uk/sphysics/index.php/Main_Page) zur Untersuchung von Phänomenen der freien Oberflächenströmung wie z.B. brechenden Wellen.

DesignSPHysics ist ein in FreeCAD integrierter externer Arbeitsbereich, der eine grafische Benutzeroberfläche für DualSPHysics bietet: [Haupt-Website](https://design.sphysics.org/), [Code Repositorium](https://github.com/dualsphysics/DesignSPHysics), [Interessantes Projekt: DesignSPHysics Fluidsimulator](https://forum.freecadweb.org/viewtopic.php?f=18&t=20595) (Forumsthema).

DesignSPHysics kann über den [Addon-Manager](Std_AddonMgr/de.md) installiert werden.



### FastHenry und FasterCap 

FastHenry und FasterCap sind von FastFieldSolvers entwickelte Induktivitäts-Widerstands und Kapazitäts Feldlöser: [Hauptwebsite](https://www.fastfieldsolvers.com/default.asp), [Downloadseite](https://www.fastfieldsolvers.com/download.htm) (Binär- und Quellcode), [Forum](https://www.fastfieldsolvers.com/forum/).

Die [EM Arbeitsbereich](EM_Workbench/de.md) ist ein externer Arbeitsbereich, die als Front-End für diese elektromagnetischen Löser geschaffen wurde. FastHenry, für die 3D magneto-quasistatische Impedanzanalyse, wird vollständig unterstützt, während FasterCap über einige Python Makros zugänglich ist.

See: [ElectroMagnetic Workbench (main forum topic)](https://forum.freecadweb.org/viewtopic.php?f=9&t=33372) , [Electromagnetic Workbench - again.. (forum topic)](https://forum.freecadweb.org/viewtopic.php?f=18&t=31920), [FreeCAD for ElectroMagnetics (forum topic)](https://forum.freecadweb.org/viewtopic.php?f=18&t=5400), [code repository for the workbench](https://github.com/ediloren/EM-Workbench-for-FreeCAD).

The EM Workbench can be installed through the [AddonManager](Std_AddonMgr.md).

### fcFEM

fcFEM is a finite element solver for structural and mechanical studies, implemented in Python, and which can be run directly from FreeCAD without calling external binary solvers. Therefore, it can be considered FreeCAD\'s own internal solver.

fcFEM was designed to overcome certain limitations from other solvers, such as CalculiX, in order to perform various structural engineering studies.

Some of the problems that are intended to be overcome by this solver include

-   Mixed mesh analyses (solid-shell) for dealing with composite columns or prefabricated architectural components: [FEM object types (forum topic)](https://forum.freecadweb.org/viewtopic.php?f=18&t=21029&p=216682&hilit=sandwich#p216682).
-   Improved beam and shell elements, as CalculiX\'s beam elements seem to give wrong results: [CalculiX 3-node Beam Element (forum topic)](https://forum.freecadweb.org/viewtopic.php?f=18&t=27903&hilit=beam#p226038), [FEM object types (forum topic)](https://forum.freecadweb.org/viewtopic.php?f=18&t=21029&start=100), [Example for 1D analysis (forum topic)](https://forum.freecadweb.org/viewtopic.php?f=18&t=16044).
-   Arc-length control for overcoming limit points for elastic-plastic collapse analysis: [FEM - Tubular Connection with Shell Elements (forum topic)](https://forum.freecadweb.org/viewtopic.php?f=24&t=26921&hilit=riks#p215325).
-   Zero-thickness interface elements for various applications, like post-tensioned concrete with friction: [pre-stressed pre/post-tensioned concrete bridge (forum topic)](https://forum.freecadweb.org/viewtopic.php?f=18&t=30286&hilit=classical&start=20#p259636).

The author considers FreeCAD a good prototyping platform to quickly set up, test, and visualize different structural problems, so having an integrated yet flexible solver is very helpful. See [fcFEM - FEA from start to finish (main forum topic)](https://forum.freecadweb.org/viewtopic.php?f=18&t=33974).

fcFEM is packaged as a python library and a macro, and can be downloaded from the [github repository](https://github.com/HarryvL/fcFEM). It will eventually be available from the [AddonManager](Std_AddonMgr.md), or will be distributed as part of FreeCAD itself.

### OpenFoam

[OpenFoam](https://openfoam.org/) ist ein leistungsfähiges Framework für [Numerische Strömungsmechanik](https://en.wikipedia.org/wiki/Computational_fluid_dynamics) (engl.: computational fluid dynamics, CFD) Simulation, verteilt als eine Reihe von C++ Bibliotheken.

OpenFoam ist in FreeCAD über zwei externe Arbeitsbereiche verfügbar:

-   [Cfd](https://github.com/qingfengxia/Cfd), ursprünglich von Qingfeng Xia.
-   [CfdOF](https://github.com/jaheyns/CfdOF), eine Abspaltung von Cfd, die sich auf die Benutzerfreundlichkeit konzentriert.

Während Cfd für fortgeschrittene Anwender gedacht ist, konzentriert sich CfdOF auf Anwender, die gerade erst in die Welt von CFD und OpenFoam einsteigen.

Für Cfd: [Aktualisierung von FreeCAD + OpenFOAM Fluiddynamik Berechnung](https://forum.freecadweb.org/viewtopic.php?f=18&t=13699) (Forumsthema), [Fortschritte des Arbeitsbereichs allgemeinen Numerischen Strömungsmechanik (CFD): CfdWorkbench](https://forum.freecadweb.org/viewtopic.php?f=37&t=22993) (altes Forumsthema).

Füor CfdOF: [Computational Fluid Dynamics (CFD) Arbeitsbereich OpenFOAM verwendend](https://forum.freecadweb.org/viewtopic.php?f=18&t=21576) (Forumsthema), [Trainingsmaterial](http://opensim.co.za/training.html).

Beide Arbeitsbereiche können über den [Addon-Manager](Std_AddonMgr/de.md) installiert werden, und beide haben einen Platz für Diskussionen im [CfdOF / CFD-Unterforum](https://forum.freecadweb.org/viewforum.php?f=37).

## Implementation in progress 

### FEniCS

FEniCS is a computing framework for solving partial differential equations (PDEs), with high-level programming interfaces in Python and C++. It can be used to establish scientific problems in finite element formulations that then can be solved numerically.

See: [main website](https://fenicsproject.org/), [Fenics as Solver (forum topic)](https://forum.freecadweb.org/viewtopic.php?f=18&t=4677).

[FenicsSolver](https://github.com/qingfengxia/FenicsSolver) is a simulation platform to deal with multi-body, multi-physics (coupled), multi-scale problems. It hopes to integrate the FEniCS solver into both the [FEM Workbench](FEM_Workbench.md) and the Cfd [external workbench](External_workbenches.md), so the resulting system functions like a free alternative to Comsol or Moose. FenicsSolver is being developed by the same author of Cfd.

### OOFEM

[OOFEM](http://www.oofem.org/) is an object oriented FEM program by the Czech Technical University, for solving mechanical, transport and fluid mechanics problems.

It was mentioned as having some advantages over CalculiX, like interface elements ([pre-stressed pre/post-tensioned concrete bridge (forum topic)](https://forum.freecadweb.org/viewtopic.php?f=18&t=30286&start=20#p260275)), and arc-length control for elastic-plastic collapse analysis ([FEM - Tubular Connection with Shell Elements (forum topic)](https://forum.freecadweb.org/viewtopic.php?f=24&t=26921&hilit=Arc#p215325)).

Preliminary integration into the FEM Workbench has been done. See: [OOFem (main forum topic)](https://forum.freecadweb.org/viewtopic.php?f=18&t=31288), [test request, multiple solvers (forum topic)](https://forum.freecadweb.org/viewtopic.php?t=15568&start=20#p126338).

Until the solver integration is completed and the new code is merged into the main FreeCAD repository, the required files for using the solver in the FEM Workbench can be downloaded from a [forked FreeCAD branch](https://github.com/berndhahnebach/FreeCAD_bhb/tree/femoofem/src/Mod/Fem/). For a implementation overview have a look at the very clean commit history <https://github.com/berndhahnebach/FreeCAD_bhb/commits/femoofem>

### MBDyn

-   OpenSource general purpose Multibody Dynamics analysis software
-   [MBDyn](https://www.mbdyn.org/)
-   [FreeCAD as pre-post processor for MBDyn (forum topic)](https://forum.freecadweb.org/viewtopic.php?f=18&t=39165)

## Solvers not integrated 

The following solvers have not been integrated into FreeCAD but they have garnered some interest by the user community. If a developer wishes to create a communication bridge for a particular solver, he or she should refer to the [FEM subforum](https://forum.freecadweb.org/viewforum.php?f=18) for advice and assistance.

The following articles may be outdated, but the information they contain may still be useful to understand how to integrate solvers into FreeCAD

-   [Extend FEM Module](Extend_FEM_Module.md)
-   [Add FEM Equation Tutorial](Add_FEM_Equation_Tutorial.md)
-   [Add FEM Constraint Tutorial](Add_FEM_Constraint_Tutorial.md)

### ADAPy

See [ADAPy](https://github.com/Krande/adapy/) and [ADA - Assembly for Design & Analysis (forum topic)](https://forum.freecadweb.org/viewtopic.php?f=18&t=64929).

### Agros2D and Hermes 

[Agros2D](http://www.agros2d.org/) is a multiplatform graphical program designed for solving different physical problems. Internally it uses the [Hermes](http://www.hpfem.org/hermes/) C++ libraries for the solution of simple and complex time-dependent nonlinear partial differential equation (PDE) systems using a general version of the finite element method [(hp-FEM)](https://en.wikipedia.org/wiki/Hp-FEM). Main code [repository](https://github.com/hpfem/hermes), and [tutorials](https://github.com/hpfem/hermes-tutorial).

### Code-Aster and Code-Saturne 

[Code-Aster](https://www.code-aster.org/) is an open source multiphysics solver; together with the Salomé-Meca pre-processor they form a simulation platform developed by EDF-GDF, France\'s biggest energy company. It was an early package considered for inclusion in FreeCAD: [FreeCAD and Code-Aster/Salome-Meca (forum topic)](https://forum.freecadweb.org/viewtopic.php?t=2839).

[Code-Saturne](https://www.code-saturne.org/cms/) is a free, open-source software developed and released by EDF to solve computational fluid dynamics (CFD).

### FElt

[FElt](http://felt.sourceforge.net/) is a finite element package to solve linear static and dynamic structural analysis problems. The [original code](https://sourceforge.net/projects/felt/) is outdated, so it was forked to a [new repository](https://github.com/Sudhanshu-Dubey14/felt) to revive the project and make it compile in a modern system.

It was suggested in the forums to perform reinforced concrete frames analysis (beam and column assemblies) using 1D beam elements: [Automation in Design (forum topic)](https://forum.freecadweb.org/viewtopic.php?f=18&t=17061&start=20#p268503), [Felt in FEM Workbench (forum topic)](https://forum.freecadweb.org/viewtopic.php?f=18&t=33463).

### Frame3DD

[Frame3DD](http://frame3dd.sourceforge.net/) is a software package for static and dynamic structural analysis of 2D and 3D frames and trusses, [main repository](https://github.com/pslack/frame3dd). A preliminary reader for input files was announced in the forums: [Test read data from Frame3DD file](https://forum.freecadweb.org/viewtopic.php?f=24&t=19428). General topic in the FEM forum: [Frame3DD](https://forum.freecadweb.org/viewtopic.php?f=18&t=43389).

### Impact FEM 

-   <http://www.impact-fem.org/> (broken link)

### libMesh

[libMesh](https://libmesh.github.io/) is a c++ finite element library for the numerical solution of partial differential equations, with a major goal to provide support for adaptive mesh refinement (AMR) computations in parallel: [code repository](https://github.com/libMesh/libmesh).

It was suggested to integrate this library into FreeCAD as part of a [Google Summer of Code project](Google_Summer_of_Code.md): [GSOC 2019 Configuration Management Project (forum topic)](https://forum.freecadweb.org/viewtopic.php?f=8&t=35493).

### Modelica

[Modelica](https://www.modelica.org/) is a language to model and optimize complex, and interconnected physical systems, for example, mechanical, electrical, thermal, hydraulic, and others. The language itself and its standard libraries are open source. Some simulation environments based on Modelica, like Catia\'s Dymola, are proprietary, but there are also free implementations like [OpenModelica](https://openmodelica.org/) and [JModelica](https://jmodelica.org/).

With FreeCAD, Modelica was suggested to help perform animations, but more broadly it could be used in mechanical and building engineering to solve equations and optimize a particular design: [Modelica (forum topic)](https://forum.freecadweb.org/viewtopic.php?f=18&t=32556).

The [PyFMI](https://pypi.org/project/PyFMI/) package contains Python bindings to work with FMU models, which are standardized models in binary format produced by compliant Modelica environments, including Dymola, OpenModelica, and JModelica. It was suggested that this library could help FreeCAD connect to a [Modelica system](https://forum.freecadweb.org/viewtopic.php?f=18&t=32556#p272632) (forum topic).

### Mumps

[Mumps](http://mumps-solver.org/) is a generic solver for massive systems of equations, which generally deals with factorizing and operating on sparse matrices. It was mentioned in the forum: [Test request, multiple solvers (forum topic)](https://forum.freecadweb.org/viewtopic.php?t=15568&start=20#p126087).

It does not perform finite element analysis directly, but it may be used internally by other packages like Code-Aster.

### Nastran

Nastran is a structural analysis program developed by NASA in the 1970s. Modern versions of it are commercial products and closed source; however, older versions of it, [Nastran-93](https://github.com/nasa/NASTRAN-93) and [Nastran-95](https://github.com/nasa/NASTRAN-95) were released as open source in 2015. Forum post: [Nastran (forum topic)](https://forum.freecadweb.org/viewtopic.php?f=18&t=12753).

There is no technical support for the open source code, and it is probably difficult to compile in a modern system.

### OpenSees

[OpenSees](https://opensees.berkeley.edu/) is a software framework for developing applications to simulate structural and geotechnical systems mainly in the field of earthquake engineering. [OpenSees, the Open System for Earthquake Engineering Simulation (forum topic)](https://forum.freecadweb.org/viewtopic.php?f=18&t=20745) and [Relicensing of OpenSees (forum topic)](https://forum.freecadweb.org/viewtopic.php?f=18&t=31922).

### PolyFEM

[PolyFEM](https://polyfem.github.io/) is a simple C++ and Python finite element library. We provide a wide set of common partial differential equations including: Laplace, Helmholtz, Linear Elasticity, Saint-Venant Elasticity, Neo-Hookean Elasticity and Stokes. [PolyFEM (forum topic)](https://forum.freecadweb.org/viewtopic.php?f=18&t=42857).

### Sparselizard

[Sparselizard](http://www.sparselizard.org/) is a fast, general, multiphysics, p-adaptive, open source C++ finite element library running on Linux, Mac and Windows. It is used to design next generation microdevices (ultrasound transducers, micromirrors, microvalves, comb drives,\...) and it is carefully validated against analytical solutions, third party software and measurements of the fabricated devices. It looks like it is developed by the team of gmsh mesh generator.

### SU2

[SU2](https://su2code.github.io/) is a collection of software tools developed in C++ and Python for the solution of [partial differential equations](https://en.wikipedia.org/wiki/Partial_differential_equation) (PDE) and PDE-constrained optimization problems on unstructured meshes. It is particularly used in the fields of aerodynamics and computational fluid dynamics (CFD).

### Technog

Technog Professional is a closed source program to perform geotechnical simulations such as landslides, driving piles, slope stability, and civil engineering calculations (masonry and earthquake response), [website](http://www.feat.nl/) (broken link).

Technog was successfully used in FreeCAD as a substitute of CalculiX, although the trial version is limited in the number of elements it can handle: [Integration of tochnog solver in FreeCAD FEM (forum topic)](https://forum.freecadweb.org/viewtopic.php?f=18&t=26772).

### XC

[XC](http://www.xcengineering.xyz/) is a FEA program designed to solve structural problems in civil engineering like real beam shell analysis. Internally it uses the OpenSees libraries: [main repository](https://github.com/xcfem/xc), [XC, opensource structural engineering FEM code (forum topic)](https://forum.freecadweb.org/viewtopic.php?f=18&t=31262).


{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM Solver/de
