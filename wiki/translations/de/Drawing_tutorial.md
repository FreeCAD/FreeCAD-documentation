---
- TutorialInfo:/de
   Topic: Blaupausen/ Zeichnungen
   Level: Anfänger
   Time: 15 Minuten
   Author:[http://freecadweb.org/wiki/index.php?title=User:Drei Drei]
   FCVersion:0.16 oder neuer
   Files:
---

# Drawing tutorial/de

 **Entwicklung des [Drawing Arbeitsbereich](Drawing_Workbench/de.md) wurde in FreeCAD v0.16 gestoppt und der neue in v0.17 eingeführte [TechDraw-Arbeitsbereich](TechDraw_Workbench/de.md) zielt darauf, ihn zu ersetzen. Beide Arbeitsbereiche werden in v0.17 bereitgestellt, aber der Drawing-Arbeitsbereich könnte in zukünftigen Ausgaben entfernt werden.**



### Einleitung

Dieses Tutorial soll den Leser in den Arbeitsbereich [Zeichnung](Drawing_Workbench/de.md) und andere Elemente zum Erstellen von Blaupausen einführen.

<img alt="" src=images/Drawing_tutorial_result.png  style="width:480px;">

### Voraussetzungen

-   FreeCAD Version 0.16 oder neuer
-   Grundlagenwissen über die Arbeitsbereiche *Part* und *PartDesign*
-   Das [Entwurfstutorium](Draft_tutorial/de.md) wurde bereits abgeschlossen

### Prozedur

#### Vorbereitungen

Um den Zeitaufwand für dieses Tutorial zu reduzieren, ist es zwingend erforderlich ähnliche Elemente im Modellbaum zu gruppieren, um eine Operation auf mehrere Elemente gleichzeitig anwenden zu können.

#### Gruppieren von Elementen 

1.  Im **Modellbaum** einen Rechtsklick auf den Dokumentnamen (Standard: *Unbenannt*) ausführen.
2.  Im dann sichtbaren Menü auf **Gruppe erstellen** klicken und die Gruppe bei Bedarf umbenennen (mit Doppelklick auf die Gruppe).
3.  Die passenden Elemente im Modellbaum auswählen und bei gedrückter Maustaste in die Gruppe ziehen.

Erstellen Sie folgende Gruppen:

-   Draft_objects
-   Draft_dimensions
-   Draft_annotations_text

#### Schablonen zeichnen 

Schablonen sind die Grundlage für das Erstellen von Zeichnungen, wobei entweder die mitgelieferten Schablonen oder selbst erstellte verwendet werden können.

Wählen Sie im Arbeitsbereich *Drawing* das Untermenü neben der Schaltfläche [A3 landscape](Drawing_Landscape_A3/de.md) <img alt="" src=images/Drawing_Landscape_A3.png  style="width:32px;"> und klicken Sie auf *A4 Landschaft* (Alternativ über das Menü **Zeichnung \> Neue Zeichnung einfügen \> A4 Landschaft**).

Im Modellbaum ist nun ein neuer Ordner namens *Page* zu sehen. Darin werden alle zur Zeichnung gehörenden Elemente vom Programm gespeichert.

#### Projektionen

Projektionen sind definiert als visuelle Repräsentation eines 3D-Objektes auf einer bestimmten Ebene. Es stellt die verschiedenen Eigenschaften des Objektes aus Sicht dieser Ebene dar.

##### Orthografische Projektionen 

Diese Art der Projektion wird in den Ingenieurwissenschaften genutzt, um bestimmte Eigenschaften des Objektes, z.B. Maße oder Winkel, vor der Herstellung festzulegen und darzustellen. Dabei gibt es zwei übliche Standards: **Dritter Winkel** und **Erster Winkel** Projektionen.

In diesem Tutorial werden diese beiden Standardprojektionen jedoch nicht verwendet, weil das Beispielobjekt nur in der XY-Ebene sinnvoll dargestellt werden kann.

1.  Wählen Sie das Objekt, das in die Zeichnung projeziert werden soll.
2.  Klicken Sie auf [Orthografische Ansichten einfügen](Drawing_Orthoviews/de.md) <img alt="" src=images/Drawing_Orthoviews.png  style="width:32px;">
3.  Wählen Sie die gewünschten Eigenschaften der Projektion und der Ansicht aus

In den Tabs **Allgemein** und **Axonometrisch** können der Ort, die Skalierung und der Abstand der Darstellungen für jede Ansicht festgelegt werden.

##### Andere Projektionen 

Es ist auch möglich, eigene Ansichten des Objekts zu erstellen

1.  Wählen Sie das zu projezierende Objekt aus
2.  Klicken Sie auf [Ansicht in Zeichnung einfügen](Drawing_View/de.md) <img alt="" src=images/Drawing_View.png  style="width:32px;">, sodass ein neues Objekt namens *View* im Modellbaum erscheint.
3.  Nach einem Klick auf das neue Objekt kann im Tab *Daten* die Blickrichtung durch Ändern der Koordinaten *X*, *Y* und *Z* unter *Direction* geändert werden. Standardmäßig ist hier (0,0,1) eingetragen.

Im gleich Tab lassen sich auch der Ort (*location*), die Skalierung (*scale*) und der Drehwinkel (*rotation*) der Ansicht ändern.

##### Entwurfsprojektionen

Objekte die mittels des Arbeitsbereichs *Draft* erstellt wurden, sollten idealerweise mit dem dort verfügbaren Werkzeug *Zeichnung* <img alt="" src=images/Draft_PutOnSheet.png  style="width:16px;"> dargestellt werden. Auf diesem Wege lassen sich Maße, Anmerkungen, *Shapestrings* und andere Elemente des Arbeitsbereichs *Draft* einfügen.

1.  Wechseln Sie in den Arbeitsbereich *Draft*
2.  Wählen Sie die Gruppe von Objekten oder das Objekt, das dargestellt werden soll. In diesem Falls ist das **Draft_dimensions**.
3.  Klicken Sie auf [Zeichnung](Draft_Drawing/de.md) ![](images/Draft_PutOnSheet.png )
4.  Ändern Sie die X- und Y-Koordinate in (140, 100)
5.  Ändern Sie die Skalierung in 0.5

Wiederholen Sie die letzten Schritte für jede Gruppe.

#### Exportieren der Zeichnungen 

FreeCAD unterstützt den Export als SVG und PDF Dateien, basierend auf den eigenen Zeichnungen

##### SVG

1.  Klick auf <img alt="" src=images/Drawing_Save.png  style="width:32px;"> [Save sheet](Drawing_Save.md)
2.  Legen Sie den Pfad und den Namen der zu exportierenden Datei fest

##### PDF

1.  In dem Menü **Datei** den Punkt **Exportiere PDF \...** auswählen
2.  Legen Sie den Pfad und den Namen der zu exportierenden Datei fest

Wir sind nun fertig mit dem grundlegenden Arbeitsablauf für den [Drawing-Arbeitsbereich](Drawing_Workbench/de.md).



## Empfohlene Lektüre 

-   Um zu lernen, wie man eigene Vorlagen erstellt, siehe [Zeichnungsvorlage Anleitung](Drawing_Template_HowTo/de.md)
-   Für weitere Informationen über die verfügbaren Werkzeuge siehe die Seite [Zeichnung-Arbeitsbereich](Drawing_Workbench/de.md)


{{Drawing Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Drawing](Category_Drawing.md) > Drawing tutorial/de
