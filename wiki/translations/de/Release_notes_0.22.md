# Release notes 0.22/de
**FreeCAD 0.22 ist in Entwicklung, es steht noch kein Veröffentlichungstermin fest.**


{{Message|
Fehlen Funktionen? Das spricht man am besten im Forumsbeitrag [https://forum.freecadweb.org/viewtopic.php?f&#61;10&t&#61;80197 Release notes for v0.22] an.

Siehe [FreeCAD Unterstützen](Help_FreeCAD/de.md) für Möglichkeiten etwas zu FreeCAD beizutragen.}}


{{Message|Alle Bilder auf dieser Seite müssen das Suffix **_relnotes_0.22** tragen.}}




**FreeCAD 0.22** wurde am **T Monat 2024** veröffentlicht, es kann von der [Download](Download/de.md)-Seite heruntergeladen werden. Diese Seite listet alle Neuerungen und Änderungen auf.

Ältere FreeCAD-Versionshinweise findet man in der [Funktionsliste](Feature_list/de#Versionshinweise.md).

Platzhalter für ein auffälliges Bild, das von den Admins im [user showcases forum](https://forum.freecadweb.org/viewforum.php?f=24) ausgesucht wird.



## Allgemein



## Benutzeroberfläche

+++
| <img alt="" src=images/Rotation_Center_Indicator_relnotes_0.22.gif  style="width:320px;"> | Ein Indikator für das Drehzentrum wurde hinzugefügt. Dieser Indikator wird angezeigt, wenn die Ansicht durch Ziehen mit der Maus gedreht wird. Er kann wahlweise in den Voreinstellungen deaktiviert werden. Außerdem gibt es Einstellungen für seine Farbe, Transparenz und Größe. [Pull-Request #9909](https://github.com/FreeCAD/FreeCAD/pull/9909) und [Pull-Request #10790](https://github.com/FreeCAD/FreeCAD/pull/10790) |
+++

   
  <img alt="" src=images/Selection_filters_relnotes_0.22.gif  style="width:320px;">Klick auf das Bild, wenn die Animation nicht automatisch startet.   Auswahlfilter wurden hinzugefügt; und grenzen die Auswahl auf Knoten, Kanten oder Flächen ein. [Pull-Request #10271](https://github.com/FreeCAD/FreeCAD/pull/10271)
   

+++
| <img alt="" src=images/Tasks_Dockable_relnotes_0.22.png  style="width:320px;"> | Für mehr Flexibilität ist der Aufgaben-Bereich jetzt ein eigenständiges, andockbares Widget, aber das alte Layout wird als Voreinstellung beibehalten. [Pull-Request #10681](https://github.com/FreeCAD/FreeCAD/pull/10681) und [Pull-Request #10848](https://github.com/FreeCAD/FreeCAD/pull/10848) |
+++

+++
| <img alt="" src=images/Transform_tool_relnotes_0.22.png  style="width:320px;"> | Die Darstellung der Anfasser des Werkzeugs [Bewegen](Std_TransformManip/de.md) wurde verbessert. Es besitzt jetzt auch drei Ebenen-Anfasser, um Objekte entlang der 3 Hauptebenen zu bewegen. [Pull-Request #10706](https://github.com/FreeCAD/FreeCAD/pull/10706) |
+++

+++
| <img alt="" src=images/Overlay_relnotes_0.22.png  style="width:320px;"> | Realthunders Funktion, die das Überlagern von Dock-Widgets ermöglicht (Baum- und Aufgaben-Transparenz) wurde hinzugefügt. [Pull-Request #7888](https://github.com/FreeCAD/FreeCAD/pull/7888) |
+++

+++
| <img alt="" src=images/Light_source_relnotes_0.22.PNG  style="width:320px;"> | Die Lichtquelle kann jetzt in den Voreinstellungen eingestellt werden (Einstellungen\... → Anzeige). [Pull-Request #11146](https://github.com/FreeCAD/FreeCAD/pull/11146) |
+++

+++
| <img alt="" src=images/Preference_tree_relnotes_0.22.png  style="width:320px;"> | Das Voreinstellungsfenster wurde übrearbeitet um die Karteitreiter durch eine Baumstruktur zu ersetzen. [Pull-Request #11018](https://github.com/FreeCAD/FreeCAD/pull/11018) |
+++



### Weitere Verbesserungen der Benutzeroberfläche 

-   Es wurde ein \"project unit system\" eingeführt. [Pull-Request #9521](https://github.com/FreeCAD/FreeCAD/pull/9521)
-   Das Werkzeug [Part Schnittansicht](Part_SectionCut/de.md) funktioniert jetzt auch in einer perspektivischen Ansicht. [Pull-Request #10143](https://github.com/FreeCAD/FreeCAD/pull/10143)
-   Eine Option zum alphabetischen Sortieren von Arbeitsbereichen wurde hinzugefügt (steht nach einem Rechtsklick in Einstellungen → Arbeitsbereiche zur Verfügung). [Pull-Request #10363](https://github.com/FreeCAD/FreeCAD/pull/10363)
-   Ein Filter **Datei suchen** und ein Filter **In Datei suchen** wurden zum Dialog [Std DlgMakroAusführen](Std_DlgMacroExecute/de.md) hinzugefügt. [Pull-Request #10714](https://github.com/FreeCAD/FreeCAD/pull/10714)
-   Das [Menü Ansicht](Std_View_Menu/de.md) und die Symbolleiste Ansicht wurden überarbeitet. [Pull-Request #10761](https://github.com/FreeCAD/FreeCAD/pull/10761)
-   Die Stop-Schaltfläche wurde aus der [Makro](Macros/de.md)-Symbolleiste entfernt. Die Schaltfläche [Makro aufzeichnen\...](Std_DlgMacroRecord/de.md) Wandelt sich jetzt in eine Stop-Schaltfläche, während ein Makro aufgezeichnet wird. [Pull-Request #10836](https://github.com/FreeCAD/FreeCAD/pull/10836)
-   Die Reset-Schaltfläche in den Voreinstellungen zeigt jetzt ein Menü an, das Optionen für das Zurücksetzen der Einstellungen auf unterschiedlichen Ebenen enthält: alle, die der aktuellen Gruppe oder die im aktuellen Menüreiter. [Pull-Request #10688](https://github.com/FreeCAD/FreeCAD/pull/10688) and [Pull-Request #11038](https://github.com/FreeCAD/FreeCAD/pull/11038)
-   Das Hilfe-Modul wurde integriert und muss nicht länger als Addon heruntergeladen werden, um es zu benutzen.[Pull-Request #11008](https://github.com/FreeCAD/FreeCAD/pull/11008)
-   Einstellungen zum Anpassen des aktuellen Themas wurden hinzugefügt. [Pull-Request #10238](https://github.com/FreeCAD/FreeCAD/pull/10238)
-   Die Standardeinstellungen für Auswahlen wurden geändert, um das Auswählen von Objekten in der 3D-Ansicht zu vereinfachen. [Pull-Request #11187](https://github.com/FreeCAD/FreeCAD/pull/11187)
-   Ein Einheitenschema **Meter dezimal** wurde hinzugefügt, da das MKS-System (m/kg/s/Grad) nicht immer Maßangaben in Metern anzeigt - Größen unter 0,1 m werden auch noch in Millimetern angezeigt, obwohl für einige Anwendungen (z.B. Bauwesen) ein Einheitssystem, das alle Maße in Metern anzeigt sinnvoller ist.[Pull-Request #11365](https://github.com/FreeCAD/FreeCAD/pull/11365)
-   Weitere Markergrößen (20, 25 and 30px) wurden zu *Einstellungen → Anzeige → 3D-Viewer → Markergröße* hinzugefügt, um Anwender mit 4K-Bildschirmen zu unterstützen. [Pull-Request #11524](https://github.com/FreeCAD/FreeCAD/pull/11524)
-   Eine Option *Transparenzmodus umschalten* wurde dem Menü Ansicht und den Kontextmenüs hinzugefügt um den Transparenzmodus für ausgewählte Objekte schnell ein- oder ausschalten zu können. [Pull-Request #10805](https://github.com/FreeCAD/FreeCAD/pull/10805)



## Kernsystem und API 



### Kern

-   Vektor-Funktionen der [Vector-API](Vector_API/de.md) können jetzt in [Ausdrücken](Expressions/de.md) verwendet werden. [Pull-Request #8603](https://github.com/FreeCAD/FreeCAD/pull/10237).
-   Die Dateiliste im Dialog [Makro ausführen](Std_DlgMacroExecute/de.md) kann jetzt gefiltert werden, sowohl nach Dateinamen als auch nach Datei-Inhalt.[Pull-Request](https://github.com/FreeCAD/FreeCAD/pull/10714).
-   Der Python-Editor passt das Einrücken jetzt an die vorherige Zeile an, wenn die Enter-Taste gedrückt wird. [Pull-Request](https://github.com/FreeCAD/FreeCAD/pull/11356).



### API



#### Neue Python-API 

-    {{Incode|getUpDirection}}: Ermittelt die Nach-oben-Richtung einer View3DInventor-Ansicht. [Pull-Request #10060](https://github.com/FreeCAD/FreeCAD/pull/10060)



#### Entfernte Python-API 



## Addon-Manager 



## Arbeitsbereich Arch 



### Weitere Arch-Verbesserungen 



## Arbeitsbereich Draft 

-   Eine Option für die Ausrichtung und mehrere zugehörige Eigenschaften wurden zur [Draft Textform](Draft_ShapeString/de.md) hinzugefügt. [Pull-Request #10233](https://github.com/FreeCAD/FreeCAD/pull/10233)
-   [Radiale Maße](Draft_Dimension/de#Anwendung_radiales_Maß.md) zeigen jetzt nur noch eine Pfeilspitze.[Pull-Request #10655](https://github.com/FreeCAD/FreeCAD/pull/10655)
-   Eine Eigenschaft Oblique Angle (schiefer Winkel) wurde zu [Draft Textform](Draft_ShapeString/de.md) hinzugefügt. [Pull-Request #10783](https://github.com/FreeCAD/FreeCAD/pull/10783)
-   Unterstützung für Hyperlinks wurde hinzugefügt. Hyperlinks zu lokalen und entfernten Dateien und URLs, in [Draft-Texten](Draft_Text.md) und [Draft Beschreibungen](Draft_Label.md) können aus ihrem Kontextmenü in der [Baumansicht](Tree_view/de.md) oder [3D-Ansicht](3D_view.md) geöffnet werden. [Pull-Request #10878](https://github.com/FreeCAD/FreeCAD/pull/10878)
-   Der Code von [Draft Arbeitsebene](Draft_SelectPlane/de.md) wurde überarbeitet. Es gibt jetzt eine Arbeitsebene pro 3D-Ansicht. [Pull-Request #11010](https://github.com/FreeCAD/FreeCAD/pull/11010)
-   Die Bauteilhistorie-Funktion und die Ausrichtungsoptionen des Befehls [Draft EbeneAuswählen](Draft_SelectPlane/de.md) wurden verbessert. [Pull-Request #11062](https://github.com/FreeCAD/FreeCAD/pull/11062)
-   Das Verhalten des [Draft-Rasters](Draft_ToggleGrid.md) wurde verbessert. Seine Sichtbarkeit wird jetzt in jeder 3D-Ansicht gespeichert. Wird der Arbeitsbereich gewechselt, werden alle Raster ausgeblendet (Es gibt einen [Fine-Tuning](Fine-tuning/de.md)-Parameter, um dies zu deaktivieren). [Pull-Request #11336](https://github.com/FreeCAD/FreeCAD/pull/11336)
-   Die Draft-Einstellungen wurden geprüft und verbessert. Einige Voreinstellungen wurden hinzugefügt, veraltete Voreinstellungen wurden entfernt. Die Seiten im [Voreinstellungseditor](Preferences_Editor/de.md) wurden neu angeordnet und zeigen jetzt Einheiten an, wo es passt. Ein Neustart von FreeCAD nach Anpassung der Draft-Einstellungen ist nicht mehr nötig. [Pull request #11379](https://github.com/FreeCAD/FreeCAD/pull/11379), [Pull-Request #11503](https://github.com/FreeCAD/FreeCAD/pull/11503), [Pull-Request #11512](https://github.com/FreeCAD/FreeCAD/pull/11512), [Pull-Request #11550](https://github.com/FreeCAD/FreeCAD/pull/11550), [Pull-Request #11579](https://github.com/FreeCAD/FreeCAD/pull/11579), [Pull-Request #11585](https://github.com/FreeCAD/FreeCAD/pull/11585), [Pull-Request #11677](https://github.com/FreeCAD/FreeCAD/pull/11677) und [Pull-Request #11694](https://github.com/FreeCAD/FreeCAD/pull/11694)



### Weitere Draft-Verbesserungen 

-   Der [Draft Flächenbinder](Draft_Facebinder/de.md) kann jetzt Flächen verarbeiten, die zu Verknüpfungen gehören oder zu Flächen, die in [Std Parts](Std_Part/de.md) eingebettet sind. [Pull-Request #11081](https://github.com/FreeCAD/FreeCAD/pull/11081)
-   Einige Einstellungen wurden zum Befehl [Draft StilFestlegen](Draft_SetStyle.md) hinzugefügt. [Pull-Request #11593](https://github.com/FreeCAD/FreeCAD/pull/11593) und [Pull-Request #11694](https://github.com/FreeCAD/FreeCAD/pull/11694)
-   Einstellungen wurden auch zum Befehl [Draft StilAnwenden](Draft_ApplyStyle.md) hinzugefügt. [Pull-Request #11610](https://github.com/FreeCAD/FreeCAD/pull/11610)
-   Einrasten, Bearbeiten und Tracker-Markerkierungen verwenden jetzt die Voreinstellung [Markergröße](Preferences_Editor/de#3D-Viewer.md). [Pull-Request #11688](https://github.com/FreeCAD/FreeCAD/pull/11688)



## Arbeitsbereich FEM 

+++
| <img alt="" src=images/FEM_legend_labels_relnotes_0.22.PNG  style="width:384px;"> | Die Position der Beschriftung der Farblegende wurde angepasst, damit die oberen weniger anfällig dafür sind, vom Navigationswürfel verdeckt zu werden. Die Voreinstellungen für Schriftart und Farbe der Beschriftung wurden für eine bessere Sichtbarkeit angepasst und Voreinstellungen wurden hinzugefügt, die eine Anpassung von Farbe und Größe der Beschriftung ermöglichen. [Pull-Request #10552](https://github.com/FreeCAD/FreeCAD/pull/10552) |
+++

+++
| <img alt="" src=images/FEM_stress_component_linearization_relnotes_0.22.png  style="width:384px;"> | Der Befehl [FEM PostFilterLinearizedStresses](FEM_PostFilterLinearizedStresses/de.md) kann jetzt die Spannungstensor-Komponenten für linearisierte Spannungsberechnungen verwenden. Vorher konnten nur Von Mises- und Tresca-Spannung sowie (größte/mittlere/kleinste) Hauptspannungen hierfür verwendet werden. [Pull-Request #11724](https://github.com/FreeCAD/FreeCAD/pull/11724) |
+++



### Weitere FEM-Verbesserungen 

-   Der Menüeintrag **Modell → Randbedingungen ohne Löser** wurde aus der Benutzerschnittstelle (GUI) entfernt. die gelisteten Randbedingungen konnten nicht verwendet werden. [Pull-Request #10457](https://github.com/FreeCAD/FreeCAD/pull/10457) and [Pull-Request #10459](https://github.com/FreeCAD/FreeCAD/pull/10459)
-   Das Wort \"constraint\" wurde aus den Namen und Beschreibungen der meisten Elemente des Arbeitsbereichs FEM entfernt, um eine korrekte Benennung sicherzustellen. Die (englischen) Namen wurden so geändert, dass sie den Normen der FEA-Industrie entsprechen und für neue Anwender intuitiv benutzbar sind. [Pull-Request #10519](https://github.com/FreeCAD/FreeCAD/pull/10519) und [Pull-Request #10799](https://github.com/FreeCAD/FreeCAD/pull/10799)

(die Übersetzungen sind noch anzupassen)

-   Neue Symbole wurden für [Solver CalculiX Standard](FEM_SolverCalculixCxxtools/de.md), [Solver job control](FEM_SolverControl/de.md) und [Run solver calculations](FEM_SolverRun/de.md) hinzugefügt, um sie intuitiver bedinbar zu machen.
-   Löser CalculiX (new framework) wurde aus der Benutzerschnittstelle entfernt, da er unfertig und im Moment unnötig ist. [Pull-Request #10823](https://github.com/FreeCAD/FreeCAD/pull/10823)
-   Das Layout einiger Aufgaben-Bereiche der Nachbereitungswerkzeuge wurde verbessert, um ihren horizontalen Platzverbrauch zu reduzieren. [Pull-Request #11066](https://github.com/FreeCAD/FreeCAD/pull/11066)
-   Der Aufgaben-Bereich von [FEM RandbedingungTemperatur](FEM_ConstraintTemperature.md) wurde überarbeitet, um Fehler bei der Bearbeitung dieser Funktion zu beheben.[Pull-Request #11126](https://github.com/FreeCAD/FreeCAD/pull/11126)
-   Ein alter Fehler der Funktion [FEM NachbereitungDataAlongLine](FEM_PostFilterDataAlongLine.md), der nur die Ausgabe der Größe aber nicht die der Vektorkomponenten ermöglichte wurde endlich behoben. [Pull-Request #10992](https://github.com/FreeCAD/FreeCAD/pull/10992)
-   [FEM RandbedingungKraft](FEM_ConstraintForce.md) and [FEM RandbedingungDruck](FEM_ConstraintPressure.md) wurden überholt, damit sie quellcodeseitig besser funktionieren. [Pull-Request #10935](https://github.com/FreeCAD/FreeCAD/pull/10935) and [Pull request #10923](https://github.com/FreeCAD/FreeCAD/pull/10923)
-   Der [FEM NachbereitungDataAtPoint](FEM_PostFilterDataAtPoint.md) hat jetzt eine Eigenschaft PointSize, um die Größe des Punktsymbols für eine bessere Sichtbarkeit ändern zu können [Pull-Request #11054](https://github.com/FreeCAD/FreeCAD/pull/11054)
-   Der Befehl [FEM Netzbereich](FEM_MeshRegion/de.md) wurde für bessere Verständlichkeit in der Benutzerschnittstelle (GUI) in *FEM Netz aufbereiten* umbenannt (der Name des Befehls bleibt unverändert). [Pull-Request #11489](https://github.com/FreeCAD/FreeCAD/pull/11489)



## Export



## Werkstoff

+++
| <img alt="" src=images/Materials_relnotes_0.22.PNG  style="width:384px;"> | Das System zum Verarbeiten von Werkstoffdaten, inklusive des Editors, wurde komplett überarbeitet. Weitere diesbezügliche Verbesserungen werden folgen. [Pull request #10690](https://github.com/FreeCAD/FreeCAD/pull/10690) |
+++

+++
| <img alt="" src=images/Appearance_preview_relnotes_0.22.png  style="width:384px;"> | Eine Voransicht der Materialdarstellung wurde hinzugefügt, um Materialien auf dieselbe Weise wie im Dokument anzuzeigen. [Pull-Request #11628](https://github.com/FreeCAD/FreeCAD/pull/11628) |
+++



## Arbeitsbereich Mesh 



### Weitere Mesh-Verbesserungen 



## Arbeitsbereich OpenSCAD 



### Weitere OpenSCAD-Verbesserungen 



## Arbeitsbereich Part 

+++
| <img alt="" src=images/Part_scale_relnotes_0.22.PNG  style="width:384px;"> | Das Werkzeug [Part Skalieren](Part_Scale/de.md) wurde hinzugefügt, um das einfache Skalieren von Formen zu ermöglichen, ohne die Werkzeuge des Arbeitsbereichs Draft verwenden zu müssen. [Pull-Request #10583](https://github.com/FreeCAD/FreeCAD/pull/10583) |
+++

+++
| <img alt="" src=images/Part_Mirror_relnotes_0.22.png  style="width:384px;"> | [Part Spiegeln](Part_Mirror/de.md) Unterstützt jetzt auch Referenzobjekte wie [Part Ebene](Part_Plane/de.md), um eine beliebige Spiegelebene zusätzlich zu den XY-, XZ- und YZ-Standardebenen festzulegen. [Pull-Request #11535](https://github.com/FreeCAD/FreeCAD/pull/11535) |
+++



### Weitere Part-Verbesserungen 

-   Die Eigenchaft *Frenet* ist jetzt die Standardeinstellung für das Werkzeug [Part Sweep](Part_Sweep.md), um übliche Darstellungsprobleme zu vermeiden.[Pull-Request #11590](https://github.com/FreeCAD/FreeCAD/pull/11590)



## Arbeitsbereich PartDesign 

+++
| <img alt="" src=images/Pad_task_dialog_relnotes_0.22.png  style="width:384px;"> | Die Aufgaben-Dialoge von [Block](PartDesign_Pad/de.md) und [Tasche](PartDesign_Pocket/de.md) wurden verbessert (neu arrangierte UI-Elemente, die Option **Fläche auswählen** bleibt deaktiviert, wenn nicht benötigt usw.). [Pull-Request #10392](https://github.com/FreeCAD/FreeCAD/pull/10392) |
+++

+++
| <img alt="" src=images/Pattern_offset_mode_relnotes_0.22.png  style="width:384px;"> | Ein Versetzen-Modus (offset-mode) wurde dem [Linearen Muster](PartDesign_LinearPattern/de.md) und dem [Polaren Muster](PartDesign_PolarPattern/de.md) hinzugefügt. Der bisherige Modus wurde in **Overall Length/Angle** (Gesamtlänge/-winkel) umbenannt. [Pull-Request #10377](https://github.com/FreeCAD/FreeCAD/pull/10377) |
+++



### Weitere PartDesign-Verbesserungen 

-   Die Option *Dicke nach innen auftragen* im Werkzeug [Dicke](PartDesign_Thickness/de.md) ist jetzt standardmäßig aktiviert. [Pull-Request #7488](https://github.com/FreeCAD/FreeCAD/pull/7488)



## Arbeitsbereich Path 



### Weitere Path-Verbesserungen 



## Plot-Modul 



## Arbeitsbereich Points 



### Weitere Points-Verbesserungen 



## Arbeitsbereich Sketcher 

+++
| <img alt="" src=images/Arc_helper_relnotes_0.22.png  style="width:384px;"> | Es wurde ein Ergänzungskreis für Bögen implementiert (um das Problem der Randbedingungen, die scheinbar nicht mit diesen verbunden sind, zu lösen) einschließlich des Befehls zum Ein-bzw.Ausschalten. [Pull-Request #9703](https://github.com/FreeCAD/FreeCAD/pull/9703) |
+++

   
  <img alt="" src=images/Contextual_dimension_relnotes_0.22.gif  style="width:320px;">Bild anklicken, wenn die Animation nicht automatisch startet.   Die kontextabhängige maßliche Randbedingung wurde hinzugefügt, um schnell und intuitiv unterschiedliche maßliche Randbedingungen festzulegen, mit einem einzigen vielseitigen Werkzeug. [Pull-Request #9810](https://github.com/FreeCAD/FreeCAD/pull/9810)
   

   
  <img alt="" src=images/Tool_parameters_relnotes_0.22.gif  style="width:320px;">Das Bild anklicken, wenn die Animation nicht automatisch startet.   Werkzeugparameter wurden hinzugefügt, die ermöglichen, dass Maße nebenher (während Formen gezeichnet werden) hinzugefügt werden. Abhängig von der Voreinstellung On-View-Parameters können sie deaktiviert, reduziert auf nur Maße (keine initialen Koordinaten) oder vollständig aktiviert sein. Außerdem wurden Auswahlmöglichkeiten zu den Formwerkzeugen hinzugefügt. Sie können mit der Taste M oder aus einer Ausklappliste im Aufgaben-Bereich ausgewählt werden. Einige Werkzeuge haben zusätzliche Einstellungen in Form von Checkboxen im Aufgaben-Bereich und zusätzliche Tastaturkürzel. Gegenwärtig stehen die neuen Elemente für Punkte, Linien, Kreisbögen, Ellipsen Rechtecke, Vielecke und Nuten zur Verfügung. Dies ist noch in Arbeit. [Pull-Request #11048](https://github.com/FreeCAD/FreeCAD/pull/11048), [Pull-Request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174) und folgende
   

+++
| <img alt="" src=images/Offset_relnotes_0.22.png  style="width:384px;"> | Ein Werkzeug [Versatzkontur](Sketcher_Offset/de.md) wurde hinzugefügt und ermöglicht Kurven mit konstantem Abstand zu erstellen. [Pull-Request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174) |
+++

+++
| <img alt="" src=images/Three_point_rectangle_relnotes_0.22.png  style="width:384px;"> | Die Variante [Rechteck](Sketcher_CompCreateRectangles/de.md) über drei Punkte wurde in zwei Versionen hinzugefügt: 3 Eckpunkte oder Mittelpunkt und 2 Eckpunkte. [Pull-Request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174) |
+++

+++
| <img alt="" src=images/Arc_slot_relnotes_0.22.png  style="width:384px;"> | Ein Bogennut-Werkzeug wurde mit zwei Varianten zum Erstellen gekrümmter Nuten (Runde Enden und gerade Enden) hinzugefügt [Pull-Request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174) |
+++

   
  <img alt="" src=images/Auto_horizontal-vertical_relnotes_0.22.gif  style="width:320px;">Abbildung anklicken, wenn die Animation nicht automatisch startet.   Eine Randbedingung Horizontal/Vertikal wurde hinzugefügt. Sie fügt automatisch eine Randbedingung HorizontalFestlegen ein, wenn eine Linie eher einer horizontal ausgerichtet ist oder eine Randbedingung VertikalFestlegen, wenn sie eher vertikal ausgerichtet ist. [Pull-Request #11538](https://github.com/FreeCAD/FreeCAD/pull/11538)
   

+++
| <img alt="" src=images/Angle_radius_rendering_relnotes_0.22.png  style="width:384px;"> | Die Darstellung der Randbedingungen für Winkel und Radius wurde verbessert. Randbedingungen für Winkel haben jetzt richtige Maßhilfslinien. [Pull-Request #11507](https://github.com/FreeCAD/FreeCAD/pull/11507) |
+++

+++
| <img alt="" src=images/Polar_transform_relnotes_0.22.png  style="width:384px;"> | Ein Werkzeug Schwenken wurde hinzugefügt, das das Schwenken von Sketcher-Geometrien ermöglicht sowie das Erstellen von kreisförmigen Mustern aus ihnen. [Pull-Request #11264](https://github.com/FreeCAD/FreeCAD/pull/11264) |
+++



### Weitere Sketcher-Verbesserungen 

-   Die Option Rahmen wurde dem Rechteckwerkzeug hinzugefügt. [Pull-Request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174)
-   Zwei neue Optionen wurden dem Linienwerkzeug hinzugefügt: *Punkt, Länge, Winkel* und *Punkt, Breite, Höhe*. [Pull-Request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174)
-   Die Symbole [UmschalterKonstruktion](Sketcher_ToggleConstruction/de.md) und [UmschalterFührendeRandbedingung](Sketcher_ToggleDrivingConstraint/de.md) wurden geändert. Ersteres ist jetzt dem Symbol [Pause](Sketcher_CarbonCopy/de.md) weniger ähnlich und beide Schaltflächen wechseln ihre Symbole, wenn sie angeklickt werden. [Pull-Request #11500](https://github.com/FreeCAD/FreeCAD/pull/11500)
-   Sketcher-Symbole wurden überholt, um ihre Darstellung zu vereinheitlichen (Strichbreiten, Farben und Punktgröße). [Pull-Request #11785](https://github.com/FreeCAD/FreeCAD/pull/11785)
-   Eine wahlweise (standardmäßig deaktivierte) Zusammenfassung von [KoinzidentFestlegen](Sketcher_ConstrainCoincident/de.md) and [PunktAufObjektFestlegen](Sketcher_ConstrainPointOnObject/de.md) wurde eingeührt. [Pull-Request #11494](https://github.com/FreeCAD/FreeCAD/pull/11494)



## Arbeitsbereich Spreadsheet 



### Weitere Spreadsheet-Verbesserungen 



## Arbeitsbereich Start 

+++
| <img alt="" src=images/Start_page_template_buttons_new_relnotes_0.22.PNG  style="width:384px;"> | Ein Abschnitt **Neue Datei**, der einige Quick-Start-Schaltflächen enthält, wurde zur Startseite hinzugefügt. [Pull-Request #10171](https://github.com/FreeCAD/FreeCAD/pull/10171) |
+++

+++
| <img alt="" src=images/Start_page_layout_relnotes_0.22.png  style="width:384px;"> | Das visuelle Erscheinungsbild der Startseite wurde überholt. Sie sieht jetzt moderner und einheitlicher aus. [Pull-Request #10391](https://github.com/FreeCAD/FreeCAD/pull/10391) |
+++



### Weitere Start-Verbesserungen 

-   Die Seite der Einstellungen des Arbeitsbereichs Start wurde umgestellt. [Pull-Request #10520](https://github.com/FreeCAD/FreeCAD/pull/10520)
-   Es gibt jetzt eine Option **Custom CSS** für die Startseite, die es dem Benutzer ermöglicht, den CSS-Stil der Startseite in den Einstellungen des Arbeitsbereichs Start anzupassen.[Pull-Request #10520](https://github.com/FreeCAD/FreeCAD/pull/10520)
-   Die Einstellung **Hide scrollbars** wurde entfernt. Die Scrollbars auf der Startseite sind jetzt passend zum Thema gestaltet und sind viel dünner. [Pull-Request #10520](https://github.com/FreeCAD/FreeCAD/pull/10520)
-   Es gibt jetzt Einstellungen für das Ausblenden und das Ändern der Göße von Datei-Thumbnail-Symbolen auf der Startseite.[Pull-Request #10410](https://github.com/FreeCAD/FreeCAD/pull/10410)



## Arbeitsbereich Surface 



### Weitere Surface-Verbesserungen 



## Arbeitsbereich TechDraw 

+++
| <img alt="" src=images/TechDraw_cosmetic_circle_relnotes_0.22.png  style="width:250px;"> | Das Werkzeug [Hilfskreis](TechDraw_CosmeticCircle/de.md) wurde hinzugefügt, um das Erstellen von Hilfskreisen durch Auswahl des Mittelpunktes und Festlegen des Radius zu ermöglichen. [Pull-Request #10763](https://github.com/FreeCAD/FreeCAD/pull/10763) |
+++

+++
| <img alt="" src=images/Arc_length_relnotes_0.22.PNG  style="width:250px;"> | Das Werkzeug [HinweisBogenlänge](TechDraw_ExtensionArcLengthAnnotation/de.md) wurde hinzugefügt, um einen maßähnlichen Hinweis für die Bogenlänge ausgewählter Kanten zu erstellen. [Pull-Request #11532](https://github.com/FreeCAD/FreeCAD/pull/11532) |
+++

+++
| <img alt="" src=images/Offset_vertex_relnotes_0.22.png  style="width:250px;"> | Das Werkzeug [AddOffsetVertex](TechDraw_CommandAddOffsetVertex/de.md) wurde hinzugefügt, um Hilfspunkte relativ zu ausgewählten Knoten zu erstellen. [Pull-Request #11655](https://github.com/FreeCAD/FreeCAD/pull/11655) |
+++



### Weitere TechDraw-Verbesserungen 

-   Schnittansichten, die auf anderen Schnittansichten basieren, verwenden jetzt standardmäßig die originale (unbeschnittene) Form. Dies kann in den Einstellungen der Schnittansichten geändert werden, um stattdessen die vorhergehende beschnittene Form zu verwenden [Pull-Request #10281](https://github.com/FreeCAD/FreeCAD/pull/10281)
-   Hilfsobjekte und Mittellinien können jetzt ausgewählt und durch drücken der Löschtaste entfernt werden. Bisher wurde so die ganze Ansicht gelöscht.[Pull-Request #10695](https://github.com/FreeCAD/FreeCAD/pull/10695) und [Pull-Request #10813](https://github.com/FreeCAD/FreeCAD/pull/10813)
-   Ein neues intuitiveres Symbol wurde für das Werkzeug [Schweißsymbol](TechDraw_WeldSymbol/de.md) hinzugefügt. [Pull-Request #10936](https://github.com/FreeCAD/FreeCAD/pull/10936)
-   Das Verhalten des Modus Punkt + Kante im Werkzeug [Längenmaß](TechDraw_LengthDimension.md) wurde korrigiert. [Pull-Request #10860](https://github.com/FreeCAD/FreeCAD/pull/10860)
-   Der Schaltfläche [Ansichtsrahmen ein- oder ausschalten](TechDraw_ToggleFrame/de.md) wurde ein Aktiviert-Status hinzugefügt, damit der Anwender sehen kann, ob die Schaltfläche aktiviert ist oder nicht.[Pull-Request #11240](https://github.com/FreeCAD/FreeCAD/pull/11240)
-   Das Verhalten des Werkzeugs [LiniendarstellungÄndern](TechDraw_DecorateLine/de.md) wurde verbessert. Jetzt wird das Werkzeug (auch) durch Doppelklicken auf einer Linie aufgerufen. Und die Linieneinstellungen werden korrekt wiederhergestellt, wenn der Anwender *Abbrechen* drückt. Vorher war kein Unterschied zwischen *OK* und *Abbrechen*. [Pull-Request #11188](https://github.com/FreeCAD/FreeCAD/pull/11188)
-   Farbe und Transparenz von Flächen können jetzt pro Ansicht eingetellt werden.[Pull-Request #11315](https://github.com/FreeCAD/FreeCAD/pull/11315)
-   Der Mehrfachauswahl-Modus wurde hinzugefügt und kann in den Einstellungen aktiviert werden. In diesem Modus können mehrere Knoten, Kanten oder Flächen durch klicken mit der linken Maustaste ausgewählt werden, ohne dass die Ctrl- bzw. Strg-Taste gedrückt gehalten werden muss. [Pull-Request #11417](https://github.com/FreeCAD/FreeCAD/pull/11417)
-   [ErgänzungFlächenangabe](TechDraw_ExtensionAreaAnnotation/de.md) kann jetzt auch beliebige Flächen berechnen. [Pull-Request #11473](https://github.com/FreeCAD/FreeCAD/pull/11473)
-   Unterbreochene Linien werden jetzt ISO-/ANSI-Normen entsprechend dargestellt, anstatt nach Qt-Linienstilen. Eine neue Voreinstellung zum Auswählen der Norm wurde hinzugefügt. [Pull-Request #11594](https://github.com/FreeCAD/FreeCAD/pull/11594)
-   Das Verhalten des Werkzeugs [AxonometrischesLängenmaß](TechDraw_AxoLengthDimension/de.md) wurde verbessert. Jetzt wird der tatsächliche (3D-) Wert automatisch berechnet und in die Eigenschaft Format Spec (als Text) eingefügt, wenn Kanten parallel zu den globalen Koordinatensystemachsen bemaßt werden. [Pull-Request #11678](https://github.com/FreeCAD/FreeCAD/pull/11678)
-   Das Werkzeug [ErgänzungSchnittAusrichten](TechDraw_ExtensionPositionSectionView/de.md) kann jetzt verwendet werden, indem eine Kante in einer Schnittansicht und ein Knoten in der Quellansicht ausgewählt werden.[Pull-Request #11797](https://github.com/FreeCAD/FreeCAD/pull/11797)



## Arbeitsbereich Web 



### Weitere Web-Verbesserungen 



## Kompilieren



## Bekannte Einschränkungen



---
⏵ [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 0.22/de
