# App OriginGroupExtension/de
## Einführung

Ein [App-Origin](App_OriginGroupExtension.md)-Object, oder formal `App::OriginGroupExtension`, ist eine Klasse, die auswählbare Elemente, die die drei Standardachsen (X, Y, Z) und die drei Standardebenen (XY, XZ und YZ) darstellen, den Objekten zur Verfügung stellt, die dazu bestimmt sind, verschiedene Arten von Geometrien im Raum anzuordnen.

<img alt="" src=images/Std_Part.svg  style="width:16px;"> [Std-Part](Std_Part/de.md)-Objekte [(App-Part-Objekte)](App_Part/de.md) und <img alt="" src=images/PartDesign_Body.svg  style="width:16px;"> [PartDesign-Body](PartDesign_Body/de.md)-Objekt werden standardmäßig mit Ursprungsobjekten erstellt. Wenn erforderlich, können Ursprungsobjekte auch den <img alt="" src=images/Assembly_Assembly_Tree.svg  style="width:16px;"> [Baugruppen](Assembly3_CreateAssembly/de.md)-Objekten dem Arbeitsbereich <img alt="" src=images/Assembly3_workbench_icon.svg  style="width:16px;"> [Assembly3](Assembly3_Workbench.md) hinzugefügt werden.

<img alt="Tree view" src=images/App_OriginGroupExtension_example.png  style="width:200px;"> <img alt="3D view" src=images/App_OriginGroupExtension-02.png  style="width:400px;"> 
*Links: Die [Baumansicht](Tree_view/de.md) zeigt drei Objekte, die Ursprungsobjekte verwenden. Rechts: Darstellung der Ursprungselemente in der [3D-Ansicht](3D_view/de.md).*

Die Achsen und Ebenen sind vom Typ `App::Line` bzw. `App::Plane`. Jedes dieser Elemente kann mit der **Leertaste** einzeln ein- bzw. ausgeblendet werden. Dies kann nützlich sein bei der Auswahl der richtigen Referenz für die Erstellung anderer Objekte, wie z. B. [Skizzen](Sketch/de.md).

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Vereinfachtes Diagramm der Beziehungen zwischen den Kernobjekten im Programm. Zwei von ihnen besitzen ein Origin-Objekt (Ursprung), um die Lage der Objekte zu bestimmen, die unter ihnen gruppiert sind.*


{{Document_objects_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > App OriginGroupExtension/de
