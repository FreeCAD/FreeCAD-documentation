---
 GuiCommand:
   Name: Reinforcement HelicalRebar
   Name/de: Reinforcement Wendelbewehrung
   MenuLocation: 3D/BIM , Bewehrungswerkzeuge , Wendelbewehrung
   Workbenches: Reinforcement_Workbench/de, BIM_Workbench/de
   Version: 0.17
   SeeAlso: 
---

# Reinforcement HelicalRebar/de



## Beschreibung

Das Werkzeug [Reinforcement Wendelbewehrung](Reinforcement_HelicalRebar.md) erlaubt dem Anwender, einen fortlaufenden spiralförmigen Bewehrungsstab in einem [Struktur](Arch_Structure/de.md)-Objekt zu erstellen.

Dieses Werkzeug ist Teil des Arbeitsbereichs [Reinforcement](Reinforcement_Workbench/de.md); dieser ist ein [externer Arbeitsbereich](External_workbenches/de.md), der mit dem <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon-Manager](Std_AddonMgr/de.md) installiert werden kann.

:   <img alt="" src=images/Arch_Rebar_Helical_example.png  style="width:80px;">



*Ein fortlaufender spiralförmiger Bewehrungsstab in einer [Struktur](Arch_Structure/de.md)*



## Anwendung

1.  Eine beliebige Fläche eines vorher erstellten **<img src="images/Arch_Structure.svg" width=16px> [Struktur](Arch_Structure/de.md)**-Objekts auswählen.

2.  Dann **<img src="images/Reinforcement_HelicalRebar.svg" width=16px> [Wendelbewehrung](Reinforcement_HelicalRebar/de.md)** aus den Armierungswerkzeugen auswählen.

3.  Ein [Aufgaben-Bereich](Task_panel/de.md) wird auf der linken Seite des Bildschirm angezeigt wie im folgenden Bild dargestellt.

4.  Die gewünschte Ausrichtung auswählen.

5.  Die Werte für \'Left Cover\' (linke Fläche), \'Right Cover\' (rechte), \'Top Cover\' (obere), \'Bottom Cover\' (untere), \'Front Cover\' (vordere), \'Anchor length\' (Ankerlänge), \'Bent Angle\' (Biegungswinkel), \'Bent Factor\', \'Rounding\' und \'Diameter\' (Durchmesser) des Bewehrungsstabes eingeben.

6.  Die Art der Verteilung auswählen, entweder `'Amount'` (Menge) oder `'Spacing'` (Abstand).

7.  Falls \'Spacing\' gewählt wurde, kann auch [benutzerdefinierter Abstand](Reinforcement_Custom_Spacing/de.md) gewählt werden.

8.  
    **Pick selected face**wird verwendet, um die Fläche für die Verteilung der Bewehrungsstäbe zu bestätigen oder zu ändern.

9.  Schaltfläche **OK** oder **Anwenden** drücken, um die Bewehrungsstäbe zu erstellen.

10. Schaltfläche **Abbrechen** drücken, um den Aufgaben-Bereich zu verlassen.

<img alt="" src=images/HelicalRebarDialog.png  style="width:250px;"> 
*Aufgaben-Bereich für das Werkzeug*



## Eigenschaften

-    {{PropertyData/de|Side Cover}}: Der Abstand zwischen dem Bewehrungsstab und der gekrümmten Fläche.

-    {{PropertyData/de|Top Cover}}: Der Abstand zwischen dem Bewehrungsstab und der oberen Fläche der Struktur.

-    {{PropertyData/de|Bottom Cover}}: Der Abstand zwischen dem Bewehrungsstab und der unteren Fläche der Struktur.

-    {{PropertyData/de|Pitch}}: Die Höhe einer vollständigen Helixumdrehung, gemessen parallel zu den Achsen der Helix.

-    {{PropertyData/de|Diameter}}: Durchmesser des Bewehrungsstabs.



## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md),[Reinforcement-API](Reinforcement_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Reinforcement Wendelbewehrung kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit folgender Funktion verwendet werden:


```python
Rebar = makeHelicalRebar(s_cover, b_cover, diameter, t_cover, pitch, structure=None, facename=None)
```

-   Erstellt ein `Rebar`-Objekt aus der gegebenen `structure`, die eine [Arch Struktur](Arch_Structure/de.md) ist, und `facename`, die eine Fläche dieser Struktur ist.
    -   Falls weder `structure` noch `facename` gegeben sind, wird die vom Benutzer gewählte Fläche als Eingabe genommen.

-    `s_cover`, `b_cover` und `t_cover` sind innere Abstände von den Bewehrungsstabelementen zu den Flächen der Struktur. Dies sind entsprechend die seitlichen, unteren und oberen Abstände.

-    `diameter`ist der Durchmesser der Verstärkungsstäbe innerhalb der Struktur.

-    `pitch`ist der Parameter, der festlegt, wie groß der Abstand der Windungen von einander ist.



### Beispiel


```python
import FreeCAD, Draft, Arch, HelicalRebar

Circle = Draft.makeCircle(radius=250)
Structure = Arch.makeStructure(Circle)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

Rebar = HelicalRebar.makeHelicalRebar(10, 50, 8, 50, 50, structure, "Face2")
```



### Bearbeiten der Bewehrung 

Die Eigenschaften des Bewehrungsstabes lassen sich mit der folgenden Funktion verändern


```python
editHelicalRebar(Rebar, s_cover, b_cover, diameter, t_cover, pitch, structure=None, facename=None)
```

-    `Rebar`ist ein vorher erzeugtes `HelicalRebar`-Objekt.

-   Die anderen Parameter sind die gleichen wie die für die `makeHelicalRebar()`-Funktion erforderlichen.

-    `structure`und `facename` können weggelassen werden, so dass die Bewehrung in der ursprünglichen Struktur bleibt.


```python
import HelicalRebar

HelicalRebar.editHelicalRebar(Rebar, 20, 100, 20, 20, 100)
```




{{BIM_Tools_navi}}



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [Reinforcement](Category_Reinforcement.md) > Reinforcement HelicalRebar/de
