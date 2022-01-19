# FEM Solver/ru
{{TOCright}}

## Предисловие


<div class="mw-translate-fuzzy">

На этой странице собрана вся информация о решателях метода конечных элементов (МКЭ), используемых [верстаком FEM](FEM_Workbench/ru.md). Интерфейс между решателем и FreeCAD в предварительной и последующей обработке выполнен через текстовые файлы. Теоретически это означает, что любой решатель, который может быть сконфигурирован и управляться через текстовые файлы, способен работать с FreeCAD, чтобы эта коммуникация действовала, необходимо запрограммировать соответствующий синтаксический анализатор и писатель входных и выходных файлов.


</div>

В Wikipedia [перечислены многие пакеты программ анализа конечных элементов](https://en.wikipedia.org/wiki/List_of_finite_element_software_packages). Их сравнение можно посмотреть на [feacompare.com](https://feacompare.com/).

### Available solvers in various Linux distributions 

The [FreeCAD-dependencies](https://github.com/luzpaz/FreeCAD-dependencies) repository tracks the dependencies of FreeCAD across many Linux distribution. The [FEM.md](https://github.com/luzpaz/FreeCAD-dependencies/blob/master/FC-Workbenches/FEM.md) page looks at available open source FEA solvers that could be used with the [FEM Workbench](FEM_Workbench.md). The page shows the version of a particular solver in the repository of a particular Linux distribution. This information is useful to know if a solver is current, or out of date and must be upgraded.

The information is also discussed in the forum: [supported and not supported Solver](https://forum.freecadweb.org/viewtopic.php?f=18&t=26326&start=10#p270325).

## Solvers with an interface in FreeCAD 

These solvers are well integrated into FreeCAD, which means that it\'s possible to set up and run a simulation project from the graphical interface and buttons in the FEM Workbench.

### CalculiX

This is the first solver that was integrated to work with the FEM Workbench. CalculiX is designed principally for static, thermo-mechanical, and modal analyses. More information about this solver is in [FEM CalculiX](FEM_CalculiX.md).

### Elmer

The Elmer multiphysics solver was integrated into FreeCAD as a [Google Summer of Code 2017 project](Google_Summer_of_Code_2017.md): [main website](https://www.csc.fi/web/elmer), [community portal](http://www.elmerfem.org./), [code repository](https://github.com/ElmerCSC/elmerfem), [Elmer Integration (GSoC) - Activity Log (forum topic)](https://forum.freecadweb.org/viewtopic.php?f=18&t=22576).

### Mystran

Mystran is a structural analysis program which uses Nastran input file format. It is released under MIT license. Which means it seems OpenSource. See [main website](https://www.mystran.com/), [code repository](https://github.com/dr-bill-c/MYSTRAN) and [Mystran-FreeCAD-forum (forum topic)](https://forum.freecadweb.org/viewtopic.php?t=46171).

### Z88

The Z88 solver is designed for linear static simulations with an emphasis on teaching about the finite element method. It was the second solver to be [integrated into FreeCAD](https://forum.freecadweb.org/viewtopic.php?f=18&t=15568). Afterwards, the integration was improved as a [Google Summer of Code 2017 project](Google_Summer_of_Code_2017.md).

See the information:

-   [Main website](https://en.z88.de/z88os/), [download page](https://en.z88.de/download-z88os/), [source code repository](https://github.com/LSCAD/Z88OS) (and precompiled binaries).
-   Release notes: [Z88os V15 released 17.07.2017](https://forum.z88.de/viewtopic.php?f=18&t=885), [Z88os V13 released 20.05.2009](https://forum.z88.de/viewtopic.php?t=90) (version in Debian Jessie 8, Stretch 9, Buster 10).
-   [How to use Z88 in FEM? (forum topic)](https://forum.freecadweb.org/viewtopic.php?t=23318).

There are two versions, Z88OS is the open source edition, while Z88Aurora is freeware, and includes a graphical interface and additional solution methods.

## Solvers implemented as external workbenches 

These solvers aren\'t integrated into the [FEM Workbench](FEM_Workbench.md), which means they need a separate interface to set up a simulation project. This is achieved through [macros](Macros.md) or [external workbenches](External_workbenches.md).

### DualSPHysics

[DualSPHysics](https://dual.sphysics.org/) is a set of C++, CUDA, and Java libraries that use the [smoothed particle hydrodynamics](https://en.wikipedia.org/wiki/Smoothed-particle_hydrodynamics) (SPH) model named [SPHysics](https://wiki.manchester.ac.uk/sphysics/index.php/Main_Page) to study free-surface flow phenomena such as crashing waves.

DesignSPHysics is an external workbench built into FreeCAD that provides a graphical user interface for DualSPHysics: [main website](https://design.sphysics.org/), [code repository](https://github.com/dualsphysics/DesignSPHysics), [Interesting project: DesignSPHysics fluid simulator (forum topic)](https://forum.freecadweb.org/viewtopic.php?f=18&t=20595).

DesignSPHysics can be installed through the [AddonManager](Std_AddonMgr.md).

### FastHenry and FasterCap 

FastHenry and FasterCap are inductance-resistance and capacitance field solvers developed by FastFieldSolvers: [main website](https://www.fastfieldsolvers.com/default.asp), [download page](https://www.fastfieldsolvers.com/download.htm) (binary and source code), [forum](https://www.fastfieldsolvers.com/forum/).

The [EM Workbench](EM_Workbench.md) is an external workbench that was created to serve as the front-end for these electromagnetic solvers. FastHenry, for 3D magneto-quasistatic impedance analysis, is fully supported, while FasterCap is accessible through some Python macros.

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

[OpenFoam](https://openfoam.org/) is a powerful framework for [computational fluid dynamics](https://en.wikipedia.org/wiki/Computational_fluid_dynamics) (CFD) simulation, distributed as a series of C++ libraries.

OpenFoam is available in FreeCAD through two external workbenches:

-   [Cfd](https://github.com/qingfengxia/Cfd), originally by Qingfeng Xia.
-   [CfdOF](https://github.com/jaheyns/CfdOF), a fork of Cfd focusing on ease of use.

While Cfd is intended to be feature-complete for advanced users, CfdOF focuses on users that are just starting in the world of CFD and OpenFoam.

For Cfd: [update on FreeCAD + OpenFOAM fluid dynamic computation (forum topic)](https://forum.freecadweb.org/viewtopic.php?f=18&t=13699), [Progress of the general Computational Fluid Dynamics (CFD) workbench: CfdWorkbench (old forum topic)](https://forum.freecadweb.org/viewtopic.php?f=37&t=22993).

For CfdOF: [Computational Fluid Dynamics (CFD) workbench using OpenFOAM (forum topic)](https://forum.freecadweb.org/viewtopic.php?f=18&t=21576), [training material](http://opensim.co.za/training.html).

Both workbenches can be installed through the [AddonManager](Std_AddonMgr.md), and both have a place for discussion in the [CfdOF / CFD subforum](https://forum.freecadweb.org/viewforum.php?f=37).

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

[PolyFEM](https://polyfem.github.io/) is PolyFEM is a simple C++ and Python finite element library. We provide a wide set of common PDEs including: Laplace, Helmholtz, Linear Elasticity, Saint-Venant Elasticity, Neo-Hookean Elasticity and Stokes. [PolyFEM (forum topic)](https://forum.freecadweb.org/viewtopic.php?f=18&t=42857).

### Sparselizard

[Sparselizard](http://www.sparselizard.org/) is a fast, general, multiphysics, p-adaptive, open source C++ finite element library running on Linux, Mac and Windows. It is used to design next generation microdevices (ultrasound transducers, micromirrors, microvalves, comb drives,\...) and it is carefully validated against analytical solutions, third party software and measurements of the fabricated devices. It looks like it is developed by the team of gmsh mesh generator.

### SU2

[SU2](https://su2code.github.io/) is a collection of software tools developed in C++ and Python for the solution of [partial differential equations](https://en.wikipedia.org/wiki/Partial_differential_equation) (PDE) and PDE-constrained optimization problems on unstructured meshes. It is particularly used in the fields of aerodynamics and computational fluid dynamics (CFD).

### Technog

Technog Professional is a closed source program to perform geotechnical simulations such as landslides, driving piles, slope stability, and civil engineering calculations (masonry and earthquake response), [website](http://www.feat.nl/) (broken link).

Technog was successfully used in FreeCAD as a substitute of CalculiX, although the trial version is limited in the number of elements it can handle: [Integration of tochnog solver in FreeCAD FEM (forum topic)](https://forum.freecadweb.org/viewtopic.php?f=18&t=26772).

### XC


<div class="mw-translate-fuzzy">

### XC 

[XC](http://www.xcengineering.xyz/) - это программа анализа методом конечных элементов, предназначенная для решения структурных проблем в гражданском строительстве, таких как анализ оболочки реальной балки. Внутри он использует библиотеки OpenSees: [главный репозиторий](https://github.com/xcfem/xc), [XC, код FEM для структурного проектирования с открытым исходным кодом.](https://forum.freecadweb.org/viewtopic.php?f=18&t=31262) (ветка форума).


</div>


{{FEM Tools navi

}}

---
[documentation index](../README.md) > FEM Solver/ru
