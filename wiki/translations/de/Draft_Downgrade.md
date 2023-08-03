---
 GuiCommand:
   Name: Draft Downgrade
   Name/de: Entwurf Herabstufen
   MenuLocation: Änderung , Herabstufen
   Workbenches: Draft_Workbench/de, Arch_Workbench/de
   Shortcut: **D** **N**
   SeeAlso: Draft_Upgrade/de, Part_Cut/de
---

# Draft Downgrade/de

## Beschreibung

Der <img alt="" src=images/Draft_Downgrade.svg  style="width:24px;"> **Entwurf Herabstufen** Befehl stuft ausgewählte Objekte herab. Das Ergebnis ist abhängig von der Anzahl der ausgewählten Objekte und deren Typ. Der Befehl kann zum Beispiel einen 3D Körper in einzelne Flächen und einen Draht in einzelne Kanten zerlegen. Wenn zwei Flächen ausgewählt sind, wird daraus ein [Part Schnitt](Part_Cut/de.md) Objekt erzeugt. Beachte, dass nicht alle Objekte zerlegt werden können. Dieser Befehl ist das Gegenstück zum Befehl [Entwurf Hochstufen](Draft_Upgrade/de.md).

<img alt="" src=images/Draft_Downgrade_example.jpg  style="width:400px;"> 
*Zwei überlappende Flächen werden zu einem Part Schnitt Objekt herabgestuft, das wiederum zu einer Fläche herabgestuft wird. Diese Fläche wird dann zu einem geschlossenen Draht herabgestuft, der schließlich zu separaten Kanten herabgestuft wird.*

## Anwendung

1.  Wähle optional ein oder mehrere Objekte aus.
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Drücke die **<img src="images/Draft_Downgrade.svg" width=16px> [Entwurf Herabstufen](Draft_Downgrade/de.md)**.
    -   Wähle die Option **Änderung → <img src="images/Draft_Downgrade.svg" width=16px> Herabstufen** aus dem Menü.
    -   Verwende das Tastaturkürzel: **D** dann **N**.
3.  Wenn du noch kein Objekt ausgewählt hast: Wähle ein Objekt in der [3D Ansicht](3D_view/de.md).

## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://www.freecadweb.org/api) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um Objekte herabzustufen, verwende die `downgrade` Methode des Entwurf Moduls.


```python
downgrade_list = downgrade(objects, delete=False, force=None)
```

-    `objects`enthält die Objekte, die herabgestuft werden sollen. Es ist entweder ein einzelnes Objekt oder eine Liste von Objekten.

-   Wenn `delete` gleich `True` ist, werden die Quellobjekte gelöscht.

-    `force`erzwingt eine bestimmte Art der Herabstufung durch den Aufruf einer bestimmten internen Funktion. Das kann sein: `"explode"`, `"shapify"`, `"subtr"`, `"splitFaces"`, `"cut2"`, `"getWire"`, `"splitWires"` oder `"splitCompounds"`.

-    `downgrade_list`wird zurückgegeben. Es ist eine Liste, die zwei Listen enthält: eine Liste der neuen Objekte und eine Liste der zu löschenden Objekte. Wenn `delete` `True` ist, ist die zweite Liste leer.

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

circle = Draft.make_circle(1000)
rectangle = Draft.make_rectangle(2000, 800)
doc.recompute()

add_list1, delete_list1 = Draft.upgrade([circle, rectangle], delete=True)

compound = add_list1[0]
add_list2, delete_list2 = Draft.downgrade(compound, delete=False)
face = add_list2[0]
add_list3, delete_list3 = Draft.downgrade(face, delete=False)

box = doc.addObject("Part::Box", "Box")
box.Length = 2300
box.Width = 800
box.Height = 1000

add_list4, delete_list4 = Draft.downgrade(box, delete=True)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Downgrade/de
