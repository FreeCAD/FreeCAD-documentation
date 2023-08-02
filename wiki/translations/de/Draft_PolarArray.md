---
- GuiCommand:
   Name: Draft PolarArray
   Name/de: Draft PolareAnordnung
   MenuLocation: Änderung -> Array tools -> Polare Anordnung
   Workbenches: Draft_Workbench/de, Arch_Workbench/de
   Version: 0.19
   SeeAlso: Draft_OrthoArray/de, Draft_CircularArray/de, Draft_PathArray/de, Draft_PathLinkArray/de, Draft_PointArray/de, Draft_PointLinkArray/de
---

# Draft PolarArray/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_PolarArray.svg  style="width:24px;"> **Draft PolareAnordnung** erstellt eine Anordnung aus einem ausgewählten Objekt, indem er Kopien entlang einer Kreisumfangslinie positioniert. Der Befehl kann wahlweise auch eine Verknüpfungsanordnung ([Link](App_Link/de.md)-Array,) erstellen, die effizienter ist, als eine normale Anordnung.

Dieser Befehl kann für 2D-Objekte verwendet werden, die mit den Arbeitsbereichen [Draft](Draft_Workbench/de.md) oder [Sketcher](Sketcher_Workbench/de.md) erstellt wurden, aber auch für viele 3D-Objekte, die mit anderen Arbeitsbereichen wie [Part](Part_Workbench/de.md), [PartDesign](PartDesign_Workbench/de.md) oder [Arch](Arch_Workbench/de.md) erstellt wurden.

<img alt="" src=images/Draft_PolarArray_example.png  style="width:400px;"> 
*Draft PolareAnordnung*



## Anwendung

Siehe auch: [Draft Fangen](Draft_Snap/de.md).


<div class="mw-translate-fuzzy">

1.  Wähleein Objekt aus, von dem du die Polaranordnung erstellen möchtest.
2.  Drücke die **[<img src=images/Draft_PolarArray.svg style="width:16px"> [Polar Anordnung](Draft_PolarArray.md)** Schaltfläche. Wenn kein Objekt ausgewählt ist, wird das [Aufgabenpaneel](task_panel/de.md) geöffnet, aber du musst trotzdem ein Objekt auswählen, um fortzufahren.
3.  Wähle den Polarwinkel, der bestimmt, wo sich das letzte Element der Anordnung befindet.
4.  Wähle die Anzahl der Elemente in der Anordnung. Minimum von 2, Maximum von 99.
5.  Wähle das Zentrum der Rotationsachse. Du kannst auf die [3D Ansicht](3D_view/de.md) klicken, um gleichzeitig die Position des Rotationszentrums festzulegen und den Befehl abzuschließen.
6.  Optional hake die verschmelzungs- oder Verknüpfungsoptionen an.
7.  Drücke **OK**, um den Befehl abzuschließen.


</div>



## Optionen


<div class="mw-translate-fuzzy">

-   Drücke **Reset point** um das Drehzentrum auf den Ursprung zu setzen {{Value|(0, 0, 0)}}.
-   Wenn das Kontrollkästchen **Fuse** aktiviert ist, werden die resultierenden Objekte in der Anordnung zu einer einzigen Form verschmolzen, wenn sie einander berühren oder schneiden.
-   Wenn das Kontrollkästchen **Use Links** markiert ist, werden die resultierenden Objekte in der Anordnung nicht als einfache Kopien, sondern als [App Verknüpfungen](App_Link/de.md) erstellt. Dies verbessert die Speichernutzung der Anordnung, da die App Verknüpfung die [Form](Shape/de.md) des Originalobjekts wiederverwendet und keine neuen Formen erstellt. Wenn diese Option verwendet wird, hat das **Fuse** Kontrollkästchen keine Wirkung.
-   Drücke **Esc** oder die **Cancel** Schaltfläche, um den aktuellen Befehl abzubrechen.


</div>



## Hinweise


<div class="mw-translate-fuzzy">

Hinweise:

-   Standardmäßig ist die Rotationsachse die positive Z Achse {{Value|(0, 0, 1)}}. Dies kann im [Eigenschaftseditor](property_editor/de.md) geändert werden, nachdem das Objekt erzeugt wurde.
-   Der Polarwinkel ist positiv im Gegenuhrzeigersinn und negativ im Uhrzeigersinn.
-   Jedes Element in der Anordnung ist ein exakter Klon des ursprünglichen Objekts, aber die gesamte Anordnung wird in Bezug auf Eigenschaften und Aussehen als eine Einheit betrachtet.
-   Mit diesem Befehl wird dasselbe Objekt erstellt, das mit den [Anordnung](Draft_Array/de.md) und [KreisAnordnung](Draft_CircularArray/de.md) Werkzeugen erstellt wurde. Daher kann die Anordnung einfach durch Ändern seiner Eigenschaften in orthogonal, polar oder zirkular umgewandelt werden.


</div>



## Einstellungen

Siehe auch: [Voreinstellungseditor](Preferences_Editor/de.md) und [Draft Einstellungen](Draft_Preferences/de.md).

-   Um die Anzahl der Dezimalstellen für die Eingabe der Koordinaten und Winkel zu ändern: **Bearbeiten → Eigenschaften... → Allgemein → Einheiten → Einheiten-Einstellungen → Anzahl der Nachkommastellen**



## Eigenschaften

Siehe [Draft RechtwinkligeAnordnung](Draft_OrthoArray/de#Eigenschaften.md).



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).



### Parametrische Anordnung 

Zum Erstellen einer parametrischen polaren Anordnung wird die Methode `make_array` des Draft-Moduls verwendet ({{Version/de|0.19}}). Diese Methode ersetzt die veraltete Methode `makeArray`. Die Methode `make_array` kann [Draft RechtwinkligeAnordnungen](Draft_OrthoArray/de.md), Draft PolareAnordnungen und [Draft KreisAnordnungen](Draft_CircularArray/de.md) erstellen. Für jede Anordnungsart stehen eine oder mehrere Wrapper-Methoden zur Verfügung.

Die Hauptmethode:


```python
array = make_array(base_object, arg1, arg2, arg3, arg4=None, arg5=None, arg6=None, use_link=True)
```

The wrapper for polar arrays is:


```python
array = make_polar_array(base_object,
                         number=5, angle=360, center=App.Vector(0, 0, 0),
                         use_link=True)
```


<div class="mw-translate-fuzzy">

-   Erstellt eine Anordnung aus den in `obj` enthaltenen Objekten, die ein einzelnes Objekt oder eine Liste von Objekten sein kann.

-   Der Wert von `center` ist ein Vektor, der den Mittelpunkt des Anordnungkreises definiert; `angle` ist der Winkel des Bogens in Grad, und `number` ist die Anzahl der Kopien im Kreismuster, einschließlich des Originalobjekts.

-   Wenn `use_link` `True` ist, handelt es sich bei den erstellten Kopien um [App Verknüpfungen](App_Link/de.md) und nicht um reguläre Kopien.

-    `array_list`wird mit den neuen Kopien zurückgegeben.

    -   
        `array_list`
        
        ist entweder ein einzelnes Objekt oder eine Liste von Objekten, abhängig von der Eingabe `obj`.


</div>

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
