# Basic TechDraw Tutorial/de
---
- TutorialInfo:/de
   Topic:Modellierung
   Level:Anfänger
   Author:[WandererFan](User_WandererFan.md)
   Time:Weniger als eine Stunde
   FCVersion:0.17 oder höher
   Files:[https://github.com/FreeCAD/Examples/blob/master/Basic_Part_Design_Tutorial_Example_017_Files/Basic_Part_Design_Tutorial_017.fcstd
Basic Part Design for v0.17 Sample]<br />[https://github.com/FreeCAD/Examples/blob/master/Basic_TechDraw_Tutorial_Example_Files/Basic_TechDraw_Tutorial.fcstd Basic TechDraw Tutorial Sample]
}}

## Einführung

Dieses Tutorium führt den neuen Anwender in einige der verwendeten Werkzeuge und Techniken des **![](images/)**_ein. Dieses Tutorium ist kein vollständiger und umfassender Führer zum TechDraw Arbeitsbereich und viele der Werkzeuge und Möglichkeiten werden nicht abgedeckt. Dieses Tutorium nimmt den Anwender mit durch die benötigten Schritte, um technische Zeichnungen des Teils aus dem [Grundlagen Part Design Tutorium](Basic_Part_Design_Tutorial/de.md) zu erzeugen.

## Bevor Du anfängst 

Lade die [Beispieldatei](https://github.com/FreeCAD/Examples/blob/master/Basic_Part_Design_Tutorial_Example_017_Files/Basic_Part_Design_Tutorial_017.fcstd) aus dem Part Design Tutorium herunter.

## Die Aufgabe 

In diesem Tutorium wirst Du den TechDraw Arbeitsbereich verwenden, um aus dem folgenden 3D Teil verschiedene 2D Zeichnungen zu erzeugen. Wir werden mehrere Ansichten des Teils erstellen und wichtige Bemaßungen hinzufügen. Dieses Tutorium wird nicht jede Funktion und jedes Werkzeug innerhalb des TechDraw Arbeitsbereichs verwenden, sollte aber genug zeigen, um dem Anwender dieses Tutoriums eine grundlegende Basis erhält, auf der er seine Kenntnisse und Fähigkeiten aufbauen kann.

## Das Bauteil 

![](images/Tut17_final_refined.png )

## Erstellen einer Zeichnung 

### Anfang

-   Du möchtest vielleicht deine [Einstellung](TechDraw_Preferences/de.md) Einstellungen vor dem Anfang anpassen. Siehe Anmerkung 1.
-   Öffne zuerst die Datei, die unser 3D Teil enthält. Stelle dann sicher, dass du dich im TechDraw Arbeitsbereich befindest.
-   Du wählst die Elemente im Zeichnungsfenster und/oder im Combo Paneel aus. Die Auswahl in TechDraw funktioniert auf dieselbe Weise wie im 3D Fenster. Die Elemente werden gelb, wenn sich der Cursor in der Position befindet, in der sie ausgewählt werden sollen, und werden grün, wenn sie ausgewählt werden. Um mehrere Elemente auszuwählen, verwende beim Klicken die **Strg** Taste und halte sie gedrückt.

### Ansichten und Abmessungen 

Jede Arbeit in TechDraw beginnt mit einer Zeichnungsseite (Page). Zeichnungsseiten basieren auf Vorlagen und enthalten Ansichten.

1.  Klicke auf <img alt="" src=images/TechDraw_PageDefault.svg  style="width:32px;"> [TechDraw StandardSeite](TechDraw_PageDefault/de.md), um eine neue Seite zu erstellen.
2.  Klicke auf den zu zeichnenden Körper in der [3D-Ansicht](3D_view/de.md) oder in der [Combo Ansicht](Combo_view.md) (linke Seite oben).
3.  Klicke auf <img alt="" src=images/TechDraw_View.svg  style="width:32px;"> [TechDraw Ansicht](TechDraw_View/de.md). Es wird die Ansicht zu der Seite hinzugefügt, die wir gerade erstellt haben.

Jetzt haben wir eine Ansicht auf der Seite, die die Oberseite des Körpers zeigt. Es ist allerdings ein bisschen klein.

![](images/TDTut_TopView1to1.png )

1.  Wähle in der [Combo Ansicht](Combo_view/de.md) \"ProjGroup\" und gehe unten im Daten-Reiter zu \"Scale\".
2.  Ändere den Maßstab von 1 auf 2 und drücke **Enter**. Die Ansicht wird größer.
3.  Ziehe die Ansicht mit gedrückter linker Maustaste auf dem Zeichenblatt wohin Du willst.

![](images/TDTut_TopView2to1.png )

Besser, aber ein wenig langweilig. Lass\' uns einige Bemaßungen hinzufügen.

1.  Wähle den oberen linken Eckpunkt (kleiner Punkt) mit dem **LMB** (linken Maus-Button), wähle dann auch (**Strg**+**LMB**) den unteren linken Eckpunkt.
2.  Klicke auf <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width:32px;"> [TechDraw VertikaleBemaßung](TechDraw_VerticalDimension/de.md). Ziehe den Bemaßungstext weg vom Körper.
3.  Versuche das nochmal mit den oberen linken und oberen rechten Knoten und <img alt="" src=images/TechDraw_HorizontalDimension.svg  style="width:32px;"> [TechDraw HorizontaleBemaßung](TechDraw_HorizontalDimension/de.md).

![](images/TDTut_TopView2Dims.png )

### Änderbarer Text 

Wir sollten ein wenig Dokumentation zu unserer Zeichnung hinzufügen.

1.  Klicke auf das kleine grüne Quadrat neben \"Title\" im Dokumentationsblock. Es öffnet sich ein Fenster, in dem Du \"Title\" in etwas Sinnvolleres änderst.
2.  Nur zur Übung kannst Du Deinen Namen im \"Designed by Name\"-Feld auf die gleiche Weise ändern.

![](images/TDTut_DocBlock.png )

Es wird besser. Lass\' uns etwas Text auf der Seite hinzufügen.

1.  Klicke auf <img alt="" src=images/TechDraw_Annotation.svg  style="width:32px;"> [TechDraw Anmerkungen](TechDraw_Annotation/de.md). In der Mitte der Seite erscheint ein Textblock.
2.  Ziehe den Textblock mit der linken Maustaste dorthin, wo Du ihn haben willst.
3.  Klicke in der Combo Ansicht (linke Seite oben) auf \"Annotation\". Daraufhin erscheint das zugehörige Eigenschaftsfeld (linke Seite unten) mit zwei Reitern
4.  Klicke auf den Reiter \"Daten\". Oben im Eigenschaftsfeld siehst Du \"Default Text\", dort klickst Du hinein. Es erscheinen 3 Punkte ganz rechts in diesem Feld. Dort klickst Du und ein neues Fenster öffnet sich. Lösche den Text darin und ersetze ihn mit einem von Dir gewünschten Text.

![](images/TDTut_Annotation.png )

Bevor wir diese Seite verlassen, können wir uns ansehen, wie es aussieht, wenn wir es ausdrucken.

1.  Klicke auf <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width:32px;"> [TechDraw ToggleFrame](TechDraw_ToggleFrame/de.md). Die Knoten und Ansichtsrahmen werden verschwinden. Durch erneutes Klicken auf \"Toggle\" erscheinen sie wieder.

![](images/TDTut_Toggle.png )

### Mehrfache Ansichten eines Einzelteils 

Lass uns eine Mehransichtzeichnung mit einer anderen Vorlage als Ausgangspunkt erstellen. Wir werden die Konvention des ersten Winkels verwenden, aber du kannst zum dritten Winkel wechseln, wenn das deine lokale Konvention ist.

1.  Klicke auf <img alt="" src=images/TechDraw_PageTemplate.svg  style="width:32px;"> [TechDraw SeitenVorlage](TechDraw_PageTemplate/de.md). Ein Dateiauswahldialog erscheint, aus dem eine Vorlagedatei auszuwählen ist. Wir werden \"ANSIB.SVG\" verwenden. Ein neuer Reiter erscheint.
2.  Wähle \"Body\" und \"Page001\" (wenn Du mehr als eine Seite in Deinem Dokument hast, musst Du TechDraw mitteilen, welche zu verwenden ist).
3.  Klicke auf <img alt="" src=images/TechDraw_ProjectionGroup.svg  style="width:32px;"> [TechDraw ProjektionsGruppe](TechDraw_ProjectionGroup/de.md). Die bekannte kleine Ansicht in der Seitenmitte und ein Dialog im Aufgaben-Panel erscheinen. Wir werden bei \"Projektion\" \--\> \"Erster Winkel\" verwenden, Du kannst aber auch \"Dritter Winkel\" nutzen.
4.  Klicke mehrere zusätzliche Ansichten in \"Sekundäre Projektion\" in der Dialogbox an. Bestätige mit \"Anwenden\" und \"OK\".
5.  Ziehe mit der linken Maustaste die Ansicht namens \"Front\". Die sekundären Projektionsansichten folgen der Verschiebung.
6.  Gehe in der Combo Ansicht (linke Seite oben) auf \"ProjGroup\" und Doppelklick. In der sich öffnenden Box bei \"Skalieren\" auf \"Benutzerdefiniert\". Ändere den Maßstab auf 2:1 und bestätige mit \"Anwenden\" und **OK**.

![](images/TDTut_ProjGroup21.png )

1.  Wähle in der Ansicht \"TopLeftFront\" die beiden Knoten an den äußersten Enden der Vorderkante des Werkstücks.
2.  Klicke auf <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:32px;"> [TechDraw LängenBemaßung](TechDraw_LengthDimension/de.md). Ziehe den Bemaßungstext weg vom Körper.

### Verbinden von Bemaßungen mit dem 3D Modell 

Hast Du ein Problem mit der Bemaßung bemerkt, die wir gerade angelegt haben?

![](images/TDTut_NewLengthDim.png )

Aus dem ersten Teil dieses Tutorials wissen wir, dass das Werkstück 53 mm breit ist, aber unsere neuen Abmessungen lauten 43,27. Das liegt daran, dass \"FrontTopLeft\" eine [isometrische Projektion](https://en.wikipedia.org/wiki/Isometric_projection) ist, und unsere erste Zeichnung eine [orthogonale (Mehrfachansichts) Projektion](https://en.wikipedia.org/wiki/Orthographic_projection) war. Um den richtigen Wert zu erhalten, müssen wir unsere Bemaßung direkt mit dem 3D Modell verknüpfen.

1.  Beachte den Namen unserer fehlerhaften Bemaßung im Combo Paneel. Wir brauchen sie in einer Minute.
2.  Wechsle zum 3D Reiter und wähle die Knoten der Vorderkante des Werkstücks. Wähle auch Page001.
3.  Klicke auf <img alt="" src=images/TechDraw_LinkDimension.svg  style="width:32px;"> [TechDraw BemaßungVerknüpfen](TechDraw_LinkDimension/de.md). Ein Dialog wird im Aufgabenpaneel geöffnet.
4.  Verschiebe in diesem Dialog unsere Bemaßung von der Spalte Verfügbar in die Spalte Ausgewählt. Drücke **OK**.
5.  Kehre zurück zu Page001. Unsere Bemaßung sollte nun den korrekten Wert von 53 anzeigen (Wenn Du immer noch 43.27 siehst, solltest Du die **Neuberechnen** Schaltfläche drücken oder den Bemaßungswert ein wenig ziehen, bis er sich ändert).

## Weitermachen

In diesem Tutorial hast Du genug über TechDraw kennengelernt, um eine Zeichnung wie diese (von [NormandC](User_Normandc.md)) zu erstellen. Siehe Anmerkung 2.

![](images/TDTut_FC018_TechDraw_Dim_Iso_View_01_NC.png )

Es gibt viel mehr Funktionalitäten in TechDraw zu erforschen - Section Views, Detail Views, Svg Symbols, Images, face hatching.

## Anmerkungen

1.  Es gibt einen exzellenten Satz von vorgeschlagenen Einstellungen in diesem (englischsprachigen) [Forumseintrag](https://www.forum.freecadweb.org/viewtopic.php?f=3&t=30083#p248189).
2.  Diese Zeichnung wurde mit v0.18 erstellt. Sie zeigt Bemaßungen im richtigen Format für eine isometrische Ansicht. In v0.17 sind die Verlängerungslinien (?; extension lines) rechtwinklig zur Kante anstatt an den Achsen ausgerichtet.

## Zusätzliche Quellen 

-   FreeCAD-Datei dieser Übung zum Vergleich (erstellt mit v0.17) [Download](https://github.com/FreeCAD/Examples/blob/master/Basic_TechDraw_Tutorial_Example_Files/Basic_TechDraw_Tutorial.fcstd)


 {{TechDraw Tools navi}} {{Userdocnavi
---



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [TechDraw](Category_TechDraw.md) > Basic TechDraw Tutorial/de
