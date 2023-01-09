---
- GuiCommand:/de
   Name:Arch Pipe
   Name/de:Arch Rohr
   MenuLocation:Arch → Pipe tools → Rohr
   Workbenches:[Arch](Arch_Workbench/de.md)
   Shortcut:**P** **I**
   Version:0.17
   SeeAlso:[Arch RohrVerbinder](Arch_PipeConnector/de.md), [Arch Ausstattung](Arch_Equipment/de.md)
---

# Arch Pipe/de

## Beschreibung

Dieses Werkzeug ermöglicht es, Rohre von Grund auf oder aus ausgewählten Objekten zu erstellen. Die ausgewählten Objekte müssen Teilbasiert sein (Entwurf, Skizze, etc\...) und einen und nur einen offenen Draht enthalten.

## Anwendung

1.  Wähle optional eine lineare [Part](Part_Workbench/de.md) Form wie eine [Draft Line](Draft_Line/de.md), a [Entwurf Draht](Draft_Wire/de.md) oder eine offene [Skizze](Sketcher_NewSketch/de.md).
2.  Rufe diesen Befehl mit mehreren Methoden auf:
    -   Drücken der **<img src="images/Arch_Pipe.svg" width=16px> [Arch Rohr](Arch_Pipe/de.md)** Schaltfläche auf der Werkzeugleiste.
    -   Drücken der **P** dann **I** Tastaturkürzel.
    -   Drücken der **Arch → Rohrwerkzeuge → Rohr** Eintrag aus dem oberen Menü.

## Optionen

-   Rohre haben die gemeinsamen Eigenschaften und Verhaltensweisen aller [Arch Komponenten](Arch_Component/de.md) gemeinsam

## Eigenschaften

-    **Länge**: Setzt die Länge dieses Rohrs, wenn sie nicht auf einem Draht basiert

-    **Durchmesser**: Der Durchmesser dieses Rohres, wenn es nicht auf einem Profil basiert

-    **Basis**: Der Basisdraht dieses Rohrs, falls vorhanden

-    **Profil**: Das Basisprofil dieses Rohres. Wenn nicht angegeben, ist das Rohr zylindrisch.

## Typischer Arbeitsablauf 

-   Beginne mit der Platzierung von Sanitär-/Hydraulikgeräten (unten ist eine importierte step datei). Du verwandelst diese Objekte in Arch Ausstattungen, indem du sie auswählst und die Schaltfläche [Arch Ausstattung](Arch_Equipment/de.md) drückst.

![](images/Arch_pipe_example_01.jpg )


<div class="mw-translate-fuzzy">

-   Arch Equipments haben jetzt eine neue **FangPunkte** Eigenschaft, bei der es sich um eine Liste von 3D Vektoren handelt. Dies erlaubt dir benutzerdefinierte Fangpunkte hinzuzufügen, an denen du fangen kannst, wenn die neue [Entwurf Spezial](Draft_Snap_Special/de.md) Fang Schaltfläche aktiviert ist. Derzeit ist diese Eigenschaft allerdings nur für Python verfügbar. Im obigen Fall habe ich einen neuen Fangpunkt am Ausgang der WC Anlage hinzugefügt. Die Vektoren innerhalb der FangPunkte erscheinen auf dem Modell als weiße Punkte:


</div>

FreeCAD.ActiveDocument.Equipment.SnapPoints=[FreeCAD.Vector(0,0,100)]

![](images/Arch_pipe_example_02.jpg )

-   Mit dem neuen [\"Fang Spezial\"](Draft_Snap_Special/de.md) Entwurfsfang kannst du nun diese benutzerdefinierten Punkte fangen:

![](images/Arch_pipe_example_03.jpg )

-   Jetzt können wir unsere Rohrleitungen mit Hilfe von Entwurfslinien, Entwurfsdrähten oder Skizzen zeichnen. Am besten ist es jedoch, wenn wir nur Entwurfslinien verwenden:

![](images/Arch_pipe_example_04.jpg )


<div class="mw-translate-fuzzy">

-   Dort ist jetzt ein neues [Entwurf Neigungs](Draft_Slope/de.md) Werkzeug , mit dem die Neigung von Entwurfslinien geändert werden kann, z.B. auf 5% (0,05). So können wir unseren Abfalllinien schnell eine korrekte Neigung geben. Nur die z Koordinaten werden durch dieses Werkzeug geändert, wir brauchen sie also nur wieder aneinander zu fangen, die obere Projektion bleibt unverändert.


</div>

![](images/Arch_pipe_example_05.jpg )

-   Jetzt müssen wir nur noch alle unsere Linien auswählen und die [Arch Rohr](Arch_Pipe/de.md) Schaltfläche drücken. Arch Rohr funktioniert mit jedem Teil-basierten Objekt, das einen und nur einen offenen Draht enthält.

![](images/Arch_pipe_example_06.jpg )

-   Wir können jetzt Verbindungen erstellen, indem wir 2 oder 3 deckungsgleiche Rohre auswählen und die [Rohr Verbinder](Arch_PipeConnector/de.md) Schaltfläche drücken. Wenn 3 Rohre ausgewählt werden, müssen zwei davon ausgerichtet sein, um ein T Element zu erzeugen:

![](images/Arch_pipe_example_07.jpg )

-   Die Änderung des Verbinderradius ändert nicht die Länge der zugrunde liegenden Basislinie, sondern nur das resultierende Rohr (durch Änderung ihrer VersatzAnfang oder VersatzEnde Eigenschaft). Du kannst also weiterhin dein Linienlayout nur mit geraden Linien zeichnen, ohne sich um Kurven und Radius kümmern zu müssen.

Es ist auch möglich, Arch Rohre ohne Grundlinie zu erstellen. In diesem Fall verwende die Eigenschaft \"Länge\", um die Länge zu definieren.

## Scripting


<div class="mw-translate-fuzzy">

## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).


</div>


<div class="mw-translate-fuzzy">

Das Rohr Werkzeug kann in [Makros](macros/de.md) und von der [Python](Python/de.md) Konsole aus mit der folgenden Funktion verwendet werden:


</div>


```python
Pipe = makePipe(baseobj=None, diameter=0, length=0, placement=None, name="Pipe")
```

-   Creates a `Pipe` object from the given `baseobj` and `diameter`.
    -   
        `baseobj`
        
        is a [Draft Line](Draft_Line.md) or [Draft Wire](Draft_Wire.md).

    -   If `baseobj` is omitted, a straight pipe can be created with just the `diameter` and the `length` in the Z direction.
-   If a `placement` is given, it is used.


```python
import Draft, Arch

p1 = FreeCAD.Vector(1000, 0, 0)
p2 = FreeCAD.Vector(2500, 200, 0)
p3 = FreeCAD.Vector(3100, 1000, 0)
p4 = FreeCAD.Vector(3500, 500, 0)
Line = Draft.makeWire([p1, p2, p3, p4])

Pipe = Arch.makePipe(Line, 200)
FreeCAD.ActiveDocument.recompute()

Pipe2 = Arch.makePipe(diameter=120, length=3000)
FreeCAD.ActiveDocument.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Pipe/de
