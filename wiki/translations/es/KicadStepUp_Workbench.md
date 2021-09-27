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

Kicad ([website](https://kicad-pcb.org/)) es una suite de automatización del diseño electrónico de código abierto. Permite diseñar un circuito eléctrico y crear una placa de circuito de una o varias capas utilizando una amplia biblioteca de piezas. Lo mejor es que el uso de FreeCAD y KicadStepUp ambiente de trabajo es la forma oficial de Kicad para crear piezas 3D de componentes eléctricos para Kicad. Las bibliotecas están alojadas [aquí](https://kicad.github.io/), por lo que todo el mundo puede crear y comprobar las piezas.


<div class="mw-translate-fuzzy">

La filosofía de la interfaz gráfica de KiCAD es un poco diferente en comparación con FreeCAD, especialmente cuando se trata de crear elementos y moverlos. Sin embargo, ya que Kicad se utiliza en la producción desde hace años hay una excelente documentación, por ejemplo, un documento muy bueno \"Cómo empezar\". Además, cada herramienta tiene su propio manual.


</div>

Si uno no conoce todavía [Kicad](https://kicad-pcb.org/), se recomienda completar un PCB autónomo de acuerdo con la [Guía de inicio](https://docs.kicad-pcb.org/5.1/en/getting_started_in_kicad/getting_started_in_kicad.pdf) para entender los conceptos involucrados. Aunque algunos temas como la adición de nuevos esquemas y huellas (Inglés:footprints) a una biblioteca local parecen ser de poco interés para el principiante, en la práctica se encuentran rápidamente después de comenzar un proyecto serio.

Para todos estos conceptos [Kicad](https://kicad-pcb.org/) se puede encontrar una función de algún tipo en el ambiente de trabajo KicadStepUp. Por lo tanto, conocer estos conceptos hace que sea mucho más fácil de entender cómo utilizar este ambiente de trabajo.

## Características


{{emphasis|En progreso}}

-   Load kicad board and parts in FreeCAD and export it to STEP (or IGES) for a full ECAD MCAD collaboration
-   Load kicad\_mod footprint in FreeCAD to easy and precisely align the mechanical model to kicad footprint
-   Convert the STEP 3D model of parts, board, enclosure to VRML with Materials properties for the best use in kicad
-   Check interference and collisions for enclosure and footprint design
-   Design a new pcb Edge with FreeCAD Sketcher and PUSH it to an existing kicad\_pcb Board
-   PULL a pcb Edge from a kicad\_pcb Board, edit it in FC Sketcher and PUSH it back to kicad
-   Design a new footprint in FreeCAD to get the power of Sketch in footprints
-   Generate Blender compatible VRML files

<img alt="" src=images/ECAD-MCAD-collaboration.png  style="width:800px;">

## Instalación

KicadStepUp es parte de los _ que viene incluido con FreeCAD 0.17, en el menú **Herramientas → Gestor de complementos**.


<div class="mw-translate-fuzzy">

## Utilización


{{emphasis|En progreso}}


</div>


{{emphasis|In progress}}

### General Approach 

The basic idea of KicadStepUp is to synchronise data between the two applications. For home use you might have open FreeCAD and Kicad at the same time. Professional use work on the same files (e.g. on a central server) and have specialists on mechanical CAD (MCAD) working in FreeCAD and electronics experts on electrical CAD (ECAD).

KicadStepUp will converts standard FreeCAD files to Kicad files and vise versa. That way each application can work with its native data files. Projects can be used without the other application or KicadStepUp installed. That also the reason, that no plugin on the Kicad side is required.

Undestanding the fine details of the workflow its helpful to note that the differences between the two programs impose some difficulties for a full data exchange.
One example is that the Sketcher used in Kicad to define the board outline is much more limited compared to the FreeCAD Sketcher, so in order to synchronise back and forth the model content can not be more complex than the Kicad Sketcher can handle. From a FreeCAD point of view, that means you may loose data. KicadStepUp offers workarounds that might be more difficult to understand if you do not have this background.

### Basic Workflow 

A a collaboration can be started with a new or an existing project. We consider here a new project to keep things simple:

1.  Create a new Kicad Project anywhere you like. Lets name it \"KsuTest\"
2.  Open the PCB Editor and create on the layer \"Edit.Cuts\" a closed outline. Shape does not matter, we will overwrite it anyway.
3.  Create a new FreeCAD file for the PCB, the name does not matter. \*
4.  Create a sketch with an outline of the desired PCB. Lets name it \"pcb design\" (but could be any other name) and put at least one circle into it for a hole.

    :   you may use any FreeCAD features to include holes, cutouts and outer shape to other components you might have. We assume here you would use Sketcher features as Dimensioning, Constraints and Work geometry in your sketch.
    :   If you are using PartDesign WB for creating the sketch there is no need to create a PartDesign body, since we are not going to pad this sketch.
5.  Switch to the KicadStepUp Workbech
6.  Select the \"pcb design\" sketch
7.  Select the Toolbar button \"Push Sketch to PCB Edge\" or the menu *ksu PushPull/ksu Push Sketch to PCB*
    -   first a dialog will open with defaults \"Edge.Cuts\" for layer and \"0.16\" for line width. Keep those defaults.
    -   next a file dialog will open. Click to your Kicad \"KsuTest\" project, where you should see a file \"KsuTest.kucad\_pcb\". That is the PCB file with the temporary outline we created before. Select is and confirm to replace the old file.
        Now a dialog should say \"new Edge pushed to kicad board!\"

        :   if you forgot the 2nd step, you the push operation might fail as a pcb file must exist and it must not be empty.
8.  Cloase and re-open the PCB Editor in Kicad. \*\*

    :   The shape from the FreeCAD sketch should appear.
9.  go over the circle with the mouse and press *m* on the keyboard to move the circle. Click to place to another position. Press the save toolbar button on the top left.
10. Switch to FreeCAD and select in the KicadStepUp Workbech the tool button \"Pull Sketch from PCB\" or the menu *ksu PushPull/ksu Pull Sketch from PCB*
    -   first dialog with default layer \"Edge.Cuts\" and three choices will open. Select choice \"replace PCB and Sketch in current document\" \*\*\*
    -   next a file dialog should show again the file \"KsuTest.kucad\_pcb\". Select it and press *Open*

        :   You should see your PCB as 3D model. Note that the hole has moved compared to you \"pcb design\" sketch.
        :   In the tree appears a new structure with a yellow *Part Container* with the Kicad Filename and within another *Part Container* with \"Board\_Geoms\_e63b\" (the part with the number probably different). In the second container there are the following three files. Do not change any names in that structure, because KicadStepUp uses them to find the parts to update.
        :   Do not forget to save your file




    Local_CS_e63b      the PCB origin. 
                         same as the origin in "pcb design" sketch
    Pcb_e63b           3D object with the PCB. 
                          Don't edit, it will be overwritten by KicadStepUp 
    PCB_Sketch_e63b    sketch with all part of "pcb design" sketch that Kicad recognized. 
                          all other were deleted. Also note that if you change this sketch
                          and recalculate 3D object will not change.

Try to make another PushPull round trip: adjust you \"pcb design\" sketch to the changes from Kicad, add some other change and start again. Do that a few times to appreciate how quickly and naturally this procedure becomes in a very short time.

Now you can use the new 3D PCB file to align 3D components as connectors, buttons, switches, fasteners, etc. or add this to your assembly if you have a larger project.

This only shows the very basic way KicadStepUp works. Your are still missing a lot at this point, e.g. footprints and 3D parts. But from there its a lot easier to start exploring KicadStepUp on your own. Use the documentation PDF file in the menu *ksu Tools/Demo*

:   \'\'Notes:
    -   As long as the name of the created strucure (and its parts) is unchanged any workflow interactions will just update the structure. If you change any names, a new structure will be created each time.
    -   It is not required to have Kicad running to update Kicad project files. Actually, Kicad does not even have to be installed on the PC.
    -   The standard approach is to use the same sketch on both sides Kicad and Freecad. Any changes will be synchronized to the other application. This is the most natural and clean way to work with KicadStepUp
        However, this causes a problem if you want to use any of the following features in your sketch definting you PCB shape: dimensions, geometry constraints, work geometry (blue lines) or external linked geometry. There is no clean way to do this, because Kicad does not know any of the features. That means that on the round trip between the applications any of those features will be deleted. There is not real solution for that problem, just a selection of one of several workarounds. So if you want to use any of those features that means you define the PCB shape in FreeCAD only and sync in one way to Kicad. Any outline changes done in Kicad need to be added manually on the FreeCAD side. This might make sense, e.g. if future changes from the mechanical side are much more likely than from the electrical side. There several ways to do it
        -   Put the design sketch inside the KicadStepUp structure, an select \"replace PCB and keep Sketch in curr. doc\" every time you import back from Kicad.
        -   Keep the design sketch outside the KicadStepUp structure. Ignore the sketch imported from Kicad.

    :   The second choice has the advantag that changes in Kicad can be traced to the original sketch and the FreeCAD sketch is protected against an accidently wrong import choice. The described workflow uses this approach to make sure the issue is well understood. From there its easy to switch to modifying the KicadStepUp supplied sketch with none of the more advanced FreeCAD features.

    -   To use KicadStepUp with a FreeCAD assembly (\> V0.19) you could add a new file for the PCB. After the workflow above has been run once add the 3D object for the PCB to your assembly like any other mechanical part. Make sure you save the file when it was updated by KicadStepUp (KicadStepUp writes to FreeCAD memory not to FreeCAD files).

\'\'

Consulte la [kicadStepUp ficha de ayuda](https://github.com/easyw/kicadStepUpMod/blob/master/demo/kicadStepUp-cheat-sheet.pdf) para conocer las demás características.

## Referencias

-   Autor: Github: [\@easyw](https://github.com/easyw) \| Foros de FreeCAD: [kicad StepUp: Colaboración bidireccional ECAD MCAD](https://forum.freecadweb.org/viewtopic.php?f=24&t=14276)
-   Código fuente en GitHub: <https://github.com/easyw/kicadStepUpMod>

## Nota al margen sobre los ambientes de trabajo externos 

Los ambientes de trabajo de FreeCAD son fáciles de programar en [Python](Python/es.md), por lo que hay mucha gente desarrollando ambientes de trabajo adicionales fuera de los desarrolladores principales de FreeCAD.

La página [Ambientes de trabajo externos](external_workbenches/es.md) tiene información y tutoriales sobre algunos de ellos, y el proyecto [FreeCAD Complementos](https://github.com/FreeCAD/FreeCAD-addons) pretende reunirlos y hacerlos fácilmente instalables desde FreeCAD.

Nuevos ambientes de trabajo están en desarrollo, esté atento!




_ _

---
[documentation index](../README.md) > [Addons](Category_Addons.md) > KicadStepUp Workbench/es
