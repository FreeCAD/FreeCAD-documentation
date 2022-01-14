# Thread for Screw Tutorial/de
{{TutorialInfo/de
|Topic= Produktgestaltung
|Level= Fortgeschrittene
|Time= 60 Minuten
|Author=[DeepSOIC](User_DeepSOIC.md), [Murdic](User_Murdic.md), vocx
|FCVersion=0.19
|Files=[https://forum.freecadweb.org/viewtopic.php?f=36&t=44668 Aktualisiert: Gewinde für Schrauben Tutorium]
}}

## Einführung

Dieses Tutorium ist eine Sammlung von Techniken zum Modellieren von Schraubengewinden in FreeCAD. Es wurde für v0.19 aktualisiert, obwohl der Gesamtprozess seit v0.14, als das Tutorial ursprünglich geschrieben wurde, im Wesentlichen gleich geblieben ist. Der aktualisierte Inhalt konzentriert sich auf die Verwendung der <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md), um das Gewinde zu erstellen, sowie neue Illustrationen für die Methoden 0 bis 3.

In herkömmlichen CAD Systemen wird von der Modellierung von Schraubengewinden abgeraten, da dies eine große Belastung für den Modellierungskern sowie für die Darstellung der Formen darstellt. In herkömmlichen Systemen muss ein Gewinde nicht direkt im 3D Raum dargestellt werden, da es in der technischen 2D Zeichnung, die zur Fertigung geschickt wird, mit seinen erforderlichen Eigenschaften angegeben werden kann. Mit der Popularisierung der additiven Fertigung (3D Druck) besteht nun jedoch ein echter Bedarf, 3D Gewinde zu modellieren, um sie genau so drucken zu können, wie sie entworfen wurden. Dafür ist dieses Tutorium gedacht.

Viele der hier vorgestellten Techniken wurden aus verschiedenen Forumsbeiträgen zusammengetragen:

-   [Zusammenstellung von Gewindemodellierungstechniken](https://forum.freecadweb.org/viewtopic.php?f=3&t=12593)
-   [Erstellen eines Gewindes: Unerwartete Ergebnisse](https://forum.freecadweb.org/viewtopic.php?f=3&t=6506)

Siehe auch hilfreiche Videos:

-   [Einführung einer Strategie zur Konstruktion einer Schraube ohne die häufig auftretenden Probleme](https://forum.freecadweb.org/viewtopic.php?f=8&t=44259).

Denke daran, dass Gewindeformen viel Speicherplatz beanspruchen und dass ein einziges Gewinde in einem Dokument die Dateigröße erheblich erhöhen kann, weshalb dem Benutzer empfohlen wird, Gewinde nur dann zu erstellen, wenn dies absolut notwendig ist.

## Methode 0. Eins aus der Teilebibliothek beziehen 

Die Verwendung von Modellen, die andere Leute geschaffen haben, ist einfach und zeitsparend. Sieh dir [externe Arbeitsbereiche](external_workbenches/de.md) Seite an zu Informationen über externe Werkzeuge.

Insbesondere werden zwei Ressourcen empfohlen, die über den [Erweiterungsverwalter](Std_AddonMgr/de.md) installiert werden können:

-   [Verbindungselemente Arbeitsbereich](https://github.com/shaise/FreeCAD_FastenersWB), um parametrische Schrauben und Unterlegscheiben zu platzieren, die den ISO Normen entsprechen. Die Schrauben und Muttern zeigen standardmäßig kein Gewinde, aber dies kann mit einer Option gesteuert werden.
-   [BOLTSFC](https://github.com/berndhahnebach/BOLTSFC), um Normteile aus der BOLTS Bibliothek zu platzieren, die ebenfalls ISO Normen entsprechen.

<img alt="" src=images/T13_00_Threads_fasteners.png  style="width:" height="300px;"> 
*Verschiedene ISO Normschrauben, die mit dem Arbeitsbereich Verbindungselemente eingesetzt werden. Eine Option steuert, ob ein Objekt das echte Gewinde oder nur einen einfachen Zylinder zeigt.*

## Methode 1: Verwendung von Makros (veraltet) 

-   In der Vergangenheit wurden die Teile aus der BOLTS Bibliothek mit [Makro BOLTS](Macro_BOLTS/de.md) eingefügt. Dies ist nun veraltet. Verwende stattdessen den BOLTSFC Arbeitsbereich.

-   In der Vergangenheit wurde das autonome [Schraubenmacher Makro](Macro_screw_maker1_2/de.md) von ulrich1a verwendet, um einzelne Bolzen, Schrauben und Unterlegscheiben zu erstellen. Dies ist nun veraltet. Der Arbeitsbereich für Verbindungselemente von shaise enthält das Schraubenherstellungsmakro vollständig, zusammen mit einer Werkzeugleiste zur Auswahl der richtigen Komponente.

## Methode 2. Verbindungselemente-Arbeitsbereich 

Benutze den externen [Arbeitsbereich Verbindungselemente](Fasteners_Workbench/de.md), um verschiedene Verbindungselemente zu Teilen hinzuzufügen/an Teilen anzubringen. Dieser Arbeitsbereich kann mit dem [Erweiterungsverwalter](Std_AddonMgr/de.md) installiert werden.

## Methode 3. Scheingewinde: nicht spiralförmig 

In vielen Fällen brauchen wir keine echten Gewinde, wir brauchen nur ein visuelles Anzeichen dafür, dass die Gewinde vorhanden sein werden.

Wir können ein Scheingewinde erzeugen, indem wir eine nicht spiralförmige Bahn verwenden, zum Beispiel durch Drehen eines Sägezahnprofils oder durch Stapeln von Scheiben mit konischen Kanten. Dieses Scheingewinde ist durch einfache Kontrolle kaum von dem echten schraubenförmigen Gewinde zu unterscheiden. Diese Methode ist gut geeignet, um ein gewindeähnliches Objekt zu visualisieren, aber sie ist nicht nützlich, wenn wir ein echtes Gewinde in 3D drucken müssen.

<img alt="" src=images/T13_01_Threads_comparison_fake_real.png  style="width:" height="300px;"> 
*Links: einfacher Bolzen mit einem unechten, nicht spiralförmigen Gewinde. Rechts: einfacher Bolzen mit einem echten spiralförmigen Gewinde. Wenn der 3D Druck nicht erforderlich ist, ist ein simuliertes Gewinde oft ausreichend für die Visualisierung.*

### Umlaufendes Sägezahnprofil 

1.  Klicke auf **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Körper](PartDesign_Body/de.md)**.
2.  Klicke auf **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [PartDesign Neue Skizze](PartDesign_NewSketch/de.md)**. Wähle {{Value|XZ_Ebene}}.
3.  Zeichne eine geschlossene Skizze mit dem erforderlichen Innendurchmesser {{Value|10 mm}}, Außendurchmesser um {{Value|12.6 mm}}, Steigung {{Value|3 mm}}, Zähnezahl {{Value|8}}, und Gesamthöhe {{Value|30 mm}}.
4.  Wähle die Skizze aus und klicke dann auf **[<img src=images/PartDesign_Revolution.svg style="width:16px"> [PartDesign Umdrehung](PartDesign_Revolution/de.md)**. Wähle {{Value|Vertikale Skizzenachse}}, und drücke **OK**.

<img alt="" src=images/T13_02_Threads_Sawtooth_sketch_profile.png  style="width:" height="300px;"> 
*Profil, das zur Erstellung der Umdrehung verwendet wird, die ein Gewinde simuliert.*

<img alt="" src=images/T13_03_Threads_Sawtooth_revolution_1.png  style="width:" height="300px;"> <img alt="" src=images/T13_04_Threads_Sawtooth_revolution_2.png  style="width:" height="300px;"> 
*Schnittdarstellung des resultierenden nicht spiralförmigen Gewindes, das durch Drehen des Sägezahnprofils um die vertikale Achse erzeugt wird.*

### Stapeln von Scheiben 

1.  Wiederhole die ersten beiden Schritte aus dem vorherigen Abschnitt.
2.  Zeichne eine geschlossene Skizze mit dem erforderlichen Innendurchmesser {{Value|10 mm}}, dem Außendurchmesser um {{Value|12.6 mm}} und der Steigung {{Value|3 mm}}, aber zeichne nur einen einzelnen Zahn des Sägezahns.
3.  Wähle die Skizze aus und klicke dann auf **[<img src=images/PartDesign_Revolution.svg style="width:16px"> [PartDesign Umdrehung](PartDesign_Revolution/de.md)**. Wähle {{Value|Vertikale Skizzenachse}}, und drücke **OK**.




1.  Wähle die {{Value|Umdrehung}}, klicke dann auf **[<img src=images/PartDesign_LinearPattern.svg style="width:16px"> [PartDesign Lineares Muster](PartDesign_LinearPattern/de.md)**. Wähle {{Value|Vertikale Skizzenachse}}. Für ein Scheingewinde mit einer Steigung von {{Value|3 mm}}, setze die **Länge** auf {{Value|3}}, und **Häufigkeiten** auf {{Value|2}}, dann drücke **OK**. Dadurch werden zwei Scheiben erstellt, eine über der anderen.
2.  Du kannst weitere Scheiben hinzufügen, indem du den Wert der **Häufigkeiten** im linearen Muster, und durch Erhöhen der **Länge**, die die Gesamtlänge des Scheingewindes darstellt.

Die {{MenuCommand/de|Länge}} und {{MenuCommand/de|Häufigkeiten}} sind miteinander verwandt. Wenn die Länge zu groß ist, aber die Anzahl der Häufigkeiten nicht hoch genug ist, hast du getrennte Scheiben, und die Berechnung des Körpers wird fehlschlagen, da das resultierende Objekt immer ein [einzelne aneinandergrenzende Festkörper](PartDesign_Body/de.md) sein muss. Um beispielsweise eine Gesamthöhe von {{Value|30 mm}} zu erhalten, setze {{MenuCommand/de|Länge}} auf {{Value|27 mm}} und **/de|Häufigkeiten** auf {{Value|10}}.

Wenn du möchtest, kannst du einen **[<img src=images/PartDesign_AdditiveCylinder.svg style="width:16px"> [/de|PartDesign AdditiverZylinder](PartDesign_AdditiveCylinder.md)** mit einem Durchmesser, der dem Innendurchmesser der Scheiben entspricht und so hoch ist wie die gesamte Gewindehöhe. Dadurch werden alle Scheiben zu einem einzigen Festkörper verbunden, wodurch gewährleistet wird, dass es keine getrennten Scheiben gibt.

<img alt="" src=images/T13_05_Threads_Stacked_discs_sketch.png  style="width:" height="300px;"> 
*Profil, das zur Erstellung der Umdrehung verwendet wird, die ein Gewinde simuliert.*

<img alt="" src=images/T13_06_Threads_Stacked_discs_1.png  style="width:" height="300px;"> <img alt="" src=images/T13_07_Threads_Stacked_discs_2.png  style="width:" height="282px;"> 
*Links: einzelne Scheibe, die durch Umdrehung entstanden ist. Rechts: mehrere Scheiben, die in einem linearen Muster in Z Richtung angeordnet sind und ein spiralförmiges Gewinde simulieren.*

## Methode 4. Austragen eines vertikalen Profils 

### Part Design 

Ein echtes Gewinde besteht aus einem geschlossenen Profil, das einen Festkörper entlang einer spiralförmigen Bahn austrägt.

1.  Im <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Arbeitsbereich](Part_Workbench.md), klicke auf **[<img src=images/Part_Primitives.svg style="width:16px"> [Part Grundkörper](Part_Primitives/de.md)** zum Erstellen einer **[<img src=images/Part_Helix.svg style="width:16px"> [Part Spirale](Part_Helix/de.md)**. Gib ihm die entsprechenden Werte für {{MenuCommand/de|Steigung}} {{Value|3 mm}}, **Höhe** {{Value|23 mm}}, und **Radius** {{Value|10 mm}}.
2.  Gehe zum <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md), und klicke auf **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Körper](PartDesign_Body/de.md)**.
3.  Klicke auf **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [PartDesign Neue Skizze](PartDesign_NewSketch/de.md)**. Wähle {{Value|XZ_Ebene}}.
4.  Zeichne eine geschlossene Skizze mit dem erforderlichen Profil für die Gewindezähne, normalerweise eine dreieckige Form. In diesem Fall werden wir eine Höhe von {{Value|2,9 mm}} verwenden, die etwas kleiner ist als die für den Spiralpfad verwendete Steigung {{Value|3,0 mm}}. Das Profil darf keine Selbstüberschneidungen erzeugen, wenn es entlang der Spirale bewegt wird, weder zwischen den Windungen noch in der Mitte, daher kann die Skizze, wie sie für Stapelscheiben gezeigt wird, nicht verwendet werden.
5.  Wähle die Skizze aus und klicke dann auf **[<img src=images/PartDesign_AdditivePipe.svg style="width:16px"> [PartDesign Additives Rohr](PartDesign_AdditivePipe.md)**. Im {{MenuCommand/de|Pad für die Austragung}} klicke auf {{MenuCommand/de|Objekt}}, und wähle das zuvor erstellte Spiralobjekt aus. Ändere dann {{MenuCommand/de|Richtungsmodus}} in {{Value|Frenet}}, so dass das Profil den Pfad ohne Verdrehung überstreicht; drücke dann **OK**.
6.  Wenn der Dialog nach einem Verweis fragt, wähle {{Value|Querverweis erstellen}}.
7.  Der schraubenförmige Wendel wird erstellt, aber es gibt keinen zentralen Körper oder Welle.
8.  Klicke auf **[<img src=images/PartDesign_AdditiveCylinder.svg style="width:16px"> [PartDesign Additiver Zylinder](PartDesign_AdditiveCylinder.md)** mit dem entsprechenden {{MenuCommand/de|Radius}} {{Value|10 mm}} und {{MenuCommand/de|Höhe}} {{Value|29.9 mm}}, um den Rest des spiralförmigen Gewindes zu berühren und automatisch mit ihm zu verschmelzen.
9.  Zusätzliche boolesche Operationen sind erforderlich, um die abrupten Enden der Wendels zu formen. Sie können z.B. additive Merkmale verwenden, um der Schraube einen Kopf und eine Spitze zu geben.

<img alt="" src=images/T13_08_Threads_Helical_thread_profile.png  style="width:" height="300px;"> <img alt="" src=images/T13_09_Threads_Helical_thread_path.png  style="width:" height="300px;"> 
*Links: Profil für ein spiralförmiges Gewinde. Rechts: Spiralenpfad, die zur Erzeugung einer Austragung verwendet wird.*

<img alt="" src=images/T13_10_Threads_Helical_thread_coil.png  style="width:" height="300px;"> <img alt="" src=images/T13_11_Threads_Helical_thread_coil_sliced.png  style="width:" height="300px;"> 
*Links: spiralförmiger Wendel, die sich aus dem Austragungsvorgang des geschlossenen Profils entlang der spiralförmigen Bahn ergibt. Rechts: Schnitt durch das Wendel, der sich aus der Austragung ergibt.*

<img alt="" src=images/T13_12_Threads_Helical_thread_cylinder.png  style="width:" height="300px;"> <img alt="" src=images/T13_13_Threads_Helical_thread_finished.png  style="width:" height="300px;"> 
*Links: spiralförmiger Wendel, der mit einem zentralen Zylinder verschmolzen ist, um den Körper der Schraube zu bilden. Rechts: weitere Merkmale, ein Kopf und eine Spitze, hinzugefügt, um die Form der Schraube zu verbessern.*

### Part

Dieser Arbeitsgang kann auch mit den Werkzeugen dem [Part Arbeitsbereich](Part_Workbench/de.md) durchgeführt werden.

1.  Im <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Arbeitsbereich](Part_Workbench.md), klicke auf **[<img src=images/Part_Primitives.svg style="width:16px"> [Part Grundkörper](Part_Primitives/de.md)** zum Erstellen einer **[<img src=images/Part_Helix.svg style="width:16px"> [Part Spirale](Part_Helix/de.md)**. Gib ihm die entsprechenden Werte für {{MenuCommand/de|Steigung}}. {{Value|3 mm}}, **Höhe** {{Value|23 mm}}, und **Radius** {{Value|10 mm}}.
2.  In diesem Fall benötigst du keinen **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Körper](PartDesign_Body/de.md)**. Wechsle zum <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Skizzierer Arbeitsbereich](Sketcher_Workbench/de.md), und klicke dann **[<img src=images/Sketcher_NewSketch.svg style="width:16px"> [Skizzierer Neue Skizze](Sketcher_NewSketch/de.md)**, und wähle die globale XZ Ebene.
3.  Kehre dann zurück zum <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Arbeitsbereich](Part_Workbench/de.md), und verwende **[<img src=images/Part_Sweep.svg style="width:16px"> [PartAustragung](Part_Sweep/de.md)**.
4.  Wähle die entsprechende Skizze aus {{MenuCommand/de|Verfügbares Profil}} und klicke auf den Pfeil, um sie an {{MenuCommand/de|Gewählte Profile}} zu übergeben.
5.  Klicke auf **Austragungspfad**, und wähle alle Kanten der vorhandenen Spirale in der [3D Ansicht](3D_view/de.md). Klicke auf **Fertig**.
6.  Stelle sicher, dass die {{CheckBox|TRUE|Festkörper erzeugen}} und {{CheckBox|TRUE|Frenet}} angehakt sind. Das Erhalten eines Volumenkörpers ist der Schlüssel, um [Part Boolsche](Part_Boolean/de.md) Operationen mit dem resultierenden Wendel durchführen zu können, andernfalls wird nur eine Fläche erzeugt.
7.  Klicke auf **OK**, um das Dialogfeld zu verlassen und den Wendel zu erzeugen.

Nun kannst du fortfahren, andere Grundelemente wie **[<img src=images/Part_Cylinder.svg style="width:16px"> [Part Zylinder](Part_Cylinder/de.md)**, oder andere Formen, um **[<img src=images/Part_Fuse.svg style="width:16px"> [Part Verschmelzen](Part_Fuse/de.md)** auszuführen, und **[<img src=images/Part_Cut.svg style="width:16px"> [Part Schnitte](Part_Cut/de.md)** hinzuzufügen, um den Bau der Schraube abzuschließen.

<img alt="" src=images/T13_14_Threads_components.png  style="width:" height="300px;"> 
*Erstellen eines Gewindewendels durch Austragen eines vertikalen Profils, (1) das [Skizzenprofil](Sketch/de.md), (2) der [spiralförmige](Part_Helix/de.md) Austragungspfad und (3) das Ergebnis der [Austragung](Part_Sweep/de.md).*

### Tips für den Erfolg 

-    **Regel 1.**Wenn das Profil die Spirale austrägt, darf sich die resultierende feste Wendel nicht berühren oder sich selbst schneiden, da es sich dann um einen ungültigen Festkörper handelt. Dies gilt sowohl für das Profil, das sich entlang des Spirale bewegt, als auch für Schnittpunkte in der Mitte der Spirale. Versuche, damit boolsche Operationen durchzuführen (Verschmelzen oder Schneiden), werden sehr wahrscheinlich fehlschlagen. Prüfe die Qualität des Wendels mit **[<img src=images/Part_CheckGeometry.svg style="width:16px"> [Part PrüfeGeometrie](Part_CheckGeometry.md)**; wenn Selbstüberschneidungen gemeldet werden, musst du die Steigung der Spirale erhöhen.

<img alt="" src=images/T13_15_Threads_self_intersection.png  style="width:" height="300px;"> <img alt="" src=images/T13_16_Threads_no_self_intersections_OK.png  style="width:" height="300px;"> 
*Links: ungültige Austragung, der durch die Verwendung einer sehr kleinen Steigung der Spirale im Vergleich zur Höhe des Dreiecksprofils erzeugt wurde. Rechts: Steigung, die ausreichend groß ist und keine Selbstüberschneidungen verursacht.*

-    **Regel 2.**Wenn ein Zylinder zu einem Wendel hinzugefügt wird, um den Hauptschaft einer Schraube zu bilden, darf der Zylinder das Wendelprofil nicht tangieren. Das heißt, der Zylinder darf nicht den gleichen Radius wie der Innenradius des Gewindes haben, da dies sehr wahrscheinlich zum Versagen eines Verschmelzungsvorgangs führt.

Im Allgemeinen vermeide Geometrie deckungsgleich mit Elementen der Austragung, wie z.B. tangentiale Flächen oder Kanten, die Flächen berühren, mit denen sie nicht verbunden sind. Um eine guten boolesche Vereinigung herzustellen, muss sich der ausgetragene Wendel und der Zylinder kreuzen. Prüfe die Qualität der Verschmelzung mit **[<img src=images/Part_CheckGeometry.svg style="width:16px"> [Part PrüfeGeometrie](Part_CheckGeometry.md)**; Wenn koplanare Flächen gemeldet werden, erhöhe den Radius des Zylinders um einen kleinen Betrag.

-   Wenn der Wendel und der Zylinder tangential verlaufen, kann es bei nachfolgenden boolschen Operationen mit einem dritten Festkörper fehlschlagen, selbst wenn die erste Verschmelzung erfolgreich ist.
-   Dies ist eine Begrenzung des OpenCASCADE Technology (OCCT)-Kerns; im Allgemeinen kommt er mit Operationen zwischen koplanaren Flächen nicht gut zurecht.

<img alt="" src=images/T13_17_Threads_tangent_faces.png  style="width:" height="300px;"> <img alt="" src=images/T13_18_Threads_no_tangent_faces_OK.png  style="width:" height="300px;"> 
*Links: der Massivzylinder verläuft tangential zum Innenradius des Gewindes ; dies kann zu einer ungültigen boolschen Vereinigung führen. Rechts: der Zylinder hat einen etwas größeren Radius, so dass sich die beiden Festkörper schneiden; dies führt zu einer gültigen Verschmelzung.*

-    **Regel 3.**Der innere Zylinder hat eine Nahtlinie. Du solltest vermeiden, den Anfang der Wendel entlang dieser Naht zu platzieren. Drehe entweder die Spirale oder den Zylinder um einige Grad.

-    **Tip 1.**Der Radius des Spiralpfades spielt keine Rolle, es sei denn, die Spirale ist verjüngt. Alles, was zählt, ist die Steigung und die Höhe der Spirale. Das bedeutet, dass du eine einzige **[<img src=images/Part_Helix.svg style="width:16px"> [Part Spirale](Part_Helix/de.md)**, verwenden kannst um mehrere Gewinde mit gleicher Steigung zu erzeugen. Was die Position der resultierenden Wendel bestimmt, ist die Position des Profils [Skizze](Sketch/de.md).

-    **Tip 2.**Halte das Gewinde kurz, d.h. mit einer geringen Anzahl von Windungen. Lange Gewinde neigen dazu, bei boolschen Operationen zu versagen. Wenn du viele Windungen hinzufügen musst, ziehe in Betracht, zuerst ein kurzes Gewinde zu erstellen und dann **[<img src=images/Draft_OrthoArray.svg style="width:16px"> [Entwurf AnordnungRechtwinklig](Draft_OrthoArray/de.md)**, um das gleiche Muster mehrmals zu duplizieren.

-    **Tip 3.**Für die 3D Visualisierung und den 3D Druck kann es in Ordnung sein, den Zylinder und das Gewinde unverschmolzen zu lassen, d.h. mit Schnittpunkten zwischen den beiden Volumenkörpern. Die Reduzierung der Anzahl der booleschen Operationen führt zu weniger Speicherverbrauch und kleineren Dateien.

### Vor- und Nachteile 

-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> Leicht verständlich.
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> Sehr natürliche Art der Festlegung eines Gewindeprofils.
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> Keine Probleme mit der Netzbildung des resultierenden Objekts, im Gegensatz zu Methode 4.

-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> Aufgrund der Ungültigkeit sich selbst überschneidender Austragungen ist es nahezu unmöglich, ein Gewinde ohne Lücke zwischen den einzelnen Zähnen zu erzeugen, d.h. ohne gerade zylindrische Fläche an den Innenseiten des Gewindes.
-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> Boolesche Operationen sind erforderlich, um einen einzigen zusammenhängenden Festkörper zu erhalten. Die Berechnung boolescher Operationen nimmt relativ viel Zeit in Anspruch und schlägt häufig fehl.
-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> TGewinde mit einer großen Anzahl von Windungen sind problematisch.

## Methode 5. Austragen eines horizontalen Profils 

### Allgemein

Die Idee besteht darin, einen horizontalen Querschnitt des Gewindes entlang einer Helix auszutragen. Das Hauptproblem hierbei ist die Ermittlung des Profils, das zur Herstellung eines solchen Gewindes verwendet werden soll.

<img alt="" src=images/thread-by-horz-profile.png  style="width:600px;">

Wenn man einen Kreis als horizontales Profil verwendet (der Kreis muss außerhalb des Ursprungs platziert werden, dieser Versatz definiert die Tiefe des Gewindes), wird das Gewindeprofil sinusförmig sein.

Um ein Standard Sägezahnprofil zu erhalten, muss ein Paar gespiegelter archimedischer Spiralen zu einem Draht verschmolzen werden. Es entsteht eine Herzform, die von einem Kreis kaum unterscheidbar wird, wenn die Tiefe des Gewindes im Vergleich zu seinem Durchmesser gering ist. Deshalb ist auf dem obigen Bild ein \"dickes\" Gewinde dargestellt.

### Generieren des Profils 

Es ist nicht einfach, das horizontale Profil zu ermitteln, um ein bestimmtes vertikales Profil zu erhalten. Für einfache Fälle wie dreieckig oder trapezförmig kann es manuell konstruiert werden. Alternativ kann es konstruiert werden, indem man mit Methode 3 ein kurzes Gewinde erzeugt und ein Stück davon durch ein [Part Schnittmenge](Part_Common/de.md) zwischen einer horizontalen ebenen Fläche und dem Gewinde erhält.

#### Profil für ein dreieckigförmiges Gewinde 

1.  Erstelle zuerst eine archimedische Spirale in der XY Ebene
    1.  Setze die Anzahl der Windungen auf 0.5
    2.  Setze den Radius auf den Innenradius des Gewindes, der Außenradius entspricht diesem plus der Schnitttiefe.
    3.  Stelle das Wachstum auf die doppelte Schnitttiefe des Gewindes ein.
    4.  [Part Spiegel](Part_Mirror/de.md) die Spirale gegen die XY Ebene
2.  [Part Verschmelzen](Part_Fuse/de.md) die Spirale und den Spiegel, um einen geschlossenen Draht zu erhalten, der wie ein Herz geformt ist.

#### Profil für beliebigen Querschnitt 

<img alt="" src=images/thread-by-horz-profile-profileMake.png  style="width:1000px;">

1.  Erstelle ein vertikales Schnittprofil. Stelle sicher, dass die Höhe der Skizze mit der Steigung des Gewindes übereinstimmt, das du benötigst.




1.  erstelle eine Helix1 mit einer Höhe, die der Steigung entspricht, und einer Steigung, die der Gewindesteigung entspricht, und einem Helixradius von 0,42\*Nenndurchmesser des Gewindes.
2.  trage das Schnittprofil entlang der Helix1 aus. Hake an *Erzeuge Volumenkörper* und *Frenet*.
3.  Erstelle einen Kreis mit dem Nennradius des Gewindes in der x-y-Ebene.
4.  Erstelle eine Fläche aus dem Kreis. (Part Arbeitsbereich: erweitertes Dienstprogramm zum Erstellen von Formen oder [Entwurf Hochstufen](Draft_Upgrade/de.md) und ErstelleFläche = true)
5.  die Fläche mit dem Sweep Profil schneiden\# einen Klon aus dem Schnitt erstellen (Entwurf Arbeitsbereich)
6.  Herabstufung des Klons, um einen Draht zu erlangen. (Entwurf Arbeitsbereich) Dieser Draht ist das horizontale Profil, das für diese Methode benötigt wird.
7.  Erstelle eine Spirale mit dem Radius des Nennradius des Gewindes und einer Steigung des Gewindes und der Höhe des benötigten Gewindes.
8.  Trage den Draht entlang der Spirale aus. Hake Vollmaterial und Frenet an.

Fertig.

Die Schritt-für-Schritt Anleitung wurde diesem [Forumsantwort von Ulrich1a](http://forum.freecadweb.org/viewtopic.php?f=3&t=6506#p52558) entnommen. (\"Erstellen eines Gewindes: Unerwartete Ergebnisse\"), leicht modifiziert.

Die Schritte werden auch in Aktion gezeigt auf [dieses Video von Gaurav Prabhudesai](http://www.youtube.com/watch?v=fxKxSOGbDYs) (\"FreeCAD : Wie Gewinde erstellen\").

### Vor- und Nachteile 

-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> eine gebrauchsfertige, massive Gewinde-auf-einer-Stange Massivform wird direkt durch die Austragung erzeugt.
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> Es werden weniger oder sogar keine booleschen Operationen erforderlich, so dass die Generierungsgeschwindigkeit im Vergleich zu Methode 3 sehr hoch ist.
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> Gewindeenden werden sofort schön geschnitten
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> lange Gewinde sind kein Problem, es sei denn, es ist eine boolesche Operation erforderlich. Andernfalls wird sie nicht viel besser als Methode 3 sein.
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> Gewinde ohne Lücke sind kein Problem.

-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> die Festlegung des Gewindeprofils ist kompliziert.
-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> Die Verwendung des Standardnetz mit einem auf diese Weise erzeugten Gewinde erzeugt hässliche Netze, was zu Problemen führen kann. Andere Netze sind besser, z.B. scheint Mefisto die besten Ergebnisse zu liefern.
-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> großer Speicherplatzbedarf gemäß der [Zusammenstellung von Gewinde-Modellierungstechniken](http://forum.freecadweb.org/viewtopic.php?f=3&t=12593&start=10#p101197).

## Methode 5. Ausformung zwischen wendelförmig extrudierten Flächen 

### Allgemein 

Wendelförmige Splines extrudieren koaxiale Flächen, die ausgeformt werden können, während die parametrische Wendel von FreeCAD dies nicht tut. Zur Definition eines Gewindes sind zwei wendelförmige Splines erforderlich. Diese beiden können aus einem Bibliotheks Spline skaliert und dann entsprechend positioniert und extrudiert werden, um die richtige Form zu erhalten.

Die parametrischen Wendel von FreeCAD sind nicht wirklich spiralförmig, aber wendelförmige B-Splines sind nicht schwer zu entwerfen. Eine manuelle Methode besteht darin, Zwölfeck Polygone (12-seitige Polygone) mit 5 mm Radius/10 mm Durchmesser in 1/12mm (0,08333.mm) z Intervallen anzuordnen und Splines von Knotenpunkt zu Knotenpunkt in aufsteigender und rotierender Folge zu verfolgen, und es in Betracht zu ziehen, dies einmal mit z.B. 10 Windungen zu tun, so dass dieser Spline als Bibliotheksdatei für den Import und die Wiederverwendung wiederverwendet werden kann. Es ist praktisch, 10 mm Durchmesser/1 mm Teilung zu verwenden, um die Skalierung zu erleichtern. Wenn du es manuell machst, ist es einfacher, einen DDraht zu zeichnen und ihn dann in einen B-Spline zu konvertieren, als einen Spline zu zeichnen. Bei Drähten wird die Krümmung nicht während des Zeichnens berechnet, so dass sie dem Cursor folgen und gefügiger einrasten.

Sobald die Splines auf die richtige Größe skaliert und so angeordnet sind, dass die Ausformung den richtigen Winkel zwischen den Gewindeflanken aufweist, werden sie entlang ihrer Achse extrudiert, wobei eine Steigungslänge für den inneren Spline, die äußere Steigung/8, gilt.

<img alt="" src=images/splineextrudeloft.png  style="width:912px;">

ISO- und andere Gewinde haben reduzierte, d.h. flache, innere und äußere Kanten statt scharfer, was für FreeCAD Anwender mit dieser Methode geeignet ist, da wir die wendelförmige Stirnfläche bei der nominalen Größe der Befestigungselemente loften können, während eine Innenfläche nicht an einen Spline an der Außenkante geloft werden kann, weil eine Fläche ein geschlossenes Profil ist, ein Spline ist offen. Die ISO Norm besagt, dass die Nenngröße von Außengewinden eine Steigung der Stirnfläche von 8 mm haben. Das Bild zeigt die Anordnung der Geometrie und die daraus resultierenden wendelförmigen Flächen. Dann ausgeformt zwischen den Stirnseiten, und dann ein Zylinder, der die innere wendelförmige Stirnfläche ergibt, die nach ISO eine Steigung von 4/4 Breite hat, wird zu den Gewinden hinzugefügt.

![761PX](images/Threadform.PNG )

Diese Methode erzeugt zuverlässige Festkörper, die korrekt boolesch sind. Obwohl sie keine \"parametrischen\" Schraubengewinde in Standardgrößen im Sinne eines einfachen Zugriffs auf die Form durch die Größe des Befestigungselements erzeugt, ist es eine einfache Möglichkeit, eine genaue Bibliothek zur Wiederverwendung zu erstellen, und Modelle von Spezialformen wie ACME oder archimedische Schrauben sind auch als Einzelstücke unkompliziert. {{Tutorials navi}}  {{PartDesign Tools navi}} {{Sketcher Tools navi}}

---
[documentation index](../README.md) > Thread for Screw Tutorial/de
