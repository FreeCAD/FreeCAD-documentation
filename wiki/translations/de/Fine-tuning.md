# Fine-tuning/de
{{TOCright}}



## Einleitung

Der FreeCAD [Einstellungseditor](Preferences_Editor/de.md) unter dem Menüpunkt **Bearbeitungen → Einstellungen** wird üblicherweise verwendet, um die FreeCAD Parametertabelle festzulegen und zu ändern.

Jedoch ist es auch möglich, unter Verwendung des [Parameter Editors](Std_DlgParameter/de.md) der im Menü **Werkzeuge → Parameter bearbeiten** gefunden werden kann, auf Parameter manuell zuzugreifen, diese zu ändern und zu erstellen.

Diese Seite listet Parameter, die nicht über den Einstellungseditor zugänglich sind, aber manuell festgelegt werden können, für das Fine-Tuning der FreeCAD-Installation oder zur Fehlerbeseitigung. Alle Parameter befinden sich in **BaseApp/Preferences/**.

## General


<div class="mw-translate-fuzzy">

-   **Mod/Part/ParametricRefine** (boolesch) : Wenn der Wert auf `False` gesetzt ist, erstellt [Part FormVerfeinern](Part_RefineShape/de.md) eine unabhängige Kopie anstatt einer verknüpften Kopie. Der Standardwert ist `True`, wenn der Wert nicht existiert.
-   **Mod/PartDesign/SwitchToTask** (boolesch): Setze den Wert auf `False`, um zu verhindern, dass der [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md) beim Start in den Aufgabenbereich wechselt. Der Standardwert ist `True`, wenn der Wert nicht existiert.
-   **Mod/Bauteil-Design/SwitchToWB** (boolesch): Setze den Wert auf `False`, um zu verhindern, dass der [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md) automatisch aufgerufen wird, wenn ein [PartDesign Körper](PartDesign_Body/de.md) aktiviert wird. Der Standardwert ist `True`, wenn der Wert nicht existiert.
-   **Document/SaveThumbnailFix** (boolesch): Setze den Wert auf `True`, um ein Problem mit Qt5 zu beheben, das die Erzeugung von `.FCStd` Datei-Miniaturansichten verhindert.
-   **View/SavePicture** (Zeichenfolge / string): Setze den Wert auf **FramebufferObject**, **PixelBuffer** oder **CoinOffscreenRenderer** für verschiedene Methoden zur Erzeugung von Bildern aus der 3D Ansicht
-   **View/NaviStepByTurn** (ganzzahlig / integer) : Definiert, wie viele inkrementelle Schritte (Kerben) eine Umdrehung vollzieht, wenn die Pfeile des NaviCube verwendet werden. Wenn der Wert nicht definiert ist, wird er standardmäßig auf **8** gesetzt, d.h., dass jeder inkrementelle Schritt um 360/8 = 45 Grad rotiert.
-   **Mod/Draft/defaultCameraHeight** (ganzzahlig / integer): legt die Höhe der Kamera fest, wenn der Arbeitsbereich Entwurf in einem leeren Dokument beginnt. Eine 0 deaktiviert. Der FreeCAD-Standard ist 5. Das ist gut, wenn in Millimetern gearbeitet wird. Eine gute Höhe für Arbeiten im Bogenmaß ist 4500.
-   **DockWindows/TreeView/Enabled** (boolesch): Setze den Wert auf `True`, um in der [Baumansicht](Document_structure/de.md) ein anhängbares Element zu aktivieren, unabhängig von der Comboansicht. Nach dem Ändern des Parameterwertes ist es erforderlich, FreeCAD neu zu starten. Damit wird das Element in der Liste Ansicht/Konsole verfügbar.
-   **DockWindows/PropertyView/Enabled** (boolesch): Setze den Wert auf `True`, um im [Eigenschafteneditor](Property_editor/de.md) ein anhängbares Element zu aktivieren, unabhängig von der Comboansicht. Nach dem Ändern des Parameterwertes ist es erforderlich, FreeCAD neu zu starten. Damit wird das Element in der Liste Ansicht/Konsole verfügbar.
-   **DockWindows/DAGView/Enabled** (boolesch): Setze den Wert auf `True`, um in der Beta-[DAG Ansicht](DAG_view/de.md) ein anhängbares Element zu aktivieren. Nach dem Ändern des Parameterwertes ist es erforderlich, FreeCAD neu zu starten. Damit wird das Element in der Liste Ansicht/Konsole verfügbar.
-   **Document/ChangeViewProviderTouchDocument** (boolesch): Setze den Wert auf `True`, damit eine Änderung des Parameter Sichtbarkeit das Dokument nicht als geändert markiert.


</div>




<div class="mw-translate-fuzzy">

### Standard Dateinamen exportieren 


</div>

-   **General/ExportDefaultFilenameMultiple** (string): Set the default filename to use when exporting multiple objects. Defaults to \"%F\".
-   **General/ExportDefaultFilenameSingle** (string): Set the default filename to use when exporting a single object. Defaults to \"%F-%P-\".

Both of these options support the automatic insertion of various pieces of information into the filename, using the following format characters:

-   %F - the name of the .FCStd file (or the label, if it is not saved yet)
-   %Lx - the label of the selected object(s), separated by character \'x\'
-   %Px - the label of the selected object(s) and their first parent, separated by character \'x\'
-   %U - the date and time, in UTC, [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
-   %D - the date and time, in local timezone, [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)

Any other characters are treated literally. If the resulting filename is illegal it will be changed on saving, with illegal characters replaced by the underscore (\_).



## Mausbezogenes


<div class="mw-translate-fuzzy">

-   **General/ComboBoxWheelEventFilter** (boolesch) : Setze den Wert auf `True`, damit sich Mausradereignisse nicht auf Elemente auswirken und rollbare (scrollbar) Bereiche nicht gerollt werden.
-   **View/GestureMoveThreshold** (ganzzahlig / integer) : der Weg (px), den der Mauszeiger sich bewegen muss, um einen Rotations- oder Schwenkmodus des Gesture-Navigationsstils zu starten. Der Standardwert ist 5.
-   **View/GestureRollFwdCommand**, **View/GestureRollBackCommand** (Zeichenfolge / string): sind Befehle des Gesture-Navigationsstils, die durch Rollgesten mit der Maustaste ausgeführt werden.
-   **View/GestureTapHoldTimeout** (ganzzahlig / integer) : der Wert besagt in Millisekunden, wie lange gewartet wird, um im Gesture-Navigationsstil den Schwenkmodus (pan-mode) zu starten. Den Wert zu erhöhen kann helfen, wenn das Ziehen einer Geometrie mit der Maus im Skizzierer schwierig ist. Der Standardwert ist 700.


</div>



## Tastaturkurzbefehle




<div class="mw-translate-fuzzy">

### Abbruchtaste


</div>


<div class="mw-translate-fuzzy">

-   **General/TasksKeyEsc** (boolesch): erstelle und setze den Parameter auf `False`, um die Funktion der **Esc**-Taste, den [Aufgabenbereich](Task_panel/de.md) zu verlassen, wenn dieser den Fokus hat, zu deaktivieren. **Hinweis:** Ersetzt durch [Skizzen Einstellungen](Sketcher_Preferences/de#Allgemein.md)
-   **Mod/Sketcher/ViewKeyEsc** (boolesch): erstelle und setze den Parameter auf `False`, um Fehler zu vermeiden, wenn die **Esc**-Taste während des Fortführmodus zur Erstellung von Geometrie/Einschränkungen im Skizzierer einmal zu oft gedrückt wird (siehe [Foren-Thema](https://forum.freecadweb.org/viewtopic.php?f=3&t=42207&start=60#p367584))


</div>

## Navigation Cube 

See [Navigation Cube](Navigation_Cube#Advanced_parameters.md).



## Bestimmte Arbeitsbereiche 

### <img alt="" src=images/Workbench_BIM.svg  style="width:24px;"> [BIM Workbench](BIM_Workbench.md) 

-   **Mod/BIM/DefaultPageScale** (float): Default scaling for new TechDraw pages created from the BIM Workbench, in case the template doesn\'t contain any \"Scale\" or \"Scaling\" (case insensitive) editable text field.

### <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft Workbench](Draft_Workbench.md) 

-   **Mod/Draft/defaultCameraHeight** (int): Sets the height of the camera when Draft starts in an empty document. 0 disables, FreeCAD default is 5, good when working in millimeters, a good height for arch work is 4500.

### <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Workbench](Part_Workbench.md) 

-   **Mod/Part/ParametricRefine** (boolean): Set to `False` so [Part RefineShape](Part_RefineShape.md) creates an independent copy rather than a linked one. Defaults to `True`.

### <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign Workbench](PartDesign_Workbench.md) 

-   **Mod/PartDesign/AdditiveHelixPreview** (boolean): Set to `True` to ensure an additive helix that does not intersect the body is visible in the preview. Defaults to `False`.
-   **Mod/PartDesign/SubtractiveHelixPreview** (boolean): Set to `True` to ensure a subtractive helix that does not intersect the body is visible in the preview. Defaults to `True`.
-   **Mod/PartDesign/SwitchToTask** (boolean): Set to `False` to prevent the [PartDesign Workbench](PartDesign_Workbench.md) from switching to the Task panel when starting. Defaults to `True`.
-   **Mod/PartDesign/SwitchToWB** (boolean): Set to `False` to prevent the [PartDesign Workbench](PartDesign_Workbench.md) to be automatically called when a [PartDesign Body](PartDesign_Body.md) is activated. Defaults to `True`.

### <img alt="" src=images/Workbench_Path.svg  style="width:24px;"> [Path Workbench](Path_Workbench.md) 

-   The [Path Workbench](Path_Workbench.md) has two switches to enable experimental features documented on the [Path experimental](Path_experimental.md) page.

### <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher Workbench](Sketcher_Workbench.md) 

-   **Mod/Sketcher/RadiusDiameterConstraintDisplayAngleRandomness** (float): Set an angle randomness on the above value. Value is the range of the random angle, centered on base angle. Default is 0 degree.
-   **Mod/Sketcher/RadiusDiameterConstraintDisplayBaseAngle** (float): Set the angle (from horizontal) used to display radius/diameter constraints in Sketcher at creation time. Default is 15 degrees (if no value set).
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

-   **Mod/Start/DefaultImportXXX** (string): Where XXX is a lowercase file extension. For example DefaultImportifc for .IFC files. Allows to set a default import module to be used when clicking an icon on the start page, when several importers are available. For example, setting DefaultImportifc = ifc_import will use the NativeIFC importer if available. <small>(v0.21)</small>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Fine-tuning/de
