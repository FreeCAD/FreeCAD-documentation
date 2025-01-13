---
 GuiCommand:
   Name: Arch Pipe
   Name/de: Arch Rohr
   MenuLocation: 3D/BIM , Rohr
   Workbenches: BIM_Workbench/de
   Shortcut: **P** **I**
   Version: 0.17
   SeeAlso: 
---

# Arch Pipe/de



## Beschreibung

Das Werkzeug **Arch Rohr** ermöglicht Rohre von Grund auf oder aus ausgewählten Objekten zu erstellen. Die ausgewählten Objekte müssen Part-basiert sein (Draft, Skizze, usw\...) und dürfen nur genau einen offenen Linienzug enthalten.



## Anwendung

1.  Wahlweise eine lineare [Part](Part_Workbench/de.md)-Form wie eine [Draft Linie](Draft_Line/de.md), einen [Draft Linienzug](Draft_Wire/de.md) oder eine offene [Skizze](Sketcher_NewSketch/de.md).
2.  Es gibt mehrere Möglichkeiten, diesen Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Arch_Pipe.svg" width=16px> [Rohr](Arch_Pipe/de.md)** drücken.
    -   Das Tastaturkürzel **P** dann **I**.
    -   Den Menüeintrag **3D/BIM → Rohr** auswählen.



## Optionen

-   Rohre haben die gleichen Eigenschaften und verhalten sich wie alle anderen [Arch-Komponenten](Arch_Component/de.md)



## Eigenschaften



### Daten


{{TitleProperty|Component}}

-    **Base|Link**: The base wire of this pipe, if any.

For the other properties in the group see [Arch Component](Arch_Component#Properties.md).


{{TitleProperty|Pipe}}

-    {{PropertyData/de|Diameter|Length}}: Der Durchmesser dieses Rohres, wenn seine {{PropertyData/de|Profile Type}} {{Value|Circle}} ist.

-    {{PropertyData/de|Height|Length}}: Die Höhe dieses Rohres, wenn seine {{PropertyData/de|Profile Type}} {{Value|Rectangle}} ist.

-    {{PropertyData/de|Length|Length}}: Die Länge dieses Rohres, wenn es nicht auf einem Liniezug basiert.

-    {{PropertyData/de|Offset End|Length}}: Der Abstand zum Endpunkt des Rohres. Wird automatisch gesetzt, wenn ein [Arch Rohrverbinder](Arch_PipeConnector/de.md) an diesem Punkt hinzugefügt wird, um das Rohr an den Verbinder anzupassen. Siehe [Typischer Arbeitsablauf](#Typischer_Arbeitsablauf.md) weiter unten.

-    {{PropertyData/de|Offset Start|Length}}: Der Abstand zum Startpunkt des Rohres. Wie vorhergehend beschrieben.

-    {{PropertyData/de|Profile|Link}}: Das Basis-Profil dieses Rohres. Ist nichts vorgegeben, wird das Rohrprofil von der {{PropertyData/de|Profile Type}} abgeleitet.

-    {{PropertyData/de|Profile Type|Enumeration}}: Das Profil dieses Rohres. Wird nur dann verwendet, wenn die {{PropertyData/de|Profile}} leer ist. Die Optionen sind: {{Value|Circle}} (Kreis), {{Value|Square}} (Quadrat) oder {{Value|Rectangle}} (Rechteck).

-    {{PropertyData/de|Wall Thickness|Length}}: Die Wandstärke dieses Rohres.

-    {{PropertyData/de|Width|Length}}: Die Breite dieses Rohres, wenn seine {{PropertyData/de|Profile Type}} auf {{Value|Square}} oder {{Value|Rectangle}} gesetzt ist.



## Typischer Arbeitsablauf 

-   Beginne mit der Platzierung von Sanitär-/Hydraulikgeräten (unten ist eine importierte step datei). Du verwandelst diese Objekte in Arch Ausstattungen, indem du sie auswählst und die Schaltfläche [Arch Ausstattung](Arch_Equipment/de.md) drückst.

![](images/Arch_pipe_example_01.jpg )

-   Arch Ausstattungen haben jetzt eine neue Eigenschaft **SnapPoints** (Einrastpunkte), bei der es sich um eine Liste von 3D-Vektoren handelt. Dies ermöglicht benutzerdefinierte Einrastpunkte hinzuzufügen, an denen eingerastet werden kann, wenn die neue Schaltfläche [Draft EinrastenSpezial](Draft_Snap_Special/de.md) aktiviert ist. Derzeit ist diese Eigenschaft allerdings nur für Python verfügbar. Im obigen Fall habe ich einen neuen Fangpunkt am Ausgang der WC-Anlage hinzugefügt. Die Vektoren innerhalb der FangPunkte erscheinen auf dem Modell als weiße Punkte:

FreeCAD.ActiveDocument.Equipment.SnapPoints=[FreeCAD.Vector(0,0,100)]

![](images/Arch_pipe_example_02.jpg )

-   Mit der neuen Draft-Einrastfunktion [\"EinrastenSpezial\"](Draft_Snap_Special/de.md) kann nun auf diese benutzerdefinierten Punkte eingerastet werden:

![](images/Arch_pipe_example_03.jpg )

-   Jetzt können wir unsere Rohrleitungen mit Hilfe von Draft-Linien, Draft-Linienzüge oder Skizzen zeichnen. Am besten ist es jedoch, wenn wir nur Draft-Linien verwenden:

![](images/Arch_pipe_example_04.jpg )

-   Dort gibt es jetzt ein neues Werkzeug [Draft Neigung](Draft_Slope/de.md), mit dem die Neigung von Draft-Linien geändert werden kann, z.B. auf 5% (0,05). So können wir unseren Abflussrohren schnell eine korrekte Neigung geben. Nur die Z-Koordinaten werden durch dieses Werkzeug geändert, wir brauchen sie also nur wieder aneinander einzurasten, die Draufsicht bleibt unverändert.

![](images/Arch_pipe_example_05.jpg )

-   Jetzt müssen wir nur noch alle unsere Linien auswählen und die Schaltfläche [Arch Rohr](Arch_Pipe/de.md) drücken. Arch Rohr funktioniert mit jedem Part-basierten Objekt, das einen und nur einen offenen Linienzug enthält.

![](images/Arch_pipe_example_06.jpg )

-   Wir können jetzt Verbindungen erstellen, indem wir 2 oder 3 deckungsgleiche Rohre auswählen und die Schaltfläche [Rohrverbinder](Arch_PipeConnector/de.md) drücken. Wenn 3 Rohre ausgewählt werden, müssen zwei davon kollinear ausgerichtet sein, um ein T-Element zu erzeugen:

![](images/Arch_pipe_example_07.jpg )

-   Die Änderung des Verbinderradius ändert nicht die Länge der zugrunde liegenden Basislinie, sondern nur das resultierende Rohr (durch Änderung ihrer VersatzAnfang oder VersatzEnde Eigenschaft). Du kannst also weiterhin dein Linienlayout nur mit geraden Linien zeichnen, ohne sich um Kurven und Radius kümmern zu müssen.

Es ist auch möglich, Arch Rohre ohne Grundlinie zu erstellen. In diesem Fall verwende die Eigenschaft \"Länge\", um die Länge zu definieren.



## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Rohr kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit der folgenden Funktion verwendet werden:


```python
pipe = makePipe(baseobj=None, diameter=0, length=0, placement=None, name="Pipe")
```

-   Creates a `pipe` object from the given `baseobj` and `diameter`.
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
line = Draft.make_wire([p1, p2, p3, p4])

pipe = Arch.makePipe(line, 200)
FreeCAD.ActiveDocument.recompute()

pipe2 = Arch.makePipe(diameter=120, length=3000)
FreeCAD.ActiveDocument.recompute()
```





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch Pipe/de
