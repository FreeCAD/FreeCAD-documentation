# Scripts/de
 {{TutorialInfo/de
|Topic=Skripten
|Level=Basis
|Time=
|Author=onekk Carlo
|FCVersion=0.19
|Files=
}}

## Einführung

Unter Skripten verstehen wir die Erstellung topologischer Objekte mit dem Python Interpreter von FreeCAD. FreeCAD könnte ein \"sehr guter\" Ersatz für OpenSCAD sein, vor allem, weil es einen echten Python Interpreter hat, das heißt, es hat eine echte Programmiersprache an Bord, fast alles, was man mit der GUI machen kann, ist mit einem Python Skript machbar.

Bedauerlicherweise sind die Informationen über das Skripten in der Dokumentation und sogar in diesem Wiki verstreut und es mangelt an Einheitlichkeit beim \"Schreiben\", und die meisten von ihnen werden zu technisch erklärt.

## Befeuchte deinen Appetit 

Das erste Hindernis auf einem einfachen Weg zur Skripterstellung ist, dass es keine direkte Möglichkeit gibt, den FreeCAD internen Python Editor über einen Menüeintrag oder ein Symbol im Werkzeugleistenbereich aufzurufen, aber wenn man weiß, dass FreeCAD eine Datei mit der Erweiterung `.py` im internen Python Editor öffnet, ist der einfachste Trick, sie in Ihrem bevorzugten Texteditor zu erstellen und sie dann mit dem üblichen Befehl **Datei → Öffnen** zu öffnen.

Um die Dinge in einer höflichen Art und Weise zu machen, muss die Datei mit einer gewissen Ordnung geschrieben werden, FreeCAD Python Editor haben eine gute \"Syntax Hervorhebung\", die in vielen einfachen Editoren wie Windows Notepad oder einige grundlegende Linux Editoren fehlt, so ist es ausreichend, diese wenigen Zeilen zu schreiben:


```python
"""script.py

   Primo script per FreeCAD

"""

```

Speichere sie mit einem aussagekräftigen Namen mit der Erweiterung `.py` und lade die resultierende Datei in FreeCAD, mit dem besagten **Datei - Öffnen** Befehl.

Ein Minimalbeispiel dafür, was in einem Skript enthalten sein muss, wird in diesem Teil des Codes gezeigt, den du als Vorlage für fast jedes zukünftige Skript verwenden könntest:


```python
"""filename.py

   Here a short but significant description of what the script do 

"""


import FreeCAD
from FreeCAD import Base, Vector
import Part
from math import pi, sin, cos

DOC = FreeCAD.activeDocument()
DOC_NAME = "Pippo"

def clear_doc():
    """
    Clear the active document deleting all the objects
    """
    for obj in DOC.Objects:
        DOC.removeObject(obj.Name)

def setview():
    """Rearrange View"""
    FreeCAD.Gui.SendMsgToActiveView("ViewFit")
    FreeCAD.Gui.activeDocument().activeView().viewAxometric()


if DOC is None:
    FreeCAD.newDocument(DOC_NAME)
    FreeCAD.setActiveDocument(DOC_NAME)
    DOC = FreeCAD.activeDocument()

else:

    clear_doc()

# EPS= tolerance to use to cut the parts
EPS = 0.10
EPS_C = EPS * -0.5

```

Der obige Code enthält einige Tricks:

-    `import FreeCAD`Diese Zeile importiert FreeCAD in den FreeCAD Python Interpreter, es mag überflüssig erscheinen, ist es aber nicht.

-    `von der FreeCAD Importbasis, Vektor`Basis und Vektor sind in FreeCAD-Skripten weit verbreitet. Wenn du sie auf diese Weise importierst, ersparst du dir den Aufruf mit `FreeCAD.Vector` oder `FreeCAD.Base` anstelle von `Basis` oder `Vektor`, dies erspart viele Tastatureingaben und macht Codezeilen viel kleiner.

Lasse uns mit einem kleinen Skript anfangen, das eine sehr kleine Arbeit leistet, aber die Kraft dieses Ansatzes zeigt.


```python
def cubo(nome, lung, larg, alt):
    obj_b = DOC.addObject("Part::Box", nome)
    obj_b.Length = lung
    obj_b.Width = larg
    obj_b.Height = alt

    DOC.recompute()

    return obj_b

# objects definition

obj = cubo("test_cube", 5, 5, 5)

setview()

```

Setze diese Zeilen nach dem \"Vorlage\" Code und drücke den grünen Pfeil in der **Makro Werkzeugleiste**

Du wirst einige magische Dinge sehen, ein neues Dokument mit dem Namen \"Pippo\" (italienischer Name von **Goofy**\') ist geöffnet, und du wirst in der 3D Ansicht einen [Würfel](Part_Box/de.md) sehen, wie in der Abbildung unten.

![Test Cube](images/Cubo.png )

## Etwas mehr\... 

Nicht allzu erstaunlich? Ja, aber irgendwo müssen wir anfangen, wir können das Gleiche mit einem [Zylinder](Part_Cylinder/de.md) tun, diese Codezeilen nach der `cubo(` Methode und vor der Zeile `# objects definition` hinzufügen.


```python
def base_cyl(nome, ang, rad, alt ):
    obj = DOC.addObject("Part::Cylinder", nome)
    obj.Angle = ang
    obj.Radius = rad
    obj.Height = altDOC.recompute()

    return obj   

```

Auch hier nichts allzu Aufregendes. Aber bitte beachte einige Besonderheiten:

-   Das Fehlen des üblichen Verweises auf die `App.`, die in vielen Dokumentations Codeschnipseln vorhanden ist, ist beabsichtigt, dieser Code könnte sogar beim Aufruf von FreeCAD als Modul in einem externen Python Interpreter verwendet werden, die Sache ist mit einem AppImage nicht einfach zu bewerkstelligen, aber mit etwas Vorsicht wäre es machbar. Und in dem Standard Motto von Python, dass \"besser explizit als implizit\" `App.` in einer sehr \" dürftigen\" Weise erklärt, woher die Dinge kommen.
-   Beachte die Verwendung des dem aktiven Dokument zugewiesenen \"konstanten\" Namens in `DOC` = `FreeCAD. activeDocument()`; activeDocument ist keine \"Konstante\" im strengen Sinne, aber in einer \"semantischen\" Weise ist unser \"aktives Dokument\", das für unseren Gebrauch eine richtige \"Konstante\" ist, so dass die Python Konvention, den \"ALL CAPS\" Namen für \"Konstanten\" zu verwenden, ganz zu schweigen davon, dass `DOC` viel kürzer ist als `FreeCAD.activeDocument()`.
-   Jede Methode gibt eine Geometrie zurück, dies wird in der Fortsetzung der Seite deutlich.
-   Geometrie hatte nicht die Eigenschaft `Placement`, wenn die einfachen Geometrien verwendet werden, um komplexere Geometrie zu erstellen, ist die Verwaltung von `Placement` eine umständliche Sache.

Was ist nun mit diesen Geometrien zu tun?

Lasse uns boolesche Operationen einführen. Als Einstiegsbeispiel setze diese Zeilen nach `base_cyl(...`, dies erzeugt eine Methode für eine **Verschmelzung**, auch als **Vereinigung** Operation bekannt:


```python
def fuse_obj(nome, obj_0, obj_1):
    obj = DOC.addObject("Part::Fuse", nome)
    obj.Base = obj_0
    obj.Tool = obj_1
    obj.Refine = True
    DOC.recompute()

    return obj
```

Nichts Außergewöhnliches auch hier, beachte jedoch die Einheitlichkeit in der Methodencodierung; Dieser Ansatz ist linearer als derjenige, den man in anderen Tutorien zur Skripterstellung sieht, diese \"Linearität\" hilft sehr bei der Lesbarkeit und auch bei Ausschneiden-Kopieren-Einfügen Operationen.

Verwenden wir die Geometrien, löschen wir Zeilen unterhalb des Codeabschnitts, die mit `# objects definition` beginnen, und fügen wir die folgenden Zeilen ein:


```python

# objects definition

obj = cubo("cubo_di_prova", 5, 5, 5)

obj1 = base_cyl('primo cilindro', 360,2,10)

fuse_obj("Fusione", obj, obj1)

setview()

```

Starte das Skript mit dem grünen Pfeil und wir sehen in der 3D Ansicht so etwas wie:

![cube and cylinder](images/Cucil.png )

## Platzierung

Das Platzierungskonzept ist relativ komplex, siehe [Aeroplane Tutorium](Aeroplane/de.md) für eine ausführlichere Erklärung.

Normalerweise ist es notwendig, dass sich die Geometrien gegenseitig respektieren. Beim Bau komplexer Objekte ist dies eine wiederkehrende Aufgabe, am häufigsten wird die Geometrie `Placement` Eigenschaft verwendet.

FreeCAD bietet eine große Auswahl an Möglichkeiten, diese Eigenschaft zu setzen, eine ist mehr auf eine andere zugeschnitten, abhängig vom Wissen und dem Hintergrund des Benutzers, aber je klarer das Schreiben im zitierten Tutoriumerklärt wird, verwendet es eine eigentümliche Definition des `Rotation` Anteils von `Placement`, recht einfach zu erlernen.


```python 
FreeCAD.Placement(Vector(0,0,0), FreeCAD.Rotation(10,20,30), Vector(0,0,0))
```

Aber gegenüber anderen Überlegungen ist eine Sache ausschlaggebend, nämlich der geometrische **Referenzpunkt**, also der Punkt, von dem aus das Objekt von FreeCAD modelliert wird, wie in dieser Tabelle beschrieben, kopiert von [Platzierung](Placement/de.md):

  Objekt                                Referenzpunkt
  ------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Part.Box                              links (minx), vorne (miny), unten (minz) Knoten
  Part.Sphere                           Mittelpunkt der Kugel (d.h. Zentrum des Begrenzungskastens)
  Part.Cylinder                         Mitte der Unterseite
  Part.Cone                             Mittelpunkt der Unterseite (oder Scheitelpunkt, wenn der Unterseitenradius 0 ist)
  Part.Torus                            Mittelpunkt des Torus
  Formelemente abgeleitet aus Skizzen   das Formelement erbt die Position der zugrunde liegenden Skizze. Skizzen beginnen immer mit Position = (0,0,0). Diese Position entspricht dem Ursprung in der Skizze.

Diese Informationen müssen wir vor allem dann im Auge behalten, wenn wir eine Rotation anwenden müssen.

Einige Beispiele mögen helfen, lösche die gesamte Zeile nach der `base_cyl` Methode und füge den Teil des Codes darunter ein:


```python

def sfera(nome, rad):
    obj = DOC.addObject("Part::Sphere", nome)
    obj.Radius = radDOC.recompute()

    return obj   


def mfuse_obj(nome, objs):
    obj = DOC.addObject("Part::MultiFuse", nome)
    obj.Shapes = objs
    obj.Refine = True
    DOC.recompute()

    return obj


def aeroplano():

    lung_fus = 30
    diam_fus = 5
    ap_alare = lung_fus * 1.75
    larg_ali = 7.5
    spess_ali = 1.5   
    alt_imp = diam_fus * 3.0  
    pos_ali = (lung_fus*0.70)
    off_ali = (pos_ali - (larg_ali * 0.5))

    obj1 = base_cyl('primo cilindro', 360, diam_fus, lung_fus)

    obj2 = cubo('ali', ap_alare, spess_ali, larg_ali, True, off_ali)

    obj3 = sfera("naso", diam_fus)
    obj3.Placement = FreeCAD.Placement(Vector(0,0,lung_fus), FreeCAD.Rotation(0,0,0), Vector(0,0,0))

    obj4 = cubo('impennaggio', spess_ali, alt_imp, larg_ali, False, 0)
    obj4.Placement = FreeCAD.Placement(Vector(0,alt_imp * -1,0), FreeCAD.Rotation(0,0,0), Vector(0,0,0))

    objs = (obj1, obj2, obj3, obj4)

    obj = mfuse_obj("Forma esempio", objs)
    obj.Placement = FreeCAD.Placement(Vector(0,0,0), FreeCAD.Rotation(0,0,-90), Vector(0,0,pos_ali))

    DOC.recompute()

    return obj

# objects definition

aeroplano()

setview()

```

Lasse uns etwas im Code erklären:

-   Wir haben eine Methode verwendet, um eine Kugel zu definieren, wobei wir die einfachste Definition verwendet haben und nur den Radius verwendet haben.
-   Wir haben eine zweite Schreibweise für die **Vereingung** oder **Verschmelzung** eingeführt, die mehrere Objekte verwendet, nicht weiter entfernt von dem üblichen **Part::Fuse** es verwendet **Part:Multifuse**. Wir verwenden nur eine Eigenschaft `Formen`. Wir haben ein **Tupel** als Argumente übergeben, aber es akzeptiert auch eine **Liste**.
-   Wir haben ein komplexes Objekt **aeroplano**\' definiert. (italienisches Wort für Flugzeug), aber wir haben es auf eine **\"parametrische\"** Art und Weise getan, indem wir einige Parameter definiert und andere Parameter durch einige Berechnungen auf der Grundlage der Hauptparameter abgeleitet haben.
-   Wir haben einige Platzierungs `Platzierung` Eigenschaften in der Methode verwendet, und bevor wir die endgültigen Geometrien zurückgeben, haben wir eine `Rotation` Eigenschaft mit der *Gieren-Stampfen-Rollen* Schreibweise verwendet. Beachte die letzten `Vector(0,0, pos_ali)`, die ein **Rotationszentrum** der gesamten Geometrie definieren.

  ----------------------------------------------------- ---------------------------------------------- ----------------------------------------------------
  ![aeroplane example](images/Aereo.png )   ![aereo rotated](images/Aereo2.png )   ![Prop Placement](images/Aereo-prop.png )
  ----------------------------------------------------- ---------------------------------------------- ----------------------------------------------------

Man kann leicht feststellen, dass **aeroplano** Geometrie um sein \"Baryzentrum\" oder seinen \"Schwerpunkt\" rotiert, den ich in der Flügelmitte festgelegt habe, ein Ort, der relativ \"natürlich\" ist, aber wo immer man will, platziert werden könnte.

Der erste `Vector(0,0,0)` ist der Übersetzungsvektor, der hier nicht verwendet wird, aber wenn du `aeroplano()` durch diese Zeilen ersetzt:


```python

obj_f = aeroplano()

print(obj_F.Placement)

```

Du wirst diesen Text im Berichtsfenster sehen:


```python
Placement [Pos=(0,-21,21), Yaw-Pitch-Roll=(0,0,-90)]
```

Was ist geschehen?

FreeCAD hat die `Vector(0,0,0), FreeCAD.Rotation(0,0,-90), Vector(0,0,pos_ali)` mit anderen Worten unsere `Placement` Definition übersetzt, die drei Komponenten, **Translation**, **Rotation** und *Rotationszentrum*\' in den \"internen\" Werten von nur zwei Komponenten, **Translation** und **Rotation**, spezifiziert.

du kannst leicht den Wert von `pos_ali` mit einer print Anweisung in der `aeroplano(...` Methode visualisieren und sehen das es ist:


```python
pos ali =  21.0
```

mit anderen Worten, das **Rotationszentrum** der Geometrie liegt bei `Vector(0,0,21)`, aber dieses Rotationszentrum wird in der GUI nicht angezeigt, es könnte als `Placement` Wert eingegeben werden, es könnte nicht leicht abgerufen werden.

Dies ist die Bedeutung des Wortes \"umständlich\", das ich zur Definition der `Placement` Eigenschaft verwendet habe.


{{Powerdocnavi

}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)
