# <img alt="Symbol des Arbeitsbereichs Assembly" src=images/Workbench_Assembly.svg  style="width:64px;"> Assembly Workbench/de






## Einleitung


{{Version/de|1.0}}

Der Arbeitsbereich <img alt="" src=images/Workbench_Assembly.svg  style="width:24px;"> [Assembly](Assembly_Workbench/de.md) ist FreeCADs neuer eingebauter Arbeitsbereich für das Erstellen von Baugruppen bzw. Zusammenbauten. Er verwendet den quelloffenen Gleichungslöser [OndselSolver](https://github.com/Ondsel-Development/OndselSolver).

<img alt="" src=images/Assembly_Workbench_Example.png  style="width:400px;">



## Werkzeuge



### Zusammenbau

-   <img alt="" src=images/Assembly_CreateAssembly.svg  style="width:32px;"> [Baugruppe erstellen](Assembly_CreateAssembly/de.md): Erstellt eine Hauptbaugruppe (Assembly-Objekt) im aktuellen Dokument oder eine Unterbaugruppe in einer schon vorhandenen aktiven Baugruppe.

-   <img alt="" src=images/Assembly_InsertLink.svg  style="width:32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Einfügen:

  - <img alt="" src=images/Assembly_InsertLink.svg  style="width:32px;"> [Komponente einfügen](Assembly_InsertLink/de.md): Fügt eine Komponente in die aktuelle Baugruppe ein.

-   -   <img alt="" src=images/Assembly_InsertNewPart.svg  style="width:32px;"> [Neues Part einfügen](Assembly_InsertNewPart/de.md): Fügt ein neues Part-Objekt ein.

-   <img alt="" src=images/Assembly_SolveAssembly.svg  style="width:32px;"> [Baugruppe lösen](Assembly_SolveAssembly/de.md): Berechnet die gerade aktive Baugruppe.

-   <img alt="" src=images/Assembly_CreateView.svg  style="width:32px;"> [Explosionsansicht erstellen](Assembly_CreateView/de.md): Erstellt einen Behälter für Explosionsansichten (Exploded_Views-Objekt) in der aktiven Baugruppe, der eine oder mehrere Explosionsansichten (Exploded_View-Objekte) enthält

-   <img alt="" src=images/Assembly_CreateSimulation.svg  style="width:32px;"> [Simulation erstellen](Assembly_CreateSimulation/de.md): Erstellt eine Bewegungssimulation der aktuellen Baugruppe. {{Version/de|1.1}}

-   <img alt="" src=images/Assembly_CreateBom.svg  style="width:32px;"> [Stückliste erstellen](Assembly_CreateBom/de.md): Leitet eine Stückliste (Bill_of_Materials-Objekt) aus einer ausgewählten Baugruppe oder aus dem Dokument ab.

-   <img alt="" src=images/Assembly_ExportASMT.svg  style="width:32px;"> [ASMT-Datei exportieren](Assembly_ExportASMT/de.md): Exportiert die gerade aktive Baugruppe als ASMT-Datei.



### Verbindungen

-   <img alt="" src=images/Assembly_ToggleGrounded.svg  style="width:32px;"> [Festsetzen umschalten](Assembly_ToggleGrounded/de.md): Setzt Position und Ausrichtung einer Form im Bezug zum Koordinatensystem der Baugruppe fest, zu der sie gehört.

-   <img alt="" src=images/Assembly_CreateJointFixed.svg  style="width:32px;"> [Starre Verbindung erstellen](Assembly_CreateJointFixed/de.md): Erstellt eine starre Verbindung zwischen zwei Bauteilen, die keine Verschiebung oder Drehung zulässt, kann aber auch zum Festlegen andersartiger Verbindungen eingesetzt werden.

-   <img alt="" src=images/Assembly_CreateJointRevolute.svg  style="width:32px;"> [Drehverbindung erstellen](Assembly_CreateJointRevolute/de.md): Erstellt eine Drehverbindung (auch Scharnier genannt) zwischen zwei ausgewählten Bauteilen, die eine Drehung um eine gemeinsame Achse ermöglicht.

-   <img alt="" src=images/Assembly_CreateJointCylindrical.svg  style="width:32px;"> [Zylindrische Verbindung erstellen](Assembly_CreateJointCylindrical/de.md): Erstellt eine zylindrische Führung zwischen zwei ausgewählten Bauteilen, die eine Drehung um eine gemeinsame Achse und eine Verschiebung entlang derselben Achse ermöglicht.

-   <img alt="" src=images/Assembly_CreateJointSlider.svg  style="width:32px;"> [Gleitverbindung erstellen](Assembly_CreateJointSlider/de.md): Erstellt eine prismatische Führung (auch Schubgelenk genannt) zwischen zwei ausgewählten Bauteilen, die eine geradlinige Verschiebung entlang einer gemeinsamen Achse ermöglicht, während sämtliche Drehungen verhindert werden.

-   <img alt="" src=images/Assembly_CreateJointBall.svg  style="width:32px;"> [Kugelverbindung erstellen](Assembly_CreateJointBall/de.md): Erstellt ein Kugelgelenk zwischen zwei ausgewählten Bauteilen an einem gemeinsamen Punkt, das eine ungehinderte Drehung um den Punkt herum ermöglicht, während beide Bauteile an diesem Punkt verbunden bleiben.

-   <img alt="" src=images/Assembly_CreateJointDistance.svg  style="width:32px;"> [Abstandsverbindung erstellen](Assembly_CreateJointDistance/de.md): Erstellt eine Verbindung, die den Abstand zwischen den ausgewählten Elementen zweier Bauteile konstant hält.

-   <img alt="" src=images/Assembly_CreateJointParallel.svg  style="width:32px;"> [Parallelführung erstellen](Assembly_CreateJointParallel/de.md): Erstellt eine Parallelführung zwischen zwei ausgewählten Bauteilen, wobei die Z-Achsen der ausgewählten Koordinatensysteme parallel ausgerichtet werden.

-   <img alt="" src=images/Assembly_CreateJointPerpendicular.svg  style="width:32px;"> [Rechtwinklige Führung erstellen](Assembly_CreateJointPerpendicular/de.md): Erstellt eine rechtwinklige Führung zwischen zwei ausgewählten Bauteilen, wobei die Z-Achsen der ausgewählten Koordinatensysteme rechtwinklig ausgerichtet werden.

-   <img alt="" src=images/Assembly_CreateJointAngle.svg  style="width:32px;"> [Winkelführung erstellen](Assembly_CreateJointAngle/de.md): Erstellt eine Wikelführung zwischen zwei ausgewählten Bauteilen, die den Winkel zwischen den Z-Achsen der ausgewählten Koordinatensysteme konstant hält

-   <img alt="" src=images/Assembly_CreateJointRackPinion.svg  style="width:32px;"> [Zahnstange-Ritzel-Verbindung erstellen](Assembly_CreateJointRackPinion/de.md): Erstellt eine Zahnstange-Ritzel-Verbindng, die die Verschiebung eines Bauteils einer prismatischen Verbindung und die Drehung eines Bauteils einer Drehverbindung koppelt.

-   <img alt="" src=images/Assembly_CreateJointScrew.svg  style="width:32px;"> [Schraubverbindung erstellen](Assembly_CreateJointScrew/de.md): Erstellt eine Spindelverbindung (wendelförmige Verbindung), die die Verschiebung eines Bauteils einer prismatischen Verbindung und die Drehung eines Bauteils einer Drehverbindung koppelt.

-   <img alt="" src=images/Assembly_CreateJointGears.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Zahnrad-/Riemenverbindung erstellen:

  - <img alt="" src=images/Assembly_CreateJointGears.svg  style="width:32px;"> [Zahnradverbindung erstellen](Assembly_CreateJointGears/de.md): Erstellt eine Zahnradverbindung, die die Drehungen zweier Bauteile aus unterschiedlichen Drehverbindungen koppelt.

  - <img alt="" src=images/Assembly_CreateJointBelt.svg  style="width:32px;"> [Riemenverbindung erstellen](Assembly_CreateJointBelt/de.md): Erstellt eine Riemenverbindung, die die Drehungen zweier Bauteile aus unterschiedlichen Drehverbindungen koppelt.



## Einstellungen

-   <img alt="" src=images/Preferences-assembly.svg  style="width:32px;"> [Einstellungen](Assembly_Preferences/de.md): Voreinstellungen für den Arbeitsbereich Assembly



## Beispiel Kurbel und Schieber 


<div class="mw-collapsible mw-collapsed toccolours">

<img alt="" src=images/Assembly3_KinematicExample-01.png  style="width:80px;"> Dies ist ein temporäres Beispiel und kann entfernt werden, sobald ausführliche Beschreibungen bzw. Anleitungen zur Verfügung stehen.


<div class="mw-collapsible-content">



### Baugruppe Kurbel und Schieber 

Der Zusammenbau (Baugruppe), der erstellt wird, besteht aus vier Bauteilen: Eine Basis, ein Schieber, eine Kurbel und ein Pleuel (Verbindungsstange). Sie sind mit vier Gelenken verbunden.

<img alt="" src=images/Assembly3_KinematicExample-01.png  style="width:300px;">



*Die zusammengebauten Bauteile: Basis (bernsteinfarben), Schieber (hellblau), Kurbel (rot), Pleuel (grün)*



### Bauteile vorbereiten 

In diesem Beispiel werden alle Bauteile und der Zusammenbau in einem Dokument erstellt.

Die zylindrischen Geometrien der Objekte sind entweder parallel oder rechtwinklig, der Rest ist für dieses Beispiel nicht von Bedeutung, solange es keine Kollision verursacht. Mit dieser Info im Hinterkopf modelliert man seine eigenen Objekte oder erstellt ähnliche mit dem nachfolgenden Python-Code. Der Code erstellt ein neues Dokument mit den vier Objekten (simpler als in den Abbildungen). Einfach die folgenden Zeilen kopieren und in die [Python-Konsole](Python_console/de.md) einfügen:


```python
import FreeCAD as App
import FreeCADGui as Gui
import Part

doc = App.newDocument()

box1 = Part.makeBox(140, 40, 7, App.Vector(0, -20, 0))
cyl1 = Part.makeCylinder(4, 8, App.Vector(120, 0, 7))
box2 = Part.makeBox(20, 12, 10, App.Vector(5, -6, 7))
cyl2 = Part.makeCylinder(6, 20, App.Vector(25, 0, 17), App.Vector(-1, 0, 0))
cyl3 = Part.makeCylinder(4, 20, App.Vector(25, 0, 17), App.Vector(-1, 0, 0))
shape = box1.fuse([cyl1, box2, cyl2]).removeSplitter().cut(cyl3)
base = doc.addObject("Part::Feature", "Base")
base.Shape = shape

box1 = Part.makeBox(4, 12, 12, App.Vector(-12, -6, 0))
box2 = Part.makeBox(14, 12, 4, App.Vector(-8, -6, 0))
cyl1 = Part.makeCylinder(4, 8, App.Vector(0, 0, 4))
cyl2 = Part.makeCylinder(4, 88, App.Vector(-12, 0, 6),App.Vector(-1, 0, 0))
shape = box1.fuse([box2, cyl1, cyl2]).removeSplitter()
slider_rod = doc.addObject("Part::Feature", "SliderRod")
slider_rod.Shape = shape
slider_rod.Placement.Base = App.Vector(100, -40, 0)

cyl1 = Part.makeCylinder(7.5, 4)
box1 = Part.makeBox(15, 30, 4, App.Vector(-7.5, 0, 0))
cyl2 = Part.makeCylinder(7.5, 4, App.Vector(0, 30, 0))
cyl3 = Part.makeCylinder(4, 6, App.Vector(0, 30, 4))
cyl4 = Part.makeCylinder(4, 4)
shape = cyl1.fuse([box1, cyl2]).removeSplitter().fuse(cyl3).cut(cyl4)
crank = doc.addObject("Part::Feature", "Crank")
crank.Shape = shape
crank.Placement.Base = App.Vector(125, -70, 0)

cyl1 = Part.makeCylinder(6, 4)
box1 = Part.makeBox(50, 12, 4, App.Vector(0, -6, 0))
cyl2 = Part.makeCylinder(6, 4, App.Vector(50, 0, 0))
cyl3 = Part.makeCylinder(4, 4)
cyl4 = Part.makeCylinder(4, 4, App.Vector(50, 0, 0))
shape = cyl1.fuse([box1, cyl2]).removeSplitter().cut(cyl3.fuse(cyl4))
connecting_rod = doc.addObject("Part::Feature", "ConnectingRod")
connecting_rod.Shape = shape
connecting_rod.Placement.Base = App.Vector(25, -70, 0)

mat = base.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.80, 0.60, 0.15, 0.0)
base.ViewObject.ShapeAppearance = (mat,)

mat = slider_rod.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.55, 0.70, 0.70, 0.0)
slider_rod.ViewObject.ShapeAppearance = (mat,)

mat = crank.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.70, 0.30, 0.20, 0.0)
crank.ViewObject.ShapeAppearance = (mat,)

mat = connecting_rod.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.55, 0.70, 0.0, 0.0)
connecting_rod.ViewObject.ShapeAppearance = (mat,)

doc.recompute()
view = Gui.ActiveDocument.ActiveView
view.viewIsometric()
view.fitAll()
```



### Eine Baugruppe hinzufügen 

Der Befehl <img alt="" src=images/Assembly_CreateAssembly.svg  style="width:24px;"> [Baugruppe erstellen](Assembly_CreateAssembly/de.md) fügt dem Dokument eine Baugruppe hinzu.

<img alt="" src=images/Assembly_KinematicExample-01.png  style="width:200px;">



*Baumansicht von Bauteilen (Parts) und Baugruppe (Assembly)*



### Die Bauteile in die Baugruppe verschieben 

Die Bauteile in der [Baumansicht](Tree_view/de.md) auf das Baugruppenobjekt (Assembly object) ziehen und ablegen. Sie können jetzt vom Assembly-Gleichungslöser verarbeitet werden.

<img alt="" src=images/Assembly_KinematicExample-02.png  style="width:200px;">



*Die Bauteile sind jetzt im Assembly-Behälter*



### Ein Bauteil festsetzen 

Um eine Baugruppe an der gewünschten Stelle zu behalten, sollte das Bauteil Basis verankert werden, oder festgesetzt, wie es hier genannt wird. Ein Bauteil in der [Baumansicht](Tree_view/de.md) oder in der [3D-Ansicht](3D_view/de.md) auswählen und den Befehl <img alt="" src=images/Assembly_ToggleGrounded.svg  style="width:24px;"> [Festsetzen umschalten](Assembly_ToggleGrounded/de.md) aufrufen. Dies legt die Position der Basis im Bezug auf das lokale Koordinatensystem (LKS) des Assembly-Behälters fest. Ein GroundedJoint-Objekt wird dem Joints-Behälter hinzugefügt.

<img alt="" src=images/Assembly_KinematicExample-03.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_KinematicExample-04.png  style="width:240px;">



*Den Joints-Behälter erweitern, um das GroundedJoint-Objekt zu finden*



### Alternative: Komponente einfügen 

Anstelle der zwei oben genannten Schritte ist es auch möglich den Befehl <img alt="" src=images/Assembly_InsertLink.svg  style="width:24px;"> [Komponente einfügen](Assembly_InsertLink/de.md) zu verwenden, um Objekte in einen Zusammenbau einzufügen. Das erste Objekt wird automatisch festgesetzt, daher muss man (die Auswahl) mit der Basis beginnen. Der Befehl erstellt Komponenten (Verknüpfungen) und die originale Objekte bleiben außerhalb des Zusammenbaus. Um Verwechslungen zu vermeiden, ist es ratsam, sie auszublenden.



### Verbindungen hinzufügen 

Eine Verbindung (ein Gelenk) verbindet genau zwei Elemente unterschiedlicher Bauteile. Sie können wahlweise ausgewählt werden, bevor der Befehl für die gewünschte Verbindung aufgerufen wird (jede Anzahl ausgewählter Elemente außer zwei ergibt eine leere Auswahl). Die Elemente legen die Position und Ausrichtung eines LKS fest, das durch einen gefüllten Kreis auf der lokalen XY-Ebene und drei Linien entlang der lokalen X- (rot), Y- (grün) und Z-Achse (blau) dargestellt wird.

-   Ein Drehgelenk (Scharnier) zwischen Basis und Kurbel

<img alt="" src=images/Assembly_KinematicExample-05.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_KinematicExample-06.png  style="width:200px;">



*Ausgewählte Elemente + <img src="images/Assembly_CreateJointRevolute.svg" width=24px> [Drehverbindung erstellen](Assembly_CreateJointRevolute/de.md) → neu angeordnete Kurbel*

Die **Kurbel** mit der linken Maustaste bewegen. Es sollte jetzt nur eine Drehung um die Drehachse (Z-Achse) möglich sein.

-   Eine prismatische Führung zwischen Basis und Schieber

<img alt="" src=images/Assembly_KinematicExample-07.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_KinematicExample-08.png  style="width:200px;">



*Ausgewählte Elemente +<img src="images/Assembly_CreateJointSlider.svg" width=24px> [Prismatische Verbindung erstellen](Assembly_CreateJointSlider/de.md) → neu angeordneter Schieber*

Den **Schieber** mit der linken Maustaste bewegen. Es sollte jetzt nur das Verschieben entlang seiner Mittellinie (Z-Achse) möglich sein.

-   Ein Drehgelenk (Scharnier) zwischen Kurbel und Pleuel

<img alt="" src=images/Assembly_KinematicExample-09.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_KinematicExample-10.png  style="width:200px;">



*Ausgewählte Elemente + <img src="images/Assembly_CreateJointRevolute.svg" width=24px> [Drehverbindung erstellen](Assembly_CreateJointRevolute/de.md) → neu angeordnetes Pleuel*

Den **Pleuel** mit der linken Maustaste bewegen. Er sollte jetzt nur eine Drehung um die Drehachse (Z-Achse) möglich sein.

<img alt="" src=images/Assembly_KinematicExample-11.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_KinematicExample-12.png  style="width:200px;">



*Wenn sich mehrere Gelenke in einer Reihe ergeben, müssen wir dem Gleichungslöser helfen eine sinnvolle Lösung zu finden.<br>
Wenn erforderlich, die Bauteile anklicken und auf eine einfacher zu berechnende Position ziehen.*

-   Eine zylindrische Führung zwischen Pleuel und Schieber

<img alt="" src=images/Assembly_KinematicExample-13.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_KinematicExample-14.png  style="width:200px;">



*Ausgewählte Elemente +<img src="images/Assembly_CreateJointCylindrical.svg" width=24px> [Zylindrische Verbindung erstellen](Assembly_CreateJointCylindrical/de.md) → fertiger Zusammenbau*

Im fertiggestellten Zusammenbau können die Bauteile entsprechend den verwendeten Verbindungen mit dem Mauszeiger bewegt werden.



#### Hinweis

Die Ausrichtung des Zapfens des Schiebers ist redundant festgelegt. Seine Mittellinie ist parallel zum Zapfen der Basis über die kinematisch Kette von der Basis über die Kurbel und dem Pleuel, d.h. dass seine lokale Z-Achse sich um keine der X- oder Y-Achsen drehen kann. Die prismatische Verbindung verhindert ebenfalls seine Drehung um zwei lokale Achsen, woraus sich zwei überbestimmte (doppelt festgelegte) Freiheitsgrade ergeben. Eine zylindrische Verbindung anstelle der prismatischen Verbindung würde nur eine Drehung sperren und ergibt so nur einen einzigen überbestimmten Freiheitsgrad.



### Die Kurbel antreiben 

Um die Lage aller Bauteile der Baugruppe zueinander durch den Winkel zwischen der Basis und der Kurbel zu steuern, muss deren Drehgelenk in eine starre Verbindung umgewandelt werden. Dafür klickt man das Revolute-Objekt in der Baumansicht doppelt an. Im Dialog ändert man Rehverbindung zu Starrer Verbund und passt den Wert des Drehwinkels nach Wunsch an (die Bewegung sollte der Drehung des Mausrades folgen).

Man beachte, dass das Ändern der Verbindungsart die Benennung (Label) der Verbindung ändert, aber nicht ihren Namen. In diesem Falle wird die Benennung zu \"Fixed\" (Starrer Verbund) geändert.

Um die Kinematik zu bewegen können wir den Drehwinkel (Offset1.Angle) der starren Verbindung mit Python-Code verändern. Einfach die folgenden Zeilen kopieren und in die Python-Konsole einfügen:


```python
import math
import FreeCAD as App
import FreeCADGui as Gui

actuator = App.ActiveDocument.getObjectsByLabel("Fixed")[0]

for angle in range(0, 361, 10):
    # A full rotation of the Crank in steps of 10°
    actuator.Offset1.Rotation.Angle = math.radians(angle)
    App.ActiveDocument.recompute()
    Gui.updateGui()
```

Der Endwert des Bereiches muss größer als 360° sein, damit auch dieser Winkel noch als gültiges Ergebnis anerkannt wird.


</div>


</div>



## Beispiel Kreuzgelenk 


<div class="mw-collapsible mw-collapsed toccolours">

<img alt="" src=images/Assembly_UniversalJointExample-01.png  style="width:80px;"> Dies ist ein temporäres Beispiel und kann entfernt werden, sobald ausführliche Beschreibungen bzw. Anleitungen zur Verfügung stehen.


<div class="mw-collapsible-content">



### Baugruppe Kreuzgelenk 

<img alt="" src=images/Assembly_UniversalJointExample-01.png  style="width:300px;">

In diesem Beispiel wird ein [Kreuzgelenk](https://de.wikipedia.org/wiki/Kreuzgelenk) erstellt.

Der Zusammenbau besteht aus drei Festkörpern: zwei identischen (Gelenk-) Gabeln (Forks) und einem (Achsen-) Kreuz (Cross). Zwei zusätzliche Elemente, Welle1 und Welle2 (Axle1 und Axle2), die keine Festkörper sind und die abgewinkelten Wellen darstellen, werden auch noch gebraucht. Die Wellen und Festkörperbauteile werden mit mehreren Gelenken verbunden.



### Bauteile vorbereiten 

In diesem Beispiel werden alle Bauteile und der Zusammenbau in einem Dokument erstellt.

Der nachfolgende Python-Code erstellt ein neues Dokument mit vier Objekten (nur eine Gabel). Einfach die folgenden Zeilen kopieren und in die [Python-Konsole](Python_console/de.md) einfügen:


```python
import math
import FreeCAD as App
import FreeCADGui as Gui
import Part

doc = App.newDocument()

axle1 = doc.addObject("Part::Line", "Axle1")
axle1.X2 = -80
axle1.Y2 = 0
axle1.Z2 = 0

axle2 = doc.addObject("Part::Line", "Axle2")
axle2.X2 = 80
axle2.Y2 = 0
axle2.Z2 = 0
axle2.Placement.Rotation.Angle = math.radians(20)

sph1 = Part.makeSphere(50, App.Vector(0, 0, 0), App.Vector(-1, 0, 0), 0, 90, 360)
box1 = Part.makeBox(50, 40, 80, App.Vector(-50, -20, -40))
cyl1 = Part.makeCylinder(20, 80, App.Vector(0, 0, -40))
cyl2 = Part.makeCylinder(20, 80, App.Vector(0, 0, 0), App.Vector(-1, 0, 0))
cyl3 = Part.makeCylinder(30, 60, App.Vector(0, -30, 0), App.Vector(0, 1, 0))
box2 = Part.makeBox(30, 60, 60, App.Vector(0, -30, -30))
cyl4 = Part.makeCylinder(15, 80, App.Vector(0, 0, -40))
cyl5 = Part.makeCylinder(15, 80, App.Vector(0, 0, 0), App.Vector(-1, 0, 0))
shape = sph1.common(box1).fuse([cyl1, cyl2]).cut(cyl3.fuse([box2, cyl4, cyl5]))
fork = doc.addObject("Part::Feature", "Fork")
fork.Shape = shape.removeSplitter()
fork.Placement.Base = App.Vector(0, 100, 0)

cyl1 = Part.makeCylinder(15, 80, App.Vector(0, 0, -40))
cyl2 = Part.makeCylinder(15, 80, App.Vector(0, -40, 0), App.Vector(0, 1, 0))
shape = cyl1.fuse([cyl2])
cross = doc.addObject("Part::Feature", "Cross")
cross.Shape = shape.removeSplitter()
cross.Placement.Base = App.Vector(70, 100, 0)

mat = fork.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.80, 0.60, 0.15, 0.0)
fork.ViewObject.ShapeAppearance = (mat,)

mat = cross.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.55, 0.70, 0.70, 0.0)
cross.ViewObject.ShapeAppearance = (mat,)

doc.recompute()
view = Gui.ActiveDocument.ActiveView
view.viewIsometric()
view.fitAll()
```



### Den Winkel der Wellen ändern 

Der Winkel zwischen den Wellen wird auf 20° festgelegt. Soll der Winkel geändert werden, wird Welle2 (Axle2) ausgewählt und deren Eigenschaft Placement.Angle angepasst. Diese Eigenschaft muss geändert werden, bevor Welle2 in die Baugruppe bewegt wird.

Warnung: Die Bauteile können kollidieren, wenn der Winkel zu groß ist.



### Eine Baugruppe hinzufügen 

Der Befehl <img alt="" src=images/Assembly_CreateAssembly.svg  style="width:24px;"> [Baugruppe erstellen](Assembly_CreateAssembly/de.md) fügt dem Dokument eine Baugruppe hinzu.



### Die Wellen in die Baugruppe verschieben 

In der [Baumansicht](Tree_view/de.md) die Wellen auf die Baugruppe (Assembly-Objekt) zeihen und ablegen.



### Die Wellen festlegen 

Beide Wellen in der Baumansicht auswählen und das Werkzeug <img alt="" src=images/Assembly_ToggleGrounded.svg  style="width:24px;"> [Festlegen umschalten](Assembly_ToggleGrounded/de.md) aufrufen.



### Die Festkörper in die Baugruppe verschieben 

Für die anderen vier Objekte verwenden wir das Werkzeug <img alt="" src=images/Assembly_InsertLink.svg  style="width:24px;"> [Komponente einfügen](Assembly_InsertLink/de.md):

1.  Das Werkzeug aufrufen.
2.  Im Dialogfenster, das sich öffnet, klickt man einmal auf das Kreuz-Objekt und zweimal auf das Gabel-Objekt.
3.  Die Schaltfläche **OK** drücken.
4.  Die Objekte außerhalb der Baugruppe ausblenden.
5.  Sollten sich die Objekte innerhalb der Baugruppe zu sehr überlappen, können sie auf eine neue Position gezogen werden.



### Verbindungen hinzufügen 

-   Ein Drehgelenk (Scharnier) zwischen Axle1 (Welle1) und Fork001 (Gabel1)

<img alt="" src=images/Assembly_UniversalJointExample-02.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_UniversalJointExample-03.png  style="width:200px;">



*Ausgewählte Elemente + <img src="images/Assembly_CreateJointRevolute.svg" width=24px> [Drehverbindung erstellen](Assembly_CreateJointRevolute/de.md) + Versatz von +40 mm oder -40 mm → neu angeordnete Gabel1*

Wird das Werkzeug zuerst aufgerufen, kann man in die Nähe des korrekten Endpunktes der Welle1 klicken, um die Eingabe eines Versatzes zu vermeiden.

-   Eine Zylindrische Führung zwischen Gabel1 (Fork001) und Kreuz (Cross001)

<img alt="" src=images/Assembly_UniversalJointExample-04.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_UniversalJointExample-05.png  style="width:200px;">



*Ausgewählte Elemente +<img src="images/Assembly_CreateJointCylindrical.svg" width=16px> [Zylindrische Verbindung erstellen](Assembly_CreateJointCylindrical/de.md) → neu angeordnetes Kreuz*

-   Eine zylindrische Führung zwischen Welle2 (Axle2) und Gabel2 (Fork002)

<img alt="" src=images/Assembly_UniversalJointExample-06.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_UniversalJointExample-07.png  style="width:200px;">



*Ausgewählte Elemente +<img src="images/Assembly_CreateJointCylindrical.svg" width=16px> [Zylindrische Verbindung erstellen](Assembly_CreateJointCylindrical/de.md) → neu angeordnete Gabel2*

Wenn nötig, die Ausrichtung der Verbindung umkehren, indem man die Schaltfläche **<img src="images/Button_sort.svg" width=16px>** im Aufgaben-Fenster drückt.

-   Eine zylindrische Führung zwischen Kreuz (Cross001) und Gabel2 (Fork002)

<img alt="" src=images/Assembly_UniversalJointExample-08.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_UniversalJointExample-09.png  style="width:200px;">



*Ausgewählte Elemente +<img src="images/Assembly_CreateJointCylindrical.svg" width=16px> [Zylindrische Verbindung erstellen](Assembly_CreateJointCylindrical/de.md) → Kreuz (Cross001) und Gabel2 (Fork002) neu angeordnet*



### Das Kreuzgelenk antreiben 

Das Kreuzgelenk kann angetrieben werden, indem Gabel1 mit der linken Maustaste bewegt wird.

Soll die Anordnung an bestimmten Drehwinkeln geprüft werden, macht man folgendes:

1.  Die zylindrische Verbindung zwischen Welle1 und Gabel1 in eine starre Verbindung ändern.
2.  Die Eigenschaft Offset1.Angle der starren Verbindung auswählen und das Mausrad bewegen.
3.  Das Kreuzgelenk kann auf einen beliebigen Winkel eingestellt werden.


</div>


</div>



## Beispiel Schraubstock 


<div class="mw-collapsible mw-collapsed toccolours">

<img alt="" src=images/Assembly_ViseExample-01.png  style="width:80px;"> Dies ist ein temporäres Beispiel und kann entfernt werden, sobald ausführliche Beschreibungen bzw. Anleitungen zur Verfügung stehen.


<div class="mw-collapsible-content">



### Baugruppe Schraubstock 

<img alt="" src=images/Assembly_ViseExample-01.png  style="width:300px;">

In diesem Beispiel wird ein [Schraubstock](https://de.wikipedia.org/wiki/Schraubstock) erzeugt.

Der Zusammenbau besteht aus drei Festkörpern: einer feststehenden und einer beweglichen Klemmbacke und einer Verstellschraube mit einem Hebel. Ein zusätzliches Element, eine Kurbel, die kein Festkörper ist wird auch noch gebraucht. Die Kurbel und die Festkörperbauteile werden mit mehreren Gelenken verbunden.

Eine Schraubenverbindung koppelt die Verschiebung eines Bauteiles mit einer Gleitverbindung mit der Drehbewegung eines Bauteiles mit einer Drehverbindung. Die Schraube soll beides eine Verschiebung und eine Drehbewegung machen, deshalb muss sie ein Bauteil mit einer zylindrischen Verbindung sein. In dieser Baugruppe wird die Schraube mit einer Abstandsverbindung an die bewegliche Klemmbacke, an die Kurbel die kein Festkörper ist mit einer Parallelführung, und an die feststehende Klemmbacke mit einer zylindrischen Verbindung, angeheftet.



### Bauteile vorbereiten 

In diesem Beispiel werden alle Bauteile und der Zusammenbau in einem Dokument erstellt.

Der nachfolgende Python-Code erstellt ein neues Dokument mit vier Objekten. Einfach die folgenden Zeilen kopieren und in die [Python-Konsole](Python_console/de.md) einfügen:


```python
import math
import FreeCAD as App
import FreeCADGui as Gui
import Part

doc = App.newDocument()

box1 = Part.makeBox(95, 40, 75, App.Vector(0, -20, -22))
cyl1 = Part.makeCylinder(35, 80, App.Vector(0, -40, 53), App.Vector(0, 1, 0), 90)
box2 = Part.makeBox(20, 80, 30, App.Vector(-20, -40, 58))
cyl2 = Part.makeCylinder(15, 80, App.Vector(-15, -40, 58), App.Vector(0, 1, 0), 90)
box3 = Part.makeBox(5, 80, 15, App.Vector(-20, -40, 58))
box4 = Part.makeBox(35, 24, 24, App.Vector(0, -12, -12))
box5 = Part.makeBox(60, 34, 69, App.Vector(35, -17, -19))
cyl3 = Part.makeCylinder(20, 55, App.Vector(-20, -40, 53), App.Vector(1, 0, 0))
cyl4 = Part.makeCylinder(20, 55, App.Vector(-20, 40, 53), App.Vector(1, 0, 0))
cyl5 = Part.makeCylinder(5, 35, App.Vector(0, 0, 38), App.Vector(1, 0, 0))
box6 = Part.makeBox(7, 88, 15, App.Vector(-22, -44, 75))
box7 = Part.makeBox(95, 90, 10, App.Vector(0, -45, -32))
shape = box1.fuse([cyl1, box2, box6, box7]).cut(cyl2.fuse([box3, cyl3, cyl4, cyl5, box4, box5]))
fixedJaw = doc.addObject("Part::Feature", "FixedJaw")
fixedJaw.Shape = shape.removeSplitter()
fixedJaw.Placement.Rotation.Axis = App.Vector(0, 0, 1)
fixedJaw.Placement.Rotation.Angle = math.radians(180)

box1 = Part.makeBox(35, 40, 75, App.Vector(0, -20, -22))
cyl1 = Part.makeCylinder(35, 80, App.Vector(0, -40, 53), App.Vector(0, 1, 0), 90)
box2 = Part.makeBox(20, 80, 30, App.Vector(-20, -40, 58))
cyl2 = Part.makeCylinder(15, 80, App.Vector(-15, -40, 58), App.Vector(0, 1, 0), 90)
box3 = Part.makeBox(160, 24, 24, App.Vector(-160, -12, -12))
box4 = Part.makeBox(5, 80, 15, App.Vector(-20, -40, 58))
box5 = Part.makeBox(160, 18, 18, App.Vector(-160, -9, -9))
cyl3 = Part.makeCylinder(20, 55, App.Vector(-20, -40, 53), App.Vector(1, 0, 0))
cyl4 = Part.makeCylinder(20, 55, App.Vector(-20, 40, 53), App.Vector(1, 0, 0))
cyl5 = Part.makeCylinder(5, 35, App.Vector(0, 0, 38), App.Vector(1, 0, 0))
box6 = Part.makeBox(7, 88, 15, App.Vector(-22, -44, 75))
shape = box1.fuse([cyl1, box2, box3, box6]).cut(cyl2.fuse([box4, cyl3, cyl4, box5, cyl5]))
movableJaw = doc.addObject("Part::Feature", "MovableJaw")
movableJaw.Shape = shape.removeSplitter()
movableJaw.Placement.Base = App.Vector(150, 100, 0)

cyl1 = Part.makeCylinder(5, 190, App.Vector(0, 0, 0), App.Vector(1, 0, 0))
cyl2 = Part.makeCylinder(10, 20, App.Vector(190, 0, 0), App.Vector(1, 0, 0))
cyl3 = Part.makeCylinder(4, 100, App.Vector(200, 0, -50), App.Vector(0, 0, 1))
shape = cyl1.fuse([cyl2, cyl3])
leverScrew = doc.addObject("Part::Feature", "LeverScrew")
leverScrew.Shape = shape.removeSplitter()
leverScrew.Placement.Base = App.Vector(150, -100, 0)

wire1 = Part.makePolygon([App.Vector(0, 0, 100), App.Vector(0, 0, 0), App.Vector(100, 0, 0)])
crank = doc.addObject("Part::Feature", "Crank")
crank.Shape = wire1
crank.Placement.Base = App.Vector(0, -100, 0)

mat = fixedJaw.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.80, 0.60, 0.15, 0.0)
fixedJaw.ViewObject.ShapeAppearance = (mat,)

mat = movableJaw.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.55, 0.70, 0.70, 0.0)
movableJaw.ViewObject.ShapeAppearance = (mat,)

mat = leverScrew.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.70, 0.30, 0.20, 0.0)
leverScrew.ViewObject.ShapeAppearance = (mat,)

doc.recompute()
view = Gui.ActiveDocument.ActiveView
view.viewIsometric()
view.fitAll()
```



### Eine Baugruppe hinzufügen 

Der Befehl <img alt="" src=images/Assembly_CreateAssembly.svg  style="width:24px;"> [Baugruppe erstellen](Assembly_CreateAssembly/de.md) fügt dem Dokument eine Baugruppe hinzu



### Die Bauteile in die Baugruppe verschieben 

In der [Baumansicht](Tree_view/de.md) die Bauteile in die Baugruppe ziehen und ablegen. Sie können jetzt vom Baugruppen-Gleichungslöser (Assembly solver) verarbeitet werden.



### Ein Bauteil festsetzen 

Um die Baugruppe an der gewünschten Position festzusetzen, sollte die feststehende Klemmbacke festgesetzt (grounded) werden. Die feststehende Klemmbacke in der [Baumansicht](Tree_view/de.md) oder in der [3D-Ansicht](3D_view/de.md) auswählen und den Befehl <img alt="" src=images/Assembly_ToggleGrounded.svg  style="width:24px;"> [Festsetzen umschalten](Assembly_ToggleGrounded/de.md) aufrufen. Ein GroundedJoint-Objekt wird dem Joints-Behälter hinzugefügt.



### Verbindungen hinzufügen 

-   Eine Drehverbindung zwischen feststehender Klemmbacke und Kurbel

<img alt="" src=images/Assembly_ViseExample-02.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ViseExample-03.png  style="width:200px;">



*Ausgewählte Elemente + <img src="images/Assembly_CreateJointRevolute.svg" width=24px> [Drehverbindung](Assembly_CreateJointRevolute/de.md) → neu angeordnete Kurbel*

-   Eine Gleitverbindung zwischen feststehender und beweglicher Klemmbacke

<img alt="" src=images/Assembly_ViseExample-04.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ViseExample-05.png  style="width:200px;">



*Ausgewählte Elemente + <img src="images/Assembly_CreateJointSlider.svg" width=24px> [Gleitverbindung](Assembly_CreateJointSlider/de.md) → neu angeordnete bewegliche Klemmbacke*

Den kleinsten Abstand (Min length) auf -77 mm und den größten Abstand (Max length) auf -7 mm einstellen. Dies beschränkt die Öffnung des Schraubstockes auf 70 mm.

Die nächsten drei Verbindungen sind notwendig, um die Hebel-Schraube zu folgendem zu zwingen: verschiebe gleich wie die bewegte Klemmbacke, drehe gleich wie die Kurbel, rotiere um die Hauptachse.

-   Eine Abstandsverbindung zwischen der Hebel-Schraube und der beweglichen Klemmbacke

<img alt="" src=images/Assembly_ViseExample-06.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ViseExample-07.png  style="width:200px;">



*Ausgewählte Elemente + <img src="images/Assembly_CreateJointDistance.svg" width=24px> [Abstandsverbindung](Assembly_CreateJointDistance/de.md) → neu angeordnete Hebel-Schraube*

Zwei Flächen auswählen. Den Wert des Abstandes auf 20 mm setzen.

-   Eine Parallelführung zwischen der Hebel-Schraube und der Kurbel

<img alt="" src=images/Assembly_ViseExample-08.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ViseExample-09.png  style="width:200px;">



*Ausgewählte Elemente + <img src="images/Assembly_CreateJointParallel.svg" width=24px> [Parallelführung](Assembly_CreateJointParallel/de.md) → neu angeordnete Hebel-Schraube*

-   Eine zylindrische Führung zwischen der Hebel-Schraube und der feststehenden Klemmbacke

<img alt="" src=images/Assembly_ViseExample-10.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ViseExample-11.png  style="width:200px;">



*Ausgewählte Elemente + <img src="images/Assembly_CreateJointCylindrical.svg" width=24px> [Zylindrische Führung](Assembly_CreateJointCylindrical/de.md) → neu angeordnete Hebel-Schraube*

-   Eine Schraubverbindung zwischen der beweglichen Klemmbacke und der Kurbel

<img alt="" src=images/Assembly_ViseExample-12.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ViseExample-13.png  style="width:200px;">



*Ausgewählte Elemente (Hebel-Schraube unsichtbar) + <img src="images/Assembly_CreateJointScrew.svg" width=24px> [Schraubverbindung](Assembly_CreateJointScrew/de.md) → fertiger Mechanismus (Hebel-Schraube sichtbar)*

Falls notwendig, während des Auswahlvorganges die Hebel-Schraube ausblenden.

Der Steigung der Schraube auf 5 mm einstellen.



### Den Schraubstock antreiben 

Der Schraubstock kann angetrieben werden, indem die Kurbel oder die bewegliche Klemmbacke mit der linken Maustaste bewegt wird.


</div>


</div>



## Beispiel Stoßdämpfer 


<div class="mw-collapsible mw-collapsed toccolours">

<img alt="" src=images/Assembly_ShockAbsorberExample-01.png  style="width:80px;"> Dies ist ein temporäres Beispiel und kann entfernt werden, sobald ausführliche Beschreibungen bzw. Anleitungen zur Verfügung stehen.


<div class="mw-collapsible-content">



### Baugruppe Stoßdämpfer 

<img alt="" src=images/Assembly_ShockAbsorberExample.gif  style="width:300px;">

In diesem Beispiel wird ein Stoßdämpfer ([shock absorber](https://en.wikipedia.org/wiki/Shock_absorber)) erstellt.

Die Baugruppe besteh aus drei Festkörpern: ei Kolben, ein Zylinder und eine Feder. Außerdem werden drei Nicht-Festkörper-Elemente gebraucht, zwei Achsen und eine Stange. Alle Bauteile werden mit mehreren Verbindungen zusammengefügt.

Das Gelenk des Kolbens rotiert um Achse2 (Axle2), während das Gelenk des Zylinders sich auf einem Kreisbogen mit dem Mittelpunkt auf Achse1 (Axle1) bewegt. Für diese Bewegung wird der Nicht-Festkörper Stange (Rod) verwendet. Die Länge der Stange ist der Radius des Kreisbogens.



### Bauteile vorbereiten 

Der folgende Python-Code erstellt ein neues Dokument mit 6 Objekten. Ein neues [Makro](Macros/de.md) erstellen, den Code kopieren und in den Python-Editor einfügen (nicht in die Python-Konsole). Dann das [Makro ausführen](Std_DlgMacroExecuteDirec/det.md).

Der unten stehende Programm-Kode kann nicht in der Python Konsole ausgeführt werden, weil die Feder durch eine Klasse welche die Callback Funktionen {{Incode|execute()}} und {{Incode|onChanged()}} enthält, als ein [Part::FeaturePython](App_FeaturePython.md) Objekt definiert werden muss. Nur dann kann ihre Höhe durch eine Eigenschaft verändert werden.


```python
import math
import FreeCAD as App
import FreeCADGui as Gui
import Part

doc = App.newDocument()

class Spring():
    def __init__(self, spring):
        spring.addProperty("App::PropertyLength", "Height", "Spring", "Height of the helix").Height = 200.0
        spring.Proxy = self
        spring.ViewObject.Proxy = 0
        
    def execute(self, spring):
        helix = Part.makeHelix(spring.Height/8.5, spring.Height, 35)
        startPnt = helix.Edges[0].Curve.value(0)
        section = Part.Wire([Part.Circle(startPnt, App.Vector(0, 1, 0), 5).toShape()])
        hel1 = helix.makePipeShell([section], True, True)
        box1 = Part.makeBox(80, 80, 10, App.Vector(-40, -40, -10))
        box2 = Part.makeBox(80, 80, 10, App.Vector(-40, -40, spring.Height))
        shape = hel1.cut(box1).cut(box2)
        spring.Shape = shape
        
    def onChanged(self, spring, prop):
        if prop == "Height":
            self.execute(spring) 
            
spring = doc.addObject("Part::FeaturePython", "Spring")
Spring(spring)
spring.Placement.Base = App.Vector(0, 100, 0)

axle1 = doc.addObject("Part::Line", "Axle1")
axle1.X2 = 0
axle1.Y2 = 80
axle1.Z2 = 0

axle2 = doc.addObject("Part::Line", "Axle2")
axle2.X2 = 0
axle2.Y2 = 80
axle2.Z2 = 0
axle2.Placement.Base = App.Vector(120, 0, -250)

rod = doc.addObject("Part::Line", "Rod")
rod.X2 = 100
rod.Y2 = 0
rod.Z2 = 0
rod.Placement.Base = App.Vector(0, -50, 0)

cyl1 = Part.makeCylinder(40, 10,App.Vector(0, 0, -5))
tor1 = Part.makeTorus(40, 5)
cyl2 = Part.makeCylinder(45, 5)
box1 = Part.makeBox(30, 10, 30,App.Vector(-15, -5, -35))
cyl3 = Part.makeCylinder(15, 10, App.Vector(0, -5, -35), App.Vector(0, 1, 0))
cyl4 = Part.makeCylinder(40, 5)
cyl5 = Part.makeCylinder(5, 10,App.Vector(0, -5, -35), App.Vector(0, 1, 0))
cyl6 = Part.makeCylinder(5, 130)
cyl7 = Part.makeCylinder(20, 5,App.Vector(0, 0, 130))
shape = cyl1.fuse([tor1,cyl2, box1, cyl3]).cut(cyl4.fuse([cyl5])).fuse([cyl6, cyl7])
piston = doc.addObject("Part::Feature", "Piston")
piston.Shape = shape.removeSplitter()
piston.Placement.Base = App.Vector(200, 100, -200)

cyl1 = Part.makeCylinder(40, 10,App.Vector(0, 0, -5))
tor1 = Part.makeTorus(40, 5)
cyl2 = Part.makeCylinder(45, 5)
box1 = Part.makeBox(30, 10, 30,App.Vector(-15, -5, -35))
cyl3 = Part.makeCylinder(15, 10,App.Vector(0, -5, -35), App.Vector(0, 1, 0))
cyl4 = Part.makeCylinder(40, 5)
cyl5 = Part.makeCylinder(5, 10,App.Vector(0, -5, -35), App.Vector(0, 1, 0))
cyl6 = Part.makeCylinder(25, 130)
tor2 = Part.makeTorus(20, 5,App.Vector(0, 0, 130))
cyl7 = Part.makeCylinder(20, 135)
cyl8 = Part.makeCylinder(20, 130)
cyl9 = Part.makeCylinder(5, 135)
shape = cyl1.fuse([tor1, cyl2, box1, cyl3]).cut(cyl4.fuse([cyl5])).fuse([cyl6, tor2, cyl7]).cut(cyl8.fuse([cyl9]))
cylinder = doc.addObject("Part::Feature", "Cylinder")
cylinder.Shape = shape.removeSplitter()
cylinder.Placement.Rotation.Axis = App.Vector(0, 1, 0)
cylinder.Placement.Rotation.Angle = math.pi
cylinder.Placement.Base = App.Vector(100, 100, 0)

mat = piston.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.80, 0.60, 0.15, 0.0)
piston.ViewObject.ShapeAppearance = (mat,)

mat = cylinder.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.55, 0.70, 0.70, 0.0)
cylinder.ViewObject.ShapeAppearance = (mat,)

doc.recompute()
view = Gui.ActiveDocument.ActiveView
view.viewIsometric()
view.fitAll()
```



### Eine Baugruppe hinzufügen 

Der Befehl <img alt="" src=images/Assembly_CreateAssembly.svg  style="width:24px;"> [Baugruppe erstellen](Assembly_CreateAssembly/de.md) fügt dem Dokument eine Baugruppe hinzu.



### Die Bauteile in die Baugruppe verschieben 

Die Bauteile in der [Baumansicht](Tree_view/de.md) auf das Baugruppenobjekt (Assembly object) ziehen und ablegen. Sie können jetzt vom Assembly-Gleichungslöser verarbeitet werden.


<div lang="en" dir="ltr" class="mw-content-ltr">

### Ground the two axles 


</div>

Um die Baugruppe an der gewünschten Position zu halten, sollten die beiden Achsen gesperrt oder, wie es hier genannt wird, geerdet werden. Wählen Sie die beiden Achsen in der [Baumansicht](Tree_view.md) oder in der [3D-Ansicht](3D_view.md) aus und verwenden Sie das Werkzeug <img alt="" src=images/Assembly_ToggleGrounded.svg  style="width:24px;"> [Geerdet umschalten](Assembly_ToggleGrounded.md). Dem Joints-Container werden zwei GroundedJoint-Objekte hinzugefügt.



### Verbindungen hinzufügen 


<div lang="en" dir="ltr" class="mw-content-ltr">

-   A Revolute joint between Axle2 and Piston


</div>

<img alt="" src=images/Assembly_ShockAbsorberExample-02.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-03.png  style="width:200px;">


<div lang="en" dir="ltr" class="mw-content-ltr">



*<img src="images/Assembly_CreateJointRevolute.svg" width=24px> [Create Revolute Joint](Assembly_CreateJointRevolute.md) + Selected elements → rearranged Piston*


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   A Slider joint between Piston and Cylinder


</div>

<img alt="" src=images/Assembly_ShockAbsorberExample-04.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-05.png  style="width:200px;">


<div lang="en" dir="ltr" class="mw-content-ltr">



*<img src="images/Assembly_CreateJointSlider.svg" width=24px> [Create Slider Joint](Assembly_CreateJointSlider.md) + Selected elements → rearranged and moved Cylinder*


</div>

Bitte achten Sie vor der Auswahl einer Fläche auf die Lage des Koordinatensystems. Es sollte sich jeweils im Mittelpunkt der Fläche befinden.

Ziehen Sie den Zylinder, um eine gewisse Abgrenzung zum Kolben zu schaffen. Die Stützflächen für die Feder sollten sichtbar sein.


<div lang="en" dir="ltr" class="mw-content-ltr">

-   A Distance joint between Piston and Cylinder


</div>

<img alt="" src=images/Assembly_ShockAbsorberExample-06A.png  style="width:200px;"> <img alt="" src=images/List-add.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-06B.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-07.png  style="width:200px;">


<div lang="en" dir="ltr" class="mw-content-ltr">



*<img src="images/Assembly_CreateJointDistance.svg" width=24px> [Create Distance Joint](Assembly_CreateJointDistance.md) + Selected faces → rearranged Cylinder Distance set to 200 mm*


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Set the distance value to 200 mm.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The next two joints are necessary to force the hinge of the Cylinder to move on an arc of circle.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   A Cylindrical joint between Axle1 and Rod


</div>

<img alt="" src=images/Assembly_ShockAbsorberExample-08.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-09.png  style="width:200px;">


<div lang="en" dir="ltr" class="mw-content-ltr">



*<img src="images/Assembly_CreateJointCylindrical.svg" width=24px> [Create Cylindrical Joint](Assembly_CreateJointCylindrical.md) + Selected elements → rearranged Rod*


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Make sure the Z axis of the coordinate system (blue) is perpendicular to the Rod by selecting an endpoint.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   A Revolute joint between Rod and Cylinder


</div>

<img alt="" src=images/Assembly_ShockAbsorberExample-10.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-11.png  style="width:200px;">


<div lang="en" dir="ltr" class="mw-content-ltr">



*<img src="images/Assembly_CreateJointRevolute.svg" width=24px> [Create Revolute Joint](Assembly_CreateJointRevolute.md) + Selected elements → rearranged Cylinder*


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Again make sure the Z axis of the coordinate system (blue) is perpendicular to the Rod.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

You may encounter problems with this joint. If that is the case try the following:

1.  Delete the joint.
2.  Switch to the [front view](Std_ViewFront.md).
3.  Rotate the assembly (by dragging the Piston) and rotate the Rod so that center of the hinge hole of the Cylinder lies on the Rod.
4.  Create the joint again.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The next two joints are necessary to fix the Spring to the support face.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   A Parallel joint between Spring and Piston


</div>

<img alt="" src=images/Assembly_ShockAbsorberExample-12A.png  style="width:200px;"> <img alt="" src=images/List-add.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-12B.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-13.png  style="width:200px;">


<div lang="en" dir="ltr" class="mw-content-ltr">



*<img src="images/Assembly_CreateJointParallel.svg" width=24px> [Create Parallel Joint](Assembly_CreateJointParallel.md) + Selected faces → rearranged Spring*


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Select the center of the support face on the Piston and the center of the bottom face of the spring. Keep the distance value 0.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   A Fixed joint between Spring and Piston


</div>

<img alt="" src=images/Assembly_ShockAbsorberExample-14A.png  style="width:200px;"> <img alt="" src=images/List-add.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-14B.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-15.png  style="width:200px;">


<div lang="en" dir="ltr" class="mw-content-ltr">



*<img src="images/Assembly_CreateJointFixed.svg" width=24px> [Create Fixed Joint](Assembly_CreateJointFixed.md) + Selected elements → rearranged Spring*


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Select the bottom vertex of the cylinder\'s seam in the Piston and the corner vertex in the Spring.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   Connect the distance property of the **Distance** joint to the Spring\'s **Height** property using an [expression](Expressions.md):


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

1.  Select the Spring in the [Tree view](Tree_view.md).
2.  Select the blue icon <img alt="" src=images/Bound-expression.svg  style="width:16px;"> in the Height property field.
3.  Enter in the expression editor: {{Incode|<<Distance>>.Distance}}


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Drive the shock absorber 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

To do so double-click the Distance object in the Tree view and change its Distance property. Recompute the document. The spring changes its length.


</div>


</div>


</div>





{{Assembly_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Assembly](Category_Assembly.md) > Assembly Workbench/de
