# Fine-tuning/de
{{TOCright}}

Diese Seite enthält verschiedene Einstellungen und Parameter, die du zur Feinabstimmung deiner FreeCAD Installation oder zur Behebung von Problemen verwenden kannst.

## Optionsparameter

Der FreeCAD [Einstellungseditor](Preferences_Editor/de.md) unter dem Menüpunkt {{MenuCommand/de|Bearbeitungen → Einstellungen}} wird üblicherweise verwendet, um die FreeCAD Parametertabelle festzulegen und zu ändern.

Jedoch ist es auch möglich, unter Verwendung des [Parameter Editors](Std_DlgParameter/de.md) der im Menü {{MenuCommand/de|Werkzeuge → Parameter bearbeiten}} gefunden werden kann, auf Parameter manuell zuzugreifen, diese zu ändern und zu erstellen.

Die folgende Liste zeigt Parameter, die nicht über den Einstellungseditor zugänglich sind, die du aber manuell festlegen kannst (befindet sich in **BaseApp/Preferences**)


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

### Standard Dateinamen exportieren 

-   **General/ExportDefaultFilenameMultiple** (string): Set the default filename to use when exporting multiple objects. Defaults to \"%F\".
-   **General/ExportDefaultFilenameSingle** (string): Set the default filename to use when exporting a single object. Defaults to \"%F-%P-\".

Both of these options support the automatic insertion of various pieces of information into the filename, using the following format characters:

-   %F - the name of the .FCStd file (or the label, if it is not saved yet)
-   %Lx - the label of the selected object(s), separated by character \'x\'
-   %Px - the label of the selected object(s) and their first parent, separated by character \'x\'
-   %U - the date and time, in UTC, [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
-   %D - the date and time, in local timezone, [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)

Any other characters are treated literally. If the resulting filename is illegal it will be changed on saving, with illegal characters replaced by the underscore (\_).

### Sketcher Constraint Label Colors 

The label in Sketcher that displays the current status of the constraints (e.g. \"Underconstrained,\" \"Overconstrained,\" \"Fully Constrained,\" etc.) is styleable on a per-state basis either using the Qt stylesheet, or via user preferences. User preferences take precedence if they have been set (in **Mod/Sketcher/General**):

-   **EmptySketchMessageColor** - Defaults to 50% opacity black
-   **UnderconstrainedMessageColor** - Defaults to black
-   **MalformedConstraintMessageColor** - Defaults to red
-   **ConflictingConstraintMessageColor** - Defaults to red
-   **RedundantConstraintMessageColor** - Defaults to orange red
-   **PartiallyRedundantConstraintMessageColor** - Defaults to royal blue
-   **SolverFailedMessageColor** - Defaults to red
-   **FullyConstrainedMessageColor** - Defaults to green

## Mausbezogenes


<div class="mw-translate-fuzzy">

-   **General/ComboBoxWheelEventFilter** (boolesch) : Setze den Wert auf `True`, damit sich Mausradereignisse nicht auf Elemente auswirken und rollbare (scrollbar) Bereiche nicht gerollt werden.
-   **View/GestureMoveThreshold** (ganzzahlig / integer) : der Weg (px), den der Mauszeiger sich bewegen muss, um einen Rotations- oder Schwenkmodus des Gesture-Navigationsstils zu starten. Der Standardwert ist 5.
-   **View/GestureRollFwdCommand**, **View/GestureRollBackCommand** (Zeichenfolge / string): sind Befehle des Gesture-Navigationsstils, die durch Rollgesten mit der Maustaste ausgeführt werden.
-   **View/GestureTapHoldTimeout** (ganzzahlig / integer) : der Wert besagt in Millisekunden, wie lange gewartet wird, um im Gesture-Navigationsstil den Schwenkmodus (pan-mode) zu starten. Den Wert zu erhöhen kann helfen, wenn das Ziehen einer Geometrie mit der Maus im Skizzierer schwierig ist. Der Standardwert ist 700.


</div>

## Tastaturkurzbefehle

### Abbruchtaste


<div class="mw-translate-fuzzy">

-   **General/TasksKeyEsc** (boolesch): erstelle und setze den Parameter auf `False`, um die Funktion der **Esc**-Taste, den [Aufgabenbereich](Task_panel/de.md) zu verlassen, wenn dieser den Fokus hat, zu deaktivieren. **Hinweis:** Ersetzt durch [Skizzen Einstellungen](Sketcher_Preferences/de#Allgemein.md)
-   **Mod/Sketcher/ViewKeyEsc** (boolesch): erstelle und setze den Parameter auf `False`, um Fehler zu vermeiden, wenn die **Esc**-Taste während des Fortführmodus zur Erstellung von Geometrie/Einschränkungen im Skizzierer einmal zu oft gedrückt wird (siehe [Foren-Thema](https://forum.freecadweb.org/viewtopic.php?f=3&t=42207&start=60#p367584))


</div>

## Bestimmte Arbeitsbereiche 

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:16px;"> [TechDraw Arbeitsbereich](TechDraw_Workbench/de.md) hat mehrere versteckte Schalter, die in [TechDraw Einstellungen](TechDraw_Preferences/de#Ausgeblendete_Einstellungen.md) dokumentiert sind.
-   <img alt="" src=images/Workbench_Path.svg  style="width:16px;"> [Pfad Arbeitsbereich](Path_Workbench/de.md) hat einen Schalter zur Aktivierung experimenteller Funktionen, die in [Pfad experimentell](Path_experimental/de.md) dokumentiert sind.
-   <img alt="" src=images/Workbench_BIM.svg  style="width:16px;"> [BIM Arbeitsbereich](BIM_Workbench/de.md):
    -   **Mod/BIM/DefaultPageScale** (Float): Standard Skalierung für neue TechDraw Seiten, die vom BIM Arbeitsbereich aus erstellt werden, falls die Vorlage kein editierbares Textfeld \"Skalieren\" oder \"Skalierung\" (Text unempfindlich) enthält.

## Verwandtes

-   [Parametereditor](Std_DlgParameter.md)
-   [Eigenschaftseditor](Preferences_editor.md)




[<img src="images/Property.png" style="width:16px"> Developer Documentation](Category_Developer_Documentation.md)

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Fine-tuning/de
