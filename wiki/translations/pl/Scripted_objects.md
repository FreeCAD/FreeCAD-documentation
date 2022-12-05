# Scripted objects/pl
{{TOCright}}

## Wprowadzenie

Oprócz standardowych typów obiektów, takich jak adnotacje, siatki i obiekty części, FreeCAD oferuje również niesamowitą możliwość tworzenia obiektów parametrycznych w 100% napisanych w języku Python, zwanych [właściwościami Python](App_FeaturePython/pl.md). Obiekty te zachowują się dokładnie tak, jak każdy inny obiekt programu FreeCAD i są zapisywane i przywracane automatycznie podczas zapisywania/wczytywania pliku.

Należy pamiętać o jednej szczególnej kwestii: Ze względów bezpieczeństwa pliki FreeCAD nigdy nie zawierają żadnego osadzonego kodu. Kod Pythona, który piszesz, aby utworzyć obiekty parametryczne, nigdy nie jest zapisywany wewnątrz pliku. Oznacza to, że jeśli otworzysz plik zawierający taki obiekt na innym komputerze, to jeśli ten kod nie będzie dostępny na tym komputerze, obiekt nie zostanie w pełni odtworzony. Jeśli rozpowszechniasz takie obiekty, będziesz musiał rozpowszechnić również swój skrypt Python, na przykład jako [makrodefinicję](Macros/pl.md).

**Uwaga**: Możliwe jest spakowanie kodu Python wewnątrz pliku FreeCAD za pomocą serializacji json z obiektem App::PropertyPythonObject, ale ten kod nigdy nie może być bezpośrednio uruchomiony i dlatego jest mało przydatny w naszym przypadku.

[Funkcje Python](App_FeaturePython.md) działają według tej samej zasady, co wszystkie funkcje programu FreeCAD. Są podzielone na część aplikacji i część GUI. Część aplikacji, Obiekt Dokumentu, definiuje geometrię naszego obiektu, podczas gdy jego część GUI, Obiekt Dostawcy Widoku, definiuje sposób, w jaki obiekt będzie rysowany na ekranie. Obiekt View Provider, jak każda inna funkcja programu FreeCAD, jest dostępny tylko wtedy, gdy uruchamiamy program FreeCAD w jego własnym GUI. Istnieje kilka właściwości i metod dostępnych w celu zbudowania obiektu. Właściwości muszą należeć do jednego z predefiniowanych typów właściwości, które oferuje FreeCAD, i będą wyświetlane w oknie widoku właściwości, tak aby użytkownik mógł je edytować. W ten sposób obiekty FeaturePython są prawdziwie i całkowicie parametryczne. Możesz zdefiniować właściwości osobno dla obiektu i osobno dla jego obiektu ViewObject.

## Przykład podstawowy 

Poniższy przykład można znaleźć w pliku [FeaturePython.py](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/TemplatePyMod/FeaturePython.py), wraz z kilkoma innymi przykładami:


```python
'''Examples for a feature class and its view provider.'''

import FreeCAD, FreeCADGui
from pivy import coin

class Box:
    def __init__(self, obj):
        '''Add some custom properties to our box feature'''
        obj.addProperty("App::PropertyLength","Length","Box","Length of the box").Length=1.0
        obj.addProperty("App::PropertyLength","Width","Box","Width of the box").Width=1.0
        obj.addProperty("App::PropertyLength","Height","Box", "Height of the box").Height=1.0
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
        obj.addProperty("App::PropertyColor","Color","Box","Color of the box").Color=(1.0,0.0,0.0)
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
        obj.addDisplayMode(self.shaded,"Shaded");
        style=coin.SoDrawStyle()
        style.style = coin.SoDrawStyle.LINES
        self.wireframe.addChild(style)
        self.wireframe.addChild(self.scale)
        self.wireframe.addChild(self.color)
        self.wireframe.addChild(data)
        obj.addDisplayMode(self.wireframe,"Wireframe");
        self.onChanged(obj,"Color")

    def updateData(self, fp, prop):
        '''If a property of the handled feature has changed we have the chance to handle this here'''
        # fp is the handled feature, prop is the name of the property that has changed
        l = fp.getPropertyByName("Length")
        w = fp.getPropertyByName("Width")
        h = fp.getPropertyByName("Height")
        self.scale.scaleFactor.setValue(float(l),float(w),float(h))
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
            self.color.rgb.setValue(c[0],c[1],c[2])

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

    def __getstate__(self):
        '''When saving the document this object gets stored using Python's json module.\
                Since we have some un-serializable parts here -- the Coin stuff -- we must define this method\
                to return a tuple of all serializable objects or None.'''
        return None

    def __setstate__(self,state):
        '''When restoring the serialized object from document we have the chance to set some internals here.\
                Since no data were serialized nothing needs to be done here.'''
        return None

def makeBox():
    FreeCAD.newDocument()
    a=FreeCAD.ActiveDocument.addObject("App::FeaturePython","Box")
    Box(a)
    ViewProviderBox(a.ViewObject)

makeBox()
```

### Warto wiedzieć 

Jeśli twój obiekt wymaga ponownego obliczenia zaraz po utworzeniu, musisz to zrobić ręcznie w funkcji `__init__`, ponieważ nie jest ona wywoływana automatycznie. W tym przykładzie nie jest to wymagane, ponieważ metoda `onChanged` klasy `Box` wywołuje ten sam rezultat, co funkcja `execute`, ale w poniższych przykładach wymagane jest ponowne obliczenie, zanim cokolwiek zostanie wyświetlone w widoku 3D. W przykładach jest to wykonywane ręcznie za pomocą funkcji `ActiveDocument.recompute()`, ale w bardziej złożonych scenariuszach należy zdecydować, w którym miejscu ponownie obliczyć cały dokument lub obiekt FeaturePython.

Ten przykład powoduje powstanie wielu śladów stosu wyjątków w oknie widoku raportu. Dzieje się tak, ponieważ metoda `onChanged` klasy `Box` jest wywoływana za każdym razem, gdy w `__init__` dodawana jest jakaś właściwość. Gdy dodawana jest pierwsza właściwość, właściwości Width i Height jeszcze nie istnieją, więc próba uzyskania do nich dostępu kończy się niepowodzeniem.

Wyjaśnienie działania funkcji `__getstate__` i `__setstate__` znajduje się w wątku na forum [obj.Proxy.Type jest wartością typu dict, a nie string](https://forum.freecadweb.org/viewtopic.php?f=18&t=44009&start=10#p377892).

## Dostępne metody 

Zobacz stronę [Metody FeaturePython](FeaturePython_methods.md), aby zapoznać się z pełnym opisem.

## Dostępne własności 

Właściwości są prawdziwymi kamieniami węgielnymi obiektów FeaturePython. Dzięki nim użytkownik będzie mógł wchodzić w interakcje z obiektem i modyfikować go. Po utworzeniu nowego obiektu FeaturePython w swoim dokumencie *(obj=FreeCAD.ActiveDocument.addObject(\"App::FeaturePython\", \"Box\") )* możesz uzyskać listę dostępnych właściwości, wydając polecenie:


```python
obj.supportedProperties()
```

Pojawi się lista dostępnych właściwości, które są opisane bardziej szczegółowo na stronie [Właściwości niestandardowe funkcji Python](FeaturePython_Custom_Properties/pl.md):

-   [App::PropertyAcceleration](FeaturePython_Custom_Properties#App:_PropertyAcceleration.md)
-   [App::PropertyAngle](FeaturePython_Custom_Properties#App:_PropertyAngle.md)
-   [App::PropertyArea](FeaturePython_Custom_Properties#App:_PropertyArea.md)
-   [App::PropertyBool](FeaturePython_Custom_Properties#App:_PropertyBool.md)
-   [App::PropertyBoolList](FeaturePython_Custom_Properties#App:_PropertyBoolList.md)
-   [App::PropertyColor](FeaturePython_Custom_Properties#App:_PropertyColor.md)
-   [App::PropertyColorList](FeaturePython_Custom_Properties#App:_PropertyColorList.md)
-   [App::PropertyDirection](FeaturePython_Custom_Properties#App:_PropertyDirection.md)
-   [App::PropertyDistance](FeaturePython_Custom_Properties#App:_PropertyDistance.md)
-   [App::PropertyEnumeration](FeaturePython_Custom_Properties#App:_PropertyEnumeration.md)
-   [App::PropertyExpressionEngine](FeaturePython_Custom_Properties#App:_PropertyExpressionEngine.md)
-   [App::PropertyFile](FeaturePython_Custom_Properties#App:_PropertyFile.md)
-   [App::PropertyFileIncluded](FeaturePython_Custom_Properties#App:_PropertyFileIncluded.md)
-   [App::PropertyFloat](FeaturePython_Custom_Properties#App:_PropertyFloat.md)
-   [App::PropertyFloatConstraint](FeaturePython_Custom_Properties#App:_PropertyFloatConstraint.md)
-   [App::PropertyFloatList](FeaturePython_Custom_Properties#App:_PropertyFloatList.md)
-   [App::PropertyFont](FeaturePython_Custom_Properties#App:_PropertyFont.md)
-   [App::PropertyForce](FeaturePython_Custom_Properties#App:_PropertyForce.md)
-   [App::PropertyFrequency](FeaturePython_Custom_Properties#App:_PropertyFrequency.md)
-   [App::PropertyInteger](FeaturePython_Custom_Properties#App:_PropertyInteger.md)
-   [App::PropertyIntegerConstraint](FeaturePython_Custom_Properties#App:_PropertyIntegerConstraint.md)
-   [App::PropertyIntegerList](FeaturePython_Custom_Properties#App:_PropertyIntegerList.md)
-   [App::PropertyIntegerSet](FeaturePython_Custom_Properties#App:_PropertyIntegerSet.md)
-   [App::PropertyLength](FeaturePython_Custom_Properties#App:_PropertyLength.md)
-   [App::PropertyLink](FeaturePython_Custom_Properties#App:_PropertyLink.md)
-   [App::PropertyLinkChild](FeaturePython_Custom_Properties#App:_PropertyLinkChild.md)
-   [App::PropertyLinkGlobal](FeaturePython_Custom_Properties#App:_PropertyLinkGlobal.md)
-   [App::PropertyLinkHidden](FeaturePython_Custom_Properties#App:_PropertyLinkHidden.md)
-   [App::PropertyLinkList](FeaturePython_Custom_Properties#App:_PropertyLinkList.md)
-   [App::PropertyLinkListChild](FeaturePython_Custom_Properties#App:_PropertyLinkListChild.md)
-   [App::PropertyLinkListGlobal](FeaturePython_Custom_Properties#App:_PropertyLinkListGlobal.md)
-   [App::PropertyLinkListHidden](FeaturePython_Custom_Properties#App:_PropertyLinkListHidden.md)
-   [App::PropertyLinkSub](FeaturePython_Custom_Properties#App:_PropertyLinkSub.md)
-   [App::PropertyLinkSubChild](FeaturePython_Custom_Properties#App:_PropertyLinkSubChild.md)
-   [App::PropertyLinkSubGlobal](FeaturePython_Custom_Properties#App:_PropertyLinkSubGlobal.md)
-   [App::PropertyLinkSubHidden](FeaturePython_Custom_Properties#App:_PropertyLinkSubHidden.md)
-   [App::PropertyLinkSubList](FeaturePython_Custom_Properties#App:_PropertyLinkSubList.md)
-   [App::PropertyLinkSubListChild](FeaturePython_Custom_Properties#App:_PropertyLinkSubListChild.md)
-   [App::PropertyLinkSubListGlobal](FeaturePython_Custom_Properties#App:_PropertyLinkSubListGlobal.md)
-   [App::PropertyLinkSubListHidden](FeaturePython_Custom_Properties#App:_PropertyLinkSubListHidden.md)
-   [App::PropertyMap](FeaturePython_Custom_Properties#App:_PropertyMap.md)
-   [App::PropertyMaterial](FeaturePython_Custom_Properties#App:_PropertyMaterial.md)
-   [App::PropertyMaterialList](FeaturePython_Custom_Properties#App:_PropertyMaterialList.md)
-   [App::PropertyMatrix](FeaturePython_Custom_Properties#App:_PropertyMatrix.md)
-   [App::PropertyPath](FeaturePython_Custom_Properties#App:_PropertyPath.md)
-   [App::PropertyPercent](FeaturePython_Custom_Properties#App:_PropertyPercent.md)
-   [App::PropertyPersistentObject](FeaturePython_Custom_Properties#App:_PropertyPersistentObject.md)
-   [App::PropertyPlacement](FeaturePython_Custom_Properties#App:_PropertyPlacement.md)
-   [App::PropertyPlacementLink](FeaturePython_Custom_Properties#App:_PropertyPlacementLink.md)
-   [App::PropertyPlacementList](FeaturePython_Custom_Properties#App:_PropertyPlacementList.md)
-   [App::PropertyPosition](FeaturePython_Custom_Properties#App:_PropertyPosition.md)
-   [App::PropertyPrecision](FeaturePython_Custom_Properties#App:_PropertyPrecision.md)
-   [App::PropertyPressure](FeaturePython_Custom_Properties#App:_PropertyPressure.md)
-   [App::PropertyPythonObject](FeaturePython_Custom_Properties#App:_PropertyPythonObject.md)
-   [App::PropertyQuantity](FeaturePython_Custom_Properties#App:_PropertyQuantity.md)
-   [App::PropertyQuantityConstraint](FeaturePython_Custom_Properties#App:_PropertyQuantityConstraint.md)
-   [App::PropertySpeed](FeaturePython_Custom_Properties#App:_PropertySpeed.md)
-   [App::PropertyString](FeaturePython_Custom_Properties#App:_PropertyString.md)
-   [App::PropertyStringList](FeaturePython_Custom_Properties#App:_PropertyStringList.md)
-   [App::PropertyUUID](FeaturePython_Custom_Properties#App:_PropertyUUID.md)
-   [App::PropertyVacuumPermittivity](FeaturePython_Custom_Properties#App:_PropertyVacuumPermittivity.md)
-   [App::PropertyVector](FeaturePython_Custom_Properties#App:_PropertyVector.md)
-   [App::PropertyVectorDistance](FeaturePython_Custom_Properties#App:_PropertyVectorDistance.md)
-   [App::PropertyVectorList](FeaturePython_Custom_Properties#App:_PropertyVectorList.md)
-   [App::PropertyVolume](FeaturePython_Custom_Properties#App:_PropertyVolume.md)
-   [App::PropertyXLink](FeaturePython_Custom_Properties#App:_PropertyXLink.md)
-   [App::PropertyXLinkList](FeaturePython_Custom_Properties#App:_PropertyXLinkList.md)
-   [App::PropertyXLinkSub](FeaturePython_Custom_Properties#App:_PropertyXLinkSub.md)
-   [App::PropertyXLinkSubList](FeaturePython_Custom_Properties#App:_PropertyXLinkSubList.md)
-   [Mesh::PropertyCurvatureList](FeaturePython_Custom_Properties#Mesh:_PropertyCurvatureList.md)
-   [Mesh::PropertyMeshKernel](FeaturePython_Custom_Properties#Mesh:_PropertyMeshKernel.md)
-   [Mesh::PropertyNormalList](FeaturePython_Custom_Properties#Mesh:_PropertyNormalList.md)
-   [Part::PropertyFilletEdges](FeaturePython_Custom_Properties#Part:_PropertyFilletEdges.md)
-   [Part::PropertyGeometryList](FeaturePython_Custom_Properties#Part:_PropertyGeometryList.md)
-   [Part::PropertyPartShape](FeaturePython_Custom_Properties#Part:_PropertyPartShape.md)
-   [Part::PropertyShapeHistory](FeaturePython_Custom_Properties#Part:_PropertyShapeHistory.md)
-   [Path::PropertyPath](FeaturePython_Custom_Properties#Path:_PropertyPath.md)
-   [Path::PropertyTool](FeaturePython_Custom_Properties#Path:_PropertyTool.md)
-   [Path::PropertyTooltable](FeaturePython_Custom_Properties#Path:_PropertyTooltable.md)
-   [Sketcher::PropertyConstraintList](FeaturePython_Custom_Properties#Sketcher:_PropertyConstraintList.md)
-   [Spreadsheet::PropertyColumnWidths](FeaturePython_Custom_Properties#Spreadsheet:_PropertyColumnWidths.md)
-   [Spreadsheet::PropertyRowHeights](FeaturePython_Custom_Properties#Spreadsheet:_PropertyRowHeights.md)
-   [Spreadsheet::PropertySheet](FeaturePython_Custom_Properties#Spreadsheet:_PropertySheet.md)
-   [Spreadsheet::PropertySpreadsheetQuantity](FeaturePython_Custom_Properties#Spreadsheet:_PropertySpreadsheetQuantity.md)
-   [TechDraw::PropertyCenterLineList](FeaturePython_Custom_Properties#TechDraw:_PropertyCenterLineList.md)
-   [TechDraw::PropertyCosmeticEdgeList](FeaturePython_Custom_Properties#TechDraw:_PropertyCosmeticEdgeList.md)
-   [TechDraw::PropertyCosmeticVertexList](FeaturePython_Custom_Properties#TechDraw:_PropertyCosmeticVertexList.md)
-   [TechDraw::PropertyGeomFormatList](FeaturePython_Custom_Properties#TechDraw:_PropertyGeomFormatList.md)

Podczas dodawania właściwości do obiektów niestandardowych należy zwrócić uwagę na następujące kwestie:

-   Nie używaj znaków **<** lub **>** w opisach właściwości *(spowodowałoby to przerwanie fragmentów xml w pliku .fcstd)*
-   Właściwości są przechowywane w pliku .fcstd w porządku alfabetycznym. Jeśli we właściwościach znajduje się kształt, każda właściwość, której nazwa w porządku alfabetycznym znajduje się za \"Kształtem\", zostanie wczytana PRZED kształtem, co może powodować dziwne zachowania.

Pełną listę atrybutów właściwości można znaleźć w pliku nagłówkowym [PropertyStandard C++](https://github.com/FreeCAD/FreeCAD/blob/master/src/App/PropertyStandard.h). Na przykład, jeśli chcesz pozwolić użytkownikowi na wprowadzenie tylko ograniczonego zakresu wartości *(np. używając PropertyIntegerConstraint)*, w Pythonie przypiszesz tuple zawierające nie tylko wartość właściwości, ale także dolny i górny zakres oraz wielkość kroku, jak przedstawiono poniżej:


```python
prop = (value, lower, upper, stepsize)
```

## Typy właściwości 

Domyślnie właściwości mogą być aktualizowane. Możliwe jest nadanie właściwościom statusu tylko do odczytu, na przykład w sytuacji, gdy chcemy pokazać wynik działania metody. Możliwe jest także ukrycie właściwości. Typ właściwości można ustawić za pomocą:


```python
obj.setEditorMode("MyPropertyName", mode)
```

gdzie *mode* jest krótką liczbą całkowitą, której można nadać następujące wartości:

 0 -- tryb domyślny, odczyt i zapis
 1 -- tylko do odczytu
 2 -- ukryty

Tryby edytora nie są ustawiane przy ponownym wczytywaniu pliku FreeCAD. Można to zrobić za pomocą funkcji \_\_setstate\_\_. Zobacz <http://forum.freecadweb.org/viewtopic.php?f=18&t=13460&start=10#p108072>. Dzięki użyciu setEditorMode właściwości są tylko do odczytu w Edytorze właściwości. Nadal można je zmieniać z poziomu Pythona. Aby naprawdę uczynić je tylko do odczytu, ustawienie musi być przekazane bezpośrednio wewnątrz funkcji addProperty. Przykład można znaleźć na stronie <http://forum.freecadweb.org/viewtopic.php?f=18&t=13460&start=20#p109709>.

Korzystając z bezpośredniego ustawienia w funkcji addProperty, masz też więcej możliwości. W szczególności interesującą możliwością jest oznaczenie właściwości jako właściwości wyjściowej. W ten sposób FreeCAD nie będzie oznaczał właściwości jako dotkniętej podczas jej zmiany *(nie ma więc potrzeby ponownego obliczania)*.

Przykład właściwości wyjściowej *(zob. też <https://forum.freecadweb.org/viewtopic.php?t=24928>)*:


```python
obj.addProperty("App::PropertyString","MyCustomProperty","","",8)
```

Typy właściwości, które można ustawić w ostatnim parametrze funkcji addProperty, są następujące:

 0 -- Prop_None, brak specjalnego typu właściwości
 1 -- Prop_ReadOnly, właściwość jest tylko do odczytu w edytorze
 2 -- Prop_Transient, właściwość nie zostanie zapisana do pliku
 4 -- Prop_Hidden, właściwość nie będzie widoczna w edytorze
 8 -- Prop_Output, Zmodyfikowana właściwość nie dotyka swojego kontenera nadrzędnego
 16 -- Prop_NoRecompute, Zmodyfikowana właściwość nie dotyka swojego kontenera do rekompilacji

Te różne typy właściwości można znaleźć w [source code C++ header for PropertyContainer](https://github.com/FreeCAD/FreeCAD/blob/master/src/App/PropertyContainer.h).

## Inny, bardziej złożony przykład 

Ten przykład wykorzystuje środowisko pracy [Część](Part_Workbench/pl.md) do utworzenia ośmiościanu, a następnie tworzy jego reprezentację \"coin\" za pomocą Pivy.

Pierwszym z nich jest sam obiekt Dokumentu:


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

Następnie mamy obiekt dostawcy widoku, odpowiedzialny za wyświetlanie obiektu na scenie 3D:


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

  def __getstate__(self):
     return None

  def __setstate__(self,state):
     return None
```

Na koniec, gdy nasz obiekt i jego viewobject są już zdefiniowane, wystarczy je wywołać *(kod klasy Octahedron i klasy viewprovider można skopiować bezpośrednio w konsoli Python programu FreeCAD)*:


```python
FreeCAD.newDocument()
a=FreeCAD.ActiveDocument.addObject("App::FeaturePython","Octahedron")
Octahedron(a)
ViewProviderOctahedron(a.ViewObject)
```

## Robienie obiektów wybieralnymi 

Jeśli chcesz, aby Twój obiekt był wybieralny, lub przynajmniej jego część, przez kliknięcie na nim w rzutni, musisz umieścić jego geometrię coin w węźle SoFCSelection. Jeśli obiekt ma złożoną reprezentację, z widżetami, adnotacjami itp, możesz chcieć zawrzeć tylko jego część w węźle SoFCSelection. Wszystko, co jest węzłem SoFCSelection, jest stale skanowane przez FreeCAD w celu wykrycia zaznaczenia/poprzedzenia zaznaczenia, więc warto spróbować nie przeciążać go niepotrzebnym skanowaniem.

Gdy fragmenty scenogramu, które mają być wybieralne, znajdą się w węzłach SoFCSelection, należy dostarczyć dwie metody do obsługi ścieżki wyboru. Ścieżka wyboru może mieć postać łańcucha podającego nazwy poszczególnych elementów ścieżki lub tablicy obiektów scenogramu. Dwie metody, które udostępniasz, to `getDetailPath`, która konwertuje ścieżkę łańcuchową na tablicę obiektów scenograficznych, oraz `getElementPicked`, która pobiera element kliknięty w scenogramie i zwraca jego nazwę w postaci łańcucha *(uwaga, nie jego ścieżkę w postaci łańcucha)*.

Oto powyższy przykład cząsteczki, dostosowany do wyboru elementów cząsteczki:


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

    def __getstate__(self):
        return None

    def __setstate__(self,state):
        return None

def makeMolecule():
    FreeCAD.newDocument()
    a=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","Molecule")
    Molecule(a)
    ViewProviderMolecule(a.ViewObject)
    FreeCAD.ActiveDocument.recompute()
```

## Praca z prostymi kształtami 

Jeśli obiekt parametryczny po prostu wyprowadza kształt, nie trzeba używać obiektu dostawcy widoku. Kształt zostanie wyświetlony przy użyciu standardowej reprezentacji kształtu programu FreeCAD:


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

Ten sam kod z użyciem **ViewProviderLine**.


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

## Struktura scenograficzna 

Być może zauważyłeś, że powyższe przykłady konstruują swoje scenagramy w nieco inny sposób. Niektóre używają `obj.addDisplayMode(node, "modename")`, podczas gdy inne `obj.SwitchNode.getChild(x).addChild(y)`.

Każdy element w dokumencie FreeCAD jest oparty na następującej strukturze scenogramu:


```python
RootNode
 \- SwitchNode
     \- Shaded
      - Wireframe
      - etc
```

Węzeł `SwitchNode` wyświetla tylko jeden ze swoich potomków, w zależności od tego, jaki tryb wyświetlania został wybrany w programie FreeCAD.

Przykłady, które używają `addDisplayMode`, konstruują swoje scenagramy wyłącznie z elementów scenogramu coin3d. Pod przykrywką, `addDisplayMode` dodaje nowego potomka do węzła `SwitchNode`. Nazwa tego węzła będzie odpowiadać trybowi wyświetlania, który został mu przekazany.

Przykłady, które używają `SwitchNode.getChild(x).addChild`, konstruują również część swojej geometrii przy użyciu funkcji ze środowiska pracy Część, takich jak `1=fp.Shape = Part.makeLine(fp.p1,fp.p2)`. Dzięki temu pod węzłem `SwitchNode` powstają scenografie z różnymi trybami wyświetlania. Gdy później chcemy dodać do nich elementy coin3d, musimy je dodać do istniejących scenogramów z trybami wyświetlania, używając `addChild`, a nie tworząc nowego potomka węzła `SwitchNode`.

Podczas używania `addDisplayMode()` w celu dodania geometrii do scenogramu, każdy tryb wyświetlania powinien mieć swój własny węzeł, który jest przekazywany do `addDisplayMode()`; nie używaj do tego ponownie tego samego węzła. Spowoduje to zmylenie mechanizmu selekcji. W porządku, jeśli węzeł każdego trybu wyświetlania ma te same węzły geometrii dodane poniżej, tylko korzeń każdego trybu wyświetlania musi być inny.

Oto powyższy przykład cząsteczki, przystosowany do rysowania tylko obiektami scenograficznymi Coin3D, a nie obiektami z środowiska pracy Część:


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

    def __getstate__(self):
        return None

    def __setstate__(self,state):
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

## Obiekty skryptowe środowiska pracy Projekt Części 

Podczas tworzenia obiektów skryptowych w środowisku pracy Projekt Części proces jest podobny do tworzenia obiektów skryptowych omówionych powyżej, ale z kilkoma dodatkowymi uwagami. Musimy obsługiwać dwie właściwości kształtu, jedną dla kształtu, który widzimy w oknie widoku 3D, a drugą dla kształtu używanego przez narzędzia wzorca, takie jak cechy wzoru biegunowego. Kształty obiektów muszą również zostać połączone z istniejącym materiałem już znajdującym się w zawartości *(lub wycięte z niego w przypadku cech typu Subtractive)*. Musimy także w nieco inny sposób uwzględniać umieszczanie i mocowanie naszych obiektów.

Opisane w skryptach funkcje obiektów bryłowych Projekt Części powinny opierać się na: PartDesign::FeaturePython, PartDesign::FeatureAdditivePython lub PartDesign::FeatureSubtractivePython, a nie na Part::FeaturePython. Tylko warianty Additive i Subtractive mogą być używane we wzorcach cech, a jeśli bazują na Part::FeaturePython, gdy użytkownik upuści obiekt do bryły Projekt Części, staje się on BaseFeature, zamiast być traktowany przez bryłę jako natywny obiekt Projekt Części. **Uwaga**: wszystkie te obiekty mają być bryłami, więc jeśli tworzysz obiekt nie będący bryłą, powinien on być oparty na Part::FeaturePython, w przeciwnym razie następny obiekt w drzewie będzie próbował połączyć się z nim jako bryłą i to się nie uda.

Oto prosty przykład tworzenia elementu pierwotnego rury, podobnego do elementu pierwotnego rury w środowisku pracy Część, z tą różnicą, że ten element będzie obiektem bryłowym środowiska pracy Projekt Części. W tym celu utworzymy dwa osobne pliki: pdtube.FCMacro i pdtube.py. Plik .FCMacro będzie wykonywany przez użytkownika w celu utworzenia obiektu. Plik .py będzie zawierał definicje klas zaimportowane przez plik .FCMacro. Powodem takiego postępowania jest zachowanie parametrycznego charakteru obiektu po ponownym uruchomieniu programu FreeCAD i otwarciu dokumentu zawierającego jedną z naszych rur.

Po pierwsze, plik definicji klasy:


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

    def __getstate__(self):
        '''When saving the document this object gets stored using Python's json module.\
                Since we have some un-serializable parts here -- the Coin stuff -- we must define this method\
                to return a tuple of all serializable objects or None.'''
        return None

    def __setstate__(self,state):
        '''When restoring the serialized object from document we have the chance to set some internals here.\
                Since no data were serialized nothing needs to be done here.'''
        return None
```

A teraz plik makrodefinicji do utworzenia obiektu:


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

## Informacje dodatkowe 

Dodatkowe strony:

-   [Obiekty tworzone skryptami, zapis atrybutów](Scripted_objects_saving_attributes/pl.md)
-   [Obiekty tworzone skryptami, migracja](Scripted_objects_migration/pl.md)
-   [Obiekty tworzone skryptami, z załącznikiem](Scripted_objects_with_attachment/pl.md)
-   [Dostawca widoku](Viewprovider/pl.md)

Ciekawe wątki na forum dotyczące obiektów tworzonych skryptami:

-   [Python object attributes lost at load](http://forum.freecadweb.org/viewtopic.php?f=22&t=13740)
-   [New FeaturePython is grey](http://forum.freecadweb.org/viewtopic.php?t=12139)
-   [Explanation on \_\_getstate\_\_ and \_\_setstate\_\_](https://forum.freecadweb.org/viewtopic.php?f=18&t=44009), [official documentation](https://docs.python.org/3/library/pickle.html#object.__getstate__)
-   [Eigenmode frequency always 0?](https://forum.freecadweb.org/viewtopic.php?f=18&t=13460&start=20#p109709)
-   [how to implement python feature\'s setEdit properly?](https://forum.freecadweb.org/viewtopic.php?f=22&t=21330)

Oprócz przykładów przedstawionych tutaj więcej przykładów można znaleźć w kodzie źródłowym programu FreeCAD [src/Mod/TemplatePyMod/FeaturePython.py](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/TemplatePyMod/FeaturePython.py).



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Scripted objects/pl
