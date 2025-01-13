# Release notes 1.1/de
**FreeCAD 1.1 ist in Entwicklung, es steht noch kein Veröffentlichungstermin fest.**


{{Message|
Fehlen Funktionen? Das spricht man am besten im Forumsbeitrag [https://forum.freecad.org/viewtopic.php?f&#61;10&t&#61;92080 Release notes for v1.1] an.

Siehe [FreeCAD Unterstützen](Help_FreeCAD/de.md) für Möglichkeiten etwas zu FreeCAD beizutragen.}}


{{Message|Alle Bilder auf dieser Seite müssen das Suffix **_relnotes_1.1** tragen.}}




**FreeCAD 1.1** wurde am **T Monat Jahr** veröffentlicht, es kann von der [Download](Download/de.md)-Seite heruntergeladen werden. Diese Seite listet alle Neuerungen und Änderungen auf.

Ältere FreeCAD-Versionshinweise findet man in den [Versionshinweisen](Feature_list/de#Versionshinweise.md).

Platzhalter für ein auffälliges Bild, das von den Admins im [user showcases forum](https://forum.freecad.org/viewforum.php?f=24) ausgesucht wird.



## Allgemein



## Benutzeroberfläche



### Weitere Verbesserungen der Benutzeroberfläche 

-   Ein Standardkürzel für [Std DlgEinstellungen](Std_DlgPreferences/de.md) wurde hinzugefügt. [Pull-Request #15536](https://github.com/FreeCAD/FreeCAD/pull/15536)
-   Die Seite der Einstellungen für den Benachrichtigungsbereich wurde verbessert. [Pull-Request #15207](https://github.com/FreeCAD/FreeCAD/pull/15207)
-   Die Funktionen Automatisches Sichern und additives Auswählen wurden zum Werkzeug [Messen](Std_Measure/de.md) hinzugefügt. [Pull-Request #17717](https://github.com/FreeCAD/FreeCAD/pull/17717)



## Kernsystem und API 



### Kern

+++
| <img alt="" src=images/Core_datums_relnotes_1.1.png  style="width:384px;"> | Werkzeuge für Hauptbezüge (Core Datums) wurden implementiert, um Koordinatensysteme, Bezugsebenen, Bezugslinien und Bezugspunkte zu erstellen, die in Assembly befestigt und auch verwendet werden können. (oder: \...die befestigt werden (können) und in Assembly verwendet werden können.) [Pull-Request #18332](https://github.com/FreeCAD/FreeCAD/pull/18332) |
+++

   
  <img alt="" src=images/Core_Transform_relnotes_1.1.gif  style="width:384px;">Click on the image if the animation does not start.   Das Werkzeug [Bewegen](Std_TransformManip/de.md) wurde überholt und ermöglicht jetzt präzise Eingaben neben dem Ziehen in der 3D-Ansicht. Es ist möglich den interaktiven Dragger an jedem Element im Dokument auszurichten und das Objekt im lokalen (UVW-) Koordinatensystem des Draggers zu bewegen oder im globalen Koordinatensystem des Dokuments. Der Dragger kann wie zuvor zum Ursprung des Objekts ausgerichtet werden und auch zum Schwerpunkt des Objekts. Es besitzt eine neue Möglichkeit das Objekt (an der Position des Draggers) zu einer Zielposition im Dokument zu bewegen und seine Ausrichtung umzukehren. [Pull-Request #17564](https://github.com/FreeCAD/FreeCAD/pull/17564)
   



### API



#### Entfernte Python API 



#### Geänderte Python-API 



#### Neue Python-API 



## Start



## Addon-Manager 



## Arbeitsbereich Assembly 

-   Das Werkzeug [Ein neues Part einfügen](Assembly_InsertNewPart/de.md) wurde hinzugefügt, und ermöglicht Part-Objekte einfach innerhalb einer Baugrube hinzuzufügen.[Pull-Request #17922](https://github.com/FreeCAD/FreeCAD/pull/17922)
-   Das Werkzeug [Simulation erstellen](Assembly_CreateSimulation/de.md) wurde hinzugefügt und ermöglicht Bewegungen zu Verbindungen hinzuzufügen und Animationen zu erstellen. [Pull-Request #16414](https://github.com/FreeCAD/FreeCAD/pull/16414)



### Weitere Assembly-Verbesserungen 

-   Die neuen Hauptbezüge können zum Befestigen von Verbindungen verwendet werden, um mehrere Bauteile zusammenzubauen. [Pull-Request #18332](https://github.com/FreeCAD/FreeCAD/pull/18332)



## Arbeitsbereich BIM 



### Weitere BIM-Verbesserungen 

-   Das Fenster [BIM Asichten](BIM_Views/de.md) wurde überholt und hat jetzt einen Abschnitt für alle 2D-Ansichten. [Pull-Request #15836](https://github.com/FreeCAD/FreeCAD/pull/15836)
-   NativeIFC-Unterstützung für 2D-Objekte wurde zu BIM hinzugefügt und ermöglicht 2D-Objekte (Linien, Texte, Maße) in IFC-Dateien einzubetten und auch solche Dateien anderer BIM-Anwendungen zu öffnen.[Pull-Request #16629](https://github.com/FreeCAD/FreeCAD/pull/16629)



## Arbeitsbereich CAM 



### Weitere CAM-Verbesserungen 

-   G84/G74 Operationen zum Gewindeschneiden wurden hinzugefügt. [Pull-Request #8069](https://github.com/FreeCAD/FreeCAD/pull/8069)
-   Multi-Pass-Unterstützung wurde für Profil-Operationen hinzugefügt. [Pull-Request #17326](https://github.com/FreeCAD/FreeCAD/pull/17326)



## Arbeitsbereich Draft 



### Weitere Draft-Verbesserungen 

-   Unterstützung für relative Schriftpfade wurde den [Textformen](Draft_ShapeString/de.md) hinzugefügt. [Pull-Request #17819](https://github.com/FreeCAD/FreeCAD/pull/17819)
-   Der Befehl [Draft Verrundung](Draft_Fillet/de.md) bearbeitet jetzt ausgewählte Kanten, anstatt der ersten Kante von ausgewählten Objekten. [Pull-Request #17945](https://github.com/FreeCAD/FreeCAD/pull/17945) und [Pull-Request #18150](https://github.com/FreeCAD/FreeCAD/pull/18150)
-   Das Ebenen-Menü des Befehls [Draft AutoGruppieren](Draft_AutoGroup/de.md) wird jetzt alphabetisch geordnet. [Pull-Request #18172](https://github.com/FreeCAD/FreeCAD/pull/18172)
-   Der Umgang mit Verknüpfungen in [TechDraw Draft-Ansichten](TechDraw_DraftView/de.md) wurde berichtigt. [Pull-Request #18175](https://github.com/FreeCAD/FreeCAD/pull/18175)
-   Die Position des Feldes *Skalierungsfaktor* in der Benutzerschnittstelle wurde verbessert ([Draft StilFestlegen](Draft_SetStyle/de.md), [Draft Beschriftungsstileditor](Draft_AnnotationStyleEditor/de.md) und [Draft Einstellungen](Draft_Preferences/de.md)). [Pull-Request #18299](https://github.com/FreeCAD/FreeCAD/pull/18299)



## Arbeitsbereich FEM 



### Weitere FEM-Verbesserungen 

-   Log verbosity kann jetzt in den [Einstellungen](FEM_Preferences/de#Gmsh.md) für Gmsh eingestellt werden. [Pull-Request #17699](https://github.com/FreeCAD/FreeCAD/pull/17699)
-   Die {{PropertyData/de|Second Order Linear}} und die Unterstützung für [lokales Aufbereiten](FEM_MeshRegion/de.md), die vorher nur für Gmsh zur Verfügung standen, stehen jetzt auch der neuen Implementation von [Netgen](FEM_MeshNetgenFromShape/de.md) zur Verfügung. [Pull-Request #17170](https://github.com/FreeCAD/FreeCAD/pull/17170)
-   Box und elliptische Balkenquerschnitte wurden zur [FEM Elementgeometrie1D](FEM_ElementGeometry1D/de.md) hinzugefügt. [Pull-Request #15843](https://github.com/FreeCAD/FreeCAD/pull/15843)
-   Das Werkzeig [Ergebnisse bereinigen](FEM_ResultsPurge/de.md) löscht jetzt alle Ergebnisobjekte, nicht nur die zu CalculiX gehörigen. [Pull-Request #18328](https://github.com/FreeCAD/FreeCAD/pull/18328)
-   Die [RandbedingungVerbinder](FEM_ConstraintTie/de.md) kann jetzt auch auf Schalenflächen angewendet werden. [Pull-Request #18325](https://github.com/FreeCAD/FreeCAD/pull/18325)
-   Das Ausgabeformat (binär oder ASCII) und das Speichern von Geometrie-IDs kann jetzt für Elmer eingestellt werden, auch in den [Voreinstellungen](FEM_Preferences/de#Elmer.md). [Pull-Request #17972](https://github.com/FreeCAD/FreeCAD/pull/17972)
-   Eine Option zum Glätten wurde dem [Contours filter](FEM_PostFilterContours/de.md) hinzugefügt. [Pull-Request #18088](https://github.com/FreeCAD/FreeCAD/pull/18088)
-   Der Parameter *BucklingAccuracy* wurde zum Gleichungslöser [CalculiX](FEM_SolverCalculixCxxtools.md) hinzugefügt - es kann erforderlich sein, den ersten \"eigenvalue-?\" in einigen linearen Knickanalysen zu bestimmen (Das kann ein Fachmann sicher besser ausdrücken). [Pull-Request #18790](https://github.com/FreeCAD/FreeCAD/pull/18790)
-   Jetzt können alle FEM-Objekte unterdrückt werden, für die Unterdrücken sinnvoll ist. Vorher konnten nur Randbedingungen unterdrückt werden.[Pull-Request #18636](https://github.com/FreeCAD/FreeCAD/pull/18636)



## Arbeitsbereich Material 



### Weitere Material-Verbesserungen 



## Arbeitsbereich Mesh 



### Weitere Mesh-Verbesserungen 



## Arbeitsbereich OpenSCAD 



### Weitere OpenSCAD-Verbesserungen 



## Arbeitsbereich Part 



### Weitere Part-Verbesserungen 

-   Das Werkzeug [Geometrie überprüfen](Part_CheckGeometry/de.md) enthält jetzt auch Ergebniseinträge für gültige Formen, zeigt ausgelassene Objekte und erstellt Berichte im [Ausgabefenster](Report_view/de.md).



## Arbeitsbereich PartDesign 



### Weitere PartDesign-Verbesserungen 

-   Das Element Ursprung (origin feature) in einem PartDesign-Körper verwendet die neuen Hauptbezüge (core datums). Das Aussehen wurde geändert und die Ebenen werden vergrößert, wenn eine neue Skizze erstellt wird. Da die Ausrichtung in älteren FreeCAD-Versionen falsch war, müssen Dateien, die mit diesen Versionen erstellt wurden, beim Öffnen umgewandelt werden. Es kann Dateien zerstören, die auf diese Bezüge referenzieren und Dateien, die umgewandelt wurden oder in der {{VersionPlus/de|1.1}} erstellt wurden, werden in {{VersionMinus/de|1.0}} zerstört.[Pull-Request #18126](https://github.com/FreeCAD/FreeCAD/pull/18126)
-   Der Befehl [Enfrieren umschalten](Std_ToggleFreeze/de.md) steht jetzt in PartDesign zur Verfügung. [Pull-Request #18373](https://github.com/FreeCAD/FreeCAD/pull/18373)
-   Das Werkzeug [Bohrung](PartDesign_Hole/de.md) kann jetzt verschiedene [Whitworth-Gewinde](https://de.wikipedia.org/wiki/Whitworth-Gewinde) nach BSW-, BSF-, BSP- und NPT-Norm erstellen. [Pull-Request #15744](https://github.com/FreeCAD/FreeCAD/pull/15744)
-   Die Leistung der modellierten Gewinde des Werkzeugs [Bohrung](PartDesign_Hole/de.md) wurde verbessert. [Pull-Request #15744](https://github.com/FreeCAD/FreeCAD/pull/15744)
-   Der Startwinkel konischer Gewinde des Werkzeugs [Bohrung](PartDesign_Hole/de.md) wird jetzt automatisch auf den Wert aus den Normen ISO 7-1 und ASME B1.20.1 gesetzt. [Pull-Request #15744](https://github.com/FreeCAD/FreeCAD/pull/15744)



## Arbeitsbereich Points 



### Weitere Points-Verbesserungen 



## Arbeitsbereich Sketcher 

   
  <img alt="" src=images/Sketcher_defining_external_relnotes_1.1.gif  style="width:384px;">Bild anklicken, wenn die Animation nicht automatisch startet.   Das Werkzeug [Projektion](Sketcher_Projection/de.md) wurde hinzugefügt und ermöglicht, projizierte [externe Geometrie](Sketcher_External/de.md) zu erstellen; dabei kann die Art der erstellten externen Geometrie zwischen beschreibender Geometrie und Hilfsgeometrie umgeschaltet werden. [Pull-Request #17736](https://github.com/FreeCAD/FreeCAD/pull/17736)
   

+++
| <img alt="" src=images/Sketcher_intersection_relnotes_1.1.png  style="width:384px;"> | [Schneiden](Sketcher_Intersection/de.md) wurde hinzugefügt und ermöglicht, [externe Geometrie](Sketcher_External.md) zu erstellen, wobei ausgewählte Geometrie mit der Skizzenebene geschnitten wird. [Pull-Request #17736](https://github.com/FreeCAD/FreeCAD/pull/17736) |
+++

   
  <img alt="" src=images/Sketcher_external_faces_relnotes_1.1.gif  style="width:384px;">Bild anklicken, wenn die Animation nicht automatisch startet.   [Externe Geometrie](Sketcher_External/de.md) (sowohl projiziert als auch geschnitten) kann jetzt durch Auswählen einer Fläche erstellt werden. [Pull request #17736](https://github.com/FreeCAD/FreeCAD/pull/17736)
   



### Weitere Sketcher-Verbesserungen 

-   Es ist jetzt möglich, externe Geometrie direkt als Eingabe für Werkzeuge wie Bewegen / linear anordnen zu verwenden, sowohl externe Hilfsgeometrie als auch externe beschreibende Geometrie. [Pull-Request #17615](https://github.com/FreeCAD/FreeCAD/pull/17615)
-   Externe Geometrie (projiziert oder als Schnittlinie) ist jetzt standardmäßig richtige (beschreibende) Geometrie (die nicht nachgezeichnet werden muss, wie in Version 1.0 und davor). Sie kann zu Hilfsgeometrie umgeschaltet werden, wie jede andere Geometrie auch.[Pull-Request #17736](https://github.com/FreeCAD/FreeCAD/pull/17736)
-   Die Sketcher-Achsen werden jetzt unendlich lang angezeigt. [Pull-Request #17312](https://github.com/FreeCAD/FreeCAD/pull/17312)
-   Skizzen werden jetzt in alphabetischer Reihenfolge im Dialog [Skizze auswählen](Sketcher_MapSketch/de.md) aufgelistet. [Pull-Request #16518](https://github.com/FreeCAD/FreeCAD/pull/16518)
-   Das Ziehen von Gruppen wurde hinzugefügt und ermöglicht alle ausgewählten Geometrieelemente zu ziehen. [Pull-Request #18273](https://github.com/FreeCAD/FreeCAD/pull/18273)
-   Es gibt eine neue Voreinstellung, die, wenn sie aktiviert ist, externe Geometrie immer als Hilfsgeometrie erstellt, unabhängig vom eingestellten Modus. [Pull-Request #18697](https://github.com/FreeCAD/FreeCAD/pull/18697)



## Arbeitsbereich Spreadsheet 



### Weitere Spreadsheet-Verbesserungen 

-   Standardkürzel für [Text in Fettschrift](Spreadsheet_StyleBold/de.md), [Text in Kursivschrift](Spreadsheet_StyleItalic/de.md) und [Text unterstreichen](Spreadsheet_StyleUnderline/de.md) wurden hinzugefügt. [Pull-Request #15556](https://github.com/FreeCAD/FreeCAD/pull/15556)
-   Ein Doppelklick auf den Trenner in der Überschriftenzeile, passt jetzt die Spaltenbreite an den Inhalt an. [Pull-Request #16296](https://github.com/FreeCAD/FreeCAD/pull/16296)
-   Zoom wurde zu Spreadsheet hinzugefügt. [Pull-Request #16130](https://github.com/FreeCAD/FreeCAD/pull/16130)



## Arbeitsbereich Surface 



### Weitere Surface-Verbesserungen 



## Arbeitsbereich TechDraw 



### Weitere TechDraw-Verbesserungen 

-   Das Werkzeug [Flächeninhalt einfügen](TechDraw_AreaDimension/de.md) erkennt jetzt sicher die Löcher in Flächen. [Pull-Request #17740](https://github.com/FreeCAD/FreeCAD/pull/17740)
-   Form prüfen (Shape validation) steht jetzt zur Verfügung und kann in den [Voreinstellungen](TechDraw_Preferences/de#Erweitert.md) aktiviert werden. [Pull-Request #18282](https://github.com/FreeCAD/FreeCAD/pull/18282)



## Kompilieren



## Bekannte Einschränkungen 



## Andere Quellen



---
⏵ [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 1.1/de
