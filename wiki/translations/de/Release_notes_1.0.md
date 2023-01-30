# Release notes 1.0/de
**FreeCAD 1.0 ist in Entwicklung, es steht noch kein Veröffentlichungstermin fest.**


{{Message|
Fehlen Funktionen? Das spricht man am besten im Forumsbeitrag [https://forum.freecadweb.org/viewtopic.php?f&#61;10&t&#61;69438 Release notes for v1.0] an.

Siehe [FreeCAD Unterstützen](Help_FreeCAD/de.md) für Möglichkeiten etwas zu FreeCAD beizutragen.}}


{{Message|Alle Bilder auf dieser Seite müssen das Suffix **_relnotes_1.0** tragen.}}


{{TOCright}}

**FreeCAD 1.0** wurde am **DD MM 2023** veröffentlicht, es kann von der [Download](Download/de.md)-Seite heruntergeladen werden. Diese Seite listet alle Neuerungen und Änderungen auf.

Ältere FreeCAD-Versionshinweise findet man in der [Funktionsliste](Feature_list/de#Versionshinweise.md).

Platzhalter für ein auffälliges Bild, das von den Admins im [user showcases forum](https://forum.freecadweb.org/viewforum.php?f=24) ausgesucht wird.



## Allgemein



## Benutzeroberfläche

   
  ![](images/Navi_Cube_relnotes_1.0.gif )   Die Ecken des Navigationswürfels sind jetzt sechseckig und größer, dadurch sind sie einfacher anzuklicken. [Pull request #7876](https://github.com/FreeCAD/FreeCAD/pull/7876).
   

   
  <img alt="" src=images/Measurement-Part_relnotes_1.0.png  style="width:384px;">   Die Darstellungsart von [Messergebnissen](Part_Workbench/de#Messung.md), die in den Arbeitsbereichen [Part](Part_Workbench/de.md) oder [PartDesign](PartDesign_Workbench/de.md) erstellt wurden, können jetzt in den [Einstellungen](PartDesign_Preferences/de#Measure.md) angepasst werden. [Pull request #7148](https://github.com/FreeCAD/FreeCAD/pull/7148)
   

   
  <img alt="" src=images/WbSelector_relnotes_1.0.png  style="width:300px;">   Das Auswahlfeld für Arbeitsbereiche kann jetzt wahlweise in die Menüleiste gelegt werden, anstatt im Bereich der Symbolleisten. [Pull request #7679](https://github.com/FreeCAD/FreeCAD/pull/7679)
   



### Weitere Verbesserungen der Benutzeroberfläche 

-   Die Schaltfläche für den <img alt="" src=images/Std_UserEditModeDefault.svg  style="width:24px;"> [Bearbeitungsmodus](Std_UserEditMode/de.md) wurde aus der Standard-Symbolleiste entfernt. Sie kann erneut hinzugefügt werden, indem man eine eigene Symbolleiste [anpasst](Std_DlgCustomize/de.md).[Pull request #7570](https://github.com/FreeCAD/FreeCAD/pull/7570)
-   Die Schaltflächen für <img alt="" src=images/Std_Print.svg  style="width:24px;"> [Drucken](Std_Print/de.md), <img alt="" src=images/Std_Copy.svg  style="width:24px;"> [Kopieren](Std_Copy/de.md), <img alt="" src=images/Std_Paste.svg  style="width:24px;"> [Einfügen](Std_Paste/de.md) und <img alt="" src=images/Std_Cut.svg  style="width:24px;"> [Ausschneiden](Std_Cut/de.md) wurden aus der Standard-Symbolleiste entfernt. Sie können erneut hinzugefügt werden, indem man eine eigene Symbolleiste [anpasst](Std_DlgCustomize/de.md).[Pull request #7571](https://github.com/FreeCAD/FreeCAD/pull/7571) und [commit ea9a04e](https://github.com/FreeCAD/FreeCAD/commit/ea9a04e)
-   Befehle zum [Speichern](Std_StoreWorkingView/de.md) und [Abrufen](Std_RecallWorkingView/de.md) temporärer Arbeitsansichten wurden hinzugefügt. [Pull request #7525](https://github.com/FreeCAD/FreeCAD/pull/7525)
-   Das Ändern der Werte mit dem Mausrad in Eingabefeldern (eine Widget-Art, die verwendet wird, um Werte im Aufgabenbereich einzugeben, z.B. von [Draft Linie](Draft_Line/de.md)) ist deaktiviert, wenn der Fokus nicht auf dem Widget liegt und der Schalter [ComboBoxWheelEventFilter](Fine-tuning.md) aktiviert ist. Dies verhindert ungewollte Wertveränderungen während des Scrollens, wie schon bei Spin- und Combo-Boxen. [Pull request #7561](https://github.com/FreeCAD/FreeCAD/pull/7561)
-   Es ist jetzt möglich, eine Standardeinstellung für die Transparenz neu erstellter [Part-](Part_Module/de.md) oder [PartDesign-](PartDesign_Workbench/de.md) Objekte in den [Einstellungen](PartDesign_Preferences/de.md) festzulegen. [Pull request #7103](https://github.com/FreeCAD/FreeCAD/pull/7103)
-   Es gibt einen neuen Orbit-Stil **Free Turntable**. Er kann im [Voreinstellungseditor](Preferences_Editor/de#Navigation.md) aktiviert werden oder durch Drücken der Schaltfläche **[<img src=images/NavigationCAD_dark.svg style="width:16px">** in der [Statusleiste](Status_bar/de.md) and then using the menu **Settings → Orbit**). [Pull request #8048](https://github.com/FreeCAD/FreeCAD/pull/8048)
-   Der Aufgabenbereich [Std Darstellung](Std_SetAppearance/de.md) besitzt jetzt eine Schaltfläche zum Festlegen der Eigenschaft Point-Color. [Pull request #7708](https://github.com/FreeCAD/FreeCAD/pull/7708)
-   Eine Schaltfläche zum wechseln der Farben des Hintergrundverlaufs der [3D-Ansicht](3D_view/de.md) wurde im [Voreinstellungseditor](Preferences_Editor/de#Farben.md) hinzugefügt. [Pull request #7155](https://github.com/FreeCAD/FreeCAD/pull/7155)
-   Alle Transparenzeinstellungen verwenden jetzt einheitlich eine Schrittweite von 5% für Spin-Buttons: Ein Klick auf die Schaltfläche in einem Dialog oder dem [Eigenschafteneditor](Property_editor/de.md) ändert die Transparenz um 5%. Wird die Schaltfläche gedrückt gehalten, werden mehrere 5%-Schritte auf einmal ausgeführt. [Pull request #7723](https://github.com/FreeCAD/FreeCAD/pull/7723)
-   Das Ausgabefenster (Output window) wurde in ??? (Report view) geändert, zur Vereinheitlichung (mit) der Benutzerschnittstelle (UI). [Pull Request #7739](https://github.com/FreeCAD/FreeCAD/pull/7739)



## Kernsystem und API 



### Kern

### API


<div class="mw-collapsible mw-collapsed toccolours">



#### Neue Python API 


<div class="mw-collapsible-content">

-   *BSplineSurfacePy::scaleKnotsToBounds*: Skaliert die Listen der U- und V-Knoten, um sie in die vorgegebenen Grenzen einzupassen. [Pull request #7258](https://github.com/FreeCAD/FreeCAD/pull/7258) und [Pull request #7385](https://github.com/FreeCAD/FreeCAD/pull/7385)
-   *BSplineCurvePy::scaleKnotsToBounds*: Skaliert die Knotenliste, um sie in die vorgegebenen Grenzen einzupassen. [Pull request #7385](https://github.com/FreeCAD/FreeCAD/pull/7385)

-   *ShapeFix_EdgeConnectPy*: Root class for fixing operations. [commit 4d4adb93](https://github.com/FreeCAD/FreeCAD/commit/4d4adb93)
-   *ShapeFix_EdgePy*: Fixing invalid edge. [commit 4089cbfb](https://github.com/FreeCAD/FreeCAD/commit/4089cbfb)
-   *ShapeFix_FaceConnectPy*: Rebuilds connectivity between faces in shell. [commit a0eb2e9d](https://github.com/FreeCAD/FreeCAD/commit/a0eb2e9d)
-   *ShapeFix_FacePy*: Class for fixing operations on faces. [commit b6cd635c](https://github.com/FreeCAD/FreeCAD/commit/b6cd635c)
-   *ShapeFix_FixSmallFacePy*: Class for fixing operations on faces. [commit 4c2946c8](https://github.com/FreeCAD/FreeCAD/commit/4c2946c8)
-   *ShapeFix_FixSmallSolidPy*: Fixing solids with small size. [commit b70d8d37](https://github.com/FreeCAD/FreeCAD/commit/b70d8d37)
-   *ShapeFix_FreeBoundsPy*: Intended to output free bounds of the shape. [commit 1ee1aee1](https://github.com/FreeCAD/FreeCAD/commit/1ee1aee1)
-   *ShapeFix_RootPy*: Root class for fixing operations. [commit f3e941a3](https://github.com/FreeCAD/FreeCAD/commit/f3e941a3)
-   *ShapeFix_ShapePy*: Class for fixing operations on shapes. [commit 87db9dcc](https://github.com/FreeCAD/FreeCAD/commit/87db9dcc)
-   *ShapeFix_ShapeTolerancePy*: Modifies tolerances of sub-shapes (vertices, edges, faces). [commit 125d5b63](https://github.com/FreeCAD/FreeCAD/commit/125d5b63)
-   *ShapeFix_ShellPy*: Root class for fixing operations. [commit f3e941a3](https://github.com/FreeCAD/FreeCAD/commit/f3e941a3)
-   *ShapeFix_SolidPy*: Root class for fixing operations. [commit 8d568793](https://github.com/FreeCAD/FreeCAD/commit/8d568793)
-   *ShapeFix_SplitCommonVertexPy*: Class for fixing operations on shapes. [commit 4b44c54c](https://github.com/FreeCAD/FreeCAD/commit/4b44c54c)
-   *ShapeFix_SplitToolPy*: Tool for splitting and cutting edges. [commit bbecc3f2](https://github.com/FreeCAD/FreeCAD/commit/bbecc3f2)
-   *ShapeFix_WireframePy*: Provides methods for fixing wireframe of shape. [commit 6843a461](https://github.com/FreeCAD/FreeCAD/commit/6843a461)
-   *ShapeFix_WirePy*: Class for fixing operations on wires. [commit 94f6279a](https://github.com/FreeCAD/FreeCAD/commit/94f6279a)
-   *ShapeFix_WireVertexPy*: Fixing disconnected edges in the wire. [commit 8c6ffc99](https://github.com/FreeCAD/FreeCAD/commit/8c6ffc99)


</div>



#### Entfernte Python API 

-   *FreeCAD.EndingAdd*: Ersetzt durch *FreeCAD.addImportType*. [Pull request #7167](https://github.com/FreeCAD/FreeCAD/pull/7167)
-   *FreeCAD.EndingGet*: Ersetzt durch *FreeCAD.getImportType*. [Pull request #7167](https://github.com/FreeCAD/FreeCAD/pull/7167)


</div>



## Addon-Manager 



## Arbeitsbereich Arch 

-   Einige Probleme des Bearbeitungsmodus wurden beseitigt und die Kontextmenüs der [Baumansicht](Tree_view/de.md) für Arch-Objekte wurden verbessert. Objekte, die bearbeitet werden können, besitzen jetzt eine Option **Edit** in dem Menü. Die Option **Set colors** wurde für Objekte ohne Flächen bzw. die nur eine einzige Fläche besitzen können, entfernt. [Pull request #8122](https://github.com/FreeCAD/FreeCAD/pull/8122)



### Weitere Arch-Verbesserungen 

-   [Profile](Arch_Profile/de.md)-Objekte unterstützen jetzt die Änderung der Profilart nach der Erstellung. [Pull request #7217](https://github.com/FreeCAD/FreeCAD/pull/7217)



## Arbeitsbereich Draft 

-   Die Ungenauigkeit von [Draft Snap Near](Draft_Snap_Near/de.md) während des Einrastens von Kurven wurde beseitigt. Außserdem kann [Draft Snap Perpendicular](Draft_Snap_Perpendicular/de.md) jetzt auch auf Flächen einrasten und vielfache Punkte finden. Zum Einrasten auf einem Knoten (z.B. einem [Draft Punkt](Draft_Point/de.md)) muss jetzt [Draft Snap Endpoint](Draft_Snap_Endpoint/de.md) anstatt [Draft Snap Near](Draft_Snap_Near/de.md) verwendet werden. [Pull request #7132](https://github.com/FreeCAD/FreeCAD/pull/7132)
-   Um das Arbeiten mit [Layern](Draft_Layer/de.md) zu vereinfachen, wurde ihr Drag-and-Drop-Verhalten geändert. Wenn jetzt ein Objekt aus einer [Std Gruppe](Std_Group/de.md) oder ein gruppenartiges Objekt, wie ein [Arch Gebäudeteilauf](Arch_BuildingPart/de.md) einen Layer abgelegt wird, wird es nicht mehr aus der Gruppe entfernt und umgekehrt. Dies funktioniert ohne das Gedrückthalten der **Ctrl**-Taste [Pull request #7462](https://github.com/FreeCAD/FreeCAD/pull/7462)
-   Der Befehl [Draft PointArray](Draft_PointArray/de.md) unterstützt jetzt mehr Punkt-Objektarten. Jedes Objekt mit einer Form und Knoten sowie [Netze](Mesh_Workbench/de.md) und [Punktewolken](Points_Workbench/de.md) kann verwendet werden. [Pull request #7597](https://github.com/FreeCAD/FreeCAD/pull/7597)
-   Die Kontextmenüs der [Baumansicht](Tree_view/de.md) von Draft-Objekten wurden verbessert. Objekte die mit dem Befehl [Draft Bearbeiten](Draft_Edit/de.md) bearbeitet werden können oder eine eigenes Bearbeitungswerkzeug besitzen, haben jetzt die Option **Bearbeiten** in ihrem Menü. Die Option **Set colors** für Objekte, die keine Flächen besitzen oder die nur eine einzige Fläche besitzen können, wurde entfernt. [Pull request #7970](https://github.com/FreeCAD/FreeCAD/pull/7970)

-   Die Eigenschaften der Draft-Annotation-Objekte wurden vereinheitlicht. Die Objekte [Draft Text](Draft_Text/de.md), [Draft Dimension](Draft_Dimension/de.md) und [Draft Label](Draft_Label/de.md) besitzen jetzt alle die Eigenschaften Schriftname (Font Name), Schrifthöhe (Font Size) und Textfarbe (Text Color). Die Optionen für den Ansichtsmodus wurden auch angeglichen und sind jetzt: Screen und World. [Issue #7861](https://github.com/FreeCAD/FreeCAD/issues/7861) und [Pull request #8081](https://github.com/FreeCAD/FreeCAD/pull/8081)



### Weitere Draft-Verbesserungen 

-   Several [Draft PathArray](Draft_PathArray.md) related issues have been fixed. [Pull request #7506](https://github.com/FreeCAD/FreeCAD/pull/7506) and [Pull request #7662](https://github.com/FreeCAD/FreeCAD/pull/7662)
-   The [Draft Edit](Draft_Edit.md) command has received several improvements. For [wires](Draft_Wire.md), [B-splines](Draft_BSpline.md) and [Bézier curves](Draft_BezCurve.md) a Close/Open option has been added to the edge context menu. For B-splines and Bézier curves a Reverse option has been added to the same menu as well. The task panels have been cleaned up. [Pull request #7527](https://github.com/FreeCAD/FreeCAD/pull/7527) and [Pull request #7541](https://github.com/FreeCAD/FreeCAD/pull/7541)
-   The [Draft Snap](Draft_Snap.md) toolbar was changed to a standard toolbar. Keyboard shortcuts can now be assigned to snaps. But using them during a command only works if none of the input boxes in the task panel has the focus as they \'catch\' the so-called in-command shortcuts. [Pull request #7656](https://github.com/FreeCAD/FreeCAD/pull/7656)
-   In the task panel of the [Draft SetStyle](Draft_SetStyle.md) command the \"Texts/dims\" button has been replaced by the \"Annotations\" button. Pressing this button will process all annotations, including [Draft Labels](Draft_Label.md). Several minor additional issues were also fixed. [Pull request #8190](https://github.com/FreeCAD/FreeCAD/pull/8190), [Pull request #8195](https://github.com/FreeCAD/FreeCAD/pull/8195) and [Pull request #8196](https://github.com/FreeCAD/FreeCAD/pull/8196)



## Arbeitsbereich FEM 

   
  <img alt="" src=images/FEM_Elmer-Multithread_relnotes_1.0.png  style="width:384px;">Simulation result where 8 mesh regions are visible (one for every CPU core used).   It is now possible to run the solver [Elmer](FEM_SolverElmer.md) using multiple CPU cores. For more info about the caveats, see [this forum post](https://forum.freecadweb.org/viewtopic.php?p=610617#p610617) [Pull request #7159](https://github.com/FreeCAD/FreeCAD/pull/7159)
   



### Weitere FEM-Verbesserungen 

-   There is now an <img alt="" src=images/FEM_ConstraintInitialPressure.svg  style="width:24px;"> [initial pressure constraint](FEM_ConstraintInitialPressure.md) to set the initial internal pressure of fluids. [Pull request #7364](https://github.com/FreeCAD/FreeCAD/pull/7364)
-   The <img alt="" src=images/FEM_ConstraintBodyHeatSource.svg  style="width:24px;"> [body heat source constraint](FEM_ConstraintBodyHeatSource.md) now has a task panel and it is possible to set the heat for several bodies or to use several constraints for different bodies in one analysis. [Pull request #7367](https://github.com/FreeCAD/FreeCAD/pull/7367)
-   It is now possible to open (and this way visualize) \*.pvtu files (partitioned VTK unstructured grid data). A \*.pvtu file is also the result of an [Elmer](FEM_SolverElmer.md) simulation, when more than one CPU core was used. [Pull request #7159](https://github.com/FreeCAD/FreeCAD/pull/7159)
-   Critical Strain Ratio has been added to the VTK result pipeline. It gives an indication of ductile rupture for materials with a \"MaterialMechanicalNonlinear\" object. [Pull request #7467](https://github.com/FreeCAD/FreeCAD/pull/7467)
-   <img alt="" src=images/FEM_FemMesh2Mesh.svg  style="width:24px;"> [FEM mesh to mesh](FEM_FemMesh2Mesh.md) enables to define the scale of deformed mesh using Python. [Forum thread](https://forum.freecadweb.org/viewtopic.php?f=18&t=71936) and [Pull request #7715](https://github.com/FreeCAD/FreeCAD/pull/7715)

## Export

## Mesh



### Weitere Mesh-Verbesserungen 

-   Unterstützung für das Hinzufügen von Transparenzen zu einem Netzobjekt. [Forum thread](https://forum.freecadweb.org/viewtopic.php?f=22&t=72531) und [Commit f88305e](https://github.com/FreeCAD/FreeCAD/commit/f88305e)



## Arbeitsbereich OpenSCAD 



## Arbeitsbereich Part 



### Weitere Part-Verbesserungen 



## Arbeitsbereich PartDesign 

   
  <img alt="" src=images/PD_Counterdrill_relnotes_1.0.png  style="width:384px;">Loch mit Senkbohrung.   Der Dialog [Bohrung](PartDesign_Hole/de.md) unterstützt den Bohrlochtyp *Senkbohrung* (Counterdrill). [Pull request #7562](https://github.com/FreeCAD/FreeCAD/pull/7562)
                                                                                                                             
   



### Weitere PartDesign-Verbesserungen 

-   Im Dialog [Bohrung](PartDesign_Hole/de.md) wurden die veralteten Schraubenkopfarten entfernt (cheese head, cap screw etc.). Sie sind seit FreeCAD 0.19 veraltet. Bohrungen die diese Arten verwenden werden in benutzerdefinierte Bohrungen mit Kegelsenkung bzw. Zylindersenkung umgewandelt und übernehmen dabei die Werte für Durchmesser und Tiefe. [Pull request #7654](https://github.com/FreeCAD/FreeCAD/pull/7654)
-   Der Befehl [SkizzeÜberprüfen](Sketcher_ValidateSketch/de.md) wurde der Helper-Symbolleiste hinzugefügt. [Pull request #7700](https://github.com/FreeCAD/FreeCAD/pull/7700)
-   Die unnützen Befehle [SkizzeVerlassen](Sketcher_LeaveSketch/de.md) und [SkizzeAnzeigen](Sketcher_ViewSketch/de.md) wurden aus dem Menü entfernt. Die Befehle [SkizzeBearbeiten](Sketcher_EditSketch/de.md), [SkizzenZusammenführen](Sketcher_MergeSketches/de.md) und [Skizze spiegeln](Sketcher_MirrorSketch/de.md) wurden dem Menü hinzugefügt. [Pull request #7700](https://github.com/FreeCAD/FreeCAD/pull/7700)



## Arbeitsbereich Pfad 

-   Integration von Camotics. Ist Camotics (Version 1.2.2 oder neuer) installiert, wird ein neues Symbol zur Path-Symbolleiste hinzugefügt. Nach Auswahl eines Path-Jobs die Schaltfläche drücken, um den Camotics-Dialog zu öffnen. Danach den Schieberegler ziehen, um einen beliebigen Zeitpunkt der Simulation des Festkörpers darzustellen. You can also launch the full camotics application to run the animated simulaton. This results in a silent post-processing of the job and creation of a camotics project file. [Pull request #6637](https://github.com/FreeCAD/FreeCAD/pull/6637)

-   Additional substitution strings for automatic output naming. If output is being split into multiple files, the filenames can automatically substitute the toolcontroller label, WCS, or operation label. This is in addition to the other existing substitution strings like date, job name, etc.

-   Implemented Chipbreaking option for peck style drill cycles. Chipbreaking emits a G73 cycle which causes the control to make a very small retraction move to break the chip without fully retracting the bit from the hole. G73 is supported natively by LinuxCNC. Some other postprocessors will have to interpret the G73 and emit control appropriate codes or decompose the retraction into G1/G0 moves. Postprocessor support for G73 decomposition has been added to the \"refactored\" postprocessors.[Pull request #7469](https://github.com/FreeCAD/FreeCAD/pull/7469)



## Modul Plot 



## Arbeitsbereich Sketcher 

   
  <img alt="" src=images/Constrain_B-spline_knots_relnotes_1.0.gif  style="width:384px;">Ziehen von B-Spline-Knoten.Bild anklicken, um die Animation anzusehen.   B-Spline-Knoten können jetzt herumgezogen und durch Randbedingungen bestimmt werden, wie jeder andere Skizzenpunkt auch. [Pull request #7484](https://github.com/FreeCAD/FreeCAD/pull/7484)
                                                                                                                                                                                                              
   

   
  <img alt="" src=images/sketcher-move-piece_relnotes_1.0.gif  style="width:384px;">Ziehen eines B-Splines.Bild anklicken, wenn die Animation nicht automatisch startet.   Ziehen an einem B-Spline bewegt jetzt nur den Teil zwischen den (angrenzenden) Knoten. [Pull request #7110](https://github.com/FreeCAD/FreeCAD/pull/7110)
                                                                                                                                                                                                                  
   

   
  <img alt="" src=images/Sketcher_BackEdit_relnotes_1.0.gif  style="width:384px;">Bild anklicken, um die Animation anzusehen.   Möglichkeit Skizzen ohne Unterbrechung von der Vorder- oder Rückseite her zu bearbeiten. Arbeitet man von der Rückseite aus, sind Punkte (und alle Geometrien und Randbedingungen) gleichermaßen auszahlbar und die Schnittansicht wird automatisch umgestellt. [Pull request #7417](https://github.com/FreeCAD/FreeCAD/pull/7417)
                                                                                                                                                       
   

   
  <img alt="" src=images/Sketcher_Element_Widget_relnotes_1.0.gif  style="width:384px;">Bild anklicken, um die Animation anzusehen.   Das Element-Widget wurde überarbeitet, um die Benutzerschnittstelle (UI) zu vereinfachen und eine einfachere Auswahl der unterschiedlichen Bestandteile jeder Geometrie zu ermöglichen: Kante, Startpunkt, Endpunkt und Mittelpunkt. [Pull request #7567](https://github.com/FreeCAD/FreeCAD/pull/7567)
                                                                                                                                                                   
   

   
  <img alt="" src=images/Sketcher_Join_Curves_relnotes_1.0.gif  style="width:384px;">Bild anklicken, um die Animation anzusehen.   Das Werkzeug [Kurven verbinden](Sketcher_JoinCurves/de.md) wurde hinzugefügt. Es kann verschiedene Kurven zu einem einzigen B-Spline zusammensetzen. [Pull request #6507](https://github.com/FreeCAD/FreeCAD/pull/6507)
                                                                                                                                                             
   



### Weitere Sketcher-Verbesserungen 

-   Die Schaltfläche [Lichtbrechung (nach Snellius-Gesetz) festlegen](Sketcher_ConstrainSnellsLaw/de.md) wurde aus der Symbolleiste entfernt. [Commit ef62fc3](https://github.com/FreeCAD/FreeCAD/commit/ef62fc3)
-   The [Maßlichen Randbedingungen](Sketcher_Workbench#Dimensional_constraints/de.md) und \"Quantity Spin-Boxes\" unterstützen dieselbe Berechnungsart wie [Ausdrücke](Expressions/de.md) (Auswertung vor Ort). [Pull Request #7124](https://github.com/FreeCAD/FreeCAD/pull/7124)
-   Die Schaltflächen [Überflüssige Randbedingungen auswählen](Sketcher_SelectRedundantConstraints/de.md) und [Widersprüchliche Randbedingungen auswählen](Sketcher_SelectConflictingConstraints/de.md) wurden aus der Symbolleiste entfernt.. [Pull request #7568](https://github.com/FreeCAD/FreeCAD/pull/7568)
-   Die Schaltfläche [Vorgang beenden](Sketcher_StopOperation/de.md) wurde aus der Symbolleiste entfernt. [Pull request #7569](https://github.com/FreeCAD/FreeCAD/pull/7569)
-   Der Abschnitt \'Bedienelemente bearbeiten\' im Sketcher-Dialog ist jetzt optional. [Pull request #7572](https://github.com/FreeCAD/FreeCAD/pull/7572)
-   Die Schaltfläche [Unterbestimmte Elemente auswählen](Sketcher_SelectElementsWithDoFs/de.md) wurde aus der Symbolleiste entfernt. [Pull request #7603](https://github.com/FreeCAD/FreeCAD/pull/7603)
-   Die Symbolleiste des Sketchers wurde in zwei aufgeteilt: \'Sketcher-Edit Mode\' und \'Skizze\' (d.h. \'nicht der Edit-Mode\'). Die Sketcher-Symbolleisten für den Bearbeitungsmodus sind außerhalb des Bearbeitungsmodus ausgeblendet und jene für den Nicht-Bearbeitungsmodus sind im Bearbeitungsmodus ausgeblendet. Auch die Structure-Symbolleiste wird innerhalb des Sketchers ausgeblendet. [Pull request #7655](https://github.com/FreeCAD/FreeCAD/pull/7655)
-   Die Randbedingung [Koinzidenz festlegen](Sketcher_ConstrainCoincident/de.md) funktioniert jetzt auch als Randbedingung Konzentrisch festlegen, wenn 2 oder mehr Kreise, Bögen, Ellipsen oder Ellipsenbögen ausgewählt wurden. [Pull request #7703](https://github.com/FreeCAD/FreeCAD/pull/7703)
-   Die Funktion [Pause](Sketcher_CarbonCopy/de.md) verwendet jetzt, wenn möglich, die Namen der Randbedingungen in den Ausdrücken, die sie erstellt, anstelle von indexbasierten Referenzen, was sie zuverlässiger macht. [Pull request #7688](https://github.com/FreeCAD/FreeCAD/pull/7688)



## Arbeitsbereich Spreadsheet 



### Weitere Spreadsheet-Verbesserungen 



## Arbeitsbereich TechDraw 

   
  <img alt="" src=images/TechDraw_SurfaceFinishExample_relnotes_1.0.png  style="width:250px;">   The [SurfaceFinishSymbol](TechDraw_SurfaceFinishSymbol.md) tool was added to allow for the creation of surface finish symbols describing roughness, lay and waviness, but also denoting the type of surface treatment. It supports both ISO and ASME styles. As shown in the image, the existing [LeaderLine](TechDraw_LeaderLine.md) tool can be used to properly refer oriented symbols to the edges of an object. [Pull request #7227](https://github.com/FreeCAD/FreeCAD/pull/7227)
  <img alt="" src=images/TechDraw_ComplexSection_relnotes_1.0.png  style="width:250px;">               The [ComplexSection](TechDraw_ComplexSection.md) tool was added. [Pull request #7658](https://github.com/FreeCAD/FreeCAD/pull/7658)
                                                                                                                      
   



### Weitere TechDraw-Verbesserungen 

-   Navigation modes have been updated to match those used in the 3D view. [Pull request #7081](https://github.com/FreeCAD/FreeCAD/pull/7081) and [Pull request #7107](https://github.com/FreeCAD/FreeCAD/pull/7107)
-   Bitmap hatching was fixed. [Issue #6582](https://github.com/FreeCAD/FreeCAD/issues/6582) and [Pull request #7121](https://github.com/FreeCAD/FreeCAD/pull/7121)
-   Support for adjustable gaps for extension lines of [dimensions](TechDraw_Preferences#Dimensions.md) was added. [Pull request #7133](https://github.com/FreeCAD/FreeCAD/pull/7133)
-   Multithreading was introduced for hidden line removal and face finding. [Pull request #7377](https://github.com/FreeCAD/FreeCAD/pull/7377)
-   The face detection algorithm was improved. [Pull request #7448](https://github.com/FreeCAD/FreeCAD/pull/7448)
-   The [PrintAll](TechDraw_PrintAll.md) tool was added. [Pull request #7460](https://github.com/FreeCAD/FreeCAD/pull/7460)
-   [Four tools](TechDraw_StackGroup.md) to control the stacking order of views were added. [Issue #6012](https://github.com/FreeCAD/FreeCAD/issues/6012) and [Pull request #7460](https://github.com/FreeCAD/FreeCAD/pull/7460)
-   [ActiveView](TechDraw_ActiveView.md) now creates a screen capture instead of an SVG image. [Pull request #7471](https://github.com/FreeCAD/FreeCAD/pull/7471)
-   All Latin script templates have been converted to \"plain svg\". [Pull request #7472](https://github.com/FreeCAD/FreeCAD/pull/7472)
-   A preview was added to the task panel of the [SectionView](TechDraw_SectionView.md) tool. [Pull request #7658](https://github.com/FreeCAD/FreeCAD/pull/7658)
-   Removed deprecated functions: DrawViewPart::replaceCenterLine, DrawViewPart::replaceCosmeticEdge, DrawViewPart::replaceCosmeticVertex and DrawViewPart::replaceGeomFormat.

## Web



## Externe Arbeitsbereiche 

### A2plus

### Assembly3

### Assembly4

### FCGear

### Ship

## Compilation

Since this release FreeCAD can only be compiled using Qt 5.x and Python 3.x. The lowest supported Python version is 3.8 according to the [FreeCAD 1.0 development goals](FreeCAD_1.0_Development_Cycle.md).

To compile FreeCAD see the instructions for [Windows](Compile_on_Windows.md), [Linux](Compile_on_Linux.md) and [MacOS](Compile_on_MacOS.md).

The supported operating systems are:

-   Windows 7, 8, 10 and 11
-   Linux Ubuntu Focal Fossa (20.04) and newer
-   MacOS: 10.12 Sierra or newer



### Bekannte Einschränkungen 

### 32bit Windows 

Seit FreeCAD 0.19 wird 32bit Windows nicht mehr offiziell unterstützt. FreeCAD kann auf solchen Systemen funktionieren, es wird aber keine Hilfestellung (mehr) dazu geben.

### Remote Desktop under Windows 

Depending on the OpenGL graphics capabilities of a computer, it might be that one encounters a crash when running FreeCAD via remote desktop. To fix this upgrade your OpenGL driver. Only if this doesn\'t help:

-   Download [this](https://downloads.fdossena.com/geth.php?r=mesa64-latest) OpenGL library for 64bit Windows and extract it.
-   Rename the DLL file to *opengl32sw.dll* and copy it to the *bin* subfolder of FreeCAD\'s installation folder (overwrite the existing DLL there).



### MacOS: Arbeitsbereich Start zeigt eine leere Seite 

Zeigt der Arbeitsbereich [Start](Start_Workbench/de.md) nur eine leere Seite, muss die Einstellung **Software OpenGL verwenden** im Menü **Edit → Einstellungen → Anzeige** aktiviert werden.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 1.0/de
