# Scripted objects/es
{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

Además de los tipos de objetos estándar, tales como anotaciones, mallas y objetos de pieza, FreeCAD también ofrece la estupenda posibilidad de construir objetos de archivos de guión hechos al 100% en Python, llamados *Funcionalidades* Python (Feature Python). Esos objetos se comportan exactamente como cualquier otro objeto de FreeCAD, y se guardar y restauran automáticamente al guardar o cargar archivos.


</div>


<div class="mw-translate-fuzzy">

Debe comprenderse una particularidad, dichos objetos son guardados en archivos FcStd de FreeCAD con el módulo de Python [cPickle](http   *//docs.python.org/release/2.5/lib/module-cPickle.html). Este módulo devuelve un objeto de Python como una cadena de texto, permitiendo que se añada al guardado del archivo. En la carga, el módulo cPickle utiliza esa cadena de texto para recrear los objetos originales, proporcionándole acceso al código fuente que creó el objeto. Es decir que si guardas un objeto personalizado y lo abres en un ordenador en el que el código de Python que generó dicho objeto no está presente, el objeto no será recreado. Si distribuyes dichos objetos a otros usuarios, tendrás que distribuirlos junta al archivo de guión de Python que los crea.


</div>

**Note**   * It is possible to pack python code inside a FreeCAD file using json serializing with an App   *   *PropertyPythonObject, but that code can never directly be run, and therefore has little use for our purpose here.


<div class="mw-translate-fuzzy">

Las Funcionalidades Python siguen las mismas reglas que todas las Funcionalidades de FreeCAD   * se separan en las partes de App y GUI. La parte de App, el objeto documento, define la geometría de nuestro objeto, mientras que su parte GUI, el objeto proveedor de vistas, define el modo en que el objeto se dibujará en la pantalla. El objeto proveedor de vistas, como cualquier otra Funcionalidad de FreeCAD, sólo está disponible cuando se ejecuta FreeCAD en su propio GUI. Hay varias propiedades y métodos disponibles para construir tu objeto. Las propiedades tienen que ser de cualquiera de los tipos predefinidos de propiedades que ofrece FreeCAD, y aparecerá en la ventana de vista de propiedades, por lo que puede ser editado por el usuario. De esta manera, los objetos Funcionalidad Python son total y absolutamente paramétricos. Puedes definir las propiedades del objeto y de su ViewObject por separado.


</div>

## Basic example 


<div class="mw-translate-fuzzy">

## Ejemplo básico 

El ejemplo siguiente se puede encontrar en el archivo [src/Mod/TemplatePyMod/FeaturePython.py](http   *//free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Mod/TemplatePyMod/FeaturePython.py?view=markup) , junto con varios otros ejemplos   *


</div>


```python
'''Examples for a feature class and its view provider.'''

import FreeCAD, FreeCADGui
from pivy import coin

class Box   *
    def __init__(self, obj)   *
        '''Add some custom properties to our box feature'''
        obj.addProperty("App   *   *PropertyLength","Length","Box","Length of the box").Length=1.0
        obj.addProperty("App   *   *PropertyLength","Width","Box","Width of the box").Width=1.0
        obj.addProperty("App   *   *PropertyLength","Height","Box", "Height of the box").Height=1.0
        obj.Proxy = self

    def onChanged(self, fp, prop)   *
        '''Do something when a property has changed'''
        FreeCAD.Console.PrintMessage("Change property   * " + str(prop) + "\n")

    def execute(self, fp)   *
        '''Do something when doing a recomputation, this method is mandatory'''
        FreeCAD.Console.PrintMessage("Recompute Python Box feature\n")

class ViewProviderBox   *
    def __init__(self, obj)   *
        '''Set this object to the proxy object of the actual view provider'''
        obj.addProperty("App   *   *PropertyColor","Color","Box","Color of the box").Color=(1.0,0.0,0.0)
        obj.Proxy = self

    def attach(self, obj)   *
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

    def updateData(self, fp, prop)   *
        '''If a property of the handled feature has changed we have the chance to handle this here'''
        # fp is the handled feature, prop is the name of the property that has changed
        l = fp.getPropertyByName("Length")
        w = fp.getPropertyByName("Width")
        h = fp.getPropertyByName("Height")
        self.scale.scaleFactor.setValue(float(l),float(w),float(h))
        pass

    def getDisplayModes(self,obj)   *
        '''Return a list of display modes.'''
        modes=[]
        modes.append("Shaded")
        modes.append("Wireframe")
        return modes

    def getDefaultDisplayMode(self)   *
        '''Return the name of the default display mode. It must be defined in getDisplayModes.'''
        return "Shaded"

    def setDisplayMode(self,mode)   *
        '''Map the display mode defined in attach with those defined in getDisplayModes.\
                Since they have the same names nothing needs to be done. This method is optional'''
        return mode

    def onChanged(self, vp, prop)   *
        '''Here we can do something when a single property got changed'''
        FreeCAD.Console.PrintMessage("Change property   * " + str(prop) + "\n")
        if prop == "Color"   *
            c = vp.getPropertyByName("Color")
            self.color.rgb.setValue(c[0],c[1],c[2])

    def getIcon(self)   *
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

    def __getstate__(self)   *
        '''When saving the document this object gets stored using Python's json module.\
                Since we have some un-serializable parts here -- the Coin stuff -- we must define this method\
                to return a tuple of all serializable objects or None.'''
        return None

    def __setstate__(self,state)   *
        '''When restoring the serialized object from document we have the chance to set some internals here.\
                Since no data were serialized nothing needs to be done here.'''
        return None

def makeBox()   *
    FreeCAD.newDocument()
    a=FreeCAD.ActiveDocument.addObject("App   *   *FeaturePython","Box")
    Box(a)
    ViewProviderBox(a.ViewObject)

makeBox()
```

### Things to note 

If your object relies on being recomputed as soon as it is created, you must do this manually in the `__init__` function as it is not called automatically. This example does not require it because the `onChanged` method of the `Box` class has the same effect as the `execute` function, but the examples below rely on being recomputed before anything is displayed in the 3D view. In the examples, this is done manually with `ActiveDocument.recompute()` but in more complex scenarios you need to decide where to recompute either the whole document or the FeaturePython object.

This example produces a number of exception stack traces in the report view window. This is because the `onChanged` method of the `Box` class is called each time a property is added in `__init__`. When the first one is added, the Width and Height properties don\'t exist yet and so the attempt to access them fails.

An explanation of `__getstate__` and `__setstate__` is in the forum thread [obj.Proxy.Type is a dict, not a string](https   *//forum.freecadweb.org/viewtopic.php?f=18&t=44009&start=10#p377892).

## Available methods 

See [FeaturePython methods](FeaturePython_methods.md) for the complete reference.

## Available properties 


<div class="mw-translate-fuzzy">

## Propiedades disponibles 

Las propiedades son las auténticas piedras de construcción de los objetos FeaturePython. A través de ellas, el usuario será capaz de interactuar y modificar su objeto. Después de crear un nuevo objeto FeaturePython en tu documento ( a=FreeCAD.ActiveDocument.addObject(\"App   *   *FeaturePython\",\"Box\") ), puedes obtener una lista de las propiedades disponibles escribiendo   *


</div>


```python
obj.supportedProperties()
```


<div class="mw-translate-fuzzy">

Obtendrás una lista de propiedades disponibles   *


</div>

-   [App   *   *PropertyAcceleration](FeaturePython_Custom_Properties#App   *_PropertyAcceleration.md)
-   [App   *   *PropertyAngle](FeaturePython_Custom_Properties#App   *_PropertyAngle.md)
-   [App   *   *PropertyArea](FeaturePython_Custom_Properties#App   *_PropertyArea.md)
-   [App   *   *PropertyBool](FeaturePython_Custom_Properties#App   *_PropertyBool.md)
-   [App   *   *PropertyBoolList](FeaturePython_Custom_Properties#App   *_PropertyBoolList.md)
-   [App   *   *PropertyColor](FeaturePython_Custom_Properties#App   *_PropertyColor.md)
-   [App   *   *PropertyColorList](FeaturePython_Custom_Properties#App   *_PropertyColorList.md)
-   [App   *   *PropertyDirection](FeaturePython_Custom_Properties#App   *_PropertyDirection.md)
-   [App   *   *PropertyDistance](FeaturePython_Custom_Properties#App   *_PropertyDistance.md)
-   [App   *   *PropertyEnumeration](FeaturePython_Custom_Properties#App   *_PropertyEnumeration.md)
-   [App   *   *PropertyExpressionEngine](FeaturePython_Custom_Properties#App   *_PropertyExpressionEngine.md)
-   [App   *   *PropertyFile](FeaturePython_Custom_Properties#App   *_PropertyFile.md)
-   [App   *   *PropertyFileIncluded](FeaturePython_Custom_Properties#App   *_PropertyFileIncluded.md)
-   [App   *   *PropertyFloat](FeaturePython_Custom_Properties#App   *_PropertyFloat.md)
-   [App   *   *PropertyFloatConstraint](FeaturePython_Custom_Properties#App   *_PropertyFloatConstraint.md)
-   [App   *   *PropertyFloatList](FeaturePython_Custom_Properties#App   *_PropertyFloatList.md)
-   [App   *   *PropertyFont](FeaturePython_Custom_Properties#App   *_PropertyFont.md)
-   [App   *   *PropertyForce](FeaturePython_Custom_Properties#App   *_PropertyForce.md)
-   [App   *   *PropertyFrequency](FeaturePython_Custom_Properties#App   *_PropertyFrequency.md)
-   [App   *   *PropertyInteger](FeaturePython_Custom_Properties#App   *_PropertyInteger.md)
-   [App   *   *PropertyIntegerConstraint](FeaturePython_Custom_Properties#App   *_PropertyIntegerConstraint.md)
-   [App   *   *PropertyIntegerList](FeaturePython_Custom_Properties#App   *_PropertyIntegerList.md)
-   [App   *   *PropertyIntegerSet](FeaturePython_Custom_Properties#App   *_PropertyIntegerSet.md)
-   [App   *   *PropertyLength](FeaturePython_Custom_Properties#App   *_PropertyLength.md)
-   [App   *   *PropertyLink](FeaturePython_Custom_Properties#App   *_PropertyLink.md)
-   [App   *   *PropertyLinkChild](FeaturePython_Custom_Properties#App   *_PropertyLinkChild.md)
-   [App   *   *PropertyLinkGlobal](FeaturePython_Custom_Properties#App   *_PropertyLinkGlobal.md)
-   [App   *   *PropertyLinkHidden](FeaturePython_Custom_Properties#App   *_PropertyLinkHidden.md)
-   [App   *   *PropertyLinkList](FeaturePython_Custom_Properties#App   *_PropertyLinkList.md)
-   [App   *   *PropertyLinkListChild](FeaturePython_Custom_Properties#App   *_PropertyLinkListChild.md)
-   [App   *   *PropertyLinkListGlobal](FeaturePython_Custom_Properties#App   *_PropertyLinkListGlobal.md)
-   [App   *   *PropertyLinkListHidden](FeaturePython_Custom_Properties#App   *_PropertyLinkListHidden.md)
-   [App   *   *PropertyLinkSub](FeaturePython_Custom_Properties#App   *_PropertyLinkSub.md)
-   [App   *   *PropertyLinkSubChild](FeaturePython_Custom_Properties#App   *_PropertyLinkSubChild.md)
-   [App   *   *PropertyLinkSubGlobal](FeaturePython_Custom_Properties#App   *_PropertyLinkSubGlobal.md)
-   [App   *   *PropertyLinkSubHidden](FeaturePython_Custom_Properties#App   *_PropertyLinkSubHidden.md)
-   [App   *   *PropertyLinkSubList](FeaturePython_Custom_Properties#App   *_PropertyLinkSubList.md)
-   [App   *   *PropertyLinkSubListChild](FeaturePython_Custom_Properties#App   *_PropertyLinkSubListChild.md)
-   [App   *   *PropertyLinkSubListGlobal](FeaturePython_Custom_Properties#App   *_PropertyLinkSubListGlobal.md)
-   [App   *   *PropertyLinkSubListHidden](FeaturePython_Custom_Properties#App   *_PropertyLinkSubListHidden.md)
-   [App   *   *PropertyMap](FeaturePython_Custom_Properties#App   *_PropertyMap.md)
-   [App   *   *PropertyMaterial](FeaturePython_Custom_Properties#App   *_PropertyMaterial.md)
-   [App   *   *PropertyMaterialList](FeaturePython_Custom_Properties#App   *_PropertyMaterialList.md)
-   [App   *   *PropertyMatrix](FeaturePython_Custom_Properties#App   *_PropertyMatrix.md)
-   [App   *   *PropertyPath](FeaturePython_Custom_Properties#App   *_PropertyPath.md)
-   [App   *   *PropertyPercent](FeaturePython_Custom_Properties#App   *_PropertyPercent.md)
-   [App   *   *PropertyPersistentObject](FeaturePython_Custom_Properties#App   *_PropertyPersistentObject.md)
-   [App   *   *PropertyPlacement](FeaturePython_Custom_Properties#App   *_PropertyPlacement.md)
-   [App   *   *PropertyPlacementLink](FeaturePython_Custom_Properties#App   *_PropertyPlacementLink.md)
-   [App   *   *PropertyPlacementList](FeaturePython_Custom_Properties#App   *_PropertyPlacementList.md)
-   [App   *   *PropertyPosition](FeaturePython_Custom_Properties#App   *_PropertyPosition.md)
-   [App   *   *PropertyPrecision](FeaturePython_Custom_Properties#App   *_PropertyPrecision.md)
-   [App   *   *PropertyPressure](FeaturePython_Custom_Properties#App   *_PropertyPressure.md)
-   [App   *   *PropertyPythonObject](FeaturePython_Custom_Properties#App   *_PropertyPythonObject.md)
-   [App   *   *PropertyQuantity](FeaturePython_Custom_Properties#App   *_PropertyQuantity.md)
-   [App   *   *PropertyQuantityConstraint](FeaturePython_Custom_Properties#App   *_PropertyQuantityConstraint.md)
-   [App   *   *PropertySpeed](FeaturePython_Custom_Properties#App   *_PropertySpeed.md)
-   [App   *   *PropertyString](FeaturePython_Custom_Properties#App   *_PropertyString.md)
-   [App   *   *PropertyStringList](FeaturePython_Custom_Properties#App   *_PropertyStringList.md)
-   [App   *   *PropertyUUID](FeaturePython_Custom_Properties#App   *_PropertyUUID.md)
-   [App   *   *PropertyVacuumPermittivity](FeaturePython_Custom_Properties#App   *_PropertyVacuumPermittivity.md)
-   [App   *   *PropertyVector](FeaturePython_Custom_Properties#App   *_PropertyVector.md)
-   [App   *   *PropertyVectorDistance](FeaturePython_Custom_Properties#App   *_PropertyVectorDistance.md)
-   [App   *   *PropertyVectorList](FeaturePython_Custom_Properties#App   *_PropertyVectorList.md)
-   [App   *   *PropertyVolume](FeaturePython_Custom_Properties#App   *_PropertyVolume.md)
-   [App   *   *PropertyXLink](FeaturePython_Custom_Properties#App   *_PropertyXLink.md)
-   [App   *   *PropertyXLinkList](FeaturePython_Custom_Properties#App   *_PropertyXLinkList.md)
-   [App   *   *PropertyXLinkSub](FeaturePython_Custom_Properties#App   *_PropertyXLinkSub.md)
-   [App   *   *PropertyXLinkSubList](FeaturePython_Custom_Properties#App   *_PropertyXLinkSubList.md)
-   [Mesh   *   *PropertyCurvatureList](FeaturePython_Custom_Properties#Mesh   *_PropertyCurvatureList.md)
-   [Mesh   *   *PropertyMeshKernel](FeaturePython_Custom_Properties#Mesh   *_PropertyMeshKernel.md)
-   [Mesh   *   *PropertyNormalList](FeaturePython_Custom_Properties#Mesh   *_PropertyNormalList.md)
-   [Part   *   *PropertyFilletEdges](FeaturePython_Custom_Properties#Part   *_PropertyFilletEdges.md)
-   [Part   *   *PropertyGeometryList](FeaturePython_Custom_Properties#Part   *_PropertyGeometryList.md)
-   [Part   *   *PropertyPartShape](FeaturePython_Custom_Properties#Part   *_PropertyPartShape.md)
-   [Part   *   *PropertyShapeHistory](FeaturePython_Custom_Properties#Part   *_PropertyShapeHistory.md)
-   [Path   *   *PropertyPath](FeaturePython_Custom_Properties#Path   *_PropertyPath.md)
-   [Path   *   *PropertyTool](FeaturePython_Custom_Properties#Path   *_PropertyTool.md)
-   [Path   *   *PropertyTooltable](FeaturePython_Custom_Properties#Path   *_PropertyTooltable.md)
-   [Sketcher   *   *PropertyConstraintList](FeaturePython_Custom_Properties#Sketcher   *_PropertyConstraintList.md)
-   [Spreadsheet   *   *PropertyColumnWidths](FeaturePython_Custom_Properties#Spreadsheet   *_PropertyColumnWidths.md)
-   [Spreadsheet   *   *PropertyRowHeights](FeaturePython_Custom_Properties#Spreadsheet   *_PropertyRowHeights.md)
-   [Spreadsheet   *   *PropertySheet](FeaturePython_Custom_Properties#Spreadsheet   *_PropertySheet.md)
-   [Spreadsheet   *   *PropertySpreadsheetQuantity](FeaturePython_Custom_Properties#Spreadsheet   *_PropertySpreadsheetQuantity.md)
-   [TechDraw   *   *PropertyCenterLineList](FeaturePython_Custom_Properties#TechDraw   *_PropertyCenterLineList.md)
-   [TechDraw   *   *PropertyCosmeticEdgeList](FeaturePython_Custom_Properties#TechDraw   *_PropertyCosmeticEdgeList.md)
-   [TechDraw   *   *PropertyCosmeticVertexList](FeaturePython_Custom_Properties#TechDraw   *_PropertyCosmeticVertexList.md)
-   [TechDraw   *   *PropertyGeomFormatList](FeaturePython_Custom_Properties#TechDraw   *_PropertyGeomFormatList.md)

Cuando se añaden propiedades a tus objetos personalizados, ten en cuenta esto   *

-   No utilices caracteres \"\<\" o \"\>\" en las descripciones de las propiedades (eso rompería las partes de xml en el archivo .fcstd)
-   Las propiedades se almacenan alfabéticamente en un archivo .fcstd. Si tienes una forma en tus propiedades, cualquier propiedad cuyo nombre va después de \"Shape\" en orden alfabético, se cargará DESPUÉS de la forma, lo que puede causar un comportamiento extraño.

A complete list of property attributes can be seen in the [PropertyStandard C++ header file](https   *//github.com/FreeCAD/FreeCAD/blob/master/src/App/PropertyStandard.h). For instance, if you want to allow the user to enter only a limited range of values (e.g. using PropertyIntegerConstraint), in Python you will assign a tuple containing not only the property value, but also the lower and upper limit as well as the stepsize, as below   *


```python
prop = (value, lower, upper, stepsize)
```

## Property Type 

By default the properties can be updated. It is possible to make the properties read-only, for instance in the case one wants to show the result of a method. It is also possible to hide the property. The property type can be set using   *


```python
obj.setEditorMode("MyPropertyName", mode)
```

where mode is a short int that can be set to   *

 0 -- default mode, read and write
 1 -- read-only
 2 -- hidden

The EditorModes are not set at FreeCAD file reload. This could to be done by the \_\_setstate\_\_ function. See <http   *//forum.freecadweb.org/viewtopic.php?f=18&t=13460&start=10#p108072>. By using the setEditorMode the properties are only read only in PropertyEditor. They could still be changed from python. To really make them read only the setting has to be passed directly inside the addProperty function. See <http   *//forum.freecadweb.org/viewtopic.php?f=18&t=13460&start=20#p109709> for an example.

Using the direct setting in the addProperty function, you also have more possibilities. In particular, an interesting one is mark a property as an output property. This way FreeCAD won\'t mark the feature as touched when changing it (so no need to recompute).

Example of output property (see also <https   *//forum.freecadweb.org/viewtopic.php?t=24928>)   *


```python
obj.addProperty("App   *   *PropertyString","MyCustomProperty","","",8)
```

The property types that can be set at last parameter of the addProperty function are   *

 0 -- Prop_None, No special property type
 1 -- Prop_ReadOnly, Property is read-only in the editor
 2 -- Prop_Transient, Property won't be saved to file
 4 -- Prop_Hidden, Property won't appear in the editor
 8 -- Prop_Output, Modified property doesn't touch its parent container
 16 -- Prop_NoRecompute, Modified property doesn't touch its container for recompute

You can find these different property types defined in the [source code C++ header for PropertyContainer](https   *//github.com/FreeCAD/FreeCAD/blob/master/src/App/PropertyContainer.h).

## Other more complex example 


<div class="mw-translate-fuzzy">

## Otro ejemplo más complejo 

En este ejemplo se hace uso del [Módulo de Pieza](Part_Workbench/es.md) para crear un octaedro, a continuación, se crea su representación Coin con Pivy.


</div>

Lo primero es el propio objeto del documento   *


```python
import FreeCAD, FreeCADGui, Part
import pivy
from pivy import coin

class Octahedron   *
  def __init__(self, obj)   *
     "Add some custom properties to our box feature"
     obj.addProperty("App   *   *PropertyLength","Length","Octahedron","Length of the octahedron").Length=1.0
     obj.addProperty("App   *   *PropertyLength","Width","Octahedron","Width of the octahedron").Width=1.0
     obj.addProperty("App   *   *PropertyLength","Height","Octahedron", "Height of the octahedron").Height=1.0
     obj.addProperty("Part   *   *PropertyPartShape","Shape","Octahedron", "Shape of the octahedron")
     obj.Proxy = self

  def execute(self, fp)   *
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
  def make_face(self,v1,v2,v3)   *
     wire = Part.makePolygon([v1,v2,v3,v1])
     face = Part.Face(wire)
     return face
```

después, conseguimos el objeto proveedor de vista, responsable de mostrar el objeto en la escena 3D   *


```python
class ViewProviderOctahedron   *
  def __init__(self, obj)   *
     "Set this object to the proxy object of the actual view provider"
     obj.addProperty("App   *   *PropertyColor","Color","Octahedron","Color of the octahedron").Color=(1.0,0.0,0.0)
     obj.Proxy = self

  def attach(self, obj)   *
     "Setup the scene sub-graph of the view provider, this method is mandatory"
     self.shaded = coin.SoGroup()
     self.wireframe = coin.SoGroup()
     self.scale = coin.SoScale()
     self.color = coin.SoBaseColor()

     self.data=coin.SoCoordinate3()
     self.face=coin.SoIndexedLineSet()

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

  def updateData(self, fp, prop)   *
     "If a property of the handled feature has changed we have the chance to handle this here"
     # fp is the handled feature, prop is the name of the property that has changed
     if prop == "Shape"   *
        s = fp.getPropertyByName("Shape")
        self.data.point.setNum(6)
        cnt=0
        for i in s.Vertexes   *
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

  def getDisplayModes(self,obj)   *
     "Return a list of display modes."
     modes=[]
     modes.append("Shaded")
     modes.append("Wireframe")
     return modes

  def getDefaultDisplayMode(self)   *
     "Return the name of the default display mode. It must be defined in getDisplayModes."
     return "Shaded"

  def setDisplayMode(self,mode)   *
     return mode

  def onChanged(self, vp, prop)   *
     "Here we can do something when a single property got changed"
     FreeCAD.Console.PrintMessage("Change property   * " + str(prop) + "\n")
     if prop == "Color"   *
        c = vp.getPropertyByName("Color")
        self.color.rgb.setValue(c[0],c[1],c[2])

  def getIcon(self)   *
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

  def __getstate__(self)   *
     return None

  def __setstate__(self,state)   *
     return None
```

Por último, una vez que nuestro objeto y su viewobject están definidos, sólo nos falta invocarlos   *


```python
FreeCAD.newDocument()
a=FreeCAD.ActiveDocument.addObject("App   *   *FeaturePython","Octahedron")
Octahedron(a)
ViewProviderOctahedron(a.ViewObject)
```

## Making objects selectable 


<div class="mw-translate-fuzzy">

## Haciendo objetos seleccionables 

Si deseas hacer tu objeto seleccionable, o al menos parte de el, haciendo clic sobre el en el visor, debes incluir su geometría Coin dentro de un nodo SoFCSelection. Si el objeto tiene una representación compleja, con widgets, anotaciones, etc, puede que desees incluir sólo una parte de el en un SoFCSelection. Todo lo que es un SoFCSelection es constantemente explorado por FreeCAD para detectar selección/preselección, por lo que tiene sentido evitar sobrecargalo con innecesarias exploraciones. Esto es lo que se haría para incluir un self.face en el ejemplo anterior   *


</div>

Once the parts of the scenegraph that are to be selectable are inside SoFCSelection nodes, you then need to provide two methods to handle the selection path. The selection path can take the form of a string giving the names of each element in the path, or of an array of scenegraph objects. The two methods you provide are `getDetailPath`, which converts from a string path to an array of scenegraph objects, and `getElementPicked`, which takes an element which has been clicked on in the scenegraph and returns its string name (note, not its string path).

Here is the molecule example above, adapted to make the elements of the molecule selectable   *


```python
class Molecule   *
    def __init__(self, obj)   *
        ''' Add two point properties '''
        obj.addProperty("App   *   *PropertyVector","p1","Line","Start point")
        obj.addProperty("App   *   *PropertyVector","p2","Line","End point").p2=FreeCAD.Vector(5,0,0)

        obj.Proxy = self

    def onChanged(self, fp, prop)   *
        if prop == "p1" or prop == "p2"   *
            ''' Print the name of the property that has changed '''
            fp.Shape = Part.makeLine(fp.p1,fp.p2)

    def execute(self, fp)   *
        ''' Print a short message when doing a recomputation, this method is mandatory '''
        fp.Shape = Part.makeLine(fp.p1,fp.p2)

class ViewProviderMolecule   *
    def __init__(self, obj)   *
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

    def getDetailPath(self, subname, path, append)   *
        vobj = self.ViewObject
        if append   *
            path.append(vobj.RootNode)
            path.append(vobj.SwitchNode)

            mode = vobj.SwitchNode.whichChild.getValue()
            if mode >= 0   *
                mode = vobj.SwitchNode.getChild(mode)
                path.append(mode)
                sub = Part.splitSubname(subname)[-1]
                if sub == 'Atom1'   *
                    path.append(self.sel1)
                elif sub == 'Atom2'   *
                    path.append(self.sel2)
                else   *
                    path.append(mode.getChild(0))
        return True

    def getElementPicked(self, pp)   *
        path = pp.getPath()
        if path.findNode(self.sel1) >= 0   *
            return 'Atom1'
        if path.findNode(self.sel2) >= 0   *
            return 'Atom2'
        raise NotImplementedError

    def updateData(self, fp, prop)   *
        "If a property of the handled feature has changed we have the chance to handle this here"
        # fp is the handled feature, prop is the name of the property that has changed
        if prop == "p1"   *
            p = fp.getPropertyByName("p1")
            self.trl1.translation=(p.x,p.y,p.z)
        elif prop == "p2"   *
            p = fp.getPropertyByName("p2")
            self.trl2.translation=(p.x,p.y,p.z)

    def __getstate__(self)   *
        return None

    def __setstate__(self,state)   *
        return None

def makeMolecule()   *
    FreeCAD.newDocument()
    a=FreeCAD.ActiveDocument.addObject("Part   *   *FeaturePython","Molecule")
    Molecule(a)
    ViewProviderMolecule(a.ViewObject)
    FreeCAD.ActiveDocument.recompute()
```

## Working with simple shapes 


<div class="mw-translate-fuzzy">

## Trabajar con formas simples 

Si tu objeto paramétrico saca simplemente una forma, no es necesario utilizar un objeto proveedor de vista. La forma se mostrará en la representación de formas de FreeCAD   *


</div>


```python
import FreeCAD as App
import FreeCADGui
import FreeCAD
import Part
class Line   *
    def __init__(self, obj)   *
        '''"App two point properties" '''
        obj.addProperty("App   *   *PropertyVector","p1","Line","Start point")
        obj.addProperty("App   *   *PropertyVector","p2","Line","End point").p2=FreeCAD.Vector(1,0,0)
        obj.Proxy = self

    def execute(self, fp)   *
        '''"Print a short message when doing a recomputation, this method is mandatory" '''
        fp.Shape = Part.makeLine(fp.p1,fp.p2)

a=FreeCAD.ActiveDocument.addObject("Part   *   *FeaturePython","Line")
Line(a)
a.ViewObject.Proxy=0 # just set it to something different from None (this assignment is needed to run an internal notification)
FreeCAD.ActiveDocument.recompute()
```

Same code with use **ViewProviderLine**


```python
import FreeCAD as App
import FreeCADGui
import FreeCAD
import Part

class Line   *
    def __init__(self, obj)   *
         '''"App two point properties" '''
         obj.addProperty("App   *   *PropertyVector","p1","Line","Start point")
         obj.addProperty("App   *   *PropertyVector","p2","Line","End point").p2=FreeCAD.Vector(100,0,0)
         obj.Proxy = self

    def execute(self, fp)   *
        '''"Print a short message when doing a recomputation, this method is mandatory" '''
        fp.Shape = Part.makeLine(fp.p1,fp.p2)

class ViewProviderLine   *
   def __init__(self, obj)   *
      ''' Set this object to the proxy object of the actual view provider '''
      obj.Proxy = self

   def getDefaultDisplayMode(self)   *
      ''' Return the name of the default display mode. It must be defined in getDisplayModes. '''
      return "Flat Lines"

a=FreeCAD.ActiveDocument.addObject("Part   *   *FeaturePython","Line")
Line(a)
ViewProviderLine(a.ViewObject)
App.ActiveDocument.recompute()
```

## Scenegraph Structure 

You may have noticed that the examples above construct their scenegraphs in slightly different ways. Some use `obj.addDisplayMode(node, "modename")` while others use `obj.SwitchNode.getChild(x).addChild(y)`.

Each feature in a FreeCAD document is based the following scenegraph structure   *


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

Here is the above molecule example, adapted to be drawn only with Coin3D scenegraph objects instead of using objects from the Part workbench   *


```python
import Part
from pivy import coin

class Molecule   *
    def __init__(self, obj)   *
        ''' Add two point properties '''
        obj.addProperty("App   *   *PropertyVector","p1","Line","Start point")
        obj.addProperty("App   *   *PropertyVector","p2","Line","End point").p2=FreeCAD.Vector(5,0,0)

        obj.Proxy = self

    def onChanged(self, fp, prop)   *
        pass

    def execute(self, fp)   *
        ''' Print a short message when doing a recomputation, this method is mandatory '''
        pass

class ViewProviderMolecule   *
    def __init__(self, obj)   *
        ''' Set this object to the proxy object of the actual view provider '''
        self.constructed = False
        obj.Proxy = self
        self.ViewObject = obj

    def attach(self, obj)   *
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

    def getDetailPath(self, subname, path, append)   *
        vobj = self.ViewObject
        if append   *
            path.append(vobj.RootNode)
            path.append(vobj.SwitchNode)

            mode = vobj.SwitchNode.whichChild.getValue()
            FreeCAD.Console.PrintWarning("getDetailPath   * mode {} is active\n".format(mode))
            if mode >= 0   *
                mode = vobj.SwitchNode.getChild(mode)
                path.append(mode)
                sub = Part.splitSubname(subname)[-1]
                print(sub)
                if sub == 'Atom1'   *
                    path.append(self.sel1)
                elif sub == 'Atom2'   *
                    path.append(self.sel2)
                elif sub == 'Line'   *
                    path.append(self.sel3)
                else   *
                    path.append(mode.getChild(0))
        return True

    def getElementPicked(self, pp)   *
        path = pp.getPath()
        if path.findNode(self.sel1) >= 0   *
            return 'Atom1'
        if path.findNode(self.sel2) >= 0   *
            return 'Atom2'
        if path.findNode(self.sel3) >= 0   *
            return 'Line'
        raise NotImplementedError

    def updateData(self, fp, prop)   *
        "If a property of the handled feature has changed we have the chance to handle this here"
        # fp is the handled feature, prop is the name of the property that has changed
        if not self.constructed   *
            return
        if prop == "p1"   *
            p = fp.getPropertyByName("p1")
            self.coords.point.set1Value(0, p)
        elif prop == "p2"   *
            p = fp.getPropertyByName("p2")
            self.coords.point.set1Value(1, p)

    def getDisplayModes(self, obj)   *
        return ['Wireframe', 'Shaded']

    def getDefaultDisplayMode(self)   *
        return 'Shaded'

    def setDisplayMode(self, mode)   *
        return mode

    def __getstate__(self)   *
        return None

    def __setstate__(self,state)   *
        return None

def makeMolecule()   *
    FreeCAD.newDocument()
    a=FreeCAD.ActiveDocument.addObject("App   *   *FeaturePython","Molecule")
    Molecule(a)
    b=ViewProviderMolecule(a.ViewObject)
    a.touch()
    FreeCAD.ActiveDocument.recompute()
    return a,b

a,b = makeMolecule()
```

## Part Design scripted objects 

When making scripted objects in Part Design the process is similar to the scripted objects discussed above, but with a few additional considerations. We must handle 2 shape properties, one for the shape we see in the 3D view and another for the shape used by the pattern tools, such as polar pattern features. The object shapes also needs to be fused to any existing material already in the Body (or cut from it in the case of Subtractive features). And we must account for the placement and attachment of our objects a little bit differently.

Part Design scripted solid object features should be based on either PartDesign   *   *FeaturePython, PartDesign   *   *FeatureAdditivePython, or PartDesign   *   *FeatureSubtractivePython rather than Part   *   *FeaturePython. Only the Additive and Subtractive variants can be used in pattern features, and if based on Part   *   *FeaturePython when the user drops the object into a Part Design Body it becomes a BaseFeature rather than being treated by the Body as a native Part Design object. Note   * all of these are expected to be solids, so if you are making a non-solid feature it should be based on Part   *   *FeaturePython or else the next feature in the tree will attempt to fuse to as a solid and it will fail.

Here is a simple example of making a Tube primitive, similar to the Tube primitive in Part Workbench except this one will be a Part Design solid feature object. For this we will 2 separate files   * pdtube.FCMacro and pdtube.py. The .FCMacro file will be executed by the user to create the object. The .py file will hold the class definitions, imported by the .FCMacro. The reason for doing it this way is to maintain the parametric nature of the object after restarting FreeCAD and opening a document containing one of our Tubes.

First, the class definition file   *


```python
# -*- coding   * utf-8 -*-
#classes should go in pdtube.py
import FreeCAD, FreeCADGui, Part
class PDTube   *
    def __init__(self,obj)   *
        obj.addProperty("App   *   *PropertyLength","Radius1","Tube","Radius1").Radius1 = 5
        obj.addProperty("App   *   *PropertyLength","Radius2","Tube","Radius2").Radius2 = 10
        obj.addProperty("App   *   *PropertyLength","Height","Tube","Height of tube").Height = 10
        self.makeAttachable(obj)
        obj.Proxy = self

    def makeAttachable(self, obj)   *

        if int(FreeCAD.Version()[1]) >= 19   *
            obj.addExtension('Part   *   *AttachExtensionPython')
        else   *
            obj.addExtension('Part   *   *AttachExtensionPython', obj)

        obj.setEditorMode('Placement', 0) #non-readonly non-hidden

    def execute(self,fp)   *
        outer_cylinder = Part.makeCylinder(fp.Radius2, fp.Height)
        inner_cylinder = Part.makeCylinder(fp.Radius1, fp.Height)
        if fp.Radius1 == fp.Radius2   * #just make cylinder
            tube_shape = outer_cylinder
        elif fp.Radius1 < fp.Radius2   *
            tube_shape = outer_cylinder.cut(inner_cylinder)
        else   * #invert rather than error out
            tube_shape = inner_cylinder.cut(outer_cylinder)

        if not hasattr(fp, "positionBySupport")   *
            self.makeAttachable(fp)
        fp.positionBySupport()
        tube_shape.Placement = fp.Placement

        #BaseFeature (shape property of type Part   *   *PropertyPartShape) is provided for us
        #with the PartDesign   *   *FeaturePython and related classes, but it might be empty
        #if our object is the first object in the tree.  it's a good idea to check
        #for its existence in case we want to make type Part   *   *FeaturePython, which won't have it

        if hasattr(fp, "BaseFeature") and fp.BaseFeature != None   *
            if "Subtractive" in fp.TypeId   *
                full_shape = fp.BaseFeature.Shape.cut(tube_shape)
            else   *
                full_shape = fp.BaseFeature.Shape.fuse(tube_shape)
            full_shape.transformShape(fp.Placement.inverse().toMatrix(), True) #borrowed from gears workbench
            fp.Shape = full_shape
        else   *
            fp.Shape = tube_shape
        if hasattr(fp,"AddSubShape")   * #PartDesign   *   *FeatureAdditivePython and
                                      #PartDesign   *   *FeatureSubtractivePython have this
                                      #property but PartDesign   *   *FeaturePython does not
                                      #It is the shape used for copying in pattern features
                                      #for example in making a polar pattern
            tube_shape.transformShape(fp.Placement.inverse().toMatrix(), True)
            fp.AddSubShape = tube_shape

class PDTubeVP   *
    def __init__(self, obj)   *
        '''Set this object to the proxy object of the actual view provider'''
        obj.Proxy = self

    def attach(self,vobj)   *
        self.vobj = vobj

    def updateData(self, fp, prop)   *
        '''If a property of the handled feature has changed we have the chance to handle this here'''
        pass

    def getDisplayModes(self,obj)   *
        '''Return a list of display modes.'''
        modes=[]
        modes.append("Flat Lines")
        modes.append("Shaded")
        modes.append("Wireframe")
        return modes

    def getDefaultDisplayMode(self)   *
        '''Return the name of the default display mode. It must be defined in getDisplayModes.'''
        return "Flat Lines"

    def setDisplayMode(self,mode)   *
        '''Map the display mode defined in attach with those defined in getDisplayModes.\
                Since they have the same names nothing needs to be done. This method is optional'''
        return mode

    def onChanged(self, vp, prop)   *
        '''Here we can do something when a single property got changed'''
        #FreeCAD.Console.PrintMessage("Change property   * " + str(prop) + "\n")
        pass

    def getIcon(self)   *
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

    def __getstate__(self)   *
        '''When saving the document this object gets stored using Python's json module.\
                Since we have some un-serializable parts here -- the Coin stuff -- we must define this method\
                to return a tuple of all serializable objects or None.'''
        return None

    def __setstate__(self,state)   *
        '''When restoring the serialized object from document we have the chance to set some internals here.\
                Since no data were serialized nothing needs to be done here.'''
        return None
```

And now the macro file to create the object   *


```python
# -*- coding   * utf-8 -*-

#pdtube.FCMacro
import pdtube
#above line needed if the class definitions above are place in another file   * PDTube.py
#this is needed if the tube object is to remain parametric after restarting FreeCAD and loading
#a document containing the object

body = FreeCADGui.ActiveDocument.ActiveView.getActiveObject("pdbody")
if not body   *
    FreeCAD.Console.PrintError("No active body.\n")
else   *
    from PySide import QtGui
    window = FreeCADGui.getMainWindow()
    items = ["Additive","Subtractive","Neither additive nor subtractive"]
    item,ok =QtGui.QInputDialog.getItem(window,"Select tube type","Select whether you want additive, subtractive, or neither   *",items,0,False)
    if ok   *
        if item == items[0]   *
            className = "PartDesign   *   *FeatureAdditivePython"
        elif item == items[1]   *
            className = "PartDesign   *   *FeatureSubtractivePython"
        else   *
            className = "PartDesign   *   *FeaturePython" #not usable in pattern features, such as polar pattern

        tube = FreeCAD.ActiveDocument.addObject(className,"Tube")
        pdtube.PDTube(tube)
        pdtube.PDTubeVP(tube.ViewObject)
        body.addObject(tube) #optionally we can also use body.insertObject() for placing at particular place in tree
```


<div class="mw-translate-fuzzy">


{{docnav/es|PySide/es|Embedding FreeCAD/es}}


</div>

Additional pages   *

-   [Scripted objects saving attributes](Scripted_objects_saving_attributes.md)
-   [Scripted objects migration](Scripted_objects_migration.md)
-   [Scripted objects with attachment](Scripted_objects_with_attachment.md)
-   [Viewproviders](Viewprovider.md)

Interesting forum threads about scripted objects   *

-   [Python object attributes lost at load](http   *//forum.freecadweb.org/viewtopic.php?f=22&t=13740)
-   [New FeaturePython is grey](http   *//forum.freecadweb.org/viewtopic.php?t=12139)
-   [Explanation on \_\_getstate\_\_ and \_\_setstate\_\_](https   *//forum.freecadweb.org/viewtopic.php?f=18&t=44009), [official documentation](https   *//docs.python.org/3/library/pickle.html#object.__getstate__)
-   [Eigenmode frequency always 0?](https   *//forum.freecadweb.org/viewtopic.php?f=18&t=13460&start=20#p109709)
-   [how to implement python feature\'s setEdit properly?](https   *//forum.freecadweb.org/viewtopic.php?f=22&t=21330)

In addition to the examples presented here have a look at FreeCAD source code [src/Mod/TemplatePyMod/FeaturePython.py](https   *//github.com/FreeCAD/FreeCAD/blob/master/src/Mod/TemplatePyMod/FeaturePython.py) for more examples.







[Category   *Developer Documentation](Category_Developer_Documentation.md) [Category   *Python Code](Category_Python_Code.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Scripted objects/es
