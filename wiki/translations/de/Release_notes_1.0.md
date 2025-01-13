# Release notes 1.0/de
**FreeCAD 1.0** wurde am **18. November 2024** veröffentlicht, es kann von der [Download](Download/de.md)-Seite heruntergeladen werden. Diese Seite listet alle Neuerungen und Änderungen auf.

Ältere FreeCAD-Versionshinweise findet man in den [Versionshinweisen](Feature_list/de#Versionshinweise.md).



## In memoriam Bradley McLean (bgbsww) 

So sehr wir uns freuen, diese neue Version vorzustellen, so sehr sind wir betrübt, mitzuteilen, dass unser Freund und überaus produktiver FreeCAD-Entwickler [bgbsww](https://github.com/bgbsww) ein paar Wochen bevor diese Version veröffentlicht wurde, verstorben ist. Er war einer der wichtigsten Architekten für die Anstrengungen das Problems der topologischen Benennung (TNP) zu beheben, schrieb eine große Menge zusätzlicher Codes und Tests und wurde FreeCADs TNP-Spezialist. Er half auch nahezu jedem anderen Entwickler dabei, Anpassungen für den neue Algorithmus bereitzustellen. Diese Version ist ihm gewidmet.



## Allgemein

+++
| <img alt="" src=images/TNP_fix_relnotes_1.0.PNG  style="width:320px;"> | Das seit langem bestehende [Problem der topologischen Benennung](Topological_naming_problem/de.md) (TNP) wurde, dank der gemeisamen Anstrengung und harter Arbeit einiger Entwickler, endlich bearbeitet. Der [Realthunder-Algorithmus](https://github.com/realthunder/FreeCAD_assembly3/wiki/Topological-Naming-Algorithm) wurde sorgfältig implementiert und so verbessert, dass er in FreeCADs Master-Version funktioniert. Das Projekt dauerte über ein Jahr und die Erst-Implementierung wurde mit dem folgenden PR abgeschlossen, der die Verbesserungen aktiviert. Das Problem der topologischen Benennung ist noch nicht vollständig gelöst und weitere Verbesserungen werden in der nächsten Version folgen. [Pull-Request #13705](https://github.com/FreeCAD/FreeCAD/pull/13705) |
+++

+++
| <img alt="" src=images/AssemblyExample_relnotes_1.0.png  style="width:320px;"> | FreeCAD besitzt einen neuen eingebauten Arbeitsbereich [Assembly](Assembly_Workbench/de.md), der auf der originalen Arbeit basiert, die für etwas geleistet wurde, das wir \"das andere FreeCAD \" ([the other FreeCAD](https://www.askoh.com/freecad/what_is_freecad/index.html))\"nannten, eine weitere Software die FreeCAD genannt wurde, mit Möglichkeiten zur Bewegungssimulation, die zur gleichen Zeit wie unsere erstellt wurde. Die Portierung wurde von dem Autor des anderen FreeCADs selbst durchgeführt, [Dr. Aik-Siong Koh](https://www.askoh.com); mit dieser dramatischen Wende sind endlich beide FreeCADs vereint. Siehe unten für [weitere Informationen](#Arbeitsbereich_Assembly.md). [Pull-Request #10427](https://github.com/FreeCAD/FreeCAD/pull/10427) |
+++

+++
| <img alt="" src=images/Freecad.svg  style="width:320px;"> | FreeCAD hat ein neues Logo. Es wurde aus den 5 Gewinnern des öffentlichen Wettbewerbs ausgewählt. Verwendungsrichtlinien und ein Logo-Kit stehen auf der Seite der [FreeCAD brand guidelines](https://fpa.freecad.org/handbook/process/logo.html) zur Verfügung. [Pull-Request #14284](https://github.com/FreeCAD/FreeCAD/pull/14284) |
+++



## Benutzeroberfläche

+++
| <img alt="" src=images/Rotation_Center_Indicator_relnotes_1.0.gif  style="width:320px;"> | Ein Indikator für das Drehzentrum wurde hinzugefügt. Dieser Indikator wird angezeigt, wenn die Ansicht durch Ziehen mit der Maus gedreht wird. Er kann wahlweise in den Voreinstellungen deaktiviert werden. Außerdem gibt es Einstellungen für seine Farbe, Transparenz und Größe. [Pull-Request #9909](https://github.com/FreeCAD/FreeCAD/pull/9909) und [Pull-Request #10790](https://github.com/FreeCAD/FreeCAD/pull/10790) |
+++

   
  <img alt="" src=images/Selection_filters_relnotes_1.0.gif  style="width:320px;">Klick auf das Bild, wenn die Animation nicht automatisch startet.   [Auswahlfilter](Part_SelectFilter/de.md) wurden hinzugefügt; sie ermöglichen die Auswahl auf Knoten, Kanten oder Flächen einzugrenzen. [Pull-Request #10271](https://github.com/FreeCAD/FreeCAD/pull/10271)
   

+++
| <img alt="" src=images/Tasks_Dockable_relnotes_1.0.png  style="width:320px;"> | Für mehr Flexibilität ist der Aufgaben-Bereich jetzt ein eigenständiges Widget. Es kann über der Combo-Asicht [angedockt](Combo_view/de#Aufgaben-Fenster_über_der_Combo-Ansicht_andocken.md) werden,um die kompakte Darstellung früherer Versionen zu erreichen. [Pull-Request #10681](https://github.com/FreeCAD/FreeCAD/pull/10681) und [Pull-Request #10848](https://github.com/FreeCAD/FreeCAD/pull/10848) |
+++

+++
| <img alt="" src=images/Transform_tool_relnotes_1.0.png  style="width:320px;"> | Die Darstellung der Anfasser des Werkzeugs [Bewegen](Std_TransformManip/de.md) wurde verbessert. Es besitzt jetzt auch drei Ebenen-Anfasser, um Objekte entlang der 3 Hauptebenen zu bewegen. [Pull-Request #10706](https://github.com/FreeCAD/FreeCAD/pull/10706) |
+++

+++
| <img alt="" src=images/Overlay_relnotes_1.0.png  style="width:320px;"> | Realthunders Funktion, die das Überlagern von Dock-Widgets ermöglicht (Baum- und Aufgaben-Transparenz) wurde hinzugefügt. [Pull-Request #7888](https://github.com/FreeCAD/FreeCAD/pull/7888) |
+++

+++
| <img alt="" src=images/Light_source_relnotes_1.0.png  style="width:320px;"> | Die Lichtquelle kann jetzt in den Voreinstellungen eingestellt werden (*Einstellungen\... → Anzeige*). [Pull-Request #11146](https://github.com/FreeCAD/FreeCAD/pull/11146) und [Pull-Request #15877](https://github.com/FreeCAD/FreeCAD/pull/15877) |
+++

+++
| <img alt="" src=images/Preference_tree_relnotes_1.0.png  style="width:320px;"> | Das Voreinstellungsfenster wurde übrearbeitet um die Karteitreiter durch eine Baumstruktur zu ersetzen. [Pull-Request #11018](https://github.com/FreeCAD/FreeCAD/pull/11018) |
+++

+++
| <img alt="" src=images/TabBar_relnotes_1.0.png  style="width:320px;"> | Für die Auswahl der Arbeitsbereiche wurde TabBar hinzugefügt. Es kann in unter *Einstellungen → Arbeitsbereiche* aktiviert und konfiguriert werden. [Pull-Request #12270](https://github.com/FreeCAD/FreeCAD/pull/12270) |
+++

+++
| <img alt="" src=images/Unified_measurement_relnotes_1.0.PNG  style="width:320px;"> | Ein neues [universelles Messwerkzeug](Std_Measure/de.md) wurde hinzugefügt und ersetzt die alten [Part Messwerkzeuge](Part_Workbench/de#Messwerkzeuge.md). [Pull-Request #9750](https://github.com/FreeCAD/FreeCAD/pull/9750) und folgende |
+++

   
  <img alt="" src=images/Normal_view_relnotes_1.0.gif  style="width:320px;">Auf das Bild klicken, wenn die Animation nicht automatisch startet.   Das Werkzeug [Auf die Auswahl ausrichten](Std_AlignToSelection/de.md) wurde hinzugefügt und ermöglicht die Richtung von Ansichten normal auf Flächen oder an Kanten entlang festzulegen. [Pull-Request #13906](https://github.com/FreeCAD/FreeCAD/pull/13906)
   



### Weitere Verbesserungen der Benutzeroberfläche 

-   Es wurde ein \"project unit system\" eingeführt. [Pull-Request #9521](https://github.com/FreeCAD/FreeCAD/pull/9521)
-   Das Werkzeug [Part Schnittansicht](Part_SectionCut/de.md) funktioniert jetzt auch in einer perspektivischen Ansicht. [Pull-Request #10143](https://github.com/FreeCAD/FreeCAD/pull/10143)
-   Eine Option zum alphabetischen Sortieren von Arbeitsbereichen wurde hinzugefügt (steht nach einem Rechtsklick in *Einstellungen → Arbeitsbereiche* zur Verfügung). [Pull-Request #10363](https://github.com/FreeCAD/FreeCAD/pull/10363)
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
-   Ein Befehl Symbolleisten sperren wurde hinzugefügt. Damit können die Positionen von Symbolleisten fixiert oder wieder freigegeben werden. Er steht im Menü Ansicht und im Kontextmenü des Symbolleistenbereichs zur Verfügung.[Pull-Request #11596](https://github.com/FreeCAD/FreeCAD/pull/11596)
-   Die Standardfarbe für Formen wurde angepasst, um die Darstellng der Modelle zu verbessern. [Pull-Request #12380](https://github.com/FreeCAD/FreeCAD/pull/12380) and [Pull-Request #12488](https://github.com/FreeCAD/FreeCAD/pull/12488)
-   Elemente in Part- und Gruppencontainern können jetzt durch Ziehen und Ablegen sortiert werden. [Pull-Request #12293](https://github.com/FreeCAD/FreeCAD/pull/12293)
-   Sichtbarkeitssymbole (Auge-Symbol) werden den Baumobjekten hinzugefügt, wenn die Option Sichtbarkeitssymbol anzeigen unter *Einstellungen\... → Anzeige → Benutzeroberfläche* aktiviert ist. [Pull-Request #12298](https://github.com/FreeCAD/FreeCAD/pull/12298)
-   Ein Status [Eingefroren](Std_ToggleFreeze/de.md) (Option *Einfrieren umschalten* (Toggle freeze) im Kontextmenü der [Baumansicht](Tree_view/de.md)) wurde hinzugefügt und ermöglicht das parametrische Verhalten eines Objekts abzuschalten (so dass es sich nicht verändert, auch wenn die Objekte von denen es abhängt geändert werden). [Pull-Request #12580](https://github.com/FreeCAD/FreeCAD/pull/12580)
-   Navigationsanimationen wurden verbessert. Animationen verwenden jetzt eine Vereinfachungsfunktion und haben eine festgelegte Dauer, die unter *Einstellungen\... → Anzeige → Navigation* eingestellt werden kann. [Pull-Request #10881](https://github.com/FreeCAD/FreeCAD/pull/10881) und [Pull-Request #12205](https://github.com/FreeCAD/FreeCAD/pull/12205)
-   Die Schaltflächen der voreingestellten Ansichten sind jetzt unter einer einzigen Schaltfläche gruppiert. Die einzelnen Schaltflächen stehen noch immer in der zusätzlichen Symbolleiste *Einzelne Ansichten* (Individual views) zur Verfügung. [Pull-Request #12878](https://github.com/FreeCAD/FreeCAD/pull/12878)
-   Der Name des gerade aktiven Dokuments wird jetzt in der Titelleiste des Fensters angezeigt. [Pull-Request #12035](https://github.com/FreeCAD/FreeCAD/pull/12035)
-   Ein Befehl zum Anzeigen des [Eigenschateneditors](Property_editor.md) wurde hinzugefügt. [Pull-Request #12024](https://github.com/FreeCAD/FreeCAD/pull/12024)
-   Die Integration von 3Dconnexion-Geräten in FreeCAD unter Windows wurde verbessert. [Pull-Request #12929](https://github.com/FreeCAD/FreeCAD/pull/12929)
-   Eine Funktion Quick Measure wurde hinzugefügt. Sie verwendet die [Statusleiste](Status_bar/de.md), um Informationen zu den Abmessungen (Kantenlänge, Flächeninhalt, Abstand zwischen Punkten und/oder Kanten, Winkel zwischen Kanten und Radius zylindrischer Kanten bzw. Flächen) der aktuellen Auswahl in der 3D-Ansicht anzuzeigen. [Pull-Request #12217](https://github.com/FreeCAD/FreeCAD/pull/12217)
-   Symbolleisten können jetzt gezogen und auf der Statusleiste und den Menüleisten abgelegt werden. [Pull-Request #13571](https://github.com/FreeCAD/FreeCAD/pull/13571)
-   Eine Schaltfläche *Reload stylesheet* wurde hinzugefügt, um die Entwicklung von Stylesheets zu unterstützen. Sie gehört standardmäßig zu keiner Symbolleiste und muss manuell mit *Werkzeuge → Benutzerdefiniert → Symbolleisten → Ansicht* hinzugefügt werden. [Pull-Request #13982](https://github.com/FreeCAD/FreeCAD/pull/13982)
-   Dokumentsymbole (einschließlich von u.a. [Öffnen](Std_Open/de.md) und [Speichern](Std_Save/de.md)) wurden verbessert und vereinheitlicht. [Pull-Request #13865](https://github.com/FreeCAD/FreeCAD/pull/13865)
-   Das [Einpassen](Std_ViewFitAll/de.md)-Symbol wurde ausgetauscht, für bessere Erkennbarkeit. [Pull-Request #14180](https://github.com/FreeCAD/FreeCAD/pull/14180)
-   Mehrere Symbole des Kernsystems (wie z.B. [Neu](Std_New/de.md)) wurden verbessert. [Pull-Request #14278](https://github.com/FreeCAD/FreeCAD/pull/14278), [Pull-Request #14434](https://github.com/FreeCAD/FreeCAD/pull/14434) und [Pull-Request #14154](https://github.com/FreeCAD/FreeCAD/pull/14154)
-   Die Symbole der Aufgaben-Tafeln von Sketcher und PartDesign wurden verbessert. [Pull-Request #13968](https://github.com/FreeCAD/FreeCAD/pull/13968)
-   Im [Headless-Modus](Headless_FreeCAD/de.md) enthält die interaktive Python-Konsole jetzt eine Tab-Vervollständigung, sofern das Modul [readline](https://docs.python.org/3/library/readline.html) zur Verfügung steht. [Pull-Request #14213](https://github.com/FreeCAD/FreeCAD/pull/14213)
-   Eine Option zur Darstellung der internen Namen in der Baumansicht wurde hinzugefügt. Sie ist standardmäßig deaktiviert und kann unter *Einstellungen → Anzeige → Benutzeroberfläche → Hide Internal Names* aktiviert werden. [Pull-Request #14237](https://github.com/FreeCAD/FreeCAD/pull/14237)
-   Die Hilfe-Schaltfläche wurde aus den Voreinstellungen entfernt, da sie ohne Funktion war. [Pull-Request #14695](https://github.com/FreeCAD/FreeCAD/pull/14695)
-   Vorgegebene Stylesheets wurden erheblich verbessert und sind jetzt in zwei Varianten neben classic vorhanden: light und dark. [Pull-Request #13772](https://github.com/FreeCAD/FreeCAD/pull/13772)
-   Die Themen- und UI-Seiten in der Gruppe Anzeige der Voreinstellungen wurden umsortiert und kombiniert. Einige Einstellungen wurden zur neuen Seite Erweitert verschoben. [Pull-Request #14974](https://github.com/FreeCAD/FreeCAD/pull/14974)
-   Die Part/Part Design-Einstellungen zum Prüfen und Aufbereiten sind jetzt standardmäßig aktiviert. [Pull-Request #14406](https://github.com/FreeCAD/FreeCAD/pull/14406)
-   Ein neuer Parameter wurde hinzugefügt - **BaseApp/Preferences/Bitmaps/Theme/UseIconTheme** (boolean): Auf true gesetzt, wird Qt gezwungen Symbole aus dem Sybolsatz des Systems zu verwenden. Der Standardwert ist false und lässt FreeCAD seine eigenen Symbole benutzen. Es beeinflusst nicht die anderen Mechanismen von Qt-Icon-Themes wie Systemdialoge, Schaltflächen und andere. Jene sollten immer die Symbole des System-Themes verwenden. [Pull-Request #16018](https://github.com/FreeCAD/FreeCAD/pull/16018)
-   Stylesheet, Theme und QtStyle-informationen sind jetzt in *Help → About FreeCAD* enthalten. [Pull-Request #16281](https://github.com/FreeCAD/FreeCAD/pull/16281)
-   Der Splash-Screen wird jetzt beim Start zufällig aus mehreren Bildern ausgewählt, die Modelle von Anwendern zeigen oder einige der Addon-Arbeitsbereiche präsentieren. [Pull-Request #16071](https://github.com/FreeCAD/FreeCAD/pull/16071)
-   Ein sicherer Modus wurde hinzugefügt und kann unter *Hilfe → Im sicheren Modus neu starten* aktiviert werden. Dieser deaktiviert zeitweise die Benutzerkonfiguration, Addons, Voreinstellungspakete (Themes) und andere Benutzereinstellungen, um FreeCAD zur Fehlerbehebung in einem \"Lieferzustand\" (factory reset) zu betreiben. [Pull-Request #16858](https://github.com/FreeCAD/FreeCAD/pull/16858)



## Dateiformatänderungen

Obwohl Vorkehrungen getroffen wurden, um zu garantieren, dass Dateien, die mit der neuen Version 1.0 erstellt wurden, weiterhin mit älteren Versionen von FreeCAD geöffnet werden können, wurden in 1.0 einige neue Funktionen eingeführt, die vorherige Versionen nicht verstehen können; dies kann dazu führen können dass Modelle, die mit 1.0 gespeichert wurden, brechen oder zu Probleme aufwerfen, wenn sie mit älteren Versionen von FreeCAD geöffnet werden. Hier ist eine Zusammenfassung möglicher Probleme, auf die man stoßen kann, und deren Lösung. Auch die Gemeinschaft im Forum kann beim Beheben von Kompatibilitätsproblemen Hilfe zur Verfügung stellen.

-   Die Eigenscaft **Attachment** wurde in **AttachmentSupport** umbenannt. Das bedeutet, dass Funktionen, die von dieser Eigenschaft abhängen, (hauptsächlich Modelle, die das Addon Assembly4 verwenden) müssen überarbeitet werde, um sie in früheren Versionen von FreeCAD öffnen zu können. Ein Makro, dass diese Dateien repariert, [steht hier zur Verfügung](Macro_Convert_021.md).



## Kernsystem und API 



### Kern

-   Vektor-Funktionen der [Vector-API](Vector_API/de.md) können jetzt in [Ausdrücken](Expressions/de.md) verwendet werden. [Pull-Request #8603](https://github.com/FreeCAD/FreeCAD/pull/10237).
-   Der Python-Editor passt das Einrücken jetzt an die vorherige Zeile an, wenn die Enter-Taste gedrückt wird. [Pull-Request](https://github.com/FreeCAD/FreeCAD/pull/11356).
-   Der Name der Eigenschaft, die die Referenzobjekte eines Anhangs enthält, wurde von **Support** zu **AttachmentSupport** geändert. [Pull-Request #12714](https://github.com/FreeCAD/FreeCAD/pull/12714).
-   Ein Eigenschaftebehälter, App::VarSet, wurde als eine Kernfunktionalität eingeführt. Ein VarSet ermöglicht dem Anwender Eigenschaften festzulegen, die in Modellen eingesetzt werden können, so wie Aliase einer Kalkulationstabelle und andere vorherige(?) Eigenschaften-Behälter (Dynamic-Data, Path-PropertyBags, und Assembly 4-Variable). [Pull-Request #12135](https://github.com/FreeCAD/FreeCAD/pull/12135)



### API



#### Neue Python-API 

-    {{Incode|getUpDirection}}: Ermittelt die Nach-oben-Richtung einer View3DInventor-Ansicht. [Pull-Request #10060](https://github.com/FreeCAD/FreeCAD/pull/10060)



#### Geänderte Python-API 

-   Die Methoden zum Speichern bzw. Wiederherstellen von benutzerdefinierten Daten eines Python-Elements wurden von {{Incode|__getstate__}} bzw. {{Incode|__setstate__}} zu {{Incode|dumps}} bzw. {{Incode|loads}} umbenannt. Dies wurde erforderlich durch interne Änderungen in Python-3.11. [Pull-Request #10769](https://github.com/FreeCAD/FreeCAD/pull/10769) and [Pull-Request #12243](https://github.com/FreeCAD/FreeCAD/pull/12243).



## Start

Der Arbeitsbereich Start wurde durch eine Startseite ersetzt, eine App, die auf QtWidgets basiert. Sie kann mit der Option *Hilfe → Start* angezeigt werden. [Pull-Request #13134](https://github.com/FreeCAD/FreeCAD/pull/13134)

Die ersten beiden unten genannten Pull-Requests gehören zum Arbeitsbereich Start, haben aber das Design der Startseite beeinflusst.

+++
| <img alt="" src=images/Start_page_template_buttons_new_relnotes_1.0.png  style="width:384px;"> | Ein Abschnitt **Neue Datei**, der einige Quick-Start-Schaltflächen enthält, wurde zur Startseite hinzugefügt. [Pull-Request #10171](https://github.com/FreeCAD/FreeCAD/pull/10171) |
+++

+++
| <img alt="" src=images/Start_page_layout_relnotes_1.0.png  style="width:384px;"> | Das visuelle Erscheinungsbild der Startseite wurde überholt. Sie sieht jetzt moderner und einheitlicher aus. [Pull-Request #10391](https://github.com/FreeCAD/FreeCAD/pull/10391) |
+++

+++
| <img alt="" src=images/First_start_relnotes_1.0.png  style="width:384px;"> | Ein einfaches Erst-Start-Widget wurde hinzugefügt und wird in naher Zukunft noch erweitert werden. [Pull-Request #13650](https://github.com/FreeCAD/FreeCAD/pull/13650) |
+++



## Arbeitsbereich Assembly 

+++
| <img alt="" src=images/Assembly_relnotes_1.0.png  style="width:384px;"> | Ein Arbeitsbereich [Assembly](Assembly_Workbench/de.md) (Zusammenbau, Baugruppe)wurde endlich als fester Bestandteil zu FreeCAD hinzugefügt. Er verwendet den quelloffenen Gleichungslöser [Ondsel-Solver](https://github.com/Ondsel-Development/OndselSolver). Grundlegende Funktionen (Verbindungen - joints) stehen schon zur Verfügung, weitere Funktionen sind in der Entwicklung. [Pull-Request #10427](https://github.com/FreeCAD/FreeCAD/pull/10427), [Pull-Request #10764](https://github.com/FreeCAD/FreeCAD/pull/10764), [Pull-Request #12406](https://github.com/FreeCAD/FreeCAD/pull/12406) und weitere |
+++



### Weitere Assembly-Verbesserungen 

-   Eine [Explosionsansicht](Assembly_CreateView/de.md) wurde hinzugefügt. [Pull-Request #12419](https://github.com/FreeCAD/FreeCAD/issues/12419)
-   Assembly-Symbole wurden überarbeitet und die experimentellen Funktionen stehen jetzt zur Verfügung. [Pull-Request #13866](https://github.com/FreeCAD/FreeCAD/pull/13866)
-   Winkellage ausrichten, Rechtwinklig ausrichten und Parallel ausrichten wurden hinzugefügt. [Pull-Request #14008](https://github.com/FreeCAD/FreeCAD/pull/14008)
-   Eine [Stücklistenfunktion](Assembly_CreateBom/de.md) wurde hinzugefügt. [Pull-Request #14198](https://github.com/FreeCAD/FreeCAD/pull/14198)
-   Unterstützung für den Code zur Minderung des [Problems der topologischen Benennung](Topological_naming_problem/de.md) (TNP) wurde hinzugefügt. [Pull-Request #14674](https://github.com/FreeCAD/FreeCAD/pull/14674)
-   Unterstützung für flexible Unterbaugruppen wurde hinzugefügt. Unterbaugruppen, die zu einer übergeordneten Baugruppen hinzugefügt werden können als starr (wie ein einziger Festkörper) oder flexibel (erlaubt die Bewegung ihrer einzelnen Komponenten) festgelegt werden. Für diese Unterbaugruppen, die während des Entwicklungszyklus eingefügt werden, sind manuelle Schritte erforderlich, bevor sie eingebunden werden. Solche Baugruppen müssen aus ihrer übergeordneten Baugruppe entfernt und wieder eingesetzt werden. [Pull-Request #15629](https://github.com/FreeCAD/FreeCAD/pull/15629)



## Arbeitsbereich BIM 

+++
| <img alt="" src=images/bim_relnotes_1.0.png  style="width:384px;"> | Der Arbeitsbereich Arch wurde mit dem Arbeitsbereich [BIM](BIM_Workbench.md) zum neuen Arbeitsbereich BIM zusammengeführt. Der neue Arbeitsbereich BIM behält alle Werkzeuge von Arch und fügt einige weitere hinzu und bringt so viele Verfeinerungen für den gesamten BIM- und Arch-Arbeitsablauf mit, bessere Werkzeugen zum Einstellen und Verwalten sowie bessere IFC-Unterstützung.[Pull request #13783](https://github.com/FreeCAD/FreeCAD/pull/13783) |
+++



### Weitere BIM-Verbesserungen 

-   Dem Arbeitsbereich BIM folgend wurden einige \"alles-in-einem\" Arch-Werkzeuge für unterschiedliche Anwendungsfälle aufgeteilt: Das Werkzeug [Arch Gebäudeteil](Arch_BuildingPart/de.md) wurde in die Werkzeuge [BIM Gebäude](Arch_Building/de.md) und [BIM Stockwerk](Arch_Floor/de.md) aufgeteilt, das Werkzeug [Arch Strukur](Arch_Structure/de.md) wurde in die Werkzeuge [BIM Stütze](BIM_Column/de.md), [BIM Beam](BIM_Beam/de.md) and [BIM Platte](BIM_Slab/de.md) aufgeteilt, und das Werkzeug [Arch Fenster](Arch_Window/de.md) wurde in die Werkzeuge [BIM Fenster](Arch_Window/de.md) and [BIM Tür](BIM_Door/de.md) aufgeteilt. Intern erstellen diese Werkzeuge noch dieselben Objekte, nur mit unterschiedlichen IFC-Typen und anderen Voreinstellungen. [Pull-Request #13783](https://github.com/FreeCAD/FreeCAD/pull/13783)
-   [NativeIFC](https://github.com/yorikvanhavre/FreeCAD-NativeIFC) wurde auch in den neuen Arbeitsbereich Bim integriert. Mit NativeIFC können jetzt IFC-Dateien nativ in FreeCAD bearbeitet werden, ohne Übersetzung ins oder aus dem FreeCAD-Dateiformat. Mehr Informationen gibt es auf der Seite [NativeIFC](NativeIFC/de.md). [Pull-Request #13783](https://github.com/FreeCAD/FreeCAD/pull/13783)
-   Der Befehl [Arch Schnittebene](Arch_CutPlane/de.md) wurde verbessert. Er beachtet jetzt Einbettungen sowie Verknüpfungen und die Auswahl ist flexibler. Es können jetzt auch Kanten ausgewählt werden, sodass der Befehl Arch Schnittlinie nicht mehr gebraucht wird. [Pull-Request #11254](https://github.com/FreeCAD/FreeCAD/pull/11254) und [Pull-Request #11792](https://github.com/FreeCAD/FreeCAD/pull/11792)
-   Die BIM-Voreinstellungen wurden überprüft und verbessert. Die Seiten im [Voreinstellungseditor](Preferences_Editor/de.md) haben ein neues Aussehen erhalten. [Pull-Request #11940](https://github.com/FreeCAD/FreeCAD/pull/11940) und [Pull-Request #12038](https://github.com/FreeCAD/FreeCAD/pull/12038)
-   Eine Einstellung *Nur Öffnung* wurde zum Befehl [Arch Fenster](Arch_Window/de.md) hinzugefügt. [Pull-Request #12209](https://github.com/FreeCAD/FreeCAD/pull/12209)
-   Das [Arch-Dach](Arch_Roof/de.md)-Objekt hat jetzt eine Eigenschaft *Subvolume*. Diese ermöglicht ein selbsterstelltes Festkörperobjekt als Abzugsvolumen für ein Dach zu verwenden. [Pull-Request #12346](https://github.com/FreeCAD/FreeCAD/pull/12346)
-   Außerdem wird für ein [Arch-Dach](Arch_Roof/de.md)-Objekt, das ein Festkörperobjekt als *Base* verwendet, automatisch ein geeignetes Abzugsvolumen erstellt. Wie ein Dach, das auf einem Linienzug basiert, kann so ein Dach von den Wänden eines Gebäudes mit [Arch Entfernen](Arch_Remove/de.md) abgezogen werden. [Pull-Request #13221](https://github.com/FreeCAD/FreeCAD/pull/13221)
-   Das Werkzeug [Arch Referenz](Arch_Reference/de.md) wurde aktualisiert: Referenzobjekte können jetzt komplette Dateiinhalte verwenden, anstatt ein Teil auswählen zu müssen; die Unterstützung für DXF- und IFC-Dateien wurde hinzugefügt. [Pull-Request #13287](https://github.com/FreeCAD/FreeCAD/pull/13287)
-   FreeCAD enthält jetzt eine neue BIM-Beispieldatei. [Pull-Request #14937](https://github.com/FreeCAD/FreeCAD/pull/14937)
-   Der neue Arbeitsbereich BIM stellt auch eine Serie neuer Verwaltungswerkzeuge zur Verfügung, die beim Einrichten eines Projekts unterstützen oder beim Verwalten größerer Mengen von IFC-Eigenschaften eines Objekts. Mehr Informationen gibt es auf der Seite [Arbeitsbereich BIM](BIM_Workbench/de.md).
-   [IfcOpenShell](IfcOpenShell/de.md), eine weitere quelloffene Software, die für die Arbeit mit IFC-Dateien in FreeCAD benötigt wird, ist jetzt mit allen offiziellen Installationspaketen gebündelt, die durch das FreeCAD-Team erhältlich sind. Bezieht man die Software von Drittanbietern, wie einer Linux-Distribution, wo IfcOpenShell noch nicht als offizielles Paket enthalten ist, lässt es sich mit Werkzeugen, die der Arbeitsbereich BIM mitbringt, herunterladen und installieren. Und wenn man keine Verwendung für IFC hat, arbeitet der Arbeitsbereich BIM auch ohne IfcOpenShell 100-prozentig.
-   Die Symbolleisten und Menüs des Arbeitsbereichs BIM wurden überarbeitet. [Pull-Request #14087](https://github.com/FreeCAD/FreeCAD/pull/14087)



## Arbeitsbereich CAM 

-   Der Arbeitsbereich Path heißt jetzt CAM. [Pull-Request #12665](https://github.com/FreeCAD/FreeCAD/pull/12665)



### Weitere CAM-Verbesserungen 

-   Rest machining wurde reimplementiert, um Eingaben aus dem G-code früherer Arbeitsgänge aufzunehmen (anstatt die internen Inhalte von [Area](CAM_Area/de.md)-Arbeitsabläufen zu verwenden). Dies ermöglicht die Unterstützung von rest machining in Area-Arbeitsabläufen nach Nicht-Area-Arbeitsabläufen (most notably Adaptive). [Pull-Request #11939](https://github.com/FreeCAD/FreeCAD/pull/11939)
-   G43-Werkzeughöhenausgleich (tool height compensation) wurde zum CAM-Post-Processor centroid hinzugefügt. [Pull-Request #12652](https://github.com/FreeCAD/FreeCAD/pull/12652)
-   Eine Option *Feed retract* wurde zu den Eigenschaften der Bohrvorgänge für Reiben und Bohren hinzugefügt.[Pull-Request #13254](https://github.com/FreeCAD/FreeCAD/pull/13254)
-   Ein neuer CAM-Simulator, der auf Low-level-OpenGL-Funktionen basiert (schneller und präziser), wurde hinzugefügt. [Pull-Request #13884](https://github.com/FreeCAD/FreeCAD/pull/13884) und [Pull-Request #15597](https://github.com/FreeCAD/FreeCAD/pull/15597)
-   Der Vorgang [VGravur](CAM_Vcarve/de.md) wurde überarbeitet um Funktionen hinzuzufügen, die in anderer CAM-Software normalerweise vorhanden sind (Step down, Finishing pass, Head movement optimization und die Methode debugVoronoi), die es ermöglichen die Qualität der gravierten Oberfläche erheblich zu verbessern und gleichzeitig die Graviergeschwindigkeit um 50% zu steigern. [Pull-Request #14093](https://github.com/FreeCAD/FreeCAD/pull/14093)
-   Maschinenfähige Material-Modelle wurden neben einigen Werkstoffen hinzugefügt. [Pull-Request #14460](https://github.com/FreeCAD/FreeCAD/pull/14460), [Pull-Request #15910](https://github.com/FreeCAD/FreeCAD/pull/15910) und [Pull-Request #16021](https://github.com/FreeCAD/FreeCAD/pull/16021)



## Arbeitsbereich Draft 

-   Eine Option für die Ausrichtung und mehrere zugehörige Eigenschaften wurden zur [Draft Textform](Draft_ShapeString/de.md) hinzugefügt. [Pull-Request #10233](https://github.com/FreeCAD/FreeCAD/pull/10233)
-   [Radiale Maße](Draft_Dimension/de#Anwendung_radiales_Maß.md) zeigen jetzt nur noch eine Pfeilspitze.[Pull-Request #10655](https://github.com/FreeCAD/FreeCAD/pull/10655)
-   Eine Eigenschaft *Oblique Angle* (schiefer Winkel) wurde zu [Draft Textform](Draft_ShapeString/de.md) hinzugefügt. [Pull-Request #10783](https://github.com/FreeCAD/FreeCAD/pull/10783)
-   Unterstützung für Hyperlinks wurde hinzugefügt. Hyperlinks zu lokalen und entfernten Dateien und URLs, in [Draft-Texten](Draft_Text.md) und [Draft Beschreibungen](Draft_Label.md) können aus ihrem Kontextmenü in der [Baumansicht](Tree_view/de.md) oder [3D-Ansicht](3D_view.md) geöffnet werden. [Pull-Request #10878](https://github.com/FreeCAD/FreeCAD/pull/10878)
-   Der Code von [Draft Arbeitsebene](Draft_SelectPlane/de.md) wurde überarbeitet. Es gibt jetzt eine Arbeitsebene pro 3D-Ansicht. [Pull-Request #11010](https://github.com/FreeCAD/FreeCAD/pull/11010)
-   Die Bauteilhistorie-Funktion und die Ausrichtungsoptionen des Befehls [Draft EbeneAuswählen](Draft_SelectPlane/de.md) wurden verbessert. [Pull-Request #11062](https://github.com/FreeCAD/FreeCAD/pull/11062)
-   Das Verhalten des [Draft-Rasters](Draft_ToggleGrid.md) wurde verbessert. Seine Sichtbarkeit wird jetzt in jeder 3D-Ansicht gespeichert. Wird der Arbeitsbereich gewechselt, werden alle Raster ausgeblendet (Es gibt einen [Fine-Tuning](Fine-tuning/de.md)-Parameter, um dies zu deaktivieren). [Pull-Request #11336](https://github.com/FreeCAD/FreeCAD/pull/11336)
-   Die Draft-Einstellungen wurden geprüft und verbessert. Einige Voreinstellungen wurden hinzugefügt, veraltete Voreinstellungen wurden entfernt. Die Seiten im [Voreinstellungseditor](Preferences_Editor/de.md) wurden neu angeordnet und zeigen jetzt Einheiten an, wo es passt. Ein Neustart von FreeCAD nach Anpassung der Draft-Einstellungen ist nicht mehr nötig. [Pull request #11379](https://github.com/FreeCAD/FreeCAD/pull/11379), [Pull-Request #11503](https://github.com/FreeCAD/FreeCAD/pull/11503), [Pull-Request #11512](https://github.com/FreeCAD/FreeCAD/pull/11512), [Pull-Request #11550](https://github.com/FreeCAD/FreeCAD/pull/11550), [Pull-Request #11579](https://github.com/FreeCAD/FreeCAD/pull/11579), [Pull-Request #11585](https://github.com/FreeCAD/FreeCAD/pull/11585), [Pull-Request #11677](https://github.com/FreeCAD/FreeCAD/pull/11677), [Pull-Request #11694](https://github.com/FreeCAD/FreeCAD/pull/11694) und [Pull-Request #16603](https://github.com/FreeCAD/FreeCAD/pull/16603)
-   Eine neue Einstellung *Mausverzögerung* (Mouse delay) wurde den Draft-Eintellungen unter Allgemein hinzugefügt. Ist sie nicht Null (Standardwert ist 1 s), wird die Mausbewegung nach jeder Zahleneingabe in einem der Eingabefelder des Aufgaben-Bereichs deaktiviert; dies verhindert die Veränderung des Wertes für eine bestimmte Dauer in Sekunden. Wird ein sehr hoher Wert eingestellt, deaktiviert dies die Mausbewegung praktisch bis der Befehl beendet ist. [Pull-Request #12624](https://github.com/FreeCAD/FreeCAD/pull/12624)
-   Eine Schaltfläche zum schnellen Ändern der Rasterfarbe wurde zum Aufgaben-Bereich des Befehls [Draft EbeneAuswählen](Draft_SelectPlane/de.md) hinzugefügt. [Pull-Request #13051](https://github.com/FreeCAD/FreeCAD/pull/13051)
-   Eine Eigenschaft *Fuse* wurde [Draft PunktAnordnung](Draft_PointArray/de.md), [Draft PfadAnordnung](Draft_PathArray.md) und Draft PathTwistedArrays hinzugefügt. [Pull-Request #13172](https://github.com/FreeCAD/FreeCAD/pull/13172) and [Pull-Request #13191](https://github.com/FreeCAD/FreeCAD/pull/13191)
-   Die Schaltfläche des Befehls [Toggle grid](Draft_ToggleGrid/de.md) verhält sit jetzt wie ein Umschalter mit visueller Rückmeldung zum Status des Rasters (sichtbar oder ausgeblendet). [Pull-Request #14452](https://github.com/FreeCAD/FreeCAD/pull/14452)



### Weitere Draft-Verbesserungen 

-   Der [Draft Flächenbinder](Draft_Facebinder/de.md) kann jetzt Flächen verarbeiten, die zu Verknüpfungen gehören oder zu Flächen, die in [Std Parts](Std_Part/de.md) eingebettet sind. [Pull-Request #11081](https://github.com/FreeCAD/FreeCAD/pull/11081)
-   Mehrere Einstellungen wurden zum Befehl [Draft StilFestlegen](Draft_SetStyle.md) hinzugefügt. [Pull-Request #11593](https://github.com/FreeCAD/FreeCAD/pull/11593), [Pull-Request #11694](https://github.com/FreeCAD/FreeCAD/pull/11694) und [Pull-Request #13914](https://github.com/FreeCAD/FreeCAD/pull/13914)
-   Einstellungen wurden auch zum Befehl [Draft StilAnwenden](Draft_ApplyStyle.md) hinzugefügt. [Pull-Request #11610](https://github.com/FreeCAD/FreeCAD/pull/11610) und [Pull-Request #13914](https://github.com/FreeCAD/FreeCAD/pull/13914)
-   Einrasten, Bearbeiten und Tracker-Markerkierungen verwenden jetzt die Voreinstellung [Markergröße](Preferences_Editor/de#3D-Viewer.md). [Pull-Request #11688](https://github.com/FreeCAD/FreeCAD/pull/11688) und [Pull-Request #16603](https://github.com/FreeCAD/FreeCAD/pull/16603)
-   Einige Draft-Symbole wurden geändert, um ihr Aussehen zu verbessern. [Pull-Request #13585](https://github.com/FreeCAD/FreeCAD/pull/13585)
-   Das [Draft Layer](Draft_Layer/de.md)-Objekt wurde für das neue Material-Handling-System aktualisiert. Es hat jetzt eine Eigenschaft *Shape Appearance* und eine Eigenschaft *Override Shape Appearance Children*. [Pull-Request #13949](https://github.com/FreeCAD/FreeCAD/pull/13949)
-   [Draft-Verrundungen](Draft_Fillet/de.md) können jetzt auch auf Kreisbögen angewendet werden. [Pull-Request #14774](https://github.com/FreeCAD/FreeCAD/pull/14774)



## Arbeitsbereich FEM 

+++
| <img alt="" src=images/FEM_better_legend_labels_relnotes_1.0.JPG  style="width:384px;"> | Die Position der Beschriftung der Farblegende wurde angepasst, damit die oberen weniger anfällig dafür sind, vom Navigationswürfel verdeckt zu werden. Die Voreinstellungen für Schriftart und Farbe der Beschriftung wurden für eine bessere Sichtbarkeit angepasst und Voreinstellungen wurden hinzugefügt, die eine Anpassung von Farbe und Größe der Beschriftung ermöglichen. [Pull-Request #10552](https://github.com/FreeCAD/FreeCAD/pull/10552) |
+++

+++
| <img alt="" src=images/FEM_stress_component_linearization_relnotes_1.0.png  style="width:384px;"> | Der Befehl [FEM PostFilterLinearizedStresses](FEM_PostFilterLinearizedStresses/de.md) kann jetzt die Spannungstensor-Komponenten für linearisierte Spannungsberechnungen verwenden. Vorher konnten nur Von Mises- und Tresca-Spannung sowie (größte/mittlere/kleinste) Hauptspannungen hierfür verwendet werden. [Pull-Request #11724](https://github.com/FreeCAD/FreeCAD/pull/11724) |
+++

+++
| <img alt="" src=images/Cyclic_symmetry_relnotes_1.0.jpg  style="width:384px;"> | Unterstützung für zyklische Symmetry über die [Randbedingung Verbinder](FEM_ConstraintTie/de.md) in CalculiX wurde hinzugefügt, und ermöglicht Modelle zu analysieren, die aus rotierend wiederholten Symmetrieobjekten eines einzelnen Sektors aufgebaut sind. [Pull-Request #12289](https://github.com/FreeCAD/FreeCAD/pull/12289) |
+++

+++
| <img alt="" src=images/2D_analyses_relnotes_1.0.png  style="width:384px;"> | Unterstützung für 2D-Analysen (ebener Spannungszustand (plane stress), ebener Verformungszustand (plane strain) und achsensymmetrisch) wurde für den Gleichungslöser [CalculiX](FEM_SolverCalculixCxxtools/de.md) hinzugefügt. Sie werden auf gleiche Weise konfiguriert, wie Simulationen mit Schalenelementen, aber es gibt ein paar zusätzliche Einschränkungen, die auf der zuvor erwähnten Wiki-Seite beschrieben werden. Die neue Option *Model Space* muss richtig gesetzt werden. [Pull-Request #12562](https://github.com/FreeCAD/FreeCAD/pull/12562) |
+++

+++
| <img alt="" src=images/Hex_subdivision_relnotes_1.0.png  style="width:384px;"> | Als ersten Schritt zur Unterstützung von Würfelelementen (Hexaeder-Elemente), ist ihre Erstellung mit der Unterteilungstechnik von Gmsh zu sehen, die jetzt Dank der neuen Gmsh-Eigenschaft *Subdivision Algorithm* zur Verfügung steht. Sie kann auch zur Erstellung von vierseitigen Elementen eingesetzt werden. [Pull-Request #12698](https://github.com/FreeCAD/FreeCAD/pull/12698) |
+++

+++
| <img alt="" src=images/Pipeline_colors_relnotes_1.0.png  style="width:384px;"> | Neue Ansicht-Eigenschaften wurden zu den Ergebnis-Pipeline-Objekten hinzugefügt. Farbe und Breite von Netzkanten können jetzt für den Modus *Surface with Edges* angepasst werden. Die Knotengröße kann jetzt für den Modus *Nodes* angepasst werden. Es gibt auch eine Transparenzeinstellung für jeden Modus. [Pull-Request #13066](https://github.com/FreeCAD/FreeCAD/pull/13066) |
+++

+++
| <img alt="" src=images/Constraint_suppress_relnotes_1.0.png  style="width:384px;"> | FEM-Randbedingungen können jetzt unterdrückt werden (ein Rechtsklick auf eine Randbedingung und *Suppress* drücken) und werden dann von den Gleichungslösern ignoriert. Auf diesem Wege ist es möglich, den Analyseaufbau zu verändern, ohne die gerade nicht benötigten Randbedingungen löschen zu müssen. [Pull-Request #12359](https://github.com/FreeCAD/FreeCAD/pull/12359) |
+++

+++
| <img alt="" src=images/Rigid_body_relnotes_1.0.JPG  style="width:384px;"> | Unterstützung für CalculiX\' [Randbedingung Starrer Körper](FEM_ConstraintRigidBody/de.md) wurde hinzugefügt und ermöglicht es endlich die Verdrehung beliebiger Komponenten zu simulieren und u.a. fern angreifende Lasten anzuwenden.[Pull-Request #13900](https://github.com/FreeCAD/FreeCAD/pull/13900) |
+++



### Weitere FEM-Verbesserungen 

-   Der Menüeintrag *Modell → Randbedingungen ohne Löser* wurde aus der Benutzerschnittstelle (GUI) entfernt. die gelisteten Randbedingungen konnten nicht verwendet werden. [Pull-Request #10457](https://github.com/FreeCAD/FreeCAD/pull/10457) and [Pull-Request #10459](https://github.com/FreeCAD/FreeCAD/pull/10459)
-   Das Wort \"constraint\" wurde aus den Namen und Beschreibungen der meisten Elemente des Arbeitsbereichs FEM entfernt, um eine korrekte Benennung sicherzustellen. Die (englischen) Namen wurden so geändert, dass sie den Normen der FEA-Industrie entsprechen und für neue Anwender intuitiv benutzbar sind. [Pull-Request #10519](https://github.com/FreeCAD/FreeCAD/pull/10519) und [Pull-Request #10799](https://github.com/FreeCAD/FreeCAD/pull/10799)

(die Übersetzungen sind noch anzupassen)

-   Neue Symbole wurden für [Solver CalculiX Standard](FEM_SolverCalculixCxxtools/de.md), [Solver job control](FEM_SolverControl/de.md) und [Run solver calculations](FEM_SolverRun/de.md) hinzugefügt, um sie intuitiver bedinbar zu machen. [Pull-Request #10885](https://github.com/FreeCAD/FreeCAD/pull/10885)
-   Löser CalculiX (new framework) wurde aus der Benutzerschnittstelle entfernt, da er unfertig und im Moment unnötig ist. Die zugehörigen Beispiele wurden auch entfernt. [Pull-Request #10823](https://github.com/FreeCAD/FreeCAD/pull/10823) und [Pull-Request #12876](https://github.com/FreeCAD/FreeCAD/pull/12876)
-   Das Layout einiger Aufgaben-Bereiche der Nachbereitungswerkzeuge wurde verbessert, um ihren horizontalen Platzverbrauch zu reduzieren. [Pull-Request #11066](https://github.com/FreeCAD/FreeCAD/pull/11066)
-   Der Aufgaben-Bereich von [FEM RandbedingungTemperatur](FEM_ConstraintTemperature.md) wurde überarbeitet, um Fehler bei der Bearbeitung dieser Funktion zu beheben.[Pull-Request #11126](https://github.com/FreeCAD/FreeCAD/pull/11126)
-   Ein alter Fehler der Funktion [FEM NachbereitungDataAlongLine](FEM_PostFilterDataAlongLine.md), der nur die Ausgabe der Größe aber nicht die der Vektorkomponenten ermöglichte wurde endlich behoben. [Pull-Request #10992](https://github.com/FreeCAD/FreeCAD/pull/10992)
-   [FEM RandbedingungKraft](FEM_ConstraintForce.md) and [FEM RandbedingungDruck](FEM_ConstraintPressure.md) wurden überholt, damit sie quellcodeseitig besser funktionieren. [Pull-Request #10935](https://github.com/FreeCAD/FreeCAD/pull/10935) and [Pull request #10923](https://github.com/FreeCAD/FreeCAD/pull/10923)
-   Der [FEM NachbereitungDataAtPoint](FEM_PostFilterDataAtPoint.md) hat jetzt eine Eigenschaft PointSize, um die Größe des Punktsymbols für eine bessere Sichtbarkeit ändern zu können [Pull-Request #11054](https://github.com/FreeCAD/FreeCAD/pull/11054)
-   Der Befehl [FEM Netzbereich](FEM_MeshRegion/de.md) wurde für bessere Verständlichkeit in der Benutzerschnittstelle (GUI) in *FEM Netz aufbereiten* umbenannt (der Name des Befehls bleibt unverändert). [Pull-Request #11489](https://github.com/FreeCAD/FreeCAD/pull/11489)
-   Die Größe der Schwerkraftbeschleunigung kann jetzt unter Verwendung der Eigenschaften von [FEM RandbedingungEigengewicht](FEM_ConstraintSelfWeight/de.md) angepasst werden. [Pull-Request #12044](https://github.com/FreeCAD/FreeCAD/pull/12044)
-   [Randbedingung Kontakt](FEM_ConstraintContact/de.md) und [Randbedingung Verbinder](FEM_ConstraintTie/de.md) wurden deutlich verbessert. Kontaktsteifigkeit (contact stiffness) verwendet jetzt die korrekte Einheit und ein Haftreibungswinkel (stick slope value) kann für Reibung (friction) in der Randbedingung Kontakt angegeben werden. Außerdem kann für die Randbedingung Kontakt eine Abstandskorrektur (clearance adjustment) angegeben werden, während für Randbedingung Verbinder ein () adjustment aktiviert oder deaktiviert werden kann. [Pull-Request #12133](https://github.com/FreeCAD/FreeCAD/pull/12133)
-   PaStiX und Pardiso wurden zu den unterstützten [CalculiX-Matrizen-Lösern](FEM_SolverCalculixCxxtools/de#Eigenschaten.md) hinzugefügt. Sie sind die schnellsten ccx-Löser aber die Einsatzmöglichkeiten hängen von der Binärversion von CalculiX und zusätzlich verfügbaren Bibliotheken ab. [Pull-Request #12478](https://github.com/FreeCAD/FreeCAD/pull/12478)
-   Die Eigenschaft *Beam Reduced Integration* (standardmäßig auf *true* gesetzt) wurde zu den [CalculiX-Löser-Einstellungen](FEM_SolverCalculixCxxtools/de.md) hinzugefügt. Sie stellt ein reduced integration scheme für Stabelemente zur Verfügung und ermöglicht so, den pipe beam-Abschnitt zu verwenden und Genauigkeitsprobleme bei Analysen mit u.a. Plastizität zu eliminieren. [Pull-Request #12513](https://github.com/FreeCAD/FreeCAD/pull/12513)
-   Das nicht fertiggestellte Werkzeug [Nodes set](FEM_CreateNodesSet/de.md) wurde aus der Benutzerschnittstelle entfernt. Es konnte nicht verwendet werden. [Pull-Request #12611](https://github.com/FreeCAD/FreeCAD/pull/12611)
-   Das CalculiX-Analyseverfahren Check Mesh erstellt die Ergebnisnetze jetzt korrekt. [Pull-Request #12612](https://github.com/FreeCAD/FreeCAD/pull/12612)
-   Im Aufgaben-Dialog wurde verdeutlicht, dass der von pipe beam section verwendete Durchmesser der Außendurchmesser ist. [Pull-Request #12609](https://github.com/FreeCAD/FreeCAD/pull/12609)
-   Die Eigenschaft *Beam Shell Result Output 3D* des Gleichnungslösers [CalculiX](FEM_SolverCalculixCxxtools.md) wird jetzt standardmäßig auf *true* gesetzt, um Ergebnisse für Balkenelemente und aussagekräftige Ergebnisse für Schalenelemente zu liefern. [Pull-Request #12493](https://github.com/FreeCAD/FreeCAD/pull/12493)
-   Symbole von Analyseelementen werden jetzt korrekt positioniert, wenn der Körper (oder Part-Behälter) eine geänderte Eigenschaft Placement enthält. [Pull-Request #12527](https://github.com/FreeCAD/FreeCAD/pull/12527)
-   [Pressure load](FEM_ConstraintPressure/de.md) funktioniert jetzt korrekt für Schalenelemente, unabhängig von der Einstellung der Mesh-Groups. Diese Einstellung kann in den Voreinstellungen angepasst werden. [Pull-Request #12437](https://github.com/FreeCAD/FreeCAD/pull/12437)
-   Einfaches Härten (simple hardening) in [FEM MaterialMechanicalNonlinear](FEM_MaterialMechanicalNonlinear/de.md) wurde in isotropes Härten (isotropic hardening) umbenannt. Außerdem wurde kinematisches Härten (kinematic hardening) hinzugefügt. [Pull-Request #12666](https://github.com/FreeCAD/FreeCAD/pull/12666)
-   Jetzt wird geometric nonlinearity automatisch aktiviert und ist erforderlich, wenn ein nicht lineares Material eingesetzt wird. Sie sind unabhängige Formen von Nichtlinearität. [Pull-Request #12703](https://github.com/FreeCAD/FreeCAD/pull/12703)
-   Gemischte Netze, die sowohl aus dreieckigen wie auch viereckigen Elementen bestehen, werden jetzt in der Ergebnis-Pipeline korrekt dargestellt. [Pull-Request #12740](https://github.com/FreeCAD/FreeCAD/pull/12740)
-   Die Eigenschaft *Output Frequency* wurde den Einstellungen des Gleichungslösers [CalculiX](FEM_SolverCalculixCxxtools/de.md) hinzugefügt. Sie legt die Frequenz von output writing in increments fest. [Pull-Request #12672](https://github.com/FreeCAD/FreeCAD/pull/12672)
-   Es können jetzt vierseitige Elemente zweiter Ordnung erstellt werden. Zuvor hat die Gmsh-Einstellung 2nd order vierseitige Elemente erster Ordnung erstellt, da ein Gmsh -Befehl *SecondOrderIncomplete* fehlte, der jetzt intern eingesetzt wird. Diese Elemente können auch für 2D-Analysen eingesetzt werden. [Pull-Request #12698](https://github.com/FreeCAD/FreeCAD/pull/12698) und [Pull-Request #12774](https://github.com/FreeCAD/FreeCAD/pull/12774)
-   Die Ermittlung der Ausrichtung von Balkenquerschnitten wurde teilweise korrigiert. Aufgrund eines Fehlers in der aktuellen Ausgabe von CalculiX können noch immer Probleme mit einigen Ausrichtungen auftreten. [Pull-Request #12833](https://github.com/FreeCAD/FreeCAD/pull/12833)
-   Die FEM-Kragbalken-Beispiele auf der Startseite wurden aktualisiert und ein neues, das 1D-Elemente verwendet, wurde hinzugefügt. [Pull-Request #12871](https://github.com/FreeCAD/FreeCAD/pull/12871)
-   Das Format in dem FreeCAD die Randbedingung [Kraft](FEM_ConstraintForce/de.md) schreibt, ist jetzt kompatibel mit dem CalculiX-Format und behebt seltene Probleme mit zu langen Zahlen. [Pull-Request #12932](https://github.com/FreeCAD/FreeCAD/pull/12932)
-   Es ist jetzt möglich, die [Results-Pipeline](FEM_PostPipelineFromResult/de.md) im VTK-Format auszugeben. [Pull-Request #12987](https://github.com/FreeCAD/FreeCAD/pull/12987)
-   Neue Eigenschaften zur Steuerung der Schrittweite wurden den Einstellungen des Gleichungslösers [CalculiX](FEM_SolverCalculixCxxtools.md) hinzugefügt. Zurzeit kann man zusätzlich zur Größe der Startschrittweite und der Dauer eines Schrittes die kleinste und die größte Schrittweite festlegen. Die Eigenschaft *Iterations Thermo Mech Maximum* wurde in *Iterations Maximum* umbenannt, da sie jetzt auch für statische (nicht thermomechanische) Analysen eingesetzt werden kann. [Pull-Request #12662](https://github.com/FreeCAD/FreeCAD/pull/12662)
-   Der Standardwert für [Elementgeometrie2D](FEM_ElementGeometry2D/de.md) wurde von 20 mm auf 1 mm geändert, da dies in der Praxis sinnvoller ist. [Pull-Request #13077](https://github.com/FreeCAD/FreeCAD/pull/13077)
-   Viele FEM-Symbole wurden erheblich verbessert, um Ähnlichkeiten zu reduzieren und zu verdeutlichen, was die Werkzeuge machen. [Pull-Request #13130](https://github.com/FreeCAD/FreeCAD/pull/13130)
-   Die Eigenschaft *Thermo Mech Type* wurde den Einstellungen des Gleichungslösers [CalculiX](FEM_SolverCalculixCxxtools.md) hinzugefügt. Dies ermöglicht eine reguläre (gekoppelte) thermomechanische Analyse in eine entkoppelte umzustellen oder in eine mit reiner Wärmeübertragung. [Pull-Request #13296](https://github.com/FreeCAD/FreeCAD/pull/13296)
-   Die Eigenschaft *Min. Size* wurde für den Vernetzer [Netgen](FEM_MeshNetgenFromShape.md) hinzugefügt, um die Erzeugung zu kleiner Elemente während der Vernetzung komplexerer Geometrien zu verhindern. [Pull-Request #12794](https://github.com/FreeCAD/FreeCAD/pull/12794)
-   Ein altes Problem mit einer nicht funktionierenden Eigenschaft zum Skalieren von Symbolen für FEM-Randbedingungen wurde endlich behoben und die Eigenschaft *Scale* kann jetzt zum Einstellen der Größe von Symbolen einer ausgewählten Randbedingung eingesetzt werden.[Pull-Request #13274](https://github.com/FreeCAD/FreeCAD/pull/13274)
-   Das automatische Skalieren von FEM-Randbedingungen wurde verbessert, um besser mit sehr kleinen und sehr großen Objekten umgehen zu können. [Pull-Request #13586](https://github.com/FreeCAD/FreeCAD/pull/13586)
-   [Wärmestrombelastung](FEM_ConstraintHeatflux/de.md) hat jetzt einen Strömungsmodus für Wärmestrahlung (radiation heat flux mode), um Oberflächenstrahlung in die Umgebung zu modellieren. [Pull-Request #13466](https://github.com/FreeCAD/FreeCAD/pull/13466)
-   Einige nicht verwendete Ansicht-Eigenschaften von Randbedingungssymbolen wurden entfernt. [Pull-Request #13569](https://github.com/FreeCAD/FreeCAD/pull/13569)
-   Neue Ansicht-Eigenschaften (mit der Haupteigenschaft *Color Mode*) wurden zu FEM-Netzobjekten hinzugefügt, so dass jetzt benutzerdefinierte Farben und Transparenzeinstellungen gespeichert und wiederhergestellt werden können. [Pull-Request #13698](https://github.com/FreeCAD/FreeCAD/pull/13698)
-   Jetzt wird standardmäßig nur noch der zuletzt hinzugefügte Filter jeder Ergebnis-Pipeline angezeigt. [Pull-Request #13820](https://github.com/FreeCAD/FreeCAD/pull/13820)
-   Die Tipps in den Aufgaben-Bereichen mehrerer Randbedingungen wurden geändert, um jetzt die Regeln zur Geometrieauswahl für die einzelnen Randbedingungen wiederzugeben. [Pull-Request #13921](https://github.com/FreeCAD/FreeCAD/pull/13921) und [Pull-Request #14002](https://github.com/FreeCAD/FreeCAD/pull/14002)
-   Unterstützung für Wärmefluss-Ergebnisse aus thermomechanischen Analysen wurde den Ergebnis-Pipelines hinzugefügt. [Pull-Request #14019](https://github.com/FreeCAD/FreeCAD/pull/14019)
-   Die [RandbedingungSectionPrint](FEM_ConstraintSectionPrint/de.md) wurde verbessert und fügt die Unterstützung für Wärmefluss- und Zugspannungsergebnisse hinzu (steht noch nicht zur Verfügung, da 3D-Fluid-Analysen mit CalculiX noch nicht implementiert sind). [Pull-Request #14046](https://github.com/FreeCAD/FreeCAD/pull/14046)
-   [Body heat source](FEM_ConstraintBodyHeatSource/de.md) kann jetzt mit CalculiX verwendet werden und hat zwei Eingabemodi - dissipation rate \[W/kg\] und total power \[W\]. [Pull-Request #14417](https://github.com/FreeCAD/FreeCAD/pull/14417)
-   Die Rotations-Eigenschaften des [lokalen Koordinatensystems](FEM_ConstraintTransform/de.md) wurden für eine vereinheitlichte Bedienung durch eine einzige Eigenschaft *Rotation* ersetzt. [Pull-Request #14353](https://github.com/FreeCAD/FreeCAD/pull/14353)
-   Ein Werkzeug [Erase Elements](FEM_CreateElementsSet/de.md) wurde hinzugefügt, um zu ermöglichen, Elemente eines Netzes auszublenden, das (die?) mit einem Linienzug ausgewählt wurde(n). [Pull-Request #11492](https://github.com/FreeCAD/FreeCAD/pull/11492)
-   Die drei FEM-Beispiele auf der Start-Seite wurden durch ein einziges ersetzt, das alle drei Varianten des Kragbalkenmodells (1D, 2D und 3D) in [Grouppen](Std_Group/de.md)-Containern enthält. [Pull-Request #15786](https://github.com/FreeCAD/FreeCAD/pull/15786)
-   Die überflüssigen *Fix-* Eigenschaften und Checkboxen von [FEM ConstraintDisplacement](FEM_ConstraintDisplacement/de.md) wurden entfernt. [Pull-Request #15531](https://github.com/FreeCAD/FreeCAD/pull/15531)
-   Das Verhalten Der Schaltfläche Abbrechen im Aufgaben-Fenster der Vernetzer [Gmsh](FEM_MeshGmshFromShape/de.md) und [Netgen](FEM_MeshNetgenFromShape/de.md) wurde repariert und kann jetzt verwendet werden, um ein laufendes Vernetzen abzubrechen, was manchmal nötig ist, wenn sich eine zu Beginn getroffene Annahme bezüglich der Elementgröße als zu niedrig herausstellt. Außerdem wurde der Vernetzer Netgen implementiert, und ermöglicht letztlich ihn auf allen Systemen einzusetzen, inklusive Linux. [Pull-Request #16515](https://github.com/FreeCAD/FreeCAD/pull/16515) und [Pull-Request #16433](https://github.com/FreeCAD/FreeCAD/pull/16433)
-   Der 2D-Algorithmus *Quasi-structured Quad*, der dem Vernetzer Gmsh fehlte wurde diesem hinzugefügt zusammen mit anderen Reparaturen. [Pull-Request #15624](https://github.com/FreeCAD/FreeCAD/pull/15624)



## Arbeitsbereich Material 

+++
| <img alt="" src=images/Materials_relnotes_1.0.png  style="width:384px;"> | Das System zum Verarbeiten von Materialdaten, inklusive des Editors, wurde komplett überarbeitet. Weitere diesbezügliche Verbesserungen werden folgen. [Pull-Request #10690](https://github.com/FreeCAD/FreeCAD/pull/10690) |
+++

+++
| <img alt="" src=images/Appearance_preview_relnotes_1.0.png  style="width:384px;"> | Eine Voransicht der Materialdarstellung wurde hinzugefügt, um Materialien auf dieselbe Weise wie im Dokument anzuzeigen. [Pull-Request #11628](https://github.com/FreeCAD/FreeCAD/pull/11628) |
+++

+++
| <img alt="" src=images/Material_appearance_relnotes_1.0.jpg  style="width:384px;"> | Das neue Materialsystem wird jetzt für Darstellungseigenschaften eingesetzt. [Pull-Request #13294](https://github.com/FreeCAD/FreeCAD/pull/13294) |
+++



### Weitere Material-Verbesserungen 

-   Dialoge zum Anzeigen der Darstellungs- und der Materialeigenschaften eines Objekts wurden hinzugefügt und stehen als Werkzeuge *Appearance\...* und *Material\...* zur Verfügung. [Pull-Request #13967](https://github.com/FreeCAD/FreeCAD/pull/13967)



## Arbeitsbereich Part 

+++
| <img alt="" src=images/Part_scale_relnotes_1.0.png  style="width:384px;"> | Das Werkzeug [Part Skalieren](Part_Scale/de.md) wurde hinzugefügt, um das einfache Skalieren von Formen zu ermöglichen, ohne die Werkzeuge des Arbeitsbereichs Draft verwenden zu müssen. [Pull-Request #10583](https://github.com/FreeCAD/FreeCAD/pull/10583) |
+++

+++
| <img alt="" src=images/Part_Mirror_relnotes_1.0.png  style="width:384px;"> | [Part Spiegeln](Part_Mirror/de.md) unterstützt jetzt auch Referenzobjekte wie [Part Ebene](Part_Plane/de.md), um eine beliebige Spiegelebene zusätzlich zu den XY-, XZ- und YZ-Standardebenen festzulegen. [Pull-Request #11535](https://github.com/FreeCAD/FreeCAD/pull/11535) |
+++



### Weitere Part-Verbesserungen 

-   Die Eigenchaft *Frenet* ist jetzt die Standardeinstellung für das Werkzeug [Part Sweep](Part_Sweep.md), um übliche Darstellungsprobleme zu vermeiden.[Pull-Request #11590](https://github.com/FreeCAD/FreeCAD/pull/11590)
-   Ein neues [Befestigungsverfahren](Part_EditAttachment#Attachment_modes/de.md), *Intersection* genannt, wurde zur Engine Line hinzugefügt. Es findet die Schnittlinie zweier ebener Flächen.[Pull-Request #12328](https://github.com/FreeCAD/FreeCAD/pull/12328)
-   Das Werkzeug [Part ProjektionAufOberfläche](Part_ProjectionOnSurface/de.md) ist jetzt parametrisch. [Pull-Request #13158](https://github.com/FreeCAD/FreeCAD/pull/13158)
-   Jetzt verwenden alle Part-Symbole ein blaues Aussehen und für Grundkörper werden dieselben Symbole in der Symbolleiste und in der Baumansicht eingesetzt [Pull-Request #14074](https://github.com/FreeCAD/FreeCAD/pull/14074)
-   Der Befehl [Skizze erstellen](Sketcher_NewSketch/de.md) wurde zu Part-Symbolleiste und -Menü hinzugefügt, da Vorgänge wie Extrudieren normalerweise Skizzen als Ausgangselemente verwenden. [Pull-Request #14318](https://github.com/FreeCAD/FreeCAD/pull/14318)
-   Ein neues [Befestigungsverfahren](Part_EditAttachment/de#Befestigungsverfahren.md), *XY parallel to plane* genannt, wurde zu Engine Plane und Engine 3D hinzugefügt. Dieses ergibt eine Befestigung wie bei *XY des Objekts* aber mit der XY-Ebene so verschoben, dass sie durch einen gewählten Punkt verläuft. Im Gegensatz zum Befestigungsverfahren *Ursprung versetzen*, verschiebt er nicht den Ursprung in 2D bzw. in der Skizze. Er kann mit den Ursprungsebenen, Bezugsebenen und Skizzen verwendet werden aber auch mit jedem anderen Objekt, das eine Eigenschaft *Placement* besitzt. [Pull-Request #14372](https://github.com/FreeCAD/FreeCAD/pull/14372)



## Arbeitsbereich PartDesign 

+++
| <img alt="" src=images/Revolve_options_relnotes_1.0.png  style="width:384px;"> | Weitere Modi wurden zu [Drehkörper](PartDesign_Revolution/de.md) und [Nut](PartDesign_Groove/de.md) hinzugefügt - to first/last, up to face und two dimensions. [Pull-Request #7193](https://github.com/FreeCAD/FreeCAD/pull/7193) |
+++

+++
| <img alt="" src=images/Pad_task_dialog_relnotes_1.0.png  style="width:384px;"> | Die Aufgaben-Dialoge von [Block](PartDesign_Pad/de.md) und [Tasche](PartDesign_Pocket/de.md) wurden verbessert (neu arrangierte UI-Elemente, die Option **Fläche auswählen** bleibt deaktiviert, wenn nicht benötigt usw.). [Pull-Request #10392](https://github.com/FreeCAD/FreeCAD/pull/10392) |
+++

+++
| <img alt="" src=images/Pattern_offset_mode_relnotes_1.0.png  style="width:384px;"> | Ein Versetzen-Modus (offset-mode) wurde dem [Linearen Muster](PartDesign_LinearPattern/de.md) und dem [Polaren Muster](PartDesign_PolarPattern/de.md) hinzugefügt. Der bisherige Modus wurde in **Overall Length/Angle** (Gesamtlänge/-winkel) umbenannt. [Pull-Request #10377](https://github.com/FreeCAD/FreeCAD/pull/10377) |
+++

+++
| <img alt="" src=images/Single_solid_rule_relnotes_1.0.PNG  style="width:384px;"> | Eine experimentelle Unterstützung für mehrteilige Festkörper innerhalb eines [Körpers](PartDesign_Body/de.md) wurde hinzugefügt. Sie kann in den Voreinstellungen (für neue Körper) oder in den Eigenschaften eines existierenden Körpers aktiviert werden. [Pull-Request #10360](https://github.com/FreeCAD/FreeCAD/pull/10360) |
+++

+++
| <img alt="" src=images/Pad_up_to_shape_relnotes_1.0.PNG  style="width:384px;"> | Der Modus *Bis Form* wurde den Werkzeugen Pad und Pocket hinzugefügt und ermöglicht sie mit mehreren Flächen zu begrenzen, im Gegensatz zum Modus *Bis Fläche*, der nur die Auswahl einer einzelnen Fläche erlaubt. [Pull-Request #11392](https://github.com/FreeCAD/FreeCAD/pull/11392) and [Pull-Request #14433](https://github.com/FreeCAD/FreeCAD/pull/14433) |
+++



### Weitere PartDesign-Verbesserungen 

-   Die Option *Dicke nach innen auftragen* im Werkzeug [Dicke](PartDesign_Thickness/de.md) ist jetzt standardmäßig aktiviert. [Pull-Request #7488](https://github.com/FreeCAD/FreeCAD/pull/7488)
-   Bezugspunkte verändern jetzt ihre Farbe, wenn sie hervorgehoben oder ausgewählt werden (wie andere Bezugselemente). [Pull-Request #12439](https://github.com/FreeCAD/FreeCAD/pull/12439)
-   PartDesign-Symbole wurden leicht verbessert. for consistency. [Pull-Request #13109](https://github.com/FreeCAD/FreeCAD/pull/13109)
-   Eine Eigenschaft *Unterdrückt* wurde hinzugefügt, um ein Formelement zeitweilig zu deaktivieren. [Pull-Request #12096](https://github.com/FreeCAD/FreeCAD/pull/12096) and [Pull-Request #12412](https://github.com/FreeCAD/FreeCAD/pull/12412)
-   Die PartDesign-Symbolleisten wurden überarbeitet; Bezugselemente und skizzenbasierte Funktionen wurden jetzt gruppiert, [Part GeometryPrüfen](Part_CheckGeometry/de.md) wurde zur Symbolleiste und zum Menü hinzugefügt; die Symbolleisten wurden in mehrere aufgeteilt, um zu ermöglichen, sie neu anzuordnen.[Pull-Request #13833](https://github.com/FreeCAD/FreeCAD/pull/13833)
-   Jetzt verwenden alle PartDesign-Formelemente dieselben Symbole in der Symbolleiste und in der Baumansicht.[Pull-Request #14074](https://github.com/FreeCAD/FreeCAD/pull/14074)
-   Ein neuer Modus *Transform body* wurde den PartDesign-Werkzeugen zum Spiegeln und Muster Erstellen hinzugefügt, der ermöglicht, die gesamte Form des Basis-Formelements zu verwenden, anstatt nur die individuellen Formen der hinzuzufügenden bzw. abzuziehenden Formelemente.[Pull-Request #12589](https://github.com/FreeCAD/FreeCAD/pull/12589)
-   Das Layout des Dialogs des Werkzeugs [Bohrung](PartDesign_Hole/de.md) wurde verbessert. [Pull-Request #14031](https://github.com/FreeCAD/FreeCAD/pull/14031)
-   Das Werkzeug [Migrieren](PartDesign_Migrate/de.md) wurde aus der Benutzerschnittstelle entfernt, da es nur nützlich war für das Aufbereiten zwischen Versionen, die längst veraltet sind.[Pull-Request #15196](https://github.com/FreeCAD/FreeCAD/pull/15196)



## Arbeitsbereich Sketcher 

+++
| <img alt="" src=images/Arc_helper_relnotes_1.0.png  style="width:384px;"> | Es wurde ein Ergänzungskreis für Bögen implementiert (um das Problem der Randbedingungen, die scheinbar nicht mit diesen verbunden sind, zu lösen) einschließlich des [ Befehls zum Ein-bzw.Ausschalten](Sketcher_ArcOverlay/de.md). [Pull-Request #9703](https://github.com/FreeCAD/FreeCAD/pull/9703) |
+++

   
  <img alt="" src=images/Contextual_dimension_relnotes_1.0.gif  style="width:384px;">Bild anklicken, wenn die Animation nicht automatisch startet.   Ein kontextabhängiges Werkzeug für maßliche Randbedingung wurde hinzugefügt, um schnell und intuitiv unterschiedliche maßliche Randbedingungen festzulegen, mit einem einzigen vielseitigen Werkzeug. [Pull-Request #9810](https://github.com/FreeCAD/FreeCAD/pull/9810)
   

   
  <img alt="" src=images/Tool_parameters_relnotes_1.0.gif  style="width:384px;">Das Bild anklicken, wenn die Animation nicht automatisch startet.   [Werkzeugparameter](Sketcher_Workbench/de#In-Ansicht-Parameter.md) wurden hinzugefügt, die ermöglichen, dass Maße nebenher (während Formen gezeichnet werden) hinzugefügt werden. Abhängig von der Voreinstellung In-Ansicht-Parameter können sie deaktiviert, reduziert auf nur Maße (keine initialen Koordinaten) oder vollständig aktiviert sein. Außerdem wurden Auswahlmöglichkeiten zu den Formwerkzeugen hinzugefügt. Sie können mit der Taste M oder aus einer Ausklappliste im Aufgaben-Bereich ausgewählt werden. Einige Werkzeuge haben zusätzliche Einstellungen in Form von Checkboxen im Aufgaben-Bereich und zusätzliche Tastaturkürzel. Gegenwärtig stehen die neuen Elemente für Punkte, Linien, Kreisbögen, Ellipsen Rechtecke, Vielecke, Nuten und B-Splines zur Verfügung. [Pull-Request #11048](https://github.com/FreeCAD/FreeCAD/pull/11048), [Pull-Request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174) und folgende
   

+++
| <img alt="" src=images/Offset_relnotes_1.0.png  style="width:384px;"> | Ein Werkzeug [Versatzkontur](Sketcher_Offset/de.md) wurde hinzugefügt und ermöglicht Kurven mit konstantem Abstand zu erstellen. [Pull-Request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174) |
+++

+++
| <img alt="" src=images/Three_point_rectangle_relnotes_1.0.png  style="width:384px;"> | Die Variante [Rechteck](Sketcher_CompCreateRectangles/de.md) über drei Punkte wurde in zwei Versionen hinzugefügt: 3 Eckpunkte oder Mittelpunkt und 2 Eckpunkte. [Pull-Request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174) |
+++

+++
| <img alt="" src=images/Arc_slot_relnotes_1.0.png  style="width:384px;"> | Ein Werkzeug [Bogennut](Sketcher_CreateArcSlot/de.md) wurde mit zwei Varianten zum Erstellen gekrümmter Nuten (Runde Enden und gerade Enden) hinzugefügt [Pull-Request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174) |
+++

   
  <img alt="" src=images/Auto_horizontal-vertical_relnotes_1.0.gif  style="width:384px;">Abbildung anklicken, wenn die Animation nicht automatisch startet.   Eine Randbedingung [Horizontal/Vertikal](Sketcher_ConstrainHorVer/de.md) wurde hinzugefügt. Sie fügt automatisch eine Randbedingung HorizontalFestlegen ein, wenn eine Linie eher einer horizontal ausgerichtet ist oder eine Randbedingung VertikalFestlegen, wenn sie eher vertikal ausgerichtet ist. [Pull-Request #11538](https://github.com/FreeCAD/FreeCAD/pull/11538)
   

+++
| <img alt="" src=images/Angle_radius_rendering_relnotes_1.0.png  style="width:384px;"> | Die Darstellung der Randbedingungen für Winkel und Radius wurde verbessert. Randbedingungen für Winkel haben jetzt richtige Maßhilfslinien. [Pull-Request #11507](https://github.com/FreeCAD/FreeCAD/pull/11507) |
+++

+++
| <img alt="" src=images/Polar_transform_relnotes_1.0.png  style="width:384px;"> | Ein Werkzeug [Schwenken](Sketcher_Rotate/de.md) wurde hinzugefügt, das das Schwenken von Sketcher-Geometrien ermöglicht sowie das Erstellen von kreisförmigen Mustern aus ihnen. [Pull-Request #11264](https://github.com/FreeCAD/FreeCAD/pull/11264) |
+++

   
  <img alt="" src=images/Sketcher_copy-cut-paste_relnotes_1.0.gif  style="width:384px;">Auf die Abbildung klicken, wenn die Animation nicht startet.   Es ist jetzt möglich Skizzengeometrie (mit Randbedingungen) auszuschneiden bzw. zu kopieren und einzufügen, indem die üblichen Tastaturkürzel : Ctrl+C, Ctrl+X and Ctrl+V verwendet werden. Nicht nur innerhalb einer einzelnen Skizze, sondern auch zwischen verschiedenen Skizen oder sogar zwischen verschiedenen Instanzen von FreeCAD. Die Geometrie wird in Form von Python-Befehlen kopiert, so kann sie auch auf anderen Wegen verwendet werden (z.B. im Forum geteilt werden). [Pull-Request #11537](https://github.com/FreeCAD/FreeCAD/pull/11537)
   

+++
| <img alt="" src=images/Scale_transform_relnotes_1.0.png  style="width:384px;"> | Ein Werkzeug zum [Skalieren](Sketcher_Scale/de.md) wurde hinzugefügt und ermöglicht, die Skalierung von Sketcher-Geometrie zu verändern, durch Auswahl eines Mittelpunktes und eines Skalierungsfaktors oder durch zwei Referenzpunkte. [Pull-Request #11265](https://github.com/FreeCAD/FreeCAD/pull/11265) |
+++

   
  <img alt="" src=images/B-spline_tangency_relnotes_1.0.gif  style="width:384px;">Bild anklicken, wenn die Animation nicht startet.   Tangetialität zu B-Spline-Kanten wurde hinzugefügt, sodass die Notwendigkeit entfällt, stattdessen Endpunkte und verschiedene Hilfskonstruktionen zu verwenden. [Pull-Request #11853](https://github.com/FreeCAD/FreeCAD/pull/11853)
   

+++
| <img alt="" src=images/Sketcher_translate_relnotes_1.0.png  style="width:384px;"> | Die Werkzeuge [RechteckigeAnordnung](Sketcher_RectangularArray/de.md), [Verschieben](Sketcher_Move/de.md), [Kopieren](Sketcher_Copy/de.md) und [Klonen](Sketcher_Clone/de.md) wurden durch ein einziges Werkzeug [Array transform](Sketcher_Translate/de.md) (Sketcher Anordnen) ersetzt. [Pull-Request #11267](https://github.com/FreeCAD/FreeCAD/pull/11267) |
+++

+++
| <img alt="" src=images/Sketcher_chamfer_relnotes_1.0.png  style="width:384px;"> | Ein Werkzeug [Fase](Sketcher_CreateChamfer/de.md) wurde hinzugefügt, mit der Option in den Modus [Verrundung](Sketcher_CreateFillet.md) zu wechseln. Außerdem gibt es das eck-erhaltende Verrundungswerkzeug nicht mehr. Eine Option *Eckpunkt erhalten* (Standardmäßig aktiviert) wurde dem Werkzeug [Sketcher VerrundungErstellen](Sketcher_CreateFillet/de.md) hinzugefügt. [Pull-Request #12898](https://github.com/FreeCAD/FreeCAD/pull/12898) |
+++

   
  <img alt="" src=images/New_symmetry_relnotes_1.0.gif  style="width:384px;">Auf das Bild klicken, wenn die Animation nicht automatisch startet.   Das Werkzeug [Symmetry](Sketcher_Symmetry.md) wurde überarbeitet. Es wird jetzt durch Auswählen der Geometrie und abschließend einer Linie oder eines Punktes, über die/den gespiegelt wird, gestartet. Eine Vorschau wird angezeigt und das Verhalten des Werkzeugs kann durch Werkzeugeinstellungen gesteuert werden. [Pull-Request #11853](https://github.com/FreeCAD/FreeCAD/pull/11853)
   

   
  <img alt="" src=images/Auto_midpoint_relnotes_1.0.gif  style="width:384px;">Bild anklicken, wenn die Animation nicht startet.   Die Randbedingung [SymmetrieFestlegen](Sketcher_ConstrainSymmetric/de.md) wird jetzt automatisch angelegt, wenn der Mittelpunkt einer Linie ausgewählt wird. [Pull-Request #13147](https://github.com/FreeCAD/FreeCAD/pull/13147)
   

+++
| <img alt="" src=images/Sketcher_arc_length_relnotes_1.0.png  style="width:384px;"> | Die Randbedingung [AbstandFestlegen](Sketcher_ConstrainDistance/de.md) Kann jetzt zum Festlegen von Bogenlängen eingesetzt werden (ein Kreisbogen muss vorausgewählt sein). [Pull-Request #12602](https://github.com/FreeCAD/FreeCAD/pull/12602) |
+++

+++
| <img alt="" src=images/Point_color_relnotes_1.0.png  style="width:384px;"> | Die Farbdarstellung von Punkten wurde geändert und hängt jetzt davon ab, ob es ein normaler Punkt bzw, Endpunkt ist (weiß, jetzt Standardfarbe, wenn das Werkzeug [PunktErstellen](Sketcher_CreatePoint/de.md) verwendet wird), ein Hilfspunkt bzw. Mittelpunk (blau) oder ein Punkt, der deckungsgleich (koinzident) mit einem anderen liegt (rot). [Pull-Request #13098](https://github.com/FreeCAD/FreeCAD/pull/13098) |
+++

   
  <img alt="" src=images/Trim_drag_relnotes_1.0.gif  style="width:384px;">Bild anklicken, wenn die Animation nicht automatsch startet.   Das Werkzeug [Trim edge](Sketcher_Trimming/de.md) kann jetzt im Modus Halten-und Ziehen verwendet werden. [Pull-Request #13188](https://github.com/FreeCAD/FreeCAD/pull/13188)
   



### Weitere Sketcher-Verbesserungen 

-   Die Option Rahmen wurde dem Rechteckwerkzeug hinzugefügt. [Pull-Request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174)
-   Zwei neue Optionen wurden dem Linienwerkzeug hinzugefügt: *Punkt, Länge, Winkel* und *Punkt, Breite, Höhe*. [Pull-Request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174)
-   Die Symbole [UmschalterKonstruktion](Sketcher_ToggleConstruction/de.md) und [UmschalterFührendeRandbedingung](Sketcher_ToggleDrivingConstraint/de.md) wurden geändert. Ersteres ist jetzt dem Symbol [Pause](Sketcher_CarbonCopy/de.md) weniger ähnlich und beide Schaltflächen wechseln ihre Symbole, wenn sie angeklickt werden. [Pull-Request #11500](https://github.com/FreeCAD/FreeCAD/pull/11500)
-   Sketcher-Symbole wurden überholt, um ihre Darstellung zu vereinheitlichen (Strichbreiten, Farben und Punktgröße). [Pull-Request #11785](https://github.com/FreeCAD/FreeCAD/pull/11785)
-   Ein neues optionales Werkzeug [KoinzidentFestlegenKombiniert](Sketcher_ConstrainCoincidentUnified/de.md) wurde eingeführt. Dieses Werkzeug kombiniert die Werkzeuge [KoinzidentFestlegen](Sketcher_ConstrainCoincident/de.md) und [PunktAufObjektFestlegen](Sketcher_ConstrainPointOnObject/de.md) zum Erstellen von Randbedingungen. [Pull-Request #11494](https://github.com/FreeCAD/FreeCAD/pull/11494)
-   Die Darstellung der Randbedingungen für Bogenwinkel, Linienwinkel und Bogenabstand (arc-angle, line-angle und arc-distance constraints) wurde verbessert. [Pull-Request #12012](https://github.com/FreeCAD/FreeCAD/pull/12012)
-   Kantenarten können jetzt angepasst werden; es kann nicht nur die Farbe geändert werden, sondern auch Linienart und Linienbreite. Dies ermöglicht Strichlinien als Konstruktionslinien. [Pull-Request #11996](https://github.com/FreeCAD/FreeCAD/pull/11996)
-   Das Rechtklick-Menü ist jetzt kontextabhängig und enthält auch B-Spline-Befehle. [Pull-Request #11884](https://github.com/FreeCAD/FreeCAD/pull/11884) und [Pull-Request #11973](https://github.com/FreeCAD/FreeCAD/pull/11973)
-   Ein Doppelklick auf eine Kante wählt jetzt die gesamte damit verbundene Geometrie aus. [Pull-Request #11925](https://github.com/FreeCAD/FreeCAD/pull/11925)
-   Die Sketcher-Symbolleisten wurden etwas umgeordnet, um Übersichtlichkeit und Einheitlichkeit zu verbessern. [Pull-Request #13407](https://github.com/FreeCAD/FreeCAD/pull/13407) und [Pull-Request #13763](https://github.com/FreeCAD/FreeCAD/pull/13763)
-   Die Symbole des Werkzeugs [Pause](Sketcher_CarbonCopy/de.md) wurden für eine bessere Erkennbarkeit überarbeitet. [Pull-Request #15074](https://github.com/FreeCAD/FreeCAD/pull/15074)



## Arbeitsbereich Spreadsheet 



### Weitere Spreadsheet-Verbesserungen 

-   Ein Doppelklick auf ein Tabellenobjekt in der Baumansicht wechselt jetzt zum Arbeitsbereich Spreadsheet. [Pull-Request #13137](https://github.com/FreeCAD/FreeCAD/pull/13137)
-   Die Spreadsheet-Symbole wurden verbessert. [Pull-Request #13996](https://github.com/FreeCAD/FreeCAD/pull/13996)



## Arbeitsbereich TechDraw 

+++
| <img alt="" src=images/TechDraw_cosmetic_circle_relnotes_1.0.png  style="width:250px;"> | Das Werkzeug [Hilfskreis](TechDraw_CosmeticCircle/de.md) wurde hinzugefügt, um das Erstellen von Hilfskreisen durch Auswahl des Mittelpunktes und Festlegen des Radius zu ermöglichen. [Pull-Request #10763](https://github.com/FreeCAD/FreeCAD/pull/10763) |
+++

+++
| <img alt="" src=images/Arc_length_relnotes_1.0.png  style="width:250px;"> | Das Werkzeug [HinweisBogenlänge](TechDraw_ExtensionArcLengthAnnotation/de.md) wurde hinzugefügt, um einen maßähnlichen Hinweis für die Bogenlänge ausgewählter Kanten zu erstellen. [Pull-Request #11532](https://github.com/FreeCAD/FreeCAD/pull/11532) |
+++

+++
| <img alt="" src=images/Offset_vertex_relnotes_1.0.png  style="width:250px;"> | Das Werkzeug [AddOffsetVertex](TechDraw_CommandAddOffsetVertex/de.md) wurde hinzugefügt, um Hilfspunkte relativ zu ausgewählten Knoten zu erstellen. [Pull-Request #11655](https://github.com/FreeCAD/FreeCAD/pull/11655) |
+++

+++
| <img alt="" src=images/Broken_view_relnotes_1.0.png  style="width:250px;"> | Das Werkzeug [UnterbrocheneAnsicht](TechDraw_BrokenView/de.md) wurde hinzugefügt, um einfacher lange Objekte darstellen zu können. [Pull-Request #13331](https://github.com/FreeCAD/FreeCAD/pull/13331) |
+++

   
  <img alt="" src=images/Techdraw_smart_dimension_relnotes_1.0.gif  style="width:320px;">Bild anklicken, wenn die Animation nicht automatsch startet.   Ein neues kontextabhängiges Werkzeug für Maßeinträge, basierend auf [dem im Sketcher eingeführten](Sketcher_Dimension/de.md), wurde hinzugefügt. [Pull-Request #13525](https://github.com/FreeCAD/FreeCAD/pull/13525)
   



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
-   Das Werkzeug [ErgänzungAnzahlpräfixEinfügen](TechDraw_ExtensionInsertRepetition/de.md) zur Angabe der Wiederholungen eines Merkmals wurde hinzugefügt. [Pull-Request #12509](https://github.com/FreeCAD/FreeCAD/pull/12509)
-   Kleine aber wichtige Verbesserungen für die Bedienbarkeit wurden hinzugefügt - Ein Doppelklick auf ein TechDraw-Zeichnungsblatt öffnet jetzt den Arbeitsbereich und das Werkzeug TechDraw Ansicht verschieben wurde durch einfaches Zeihen und Ablegen in der [Baumansicht ersetzt. Auch die Werkzeuge TechDraw Ansicht zur Ansichtsgruppe hinzufügen](Tree_view/de.md) und TechDraw Ansicht aus Ansichtsgruppe entfernen wurden durch Zeihen und Ablegen in der Baumansicht ersetzt.[Pull-Request #13063](https://github.com/FreeCAD/FreeCAD/pull/13063)
-   Die Zeichnungsvorlagen werden jetzt automatisch mit vorhandenen Informationen ausgefüllt (z.B. Datum und Benennung). [Pull-Request #13005](https://github.com/FreeCAD/FreeCAD/pull/13005)
-   Das Werkzeug [Form projizieren](TechDraw_ProjectShape/de.md) wurde aus TechDraw entfernt, da es ein Erbe des Arbeitsbereichs Drawing war und nichts mit einem TechDraw-Zeichnungsblatt zu tun hat. [Pull-Request #13655](https://github.com/FreeCAD/FreeCAD/pull/13655)
-   Das Werkzeug [Ansicht einfügen](TechDraw_View/de.md) wurde verbessert, und verwendet jetzt mehr Objektarten und Einstellungen. Dies ermöglicht folgende Werkzeuge aus der Symbolleiste zu entfernen: [Tabellenansicht](TechDraw_SpreadsheetView/de.md), [ArchAnsicht](TechDraw_ArchView/de.md), [Symbol](TechDraw_Symbol/de.md), [Bild](TechDraw_Image/de.md) und [Ansichtengruppe](TechDraw_ProjectionGroup/de.md). [Pull-Request #13219](https://github.com/FreeCAD/FreeCAD/pull/13219)
-   Einrasten wurde hinzugefügt, um das automatische Ausrichten von Ansichten und Maßen zu ermöglichen. Das Einrasten kann zeitweilig mit der Modifikatortaste Alt unterdrückt werden. [Pull-Request #13659](https://github.com/FreeCAD/FreeCAD/pull/13659)
-   Der Umgang mit Hilfsgeometrie wurde in vielerlei Hinsicht verbessert. [Pull-Request #14216](https://github.com/FreeCAD/FreeCAD/pull/14216)
-   Viele TechDraw-Symbole wurden verbessert. [Pull-Request #14873](https://github.com/FreeCAD/FreeCAD/pull/14873) und folgende



---
⏵ [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 1.0/de
