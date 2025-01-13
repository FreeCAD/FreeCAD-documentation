---
 GuiCommand:
   Name: Draft CircularArray
   Name/de: Draft KreisAnordnung
   MenuLocation: Änderung , Array tools , Kreis-Anordnung
   Workbenches: Draft_Workbench/de
   Version: 0.19
   SeeAlso: Draft_OrthoArray/de, Draft_PolarArray/de, Draft_PathArray/de, Draft_PathLinkArray/de, Draft_PointArray/de, Draft_PointLinkArray/de
---

# Draft CircularArray/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_CircularArray.svg  style="width:24px;"> **Draft KreisAnordnung** erstellt eine Anordnung aus einem ausgewählten Objekt, indem er Kopien auf konzentrischen Kreisringen positioniert. Der Befehl kann wahlweise eine Verknüpfungsanordnung ([Link](App_Link.md)-Array) erstellen, die effizienter ist als eine normale Anordnung.

Dieser Befehl kann für 2D-Objekte verwendet werden, die mit den Arbeitsbereichen [Draft](Draft_Workbench/de.md) oder [Sketcher](Sketcher_Workbench/de.md) erstellt wurden, aber auch für viele 3D-Objekte, die mit anderen Arbeitsbereichen wie [Part](Part_Workbench/de.md), [PartDesign](PartDesign_Workbench/de.md) oder [BIM](BIM_Workbench/de.md) erstellt wurden.

<img alt="" src=images/Draft_CircularArray_example.png  style="width:400px;"> 
*Draft Kreis-Anordnung*



## Anwendung

Siehe auch: [Draft Fangen](Draft_Snap/de.md).

1.  Wähle optional ein Objekt.
2.  Es gibt verschiedene Möglichkeiten den Befehl aufzurufen:
    -   Drücke die **<img src="images/Draft_CircularArray.svg" width=16px> [Draft Kreisförmige Anordnung](Draft_CircularArray/de.md)** Schaltfläche.
    -   Wähle die **Änderung → Anordnungswerkzeuge → <img src="images/Draft_CircularArray.svg" width=16px> Kreisförmige Anordnung** Option aus dem Menü.
3.  Das Aufgabenfenster **Kreisförmige Anordnung** öffnet. Siehe [Optionen](#Options.md) für weitere Information.
4.  Wenn bis jetzt kein Objekt ausgewählt ist: wähle ein Objekt aus.
5.  Gib die notwendigen Parameter im Ausgabefenster ein.
6.  Um den Befehl zu beenden mache eines der Folgenden:
    -   Wähle eine Punkt in der [3D Ansicht](3D_view/de.md) als **Mitte der Drehung**.
    -   Drücke **Enter**.
    -   Drücke die **OK** Schaltfläche.



## Optionen

-   Gib den **Radialabstand** ein, um den Abstand zwischen den umlaufenden Ebenen und zwischen dem Mittelpunkt und der ersten umlaufenden Ebene festzulegen.
-   Gib den **Tangentialer Abstand** ein um den Abstand zwischen den Elementen auf der gleichen umlaufenden Ebene festzulegen. Muss größer als Null sein.
-   Gib **Anzahl der kreisförmigen Ebenen** ein. Das Element in der Mitte gilt als eine Ebene. Muss mindestens {{Value|2}} sein. Das Maximum, welches im Arbeitsfenster eingegeben werden kann ist {{Value|99}}, aber nach dem Ändern der **Number Circles** Eigenschaft der Ebene sind größere Werte möglich.
-   Gib den **Symmetrie** Wert ein. Dieser Wert unterscheidet, wie die Elemente verteilt sind. Zum Beispiel der Wert {{Value|3}} ergibt ein Muster mit drei gleichen 120° Tortensegmenten. Größere Werte von **Symmetrie** und **Tangentialer Abstand** ergeben weniger oder gar keine Elemente in den inneren Ebenen.
-   Wähle einen Punkt in der [3D Ansicht](3D_view/de.md), beachte das beendet den Befehl, oder tippe Koodinaten für den **Drehmittelpunkt** ein. Die Drehachse der Ebene wird durch diesen Punkt verlaufen. Es ist zweckmäßig den Zeiger vor der Eingabe der Koordinaten aus der [3D Ansicht](3D_view/de.md) zu bewegen.
-   Drücke die **Punkt zurücksetzen** Schaltfläche um den **Drehmittelpunkt** auf den Ursprung zurück zu setzen.
-   Wenn das **Vereinigen** Optionsfeld ausgewählt ist, dann werden überlappende Elemente in der Ebene vereinigt. Das funktioniert nicht für verbundene Ebenen.
-   Wenn das **Verknüpfungsanordnung** Optionsfeld ausgewählt ist, dann wird an Stelle einer regulären Ebene eine verbundene Ebene erzeugt. Eine verbundene Ebene ist effizienter, weil die Elemente [App Link](App_Link/de.md) Objekte sind.
-   Drücke **Esc** oder die **Cancel** Schaltfläche um den Befehl abzubrechen.



## Hinweise

-   Die Standard Drehachse für die Ebene ist die positive Z Achse. Das kann durch Bearbeiten seiner **Achse** Eigenschaft verändert werden.
-   Eine Draft Kreisanordnung kann durch Ändern der **Ebenen Type** Eigenschaft in eine [Draft RechtwinkeligeAnordnung](Draft_OrthoArray/de.md) oder eine [Draft PolareAnordnung](Draft_PolarArray/de.md) geändert werden.
-   Eine verbundene Ebene kann nicht in eine reguläre Ebene umgewandelt werden, oder umgekehrt. Der Typ einer Ebene muss bei deren Erzeugung entschieden werden.



## Eigenschaften

Siehe [Draft RechtwinkligeAnordnung](Draft_OrthoArray/de#Eigenschaften.md).



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Zum Erstellen einer Kreis-Anordnung wird die Methode `make_array` des Draft-Moduls verwendet ({{Version/de|0.19}}). Diese Methode ersetzt die veraltete Methode `makeArray`. Die Methode `make_array` kann [Draft RechtwinkligeAnordnungen](Draft_OrthoArray/de.md), [Draft PolareAnordnungen](Draft_PolarArray.md) und Draft Kreis-Anordnungen erstellen. Für jede Anordnungsart stehen eine oder mehrere Wrapper-Methoden zur Verfügung.

Die Hauptmethode:


```python
array = make_array(base_object, arg1, arg2, arg3, arg4=None, arg5=None, arg6=None, use_link=True)
```

Der Wrapper für Kreis Anordnung ist:


```python
array = make_circular_array(base_object,
                            r_distance=100, tan_distance=50,
                            number=3, symmetry=1,
                            axis=App.Vector(0, 0, 1), center=App.Vector(0, 0, 0),
                            use_link=True)
```

-    `base_object`ist das Objekt, aus dem ein Array erzeugt wird. Es kann auch die `Label` (string) eines Objektes im aktuellen Dokument sein.

-    `r_distance`und `tan_distance` sind die radialen und tangentialen Abstände zwischen den Elementen.

-    `number`ist die Anzahl der umlaufenden Layer im Muster, das Originalobjekt gilt als erster Layer.

-    `symmetry`ist eine ganze Zahl, die in einigen Berechnungen verwendet wird welche die Art wie die Elemente über den Kreisumfang verteilt werden, beeinflussen. Üblich sind Werte von 1 bis 6. Größere Werte werden nicht empfohlen und können die Elemente der inneren Layer zum Verschwinden bringen.

-    `axis`und `center` sind Vektoren welche die Richtung der Drehachse und einen Punkt durch den die Achse verläuft beschreiben.

-   Wenn `use_link` auf `True` ist, dann sind die erzeugten Elemente [App Links](App_Link.md) sonst sind sie normale Kopien.

-    `array`wird mit dem erzeugten Array zurück gegeben.

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

tri = Draft.make_polygon(3, 600)

array = Draft.make_circular_array(tri, 1800, 1200, 4, 1)
doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft CircularArray/de
