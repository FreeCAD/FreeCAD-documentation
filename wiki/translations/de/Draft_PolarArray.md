---
 GuiCommand:
   Name: Draft PolarArray
   Name/de: Draft PolareAnordnung
   MenuLocation: Änderung , Anordnungswerkzeuge , Polare Anordnung<br>Bearbeiten , Polare Anordnung
   Workbenches: Draft_Workbench/de, BIM_Workbench/de
   Version: 0.19
   SeeAlso: Draft_OrthoArray/de, Draft_CircularArray/de, Draft_PathArray/de, Draft_PathLinkArray/de, Draft_PointArray/de, Draft_PointLinkArray/de
---

# Draft PolarArray/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_PolarArray.svg  style="width:24px;"> **Draft PolareAnordnung** erstellt eine Anordnung aus einem ausgewählten Objekt, indem er Kopien entlang einer Kreisumfangslinie positioniert. Der Befehl kann wahlweise auch eine Verknüpfungsanordnung ([Link](App_Link/de.md)-Array,) erstellen, die effizienter ist, als eine normale Anordnung.

Dieser Befehl kann für 2D-Objekte verwendet werden, die mit den Arbeitsbereichen [Draft](Draft_Workbench/de.md) oder [Sketcher](Sketcher_Workbench/de.md) erstellt wurden, aber auch für viele 3D-Objekte, die mit anderen Arbeitsbereichen wie [Part](Part_Workbench/de.md), [PartDesign](PartDesign_Workbench/de.md) oder [BIM](BIM_Workbench/de.md) erstellt wurden.

<img alt="" src=images/Draft_PolarArray_example.png  style="width:400px;"> 
*Draft PolareAnordnung*



## Anwendung

Siehe auch: [Draft Fangen](Draft_Snap/de.md).

1.  Wahlweise ein Objekt auswählen.
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_PolarArray.svg" width=16px> [Polare Anordnung](Draft_PolarArray/de.md)** drücken.
    -   [Draft](Draft_Workbench/de.md): Den Menüeintrag **Änderung → Anordnungswerkzeuge → <img src="images/Draft_PolarArray.svg" width=16px> Polare Anordnung** auswählen.
    -   [BIM](BIM_Workbench/de.md): Den Menüeintrag **Bearbeiten → <img src="images/Draft_PolarArray.svg" width=16px> Polare Anordnung** auswählen.
3.  Der Aufgaben-Bereich **Polare Anordnung** wird geöffnet. Siehe [Optionen](#Optionen.md) für wietere Informationen.
4.  Wurde noch kein Objekt ausgewählt: Ein Objekt auswählen.
5.  Im Aufgaben-Bereich die erforderlichen Parameter eingeben.
6.  Um den Befehl abzuschließen, gibt es folgende Möglichkeiten:
    -   Einen Punkt für den **Drehmittelpunkt** in der [3D-Ansicht](3D_view/de.md) auswählen.

    -   
        **Enter**
        
        drücken.

    -   Die Schaltfläche **OK** drücken.



## Optionen

-   Den **Polarwinkel** eingeben, um den Gesamtwinkel der Anordnung festzulegen. Der positive Winkel wird gegen den Uhrzeigersinn angegeben.

-   Die **Anzahl der Elemente** angeben; mindestens {{Value|2}}. Der größte Wert, der im Aufgaben-Bereich eingegeben werden kann ist {{Value|99}}, höhere Werte können aber durch Ändern der {{PropertyData/de|Number Polar}} der Anordnung gesetzt werden.

-   Einen Punkt in der [3D-Ansicht](3D_view/de.md) auswählen (dies schließt auch den Befehl ab) oder dieKoordinaten für den for the **Drehmittelpunkt** eingeben. Die Rotationsachse wird durch diesen Punkt verlaufen. Es ist ratsam, den Mauszeiger aus der [3D-Ansicht](3D_view/de.md) herauzubewegen, bevor die Koordinaten eingegeben werden.

-   Die Schaltfläche **Punkt zurücksetzen** drücken, um den **Drehmittelpunkt** auf den Ursprung (zurück) zu setzen.

-   Ist die Checkbox **Vereinigung** aktiviert, werden überlappende elemente in der Anordnung vereinigt. dies funktioniert nicht mit Verknüpfungsanordnungen (Link-Arrays).

-   Ist die Checkbox **Verknüpfungsanordnung** aktiviert, wird eine Verknüpfungsanordnung anstelle einer normalen Anordnung erstellt. Eine Verknüpfungsanordnung ist effektiver, da ihre Elemente [App-Link](App_Link/de.md)-Objekte sind.

-    **Esc**drücken oder die Schaltfäche **Cancel**, um den Befehl abzubrechen.



## Hinweise

-   Die Standarddrehachse der Anordnung ist die positive Z-Achse. Dies kann durch Anpassen ihrer {{PropertyData/de|Axis}} geändert werden.
-   Eine Draft PolareAnordnung kann in eine [Draft RechtwinkligeAnordnung](Draft_OrthoArray/de.md) oder eine [Draft Kreisanordnung](Draft_CircularArray.md) gewandelt werden, indem ihre {{PropertyData/de|Array Type}} geändert wird.
-   Eine Verknüpfungsanordnung kann nicht in eine normale Anordnung gewandelt werden oder umgekehrt. Die Art der Anordnung muss zum Zeitpunkt der Erstellung entschieden werden.



## Eigenschaften

Siehe [Draft RechtwinkligeAnordnung](Draft_OrthoArray/de#Eigenschaften.md).



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).



### Parametrische Anordnung 

Zum Erstellen einer parametrischen polaren Anordnung wird die Methode `make_array` des Draft-Moduls verwendet ({{Version/de|0.19}}). Diese Methode ersetzt die veraltete Methode `makeArray`. Die Methode `make_array` kann [Draft RechtwinkligeAnordnungen](Draft_OrthoArray/de.md), Draft PolareAnordnungen und [Draft KreisAnordnungen](Draft_CircularArray/de.md) erstellen. Für jede Anordnungsart stehen eine oder mehrere Wrapper-Methoden zur Verfügung.

Die Hauptmethode:


```python
array = make_array(base_object, arg1, arg2, arg3, arg4=None, arg5=None, arg6=None, use_link=True)
```

Der Wrapper für polare Anordnungen ist:


```python
array = make_polar_array(base_object,
                         number=5, angle=360, center=App.Vector(0, 0, 0),
                         use_link=True)
```

-    `base_object`ist das Objekt, das angeordnet wird. Es kann auch das `Label` (Benennung) eines Objekts im Dokument sein.

-    `number`ist die Anzahl der Elemente in dem Muster inklusive des Originalobjekts.

-    `angle`ist der Winkeldes polaren Bogens in Grad.

-    `center`ist der Vektor, der den Mittelpunkt des Musters festlegt.

-   Ist `use_link` auf `True` gesetzt, sind die erstellten Elemente [App-Links](App_Link.md) anstatt normale Kopien.

-    `array`wird mit dem erstellten Anordnungsobjekt zurückgegeben.

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

tri = Draft.make_polygon(3, 600)
center = App.Vector(-1600, 0, 0)

array = Draft.make_polar_array(tri, 8, 270, center)
doc.recompute()
```



### Nichtparametrische Anordnung 

Zum Erstellen einer nichtparametrischen Anordnung wird die Methode `array` des Draft-Moduls verwendet. Diese Methode gibt `None` zurück.


```python
array(objectslist, center, angle, number)
```

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

tri = Draft.make_polygon(3, 600)
center = App.Vector(-1600, 0, 0)

Draft.array(tri, center, 270, 8)
doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft PolarArray/de
