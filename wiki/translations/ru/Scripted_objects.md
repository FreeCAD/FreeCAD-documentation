# Scripted objects/ru
## Введение

Кроме стандартных типов объектов, таких как аннотации, полигональные сетки и детали, FreeCAD также предлагает удивительную возможность создавать параметрические объекты, 100% написанные на Python, такие объекты называются ([Python Features](App_FeaturePython/ru.md)). Они ведут себя точно так же, как любой другой объект FreeCAD, автоматически сохраняются и восстанавливаются при сохранении или загрузке файла.


<div class="mw-translate-fuzzy">

Должна быть понята одна особенность, эти объекты сохраняются в файлах FreeCAD FcStd вместе с модулем pythonа [json](https://docs.python.org/3/library/json.html). Этот модуль превращает объект pythonа в строку, позволяя его добавление в сохраняемый файл. При загрузке, модуль json использует эту строку для пересоздания оригинального объекта, обеспечивает его доступ к исходному коду, создавшему объект. Это значит, что если Вы сохранили этот пользовательский объект и открыли его на машине, где код python, который сгенерировал объект, отсутствует, объект не может быть восстановлен. Если Вы распространяете эти объекты среди других друзей, Вам нужно передавать вместе с ними скрипт pythonа, который его создал.


</div>

**Примечание**: Имеется возможность упаковки python кода внутрь FreeCAD файла, используя json сериализацию с помощью App::PropertyPythonObject, но этот код в конечном счете нельзя будет запустить напрямую, поэтому это мало подходит для наших целей.

[Python Features](App_FeaturePython/ru.md) следуют тому же правилу что и все остальные FreeCAD features: они разделены на App и GUI части. App часть, Объект Документ (Document Object), определяет геометрию нашего объекта, тогда как его GUI часть, Объект Визуального Представления (View Provider Object) определяет, как объект будет отображаться на экране. Объект View Provider, как и любая другая FreeCAD feature, доступен только при запуске FreeCAD в его собственном графическом интерфейсе. Существует несколько свойств и методов, доступных для создания вашего объекта. Свойства должны принадлежать к любому из предопределенных типов свойств, предлагаемых FreeCAD, и отображаться в окне просмотра свойств, чтобы пользователь мог их редактировать. Таким образом, объекты Feature Python полностью параметричны. Вы можете задать свойства как Данных, так и свойства Вида.



## Простой пример 

Следующий пример можно найти в файле [src/Mod/TemplatePyMod/FeaturePython.py](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/TemplatePyMod/FeaturePython.py) вместе с несколькими другими примерами:


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



### Что необходимо отметить 

Если Ваш объект полагается на то, что будет пересчитан во время создания, Вы должны сделать это вручную в функции `__init__`, поскольку пересчёт не вызывается автоматически. Этот пример не требует этого поскольку метод `onChanged` класса `Box` имеет тот же эффект, что и функция `execute`, но пример ниже полагается на то, что будет пересчитан перед тем как будет показан в окне трёхмерного просмотра. В этих примерах это делается вручную с помощью `ActiveDocument.recompute()`, но в более сложных сценариях Вы должны решить, где пересчитать либо весь документ, или объект FeaturePython.

Этот пример создаёт несколько исключений трасс стека в окне отчётов. Это поскольку метод `onChanged` класса `Box` вызывается каждый раз как свойство добавляется в `__init__`. Когда первое было добавлено, параметры Width и Height и потому попытки доступа к ним безуспешны.

Описание `__getstate__` и `__setstate__` находится в теме форума [obj.Proxy.Type is a dict, not a string](https://forum.freecadweb.org/viewtopic.php?f=18&t=44009&start=10#p377892).



## Доступные методы 

Полное описание доступно на странице [методы FeaturePython](FeaturePython_methods/ru.md).



## Доступные свойства 

Свойства - это \"строительные блоки\" объекта FeaturePython. Через них пользователь может взаимодействовать с объектом и вносить изменения в него. После создания нового FeaturePython объекта в вашем документе ( a=FreeCAD.ActiveDocument.addObject(\"App::FeaturePython\",\"Box\") ),вы можете получить список доступных свойств, с помощью:


```python
obj.supportedProperties()
```

Вы получите список доступных свойств, которые более подробно описаны на странице [пользовательских свойств объекта FeaturePython](FeaturePython_Custom_Properties/ru.md):

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

При добавлении новых свойств к пользовательским объектам, позаботьтесь об этом:

-   Не используйте символы \"\<\" или \"\>\" в описании свойств (это вызовет поломку xml части .fcstd файла)
-   Свойства хранятся в .fcstd файле в алфавитном порядке. Если у вас есть форма(shape) в ваших свойствах, любое свойство имя которого идет, в алфавитном порядке, после \"Shape\" , будет загружено ПОСЛЕ формы, что может привести к странному поведению.

Полный список атрибутов свойств можно посмотреть в [заголовочном файле C++ PropertyStandard](https://github.com/FreeCAD/FreeCAD/blob/master/src/App/PropertyStandard.h). Например, если Вы хотите позволить пользователю вводить ограниченный диапазон значений (например, используя using PropertyIntegerConstraint), в Python Вы назначаете кортеж, содержащий не только значение свойства, но и верхний, нижний предел и шаг изменения, как сделано ниже:


```python
prop = (value, lower, upper, stepsize)
```



## Типы свойств 

По умолчанию свойства могут быть обновлены. Имеется возможность сделать свойство только для чтения (read-only), например, в случае если требуется отображать только результат выполнения метода. Также возможно создать скрытое (hidden) свойство. Сам же тип свойства можно задать с помощью:


```python
obj.setEditorMode("MyPropertyName", mode)
```

где переменная mode (short int типа) - может иметь следующие значения:

 0 -- значение по умолчанию, допускает как чтение, так и запись
 1 -- свойство только для чтения (read-only)
 2 -- скрытое свойство (hidden)

The EditorModes are not set at FreeCAD file reload. This could to be done by the \_\_setstate\_\_ function. See <http://forum.freecadweb.org/viewtopic.php?f=18&t=13460&start=10#p108072>. By using the setEditorMode the properties are only read only in PropertyEditor. They could still be changed from python. To really make them read only the setting has to be passed directly inside the addProperty function. See <http://forum.freecadweb.org/viewtopic.php?f=18&t=13460&start=20#p109709> for an example.

Using the direct setting in the addProperty function, you also have more possibilities. In particular, an interesting one is mark a property as an output property. This way FreeCAD won\'t mark the feature as touched when changing it (so no need to recompute).

Example of output property (see also <https://forum.freecadweb.org/viewtopic.php?t=24928>):


```python
obj.addProperty("App::PropertyString","MyCustomProperty","","",8)
```

The property types that can be set at last parameter of the addProperty function are:

 0 -- Prop_None, No special property type
 1 -- Prop_ReadOnly, Property is read-only in the editor
 2 -- Prop_Transient, Property won't be saved to file
 4 -- Prop_Hidden, Property won't appear in the editor
 8 -- Prop_Output, Modified property doesn't touch its parent container
 16 -- Prop_NoRecompute, Modified property doesn't touch its container for recompute
 32 -- Prop_NoPersist, Property won't be saved to file at all

Вы можете найти эти различные типы свойств, определённые в [заголовочном файле PropertyContainer исходного кода C++](https://github.com/FreeCAD/FreeCAD/blob/master/src/App/PropertyContainer.h).



## Другой более сложный пример 

Данный пример использует [верстак Part](Part_Workbench/ru.md) для создания октаэдра, затем создает собственное Coin представление с помощью Pivy.

Сначала сам Документированный Объект:


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

Теперь , мы обладаем визуальным представлением объекта, ответственного за отображение объекта в 3D сцене:


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

Наконец, когда определен наш объект и его визуальный объект, нам просто нужно вызвать их:


```python
FreeCAD.newDocument()
a=FreeCAD.ActiveDocument.addObject("App::FeaturePython","Octahedron")
Octahedron(a)
ViewProviderOctahedron(a.ViewObject)
```



## Создание выделяемых объектов 

Если вы хотите чтобы ваш объект можно было выбрать, или по крайней мере его часть, щелкнув по нему в окне, вы должны включить его Coin геометрию внутрь узла SoFCSelection. Если ваш объект обладает сложным представлением, с виджетами, аннотациями, и т.д, вам может потребоваться только часть его в SoFCSelection. Всё, что находится в SoFCSelection постоянно сканируется FreeCAD для обнаружения выделения/предварительного отбора, так что имеет смысл попробовать не перегружать его ненужным сканированием.

Как только части графа сцены, которые должны быть выбраны, оказываются внутри узлов SoFCSelection, вам необходимо предоставить два метода для обработки пути выбора. Путь выбора может принимать форму строки, содержащей имена каждого элемента в пути, или массива объектов графа сцены. Вы предоставляете два метода: `getDetailPath`, который преобразует путь строки в массив объектов scenegraph (графа сцены), и `getElementPicked`, который принимает элемент, по которому щелкнули в графе сцены, и возвращает его строковое имя (примечание, а не его строковый путь).

Вот вышеприведённый пример с молекулой, адаптированный для выбора элементов молекулы:


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



## Работа с простыми формами 

Если ваш параметрический объект - это просто геометрическая форма, то вам не нужно использовать view provider объект. Форма будет отображаться стандартными способами представления форм FreeCAD:


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

Тот же код с применением **ViewProviderLine**


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



## Структура графа сцены 

You may have noticed that the examples above construct their scenegraphs in slightly different ways. Some use `obj.addDisplayMode(node, "modename")` while others use `obj.SwitchNode.getChild(x).addChild(y)`.

Each feature in a FreeCAD document is based the following scenegraph structure:


```python
RootNode
 \- SwitchNode
     \- Shaded
      - Wireframe
      - etc
```

The `SwitchNode` displays only one of its children, depending on which display mode is selection in FreeCAD.

The examples which use `addDisplayMode` are constructing their scenegraphs solely out of coin3d scenegraph elements. Under the covers, `addDisplayMode` adds a new child to the `SwitchNode`; the name of that node will match the display mode it was passed.

The examples which use `SwitchNode.getChild(x).addChild` also construct part of their geometry using functions from the Part workbench, such as `1=fp.Shape = Part.makeLine(fp.p1,fp.p2)`. This constructs the different display mode scenegraphs under the `SwitchNode`; when we later come to add coin3d elements to the scenegraph, we need to add them to the existing display mode scenegraphs using `addChild` rather than creating a new child of the `SwitchNode`.

When using `addDisplayMode()` to add geometry to the scenegraph, each display mode should have its own node which is passed to `addDisplayMode()`; don\'t reuse the same node for this. Doing so will confuse the selection mechanism. It\'s okay if each display mode\'s node has the same geometry nodes added below it, just the root of each display mode needs to be distinct.

Here is the above molecule example, adapted to be drawn only with Coin3D scenegraph objects instead of using objects from the Part workbench:


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



## Программируемый объект Part Design 

When making scripted objects in Part Design the process is similar to the scripted objects discussed above, but with a few additional considerations. We must handle 2 shape properties, one for the shape we see in the 3D view and another for the shape used by the pattern tools, such as polar pattern features. The object shapes also needs to be fused to any existing material already in the Body (or cut from it in the case of Subtractive features). And we must account for the placement and attachment of our objects a little bit differently.

Part Design scripted solid object features should be based on either PartDesign::FeaturePython, PartDesign::FeatureAdditivePython, or PartDesign::FeatureSubtractivePython rather than Part::FeaturePython. Only the Additive and Subtractive variants can be used in pattern features, and if based on Part::FeaturePython when the user drops the object into a Part Design Body it becomes a BaseFeature rather than being treated by the Body as a native Part Design object. Note: all of these are expected to be solids, so if you are making a non-solid feature it should be based on Part::FeaturePython or else the next feature in the tree will attempt to fuse to as a solid and it will fail.

Here is a simple example of making a Tube primitive, similar to the Tube primitive in Part Workbench except this one will be a Part Design solid feature object. For this we will 2 separate files: pdtube.FCMacro and pdtube.py. The .FCMacro file will be executed by the user to create the object. The .py file will hold the class definitions, imported by the .FCMacro. The reason for doing it this way is to maintain the parametric nature of the object after restarting FreeCAD and opening a document containing one of our Tubes.

First, the class definition file:


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

And now the macro file to create the object:


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



## Дополнительная информация 

Дополнительные страницы Вики FreeCADа:

-   [Scripted objects saving attributes](Scripted_objects_saving_attributes/ru.md)
-   [Scripted objects migration](Scripted_objects_migration/ru.md)
-   [Scripted objects with attachment](Scripted_objects_with_attachment/ru.md)
-   [Viewproviders](Viewprovider/ru.md)

Интересные темы форума про создание объектов с помощью скриптов:

-   [Python object attributes lost at load](http://forum.freecadweb.org/viewtopic.php?f=22&t=13740)
-   [New FeaturePython is grey](http://forum.freecadweb.org/viewtopic.php?t=12139)
-   [Explanation on \_\_getstate\_\_ and \_\_setstate\_\_](https://forum.freecadweb.org/viewtopic.php?f=18&t=44009), [official documentation](https://docs.python.org/3/library/pickle.html#object.__getstate__)
-   [Eigenmode frequency always 0?](https://forum.freecadweb.org/viewtopic.php?f=18&t=13460&start=20#p109709)
-   [how to implement python feature\'s setEdit properly?](https://forum.freecadweb.org/viewtopic.php?f=22&t=21330)

В дополнение к представленным примерам, посмотрите FreeCAD [src/Mod/TemplatePyMod/FeaturePython.py](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/TemplatePyMod/FeaturePython.py), находящийся в папке с исходными кодами FreeCAD.



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Scripted objects/ru
