# Fine-tuning/de
## Einleitung

Der FreeCAD [Einstellungseditor](Preferences_Editor/de.md) unter dem Menüpunkt **Bearbeitungen → Einstellungen** wird üblicherweise verwendet, um die FreeCAD Parametertabelle festzulegen und zu ändern.

Jedoch ist es auch möglich, unter Verwendung des [Parameter Editors](Std_DlgParameter/de.md) der im Menü **Werkzeuge → Parameter bearbeiten** gefunden werden kann, auf Parameter manuell zuzugreifen, diese zu ändern und zu erstellen.

Diese Seite listet Parameter, die nicht über den Einstellungseditor zugänglich sind, aber manuell festgelegt werden können, für das Fine-Tuning der FreeCAD-Installation oder zur Fehlerbeseitigung. Alle Parameter befinden sich in **BaseApp/Preferences/**.



## Allgemein

-   **Bitmaps/Theme/Name** (string): Den Namen des Icon-themes angeben, das das System-icon-theme überschreibt, das FreeCAD verwendet. Wird nur verwendet, wenn **Bitmaps/Theme/UseIconTheme** auf `True` gesetzt ist.
-   **Bitmaps/Theme/ThemeSearchPaths** (boole): auf `False` setzen, damit FreeCAD seine enthaltenen Symbole verwendet anstatt der des System-icon-themes unter Linux. {{VersionMinus/de|0.21}}. Für neuere Versionen sollte stattdessen **Bitmaps/Theme/UseIconTheme** verwendet werden.
-   **Bitmaps/Theme/UseIconTheme** (boole): Auf `True` setzen, um Qt zu zwingen die Symbole des Icon-Themes des Systems einzusetzen. Der Standardwert ist `False` und FreeCAD verwendet seine eigenen Symbole. Dies beeinflusst nicht die anderen Qt-icon-theme-Mechanismen wie Systemdialoge, Schaltflächen und andere. Jene sollten immer die Symbole des System-Themes verwenden. {{Version/de|1.0}}
-   **Dialog/DontUseNativeColorDialog** (boole): Farbauswahldialog-Einstellung. Auf `False` setzen, wenn FreeCAD eher den Farbauswaldialog des Systems verwenden soll als den Qt-Farb-Dialog. Standardwert: `True`.
-   **Dialog/DontUseNativeDialog** (boole): Einstellung des Datei-Dialogs. Auf `False` setzen, wenn der Datei-Dialog des Systems zum Öffnen von Dateien verwendet werden soll oder auf `True` setzen, um den Qt-Dateiauswahldialog zu verwenden. Der Standardwert hängt von einer Einstellung während des Kompilierens ab: #define (USE_QT_FILEDIALOG).
-   **Dialog/DontUseNativeFontDialog** (boole): Wird von dem Befehl [Draft Textform](Draft_ShapeString/de.md) verwendet. Auf `False` setzen, um den Schrift-Dialog des Systems zu verwenden. Standardwert ist `True`.
-   **DockWindows/DAGView/Enabled** (boole): Auf `True` setzen, um in der Beta-[DAG-Ansicht](DAG_view/de.md) ein andockbares Fensterelement zu aktivieren. Nach dem Ändern des Parameterwertes ist es erforderlich, FreeCAD neu zu starten, damit das Fensterelement in der Ansichten-/Fensterliste zur Verfügung steht.
-   **DockWindows/PropertyView/Enabled** (boole): Auf `True` setzen, um im [Eigenschafteneditor](Property_editor/de.md) ein andockbares Fensterelement zu aktivieren, unabhängig von der Combo-Ansicht. Nach dem Ändern des Parameterwertes ist es erforderlich, FreeCAD neu zu starten, damit das Fensterelement in der Ansichten-/Fensterliste zur Verfügung steht.
-   **DockWindows/TreeView/Enabled** (boole): Auf `True` setzen, um in der [Baumansicht](Document_structure/de.md) ein andockbares Fensterelement zu aktivieren, unabhängig von der Combo-Ansicht. Nach dem Ändern des Parameterwertes ist es erforderlich, FreeCAD neu zu starten, damit das Fensterelement in der Ansichten-/Fensterliste zur Verfügung steht.
-   **Document/AutoNameDynamicProperty** (boole): Auf `True` setzen, um FreeCAD zu veranlassen dynamische Eigenschafen mit einem gültigen Namen automatisch umzubenennen, anstatt einen Ausnahme-Fehler auszugeben (throwing an exception). Man beachte, dass Python-Code keinen Zugriff auf den neuen Namen hat.
-   **Document/ChangeViewProviderTouchDocument** (boole): Auf `False` setzen, damit Änderungen der Sichtbarkeit eines Elements das Dokument nicht als geändert markieren.
-   **Document/SaveThumbnailFix** (boole): Auf `True` setzen, um ein Problem mit Qt5 zu beheben, das das Erstellen von Miniaturansichten für `.FCStd`-Dateien verhindert.
-   **General/LockToolBars** (boole): Auf `True` setzen, um die Verschiebbarkeit der Symbolleisten zu verhindern und die kleinen Griffpunkte auszublenden. Meist im Zusammenhang mit Stylesheets eingesetzt, die Symbolleisten vertikal ausrichten.
-   **General/RecentIncludesExported** (boole): Auf `True` setzen, um auch exportierte Dateien in der Liste der zuletzt geöffneten Dateien aufzunehmen. Standardwert ist `False`.
-   **General/RecentIncludesImported** (boolean): Auf `False` setzen, um importierte Dateien von der Liste der zuletzt geöffneten Dateien auszuschließen. Standardwert ist `True`.
-   **General/ShowSplasherMessages** (boole): Auf `False` setzen, um das Anzeigen von Nachrichten auf dem Begrüßungsschirm auszulassen. Dies kann die Dauer des FreeCAD-Starts verkürzen. Standardwert ist `True`.
-   **Macro/DuplicateFrom001** (boole): Auf `True` setzen, um die Suche nach Vorschlägen für Dateinamen von duplizierten Makros stets mit \@001 zu beginnen, anstatt mit der aktuellen Version \@NNN, falls möglich. Standardwert ist `False`.
-   **Macro/DuplicateIgnoreExtraNote** (boole): Auf `True` setzen, um Extra-Angaben zu ignorieren, wenn Namen für Dateinamen von duplizierten Makros vorgeschlagen werden. Extra-Angaben sind Texte im Dateinamen nach \"@NNN\" und vor \".FCMacro\". Beispiel: \"my_macro@005.my_note.FCMacro\". Auf `True` gesetzt, ist der nächste vorgeschlagene Dateiname \"my_macro@006.FCMacro\". Auf `False` gesetzt, ist dernächste vorgeschlagene Dateiname \"my_macro@006.my_note.FCMacro\". Um als Extra-Angabe erkannt zu werden, sollte der Text mit einem dem \"@NNN\" folgenden Punkt (\".\") beginnen. Andernfalls wird z.B. \"my_macro@006_my_note.FCMacro\" zu \"my_macro@006_my_note@001.FCMacro\" als vorgeschlagener neuer Dateiname, was in manchen Fällen erwünscht sein kann. Standardwert ist `False`.
-   **Macro/ReplaceSpaces** (boole): Auf `False` setzen, wenn Leerzeichen in Dateinamen nicht automatisch in Unterstriche umgewandelt werden sollen, wenn ein Makro erstellt, umbenannt, oder dupliziert wird. Dies beeinflusst vorhandene Dateien nicht; es betrifft nur das Erstellen neuer Dateien bzw. das Umbenennen oder Duplizieren vorhandener Dateien. Standardwert ist `True`.
-   **MainWindow/ClearMenuBar** (boole): Auf `True` setzen, um die Menüleiste bei einem Wechsel des Arbeitsbereiches zu leeren; nützlich, wenn ein globales Menü verwendet wird, da diese bei einem Wechsel des Arbeitsbereiches eventuell nicht aktualisiert werden und schnell vollgestopf werden mit den Menüeinträgen jedes Arbeitsbereiches. Standardwert ist `False`. Unter macOS wird sie in beiden Fällen geleert, als Übergangslösung für einen Qt-Fehler.
-   **MainWindow/ToolBarNameAsToolTip** (boole): Auf `False` setzen, um zu verhindern, dass der Namen einer Symbolleiste als QuickInfo angezeigt wird. Standardwert ist `True`.
-   **PropertyView/AutoTransactionView** (boole): Auf `True` setzen, damit Änderungen der Eigenschaften im Reiter Ansicht zum Rückgängig-Stapel hinzugefügt werden (und so das Rückgängigmachen ermöglicht wird). Standardwert ist `False`.
-   **Selection/AutoShowSelectionView** (boole): Auf `True` setzen, um das Fenster der Auswahlansicht automatisch anzuzeigen, wenn etwas ausgewählt wird. Standardwert ist `False`.
-   **Selection/singleClickFeatureSelect** (boole): Auf `False` setzen, um die Auswahl eines Formelements in PartDesign mit einem Einzelklick zu deaktivieren. Standardwert ist `True`.
-   **TreeView/HideColumn** (boolean): Auf {{True}} setzen, um die Spalte \'Beschreibung\' in der [Baumansicht](Tree_view/de.md) auszublenden. Standardwert ist `False`.
-   **TreeView/TreeViewStretchDescription** (boolean): Auf `True` setzen, um die Spalte \'Beschreibung\' in der [Baumansicht](Tree_view/de.md) bis zum rechten Fensterrand zu strecken. Standardwert ist `False`.
-   **View/AxisLetterColor** (unsigned): Farbe der Buchstaben des Koordinatensystems, das in der rechten unteren Ecke der 3D-Ansicht angezeigt wird. Standardwert ist {{Value|255}}. Siehe [hier](Navigation_Cube/de#Anpassung.md) für Informationen über die Farbwerte.
-   **View/AxisXColor** (unsigned): Farbe der Elemente der X-Achse des [Bewegungs](Std_TransformManip/de.md)-Werkzeug. Standardwert ist {{Value|3425907456}}. Siehe [hier](Navigation_Cube/de#Anpassung.md) für Informationen über den Farbwert.
-   **View/AxisYColor** (unsigned): Wie vorher für die Elemente der Y-Achse. Standardwert ist {{Value|869020416}}.
-   **View/AxisZColor** (unsigned): Wie vorher für die Elemente der Z-Achse.. Standardwert ist {{Value|859032576}}.
-   **View/LocalCoordinateSystemSize** (float): Größe des lokalen Koordinatensystems. Standardwert ist {{Value|2.0}}.
-   **View/NavigationDebug** (boole): Aktiviert die Ausgabe für die Fehlerbereinigung von Navigationsstilen (in Version 0.19 hat nur der Navigationsstil Geste etwas zu sagen).
-   **View/SavePicture** (string): Auf **FramebufferObject**, **PixelBuffer** oder **CoinOffscreenRenderer** setzen, um verschiedene Methoden zum Erstellen von Abbildungen der 3D-Ansicht auszuwählen.



### Standard-Export-Dateiname 

-   **General/ExportDefaultFilenameMultiple** (string): Set the default filename to use when exporting multiple objects. Defaults to {{Value|%F}}.
-   **General/ExportDefaultFilenameSingle** (string): Set the default filename to use when exporting a single object. Defaults to {{Value|%F-%P-}}.

Both of these options support the automatic insertion of various pieces of information into the filename, using the following format characters:

-   %F - the name of the .FCStd file (or the label, if it is not saved yet)
-   %Lx - the label of the selected object(s), separated by character \'x\'
-   %Px - the label of the selected object(s) and their first parent, separated by character \'x\'
-   %U - the date and time, in UTC, [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
-   %D - the date and time, in local timezone, [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)

Any other characters are treated literally. If the resulting filename is illegal it will be changed on saving, with illegal characters replaced by the underscore (\_).



## Mausbezogenes

-   **General/ComboBoxWheelEventFilter** (boole): Auf `True` setzen, damit Fensterelemente keine Mausradereignisse abfangen und so verhindern, dass scrollbare Bereiche nicht gescrollt werden. Erfordert den Neustart von FreeCAD, um zur Verfügung zu stehen.
-   **View/GestureMoveThreshold** (integer): Der Weg (px), den der Mauszeiger zurücklegen muss, um einen Rotations- oder Schwenkmodus des Gesture-Navigationsstils zu starten. Standardwert ist {{Value|5}}.
-   **View/GestureRollFwdCommand**, **View/GestureRollBackCommand** (string): Befehle des Gesture-Navigationsstils, die durch Rollgesten mit der Maustaste ausgeführt werden.

-   **View/GestureTapHoldTimeout** (integer) : Der Wert legt fest, wie lange gewartet wird (in Millisekunden), um im Gesture-Navigationsstil den Schwenkmodus (pan-mode) zu starten. Es kann hilfreich sein, den Wert zu erhöhen, wenn das Ziehen von Geometrie im Sketcher schwierig ist. Standardwert ist {{Value|700}}.



## Tastaturkurzbefehle



### Esc-Taste 

-   **General/TasksKeyEsc** (boole): Erstellen und auf `False` setzen, um die Funktion der **Esc**-Taste, das [Aufgaben-Fenster](Task_panel/de.md) zu verlassen, wenn dieses den Fokus hat, in allen Arbeitsbereichen zu deaktivieren.



## Navigationswürfel

Siehe [Navigationswürfel](Navigation_Cube/de#Erweiterte_Parameter.md).



## Bestimmte Arbeitsbereiche 



### Arbeisbereich <img alt="" src=images/Workbench_BIM.svg  style="width:24px;"> [BIM](BIM_Workbench/de.md) 

-   **Mod/BIM/DefaultPageScale** (float): Default scaling for new TechDraw pages created from the BIM Workbench, in case the template doesn\'t contain any \"Scale\" or \"Scaling\" (case insensitive) editable text field.



### Arbeisbereich <img alt="" src=images/Workbench_CAM.svg  style="width:24px;"> [CAM](CAM_Workbench/de.md) 

-   The [CAM Workbench](CAM_Workbench.md) has two switches to enable experimental features documented on the [CAM experimental](CAM_experimental.md) page.



### Arbeisbereich <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft](Draft_Workbench/de.md) 

-   **Mod/Draft/DefaultAnnoDisplayMode** (integer): Set to {{Value|1}} to create Draft annotations ([texts](Draft_Text.md), [dimensions](Draft_Dimension.md) and [labels](Draft_Label.md)) with their **Display Mode** set to {{Value|Screen}}. Set to {{Value|0}} for new annotations with this property set to {{Value|World}}. Defaults to {{Value|0}}. <small>(v1.0)</small> 
-   **Mod/Draft/GridHideInOtherWorkbenches** (boolean): Set to `False` to keep the [Draft grid](Draft_ToggleGrid.md) when switching to workbenches other than [BIM](BIM_Workbench.md) or [Draft](Draft_Workbench.md). Defaults to `True`. <small>(v1.0)</small> 
-   **Mod/Draft/useSupport** (boolean): Set to `True` to set the **Support** property of Draft objects created on a face of an exiting base object to that base object. This was standard behavior before FreeCAD version 0.19. Note that this parameter may not be supported in future versions. Defaults to `False`.



### Arbeitsbereich <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/de.md) 

-   **Mod/Part/ParametricRefine** (boolean): Set to `False` so [Part RefineShape](Part_RefineShape.md) creates an independent copy rather than a linked one. Defaults to `True`.



### Arbeitsbereich <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/de.md) 

-   **Mod/PartDesign/AdditiveHelixPreview** (boolean): Set to `True` to ensure an additive helix that does not intersect the body is visible in the preview. Defaults to `False`.
-   **Mod/PartDesign/DefaultDatumColor** (unsigned): Diffuse color and transparency for [PartDesign datums](PartDesign_CompDatums.md), [PartDesign ShapeBinders](PartDesign_ShapeBinder.md) and [PartDesign SubShapeBinders](PartDesign_SubShapeBinder.md). Defaults to {{Value|4292280473}}. See [here](Navigation_Cube#Customization.md) for information about the color value.
-   **Mod/PartDesign/SubtractiveHelixPreview** (boolean): Set to `True` to ensure a subtractive helix that does not intersect the body is visible in the preview. Defaults to `True`.
-   **Mod/PartDesign/SwitchToTask** (boolean): Set to `False` to prevent the [PartDesign Workbench](PartDesign_Workbench.md) from switching to the Task panel when starting. Defaults to `True`.
-   **Mod/PartDesign/SwitchToWB** (boolean): Set to `False` to prevent the [PartDesign Workbench](PartDesign_Workbench.md) to be automatically called when a [PartDesign Body](PartDesign_Body.md) is activated. Defaults to `True`.



### Arbeisbereich <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher](Sketcher_Workbench/de.md) 

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



### Arbeisbereich <img alt="" src=images/Workbench_Start.svg  style="width:24px;"> [Start](Start_Workbench/de.md) 

Der Arbeitsbereich Start ist nach der Version 0.21 nicht mehr Bestandteil von FreeCAD:

-   **Mod/Start/DefaultImportXXX** (string): Where XXX is a lowercase file extension. For example DefaultImportifc for .IFC files. Allows to set a default import module to be used when clicking an icon on the start page, when several importers are available. For example, setting DefaultImportifc = ifc_import will use the NativeIFC importer if available. <small>(v0.21)</small> 
-   **Mod/Start/TimeFormat** (string): A time format string such as {{Value|%m/%d/%Y %H:%M:%S}} used for the date in the tooltip that is shown when an item on the start page is hovered.

### [Help Module](Help_Module.md) 

-   **Mod/Help/UseWebModule** (boolean): Allows to force the use of the Web module to open MDI tabs. This can be useful to work around QWebEngine issues in some versions of Qt5. Defaults to `False`. <small>(v1.0)</small>



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > Fine-tuning/de
