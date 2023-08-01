# KicadStepUp Workbench/es
<div class="mw-translate-fuzzy">

KicadStepUp Icono del ambiente de trabajo externo


</div>


{{TOCright}}

## Introducción


<div class="mw-translate-fuzzy">

KicadStepUp ambiente de trabajo tiene como objetivo ayudar a los usuarios de KiCad y FreeCAD a colaborar en el diseño eléctrico (ECAD) y mecánico (MCAD).


</div>

## Fondo


<div class="mw-translate-fuzzy">

Kicad ([website](https://kicad-pcb.org/)) es una suite de automatización del diseño electrónico de código abierto. Permite diseñar un circuito eléctrico y crear una placa de circuito de una o varias capas utilizando una amplia biblioteca de piezas. Lo mejor es que el uso de FreeCAD y KicadStepUp ambiente de trabajo es la forma oficial de Kicad para crear piezas 3D de componentes eléctricos para Kicad. Las bibliotecas están alojadas [aquí](https://kicad.github.io/), por lo que todo el mundo puede crear y comprobar las piezas.


</div>


<div class="mw-translate-fuzzy">

La filosofía de la interfaz gráfica de KiCAD es un poco diferente en comparación con FreeCAD, especialmente cuando se trata de crear elementos y moverlos. Sin embargo, ya que Kicad se utiliza en la producción desde hace años hay una excelente documentación, por ejemplo, un documento muy bueno \"Cómo empezar\". Además, cada herramienta tiene su propio manual.


</div>


<div class="mw-translate-fuzzy">

Si uno no conoce todavía [Kicad](https://kicad-pcb.org/), se recomienda completar un PCB autónomo de acuerdo con la [Guía de inicio](https://docs.kicad-pcb.org/5.1/en/getting_started_in_kicad/getting_started_in_kicad.pdf) para entender los conceptos involucrados. Aunque algunos temas como la adición de nuevos esquemas y huellas (Inglés:footprints) a una biblioteca local parecen ser de poco interés para el principiante, en la práctica se encuentran rápidamente después de comenzar un proyecto serio.

Para todos estos conceptos [Kicad](https://kicad-pcb.org/) se puede encontrar una función de algún tipo en el ambiente de trabajo KicadStepUp. Por lo tanto, conocer estos conceptos hace que sea mucho más fácil de entender cómo utilizar este ambiente de trabajo.


</div>

For all these [KiCad](https://kicad.org/) concepts one can find a feature of some sort in the KicadStepUp workbench. So knowing those makes it a lot easier to understand how to use this workbench.

## Características


{{emphasis|En progreso}}

-   Load KiCad board and parts in FreeCAD and export it to STEP (or IGES) for a full ECAD MCAD collaboration
-   Load KiCad footprint in FreeCAD to easy and precisely align the mechanical model to KiCad footprint
-   Convert the STEP 3D model of parts, board, enclosure to VRML with Materials properties for the best use in KiCad
-   Check interference and collisions for enclosure and footprint design
-   Design a new PCB edge with the [Sketcher Workbench](Sketcher_Workbench.md) of FreeCAD and PUSH it to an existing KiCad PCB board
-   PULL a PCB edge from a KiCad PCB board, edit it in the Sketcher Workbench of FreeCAD and PUSH it back to KiCad
-   Design a new footprint in FreeCAD to get the power of Sketch in footprints
-   Generate Blender compatible VRML files

<img alt="" src=images/ECAD-MCAD-collaboration.png  style="width:800px;">

## Instalación


<div class="mw-translate-fuzzy">

KicadStepUp es parte de los [Ambientes de trabajo externos](external_workbenches/es.md), y puede instalarse automáticamente usando el <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestor de complementos de FreeCAD](Std_AddonMgr/es.md) que viene incluido con FreeCAD 0.17, en el menú **Herramientas → Gestor de complementos**.


</div>


<div class="mw-translate-fuzzy">

## Utilización


{{emphasis|En progreso}}


</div>


{{emphasis|In progress}}

### General Approach 

The basic idea of KicadStepUp is to synchronize data between the two applications. For home use you might have FreeCAD and KiCad running at the same time. Professional users can work on the same files (e.g. on a central server) and have specialists on mechanical CAD (MCAD) working in FreeCAD and electronics experts on electrical CAD (ECAD).

KicadStepUp will convert standard FreeCAD files to KiCad files and vice versa. That way each application can work with its native data files. Projects can be used without the other application or KicadStepUp installed. That is also the reason that no plugin on the KiCad side is required.

It\'s important to note that the differences between the two programs impose some difficulties for a full data exchange.
One example is that the Sketcher used in KiCad to define the board outline is very limited compared to the Sketcher Workbench of FreeCAD. So in order to synchronize back and forth, the sketch content cannot be more complex than the KiCad Sketcher can handle. From a FreeCAD point of view, that means you may want to avoid using some of the FreeCAD sketch features. KicadStepUp offers workarounds that might be more difficult to understand if you do not have this background.

### Basic Workflow 

A collaboration can be started with a new or an existing project. We consider here a new project to keep things simple:

1.  Create a new KiCad Project anywhere you like. Lets name it \"KsuTest\"
2.  Open the PCB Editor and create on the layer \"Edit.Cuts\" a closed outline. Shape does not matter, we will overwrite it anyway.
3.  Create a new FreeCAD file for the PCB, the name does not matter. \*
4.  Create a sketch with an outline of the desired PCB. Lets name it \"pcb design\" (but could be any other name) and put at least one circle into it for a hole.

    :   you may use any FreeCAD features to include holes, cutouts, and outer shape to other components you might have. We assume here you would use Sketcher features as Dimensioning, Constraints and Work geometry in your sketch.
    :   If you are using PartDesign Workbench for creating the sketch there is no need to create a PartDesign body, since we are not going to pad this sketch.
5.  Switch to the KicadStepUp Workbech
6.  Select the \"pcb design\" sketch
7.  Select the Toolbar button \"Push Sketch to PCB Edge\" or the menu *ksu PushPull/ksu Push Sketch to PCB*
    -   first a dialog will open with defaults \"Edge.Cuts\" for layer and \"0.16\" for line width. Keep those defaults.
    -   next a file dialog will open. Click to your KiCad \"KsuTest\" project, where you should see a file \"KsuTest.kucad_pcb\". That is the PCB file with the temporary outline we created before. Select it and confirm to replace the old file.
        Now a dialog should say \"new Edge pushed to kicad board!\"

        :   if you forgot the 2nd step, the push operation might fail as a pcb file must exist and it must not be empty.
8.  Close and re-open the PCB Editor in KiCad. \*\*

    :   The shape from the FreeCAD sketch should appear.
9.  Go over the circle with the mouse and press *m* on the keyboard to move the circle. Click to place it in another position. Press the \"Save\" toolbar button on the top left.
10. Switch to FreeCAD and select in the KicadStepUp Workbech the tool button \"Pull Sketch from PCB\" or the menu *ksu PushPull/ksu Pull Sketch from PCB*
    -   first dialog with default layer \"Edge.Cuts\" and three choices will open. Select choice \"replace PCB and Sketch in current document\" \*\*\*
    -   next a file dialog should show again the file \"KsuTest.kucad_pcb\". Select it and press *Open*

        :   You should see your PCB as a 3D model. Note that the hole has moved compared to your \"pcb design\" sketch.
        :   In the tree appears a new structure with a yellow *Part Container* with the KiCad Filename and within another *Part Container* with \"Board_Geoms_e63b\" (the part with the number probably different). In the second container there are the following three files. Do not change any names in that structure, because KicadStepUp uses them to find the parts to update.
        :   Do not forget to save your file




    Local_CS_e63b      the PCB origin.
                         same as the origin in "pcb design" sketch
    Pcb_e63b           3D object with the PCB.
                          Don't edit, it will be overwritten by KicadStepUp
    PCB_Sketch_e63b    sketch with all parts of "pcb design" sketch that KiCad recognized.
                          all others were deleted. Also note that if you change this sketch
                          and recalculate, the 3D object will not change.

Try to make another PushPull round trip: adjust your \"pcb design\" sketch to the changes from KiCad, add some other change and start again. Do that a few times to appreciate how quickly and naturally this procedure becomes in a very short time.

Now you can use the new 3D PCB file to align 3D components as connectors, buttons, switches, fasteners, etc., or add it to your assembly if you have a larger project.

This only shows the very basic way KicadStepUp works. You are still missing a lot at this point, e.g., footprints and 3D parts, but from here it\'s a lot easier to start exploring KicadStepUp on your own. Use the documentation PDF file in the menu *ksu Tools/Demo*

:   \'\'Notes:
    -   As long as the name of the created structure (and its parts) is unchanged, any workflow interactions will just update the structure. If you change any names, a new structure will be created each time.
    -   It is not required to have KiCad running to update KiCad project files. Actually, KiCad does not even have to be installed on the PC.
    -   The standard approach is to use the same sketch on both sides, KiCad and Freecad. Any changes will be synchronized to the other application. This is the most natural and clean way to work with KicadStepUp .
        However, this causes a problem if you want to use any of the following features in your sketch to define your PCB shape: dimensions, geometry constraints, construction geometry (blue lines), or external linked geometry. There is no clean way to do this, because KiCad does not know any of those features. That means that on the round trip between the applications, any of those features will be deleted. There is no real solution for that problem, just a selection of one of several workarounds. So if you want to use any of those features, that means you must define the PCB shape in FreeCAD only and sync in one direction toward KiCad. Any outline changes done in KiCad need to be added manually on the FreeCAD side. This might make sense, e.g. if future changes from the mechanical side are much more likely than from the electrical side. There several ways to do it:
        -   Put the design sketch inside the KicadStepUp structure, and select \"replace PCB and keep Sketch in curr. doc\" every time you import back from Kicad.
        -   Keep the design sketch outside the KicadStepUp structure. Ignore the sketch imported from KiCad.

    :   The second choice has the advantage that changes in KiCad can be traced to the original sketch, and the FreeCAD sketch is protected against an accidentally wrong import choice. The described workflow uses this approach to make sure the issue is well understood. From there it\'s easy to switch to modifying the KicadStepUp supplied sketch with none of the more advanced FreeCAD features.

    -   To use KicadStepUp with a FreeCAD assembly (\> V0.19) you could add a new file for the PCB. After the workflow above has been run once add the 3D object for the PCB to your assembly like any other mechanical part. Make sure you save the file when it was updated by KicadStepUp (Important: KicadStepUp writes to FreeCAD memory, not to FreeCAD files).

\'\'


<div class="mw-translate-fuzzy">

Consulte la [kicadStepUp ficha de ayuda](https://github.com/easyw/kicadStepUpMod/blob/master/demo/kicadStepUp-cheat-sheet.pdf) para conocer las demás características.


</div>

## Referencias

-   Autor: Github: [\@easyw](https://github.com/easyw) \| Foros de FreeCAD: [kicad StepUp: Colaboración bidireccional ECAD MCAD](https://forum.freecadweb.org/viewtopic.php?f=24&t=14276)
-   Código fuente en GitHub: <https://github.com/easyw/kicadStepUpMod>

## Nota al margen sobre los ambientes de trabajo externos 

Los ambientes de trabajo de FreeCAD son fáciles de programar en [Python](Python/es.md), por lo que hay mucha gente desarrollando ambientes de trabajo adicionales fuera de los desarrolladores principales de FreeCAD.

La página [Ambientes de trabajo externos](external_workbenches/es.md) tiene información y tutoriales sobre algunos de ellos, y el proyecto [FreeCAD Complementos](https://github.com/FreeCAD/FreeCAD-addons) pretende reunirlos y hacerlos fácilmente instalables desde FreeCAD.

Nuevos ambientes de trabajo están en desarrollo, esté atento!



---
![](images/Button_right.svg) [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > KicadStepUp Workbench/es
