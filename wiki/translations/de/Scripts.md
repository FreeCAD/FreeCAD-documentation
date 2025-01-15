---
 TutorialInfo:e
   Topic: Skripten
   Level: Basis
   Time: 
   Author: onekk Carlo
   FCVersion: 0.19
   Files: 
---

# Scripts/de










## Einführung

Unter Skripten verstehen wir die Erstellung topologischer Objekte mit dem Python-Interpreter von FreeCAD. FreeCAD könnte ein \"sehr guter\" Ersatz für OpenSCAD sein, vor allem, weil es einen echten Python-Interpreter hat, das heißt, es hat eine echte Programmiersprache an Bord, fast alles, was man mit der GUI machen kann, ist mit einem Python-Skript machbar.

Bedauerlicherweise sind die Informationen über das Skripten in der Dokumentation und sogar in diesem Wiki verstreut und es mangelt an Einheitlichkeit beim \"Schreiben\", und die meisten von ihnen werden zu technisch erklärt.



## Erste Schritte 

Das erste Hindernis auf einem einfachen Weg zur Skripterstellung ist, dass es keine direkte Möglichkeit gibt, den FreeCAD internen Python Editor über einen Menüeintrag oder ein Symbol im Werkzeugleistenbereich aufzurufen, aber wenn man weiß, dass FreeCAD eine Datei mit der Erweiterung `.py` im internen Python Editor öffnet, ist der einfachste Trick, sie in Ihrem bevorzugten Texteditor zu erstellen und sie dann mit dem üblichen Befehl **Datei → Öffnen** zu öffnen.

Um die Dinge in einer höflichen Art und Weise zu machen, muss die Datei mit einer gewissen Ordnung geschrieben werden. Der FreeCAD-Python-Editor hat eine gute \"Syntax-Hervorhebung\", die in vielen einfachen Editoren wie Windows Notepad oder einige grundlegende Linux Editoren fehlt, so ist es ausreichend, diese wenigen Zeilen zu schreiben:


```python
"""filename.py

   A short description of what the script does

"""
```

Diese werden mit einem aussagekräftigen Namen und der Erweiterung `.py` gespeichert und die resultierende Datei in FreeCAD geladen, mit dem besagten Befehl **Datei → Öffnen**.

Ein Minimalbeispiel dafür, was in einem Skript enthalten sein muss, wird in diesem Teil des Codes gezeigt, den du als Vorlage für fast jedes zukünftige Skript verwenden könntest:


```python
"""filename.py

   First FreeCAD Script

"""

import FreeCAD
from FreeCAD import Placement, Rotation, Vector
import FreeCADGui

DOC_NAME = "Wiki_Example"
DOC = FreeCAD.newDocument(DOC_NAME)
FreeCAD.setActiveDocument(DOC.Name)

ROT0 = Rotation(0, 0, 0)
VEC0 = Vector(0, 0, 0)

# Helper function

def set_view():
    """Rearrange View."""
    if not FreeCAD.GuiUp:
        return
    doc = FreeCADGui.ActiveDocument
    if doc is None:
        return
    view = doc.ActiveView
    if view is None:
        return
    # Check if the view is a 3D view:
    if not hasattr(view, "getSceneGraph"):
        return
    view.viewAxometric()
    view.fitAll()
```

Der obige Code enthält einige Tricks:

-    `import FreeCAD`Diese Zeile importiert FreeCAD in FreeCADs Python-Interpreter. Es mag überflüssig erscheinen, ist es aber nicht.

-    `from FreeCAD import Placement, Rotation, Vector`**Placement** **Rotation** and **Vector** sind in FreeCAD-Skripten weit verbreitet. Werden sie auf diese Weise importiert, erspart dies viele Tastendrücke und verkürzt Codezeilen, da statt `FreeCAD.Vector` oder `FreeCAD.Placement` nur noch `Vector` oder `Placement` getippt werden muss.

Lasse uns mit einem kleinen Skript anfangen, das eine sehr kleine Arbeit leistet, aber die Kraft dieses Ansatzes zeigt.


```python
# Script functions

def my_box(name, len, wid, hei):
    """Create a box."""
    obj_b = DOC.addObject("Part::Box", name)
    obj_b.Length = len
    obj_b.Width = wid
    obj_b.Height = hei

    DOC.recompute()

    return obj_b

# objects definition

obj = my_box("test_cube", 5, 5, 5)

set_view()
```

Die obigen Codezeilen werden nach `# Script functions` eingegeben und der grüne Pfeil in der Symbolleiste **Macro** gedrückt.

Du wirst einige magische Dinge sehen, ein neues Dokument mit dem Namen \"Wiki_example\" wird geöffnet, und du wirst in der 3D-Ansicht einen [Würfel](Part_Box/de.md) sehen, wie in der Abbildung unten.

![Test cube](images/Cubo.png )



## Etwas mehr 

Nicht allzu erstaunlich? Ja, aber irgendwo müssen wir anfangen, wir können das Gleiche mit einem [Zylinder](Part_Cylinder/de.md) tun; diese Kodezeilen werden nach der Funktion `my_box()` und vor der Zeile `# objects definition` hinzugefügt.


```python
def my_cyl(name, ang, rad, hei):
    """Create a Cylinder."""
    obj = DOC.addObject("Part::Cylinder", name)
    obj.Angle = ang
    obj.Radius = rad
    obj.Height = hei

    DOC.recompute()

    return obj
```

Auch hier nichts allzu Aufregendes. Aber bitte beachte einige Besonderheiten:

-   Das Fehlen des üblichen Verweises auf die `App.`, die in vielen Dokumentations-Codeschnipseln vorhanden ist, ist beabsichtigt, dieser Code könnte sogar beim Aufruf von FreeCAD als Modul in einem externen Python-Interpreter verwendet werden, die Sache ist mit einem AppImage nicht einfach zu bewerkstelligen, aber mit etwas Vorsicht wäre es machbar. Und in dem Standard Motto von Python, dass \"besser explizit als implizit\" `App.` in einer sehr \" dürftigen\" Weise erklärt, woher die Dinge kommen.
-   Beachte die Verwendung des dem aktiven Dokument zugewiesenen \"konstanten\" Namens in `DOC &#61; FreeCAD. activeDocument()`; activeDocument ist keine \"Konstante\" im strengen Sinne, aber in einer \"semantischen\" Weise ist unser \"aktives Dokument\", das für unseren Gebrauch eine richtige \"Konstante\" ist, so dass die Python Konvention, den \"ALL CAPS\" Namen für \"Konstanten\" zu verwenden, ganz zu schweigen davon, dass `DOC` viel kürzer ist als `FreeCAD.activeDocument()`.
-   Jede Funktion gibt eine Geometrie zurück, dies wird in der Fortsetzung der Seite deutlich.
-   Geometrie hatte nicht die Eigenschaft `Placement`, wenn die einfachen Geometrien verwendet werden, um komplexere Geometrie zu erstellen, ist die Verwaltung von `Placement` eine umständliche Sache.

Was ist nun mit diesen Geometrien zu tun?

Lasst uns boolesche Verknüpfungen einführen. Als Einstiegsbeispiel werden diese Zeilen nach `my_cyl` eingefügt; dies erzeugt eine Funktion zum **Verschmelzen** (fuse), bekannt als **Vereinigung**:


```python
def fuse_obj(name, obj_0, obj_1):
    """Fuse two objects."""
    obj = DOC.addObject("Part::Fuse", name)
    obj.Base = obj_0
    obj.Tool = obj_1
    obj.Refine = True
    DOC.recompute()

    return obj
```

Nichts Außergewöhnliches auch hier, beachte jedoch die Einheitlichkeit in der Programmierung der Funktion; Dieser Ansatz ist linearer als derjenige, den man in anderen Anleitungen zur Skripterstellung sieht, diese \"Linearität\" hilft sehr bei der Lesbarkeit und auch bei Ausschneiden-Kopieren-Einfügen Operationen.

Verwenden wir die Geometrien, löschen wir Zeilen unterhalb des Codeabschnitts, die mit `# objects definition` beginnen, und fügen wir die folgenden Zeilen ein:


```python
# objects definition

obj = my_box("test_cube", 5, 5, 5)

obj1 = my_cyl("test_cyl", 360, 2, 10)

fuse_obj("Fusion", obj, obj1)

set_view()
```

Starte das Skript mit dem grünen Pfeil und wir sehen in der 3D_Ansicht so etwas:

![Würfel und Zylinder](images/Cucil.png )



## Platzierung

Das Platzierungskonzept ist relativ komplex, siehe [Aeroplane Tutorium](Aeroplane/de.md) für eine ausführlichere Erklärung.

Normalerweise ist es notwendig, dass sich die Geometrien gegenseitig respektieren. Beim Bau komplexer Objekte ist dies eine wiederkehrende Aufgabe, am häufigsten wird die Geometrie `Placement` Eigenschaft verwendet.

FreeCAD bietet eine große Auswahl an Möglichkeiten, diese Eigenschaft zu setzen, eine ist mehr auf eine andere zugeschnitten, abhängig vom Wissen und dem Hintergrund des Benutzers, aber je klarer das Schreiben im zitierten Tutoriumerklärt wird, verwendet es eine eigentümliche Definition des `Rotation` Anteils von `Placement`, recht einfach zu erlernen.


```python
FreeCAD.Placement(Vector(0, 0, 0), FreeCAD.Rotation(10, 20, 30), Vector(0, 0, 0))
```

Aber gegenüber anderen Überlegungen ist eine Sache ausschlaggebend, nämlich der geometrische **Referenzpunkt**, also der Punkt, von dem aus das Objekt von FreeCAD modelliert wird, wie in dieser Tabelle beschrieben, kopiert von [Platzierung](Placement/de.md):

  Objekt                                Referenzpunkt
   
  Part.Box                              links (minx), vorne (miny), unten (minz) Knoten
  Part.Sphere                           Mittelpunkt der Kugel
  Part.Cylinder                         Mitte der Unterseite
  Part.Cone                             Mittelpunkt der Unterseite (oder Scheitelpunkt, wenn der Unterseitenradius 0 ist)
  Part.Torus                            Mittelpunkt des Torus
  Formelemente abgeleitet aus Skizzen   das Formelement erbt die Position der zugrunde liegenden Skizze. Skizzen beginnen immer mit Position = (0, 0, 0). Diese Position entspricht dem Ursprung in der Skizze.

Diese Informationen müssen wir vor allem dann im Auge behalten, wenn wir eine Rotation anwenden müssen.

Einige Beispiele könnten helfen. Dazu die Funktion `my_box` und alle Zeilen nach der Funktion `my_cyl` löschen und den unten gezeigten Code nach der Funktion `my_cyl` hinzufügen:


```python
def my_sphere(name, rad):
    """Create a Sphere."""
    obj = DOC.addObject("Part::Sphere", name)
    obj.Radius = rad

    DOC.recompute()

    return obj

def my_box2(name, len, wid, hei, cent=False, off_z=0):
    """Create a box with an optional z offset."""
    obj_b = DOC.addObject("Part::Box", name)
    obj_b.Length = len
    obj_b.Width = wid
    obj_b.Height = hei

    if cent is True:
        pos = Vector(len * -0.5, wid * -0.5, off_z)
    else:
        pos = Vector(0, 0, off_z)

    obj_b.Placement = Placement(pos, ROT0, VEC0)

    DOC.recompute()

    return obj_b

def mfuse_obj(name, objs):
    """Fuse multiple objects."""
    obj = DOC.addObject("Part::MultiFuse", name)
    obj.Shapes = objs
    obj.Refine = True
    DOC.recompute()

    return obj

def airplane():
    """Create an airplane shaped solid."""
    fuselage_length = 30
    fuselage_diameter = 5
    wing_span = fuselage_length * 1.75
    wing_width = 7.5
    wing_thickness = 1.5
    tail_height = fuselage_diameter * 3.0
    tail_position = fuselage_length * 0.70
    tail_offset = tail_position - (wing_width * 0.5)

    obj1 = my_cyl("main_body", 360, fuselage_diameter, fuselage_length)

    obj2 = my_box2("wings", wing_span, wing_thickness, wing_width, True, tail_offset)

    obj3 = my_sphere("nose", fuselage_diameter)
    obj3.Placement = Placement(Vector(0, 0, fuselage_length), ROT0, VEC0)

    obj4 = my_box2("tail", wing_thickness, tail_height, wing_width, False, 0)
    obj4.Placement = Placement(Vector(0, tail_height * -1, 0), ROT0, VEC0)

    objs = (obj1, obj2, obj3, obj4)

    obj = mfuse_obj("airplane", objs)
    obj.Placement = Placement(VEC0, Rotation(0, 0, -90), Vector(0, 0, tail_position))

    DOC.recompute()

    return obj

# objects definition

airplane()

set_view()

```

Lasse uns etwas im Code erklären:

-   Wir haben eine Funktion verwendet, um eine Kugel zu definieren, wobei wir die einfachste Definition verwendet haben und nur den Radius verwendet haben.
-   Wir haben eine zweite Schreibweise für die **Vereingung** oder **Verschmelzung** eingeführt, die mehrere Objekte verwendet, nicht weiter entfernt von dem üblichen **Part::Fuse** es verwendet **Part:Multifuse**. Wir verwenden nur eine Eigenschaft `Formen`. Wir haben ein **Tupel** als Argumente übergeben, aber es akzeptiert auch eine **Liste**.
-   Wir haben ein komplexes Objekt **airplane**\' definiert, aber wir haben es auf eine **\"parametrische\"** Art und Weise getan, indem wir einige Parameter definiert und andere Parameter durch einige Berechnungen auf der Grundlage der Hauptparameter abgeleitet haben.
-   Wir haben einige Positionierungseigenschaften ` Placement` in der Funktion verwendet, und bevor wir die endgültigen Geometrien zurückgeben, haben wir eine Eigenschaft `Rotation` mit der *Gieren-Stampfen-Rollen* Schreibweise verwendet. Beachte die letzte `Vector(0, 0, tail_position)`, die ein **Rotationszentrum** der gesamten Geometrie definieren.

++++
| ![Airplane example](images/Aereo.png ) | ![Airplane rotated](images/Aereo2.png ) | ![Placement property](images/Aereo-prop.png ) |
++++

Man kann leicht feststellen, dass die **airplane**-Geometrie um ihr \"Baryzentrum\" oder ihren \"Schwerpunkt\" rotiert, den ich in der Flügelmitte festgelegt habe, ein Ort, der relativ \"natürlich\" ist, aber wo immer man will, platziert werden könnte.

Der erste `Vector(0, 0, 0)` ist der Übersetzungsvektor, der hier nicht verwendet wird, aber wenn du `airplane()` durch diese Zeilen ersetzt:


```python
obj_f = airplane()

print(obj_F.Placement)
```

Du wirst diesen Text im Berichtsfenster sehen:


```python
Placement [Pos=(0, -21, 21), Yaw-Pitch-Roll=(0, 0, -90)]
```

Was ist geschehen?

FreeCAD hat `Vector(0, 0, 0), FreeCAD.Rotation(0, 0, -90), Vector(0, 0, tail_position)` mit anderen Worten unsere `Placement`-Definition übersetzt, die drei Komponenten, **Translation**, **Rotation** und *Rotationszentrum**in die \"internen\" Werte von nur zwei Komponenten,**Translation**und**Rotation*\', festlegt.

Du kannst leicht den Wert von `tail_position` mit einer print Anweisung in der Funktion `airplane()` visualisieren und dies sehen:


```python
tail_position = 21.0
```

mit anderen Worten, das **Rotationszentrum** der Geometrie liegt bei `Vector(0, 0, 21)`, aber dieses Rotationszentrum wird in der GUI nicht angezeigt, es könnte als `Placement` Wert eingegeben werden, es könnte nicht leicht abgerufen werden.

Dies ist die Bedeutung des Wortes \"umständlich\", das ich zur Definition der `Placement` Eigenschaft verwendet habe.

This is the complete code example with a decent script docstring following [Google docstrings convention](https://www.sphinx-doc.org/en/master/usage/extensions/example_google.html#example-google):


```python
"""Sample code.

Filename:
   airplane.py

Author:
    Dormeletti Carlo (onekk)

Version:
    1.0

License:
    Creative Commons Attribution 3.0

Summary:
    This is sample code written for a FreeCAD Wiki page.
    It creates an airplane shaped solid using standard "Part WB" shapes.

"""

import FreeCAD
from FreeCAD import Placement, Rotation, Vector
import FreeCADGui

DOC_NAME = "Wiki_Example"
DOC = FreeCAD.newDocument(DOC_NAME)
FreeCAD.setActiveDocument(DOC.Name)

ROT0 = Rotation(0, 0, 0)
VEC0 = Vector(0, 0, 0)

# Helper function

def set_view():
    """Rearrange View."""
    if not FreeCAD.GuiUp:
        return
    doc = FreeCADGui.ActiveDocument
    if doc is None:
        return
    view = doc.ActiveView
    if view is None:
        return
    # Check if the view is a 3D view:
    if not hasattr(view, "getSceneGraph"):
        return
    view.viewAxometric()
    view.fitAll()

# Script functions

def my_cyl(name, ang, rad, hei):
    """Create a Cylinder."""
    obj = DOC.addObject("Part::Cylinder", name)
    obj.Angle = ang
    obj.Radius = rad
    obj.Height = hei

    DOC.recompute()

    return obj

def my_sphere(name, rad):
    """Create a Sphere."""
    obj = DOC.addObject("Part::Sphere", name)
    obj.Radius = rad

    DOC.recompute()

    return obj

def my_box2(name, len, wid, hei, cent=False, off_z=0):
    """Create a box with an optional z offset."""
    obj_b = DOC.addObject("Part::Box", name)
    obj_b.Length = len
    obj_b.Width = wid
    obj_b.Height = hei

    if cent is True:
        pos = Vector(len * -0.5, wid * -0.5, off_z)
    else:
        pos = Vector(0, 0, off_z)

    obj_b.Placement = Placement(pos, ROT0, VEC0)

    DOC.recompute()

    return obj_b

def mfuse_obj(name, objs):
    """Fuse multiple objects."""
    obj = DOC.addObject("Part::MultiFuse", name)
    obj.Shapes = objs
    obj.Refine = True
    DOC.recompute()

    return obj

def airplane():
    """Create an airplane shaped solid."""
    fuselage_length = 30
    fuselage_diameter = 5
    wing_span = fuselage_length * 1.75
    wing_width = 7.5
    wing_thickness = 1.5
    tail_height = fuselage_diameter * 3.0
    tail_position = fuselage_length * 0.70
    tail_offset = tail_position - (wing_width * 0.5)

    obj1 = my_cyl("main_body", 360, fuselage_diameter, fuselage_length)

    obj2 = my_box2("wings", wing_span, wing_thickness, wing_width, True, tail_offset)

    obj3 = my_sphere("nose", fuselage_diameter)
    obj3.Placement = Placement(Vector(0, 0, fuselage_length), ROT0, VEC0)

    obj4 = my_box2("tail", wing_thickness, tail_height, wing_width, False, 0)
    obj4.Placement = Placement(Vector(0, tail_height * -1, 0), ROT0, VEC0)

    objs = (obj1, obj2, obj3, obj4)

    obj = mfuse_obj("airplane", objs)
    obj.Placement = Placement(VEC0, Rotation(0, 0, -90), Vector(0, 0, tail_position))

    DOC.recompute()

    return obj

# objects definition

airplane()

set_view()
```



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Scripts/de
