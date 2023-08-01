# Scripted objects/fr
## Introduction

Outre les types d\'objets standard tels que les annotations, les maillages et les objets de pièces, FreeCAD offre également l\'étonnante possibilité de construire des objets paramétrique 100% Python, appelés [Python Features](App_FeaturePython/fr.md). Ces objets se comporteront exactement comme tout autre objet FreeCAD, et seront enregistrés et restaurés automatiquement lors de la sauvegarde/du chargement du fichier.

Une particularité doit être comprise : pour des raisons de sécurité, les fichiers FreeCAD ne portent jamais de code embarqué. Le code Python que vous écrivez pour créer des objets paramétriques n\'est jamais enregistré dans un fichier. Cela signifie que si vous ouvrez un fichier contenant un tel objet sur une autre machine, si ce code Python n\'est pas disponible sur cette machine, l\'objet ne sera pas entièrement recréé. Si vous distribuez de tels objets à d\'autres, vous devrez également distribuer votre script Python, par exemple sous forme de [Macro](Macros/fr.md).

**Remarque** : Il est possible d\'empaqueter du code Python dans un fichier FreeCAD en utilisant la sérialisation json avec un App::PropertyPythonObject, mais ce code ne peut jamais être exécuté directement et a donc peu d\'utilité pour notre propos ici.

Les [Python Features](App_FeaturePython/fr.md) suivent la même règle que toutes les fonctionnalités FreeCAD : elles sont séparées en plusieurs parties App (application) et GUI (interface graphique). La partie applicative, l\'objet document, définit la géométrie de notre objet, tandis que sa partie graphique, l\'objet fournisseur de vues, définit la façon dont l\'objet sera affiché à l\'écran. L\'outil View Provider Object (créateur de vue), comme toute autre fonctionnalité de FreeCAD, n\'est disponible que lorsque vous exécutez FreeCAD dans sa propre interface graphique. Plusieurs propriétés et méthodes sont disponibles pour construire votre objet. Les propriétés doivent être de l\'un des types de propriétés prédéfinis offerts par FreeCAD et apparaîtront dans la fenêtre de visualisation des propriétés, de sorte qu\'elles puissent être modifiées par l\'utilisateur. De cette façon, les objets FeaturePython sont véritablement et totalement paramétriques. Vous pouvez définir les propriétés de l\'objet et de l\'affichage ViewObject de l\'objet séparément.



## Exemples de base 

L\'exemple suivant peut être trouvé dans le fichier [src/Mod/TemplatePyMod/FeaturePython.py](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/TemplatePyMod/FeaturePython.py), avec beaucoup d\'autres exemples:


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



### Choses à noter 

Si votre objet doit être recalculé dès sa création, vous devez le faire manuellement dans la fonction `__init__` car il n\'est pas appelé automatiquement. Cet exemple n\'en a pas besoin car la méthode `onChanged` de la classe `Box` a le même effet que la fonction `execute`, mais les exemples ci-dessous reposent sur le fait d\'être recalculés avant que quoi que ce soit ne soit affiché dans la vue 3D. Dans les exemples, cela est fait manuellement avec `ActiveDocument.recompute()` mais dans des scénarios plus complexes, vous devez décider où recalculer soit le document entier, soit l\'objet FeaturePython.

Cet exemple produit un certain nombre de traces de la pile d\'exception dans la fenêtre de visualisation du rapport. En effet, la méthode `onChanged` de la classe `Box` est appelée chaque fois qu\'une propriété est ajoutée dans `__init__`. Lorsque la première est ajoutée, les propriétés Width et Height n\'existent pas encore et la tentative d\'y accéder échoue donc.

Une explication de `__getstate__` et `__setstate__` se trouve dans le fil de discussion du forum [obj.Proxy.Type is a dict, not a string](https://forum.freecadweb.org/viewtopic.php?f=18&t=44009&start=10#p377892).



## Méthodes disponibles 

Voir [Méthodes FeaturePython](FeaturePython_methods/fr.md) pour la référence complète.



## Propriétés disponibles 

Les propriétés sont les bases des FeaturePython objets. Grâce à elles, l\'utilisateur est en mesure d\'interagir et de modifier son objet. Après avoir créé un nouveau FeaturePython dans votre document ( obj=FreeCAD.ActiveDocument.addObject(\"App::FeaturePython\",\"Box\") ), ses propriétés sont directement accessibles, vous pouvez obtenir la liste,
en faisant:


```python
obj.supportedProperties()
```

Vous obtiendrez une liste des propriétés disponibles, décrites plus en détail sur la page [Propriétés personnalisées de FeaturePython](FeaturePython_Custom_Properties/fr.md) :

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

Lors de l\'ajout de propriétés à vos objets, prenez soin de ceci :

-   Ne pas utiliser de caractères **\"\<\"** ou **\"\>\"** dans les descriptions des propriétés (qui coupent des portions de code dans le fichier xml.Fcstd)
-   Les propriétés sont stockées dans un fichier texte .Fcstd.
-   Toutes les **propriétés** dont le nom vient après \"Shape\" sont triés dans l\'ordre alphabétique, donc, si vous avez une forme dans vos propriétés, et comme les propriétés sont chargées après la forme, il peut y avoir des comportements inattendus!

Une liste complète des attributs de propriété est disponible dans le [fichier d'en-tête PropertyStandard C++](https://github.com/FreeCAD/FreeCAD/blob/master/src/App/PropertyStandard.h). Par exemple, si vous souhaitez autoriser l\'utilisateur à saisir uniquement une plage de valeurs limitée (par exemple, à l\'aide de PropertyIntegerConstraint), vous affecterez à Python un tuple contenant non seulement la valeur de la propriété, mais également les limites inférieure et supérieure, ainsi que l\'incrément, comme ci-dessous :


```python
prop = (value, lower, upper, stepsize)
```



## Type de propriété 

Par défaut, les propriétés peuvent être actualisées. Il est possible de rendre les propriétés en lecture seule, par exemple dans le cas ou l\'on veut montrer le résultat d\'une méthode. Il est également possible de cacher la propriété. Le type de propriété peut être définie à l\'aide :


```python
obj.setEditorMode("MyPropertyName", mode)
```

Mode est un **integer court** qui peut avoir la valeur:

 0 -- mode par défaut, lecture et écriture
 1 -- lecture seule
 2 -- caché

Les EditorModes ne sont pas fixés dans le fichier reload de FreeCAD. Cela pourrait être fait par la fonction \_\_setstate\_\_. Voir <http://forum.freecadweb.org/viewtopic.php?f=18&t=13460&start=10#p108072> En utilisant les propriétés de setEditorMode vous ne savez que lire dans PropertyEditor. Les propriétés pourraient encore être modifiées à partir d\'une commande Python. Pour faire une lecture seul le réglage doit être transmis directement à la fonction d\'ajout de propriété. Voir le topic <http://forum.freecadweb.org/viewtopic.php?f=18&t=13460&start=20#p109709> pour voir un exemple.

En utilisant le paramètre direct dans la fonction addProperty, vous avez également plus de possibilités. En particulier, un point intéressant est de marquer une propriété en tant que propriété en sortie. De cette façon, FreeCAD ne marquera pas la fonctionnalité comme étant touchée lors de la modification (inutile donc de recalculer).

Exemple de sortie de property (see also <https://forum.freecadweb.org/viewtopic.php?t=24928>) :


```python
obj.addProperty("App::PropertyString","MyCustomProperty","","",8)
```

Les types de propriétés pouvant être définis au dernier paramètre de la fonction addProperty sont les suivants :

  0 -- Prop_None, pas de type de propriété spécial
  1 -- Prop_ReadOnly, la propriété est en lecture seule dans l'éditeur
  2 -- Prop_Transient, la propriété ne sera pas sauvegardée dans un fichier
  4 -- Prop_Hidden, la propriété n'apparaîtra pas dans l'éditeur
  8 -- Prop_Output, modifier la propriété  ne touche pas son conteneur parent
  16 - Prop_NoRecompute, modifier la propriété ne touche pas son conteneur pour le recalcul
  32 -- Prop_NoPersist, la propriété ne sera pas du tout sauvegardée dans le fichier

Vous pouvez trouver ces différents types de propriétés définis dans [source code C++ header for PropertyContainer](https://github.com/FreeCAD/FreeCAD/blob/master/src/App/PropertyContainer.h).



## Autres exemples plus complexes 

Cet exemple utilise l\'[Atelier Part](Part_Workbench/fr.md) pour créer un [octaèdre](http://fr.wikipedia.org/wiki/Octaèdre), puis crée sa représentation **[coin](http://www.coin3d.org/) avec pivy**

En premier, c\'est **l\'objet document** lui-même:


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

Puis, nous avons **view provider object**, qui est responsable d\'afficher l\'objet dans la scène 3D (votre projet à l\'écran) :


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

Enfin, une fois que notre objet et son **viewobject** sont définis, nous n\'avons plus qu\'a les appeler (la classe Octahedron et le code de la classe viewprovider peuvent être copiés directement dans la console python FreeCAD) :


```python
FreeCAD.newDocument()
a=FreeCAD.ActiveDocument.addObject("App::FeaturePython","Octahedron")
Octahedron(a)
ViewProviderOctahedron(a.ViewObject)
```



## Création d\'objets sélectionnables 

Si vous souhaitez rendre votre objet sélectionnable, ou au moins une partie de celui-ci, en cliquant dessus dans la fenêtre, vous devez inclure sa géométrie de pièce dans un nœud SoFCSelection. Si votre objet a une représentation complexe, avec des widgets, des annotations, etc\..., vous souhaiterez peut-être n\'en inclure qu\'une partie dans une SoFCSelection. Tout ce qui est un SoFCSelection est constamment analysé par FreeCAD pour détecter la sélection/présélection, il est donc logique de ne pas le surcharger avec un balayage inutile.

Une fois que les parties du scénario qui doivent être sélectionnables se trouvent à l\'intérieur des nœuds SoFCSelection, vous devez alors fournir deux méthodes pour gérer le chemin de sélection. Le chemin de sélection peut prendre la forme d\'une chaîne donnant les noms de chaque élément du chemin ou d\'un tableau d\'objets scénographiques. Les deux méthodes que vous fournissez sont `getDetailPath` qui convertit un chemin de chaîne en un tableau d\'objets de scénario, et `getElementPicked` qui prend un élément sur lequel on a cliqué dans le scénario et renvoie son nom de chaîne (notez, pas son chemin de chaîne).

Voici l\'exemple de molécule ci-dessus, adapté pour rendre les éléments de la molécule sélectionnables :


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



## Travailler avec des formes simples 

Si votre objet paramétrique renvoie simplement une forme, vous n\'avez pas besoin d\'utiliser un objet créateur de vue (*view provider object*). La forme sera affichée à l\'aide du module standard de représentation des formes de FreeCAD :


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

Même code en utilisant **ViewProviderLine**


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



## Structure du scénogramme 

Vous avez peut-être remarqué que les exemples ci-dessus construisent leurs scénarios de manière légèrement différente. Certains utilisent `obj.addDisplayMode(node, "modename")` tandis que d\'autres utilisent `obj.SwitchNode.getChild(x).addChild(y)`.

Chaque fonctionnalité d\'un document FreeCAD est basée sur la structure du scénogramme suivant :


```python
RootNode
 \- SwitchNode
     \- Shaded
      - Wireframe
      - etc
```


`SwitchNode`

n\'affiche qu\'un seul de ses enfants selon le mode d\'affichage sélectionné dans FreeCAD.

Les exemples qui utilisent `addDisplayMode` construisent leurs scénogrammes uniquement à partir d\'éléments de scénogrammes coin3d. Sous le capot, `addDisplayMode` ajoute un nouvel enfant à `SwitchNode`. Le nom de ce nœud correspondra au mode d\'affichage auquel il a été transmis.

Les exemples qui utilisent `SwitchNode.getChild(x).addChild` construisent également une partie de leur géométrie à l\'aide des fonctions de l\'atelier Part, telles que `1=fp.Shape = Part.makeLine(fp.p1,fp.p2)`. Cela construit les différents scénogrammes de mode d\'affichage sous le `SwitchNode`. Lorsque nous arriverons plus tard à ajouter des éléments coin3d au scénogramme, nous devrons les ajouter aux scénogrammes existants en mode d\'affichage en utilisant `addChild` plutôt que de créer un nouvel enfant de `SwitchNode`.

Lorsque vous utilisez `addDisplayMode()` pour ajouter une géométrie au graphe de scène, chaque mode d\'affichage doit avoir son propre nœud qui est transmis à `addDisplayMode()`. Ne réutilisez pas le même nœud pour cela. Cela entraînerait une confusion dans le mécanisme de sélection. C\'est correct si chaque nœud du mode d\'affichage a les mêmes nœuds de géométrie ajoutés en dessous, juste la racine de chaque mode d\'affichage doit être distincte.

Exemple de molécule ci-dessus, adapté pour être dessiné uniquement avec des objets scénégraphiques Coin3D au lieu d\'utiliser des objets de l\'atelier Part :


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



## Objets scriptés dans Part Design 

Lors de la création d\'objets scriptés dans Part Design, le processus est similaire à celui des objets scriptés abordés ci-dessus, mais avec quelques considérations supplémentaires. Nous devons gérer deux propriétés de forme, l\'une pour la forme que nous voyons dans la vue 3D et l\'autre pour la forme utilisée par les outils de patronage, comme les caractéristiques du motif polaire. Les formes de l\'objet doivent également être fusionnées à tout matériau existant déjà dans le corps (ou découpées dans le cas de caractéristiques soustractives). Et nous devons tenir compte de l\'emplacement et de la fixation de nos objets de manière un peu différente.

Les caractéristiques d\'objet solide écrites dans Part Design doivent être basées sur PartDesign::FeaturePython, PartDesign::FeatureAdditivePython ou PartDesign::FeatureSubtractivePython plutôt que sur Part::FeaturePython. Seules les variantes additives et soustractives peuvent être utilisées dans les caractéristiques de motifs, et si elles sont basées sur Part::FeaturePython, lorsque l\'utilisateur dépose l\'objet dans un corps Part Design, il devient une BaseFeature au lieu d\'être traité par le corps comme un objet Part Design natif. Remarque : toutes ces caractéristiques sont censées être des solides, donc si vous créez une caractéristique non solide, elle doit être basée sur Part::FeaturePython, sinon la caractéristique suivante dans l\'arbre tentera de fusionner avec un solide et échouera.

Voici un exemple simple de création d\'une primitive Tube, similaire à la primitive Tube dans l\'atelier Part sauf que celle-ci sera un objet solide Part Design. Pour cela, nous utiliserons deux fichiers distincts : pdtube.FCMacro et pdtube.py. Le fichier .FCMacro sera exécuté par l\'utilisateur pour créer l\'objet. Le fichier .py contiendra les définitions des classes, importées par le fichier .FCMacro. La raison pour laquelle nous procédons de cette manière est de maintenir la nature paramétrique de l\'objet après avoir redémarré FreeCAD et ouvert un document contenant l\'un de nos Tubes.

Tout d\'abord, le fichier de définition de la classe :


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

Et maintenant le fichier macro pour créer l\'objet :


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



## Plus d\'informations 

Pages supplémentaires :

-   [Objets créés par script enregistrant des attributs](Scripted_objects_saving_attributes/fr.md)
-   [Scripted objects migration](Scripted_objects_migration.md)
-   [Objets créés par script avec pièce jointe](Scripted_objects_with_attachment/fr.md)
-   [Viewproviders](Viewprovider/fr.md)

Fils de discussion intéressants sur les objets scriptés :

-   [Python object attributes lost at load](http://forum.freecadweb.org/viewtopic.php?f=22&t=13740)
-   [New FeaturePython is grey](http://forum.freecadweb.org/viewtopic.php?t=12139)
-   [Explanation on \_\_getstate\_\_ and \_\_setstate\_\_](https://forum.freecadweb.org/viewtopic.php?f=18&t=44009), [official documentation](https://docs.python.org/3/library/pickle.html#object.__getstate__)
-   [Eigenmode frequency always 0?](https://forum.freecadweb.org/viewtopic.php?f=18&t=13460&start=20#p109709)
-   [how to implement python feature\'s setEdit properly?](https://forum.freecadweb.org/viewtopic.php?f=22&t=21330)

En plus de ces exemples, vous pouvez voir dans le code source de FreeCAD [src/Mod/TemplatePyMod/FeaturePython.py](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/TemplatePyMod/FeaturePython.py) pour plus d\'exemples.



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Scripted objects/fr
