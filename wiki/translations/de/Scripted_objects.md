# Scripted objects/de
## Einführung

Neben den Standard-Objekttypen wie Beschriftungen, Netze und Bauteilobjekte bietet FreeCAD auch die erstaunliche Möglichkeit, 100% mit Python geschriebene parametrische Objekte zu erstellen, die als [Python-Objekt](App_FeaturePython.md) (App FeaturePython-Objekt) bezeichnet werden. Diese Objekte verhalten sich genau wie jedes andere FreeCAD-Objekt und werden beim Speichern/Laden von Dateien automatisch gespeichert und wiederhergestellt.

Eine Besonderheit muss beachtet werden: Aus Sicherheitsgründen enthalten FreeCAD Dateien niemals eingebetteten Code. Der Python Code, den du zum Erstellen von parametrischen Objekten schreibst, wird niemals innerhalb einer Datei gespeichert. Das bedeutet, dass, wenn du eine Datei, die ein solches Objekt enthält, auf einem anderen Rechner öffnest, wenn dieser Python Code auf diesem Rechner nicht verfügbar ist, das Objekt nicht vollständig neu erstellt wird. Wenn du solche Objekte an andere weitergibst, musst du auch dein Python Skript weitergeben, z. B. als [Makro](Macros/de.md).

**Hinweis**: Es ist möglich, Python Code in eine FreeCAD Datei zu packen, indem man json mit einem App::PropertyPythonObject serialisiert, aber dieser Code kann nie direkt ausgeführt werden und hat daher für unseren Zweck hier wenig Nutzen.

[Python-Objekte](App_FeaturePython/de.md) folgen der gleichen Regel wie alle FreeCAD Funktionen: Sie sind in App- und einen GUI-Teile getrennt. Der App-Teil, das Dokument-Objekt, definiert die Geometrie unseres Objekts, während sein GUI-Teil, das View-Provider-Objekt, definiert, wie das Objekt auf dem Bildschirm daegestellt wird. Das Ansichtsprovider-Objekt ist, wie jede andere FreeCAD-Funktion, nur verfügbar, wenn FreeCAD in seiner eigenen GUI ausgeführt wird. Es stehen mehrere Eigenschaften und Methoden zur Verfügung, um ein Objekt zu erstellen. Die Eigenschaften müssen zu einem der vordefinierten Eigenschaftstypen gehören, die FreeCAD anbietet und werden im Eigenschaften Ansichtsfenster angezeigt, damit sie vom Benutzer bearbeitet werden können. Auf diese Weise sind FeaturePython-Objekte wirklich und vollständig parametrisch. Du kannst Eigenschaften für das Objekt und sein Ansichtsobjekt getrennt definieren.



## Grundlegendes Beispiel 

Das folgende Beispiel ist zusammen mit einigen anderen Beispielen in der Datei [src/Mod/TemplatePyMod/FeaturePython.py](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/TemplatePyMod/FeaturePython.py) zu finden:


```python
'''Examples for a feature class and its view provider.'''

import FreeCAD, FreeCADGui
from pivy import coin

class Box:
    def __init__(self, obj):
        '''Add some custom properties to our box feature'''
        obj.addProperty("App::PropertyLength", "Length", "Box", "Length of the box").Length = 1.0
        obj.addProperty("App::PropertyLength", "Width", "Box", "Width of the box").Width = 1.0
        obj.addProperty("App::PropertyLength", "Height", "Box", "Height of the box").Height = 1.0
        obj.Proxy = self

    def onChanged(self, fp, prop):
        '''Do something when a property has changed'''
        FreeCAD.Console.PrintMessage("Change property: " + str(prop) + "\n")

    def execute(self, fp):
        '''Do something when doing a recomputation, this method is mandatory'''
        FreeCAD.Console.PrintMessage("Recompute Python Box feature\n")

class ViewProviderBox:
    def __init__(self, obj):
        '''Set this object to the proxy object of the actual view provider'''
        obj.addProperty("App::PropertyColor","Color", "Box", "Color of the box").Color = (1.0, 0.0, 0.0)
        obj.Proxy = self

    def attach(self, obj):
        '''Setup the scene sub-graph of the view provider, this method is mandatory'''
        self.shaded = coin.SoGroup()
        self.wireframe = coin.SoGroup()
        self.scale = coin.SoScale()
        self.color = coin.SoBaseColor()

        data=coin.SoCube()
        self.shaded.addChild(self.scale)
        self.shaded.addChild(self.color)
        self.shaded.addChild(data)
        obj.addDisplayMode(self.shaded, "Shaded");
        style=coin.SoDrawStyle()
        style.style = coin.SoDrawStyle.LINES
        self.wireframe.addChild(style)
        self.wireframe.addChild(self.scale)
        self.wireframe.addChild(self.color)
        self.wireframe.addChild(data)
        obj.addDisplayMode(self.wireframe, "Wireframe");
        self.onChanged(obj,"Color")

    def updateData(self, fp, prop):
        '''If a property of the handled feature has changed we have the chance to handle this here'''
        # fp is the handled feature, prop is the name of the property that has changed
        l = fp.getPropertyByName("Length")
        w = fp.getPropertyByName("Width")
        h = fp.getPropertyByName("Height")
        self.scale.scaleFactor.setValue(float(l), float(w), float(h))
        pass

    def getDisplayModes(self,obj):
        '''Return a list of display modes.'''
        modes=[]
        modes.append("Shaded")
        modes.append("Wireframe")
        return modes

    def getDefaultDisplayMode(self):
        '''Return the name of the default display mode. It must be defined in getDisplayModes.'''
        return "Shaded"

    def setDisplayMode(self,mode):
        '''Map the display mode defined in attach with those defined in getDisplayModes.\
                Since they have the same names nothing needs to be done. This method is optional'''
        return mode

    def onChanged(self, vp, prop):
        '''Here we can do something when a single property got changed'''
        FreeCAD.Console.PrintMessage("Change property: " + str(prop) + "\n")
        if prop == "Color":
            c = vp.getPropertyByName("Color")
            self.color.rgb.setValue(c[0], c[1], c[2])

    def getIcon(self):
        '''Return the icon in XPM format which will appear in the tree view. This method is\
                optional and if not defined a default icon is shown.'''
        return """
            /* XPM */
            static const char * ViewProviderBox_xpm[] = {
            "16 16 6 1",
            "   c None",
            ".  c #141010",
            "+  c #615BD2",
            "@  c #C39D55",
            "#  c #000000",
            "$  c #57C355",
            "        ........",
            "   ......++..+..",
            "   .@@@@.++..++.",
            "   .@@@@.++..++.",
            "   .@@  .++++++.",
            "  ..@@  .++..++.",
            "###@@@@ .++..++.",
            "##$.@@$#.++++++.",
            "#$#$.$$$........",
            "#$$#######      ",
            "#$$#$$$$$#      ",
            "#$$#$$$$$#      ",
            "#$$#$$$$$#      ",
            " #$#$$$$$#      ",
            "  ##$$$$$#      ",
            "   #######      "};
            """

    def dumps(self):
        '''When saving the document this object gets stored using Python's json module.\
                Since we have some un-serializable parts here -- the Coin stuff -- we must define this method\
                to return a tuple of all serializable objects or None.'''
        return None

    def loads(self,state):
        '''When restoring the serialized object from document we have the chance to set some internals here.\
                Since no data were serialized nothing needs to be done here.'''
        return None

def makeBox():
    FreeCAD.newDocument()
    a=FreeCAD.ActiveDocument.addObject("App::FeaturePython", "Box")
    Box(a)
    ViewProviderBox(a.ViewObject)

makeBox()
```



### Beachtenswertes

Wenn sich dein Objekt darauf verläßt, das es sobald es erzeugt wird neu berechnet wird, dann muss man das sofern es nicht automatisch gemacht wird in der Funktion `__init__` durchführen. In diesem Beispiel wird das nicht benötigt weil die `onChanged` Methode der Klasse `Box` den gleichen Effekt wie die Funktion `execute` hat, aber das untere Beispiel verläßt sich darauf, dass neu berechnet wird bevor irgend etwas in der 3D Ansicht angezeigt wird. In den Beispielen wird dies von Hand mit `ActiveDocument.recompute()` durchgeführt, aber in komplexeren Szenarios muss man entscheiden wo entweder das gesamte Dokument oder das FeaturePython Objekt neu berechnet wird.

Dieses Beispiel erzeugt einige Fehlermeldungen im report view Fenster. Dies erfolgt weil die Methode `onChanged` der Klasse `Box` jedes mal aufgerufen wird, wenn eine property in der Methode `__init__` hinzugefügt wird. Wenn die Erste hinzugefügt wird gibt es die properties Width und Height noch nicht, deshalb schlägt der Versuch auf diese zuzugreifen fehl.

Eine Erklärung zu `__getstate__` und `__setstate__`, die durch `dumps` und `loads` ersetzt wurden, befindet sich im Forumsbeitrag [obj.Proxy.Type is a dict, not a string](https://forum.freecad.org/viewtopic.php?f=18&t=44009&start=10#p377892).


`obj.addProperty(...)`

gibt `obj`, zurück, sodass der Wert der property in der gleichen Zeile gesetzt werden kann:


```python
obj.addProperty("App::PropertyLength", "Length", "Box", "Length of the box").Length = 1.0
```

Was Gleichwertig ist zu:


```python
obj.addProperty("App::PropertyLength", "Length", "Box", "Length of the box")
obj.Length = 1.0
```



## Andere komplexere Beispiele 

Dieses Beispiel verwendet das [Part-Modul](Part_Workbench/de.md), um ein Oktaeder zu erstellen und dann seine Coin-Darstellung mit pivy.

Das Erste ist das Documentobjekt selbst:


```python
import FreeCAD, FreeCADGui, Part
import pivy
from pivy import coin

class Octahedron:
  def __init__(self, obj):
     "Add some custom properties to our box feature"
     obj.addProperty("App::PropertyLength","Length","Octahedron","Length of the octahedron").Length=1.0
     obj.addProperty("App::PropertyLength","Width","Octahedron","Width of the octahedron").Width=1.0
     obj.addProperty("App::PropertyLength","Height","Octahedron", "Height of the octahedron").Height=1.0
     obj.addProperty("Part::PropertyPartShape","Shape","Octahedron", "Shape of the octahedron")
     obj.Proxy = self

  def execute(self, fp):
     # Define six vetices for the shape
     v1 = FreeCAD.Vector(0,0,0)
     v2 = FreeCAD.Vector(fp.Length,0,0)
     v3 = FreeCAD.Vector(0,fp.Width,0)
     v4 = FreeCAD.Vector(fp.Length,fp.Width,0)
     v5 = FreeCAD.Vector(fp.Length/2,fp.Width/2,fp.Height/2)
     v6 = FreeCAD.Vector(fp.Length/2,fp.Width/2,-fp.Height/2)

     # Make the wires/faces
     f1 = self.make_face(v1,v2,v5)
     f2 = self.make_face(v2,v4,v5)
     f3 = self.make_face(v4,v3,v5)
     f4 = self.make_face(v3,v1,v5)
     f5 = self.make_face(v2,v1,v6)
     f6 = self.make_face(v4,v2,v6)
     f7 = self.make_face(v3,v4,v6)
     f8 = self.make_face(v1,v3,v6)
     shell=Part.makeShell([f1,f2,f3,f4,f5,f6,f7,f8])
     solid=Part.makeSolid(shell)
     fp.Shape = solid

  # helper mehod to create the faces
  def make_face(self,v1,v2,v3):
     wire = Part.makePolygon([v1,v2,v3,v1])
     face = Part.Face(wire)
     return face
```

Dann haben wir das View Provider Objekt, das für die Darstellung des Objekts in der 3D Szene verantwortlich ist:


```python
class ViewProviderOctahedron:
  def __init__(self, obj):
     "Set this object to the proxy object of the actual view provider"
     obj.addProperty("App::PropertyColor","Color","Octahedron","Color of the octahedron").Color=(1.0,0.0,0.0)
     obj.Proxy = self

  def attach(self, obj):
     "Setup the scene sub-graph of the view provider, this method is mandatory"
     self.shaded = coin.SoGroup()
     self.wireframe = coin.SoGroup()
     self.scale = coin.SoScale()
     self.color = coin.SoBaseColor()

     self.data=coin.SoCoordinate3()
     self.face=coin.SoIndexedFaceSet()

     self.shaded.addChild(self.scale)
     self.shaded.addChild(self.color)
     self.shaded.addChild(self.data)
     self.shaded.addChild(self.face)
     obj.addDisplayMode(self.shaded,"Shaded");
     style=coin.SoDrawStyle()
     style.style = coin.SoDrawStyle.LINES
     self.wireframe.addChild(style)
     self.wireframe.addChild(self.scale)
     self.wireframe.addChild(self.color)
     self.wireframe.addChild(self.data)
     self.wireframe.addChild(self.face)
     obj.addDisplayMode(self.wireframe,"Wireframe");
     self.onChanged(obj,"Color")

  def updateData(self, fp, prop):
     "If a property of the handled feature has changed we have the chance to handle this here"
     # fp is the handled feature, prop is the name of the property that has changed
     if prop == "Shape":
        s = fp.getPropertyByName("Shape")
        self.data.point.setNum(6)
        cnt=0
        for i in s.Vertexes:
           self.data.point.set1Value(cnt,i.X,i.Y,i.Z)
           cnt=cnt+1

        self.face.coordIndex.set1Value(0,0)
        self.face.coordIndex.set1Value(1,1)
        self.face.coordIndex.set1Value(2,2)
        self.face.coordIndex.set1Value(3,-1)

        self.face.coordIndex.set1Value(4,1)
        self.face.coordIndex.set1Value(5,3)
        self.face.coordIndex.set1Value(6,2)
        self.face.coordIndex.set1Value(7,-1)

        self.face.coordIndex.set1Value(8,3)
        self.face.coordIndex.set1Value(9,4)
        self.face.coordIndex.set1Value(10,2)
        self.face.coordIndex.set1Value(11,-1)

        self.face.coordIndex.set1Value(12,4)
        self.face.coordIndex.set1Value(13,0)
        self.face.coordIndex.set1Value(14,2)
        self.face.coordIndex.set1Value(15,-1)

        self.face.coordIndex.set1Value(16,1)
        self.face.coordIndex.set1Value(17,0)
        self.face.coordIndex.set1Value(18,5)
        self.face.coordIndex.set1Value(19,-1)

        self.face.coordIndex.set1Value(20,3)
        self.face.coordIndex.set1Value(21,1)
        self.face.coordIndex.set1Value(22,5)
        self.face.coordIndex.set1Value(23,-1)

        self.face.coordIndex.set1Value(24,4)
        self.face.coordIndex.set1Value(25,3)
        self.face.coordIndex.set1Value(26,5)
        self.face.coordIndex.set1Value(27,-1)

        self.face.coordIndex.set1Value(28,0)
        self.face.coordIndex.set1Value(29,4)
        self.face.coordIndex.set1Value(30,5)
        self.face.coordIndex.set1Value(31,-1)

  def getDisplayModes(self,obj):
     "Return a list of display modes."
     modes=[]
     modes.append("Shaded")
     modes.append("Wireframe")
     return modes

  def getDefaultDisplayMode(self):
     "Return the name of the default display mode. It must be defined in getDisplayModes."
     return "Shaded"

  def setDisplayMode(self,mode):
     return mode

  def onChanged(self, vp, prop):
     "Here we can do something when a single property got changed"
     FreeCAD.Console.PrintMessage("Change property: " + str(prop) + "\n")
     if prop == "Color":
        c = vp.getPropertyByName("Color")
        self.color.rgb.setValue(c[0],c[1],c[2])

  def getIcon(self):
     return """
        /* XPM */
        static const char * ViewProviderBox_xpm[] = {
        "16 16 6 1",
        "    c None",
        ".   c #141010",
        "+   c #615BD2",
        "@   c #C39D55",
        "#   c #000000",
        "$   c #57C355",
        "        ........",
        "   ......++..+..",
        "   .@@@@.++..++.",
        "   .@@@@.++..++.",
        "   .@@  .++++++.",
        "  ..@@  .++..++.",
        "###@@@@ .++..++.",
        "##$.@@$#.++++++.",
        "#$#$.$$$........",
        "#$$#######      ",
        "#$$#$$$$$#      ",
        "#$$#$$$$$#      ",
        "#$$#$$$$$#      ",
        " #$#$$$$$#      ",
        "  ##$$$$$#      ",
        "   #######      "};
        """

  def dumps(self):
     return None

  def loads(self,state):
     return None
```

Schließlich, sobald unser Objekt und sein Viewobjekt definiert sind, müssen wir sie nur noch aufrufen (Der Code der Octahedron Klasse und der Viewprovider Klasse könnte direkt in die FreeCAD Python Konsole kopiert werden):


```python
FreeCAD.newDocument()
a=FreeCAD.ActiveDocument.addObject("App::FeaturePython","Octahedron")
Octahedron(a)
ViewProviderOctahedron(a.ViewObject)
```



## Objekte auswählbar machen 

Wenn du dein Objekt oder zumindest einen Teil davon durch Anklicken im Ansichtsfenster auswählbar machen möchtest, musst du seine Coin-Geometrie in einen SoFCSelection-Knoten aufnehmen. Wenn dein Objekt eine komplexe Darstellung hat, mit Widgets, Anmerkungen usw., möchtest du vielleicht nur einen Teil davon in eine SoFCSelection einschließen. Alles, was eine SoFCSelection ist, wird von FreeCAD ständig gescannt, um Auswahl/Vorwahl zu erkennen, daher ist es sinnvoll, es nicht mit unnötigem Scannen zu überlasten.

Sobald jene Teile des Scenegraph die auswählbar sein sollen sich in den SoFCSelection Knoten befinden, müssen zwei Methoden bereit gestellt werden, um den Auswahlpfad zu bearbeiten. Der Auswahlpfad kann als ein String mit den Namen jedes Elementes im Pfad, oder als ein Array aus Szenegraph Objekten aufscheinen. Die beiden Methoden welche bereitgestellt werden müssen sind `getDetailPath` welche einen String Pfad in ein Array aus Szenegraph Objekten umwandelt, und `getElementPicked` welches ein im Szenegraph angeklicktes Element nimmt, und seinen Namen als String zurückgibt (Hinweis, nicht seinen Pfad als String).

Hier ist das obige Molekülbeispiel, angepasst, um die Elemente des Moleküls auswählbar zu machen:


```python
class Molecule:
    def __init__(self, obj):
        ''' Add two point properties '''
        obj.addProperty("App::PropertyVector","p1","Line","Start point")
        obj.addProperty("App::PropertyVector","p2","Line","End point").p2=FreeCAD.Vector(5,0,0)

        obj.Proxy = self

    def onChanged(self, fp, prop):
        if prop == "p1" or prop == "p2":
            ''' Print the name of the property that has changed '''
            fp.Shape = Part.makeLine(fp.p1,fp.p2)

    def execute(self, fp):
        ''' Print a short message when doing a recomputation, this method is mandatory '''
        fp.Shape = Part.makeLine(fp.p1,fp.p2)

class ViewProviderMolecule:
    def __init__(self, obj):
        ''' Set this object to the proxy object of the actual view provider '''
        obj.Proxy = self
        self.ViewObject = obj
        sep1=coin.SoSeparator()
        sel1 = coin.SoType.fromName('SoFCSelection').createInstance()
        # sel1.policy.setValue(coin.SoSelection.SHIFT)
        sel1.ref()
        sep1.addChild(sel1)
        self.trl1=coin.SoTranslation()
        sel1.addChild(self.trl1)
        sel1.addChild(coin.SoSphere())
        sep2=coin.SoSeparator()
        sel2 = coin.SoType.fromName('SoFCSelection').createInstance()
        sel2.ref()
        sep2.addChild(sel2)
        self.trl2=coin.SoTranslation()
        sel2.addChild(self.trl2)
        sel2.addChild(coin.SoSphere())
        obj.RootNode.addChild(sep1)
        obj.RootNode.addChild(sep2)
        self.updateData(obj.Object, 'p2')
        self.sel1 = sel1
        self.sel2 = sel2

    def getDetailPath(self, subname, path, append):
        vobj = self.ViewObject
        if append:
            path.append(vobj.RootNode)
            path.append(vobj.SwitchNode)

            mode = vobj.SwitchNode.whichChild.getValue()
            if mode >= 0:
                mode = vobj.SwitchNode.getChild(mode)
                path.append(mode)
                sub = Part.splitSubname(subname)[-1]
                if sub == 'Atom1':
                    path.append(self.sel1)
                elif sub == 'Atom2':
                    path.append(self.sel2)
                else:
                    path.append(mode.getChild(0))
        return True

    def getElementPicked(self, pp):
        path = pp.getPath()
        if path.findNode(self.sel1) >= 0:
            return 'Atom1'
        if path.findNode(self.sel2) >= 0:
            return 'Atom2'
        raise NotImplementedError

    def updateData(self, fp, prop):
        "If a property of the handled feature has changed we have the chance to handle this here"
        # fp is the handled feature, prop is the name of the property that has changed
        if prop == "p1":
            p = fp.getPropertyByName("p1")
            self.trl1.translation=(p.x,p.y,p.z)
        elif prop == "p2":
            p = fp.getPropertyByName("p2")
            self.trl2.translation=(p.x,p.y,p.z)

    def dumps(self):
        return None

    def loads(self,state):
        return None

def makeMolecule():
    FreeCAD.newDocument()
    a=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","Molecule")
    Molecule(a)
    ViewProviderMolecule(a.ViewObject)
    FreeCAD.ActiveDocument.recompute()
```



## Arbeiten mit einfachen Shapes 

Wenn ein parametrisches Objekt einfach nur eine Form ausgibt, muss man keine View-Provider-Objekt verwenden. Die Form wird mit FreeCADs Standard-Form-Darstellung angezeigt.


```python
import FreeCAD as App
import FreeCADGui
import FreeCAD
import Part
class Line:
    def __init__(self, obj):
        '''"App two point properties" '''
        obj.addProperty("App::PropertyVector","p1","Line","Start point")
        obj.addProperty("App::PropertyVector","p2","Line","End point").p2=FreeCAD.Vector(1,0,0)
        obj.Proxy = self

    def execute(self, fp):
        '''"Print a short message when doing a recomputation, this method is mandatory" '''
        fp.Shape = Part.makeLine(fp.p1,fp.p2)

a=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","Line")
Line(a)
a.ViewObject.Proxy=0 # just set it to something different from None (this assignment is needed to run an internal notification)
FreeCAD.ActiveDocument.recompute()
```

Gleicher Code unter Verwendung von **ViewProviderLine**


```python
import FreeCAD as App
import FreeCADGui
import FreeCAD
import Part

class Line:
    def __init__(self, obj):
         '''"App two point properties" '''
         obj.addProperty("App::PropertyVector","p1","Line","Start point")
         obj.addProperty("App::PropertyVector","p2","Line","End point").p2=FreeCAD.Vector(100,0,0)
         obj.Proxy = self

    def execute(self, fp):
        '''"Print a short message when doing a recomputation, this method is mandatory" '''
        fp.Shape = Part.makeLine(fp.p1,fp.p2)

class ViewProviderLine:
   def __init__(self, obj):
      ''' Set this object to the proxy object of the actual view provider '''
      obj.Proxy = self

   def getDefaultDisplayMode(self):
      ''' Return the name of the default display mode. It must be defined in getDisplayModes. '''
      return "Flat Lines"

a=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","Line")
Line(a)
ViewProviderLine(a.ViewObject)
App.ActiveDocument.recompute()
```



## Struktur des Szenegraph 

Du hast vielleicht bemerkt, dass die obigen Beispiele deine Szenengraphen auf leicht unterschiedliche Weise aufbauen. Einige verwenden `obj.addDisplayMode(node, "modename")`, während andere `obj.SwitchNode.getChild(x).addChild(y)` verwenden.

Jedes Feature in einem FreeCAD Dokument basiert auf der folgenden Struktur des Szenegraph:


```python
RootNode
 \- SwitchNode
     \- Shaded
      - Wireframe
      - etc
```

The `SwitchNode` displays only one of its children, depending on which display mode is selection in FreeCAD.

Die Beispiele welche `addDisplayMode` verwenden bilden ihre Szenegraphen ausschließlich aus coin3d Szenegraph Elementen. Im Hintergrund fügt `addDisplayMode` ein neues Kind zum `SwitchNode`; der Name dieses Knotens stimmt mit dem durchgeführten display mode überein.

Die Beispiele die `SwitchNode.getChild(x).addChild` verwenden bilden Teile ihrer Geometrie durch Verwenden von Funktionen des Workbench Part, wie etwa `1=fp.Shape = Part.makeLine(fp.p1,fp.p2)`. Dies erstellt verschiedene Ausgabemodi des Szenegraph unter dem `SwitchNode`; wenn wir später coin3d Elemente zum Szenegraph hinzufügen müssen wir sie zum vorhandenen Ausgabemodus des Szenegraphen eher durch Verwenden von `addChild` als durch Erzeugen eines neuen Kindes des `SwitchNode` hinzufügen.

Bei Verwendung von `addDisplayMode()` zum Hinzufügen von Geometrie zum Szenegraph, sollte jeder Ausgabemodus seinen eigenen Knoten haben, der an `addDisplayMode()` übergeben wird; verwende nicht den Gleichen Knoten dafür. Wenn man das macht wird der Auswahlmechanismus verwirrt. Es ist in Ordnung, wenn jeder Knoten eines Ausgabemodus weiter unten die gleichen Geometrieknoten angefügt hat, nur die Wurzel jedes Ausgabemodus muss eindeutig sein.

Hier das obige Molekül Beispiel, angepasst so dass im Szenegraph nur Coin3D Objekte an Stelle von Objekten des Workbench Part gezeichnet werden:


```python
import Part
from pivy import coin

class Molecule:
    def __init__(self, obj):
        ''' Add two point properties '''
        obj.addProperty("App::PropertyVector","p1","Line","Start point")
        obj.addProperty("App::PropertyVector","p2","Line","End point").p2=FreeCAD.Vector(5,0,0)

        obj.Proxy = self

    def onChanged(self, fp, prop):
        pass

    def execute(self, fp):
        ''' Print a short message when doing a recomputation, this method is mandatory '''
        pass

class ViewProviderMolecule:
    def __init__(self, obj):
        ''' Set this object to the proxy object of the actual view provider '''
        self.constructed = False
        obj.Proxy = self
        self.ViewObject = obj

    def attach(self, obj):
        material = coin.SoMaterial()
        material.diffuseColor = (1.0, 0.0, 0.0)
        material.emissiveColor = (1.0, 0.0, 0.0)
        drawStyle = coin.SoDrawStyle()
        drawStyle.pointSize.setValue(10)
        drawStyle.style = coin.SoDrawStyle.LINES
        wireframe = coin.SoGroup()
        shaded = coin.SoGroup()
        self.wireframe = wireframe
        self.shaded = shaded

        self.coords = coin.SoCoordinate3()
        self.coords.point.setValues(0, 2, [FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(1, 0, 0)])
        wireframe += self.coords
        wireframe += drawStyle
        wireframe += material
        shaded += self.coords
        shaded += drawStyle
        shaded += material

        g = coin.SoGroup()
        sel1 = coin.SoType.fromName('SoFCSelection').createInstance()
        sel1.style = 'EMISSIVE_DIFFUSE'
        p1 = coin.SoType.fromName('SoIndexedPointSet').createInstance()
        p1.coordIndex.set1Value(0, 0)
        sel1 += p1
        g += sel1
        wireframe += g
        shaded += g

        g = coin.SoGroup()
        sel2 = coin.SoType.fromName('SoFCSelection').createInstance()
        sel2.style = 'EMISSIVE_DIFFUSE'
        p2 = coin.SoType.fromName('SoIndexedPointSet').createInstance()
        p2.coordIndex.set1Value(0, 1)
        sel2 += p2
        g += sel2
        wireframe += g
        shaded += g

        g = coin.SoGroup()
        sel3 = coin.SoType.fromName('SoFCSelection').createInstance()
        sel3.style = 'EMISSIVE_DIFFUSE'
        p3 = coin.SoType.fromName('SoIndexedLineSet').createInstance()
        p3.coordIndex.setValues(0, 2, [0, 1])
        sel3 += p3
        g += sel3
        wireframe += g
        shaded += g

        obj.addDisplayMode(wireframe, 'Wireframe')
        obj.addDisplayMode(shaded, 'Shaded')

        self.sel1 = sel1
        self.sel2 = sel2
        self.sel3 = sel3
        self.constructed = True
        self.updateData(obj.Object, 'p2')

    def getDetailPath(self, subname, path, append):
        vobj = self.ViewObject
        if append:
            path.append(vobj.RootNode)
            path.append(vobj.SwitchNode)

            mode = vobj.SwitchNode.whichChild.getValue()
            FreeCAD.Console.PrintWarning("getDetailPath: mode {} is active\n".format(mode))
            if mode >= 0:
                mode = vobj.SwitchNode.getChild(mode)
                path.append(mode)
                sub = Part.splitSubname(subname)[-1]
                print(sub)
                if sub == 'Atom1':
                    path.append(self.sel1)
                elif sub == 'Atom2':
                    path.append(self.sel2)
                elif sub == 'Line':
                    path.append(self.sel3)
                else:
                    path.append(mode.getChild(0))
        return True

    def getElementPicked(self, pp):
        path = pp.getPath()
        if path.findNode(self.sel1) >= 0:
            return 'Atom1'
        if path.findNode(self.sel2) >= 0:
            return 'Atom2'
        if path.findNode(self.sel3) >= 0:
            return 'Line'
        raise NotImplementedError

    def updateData(self, fp, prop):
        "If a property of the handled feature has changed we have the chance to handle this here"
        # fp is the handled feature, prop is the name of the property that has changed
        if not self.constructed:
            return
        if prop == "p1":
            p = fp.getPropertyByName("p1")
            self.coords.point.set1Value(0, p)
        elif prop == "p2":
            p = fp.getPropertyByName("p2")
            self.coords.point.set1Value(1, p)

    def getDisplayModes(self, obj):
        return ['Wireframe', 'Shaded']

    def getDefaultDisplayMode(self):
        return 'Shaded'

    def setDisplayMode(self, mode):
        return mode

    def dumps(self):
        return None

    def loads(self,state):
        return None

def makeMolecule():
    FreeCAD.newDocument()
    a=FreeCAD.ActiveDocument.addObject("App::FeaturePython","Molecule")
    Molecule(a)
    b=ViewProviderMolecule(a.ViewObject)
    a.touch()
    FreeCAD.ActiveDocument.recompute()
    return a,b

a,b = makeMolecule()
```



## In Part Design erzeugte Objekte 

Wenn Skript basierte Objekte in Part Design erzeugt werden, dann ist die Vorgangsweise ähnlich wie bei den oben besprochenen Skript basierten Objekten, aber mit wenigen zusätzlichen Überlegungen. Wir müssen zwei Gebilde Eigenschaften behandeln, eine für das Gebilde das wir in der 3D Ansicht sehen, und eine andere für das Gebilde dass von den Muster Werkzeugen, wie etwa polares Mustern verwendet wird. Die Objekt Gebilde müssen auch an an jedes vorhandene Material dass sich schon im Körper befindet (oder abgetrennt im Fall von Subtrahierten Features) angefügt werden.

Skript basierte Festkörper Objekte in Part Design sollten eher auf PartDesign::FeaturePython, PartDesign::FeatureAdditivePython, oder PartDesign::FeatureSubtractivePython als auf Part::FeaturePython basieren. Nur Addierte and Subtrahierte Varianten können in Muster Werkzeugen verwendet werden, und auf Part::FeaturePython basierende nur dann wenn der User das Object in einen Part Design Körper einfügt und es ein BaseFeature wird, welches eher als Body denn als native Part Design Objekt behandelt wird. Hinweis: es wird erwartet, dass alle Objekte Solids sind. Ein nicht Solid Feature sollte auf Part::FeaturePython aufbauen, sonst versucht das nächste Feature im Modellbaum es mit einem Solid zu verbinden und scheitert.

Hier ist ein einfaches Beispiel das eine Rohr Grundform erzeugt, ähnlich zur Rohr Grundform im Workbench Part, außer dass ein Part Design Solid Feature Objekt erzeugt wird. Wir verwenden zwei getrennte Dateien: pdtube.FCMacro und pdtube.py. Die .FCMacro Datei wird um das Objekt zu erzeugen vom User ausgeführt. Die .py Datei enthält die Definitionen der Klassen die vom .FCMacro importiert werden. Dies wird so gemacht, um die parametrische Natur des Objektes nach einem Neustart von FreeCAD und Öffnen des Dokumentes das eines unserer Rohre enthält zu unterstützen.

Zuerst die Datei welche die Klassen definiert:


```python
# -*- coding: utf-8 -*-
#classes should go in pdtube.py
import FreeCAD, FreeCADGui, Part
class PDTube:
    def __init__(self,obj):
        obj.addProperty("App::PropertyLength","Radius1","Tube","Radius1").Radius1 = 5
        obj.addProperty("App::PropertyLength","Radius2","Tube","Radius2").Radius2 = 10
        obj.addProperty("App::PropertyLength","Height","Tube","Height of tube").Height = 10
        self.makeAttachable(obj)
        obj.Proxy = self

    def makeAttachable(self, obj):

        if int(FreeCAD.Version()[1]) >= 19:
            obj.addExtension('Part::AttachExtensionPython')
        else:
            obj.addExtension('Part::AttachExtensionPython', obj)

        obj.setEditorMode('Placement', 0) #non-readonly non-hidden

    def execute(self,fp):
        outer_cylinder = Part.makeCylinder(fp.Radius2, fp.Height)
        inner_cylinder = Part.makeCylinder(fp.Radius1, fp.Height)
        if fp.Radius1 == fp.Radius2: #just make cylinder
            tube_shape = outer_cylinder
        elif fp.Radius1 < fp.Radius2:
            tube_shape = outer_cylinder.cut(inner_cylinder)
        else: #invert rather than error out
            tube_shape = inner_cylinder.cut(outer_cylinder)

        if not hasattr(fp, "positionBySupport"):
            self.makeAttachable(fp)
        fp.positionBySupport()
        tube_shape.Placement = fp.Placement

        #BaseFeature (shape property of type Part::PropertyPartShape) is provided for us
        #with the PartDesign::FeaturePython and related classes, but it might be empty
        #if our object is the first object in the tree.  it's a good idea to check
        #for its existence in case we want to make type Part::FeaturePython, which won't have it

        if hasattr(fp, "BaseFeature") and fp.BaseFeature != None:
            if "Subtractive" in fp.TypeId:
                full_shape = fp.BaseFeature.Shape.cut(tube_shape)
            else:
                full_shape = fp.BaseFeature.Shape.fuse(tube_shape)
            full_shape.transformShape(fp.Placement.inverse().toMatrix(), True) #borrowed from gears workbench
            fp.Shape = full_shape
        else:
            fp.Shape = tube_shape
        if hasattr(fp,"AddSubShape"): #PartDesign::FeatureAdditivePython and
                                      #PartDesign::FeatureSubtractivePython have this
                                      #property but PartDesign::FeaturePython does not
                                      #It is the shape used for copying in pattern features
                                      #for example in making a polar pattern
            tube_shape.transformShape(fp.Placement.inverse().toMatrix(), True)
            fp.AddSubShape = tube_shape

class PDTubeVP:
    def __init__(self, obj):
        '''Set this object to the proxy object of the actual view provider'''
        obj.Proxy = self

    def attach(self,vobj):
        self.vobj = vobj

    def updateData(self, fp, prop):
        '''If a property of the handled feature has changed we have the chance to handle this here'''
        pass

    def getDisplayModes(self,obj):
        '''Return a list of display modes.'''
        modes=[]
        modes.append("Flat Lines")
        modes.append("Shaded")
        modes.append("Wireframe")
        return modes

    def getDefaultDisplayMode(self):
        '''Return the name of the default display mode. It must be defined in getDisplayModes.'''
        return "Flat Lines"

    def setDisplayMode(self,mode):
        '''Map the display mode defined in attach with those defined in getDisplayModes.\
                Since they have the same names nothing needs to be done. This method is optional'''
        return mode

    def onChanged(self, vp, prop):
        '''Here we can do something when a single property got changed'''
        #FreeCAD.Console.PrintMessage("Change property: " + str(prop) + "\n")
        pass

    def getIcon(self):
        '''Return the icon in XPM format which will appear in the tree view. This method is\
                optional and if not defined a default icon is shown.'''
        return """
            /* XPM */
            static const char * ViewProviderBox_xpm[] = {
            "16 16 6 1",
            "   c None",
            ".  c #141010",
            "+  c #615BD2",
            "@  c #C39D55",
            "#  c #000000",
            "$  c #57C355",
            "        ........",
            "   ......++..+..",
            "   .@@@@.++..++.",
            "   .@@@@.++..++.",
            "   .@@  .++++++.",
            "  ..@@  .++..++.",
            "###@@@@ .++..++.",
            "##$.@@$#.++++++.",
            "#$#$.$$$........",
            "#$$#######      ",
            "#$$#$$$$$#      ",
            "#$$#$$$$$#      ",
            "#$$#$$$$$#      ",
            " #$#$$$$$#      ",
            "  ##$$$$$#      ",
            "   #######      "};
            """

    def dumps(self):
        '''When saving the document this object gets stored using Python's json module.\
                Since we have some un-serializable parts here -- the Coin stuff -- we must define this method\
                to return a tuple of all serializable objects or None.'''
        return None

    def loads(self,state):
        '''When restoring the serialized object from document we have the chance to set some internals here.\
                Since no data were serialized nothing needs to be done here.'''
        return None
```

Und jetzt die Macro Datei um das Objekt zu erzeugen:


```python
# -*- coding: utf-8 -*-

#pdtube.FCMacro
import pdtube
#above line needed if the class definitions above are place in another file: PDTube.py
#this is needed if the tube object is to remain parametric after restarting FreeCAD and loading
#a document containing the object

body = FreeCADGui.ActiveDocument.ActiveView.getActiveObject("pdbody")
if not body:
    FreeCAD.Console.PrintError("No active body.\n")
else:
    from PySide import QtGui
    window = FreeCADGui.getMainWindow()
    items = ["Additive","Subtractive","Neither additive nor subtractive"]
    item,ok =QtGui.QInputDialog.getItem(window,"Select tube type","Select whether you want additive, subtractive, or neither:",items,0,False)
    if ok:
        if item == items[0]:
            className = "PartDesign::FeatureAdditivePython"
        elif item == items[1]:
            className = "PartDesign::FeatureSubtractivePython"
        else:
            className = "PartDesign::FeaturePython" #not usable in pattern features, such as polar pattern

        tube = FreeCAD.ActiveDocument.addObject(className,"Tube")
        pdtube.PDTube(tube)
        pdtube.PDTubeVP(tube.ViewObject)
        body.addObject(tube) #optionally we can also use body.insertObject() for placing at particular place in tree
```



## Vorhandene Objekt Typen 

Die Objekt Typen die mit `FreeCAD.ActiveDocument.addObject()` erzeugt werden können hängen von den geladenen Modulen ab. Nach dem Laden aller inneren Workbenches kann man mit `FreeCAD.ActiveDocument.supportedTypes()` eine vollständige Liste aller erhalten. Nur Objekt Typen die mit `Python` enden können in Skript Objekten verwendet werden. Diese sind hier aufgelistet (für FreeCAD v1.0):

-    `App::DocumentObjectGroupPython`
    

-    `App::FeaturePython`
    

-    `App::GeometryPython`
    

-    `App::LinkElementPython`
    

-    `App::LinkGroupPython`
    

-    `App::LinkPython`
    

-    `App::MaterialObjectPython`
    

-    `App::PlacementPython`
    

-    `Fem::ConstraintPython`
    

-    `Fem::FeaturePython`
    

-    `Fem::FemAnalysisPython`
    

-    `Fem::FemMeshObjectPython`
    

-    `Fem::FemResultObjectPython`
    

-    `Fem::FemSolverObjectPython`
    

-    `Measure::MeasurePython`
    

-    `Mesh::FeaturePython`
    

-    `Part::CustomFeaturePython`
    

-    `Part::FeaturePython`
    

-    `Part::Part2DObjectPython`
    

-    `PartDesign::FeatureAdditivePython`
    

-    `PartDesign::FeatureAddSubPython`
    

-    `PartDesign::FeaturePython`
    

-    `PartDesign::FeatureSubtractivePython`
    

-    `PartDesign::SubShapeBinderPython`
    

-    `Path::FeatureAreaPython`
    

-    `Path::FeatureAreaViewPython`
    

-    `Path::FeatureCompoundPython`
    

-    `Path::FeaturePython`
    

-    `Path::FeatureShapePython`
    

-    `Points::FeaturePython`
    

-    `Sketcher::SketchObjectPython`
    

-    `Spreadsheet::SheetPython`
    

-    `TechDraw::DrawBrokenViewPython`
    

-    `TechDraw::DrawComplexSectionPython`
    

-    `TechDraw::DrawLeaderLinePython`
    

-    `TechDraw::DrawPagePython`
    

-    `TechDraw::DrawRichAnnoPython`
    

-    `TechDraw::DrawTemplatePython`
    

-    `TechDraw::DrawTilePython`
    

-    `TechDraw::DrawTileWeldPython`
    

-    `TechDraw::DrawViewPartPython`
    

-    `TechDraw::DrawViewPython`
    

-    `TechDraw::DrawViewSectionPython`
    

-    `TechDraw::DrawViewSymbolPython`
    

-    `TechDraw::DrawWeldSymbolPython`
    



## Vorhandene Methoden 

Siehe [FeaturePython Methoden](FeaturePython_methods/de.md) für eine vollständige Referenz.



## Vorhandene Eigenschaften 

Eigenschaften sind die wahren Bausteine von FeaturePython-Objekten. Durch sie kann man mit einem Objekt interagieren und es ändern. Nach dem Erstellen eines neuen FeaturePython-Objekts in einem Dokument, kann man eine Liste der vorhandenen Eigenschaften bekommen:


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "Box")
obj.supportedProperties()
```

Siehe [FunktionsPython benutzerdefinierte Eigenschaften](FeaturePython_Custom_Properties/de.md) für einen Überblick:

Beim Hinzufügen von Eigenschaften zu benutzerdefinierten Objekten bitte folgendes beachten:

-   Nicht die Zeichen {{Incode|<}} oder {{Incode| >}} in den Beschreibungen der Eigenschaften verwenden (das würde die XML-Teile in der .FCStd-Datei auseinanderbrechen)
-   Eigenschaften werden alphabetisch in einer .FCStd-Datei gespeichert. Befindet sich eine Form (shape) in den Eigenschaften, wird jede Eigenschaft, deren Name in alphabetischen Reihenfolge nach \"Shape\" kommt, auch NACH der Form geladen, was zu seltsamen Verhaltensweisen führen kann.

Die Eigenschaften sind in der C++ header-Datei [PropertyStandard.h](https://github.com/FreeCAD/FreeCAD/blob/master/src/App/PropertyStandard.h) festgelegt.

### Property attributes 

Standardmäßig können Eigenschaften durch den Anwender geändert werden, aber es ist möglich, die Eigenschaften auf schreibgeschützt zu setzen, wenn man zum Beispiel das Ergebnis einer Methode anzeigen möchte. Es ist auch möglich, eine Eigenschaft auszublenden. Diese Attribute können festgelegt werden mit:


```python
obj.setEditorMode("MyPropertyName", mode)
```

wobei mode diese Werte annehmen kann:

0 -- Standardmodus, zum Lesen und Schreiben
1 -- Schreibgeschützt (nur zum Lesen)
2 -- Ausgeblendet
3 -- Schreibgeschützt und ausgeblendet

Die Attribute können auch durch Verwenden einer Liste von Zeichenketten festgelegt werden, z.B. `obj.setEditorMode("Placement", ["ReadOnly", "Hidden"])`.

Attribute, die mit {{Incode|setEditorMode}} gesetzt wurden, können vom Anwender entfernt werden. Siehe [Eigenschafteneditor](Property_editor/de#Kontextmenü.md). Man beachte, dass schreibgeschützte Eigenschaften mit Python (-Anweisungen) geändert werden können.

Diese und weitere Attribute können auch direkt mit der Funktion {{Incode|addProperty}} gesetzt werden. Attribute, die mit dieser Funktion gesetzt wurden, können nicht vom Anwender geändert werden. Eine interessante Möglichkeit ist es, eine Eigenschaft als Ausgabe-Eigenschaft zu kennzeichnen. Auf diese Weise werden Objekte durch FreeCAD nicht als verändert gekennzeichnet, wenn sie bearbeitet werden (dadurch ist eine Neuberechnung nicht erforderlich).

Beispiel einer Ausgabe Property (siehe auch <https://forum.freecad.org/viewtopic.php?t=24928>):


```python
obj.addProperty("App::PropertyString", "MyCustomProperty", "", "", 8)
```

The attributes that can be set with {{Incode|addProperty}} are listed below. Multiple attributes can be set by adding values.

  0 -- Prop_None, No special property attribute
  1 -- Prop_ReadOnly, Property is read-only in the editor
  2 -- Prop_Transient, Property won't be saved to file
  4 -- Prop_Hidden, Property won't appear in the editor
  8 -- Prop_Output, Modified property doesn't touch its parent container
 16 -- Prop_NoRecompute, Modified property doesn't touch its container for recompute
 32 -- Prop_NoPersist, Property won't be saved to file at all

Die Attribute der Eigenschaften sind in der [PropertyContainer C++ header-Datei](https://github.com/FreeCAD/FreeCAD/blob/master/src/App/PropertyContainer.h) festgelegt.

For {{Incode|Prop_ReadOnly}} and {{Incode|Prop_Hidden}} the {{Incode|addProperty}} function has boolean arguments as well:


```python
obj.addProperty("App::PropertyString", "MyCustomProperty", "", "", 0, True, True)
```

Which is equivalent to:


```python
obj.addProperty("App::PropertyString", "MyCustomProperty", "", "", 1+4)
```


<small>(v1.0)</small> 

: The full signature of the function is:


```python
obj.addProperty(type: string, name: string, group="", doc="", attr=0, read_only=False, hidden=False, enum_vals=[])
```

-    {{Incode|type}}: Property type.

-    {{Incode|name}}: Property name.

-    {{Incode|group}}: Property subsection (used in the [Property editor](Property_editor.md)).

-    {{Incode|doc}}: Tooltip (idem).

-    {{Incode|attr}}: Attribute, see above.

-    {{Incode|read_only}}: See above.

-    {{Incode|hidden}}: See above.

-    {{Incode|enum_vals}}: Enumeration values (list of string), only relevant if type is {{Incode|"App::PropertyEnumeration"}}.



## Vorhandene Erweiterungen 

The list of available extensions can be obtained with `grep -RI EXTENSION_PROPERTY_SOURCE_TEMPLATE` in the repository of the source code and is given here (for FreeCAD v0.21).

For objects:

-    `App::GeoFeatureGroupExtensionPython`
    

-    `App::GroupExtensionPython`
    

-    `App::LinkBaseExtensionPython`
    

-    `App::LinkExtensionPython`
    

-    `App::OriginGroupExtensionPython`
    

-    `Part::AttachExtensionPython`
    

-    `TechDraw::CosmeticExtensionPython`
    

For view objects:

-    `Gui::ViewProviderExtensionPython`
    

-    `Gui::ViewProviderGeoFeatureGroupExtensionPython`
    

-    `Gui::ViewProviderGroupExtensionPython`
    

-    `Gui::ViewProviderOriginGroupExtensionPython`
    

-    `PartGui::ViewProviderAttachExtensionPython`
    

-    `PartGui::ViewProviderSplineExtensionPython`
    

There exist other extensions but they do not work as-is:

-    `App::ExtensionPython`
    

-    `TechDrawGui::ViewProviderCosmeticExtensionPython`
    

-    `TechDrawGui::ViewProviderDrawingViewExtensionPython`
    

-    `TechDrawGui::ViewProviderPageExtensionPython`
    

-    `TechDrawGui::ViewProviderTemplateExtensionPython`
    



## Weitere Informationen 

Weitere Seiten:

-   [Skriptgesteuerte Objekte, die Attribute speichern](Scripted_objects_saving_attributes/de.md)
-   [Migration von geskripteten Objekten](Scripted_objects_migration/de.md)
-   [Geskriptete Objekte mit Anhang](Scripted_objects_with_attachment/de.md)
-   [Ansichtsanbieter](Viewprovider/de.md)

Interessante Forenbeiträge über geskriptete Objekte:

-   [Python object attributes lost at load](http://forum.freecadweb.org/viewtopic.php?f=22&t=13740)
-   [New FeaturePython is grey](http://forum.freecadweb.org/viewtopic.php?t=12139)
-   [Explanation on dumps and loads](https://forum.freecadweb.org/viewtopic.php?f=18&t=44009), [official documentation](https://docs.python.org/3/library/pickle.html#object.__getstate__)
-   [Eigenmode frequency always 0?](https://forum.freecadweb.org/viewtopic.php?f=18&t=13460&start=20#p109709)
-   [how to implement python feature\'s setEdit properly?](https://forum.freecadweb.org/viewtopic.php?f=22&t=21330)

Zusätzlich zu den hier vorgestellten Beispielen solltedz du einen Blick in den FreeCAD Quellcode [src/Mod/TemplatePyMod/FeaturePython.py](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/TemplatePyMod/FeaturePython.py) für weitere Beispiele werfen.



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Scripted objects/de
