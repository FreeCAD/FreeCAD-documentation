# FEM CalculiX/ro
{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

### Prefață

Această pagină colectează toate informațiile despre solver CalculiX _, cel mai utilizat și cel mai bine dezvoltat solver din modulul FEM. În funcție de sistemul de operare pe care îl lucrați cu dvs., trebuie să instalați mai întâi CalculiX. Verificați [ FEM Install](FEM_Install.md).


</div>

The solver is able to do linear and non-linear calculations, for static, dynamic, and thermal problems. The solver operates on an Abaqus input file (`.inp`), which means it can be used with different pre-processors that support this format. The program includes its own graphical preprocessor which, however, is not used by FreeCAD, only the solver itself.

CalculiX is designed to run on Unix platforms like Linux and Irix computers but also on MS-Windows. CalculiX was developed by engineers from MTU Aero Engines, Munich, Germany, to assist them in designing machinery such as jet turbines. The software is currently released to the public on the terms of the GPL version 2.

## Integration with FreeCAD 


<div class="mw-translate-fuzzy">

### Interfața

Interacțiunea dintre modulul FEM și CalculiX se face prin fișiere text. Modulul FEM scrie un fișier de intrare CalculiX, pornește CalculiX, înregistrează ieșirea CalculiX și citește fișierele de ieșire ale CalculiX dacă acestea sunt disponibile. Instrumentul [ FEM Control Solver](FEM_SolverControl.md) gestionează întregul proces. Interacțiunea cu utilizatorul în acest proces este posibilă.


</div>

1.  A CalculiX input file is created with details required to run the simulation
2.  The CalculiX solver is started with this input file
3.  The output from the solver is logged
4.  The output files from the solver are read, if they are available

The [FEM Control Solver](FEM_SolverControl.md) tool manages the whole process. User interaction in the process is possible.

## Preprocessing interface 

The input file that CalculiX uses can be prepared and edited before the solver is started. The units used in the input file are independent of the units set in FreeCAD; they will always be millimeters (mm) and Newton (N).


**(ToDo: check this. What happens with the mesh if inch is used in FreeCAD? As density was introduced, with this we have kg and s and no longer N?! how about this?!)**

The CalculiX interface supports the following objects:

### FEM Elements 

-   Tet4 and Tet10
-   S3 and S6
-   B31 and B32
-   and those described in [FEM Mesh CalculiX](FEM_Mesh_CalculiX.md)

### Analysis

-   Linear static analysis
-   Frequency analysis
-   Coupled thermal-structural analysis

### Materials

-   One linear elastic isotropic material (uniformity in all directions)
-   Multiple material use is in development

## Postprocessing interface 


<div class="mw-translate-fuzzy">

#### Interfață postprocesare 

citiți stresul rezultat (Von Mises) și toate deplasările


</div>

Reaction forces can be found in ccx\_dat\_file which contains reaction force components (fx, fy, fz) for each Constraint fixed and for each Constraint displacement which constrains translation degrees of freedom.

## Related

-   [FEM Mesh CalculiX](FEM_Mesh_CalculiX.md)
-   [CalculiX preferences](FEM_Preferences#CalculiX.md) dialog menu in the FEM Workbench preferences menu


{{FEM Tools navi

}}

_ _

---
[documentation index](../README.md) > [Poweruser_Documentation](Category_Poweruser_Documentation.md) > FEM CalculiX/ro
