# Scripted objects/it
## Introduzione

Oltre ai tipi di oggetti standard, come le Annotazioni, gli oggetti Mesh e gli oggetti Parte, FreeCAD offre anche la straordinaria possibilità di costruire al 100% oggetti parametrici in script di Python, chiamati [Python Features](App_FeaturePython/it.md) (*Caratteristiche* Python). Questi oggetti si comportano esattamente come un qualsiasi altro oggetto di FreeCAD, e sono salvati e ripristinati automaticamente con salva/apri il file.

Una particolarità deve essere compresa: per motivi di sicurezza, i file di FreeCAD non contengono mai alcun codice incorporato. Il codice Python che scrivi per creare oggetti parametrici non viene mai salvato all\'interno di un file. Ciò significa che se apri un file contenente tale oggetto su un\'altra macchina, e quel codice Python non è disponibile su quella macchina, l\'oggetto non verrà completamente ricreato. Se distribuisci tali oggetti ad altri, dovrai distribuire anche il tuo script Python, ad esempio come [Macro](Macros/it.md).

**Nota**: è possibile impacchettare il codice Python all\'interno di un file FreeCAD utilizzando la serializzazione json con un App::PropertyPythonObject, ma quel codice non può mai essere eseguito direttamente, e quindi ha poca utilità per il nostro scopo qui.

Le [Python Features](App_FeaturePython/it.md) seguono le stesse regole di tutte le altre funzionalità di FreeCAD: sono divise in una parte App e una parte GUI. La parte App, cioè il Document Object (oggetto del documento), definisce la geometria dell\'oggetto, mentre la sua parte grafica, cioè il View Provider Object (fornitore della vista dell\'oggetto), definisce come l\'oggetto viene disegnato sullo schermo. Il View Provider Object, come qualsiasi altro elemento di FreeCAD, è disponibile solo quando si esegue FreeCAD nella sua GUI (interfaccia grafica). Per costruire il proprio oggetto, sono disponibili diversi metodi e proprietà. La Proprietà deve essere una qualsiasi dei tipi di proprietà predefinite che FreeCAD mette a disposizione. Le proprietà disponibili sono quelle che appaiono nella finestra di visualizzazione delle proprietà per consentire all\'utente di modificarle. Con questa procedura, gli oggetti FeaturePython sono realmente e totalmente parametrici. E\' possibile definire separatamente le proprietà per l\'oggetto e per la sua ViewObject (rappresentazione).



## Esempio di base 

L\'esempio seguente si trova nel file [src/Mod/TemplatePyMod/FeaturePython.py](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/TemplatePyMod/FeaturePython.py), con molti altri esempi:


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



### Cose da notare 

Se il tuo oggetto si basa sul ricalcolo non appena viene creato, devi farlo manualmente nella funzione `__init__` poiché non viene chiamato automaticamente. Questo esempio non lo richiede, perché il metodo `onChanged` della classe `Box` ha lo stesso effetto della funzione `execute`, ma gli esempi seguenti si basano sull\'essere ricalcolati prima che qualsiasi cosa venga visualizzata nella vista 3D. Negli esempi, questo viene fatto manualmente con `ActiveDocument.recompute()`, ma in scenari più complessi devi decidere dove ricalcolare l\'intero documento o l\'oggetto FeaturePython.

Questo esempio produce una serie di analisi dello stack di eccezioni nella finestra di visualizzazione del report. Questo perché il metodo `onChanged` della classe `Box` viene chiamato ogni volta che viene aggiunta una proprietà in `__init__`. Quando viene aggiunta la prima, le proprietà Width e Height non esistono ancora e quindi il tentativo di accedervi fallisce.

Una spiegazione di `__getstate__` e `__setstate__` che sono stati sostituiti da `dumps` e `loads` è nel thread del forum [obj.Proxy.Type è un dizionario, non una stringa](https://forum.freecad.org/viewtopic.php?f=18&t=44009&start=10#p377892).


`obj.addProperty(...)`

restituisce `obj`, in modo che il valore della proprietà possa essere impostato sulla stessa riga:


```python
obj.addProperty("App::PropertyLength", "Length", "Box", "Length of the box").Length = 1.0
```

Che equivale a:


```python
obj.addProperty("App::PropertyLength", "Length", "Box", "Length of the box")
obj.Length = 1.0
```



## Un altro esempio più complesso 

In questo esempio si utilizza il Modulo [Part](Part_Workbench/it.md) per creare un ottaedro, quindi si crea la sua rappresentazione Coin con Pivy.

Prima si crea l\'oggetto del documento:


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

In seguito si crea il fornitore della vista dell\'oggetto (view provider object), responsabile di mostrare l\'oggetto nella scena 3D:


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

Infine, dopo che l\'oggetto e il suo visualizzatore sono definiti, basta solo chiamarli (La classe Octahedron e il codice della classe viewprovider possono essere copiati direttamente nella console Python di FreeCAD)::


```python
FreeCAD.newDocument()
a=FreeCAD.ActiveDocument.addObject("App::FeaturePython","Octahedron")
Octahedron(a)
ViewProviderOctahedron(a.ViewObject)
```



## Rendere gli oggetti selezionabili 

Se volete rendere il vostro oggetto selezionabile, o almeno una parte di esso, facendo clic su di esso nella finestra, è necessario includere la sua geometria Coin all\'interno di un nodo SoFCSelection. Se l\'oggetto ha una rappresentazione complessa, con widget, annotazioni, etc, si potrebbe voler includere solo una parte di esso in un SoFCSelection. Tutto quello che compone un SoFCSelection viene costantemente analizzato da FreeCAD per rilevare selezioni/preselezioni, quindi non ha senso sovraccaricarlo con delle scansioni non necessarie.

Una volta che le parti dello scenegraph, che devono essere selezionabili, si trovano all\'interno dei nodi SoFCSelection, è necessario fornire due metodi per gestire il percorso di selezione. Il percorso di selezione può assumere la forma di una stringa che fornisce i nomi di ciascun elemento nel percorso o di un array di oggetti scenegraph. I due metodi che fornisci sono `getDetailPath`, che converte da un percorso stringa in un array di oggetti scenegraph, e `getElementPicked`, che prende un elemento su cui è stato fatto clic nello scenegraph e restituisce il suo nome di stringa (nota, non il suo percorso di stringa).

Ecco l\'esempio della molecola sopra, adattato per rendere selezionabili gli elementi della molecola:


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



## Lavorare con forme semplici 

Se l\'oggetto parametrico produce semplicemente una forma, non è necessario utilizzare un fornitore di vista dell\'oggetto (view provider object). La forma viene visualizzata utilizzando la rappresentazione della forma standard di FreeCAD:


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

Lo stesso codice con l\'uso di **ViewProviderLine**


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



## Struttura di Scenegraph 

Potresti aver notato che gli esempi sopra costruiscono i loro scenegraphs in modi leggermente diversi. Alcuni usano `obj.addDisplayMode(node, "modename")` mentre altri usano `obj.SwitchNode.getChild(x).addChild(y)`.

Ogni caratteristica in un documento di FreeCAD si basa sulla seguente struttura di scenegraph:


```python
RootNode
 \- SwitchNode
     \- Shaded
      - Wireframe
      - etc
```


`SwitchNode`

mostra solo uno dei suoi figli, a seconda della modalità di visualizzazione selezionata in FreeCAD.

Gli esempi che utilizzano `addDisplayMode` stanno costruendo i loro scenegraph esclusivamente dagli elementi dello scenegraph di coin3d. Dietro le quinte, `addDisplayMode` aggiunge un nuovo figlio a `SwitchNode`; il nome di quel nodo corrisponderà alla modalità di visualizzazione, che è stata passata.

Gli esempi che utilizzano `SwitchNode.getChild(x).addChild` costruiscono anche parte della loro geometria utilizzando le funzioni dell\'ambiente Part, come `1=fp.Shape = Part.makeLine(fp.p1 ,fp.p2)`. Questo costruisce i diversi scenegraph della modalità di visualizzazione sotto `SwitchNode`; quando in seguito arriveremo ad aggiungere elementi coin3d allo scenegraph, dobbiamo aggiungerli agli scenegraph della modalità di visualizzazione esistenti usando `addChild` piuttosto che creare un nuovo figlio di `SwitchNode`.

Quando si utilizza `addDisplayMode()` per aggiungere geometria allo scenegraph, ogni modalità di visualizzazione dovrebbe avere il proprio nodo che viene passato a `addDisplayMode()`; non riutilizzare lo stesso nodo per questo. Ciò confonderà il meccanismo di selezione. Va bene se il nodo di ciascuna modalità di visualizzazione ha gli stessi nodi geometrici aggiunti sotto di esso, solo la radice di ciascuna modalità di visualizzazione deve essere distinta.

Ecco l\'esempio della molecola sopra, adattato per essere disegnato solo con oggetti scenegraph Coin3D invece di utilizzare oggetti dall\'ambiente Part:


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



## Oggetti con script di Part Design 

Quando si creano oggetti con script in Part Design, il processo è simile agli oggetti con script discussi sopra, ma con alcune considerazioni aggiuntive. Dobbiamo gestire 2 proprietà della forma, una per la forma, che vediamo nella vista 3D e un\'altra per la forma utilizzata dagli strumenti del modello, come le caratteristiche del modello polare. Le forme dell\'oggetto devono anche essere fuse con qualsiasi materiale esistente già nel Corpo (o tagliate da esso nel caso di funzioni sottrattive). E dobbiamo tenere conto della collocazione e dell\'attaccamento dei nostri oggetti in modo un po\' diverso.

Le feature di oggetti solidi con script di Part Design devono essere basate su PartDesign::FeaturePython, PartDesign::FeatureAdditivePython o PartDesign::FeatureSubtractivePython piuttosto che su Part::FeaturePython. Solo le varianti Additive e Subtractive possono essere utilizzate nelle feature di ripetizione e, se basate su Part::FeaturePython, quando l\'utente rilascia l\'oggetto in un Body di Part Design, diventa una BaseFeature invece di essere trattato dal Body come un oggetto di Part Design nativo. Nota: tutti questi dovrebbero essere solidi, quindi se stai creando una caratteristica non solida dovrebbe essere basata su Part::FeaturePython altrimenti la caratteristica successiva nell\'albero tenterà di fondersi come un solido e fallirà .

Di seguito è riportato un semplice esempio di creazione di una primitiva Tube, simile alla primitiva Tube nell\'ambiente Part, tranne per il fatto che questa sarà un oggetto feature solido di Part Design. Per questo useremo 2 file separati: pdtube.FCMacro e pdtube.py. Il file .FCMacro verrà eseguito dall\'utente per creare l\'oggetto. Il file .py conterrà le definizioni delle classi, importate da .FCMacro. Il motivo per farlo in questo modo è mantenere la natura parametrica dell\'oggetto dopo aver riavviato FreeCAD e aperto un documento contenente uno dei nostri tubi.

Innanzitutto, il file di definizione della classe:


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

E ora il file macro per creare l\'oggetto:


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



## Tipi di oggetti disponibili 

I tipi di oggetto che si possono creare con `FreeCAD.ActiveDocument.addObject()` dipendono dai moduli caricati. Dopo aver caricato tutti gli ambienti di lavoro interni è possibile ottenere un elenco completo con `FreeCAD.ActiveDocument.supportedTypes()`. Solo i tipi di oggetto con un nome che termina con `Python` possono essere utilizzati per oggetti con script. Questi sono elencati qui (per FreeCAD v1.0):

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
    



## Metodi disponibili 

Vedi [Metodi FeaturePython](FeaturePython_methods/it.md) per i riferimenti completi.



## Proprietà disponibili 

Le proprietà sono i veri elementi costitutivi degli oggetti FeaturePython. Attraverso di essi si potrà interagire e modificare il proprio oggetto. Dopo aver creato un nuovo oggetto FeaturePython nel proprio documento, è possibile ottenere un elenco delle proprietà disponibili:


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "Box")
obj.supportedProperties()
```

Vedere [Proprietà personalizzate FeaturePython](FeaturePython_Custom_Properties/it.md) per una panoramica.

Quando si aggiungono proprietà ai propri oggetti personalizzati, fare attenzione a quanto segue:

-   Non utilizzare i caratteri {{Incode|<}} o {{Incode|>}} nelle descrizioni delle proprietà (questo potrebbe danneggiare le porzioni xml nel file .FCStd).
-   Le proprietà vengono memorizzate in ordine alfabetico in un file .FCStd. Se nelle proprie proprietà è presente una forma (shape), qualsiasi proprietà il cui nome viene dopo \"Shape\" in ordine alfabetico verrà caricata DOPO la forma, il che può causare comportamenti strani.

Le proprietà sono definite nel [file di intestazione PropertyStandard C++](https://github.com/FreeCAD/FreeCAD/blob/master/src/App/PropertyStandard.h).



### Attributi della proprietà 

Per impostazione predefinita le proprietà possono essere modificate dall\'utente, ma è possibile renderle di sola lettura, ad esempio se si vuole mostrare il risultato di un metodo. È anche possibile nascondere una proprietà. Questi attributi possono essere impostati utilizzando:


```python
obj.setEditorMode("MyPropertyName", mode)
```

Dove mode può avere questi valori:

 0 -- default mode, lettura e scrittura
 1 -- solo lettura
 2 -- nascosto
 3 -- di sola lettura e nascosto

Gli attributi possono essere impostati anche utilizzando un elenco di stringhe, ad es. `obj.setEditorMode("Placement", ["ReadOnly", "Hidden"])`.

Gli attributi impostati utilizzando {{Incode|setEditorMode}} possono essere rimossi dall\'utente. Vedere [Editor delle proprietà](Property_editor/it#Context_menu.md). Tenere presente che le proprietà di sola lettura possono ancora essere modificate da Python.

E\' possibile anche impostare questi e altri attributi direttamente con la funzione {{Incode|addProperty}}. Gli attributi impostati con tale funzione non possono essere modificati dall\'utente. Una possibilità interessante è contrassegnare una proprietà come proprietà di output. In questo modo FreeCAD non contrassegnerà l\'oggetto come touched quando lo si modifica (quindi non è necessario ricalcolarlo).

Esempio di proprietà di output (vedi anche <https://forum.freecad.org/viewtopic.php?t=24928>):


```python
obj.addProperty("App::PropertyString", "MyCustomProperty", "", "", 8)
```

Gli attributi che possono essere impostati con {{Incode|addProperty}} sono elencati di seguito. È possibile impostare più attributi aggiungendo valori.

   0 -- Prop_None, nessun attributo di proprietà speciale
   1 -- Prop_ReadOnly, la proprietà è di sola lettura nell'editor
   2 -- Prop_Transient, la proprietà non verrà salvata nel file
   4 -- Prop_Hidden, la proprietà non apparirà nell'editor
   8 -- Prop_Output, la proprietà modificata non tocca il suo contenitore principale
  16 -- Prop_NoRecompute, la proprietà modificata non tocca il suo contenitore per il ricalcolo
  32 -- Prop_NoPersist, la proprietà non verrà affatto salvata nel file

Gli attributi della proprietà sono definiti nel [file di intestazione PropertyContainer C++](https://github.com/FreeCAD/FreeCAD/blob/master/src/App/PropertyContainer.h).

Per {{Incode|Prop_ReadOnly}} e {{Incode|Prop_Hidden}} anche la funzione {{Incode|addProperty}} ha argomenti booleani:


```python
obj.addProperty("App::PropertyString", "MyCustomProperty", "", "", 0, True, True)
```

Che equivale a:


```python
obj.addProperty("App::PropertyString", "MyCustomProperty", "", "", 1+4)
```


{{Version/it|1.0}}

: La firma completa della funzione è:


```python
obj.addProperty(type: string, name: string, group="", doc="", attr=0, read_only=False, hidden=False, enum_vals=[])
```

-    {{Incode|type}}: Tipo di proprietà.

-    {{Incode|name}}: Nome della proprietà.

-    {{Incode|group}}: Sottosezione della proprietà (utilizzata nell\'[Editor della proprietà](Property_editor/it.md)).

-    {{Incode|doc}}: Tooltip (idem).

-    {{Incode|attr}}: Attributo, vedere sopra.

-    {{Incode|read_only}}: Vedi sopra.

-    {{Incode|hidden}}: Vedi sopra.

-    {{Incode|enum_vals}}: Valori di enumerazione (elenco di stringhe), rilevante solo se il tipo è {{Incode|"App::PropertyEnumeration"}}.



## Estensioni disponibili 

L\'elenco delle estensioni disponibili può essere ottenuto con `grep -RI EXTENSION_PROPERTY_SOURCE_TEMPLATE` nel repository del codice sorgente ed è fornito qui (per FreeCAD v0.21).

Per gli oggetti:

-    `App::GeoFeatureGroupExtensionPython`
    

-    `App::GroupExtensionPython`
    

-    `App::LinkBaseExtensionPython`
    

-    `App::LinkExtensionPython`
    

-    `App::OriginGroupExtensionPython`
    

-    `Part::AttachExtensionPython`
    

-    `TechDraw::CosmeticExtensionPython`
    

Per la vista oggetti:

-    `Gui::ViewProviderExtensionPython`
    

-    `Gui::ViewProviderGeoFeatureGroupExtensionPython`
    

-    `Gui::ViewProviderGroupExtensionPython`
    

-    `Gui::ViewProviderOriginGroupExtensionPython`
    

-    `PartGui::ViewProviderAttachExtensionPython`
    

-    `PartGui::ViewProviderSplineExtensionPython`
    

Esistono altre estensioni ma non funzionano così come sono:

-    `App::ExtensionPython`
    

-    `TechDrawGui::ViewProviderCosmeticExtensionPython`
    

-    `TechDrawGui::ViewProviderDrawingViewExtensionPython`
    

-    `TechDrawGui::ViewProviderPageExtensionPython`
    

-    `TechDrawGui::ViewProviderTemplateExtensionPython`
    



## Ulteriori informazioni 

Pagine aggiuntive:

-   [Oggetti creati con script che salvano gli attributi](Scripted_objects_saving_attributes/it.md)
-   [Migrazione di oggetti creati con script](Scripted_objects_migration/it.md)
-   [Oggetti creati da script con parti associate](Scripted_objects_with_attachment/it.md)
-   [Viewprovider](Viewprovider/it.md)

Interessanti thread del forum sugli oggetti con script:

-   [Python object attributes lost at load](http://forum.freecadweb.org/viewtopic.php?f=22&t=13740)
-   [New FeaturePython is grey](http://forum.freecadweb.org/viewtopic.php?t=12139)
-   [Explanation on dumps and loads](https://forum.freecadweb.org/viewtopic.php?f=18&t=44009), [official documentation](https://docs.python.org/3/library/pickle.html#object.__getstate__)
-   [Eigenmode frequency always 0?](https://forum.freecadweb.org/viewtopic.php?f=18&t=13460&start=20#p109709)
-   [how to implement python feature\'s setEdit properly?](https://forum.freecadweb.org/viewtopic.php?f=22&t=21330)

Oltre agli esempi presentati qui dare un\'occhiata al codice sorgente di FreeCAD [src/Mod/TemplatePyMod/FeaturePython.py](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/TemplatePyMod/FeaturePython.py) per ulteriori esempi.



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Scripted objects/it
