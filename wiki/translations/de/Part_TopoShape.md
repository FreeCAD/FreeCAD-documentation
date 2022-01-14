# Part TopoShape/de
{{TOCright}}

## Einführung

Eine [Part TopoForm](Part_TopoShape/de.md), oder formal eine `Part::TopoShape`, ist eine Klasse, die eine parametrische *\'topologische Form* in der Software definiert. Objekte im Dokument, die etwas in der [3D Ansicht](3D_view/de.md) zeigen, haben normalerweise eine TopoForm.

Die topologischen Formen sowie deren Methoden werden durch den [OpenCASCADE Technologie](OpenCASCADE/de.md) Kernel (OCCT) definiert. FreeCAD verwendet diese Formen und baut [Anwendung DokumentObjekte](App_DocumentObject/de.md) um sie herum.

Eine andere Art von Klasse ist die des [Polygonnetzes](Mesh/de.md); diese Klasse ist nicht sehr parametrisch, da sie nicht einfach umdefiniert werden kann, außer durch die Angabe einzelner Knoten und dreieckiger Oberflächen.

![](images/Shape_and_mesh.svg )



*Links: parametrische [Part_TopoForm](Part_TopoShape/de.md), definiert durch Eigenschaften. Rechts: nichtparametrisches [Polygonnetz](Mesh/de.md), definiert durch Knoten und und dreieckigen Oberflächen.*

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Vereinfachtes Diagramm der Beziehungen zwischen den Kernobjekten im Programm. Die Klasse `Part::TopoShape* wird in das {{incode|Part::Feature` Objekt eingebettet und von dort auf alle davon abgeleiteten Objekte übertragen.}}

## Anwendung

Die Part TopoForm ist ein Objekt, das einigen [Anwendung DokumentObjekten](App_DocumentObject/de.md) zugeordnet ist.

Insbesondere das Basisobjekt, das diese Arten von Attributen handhabt, ist die [Part Formelement](Part_Feature/de.md) (`Part::Feature` Klasse). Alle von dieser Klasse abgeleiteten Objekte haben Zugriff auf eine Part TopoForm.

Einige der wichtigsten Objekte mit Part TopoForm sind die folgenden:

-   Jeder primitive Festkörper, der mit der [Part Arbeitsbereich](Part_Workbench/de.md) erstellt wurde.
-   Jeder beliebige [PartDesign Körper](PartDesign_Body/de.md) und [PartDesign Formelement](PartDesign_Feature/de.md), das mit dem [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md) erstellt wurde.
-   Jedes Objekt, das von [Part Teilzu2DObjekt](Part_Part2DObject/de.md) abgeleitet ist, wie die meisten mit der [Entwurf Arbeitsbereich](Draft_Workbench/de.md) erstellten Objekte.
-   Jede [Skizze](Sketch/de.md), d.h. [Skizzierer SkizzenObjekt](Sketcher_SketchObject/de.md), das mit dem [Skizzierer Arbeitsbereich](Sketcher_Workbench/de.md) erstellt wurde.
-   Jedes Objekt, das durch den Import von STEP, BREP und ähnlichen Festkörperformatdateien erstellt wurde.

## Skripten


**Siehe auch:**

[FreeCAD Skripten Grundlagen](FreeCAD_Scripting_Basics/de.md), und [geskriptete Objekte](scripted_objects/de.md).

Alle Objekte abgeleitet von `Part::Feature` werden eine [Part TopoForm](Part_TopoShape/de.md) haben, die normalerweise über ihr `Shape` Attribut zugänglich ist. 
```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Part::Box", "Box")
print(obj.Shape)
```

Eine TopoForm hat viele Attribute (Variablen) und Methoden, die Informationen über sie enthalten, und die es erlauben, Operationen mit ihr durchzuführen. Diese Variablen und Methoden können in der [Python Konsole](Python_console/de.md) getestet werden. 
```python
print(obj.Shape.Area)
print(obj.Shape.BoundBox)
print(obj.Shape.CenterOfMass)
print(obj.Shape.ShapeType)

obj.Shape.check()
obj.Shape.copy()
obj.Shape.exportStep("my_file.step")
obj.Shape.exportStl("my_file.stl")
```

Eine vollständige Liste der Attribute und Methoden kannst Du in der [Quelldokumentation](Source_documentation/de.md) und dem **[<img src=images/Std_PythonHelp.svg style="width:16px"> [Std PythonHilfe](Std_PythonHelp/de.md)** Werkzeug nachschlagen.

Du kannst eine schnelle Zusammenfassung aller Methoden erhalten ddurch Verwendung der in Python eingebauten `help()` Funktion. 
```python
help(obj.Shape)
```


 {{Document objects navi}}

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part TopoShape/de
