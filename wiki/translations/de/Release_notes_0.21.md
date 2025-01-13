# Release notes 0.21/de
**FreeCAD 0.21** wurde am **2. August 2023** veröffentlicht; es kann von der [Download](Download/de.md)-Seite heruntergeladen werden. Diese Seite listet alle Neuerungen und Änderungen auf.

Ältere FreeCAD-Versionshinweise findet man in der [Funktionsliste](Feature_list/de#Versionshinweise.md).

<img alt="" src=images/FreeCAD_relnotes_0.21.png  style="width:720px;">



## Allgemein

-   Die Standardbenennung von Backup-Dateien ist jetzt **FCBak**. Das ältere Format (**FCStd#**) ist veraltet und wird in einer zukünftigen Version entfernt werden. Anwender, die das alte System aktiviert haben, werden beim Start gewarnt.[Pull request #9668](https://github.com/FreeCAD/FreeCAD/pull/9668)



## Benutzeroberfläche

+++
| ![](images/Navi_Cube_relnotes_0.21.png ) | Der [Navigationswürfel](Navigation_Cube/de.md) wurde aktualisiert. Er wird nicht mehr perspektivisch dargestellt, wenn für die [3D-Ansicht](3D_view/de.md) Orthogonale Ansicht eingestellt wurde. Die Ecken des Navigationswürfels sind jetzt sechseckig und größer, dadurch sind sie einfacher anzuklicken. Die Schaltflächen haben eine Einfassung bekommen. Die Auswahl von Standardschriftart und Schrifthöhe wurde verbessert. Das Miniwürfelmenü enthält jetzt eine Checkbox, um den Würfel zwischen verschiebbar und ortsfest umzuschalten. Mehrere neue Parameter wurden hinzugefügt; siehe die Seite [Navigationswürfel](Navigation_Cube/de.md) für weitere Informationen. [Pull request #7876](https://github.com/FreeCAD/FreeCAD/pull/7876), [Pull request #8266](https://github.com/FreeCAD/FreeCAD/pull/8266), [Pull request #8646](https://github.com/FreeCAD/FreeCAD/pull/8646) und [Pull request #9356](https://github.com/FreeCAD/FreeCAD/pull/9356). |
+++

+++
| <img alt="" src=images/Part_SectionCut_example_relnotes_0.21.gif  style="width:384px;">Dauerhafte Schnittdarstellung sich gegenseitig durchdringender Objekte.Ein Klick auf das Bild zeigt die Animation. | Das Werkzeug [Schnittansicht](Part_SectionCut/de.md) ermöglicht jetzt sich durchdringende Objekte zu beschneiden. Dies ist nützlich für Baugruppen, wo sich manchmal Überschneidungen von Teilen, die sich (eigentlich) berühren, aufgrund von Berechnungsabweichungen nicht vermeiden lassen. |
|                                                                                                                                                                                                                                                       | [Pull request #8252](https://github.com/FreeCAD/FreeCAD/pull/8252).                                                                                                                                                                                                                                    |
+++

+++
| <img alt="" src=images/Measurement-Part_relnotes_0.21.png  style="width:384px;"> | Die Darstellungsart von [Messergebnissen](Part_Workbench/de#Messung.md), die in den Arbeitsbereichen [Part](Part_Workbench/de.md) oder [PartDesign](PartDesign_Workbench/de.md) erstellt wurden, können jetzt in den [Einstellungen](PartDesign_Preferences/de#Measure.md) angepasst werden. [Pull request #7148](https://github.com/FreeCAD/FreeCAD/pull/7148) |
+++

+++
| <img alt="" src=images/WbSelector_relnotes_0.21.png  style="width:384px;"> | Das Auswahlfeld für Arbeitsbereiche kann jetzt wahlweise in die Menüleiste gelegt werden, anstatt in den Bereich der Symbolleisten. [Pull request #7679](https://github.com/FreeCAD/FreeCAD/pull/7679) |
+++



### Weitere Verbesserungen der Benutzeroberfläche 

-   Die Schaltflächen für <img alt="" src=images/Std_Print.svg  style="width:24px;"> [Drucken](Std_Print/de.md) und <img alt="" src=images/Std_UserEditModeDefault.svg  style="width:24px;"> [Bearbeitungsmodus](Std_UserEditMode/de.md) wurden aus der Symbolleiste Datei entfernt. Sie können erneut hinzugefügt werden, indem man eine eigene Symbolleiste [anpasst](Std_DlgCustomize/de.md).[Pull request #7570](https://github.com/FreeCAD/FreeCAD/pull/7570) und [commit ea9a04e](https://github.com/FreeCAD/FreeCAD/commit/ea9a04e)
-   Die Symbolleiste Datei wurde geteilt. Die Schaltflächen für <img alt="" src=images/Std_Undo.svg  style="width:24px;"> [Rückgängig](Std_Undo/de.md), <img alt="" src=images/Std_Redo.svg  style="width:24px;"> [Wiederherstellen](Std_Redo/de.md) und <img alt="" src=images/Std_Refresh.svg  style="width:24px;"> [Aktualisieren](Std_Refresh/de.md) wurden in die neue Symbolleiste Bearbeiten verschoben. Die Schaltflächen für <img alt="" src=images/Std_Cut.svg  style="width:24px;"> [Ausschneiden](Std_Cut/de.md), <img alt="" src=images/Std_Copy.svg  style="width:24px;"> [Kopieren](Std_Copy/de.md) und <img alt="" src=images/Std_Paste.svg  style="width:24px;"> [Einfügen](Std_Paste/de.md) wurden in die neue Symbolleiste Zwischenablage verschoben. Die Schaltfläche für die <img alt="" src=images/Std_WhatsThis.svg  style="width:24px;"> [Direkthilfe](Std_WhatsThis/de.md) wurde in die neue Symbolleiste Hilfe verschoben. [Pull request #7620](https://github.com/FreeCAD/FreeCAD/pull/7620)
-   Befehle zum [Speichern](Std_StoreWorkingView/de.md) und [Abrufen](Std_RecallWorkingView/de.md) temporärer Arbeitsansichten wurden hinzugefügt. [Pull request #7525](https://github.com/FreeCAD/FreeCAD/pull/7525)
-   Das Ändern der Werte mit dem Mausrad in Eingabefeldern (eine Widget-Art, die verwendet wird, um Werte im Aufgabenbereich einzugeben, z.B. von [Draft Linie](Draft_Line/de.md)) ist deaktiviert, wenn der Fokus nicht auf dem Widget liegt und der Schalter [ComboBoxWheelEventFilter](Fine-tuning.md) aktiviert ist. Dies verhindert ungewollte Wertveränderungen während des Scrollens, wie schon bei Spin- und Combo-Boxen. [Pull request #7561](https://github.com/FreeCAD/FreeCAD/pull/7561)
-   Es ist jetzt möglich, eine Standardeinstellung für die Transparenz neu erstellter [Part-](Part_Workbench/de.md) oder [PartDesign-](PartDesign_Workbench/de.md) Objekte in den [Einstellungen](PartDesign_Preferences/de.md) festzulegen. [Pull request #7103](https://github.com/FreeCAD/FreeCAD/pull/7103)
-   Es gibt einen neuen Orbit-Stil **Free Turntable**. Er kann im [Voreinstellungseditor](Preferences_Editor/de#Navigation.md) aktiviert werden oder durch Drücken der Schaltfläche **[<img src=images/NavigationCAD_dark.svg style="width:16px">** in der [Statusleiste](Status_bar/de.md) and then using the menu **Settings → Orbit**). [Pull request #8048](https://github.com/FreeCAD/FreeCAD/pull/8048)
-   Der Aufgabenbereich [Std Darstellung](Std_SetAppearance/de.md) besitzt jetzt eine Schaltfläche zum Festlegen der Eigenschaft Point-Color. [Pull request #7708](https://github.com/FreeCAD/FreeCAD/pull/7708)
-   Eine Schaltfläche zum wechseln der Farben des Hintergrundverlaufs der [3D-Ansicht](3D_view/de.md) wurde im [Voreinstellungseditor](Preferences_Editor/de#Farben.md) hinzugefügt. [Pull request #7155](https://github.com/FreeCAD/FreeCAD/pull/7155)
-   Alle Transparenzeinstellungen verwenden jetzt einheitlich eine Schrittweite von 5% für Spin-Buttons: Ein Klick auf die Schaltfläche in einem Dialog oder dem [Eigenschafteneditor](Property_editor/de.md) ändert die Transparenz um 5%. Wird die Schaltfläche gedrückt gehalten, werden mehrere 5%-Schritte auf einmal ausgeführt. [Pull request #7723](https://github.com/FreeCAD/FreeCAD/pull/7723)
-   Das Ausgabefenster (Output window) wurde in ??? (Report view) geändert, zur Vereinheitlichung (mit) der Benutzerschnittstelle (UI). [Pull Request #7739](https://github.com/FreeCAD/FreeCAD/pull/7739)
-   Der Arbeitsbereich Image wurde entfernt. Zum einfügen einer Bildebene kann jetzt der Befehl [Std Import](Std_Import/de.md) verwendet werden. Ausrichtung und Skalierung können nach einem Doppelklick auf die Bildebenen geändert werden. Der neue Befehl [Std AnsichtBildLaden](Std_ViewLoadImage/de.md) ersetzt den Befehl Image Öffnen. [Pull Request #8955](https://github.com/FreeCAD/FreeCAD/pull/8955)
-   Der veraltete Arbeitsbereich Raytracing wurde entfernt. Der externe Arbeitsbereich [Render](https://github.com/FreeCAD/FreeCAD-render) sollte stattdessen verwendet werden. [Pull Request #9420](https://github.com/FreeCAD/FreeCAD/pull/9420)



## Kernsystem und API 



### Kern

-   Die Funktion **cbrt(x)** für Kubikwurzeln wurde hinzugefügt für die Verwendung in [Ausdrücken](Expressions/de#Exponential-_und_Logarithmusfunktionen.md). [Pull request #8629](https://github.com/FreeCAD/FreeCAD/pull/8629)
-   Es gibt viele neue [Eigenschaften](Property/de#Alle_Arten_von_Eigenschaften.md) für die Skripterstellung. [Pull request #6717](https://github.com/FreeCAD/FreeCAD/pull/6717)
-   Hinzugefügte Funktionen für die Objekterstellung {{Incode|vector}}, {{Incode|matrix}}, {{Incode|rotation}}, {{Incode|placement}} und auch Matrix-Funktionen {{Incode|mrotate}}, {{Incode|mrotatex}}, {{Incode|mrotatey}}, {{Incode|mrotatez}}, {{Incode|mtranslate}} zur Verwendung in [Ausdrücken](Expressions/de.md). [Pull request #8603](https://github.com/FreeCAD/FreeCAD/pull/8603).

### API


<div class="mw-collapsible mw-collapsed toccolours">



#### Neue Python API 


<div class="mw-collapsible-content">

-   *BSplineSurfacePy::scaleKnotsToBounds*: Skaliert die Listen der U- und V-Knoten, um sie in die vorgegebenen Grenzen einzupassen. [Pull request #7258](https://github.com/FreeCAD/FreeCAD/pull/7258) und [Pull request #7385](https://github.com/FreeCAD/FreeCAD/pull/7385)
-   *BSplineCurvePy::scaleKnotsToBounds*: Skaliert die Knotenliste, um sie in die vorgegebenen Grenzen einzupassen. [Pull request #7385](https://github.com/FreeCAD/FreeCAD/pull/7385)

-   *ShapeFix_EdgeConnectPy*: Wurzel?-Klasse (root class) für Reparaturaktionen. [commit 4d4adb93](https://github.com/FreeCAD/FreeCAD/commit/4d4adb93)
-   *ShapeFix_EdgePy*: Reparieren ungültiger Kanten. [commit 4089cbfb](https://github.com/FreeCAD/FreeCAD/commit/4089cbfb)
-   *ShapeFix_FaceConnectPy*: Wiederherstellen der Verbindungen zwischen den Flächen eines Flächenverbundes.[commit a0eb2e9d](https://github.com/FreeCAD/FreeCAD/commit/a0eb2e9d)
-   *ShapeFix_FacePy*: Klasse für Reparaturaktionen an Flächen.[commit b6cd635c](https://github.com/FreeCAD/FreeCAD/commit/b6cd635c)
-   *ShapeFix_FixSmallFacePy*: Klasse für Reparaturaktionen an Flächen.[commit 4c2946c8](https://github.com/FreeCAD/FreeCAD/commit/4c2946c8)
-   *ShapeFix_FixSmallSolidPy*: Reparieren von kleinen Festkörpern. [commit b70d8d37](https://github.com/FreeCAD/FreeCAD/commit/b70d8d37)
-   *ShapeFix_FreeBoundsPy*: Gedacht zur Ausgabe von freien Rändern der Form.[commit 1ee1aee1](https://github.com/FreeCAD/FreeCAD/commit/1ee1aee1)
-   *ShapeFix_RootPy*: Wurzel?-Klasse (root class) für Reparaturaktionen. [commit f3e941a3](https://github.com/FreeCAD/FreeCAD/commit/f3e941a3)
-   *ShapeFix_ShapePy*: Klasse für Reparaturaktionen an Formen. [commit 87db9dcc](https://github.com/FreeCAD/FreeCAD/commit/87db9dcc)
-   *ShapeFix_ShapeTolerancePy*: Passt Toleranzen von Teilformen (Sub-Shapes) an (Knoten, Kanten, Flächen). [commit 125d5b63](https://github.com/FreeCAD/FreeCAD/commit/125d5b63)
-   *ShapeFix_ShellPy*: Wurzel?-Klasse (root class) für Reparaturaktionen. [commit f3e941a3](https://github.com/FreeCAD/FreeCAD/commit/f3e941a3)
-   *ShapeFix_SolidPy*: Wurzel?-Klasse (root class) für Reparaturaktionen. [commit 8d568793](https://github.com/FreeCAD/FreeCAD/commit/8d568793)
-   *ShapeFix_SplitCommonVertexPy*: Klasse für Reparaturaktionen an Formen. [commit 4b44c54c](https://github.com/FreeCAD/FreeCAD/commit/4b44c54c)
-   *ShapeFix_SplitToolPy*: Werkzeug zum Trennen und Beschneiden von Kanten.[commit bbecc3f2](https://github.com/FreeCAD/FreeCAD/commit/bbecc3f2)
-   *ShapeFix_WireframePy*: Enthält Methoden zum Reparieren der (Draht-) Konturen von Formen.[commit 6843a461](https://github.com/FreeCAD/FreeCAD/commit/6843a461)
-   *ShapeFix_WirePy*: Klasse für Reparaturaktionen an Drähten. [commit 94f6279a](https://github.com/FreeCAD/FreeCAD/commit/94f6279a)
-   *ShapeFix_WireVertexPy*: Reparieren unverbundener Kanten in einem Draht.[commit 8c6ffc99](https://github.com/FreeCAD/FreeCAD/commit/8c6ffc99)


</div>



#### Entfernte Python API 

-   *FreeCAD.EndingAdd*: Ersetzt durch *FreeCAD.addImportType*. [Pull request #7167](https://github.com/FreeCAD/FreeCAD/pull/7167)
-   *FreeCAD.EndingGet*: Ersetzt durch *FreeCAD.getImportType*. [Pull request #7167](https://github.com/FreeCAD/FreeCAD/pull/7167)


</div>



## Addon-Manager 

-   Ein einfacher Python-Package-Manager, zum Aktualisieren und Entfernen automatisch installierter Abhängigkeiten, wurde hinzugefügt.
-   Ein \"developer mode\" wurde hinzugefügt, um die Erstellung der Metadaten-Datei zu unterstützen, die für jedes Addon benötigt wird.



## Arbeitsbereich Arch 

-   Einige [Arch Profil](Arch_Profile/de.md)-Kategorien wurden hinzugefügt: IS RHS, IS SHS, IS Angle und IS Tee. [Pull request #7181](https://github.com/FreeCAD/FreeCAD/pull/7181) und [Pull request #7217](https://github.com/FreeCAD/FreeCAD/pull/7217)
-   [Arch Profile](Arch_Profile/de.md)-Objekte unterstützen jetzt die Änderung der Profilart nach der Erstellung. [Pull request #7217](https://github.com/FreeCAD/FreeCAD/pull/7217)
-   Einige Probleme des Bearbeitungsmodus wurden beseitigt und die Kontextmenüs der [Baumansicht](Tree_view/de.md) für Arch-Objekte wurden verbessert. Objekte, die bearbeitet werden können, besitzen jetzt eine Option **Edit** in dem Menü. Die Option **Set colors** wurde für Objekte ohne Flächen bzw. die nur eine einzige Fläche besitzen können, entfernt. [Pull request #8122](https://github.com/FreeCAD/FreeCAD/pull/8122)
-   [Arch Schnittebenen](Arch_SectionPlane/de.md) (SectionPlane-Objekte) behandeln jetzt Objekte, die keine Festkörper sind, auf die gleiche Weise wie Festkörperobjekte.[Pull request #8688](https://github.com/FreeCAD/FreeCAD/pull/8688)



### Weitere Arch-Verbesserungen 

-   Das Werkzeug **Invert hinge position** (Scharnierposition umdrehen?) wurde verbessert. Für alle rechteckigen Drähte wird jetzt die gegenüberliegende Kante korrekt ermittelt. [Pull request #8199](https://github.com/FreeCAD/FreeCAD/pull/8199)
-   Das Gelände eines [Arch Grundstücks](Arch_Site/de.md) kann jetzt auch ein Festkörper sein. [Pull request #8409](https://github.com/FreeCAD/FreeCAD/pull/8409)
-   Ein [Arch Grundstück](Arch_Site.md) zeigt nicht länger eine Phantomdarstellung der Objekte in seiner Gruppe. [Pull request #8409](https://github.com/FreeCAD/FreeCAD/pull/8409)



## Arbeitsbereich Draft 

-   Die Ungenauigkeit von [Draft Snap Near](Draft_Snap_Near/de.md) während des Einrastens von Kurven wurde beseitigt. Außerdem kann [Draft Snap Perpendicular](Draft_Snap_Perpendicular/de.md) jetzt auch auf Flächen einrasten und vielfache Punkte finden. Zum Einrasten auf einem Knoten (z.B. einem [Draft Punkt](Draft_Point/de.md)) muss jetzt [Draft Snap Endpoint](Draft_Snap_Endpoint/de.md) anstatt [Draft Snap Near](Draft_Snap_Near/de.md) verwendet werden. [Pull request #7132](https://github.com/FreeCAD/FreeCAD/pull/7132)
-   Um das Arbeiten mit [Layern](Draft_Layer/de.md) zu vereinfachen, wurde ihr Drag-and-Drop-Verhalten geändert. Wenn jetzt ein Objekt aus einer [Std Gruppe](Std_Group/de.md) oder ein gruppenartiges Objekt, wie ein [Arch Gebäudeteilauf](Arch_BuildingPart/de.md) einen Layer abgelegt wird, wird es nicht mehr aus der Gruppe entfernt und umgekehrt. Dies funktioniert ohne das Gedrückthalten der **Ctrl**-Taste [Pull request #7462](https://github.com/FreeCAD/FreeCAD/pull/7462)
-   Der Befehl [Draft PointArray](Draft_PointArray/de.md) unterstützt jetzt mehr Punkt-Objektarten. Jedes Objekt mit einer Form und Knoten sowie [Netze](Mesh_Workbench/de.md) und [Punktewolken](Points_Workbench/de.md) kann verwendet werden. [Pull request #7597](https://github.com/FreeCAD/FreeCAD/pull/7597)
-   Die Kontextmenüs der [Baumansicht](Tree_view/de.md) von Draft-Objekten wurden verbessert. Objekte die mit dem Befehl [Draft Bearbeiten](Draft_Edit/de.md) bearbeitet werden können oder eine eigenes Bearbeitungswerkzeug besitzen, haben jetzt die Option **Bearbeiten** in ihrem Menü. Die Option **Set colors** für Objekte, die keine Flächen besitzen oder die nur eine einzige Fläche besitzen können, wurde entfernt. [Pull request #7970](https://github.com/FreeCAD/FreeCAD/pull/7970)
-   Die Eigenschaften der Draft-Annotation-Objekte wurden vereinheitlicht. Die Objekte [Draft Text](Draft_Text/de.md), [Draft Dimension](Draft_Dimension/de.md) und [Draft Label](Draft_Label/de.md) besitzen jetzt alle die Eigenschaften Schriftname (Font Name), Schrifthöhe (Font Size) und Textfarbe (Text Color). Die Optionen für den Ansichtsmodus wurden auch angeglichen und sind jetzt: Screen und World. [Issue #7861](https://github.com/FreeCAD/FreeCAD/issues/7861) und [Pull request #8081](https://github.com/FreeCAD/FreeCAD/pull/8081)
-   Im Aufgabenbereich des Befehls [Draft StilFestlegen](Draft_SetStyle/de.md) wurde die Schaltfläche **Texte/Maße?** durch die Schaltfläche **Anmerkungen** ersetzt. Das Anklicken dieser Schaltfläche bewirkt die #Bearbeitung aller Beschriftungselemente inklusive [Draft Notizen](Draft_Label/de.md). Die Parameter **Dim overshoot**, **Ext lines** und **Ext overshoot** wurden hinzugefügt. Es wurden auch einige kleinere Probleme behoben. [Pull request #8190](https://github.com/FreeCAD/FreeCAD/pull/8190), [Pull request #8195](https://github.com/FreeCAD/FreeCAD/pull/8195), [Pull request #8196](https://github.com/FreeCAD/FreeCAD/pull/8196) and [Pull request #9514](https://github.com/FreeCAD/FreeCAD/pull/9514).
-   Rückgängig/Wiederherstellen (Undo/Redo) funktionierte nicht vernünftig mit den Draft Änderungsbefehlen Windows. [Pull request #8267](https://github.com/FreeCAD/FreeCAD/pull/8267)
-   Der Befehl [LayerManager](Draft_LayerManager/de.md) wurde vom Arbeitsbereich BIM Workbench zum Arbeitsbereich Draft verschoben. [Pull request #8795](https://github.com/FreeCAD/FreeCAD/pull/8795)



### Weitere Draft-Verbesserungen 

-   Wurde die Arbeitsebene an einer Fläche ausgerichtet, wurde sie nur dann passend zu den globalen Achsen gedreht, wenn es sich um eine vierseitige Fläche handelte. [Pull request #7249](https://github.com/FreeCAD/FreeCAD/pull/7249)
-   Mehrere Probleme im Zusammenhang mit [Draft PfadAnordnung](Draft_PathArray/de.md) wurden behoben. [Pull request #7506](https://github.com/FreeCAD/FreeCAD/pull/7506) und [Pull request #7662](https://github.com/FreeCAD/FreeCAD/pull/7662)
-   Der Befehl [Draft Bearbeiten](Draft_Edit/de.md) erhielt einige Verbesserungen. Für For [Drähte](Draft_Wire/de.md), [B-Splines](Draft_BSpline/de.md) und [Bézier-Kurven](Draft_BezCurve/de.md) wurde eine Option Schließen/Öffnen zum Kontextmenü von (edge ?) hinzugefügt. Für B-splines und Bézier-Kurven wurde auch eine Option ? (Reverse) zu demselben Menü hinzugefüg. Die zugehörigen Aufgabenbereiche wurden aufgeräumt.[Pull request #7527](https://github.com/FreeCAD/FreeCAD/pull/7527) und [Pull request #7541](https://github.com/FreeCAD/FreeCAD/pull/7541)
-   Wird Esc zum Verlassen eines Befehls verwendet, wird der Fortsetzungsmodus jetzt nicht mehr ausgeschaltet. [Pull request #7611](https://github.com/FreeCAD/FreeCAD/pull/7611)
-   Die Symbolleiste [Draft Snap](Draft_Snap/de.md) wurde in eine Standard-Symbolleiste geändert. Den Fangoptionen können jetzt Tastaturkürzel zugeordnet werden. Aber die Verwendung während eines laufenden Befehls funktioniert nur, wenn der Fokus nicht auf einem der Eingabefelder in Aufgabenbereich liegt, da diese die so genannten In-Command-Shortcuts \"abfangen\". [Pull request #7656](https://github.com/FreeCAD/FreeCAD/pull/7656)
-   Einige Fehler des [Draft Beschriftungsstil-Editors](Draft_AnnotationStyleEditor.md) wurden beseitigt. Die Parameter **Text color** und **Text spacing** wurden hinzugefügt.[Pull request #8207](https://github.com/FreeCAD/FreeCAD/pull/8207) und [Pull request #9702](https://github.com/FreeCAD/FreeCAD/pull/9702)
-   Die Eigenschaften Start und End Offset wurden zur Pfad-Anordnung ([Draft PathArray](Draft_PathArray/de.md)-Objekt) hinzugefügt. [Pull request #8295](https://github.com/FreeCAD/FreeCAD/pull/8295)
-   Eine Eigenschaft Count (Anzahl) wurde den Anordnungen hinzugefügt, denen diese noch fehlte: die Versionen ohne Link von [Draft RechtwinkligeAnordnung](Draft_OrthoArray/de.md), [Draft PolareAnordnung](Draft_PolarArray.md) und [Draft KreisförmigeAnordnung](Draft_CircularArray/de.md). [Pull request #8433](https://github.com/FreeCAD/FreeCAD/pull/8433)
-   Das An-/Ausschaltverhalten des [Rasters](Draft_Snap_Grid/de.md) wurde korrigiert. [Pull request #8818](https://github.com/FreeCAD/FreeCAD/pull/8818)
-   Die Bedienung des DWG-Konverters wurde verbessert. [Pull request #9444](https://github.com/FreeCAD/FreeCAD/pull/9444) und [Pull request #9830](https://github.com/FreeCAD/FreeCAD/pull/9830)



## Arbeitsbereich FEM 

   
  <img alt="" src=images/FEM_PostFilterContours_relnotes_0.21.png  style="width:384px;">Iso-Kurven, die die Y-Komponente der absoluten magnetischen Flussdichte innerhalb und außerhalb eines Kupferdrahtes zeigen, durch den ein elektrischer Strom mit einer Frequenz von 100 kHz fließt.Für weitere Informationen zu diesem Modell, siehe Abschnitt 14 des [Elmer Tutorials](https://www.nic.funet.fi/index/elmer/doc/ElmerTutorials.pdf).   Es gibt den neuen Filter <img alt="" src=images/FEM_PostFilterContours.svg  style="width:24px;"> [NachbearbeitungFilterKonturen](FEM_PostFilterContours/de.md), der es ermöglicht Iso-Linien oder Iso-Konturen zu zeichnen. Iso-Konturen sind verbundene Netzknoten mit demselben Wert für die resultierende Feldstärke. Ein typisches Beispiel sind die elektrischen Feldlinien. [Pull request #8462](https://github.com/FreeCAD/FreeCAD/pull/8462)
   

   
  <img alt="" src=images/FEM_Elmer-Multithread_relnotes_0.21.png  style="width:384px;">Simulationsergebnis (fließendes Wasser, das erhitzt wird), das 8 Netzregionen zeigt (eine für jeden verwendeten CPU-Kern).   Es ist jetzt möglich, dass der Löser [Elmer](FEM_SolverElmer/de.md) während der Berechnung mehrere CPU-Kerne verwendet. Weitere Infos zu Vorsichtsmaßnahmen (? caveats), siehe [diesen Forum-Post](https://forum.freecadweb.org/viewtopic.php?p=610617#p610617) [Pull request #7159](https://github.com/FreeCAD/FreeCAD/pull/7159)
   

   
  <img alt="" src=images/FEM_EquationMagnetodynamic2D_relnotes_0.21.png  style="width:300px;">Simulationsergebnis des imaginären Anteils derStrömungsdichte in einem Tiegel (crucible), der miteiner umgebenden Spule elektrisch aufgeheizt wurde.Dieses Modell ist in den [FEM-Beispielen](FEM_Examples/de.md) enthalten.Für weitere Informationen zu diesem Modell, siehe Abschnitt 16 des [Elmer Tutorials](https://www.nic.funet.fi/index/elmer/doc/ElmerTutorials.pdf).   Die <img alt="" src=images/FEM_EquationMagnetodynamic2D.svg  style="width:24px;"> [Magnetodynamische 2D-Gleichung](FEM_EquationMagnetodynamic2D/de.md) wurde hinzugefügt. Mit dieser ist es möglich eine elektromagnetische Simulation in 2D durchzuführen. [Pull request #8355](https://github.com/FreeCAD/FreeCAD/pull/8355)
   

   
  <img alt="" src=images/FEM_EquationMagnetodynamic_relnotes_0.21.png  style="width:384px;">Simulationsergebnis des imaginären Anteils der magnetischenFlussdichte innerhalb und außerhalb eines Kupferdrahtes, durch den ein elektrischer Strom mit einer Frequenz von100 kHz fließt.Dieses Modell ist in den [FEM-Beispielen](FEM_Examples/de.md) enthalten.Für weitere Informationen zu diesem Modelll, siehe Abschnitt 14 des [Elmer Tutorials](https://www.nic.funet.fi/index/elmer/doc/ElmerTutorials.pdf).   Die <img alt="" src=images/FEM_EquationMagnetodynamic.svg  style="width:24px;"> [Magnetodynamische Gleichung](FEM_EquationMagnetodynamic/de.md) wurde hinzugefügt. Mit dieser ist es möglich, elektromagnetische Simulationen durchzuführen. [Pull request #8380](https://github.com/FreeCAD/FreeCAD/pull/8380)
   

   
  <img alt="" src=images/FEM_EquationDeformation_relnotes_0.21.png  style="width:384px;">Simulationsergebnis eines U-Drahtes aus Eisen, der verformt wird  durch das Zusammendrücken der beiden U-Enden.Für weitere Informationen über dieses Modell, siehe Abschnitt 8 des [Elmer-Tutorials](https://www.nic.funet.fi/index/elmer/doc/ElmerTutorials.pdf).   Die <img alt="" src=images/FEM_EquationDeformation.svg  style="width:24px;"> [Verformungsgleichung](FEM_EquationDeformation/de.md) wurde hinzugefügt. Damit ist es möglich Nichtlineare-Elastizitätsanalysen (Verformung) durchzuführen. [Pull request #8981](https://github.com/FreeCAD/FreeCAD/pull/8981)
   



### Weitere FEM-Verbesserungen 

-   Wird eine Analyse mit dem Löser <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;"> [CalculiX](FEM_SolverCalculixCxxtools/de.md) durchgeführt, wird jetzt auch eine [Ergebnis-Pipeline](FEM_PostPipelineFromResult/de.md) zur Darstellung der Ergebnisse erstellt.[Pull request #8525](https://github.com/FreeCAD/FreeCAD/pull/8525) und [Pull request #8903](https://github.com/FreeCAD/FreeCAD/pull/8903)
-   Es können jetzt auch [transient analyses](FEM_SolverElmer_SolverSettings#Timestepping_(transient_analyses).md) durchgeführt werden, wenn der Löser <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Elmer](FEM_SolverElmer/de.md) verwendet wird. [Pull request #9056](https://github.com/FreeCAD/FreeCAD/pull/9056)
-   Die <img alt="" src=images/FEM_ConstraintInitialPressure.svg  style="width:24px;"> [StartbedingungDruck](FEM_ConstraintInitialPressure/de.md) wurde hinzugefügt, um einen Startwert für den inneren Druck eines Fluids festzulegen. [Pull request #7364](https://github.com/FreeCAD/FreeCAD/pull/7364)
-   Die <img alt="" src=images/FEM_ConstraintCurrentDensity.svg  style="width:24px;"> [RandbedingungStromdichte](FEM_ConstraintCurrentDensity/de.md) wurde hinzugefügt, um die Stromdichte für Körper und Flächen festzulegen. [Pull request #8348](https://github.com/FreeCAD/FreeCAD/pull/8348)
-   Die <img alt="" src=images/FEM_ConstraintMagnetization.svg  style="width:24px;"> [RandbedingungMagnetisierung](FEM_ConstraintMagnetization/de.md) wurde hinzugefügt, um die Magnetisierung von Körper und Flächen festzulegen. [Pull request #8393](https://github.com/FreeCAD/FreeCAD/pull/8393)
-   Die <img alt="" src=images/FEM_ConstraintFlowVelocity.svg  style="width:24px;"> [RandbedingungStrömungsgeschwindigkeit](FEM_ConstraintFlowVelocity/de.md) und die <img alt="" src=images/FEM_ConstraintInitialFlowVelocity.svg  style="width:24px;"> [StartbedingungStrömungsgeschwindigkeit](FEM_ConstraintInitialFlowVelocity/de.md) wurden komplett überarbeitet. Es ist jetzt auch möglich, eine Geschwindigkeit durch eine mathematische Formel anzugeben (um ein Geschwindigkeitsprofil festzulegen). [Pull request #8963](https://github.com/FreeCAD/FreeCAD/pull/8963) und [Pull request #8964](https://github.com/FreeCAD/FreeCAD/pull/8964)**Hinweis:** Dies bricht mit alten Abläufen. Analyse mit existierenden Rand- und Startbedingungen für Strömungsgeschwindigkeiten werden nicht mehr funktionieren. Sie müssen in der Analyse neu erstellt werden, damit vorhandene Analysen wieder funktionieren.**Noch ein Hinweis:** bis FreeCAD 0.21 waren die Ergebnisse des Strömungslösers falsch (Fluid-Dichte und -Viskosität waren um den Faktor 1000 zu hoch). Die notwendige Neuerstellung der Randbedingung für die Geschwindigkeit sorgt jetzt auch dafür, dass die Ergebnisse korrekt sind.
-   Es ist jetzt auch möglich, in der <img alt="" src=images/FEM_ConstraintDisplacement.svg  style="width:24px;"> [RandbedingungVersatz](FEM_ConstraintDisplacement/de.md) die Versatzwerte als Ausdrücke anzugeben (Versatz zum aktuellen Löser-Zeitpunkt).
-   Die <img alt="" src=images/FEM_ConstraintBodyHeatSource.svg  style="width:24px;"> [RandbedingungKörperwärmequelle](FEM_ConstraintBodyHeatSource/de.md) besitzt jetzt einen Aufgaben-Bereich und es ist möglich, die Wärme für mehrere Körper festzulegen oder mehrere Randbedingungen für unterschiedliche Körper in einer Analyse zu verwenden. [Pull request #7367](https://github.com/FreeCAD/FreeCAD/pull/7367)
-   Die <img alt="" src=images/FEM_ConstraintSpring.svg  style="width:24px;"> [RandbedingungFeder](FEM_ConstraintSpring/de.md) wurde von keinem Löser verwendet. Jetzt kann sie mit dem Löser [Elmer](FEM_SolverElmer/de.md) durch die Gleichungen für [Verformung](FEM_EquationDeformation/de.md) und [Elastizität](FEM_EquationElasticity.md) verwendet werden. [Pull request #9005](https://github.com/FreeCAD/FreeCAD/pull/9005)
-   Die Ergebnisnetz-Schnittfunktion <img alt="" src=images/FEM_PostCreateFunctionCylinder.svg  style="width:24px;"> [NachbereitungFunktionZylinder](FEM_PostCreateFunctionCylinder/de.md) wurde hinzugefügt.[Pull request #8735](https://github.com/FreeCAD/FreeCAD/pull/8735)
-   Die Ergebnisnetz-Schnittfunktion <img alt="" src=images/FEM_PostCreateFunctionBox.svg  style="width:24px;"> [NachbereitungFunktionQuader](FEM_PostCreateFunctionBox/de.md) wurde hinzugefügt.[Pull request #8825](https://github.com/FreeCAD/FreeCAD/pull/8825)
-   Es ist jetzt auch möglich, \*.pvtu-Dateien (partitioned VTK unstructured grid data) zu öffnen (und auf diesem Weg anzuzeigen) . Eine \*.pvtu-Datei ist auch das Ergebnis einer [Elmer](FEM_SolverElmer/de.md)-Simulation, wenn mehr als ein CPU-Kern für Berechnungen verwendet wird. [Pull request #7159](https://github.com/FreeCAD/FreeCAD/pull/7159)
-   Critical Strain Ratio (\<- ?) wurde zur VTK-Ergebnis-Pipeline hinzugefügt. Es gibt ein indication of ductile rupture (\<- ?) für Werkstoffe mit einem \"MaterialMechanicalNonlinear\"-Objekt. [Pull request #7467](https://github.com/FreeCAD/FreeCAD/pull/7467)
-   <img alt="" src=images/FEM_FemMesh2Mesh.svg  style="width:24px;"> [FEM FemNetzZuNetz](FEM_FemMesh2Mesh/de.md) hat den neuen Parameter *scale* zum Festlegen des Maßstabes verformter Netze mit Python.[Forum thread](https://forum.freecadweb.org/viewtopic.php?f=18&t=71936) und [Pull request #7715](https://github.com/FreeCAD/FreeCAD/pull/7715)
-   Die [Einstellungen](FEM_Preferences/de.md) haben eine neue Option zum Festlegen, welcher Löser automatisch hinzugefügt werden soll, wenn eine neue Analyse erstellt wird.
    -   Befindet man sich im Arbeitsbereich FEM, wenn man eine FreeCAD-Datei lädt, die eine Analyse enthält, dann wird die Analyse automatisch aktiviert (man erhält sofort Zugriff auf alle Schaltflächen der FEM-Symbolleiste).
    -   Die Symbolleiste enthält nur Schaltflächen für auf dem System installierte Löser. Nicht zur Verfügung stehende Löser werden nicht mehr angezeigt.
-   Neue Beispieldateien für die folgenden Gleichungen sind in den [FEM Beispielen](FEM_Examples/de.md) vorhanden: [Verformung](FEM_EquationDeformation/de.md), [Strömung](FEM_EquationFlow/de.md), [Fluss](FEM_EquationFlux/de.md), [Wärme](FEM_EquationHeat/de.md), [Magnetodynamik](FEM_EquationMagnetodynamic/de.md) and [ 2D-Magnetodynamik](FEM_EquationMagnetodynamic2D/de.md). Pull requests [#8550](https://github.com/FreeCAD/FreeCAD/pull/8550), [#8569](https://github.com/FreeCAD/FreeCAD/pull/8569), [#8579](https://github.com/FreeCAD/FreeCAD/pull/8579), [#8597](https://github.com/FreeCAD/FreeCAD/pull/8597), [#8630](https://github.com/FreeCAD/FreeCAD/pull/8630) und [#9004](https://github.com/FreeCAD/FreeCAD/pull/9004).
-   Neue Werkstoffkarten für Kohlen(stoff)dioxyd und eine Titanlegierung. [Pull request #8332](https://github.com/FreeCAD/FreeCAD/pull/8332) und [Pull request #8636](https://github.com/FreeCAD/FreeCAD/pull/8636)

## Mesh

-   Unterstützung für das Hinzufügen von Transparenzen zu einem Netzobjekt. [Forum thread](https://forum.freecadweb.org/viewtopic.php?f=22&t=72531) und [Commit f88305e](https://github.com/FreeCAD/FreeCAD/commit/f88305e)



## Arbeitsbereich Part 

-   Der Befehl [Part PointsFromMesh](Part_PointsFromMesh/de.md) wurde erweitert, um beliebige geometrische Objekte als Eingabe zu akzeptieren.[Pull request #8730](https://github.com/FreeCAD/FreeCAD/pull/8730)



## Arbeitsbereich PartDesign 

   
  <img alt="" src=images/PD_Counterdrill_relnotes_0.21.png  style="width:384px;">Loch mit Senkbohrung.   Der Dialog [Bohrung](PartDesign_Hole/de.md) unterstützt den Bohrlochtyp *Senkbohrung* (Counterdrill). [Pull request #7562](https://github.com/FreeCAD/FreeCAD/pull/7562)
                                                                                                                               
   

+++
| <img alt="" src=images/PartDesign_task_dialog_relnotes_0.21.png  style="width:384px;"> | Die Bedienung vieler PartDesign-Aufgaben-Dialoge zum Auswählen von Geometrien wurde verbessert; die separaten Schaltflächen zum Hinzufügen und Entfernen von Geometrien sind nicht länger erforderlich. [Pull request #8990](https://github.com/FreeCAD/FreeCAD/pull/8990) |
+++
|                                                                                                       |                                                                                                                                                                                                                                                                            |
+++



### Weitere PartDesign-Verbesserungen 

-   Im Dialog [Bohrung](PartDesign_Hole/de.md) wurden die veralteten Schraubenkopfarten entfernt (cheese head, cap screw etc.). Sie sind seit FreeCAD 0.19 veraltet. Bohrungen die diese Arten verwenden werden in benutzerdefinierte Bohrungen mit Kegelsenkung bzw. Zylindersenkung umgewandelt und übernehmen dabei die Werte für Durchmesser und Tiefe. [Pull request #7654](https://github.com/FreeCAD/FreeCAD/pull/7654)
-   In den Dialogen von [Loft](PartDesign_AdditiveLoft/de.md) und [Subtraktives Loft](PartDesign_SubtractiveLoft.md), erstellt die bisher funktionslose Option **Geschlossen** jetzt ein geschlossenes (ringförmiges) Loft. [Pull request #8748](https://github.com/FreeCAD/FreeCAD/pull/8748)
-   Der Befehl [SkizzeÜberprüfen](Sketcher_ValidateSketch/de.md) wurde der Helper-Symbolleiste hinzugefügt. [Pull request #7700](https://github.com/FreeCAD/FreeCAD/pull/7700)
-   Die unnützen Befehle [SkizzeVerlassen](Sketcher_LeaveSketch/de.md) und [SkizzeAnzeigen](Sketcher_ViewSketch/de.md) wurden aus dem Menü entfernt. Die Befehle [SkizzeBearbeiten](Sketcher_EditSketch/de.md), [SkizzenZusammenführen](Sketcher_MergeSketches/de.md) und [Skizze spiegeln](Sketcher_MirrorSketch/de.md) wurden dem Menü hinzugefügt. [Pull request #7700](https://github.com/FreeCAD/FreeCAD/pull/7700)
-   Das [Evolventenzahnprofil](PartDesign_InvoluteGear/de.md) hat neue Eigenschaften zum Einstellen der Zahnhöhe erhalten. Damit können jetzt verschiedene Eingriffsarten festgelegt werden und auch (Evolventen-)Verzahnungen (z.B. für verschiebbare Welle-Nabe-Verbindungen) erstellt werden. Siehe [involute splines](https://en.wikipedia.org/wiki/Spline_(mechanical)) (engl.). [Pull request #8184](https://github.com/FreeCAD/FreeCAD/pull/8184)
-   Das [Evolventen-Zahnprofil](PartDesign_InvoluteGear/de.md) ermöglicht jetzt auch Profilverschiebung. [Issue #5618](https://github.com/FreeCAD/FreeCAD/issues/5618) und [Pull request #8934](https://github.com/FreeCAD/FreeCAD/pull/8934)
-   Wird ein [Klon](PartDesign_Clone/de.md) erstellt, übernimmt er jetzt die Farben des geklonten Objekts. [Pull request #9547](https://github.com/FreeCAD/FreeCAD/pull/9547)



## Arbeitsbereich Path 

-   Integration von Camotics. Ist Camotics (Version 1.2.2 oder neuer) installiert, wird ein neues Symbol zur Path-Symbolleiste hinzugefügt. Nach Auswahl eines Path-Jobs die Schaltfläche drücken, um den Camotics-Dialog zu öffnen. Danach den Schieberegler ziehen, um einen beliebigen Zeitpunkt der Simulation des Festkörpers darzustellen. You can also launch the full camotics application to run the animated simulaton. This results in a silent post-processing of the job and creation of a camotics project file. [Pull request #6637](https://github.com/FreeCAD/FreeCAD/pull/6637)

-   Zusätzliche \"substitution strings\" für eine automatische Benennung der Ausgabe. Wenn die Ausgabe auf mehrere Dateien aufgeteilt wird, können die Dateinamen automatisch die \"toolcontroller label, Work Coordinate Systems (WCS), oder operation label\" ersetzen. Dies ergänzt die anderen \"substitution strings\" wie Datum, Job-Name usw.

-   Eine Option Spanbrechen wurde für \"Pilgerschritt-\"(Peck-Style) Bohrungszyklen hinzugefügt. Spanbrechen gibt einen G73-Zyklus aus, der die Steuerung veranlasst, einen sehr kleinen Rückschritt auszuführen, um den Span zu brechen, ohne das Bohr-Bit komplett aus der Bohrung zu ziehen. G73 wird nativ von LinuxCNC unterstützt. Einige andere Postprozessoren müssen den G73 interpretieren und geeignete Steuercodes ausgeben oder die Rückschritte in G1/G0 Bewegungen aufgegliedert werden. Unterstützung für G73-Aufgliederung wurde für die \"refactored\" Postprozessoren hinzugefügt.[Pull request #7469](https://github.com/FreeCAD/FreeCAD/pull/7469)



## Arbeitsbereich Sketcher 

   
  <img alt="" src=images/Constrain_B-spline_knots_relnotes_0.21.gif  style="width:384px;">Ziehen von B-Spline-Knoten.Bild anklicken, um die Animation anzusehen.   B-Spline-Knoten können jetzt herumgezogen und durch Randbedingungen bestimmt werden, wie jeder andere Skizzenpunkt auch. [Pull request #7484](https://github.com/FreeCAD/FreeCAD/pull/7484)
                                                                                                                                                                                                                
   

   
  <img alt="" src=images/sketcher-move-piece_relnotes_0.21.gif  style="width:384px;">Ziehen eines B-Splines.Bild anklicken, wenn die Animation nicht automatisch startet.   Ziehen an einem B-Spline bewegt jetzt nur den Teil zwischen den (angrenzenden) Knoten. [Pull request #7110](https://github.com/FreeCAD/FreeCAD/pull/7110)
                                                                                                                                                                                                                    
   

   
  <img alt="" src=images/Sketcher_Join_Curves_relnotes_0.21.gif  style="width:384px;">Bild anklicken, um die Animation anzusehen.   Das Werkzeug [Kurven verbinden](Sketcher_JoinCurves/de.md) wurde hinzugefügt. Es kann zwei Kurven zu einem einzigen B-Spline zusammensetzen. [Pull request #6507](https://github.com/FreeCAD/FreeCAD/pull/6507)
                                                                                                                                                               
   

   
  <img alt="" src=images/Sketcher_BackEdit_relnotes_0.21.gif  style="width:384px;">Bild anklicken, um die Animation anzusehen.   Skizzen können jetzt ohne Unterbrechung von der Vorder- oder Rückseite her bearbeitet werden. Arbeitet man von der Rückseite aus, sind Punkte (und alle Geometrien und Randbedingungen) gleichermaßen auswählbar und die Schnittansicht wird automatisch umgestellt. [Pull request #7417](https://github.com/FreeCAD/FreeCAD/pull/7417)
                                                                                                                                                         
   

+++
| <img alt="" src=images/Sketcher_Grid_Rework_relnotes_0.21.png  style="width:384px;"> | Das Sketcher-Raster wurde überarbeitet. Das Werkzeug [Raster](Sketcher_Grid/de.md) wurde hinzugefügt. Eine Option zur automatischen Größenanpassung wurde hinzugefügt. [Pull request #8473](https://github.com/FreeCAD/FreeCAD/pull/8473) |
+++
|                                                                                                   |                                                                                                                                                                                                                                                   |
+++

+++
| <img alt="" src=images/Sketcher_Constraint_Widget_relnotes_0.21.png  style="width:384px;"> | Das Sketcher-Constraint-Widget wurde überarbeitet um die Benutzerschnittstelle (UI) zu vereinfachen. [Pull request #7566](https://github.com/FreeCAD/FreeCAD/pull/7566) |
+++
|                                                                                                               |                                                                                                                                                                         |
+++

   
  <img alt="" src=images/Sketcher_Element_Widget_relnotes_0.21.gif  style="width:384px;">Bild anklicken, um die Animation anzusehen.   Das Element-Widget wurde überarbeitet, um die Benutzerschnittstelle (UI) zu vereinfachen und eine einfachere Auswahl der unterschiedlichen Bestandteile jeder Geometrie zu ermöglichen: Kante, Startpunkt, Endpunkt und Mittelpunkt. [Pull request #7567](https://github.com/FreeCAD/FreeCAD/pull/7567)
                                                                                                                                                                     
   

+++
| <img alt="" src=images/Sketcher_Grid_relnotes_0.21.gif  style="width:384px;"> | Eine Funkion zur automatischen Größenanpassung des Rasters in Abhängigkeit von der Darstellungsgröße (zoom level) und andere Verbesserungen wurden vorgestellt. [Pull request #8473](https://github.com/FreeCAD/FreeCAD/pull/8473) |
+++
|                                                                                     |                                                                                                                                                                                                                                    |
+++

+++
| <img alt="" src=images/Sketcher_layers_relnotes_0.21.gif  style="width:384px;"> | Eine grundlegende Funktionalität für Darstellungsebenen (visual layers) wurde vorgestellt; erst einmal werden 3 festeingestellte Ebenen unterstützt. Weitere Verbesserungen sind schon unterwegs. Dieser PR entfernt auch das Widget \"Edit controls\" aus dem Aufgabenbereich, da seine Inhalte an andere Orte verlegt oder entfernt wurden. Die Einstellungsmöglichkeit für die Render-Reihenfolge wurde in die Symbolleiste Sketcher edit tools verlegt. [Pull request #8716](https://github.com/FreeCAD/FreeCAD/pull/8716) und [Pull request #9590](https://github.com/FreeCAD/FreeCAD/pull/9590) |
+++
|                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+++

+++
| <img alt="" src=images/Sketcher_Circle2CircleConstraint_relnotes_0.21.png  style="width:384px;"> | Der Kreis-zu-Kreis-Abstand wurde der Randbedingung [AbstandFestlegen](Sketcher_ConstrainDistance/de.md) hinzugefügt. [Pull request #8896](https://github.com/FreeCAD/FreeCAD/pull/8896) |
+++
|                                                                                                                           |                                                                                                                                                                                                 |
+++

+++
| <img alt="" src=images/Sketcher_Circle2LineConstraint_relnotes_0.21.png  style="width:384px;"> | Der Kreis-zu-Linie-Abstand wurde der Randbedingung [AbstandFestlegen](Sketcher_ConstrainDistance/de.md) hinzugefügt. [Pull request #9044](https://github.com/FreeCAD/FreeCAD/pull/9044) |
+++
|                                                                                                                       |                                                                                                                                                                                                 |
+++

   
  <img alt="" src=images/Sketcher-snap2_relnotes_0.21.gif  style="width:384px;">Bild anklicken, um die Animation anzusehen.   Snap-Manager zum Fangen und Einrasten auf Winkeln und Mittelpunkten wurden hinzugefügt. [Pull request #8387](https://github.com/FreeCAD/FreeCAD/pull/8387)
                                                                                                                                                   
   

+++
| <img alt="" src=images/Sketcher-concentric_relnotes_0.21.gif  style="width:384px;"> | Die Randbedingung [Koinzidenz festlegen](Sketcher_ConstrainCoincident/de.md) funktioniert jetzt auch als Randbedingung Konzentrisch festlegen, wenn 2 oder mehr Kreise, Bögen, Ellipsen oder Ellipsenbögen ausgewählt wurden. [Pull request #7703](https://github.com/FreeCAD/FreeCAD/pull/7703) |
+++
|                                                                                                 |                                                                                                                                                                                                                                                                                                          |
+++

+++
| <img alt="" src=images/Sketcher-B-spline_by_knots_v2_relnotes_0.21.gif  style="width:384px;"> | Das Werkzeug [B-Spline durch Knoten](Sketcher_CreateBSplineByInterpolation/de.md) wurde hinzugefügt. [Pull request #8530](https://github.com/FreeCAD/FreeCAD/pull/8530) |
+++
|                                                                                                                     |                                                                                                                                                                                 |
+++

+++
| <img alt="" src=images/Sketcher-periodic_B-spline_by_knots_v2_relnotes_0.21.gif  style="width:384px;"> | Das Werkzeug [Geschlossener B-Spline durch Knoten](Sketcher_CreatePeriodicBSplineByInterpolation/de.md) wurde hinzugefügt. [Pull request #8530](https://github.com/FreeCAD/FreeCAD/pull/8530) |
+++
|                                                                                                                                       |                                                                                                                                                                                                       |
+++



### Weitere Sketcher-Verbesserungen 

-   Die Schaltfläche [Lichtbrechung (nach Snellius-Gesetz) festlegen](Sketcher_ConstrainSnellsLaw/de.md) wurde aus der Symbolleiste entfernt. [Commit ef62fc3](https://github.com/FreeCAD/FreeCAD/commit/ef62fc3)
-   [KanteTeilen](Sketcher_Split/de.md) unterstützt jetzt mehr Kurven (Ellipsen, Parabeln, Hyperbeln und B-Splines). [Pull request #6971](https://github.com/FreeCAD/FreeCAD/pull/6971)
-   Die [Maßlichen Randbedingungen](Sketcher_Workbench#Dimensional_constraints/de.md) und \"Quantity Spin-Boxes\" unterstützen dieselbe Berechnungsart wie [Ausdrücke](Expressions/de.md) (Auswertung vor Ort). [Pull Request #7124](https://github.com/FreeCAD/FreeCAD/pull/7124)
-   Die Schaltflächen [Überflüssige Randbedingungen auswählen](Sketcher_SelectRedundantConstraints/de.md) und [Widersprüchliche Randbedingungen auswählen](Sketcher_SelectConflictingConstraints/de.md) wurden aus der Symbolleiste entfernt.. [Pull request #7568](https://github.com/FreeCAD/FreeCAD/pull/7568)
-   Die Schaltfläche [Vorgang beenden](Sketcher_StopOperation/de.md) wurde aus der Symbolleiste entfernt. [Pull request #7569](https://github.com/FreeCAD/FreeCAD/pull/7569)
-   Die Schaltfläche [Unterbestimmte Elemente auswählen](Sketcher_SelectElementsWithDoFs/de.md) wurde aus der Symbolleiste entfernt. [Pull request #7603](https://github.com/FreeCAD/FreeCAD/pull/7603)
-   Die Symbolleiste des Sketchers wurde in zwei aufgeteilt: \'Sketcher-Edit Mode\' und \'Skizze\' (d.h. \'nicht der Edit-Mode\'). Die Sketcher-Symbolleisten für den Bearbeitungsmodus sind außerhalb des Bearbeitungsmodus ausgeblendet und jene für den Nicht-Bearbeitungsmodus sind im Bearbeitungsmodus ausgeblendet. Auch die Structure-Symbolleiste wird innerhalb des Sketchers ausgeblendet. [Pull request #7655](https://github.com/FreeCAD/FreeCAD/pull/7655)
-   Die Funktion [Pause](Sketcher_CarbonCopy/de.md) verwendet jetzt, wenn möglich, die Namen der Randbedingungen in den Ausdrücken, die sie erstellt, anstelle von indexbasierten Referenzen, was sie zuverlässiger macht. [Pull request #7688](https://github.com/FreeCAD/FreeCAD/pull/7688)
-   Das Werkzeug Interne Ausrichtung wurde entfernt. Es war veraltet seit der Einführung des Werkzeugs [InterneAusrichtungsgeometrieWiederherstellen](Sketcher_RestoreInternalAlignmentGeometry/de.md). [Pull request #8863](https://github.com/FreeCAD/FreeCAD/pull/8863)
-   Der Teil \'Meldungen des Lösers\' des Sketcher-Aufgabenbereichs wurde vereinfacht. Die Checkbox \'Automatisches Entfernen überflüssiger Randbedingungen\' wurde in das Schaltflächenmenü Einstellungen im Bereich Randbedingungen (Einschränkungen) verschoben. Die Checkbox Automatische Aktualisierung wurde in das Menü der Schaltfläche Aktualisieren verschoben.[Pull request #8864](https://github.com/FreeCAD/FreeCAD/pull/8864)



## Arbeitsbereich Surface 

+++
| <img alt="" src=images/Surface_BlendCurve_relnotes_0.21.png  style="width:250px;"> | Das Werkzeug [Blend Curve](Surface_BlendCurve/de.md) wurde hinzugefügt. [Pull request #7339](https://github.com/FreeCAD/FreeCAD/pull/7339) |
+++
|                                                                                               |                                                                                                                                                    |
+++



## Arbeitsbereich TechDraw 

+++
| <img alt="" src=images/TechDraw_SurfaceFinishExample_relnotes_0.21.png  style="width:250px;">           | Das Werkzeug [Oberflächensymbole](TechDraw_SurfaceFinishSymbols/de.md) wurde hinzugefügt, um das Erstellen von Oberflächensymbolen zu ermöglichen, die Rauheit, ? (lay) und Welligkeit beschreiben aber auch die Angaben zur Oberflächenbehandlung. Es unterstützt sowohl ISO- als auch ASME-Ausführungen. Wie im Bild gezeigt, kann das vorhandene Werkzeug [Hinweislinie](TechDraw_LeaderLine/de.md) verwendet werden, um ausgerichtete Symbole auf die Kanten eines Objekts zu beziehen. [Pull request #7227](https://github.com/FreeCAD/FreeCAD/pull/7227) |
+++
| <img alt="" src=images/TechDraw_ComplexSection_relnotes_0.21.png  style="width:250px;">                       | Das Werkzeug [KomplexerSchnitt](TechDraw_ComplexSection/de.md) wurde hinzugefügt, um das Erstellen von Halbschnitten, versetzten Schnitten und abgewinkelten Schnitten zu ermöglichen. [Pull request #7658](https://github.com/FreeCAD/FreeCAD/pull/7658)                                                                                                                                                                                                                                                                                                              |
+++
| <img alt="" src=images/TechDraw_HoleShaftFitExample_relnotes_0.21.png  style="width:250px;">             | Das Werkzeug [Passungen](TechDraw_HoleShaftFit/de.md) wurde hinzugefügt. [Pull request #8455](https://github.com/FreeCAD/FreeCAD/pull/8455)                                                                                                                                                                                                                                                                                                                                                                                                                            |
+++
| <img alt="" src=images/TechDraw_AxoLengthDimensionExample_relnotes_0.21.png  style="width:250px;"> | Das Werkzeug [AxonometrischesLängenmaß](TechDraw_AxoLengthDimension/de.md) wurde hinzugefügt. [Pull request #8359](https://github.com/FreeCAD/FreeCAD/pull/8359)                                                                                                                                                                                                                                                                                                                                                                                                       |
+++
|                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
+++



### Weitere TechDraw-Verbesserungen 

-   Die Navigations-Modi wurden aktualisiert und entsprechen den in der 3D-Ansicht benutzten.[Pull request #7081](https://github.com/FreeCAD/FreeCAD/pull/7081) und [Pull request #7107](https://github.com/FreeCAD/FreeCAD/pull/7107)
-   Bitmap-Schraffur wurde repariert. [Issue #6582](https://github.com/FreeCAD/FreeCAD/issues/6582) und [Pull request #7121](https://github.com/FreeCAD/FreeCAD/pull/7121)
-   Unterstützung für einstellbare Lücken der Maßhilfslinien von [Maßen](TechDraw_Preferences/de#Maßeinträge.md) wurde hinzugefügt. [Pull request #7133](https://github.com/FreeCAD/FreeCAD/pull/7133)
-   Multithreading wurde eingeführt für das Ausblenden verdeckter Kanten und das Finden von Flächen.[Pull request #7377](https://github.com/FreeCAD/FreeCAD/pull/7377)
-   Der Algorithmus zum Aufspühren von Flächen wurde verbessert. [Pull request #7448](https://github.com/FreeCAD/FreeCAD/pull/7448)
-   Das Werkzeug [AllesDrucken](TechDraw_PrintAll/de.md) wurde hinzugefügt. [Pull request #7460](https://github.com/FreeCAD/FreeCAD/pull/7460)
-   Vier Werkzeuge zur Steuerung der [Stapelreihenfolge](TechDraw_Workbench/de#Stapeln.md) von Ansichten wurden hinzugefügt.[Issue #6012](https://github.com/FreeCAD/FreeCAD/issues/6012) und [Pull request #7460](https://github.com/FreeCAD/FreeCAD/pull/7460)
-   Das Werkzeug [AktiveAnsicht](TechDraw_ActiveView/de.md) erstellt jetzt einen Screenshot anstatt einer SVG-Darstellung. [Pull request #7471](https://github.com/FreeCAD/FreeCAD/pull/7471)
-   Alle Vorlagen, die auf lateinischen Schriften basieren, wurden in \"plain svg\" konvertiert. [Pull request #7472](https://github.com/FreeCAD/FreeCAD/pull/7472)
-   Eine Vorschaufunktion wurde im Aufgabenbereich des Werkzeugs [Schnittansicht](TechDraw_SectionView/de.md) hinzugefügt. [Pull request #7658](https://github.com/FreeCAD/FreeCAD/pull/7658)
-   Veraltete DrawViewPart-Funktionen wurden entfernt: replaceCenterLine, replaceCosmeticEdge, replaceCosmeticVertex and replaceGeomFormat.
-   3D-Maße können jetzt auf die gleiche Art erstellt werden, wie 2D-Maße (abgesehen davon, dass die Geometrie in einer 3D-Ansicht ausgewählt werden muss). Dadurch entfällt das manuelle Verknüpfen mit der 3D-Geometrie. [Pull request #8141](https://github.com/FreeCAD/FreeCAD/pull/8141)
-   Das Werkzeug [MaßReparieren](TechDraw_DimensionRepair/de.md) wurde hinzugefügt. [Pull request #8141](https://github.com/FreeCAD/FreeCAD/pull/8141)
-   Eine Funktion zum entfernen von überlappenden Kanten, die vom Hidden-Line-Removal-Algorithmus zurückgegebeben werden, wurde hinzugefügt, inklusive einer neuen Einstellung (in den erweiterten Einstellungen) für die Anzahl der Durchgängen dieser Funktion.[Pull request #9280](https://github.com/FreeCAD/FreeCAD/pull/9280)



## Kompilieren

Seit dieser Ausgabe kann FreeCAD nur unter Verwendung von Qt 5.x und Python 3.x. kompiliert werden. Die niedrigste unterstützte Qt-Version ist 5.12, die niedrigste unterstützte Python-Version ist 3.8.

Die Anleitungen zum Kompilieren von FreeCAD gibt es für [Windows](Compile_on_Windows/de.md), [Linux](Compile_on_Linux/de.md) und [macOS](Compile_on_MacOS/de.md).

Die unterstützten Betriebssysteme sind:

-   Windows 7, 8, 10 und 11
-   Linux Ubuntu Focal Fossa (20.04) und newer
-   macOS: 10.12 Sierra oder neuer



### Bekannte Einschränkungen 

### 32bit Windows 

Seit FreeCAD 0.19 wird 32bit Windows nicht mehr offiziell unterstützt. FreeCAD kann auf solchen Systemen funktionieren, es wird aber keine Hilfestellung (mehr) dazu geben.



### Remote-Desktop unter Windows 

Abhängig von den OpenGL-Grafik-Fähigkeiten eines Rechners kann es vorkommen, dass FreeCAD abstürzt, wenn man es über Remote-Desktop ausführt. Dies lässt sich durch Aktualisieren des OpenGL-Treibers beheben. Nur wenn das nicht hilft:

-   [Diese](https://downloads.fdossena.com/geth.php?r=mesa64-latest) OpenGL-Bibliothek für 64bit-Windows herunterladen und extrahieren.
-   Die DLL-Datei zu *opengl32sw.dll* umbenennen und in das Unterverzeichnis *bin* in FreeCADs Installationsverzeichnis kopieren (die dort existierende DLL überschreiben).



### macOS: Arbeitsbereich Start zeigt eine leere Seite 

Zeigt der Arbeitsbereich [Start](Start_Workbench/de.md) nur eine leere Seite, muss die Einstellung **Software OpenGL verwenden** im Menü **FreeCAD-0.21 → Einstellungen → Anzeige** aktiviert werden.



## Andere Quellen 

-   [Mango Jelly Video über 0.21 Merkmale](https://www.youtube.com/watch?v=rPxr0yvNgxo)



---
⏵ [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 0.21/de
