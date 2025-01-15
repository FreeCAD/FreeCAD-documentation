# Fine-tuning/it
## Introduzione

Per impostare e manipolare la tabella dei parametri di FreeCAD normalmente si usa l\'[Editor delle preferenze](Preferences_Editor/it.md) nel menu **Modifica → Preferenze**.

Tuttavia, è anche possibile accedere, modificare e creare i parametri manualmente, usando l\'[Editor dei parametri](Std_DlgParameter/it.md) che si trova nel menu **Strumenti → Modifica parametri**.

Questa pagina elenca i parametri che non sono accessibili tramite l\'editor delle preferenze, ma che è possibile impostare manualmente per ottimizzare l\'installazione di FreeCAD o superare i problemi. Tutti i parametri si trovano in **BaseApp/Preferences/**.



## Generale


<div class="mw-translate-fuzzy">

-   **Mod/Part/ParametricRefine** (boolean) : impostare su `False` in modo che [Affina una forma](Part_RefineShape/it.md) crei una copia indipendente anziché una copia collegata. L\'impostazione predefinita è `True` se il valore non esiste.
-   **Mod/PartDesign/SwitchToTask** (boolean): impostare su `False` per impedire a [PartDesign](PartDesign_Workbench/it.md) di passare al pannello Azioni all\'avvio. L\'impostazione predefinita è `True` se il valore non esiste.
-   **Mod/PartDesign/SwitchToWB** (boolean): impostare su `False` per impedire che [PartDesign](PartDesign_Workbench/it.md) venga chiamato automaticamente quando viene attivato un [Corpo di PartDesign](PartDesign_Body/it.md). L\'impostazione predefinita è `True` se il valore non esiste.
-   **Document/SaveThumbnailFix** (boolean): impostare su `True` per risolvere un problema con Qt5 che impedisce la generazione delle miniature dei file `.FCStd`.
-   [TechDraw](TechDraw_Workbench/it.md) ha diverse opzioni nascost e documentate nelle [preferenze di TechDraw](TechDraw_Preferences/it#Impostazioni_nascoste.md).
-   **View/SavePicture** (string): impostare su **FramebufferObject**, **PixelBuffer** o **CoinOffscreenRenderer** per i metodi diversi per produrre immagini dalla vista 3D
-   **View/NaviStepByTurn** (integer) : Definisce il numero di passaggi incrementali (tacche) per completare un giro quando si utilizzano le frecce di NaviCube. Se il valore non è definito, il valore predefinito è **8**, il che significa che ogni incremento ruota di 360/8 = 45 gradi.
-   **View/NavigationDebug** (boolean) : abilita l\'output di debug degli stili di navigazione (a partire dalla v0.19, riguarda solo lo stile di navigazione gestuale).
-   **View/GestureRollFwdCommand**, **View/GestureRollBackCommand** (string) : comandi da eseguire con i gesti di scorrimento del pulsante del mouse nello stile di navigazione gestuale.
-   **View/GestureMoveThreshold** (integer) : la distanza (px) che il cursore del mouse deve spostarsi per passare alle modalità di rotazione o panoramica nello stile di navigazione gestuale. L\'impostazione predefinita è 5.
-   **View/GestureTapHoldTimeout** (integer) : imposta il tempo di attesa (in millisecondi) per entrare in modalità panoramica nello stile di navigazione gestuale. Può essere utile aumentarlo se il trascinamento della geometria nello sketcher è difficile. L\'impostazione predefinita è 700.
-   **Mod/Draft/defaultCameraHeight** (int) : imposta l\'altezza della videocamera all\'avvio di Draft in un documento vuoto. 0 disabilita, l\'impostazione di default è 5, buona quando si lavora in millimetri, una buona altezza per il lavoro per Arch è 4500
-   **DockWindows/TreeView/Enabled** (boolean): impostare su `True` per abilitare un widget agganciabile [Struttura del documento](Document_structure/it.md) indipendente dalla Vista combinata. Dopo aver modificato il valore del parametro, è necessario riavviare FreeCAD in modo che il widget sia disponibile nell\'elenco Visualizza → Pannelli.
-   **DockWindows/PropertyView/Enabled** (boolean): impostare su `True` per abilitare un widget agganciabile [Visualizza proprietà](Property_editor/it.md) indipendente dalla Vista combinata. Dopo aver modificato il valore del parametro, è necessario riavviare FreeCAD in modo che il widget sia disponibile nell\'elenco Visualizza → Pannelli.
-   **DockWindows/DAGView/Enabled** (boolean): Impostare su `True` per abilitare un widget agganciabile beta [Vista DAG](DAG_view/it.md). Dopo aver modificato il valore del parametro, è necessario riavvire FreeCAD in modo che il widget sia disponibile nell\'elenco Visualizza → Pannelli.
-   **General/ComboBoxWheelEventFilter** (boolean) : Impostare su `True` in modo che i widget non catturino gli eventi della rotellina del mouse e impediscano lo scorrimento delle aree scorrevoli.


</div>

## Default export filename 

-   **General/ExportDefaultFilenameMultiple** (string): Set the default filename to use when exporting multiple objects. Defaults to {{Value|%F}}.
-   **General/ExportDefaultFilenameSingle** (string): Set the default filename to use when exporting a single object. Defaults to {{Value|%F-%P-}}.

Both of these options support the automatic insertion of various pieces of information into the filename, using the following format characters:

-   %F - the name of the .FCStd file (or the label, if it is not saved yet)
-   %Lx - the label of the selected object(s), separated by character \'x\'
-   %Px - the label of the selected object(s) and their first parent, separated by character \'x\'
-   %U - the date and time, in UTC, [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
-   %D - the date and time, in local timezone, [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)

Any other characters are treated literally. If the resulting filename is illegal it will be changed on saving, with illegal characters replaced by the underscore (\_).

## Mouse related 

-   **General/ComboBoxWheelEventFilter** (boolean): Set to `True` so widgets do not catch mouse wheel event and prevent scrollable areas to be scrolled. Needs FreeCAD restart to be taken into account.
-   **View/GestureMoveThreshold** (integer): the distance (px) mouse cursor has to move to enter rotation or pan modes of Gesture navigation style. Defaults to {{Value|5}}.
-   **View/GestureRollFwdCommand**, **View/GestureRollBackCommand** (string): commands to be executed by mouse button roll gestures of Gesture navigation style.
-   **View/GestureTapHoldTimeout** (integer): sets for how long to wait (in milliseconds) to enter pan mode in Gesture navigation style. It can be helpful to increase it if dragging geometry in sketcher is difficult. Defaults to {{Value|700}}.

## Keyboard shortcuts 

### Escape key 

-   **General/TasksKeyEsc** (boolean): Create and set to `False` to disable the **ESC** key exiting the [Task panel](Task_panel.md) in all workbenches (that is if the task panel has focus).

## Navigation Cube 

See [Navigation Cube](Navigation_Cube#Advanced_parameters.md).

## Specific workbenches 

### <img alt="" src=images/Workbench_BIM.svg  style="width:24px;"> [BIM Workbench](BIM_Workbench.md) 

-   **Mod/BIM/DefaultPageScale** (float): Default scaling for new TechDraw pages created from the BIM Workbench, in case the template doesn\'t contain any \"Scale\" or \"Scaling\" (case insensitive) editable text field.

### <img alt="" src=images/Workbench_CAM.svg  style="width:24px;"> [CAM Workbench](CAM_Workbench.md) 

-   The [CAM Workbench](CAM_Workbench.md) has two switches to enable experimental features documented on the [CAM experimental](CAM_experimental.md) page.

### <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft Workbench](Draft_Workbench.md) 

-   **Mod/Draft/DefaultAnnoDisplayMode** (integer): Set to {{Value|1}} to create Draft annotations ([texts](Draft_Text.md), [dimensions](Draft_Dimension.md) and [labels](Draft_Label.md)) with their **Display Mode** set to {{Value|Screen}}. Set to {{Value|0}} for new annotations with this property set to {{Value|World}}. Defaults to {{Value|0}}. <small>(v1.0)</small> 
-   **Mod/Draft/GridHideInOtherWorkbenches** (boolean): Set to `False` to keep the [Draft grid](Draft_ToggleGrid.md) when switching to workbenches other than [BIM](BIM_Workbench.md) or [Draft](Draft_Workbench.md). Defaults to `True`. <small>(v1.0)</small> 
-   **Mod/Draft/useSupport** (boolean): Set to `True` to set the **Support** property of Draft objects created on a face of an exiting base object to that base object. This was standard behavior before FreeCAD version 0.19. Note that this parameter may not be supported in future versions. Defaults to `False`.

### <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Workbench](Part_Workbench.md) 

-   **Mod/Part/ParametricRefine** (boolean): Set to `False` so [Part RefineShape](Part_RefineShape.md) creates an independent copy rather than a linked one. Defaults to `True`.

### <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign Workbench](PartDesign_Workbench.md) 

-   **Mod/PartDesign/AdditiveHelixPreview** (boolean): Set to `True` to ensure an additive helix that does not intersect the body is visible in the preview. Defaults to `False`.
-   **Mod/PartDesign/DefaultDatumColor** (unsigned): Diffuse color and transparency for [PartDesign datums](PartDesign_CompDatums.md), [PartDesign ShapeBinders](PartDesign_ShapeBinder.md) and [PartDesign SubShapeBinders](PartDesign_SubShapeBinder.md). Defaults to {{Value|4292280473}}. See [here](Navigation_Cube#Customization.md) for information about the color value.
-   **Mod/PartDesign/SubtractiveHelixPreview** (boolean): Set to `True` to ensure a subtractive helix that does not intersect the body is visible in the preview. Defaults to `True`.
-   **Mod/PartDesign/SwitchToTask** (boolean): Set to `False` to prevent the [PartDesign Workbench](PartDesign_Workbench.md) from switching to the Task panel when starting. Defaults to `True`.
-   **Mod/PartDesign/SwitchToWB** (boolean): Set to `False` to prevent the [PartDesign Workbench](PartDesign_Workbench.md) to be automatically called when a [PartDesign Body](PartDesign_Body.md) is activated. Defaults to `True`.

### <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher Workbench](Sketcher_Workbench.md) 

-   **Mod/Sketcher/RadiusDiameterConstraintDisplayAngleRandomness** (float): Set an angle randomness on the above value. Value is the range of the random angle, centered on base angle. Defaults to {{Value|0}}.
-   **Mod/Sketcher/RadiusDiameterConstraintDisplayBaseAngle** (float): Set the angle (from horizontal) used to display radius/diameter constraints in Sketcher at creation time. Defaults to {{Value|15}}.
-   **Mod/Sketcher/RoundRectangleSuggConstraints** (boolean): Set to `False` to disable the addition of two extra construction points when creating a rounded rectangle. <small>(v0.21)</small> 

#### Constraint label colors 

The label in Sketcher that displays the current status of the constraints (e.g. \"Underconstrained,\" \"Fully Constrained,\" etc.) is styleable on a per-state basis either using the Qt stylesheet, or via user preferences. User preferences take precedence if they have been set (in **Mod/Sketcher/General**):

-   **EmptySketchMessageColor** - Defaults to 50% opacity black
-   **UnderconstrainedMessageColor** - Defaults to black
-   **MalformedConstraintMessageColor** - Defaults to red
-   **ConflictingConstraintMessageColor** - Defaults to red
-   **RedundantConstraintMessageColor** - Defaults to orange red
-   **PartiallyRedundantConstraintMessageColor** - Defaults to royal blue
-   **SolverFailedMessageColor** - Defaults to red
-   **FullyConstrainedMessageColor** - Defaults to green

### <img alt="" src=images/Workbench_Start.svg  style="width:24px;"> [Start Workbench](Start_Workbench.md) 

The Start Workbench is no longer included after version 0.21.

-   **Mod/Start/DefaultImportXXX** (string): Where XXX is a lowercase file extension. For example DefaultImportifc for .IFC files. Allows to set a default import module to be used when clicking an icon on the start page, when several importers are available. For example, setting DefaultImportifc = ifc_import will use the NativeIFC importer if available. <small>(v0.21)</small> 
-   **Mod/Start/TimeFormat** (string): A time format string such as {{Value|%m/%d/%Y %H:%M:%S}} used for the date in the tooltip that is shown when an item on the start page is hovered.

### [Help Module](Help_Module.md) 

-   **Mod/Help/UseWebModule** (boolean): Allows to force the use of the Web module to open MDI tabs. This can be useful to work around QWebEngine issues in some versions of Qt5. Defaults to `False`. <small>(v1.0)</small>



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > Fine-tuning/it
