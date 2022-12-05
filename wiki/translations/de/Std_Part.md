---
- GuiCommand:/de
   Name:Std Part
   Name/de:Std Baugruppe
   MenuLocation:None
   Workbenches:All
   Version:0.17
   SeeAlso:[Std Gruppe](Std_Group/de.md), [PartDesign Körper](PartDesign_Body/de.md)
---

# Std Part/de

## Beschreibung


**[<img src=images/Std_Part.svg style="width:16px"> [Std Teil](Std_Part/de.md)**

, intern [App-Part](App_Part/de.md) genannt, ist ein Sammelbehälter zur allgemeinen Verwendung, der eine Gruppe von Objekten (Baugruppe) zusammenhält, so dass sie zusammen als Einheit in der [3D-Ansicht](3D_view/de.md) bewegt werden können.

Das \'Std Part\'-Element wurde entwickelt, um als Grundbaustein zur Zusammenstellung von mechanischen [Zusammenbauten](assembly/de.md) (Baugruppen) zu dienen. Es dient zum Anordnen von Objekten, die eine [Part TopoForm](Part_TopoShape/de.md) haben, wie [Part Grundkörper](Part_Primitives/de.md), [PartDesign Körper](PartDesign_Body/de.md) und andere [Part Formelement](Part_Feature/de.md). Das \'Std Part\' stellt ein [Ursprungsobjekt](#Ursprung.md) mit lokalen X-, Y- und Z-Achsen und Standardebenen zur Verfügung, die als Bezug für die Positionierung der enthaltenen Objekte dienen können. Zusätzlich können \'Std Parts\' in andere \'Std Parts\' eingebettet werden, um eine Gesamtbaugruppe aus kleineren Unterbaugruppen zu erstellen.

Obwohl es hauptsächlich für Festkörper gedacht ist, kann das \'Std Part\' zur Handhabung aller Objekte verwendet werden, die die Eigenschaft [Placement](Placement/de.md) besitzen. Daher kann es auch [Mesh Formelemente](Mesh_Feature/de.md), [Skizzen](Sketch/de.md) und andere Objekte enthalten, die von der Klasse [App-GeoFeature](App_GeoFeature/de.md) abgeleitet werden.

Die **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Körper](PartDesign_Body/de.md)**-Schaltfläche darf nicht mit der **[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part/de.md)**-Schaltfläche verwechselt werden. Das erste ist ein entsprechendes Objekt aus dem <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md), um ein [einzeln zusammenhängenden Körper](PartDesign_Body/de#Einzeln_zusammenhängender_Körper.md) als [PartDesign Formelemente](PartDesign_Feature/de.md) zu erstellen. Beim anderen wird [Standard Teil](Std_Part/de.md) nicht zur Erstellung von Objekten verwendet, sondern um unterschiedliche Objekte zur Erzeugung von [Baugruppen](assembly/de.md) im Raum zu positionieren.

Das Werkzeug **[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part/de.md)** wird nicht durch einen bestimmten Arbeitsbereich festgelegt, sondern durch das Grundsystem. Daher befindet es sich in der **structure toolbar**, die es in allen [Arbeitsbereichen](Workbenches/de.md) gibt. Mit der Schaltfläche **[<img src=images/Std_Group.svg style="width:16px"> [Std Gruppe](Std_Group/de.md)** können Objekte in der Baumansicht frei gruppiert werden, ohne ihre Position zu berücksichtigen. Dieses Objekt beeinflußt die Positionen seiner Elemente nicht. Es ist im wesentlichen nur ein Ordner mit dem die [Baumansicht](Tree_view/de.md) geordnet werden kann.

![](images/Std_Part-tree.png )![](images/Std_Part_example.png )



*Links: Elemente innerhalb eines 'Std Part's in der [Baumansicht](Tree_view/de.md). Rechts: Objekte im Raum positioniert, bezogen auf den Ursprung von 'Std Part'.*

## Anwendung

1.  Die Schaltfläche **[<img src=images/Std_Part.svg style="width:16px"> [Baugruppe erstellen](Std_Part/de.md)** betätigen.
2.  Ein leeres Teil wird erzeugt und wird automatisch *[aktiv](Std_Part#Active_status.md)*.
3.  In der [Baumansicht](Tree_view/de.md) Objekte wählen und durch Drag & Drop auf dieses Teil ziehen, um sie zum Teil hinzuzufügen.
4.  Um Objekte aus einem Teil zu entfernen, zieht man es per Drag & Drop aus dem Teil auf die Dokumentenbeschriftung oben in der [Baumansicht](Tree_view/de.md).
5.  Objekte können durch Bearbeiten der {{PropertyData/de|Group}} Teileigenschaft auch hinzugefügt oder entfernt werden.

## Hinweise

-   Ein Objekt kann nur zu einer einzigen Baugruppe gehören.
-   3D-Bearbeitungen, wie [Part Boolean](Part_Boolean/de.md) können nicht auf Teile angewendet werden. Beispielsweise können keine zweit Teile markiert und [Part Vereinigung](Part_Fuse/de.md) oder [Part Differenz](Part_Cut/de.md) angewendet werden.

## Eigenschaften

Ein [Std Teil](Std_Part/de.md) wird intern [App Part](App_Part.md)(`App::Part` Klasse) genannt und stammt aus einer [App GeoFeature](App_GeoFeature/de.md) (`App::GeoFeature` Klasse) und erbt alle Eigenschaften. Sie hat weitere, zusätzliche Eigenschaften, vor allem Eigenschaften die ihr helfen Informationen im Zusammenhang einer Baugruppe / eines Zusammenbaus zu verwalten, z.B. die Eigenschaften **Type**, **Id**, **License**, **LicenseURL** und **Group**.

Diese Eigenschaften stehen im [Eigenschaftseditor](property_editor/de.md) zur Verfügung. Versteckte Eigenschaften werden durch den Befehl **Alle anzeigen** im Kontextmenü des [Eigenschaftseditors](property_editor/de.md) angezeigt.

### Daten


{{TitleProperty|Basis}}


<div class="mw-translate-fuzzy">

-    {{PropertyData/de|Typ|Zeichenfolge}}: eine Beschreibung für dieses Objekt. Standardmäßig ist es eine leere Zeichenfolge {{value|""}}.

-    {{PropertyData/de|Id|Zeichenfolge}}: eine Identifikations- oder Teilenummer für dieses Objekt. Standardmäßig handelt es sich um eine leere Zeichenfolge {{value|""}}.

-    {{PropertyData/de|Lizenz|Zeichenfolge}}: ein Feld zur Angabe der Lizenz für dieses Objekt. Standardmäßig ist es eine leere Zeichenfolge {{value|""}}.

-    {{PropertyData/de|LizenzURL|Zeichenfolge}}: ein Feld zur Angabe der Webadresse zur Lizenz oder zum Vertrag für dieses Objekt. Standardmäßig ist es eine leere Zeichenfolge {{value|""}}.

-    **Farbe|Farbe**: ein Tupel von vier Fließkomma RGBA Werten white color angezeigt wird.

-    {{PropertyData/de|Positionierung|Positionierung}}: die Position des Objekts in der [3D Ansicht](3D_view/de.md). Die Platzierung wird durch einen `Base` Punkt (Vektor) und eine `Drehung` (Achse und Winkel) definiert. Siehe [Positionierung](Placement/de.md).

    -   
        {{PropertyData/de|Winkel}}
        
        : den Drehwinkel um die {{PropertyData/de|Achse}}. Standardmäßig lautet er {{value|0°}}. (Null Grad).

    -   
        {{PropertyData/de|Achse}}
        
        : der Einheitsvektor, der die Drehachse für die Positionierung festlegt. Jede Komponente ist ein Fließkommawert zwischen {{value|0}} und {{value|1}}. Wenn irgendein Wert über {{value|1}} liegt, wird der Vektor so normiert, dass die Größenordnung des Vektors {{value|1}} ist. Standardmäßig ist dies die positive Z Achse, {{value|(0, 0, 1)}}.

    -   
        {{PropertyData/de|Position}}
        
        : ein Vektor mit den 3D Koordinaten des Basispunkts. Standardmäßig ist dies der Ursprung {{value|(0, 0, 0)}}.

-    {{PropertyData/de|Kennzeichen|Zeichenfolge}}: der vom Benutzer bearbeitbare Name dieses Objekts, es ist eine beliebige UTF8 Zeichenfolge.

-    {{PropertyData/de|Gruppe|VerknüpfungListe}}: eine Liste der verknüpften Objekte. Standardmäßig ist sie leer {{value|[]}}.


</div>

### Ansicht


{{TitleProperty|Optionen anzeigen (Display Options)}}

-    **Display Mode|Enumeration**: {{value|Group}}.

-    **Show In Tree|Bool**: if it is `True`, the object appears in the [Tree view](Tree_view.md). Otherwise, it is set as invisible.

-    **Visibility|Bool**: if it is `True`, the object appears in the [3D view](3D_view.md); otherwise it is invisible. By default this property can be toggled on and off by pressing the **Space** bar in the keyboard.


{{TitleProperty|Auswahl (Selection)}}

-    **On Top When Selected|Enumeration**: {{value|Disabled}} (default), {{value|Enabled}}, {{value|Object}}, {{value|Element}}.

-    **Selection Style|Enumeration**: {{value|Shape}} (default), {{value|BoundBox}}. If the option is {{value|Shape}}, the entire shape (vertices, edges, and faces) will be highlighted in the [3D view](3D_view.md); if it is {{value|BoundBox}} only the bounding box will be highlighted.

## Detaillierte Beschreibung 

### Aktiver Status 

Ein geöffnetes Dokument kann mehrere Teile enthalten. Aber nur ein Teil kann aktiv sein. Das aktive Teil wird in der [Baumansicht](Tree_view/de.md) mit einer Hintergrundfarbe angezeigt, die mit dem **Aktiver Behälter**-Wert im [Voreinstellungseditor](Preferences_Editor/de#Farben.md) angegeben wird. Der voreingestellte Wert ist hellblau. Es wird auch mit der Schrifteigenschaft \'fett\' angezeigt.

Eine Zusammenstellung aktivieren oder deaktivieren:

-   Doppelklick auf die Zusammenstellung in der [Baumansicht](Tree_view/de.md) oder
-   das Kontextmenü mit einem Rechtsklick öffnen und **Toggle active part** wählen.

![](images/Std_Part_active.png )



*Dokument mit zwei Std Teilen, in der das zweite aktiv ist.*

### Ursprung

Der Ursprung besteht aus den drei Standardachsen (X, Y, Z) und drei Standardebenen (XY, XZ und YZ). An diese können [Skizzen](Sketch/de.md) und andere Ojekte angehängt werden, wenn sie erstellt werden.

![](images/Part_Origin_tree.png ) ![](images/Part_Origin_view.png )



*Links: Teil Ursprung in der [Baumansicht](Tree_view/de.md). Rechts: Ansicht der Ursprungselemente in der [3D-Ansicht](3D_view/de.md).*


**Hinweis:**

der Ursprung ist ein [App-Origin](App_OriginGroupExtension/de.md)-Objekt (`App::OriginGroupExtension` Klasse), während die Achsen und Ebenen Objekte des Typs `App::Line` bzw. `App::Plane` sind. Jedes dieser Elemente kann mit der **Leertaste** individuell versteckt und wieder angezeigt werden. Damit kann sicher die korrekte Referenz gewählt werden, wenn andere Objekte erzeugt werden.


**Hinweis 2:**

alle Elemente innerhalb einer Zusammenstellung beziehen sich auf den Ursprung der Zusammenstellung. Das bedeutet, dass die Zusammenstellung bezogen auf das globale Koordinatensystem verschoben oder gedreht werden kann, ohne Auswirkung auf die Positionierung der Elemente in der Zusammenstellung.

### Anzeigeverwaltung

Die Sichtbarkeit der Zusammenstellung verdrängt die Sichtbarkeit jedes darin enthaltenen Objekts. Wenn die Zusammenstellung ausgeblendet ist, werden auch die darin enthaltenen Objekte ausgeblendet, auch wenn ihre jeweilige Eigenschaft **Sichtbarkeit** auf `True` (wahr) gesetzt ist. Ist die Zusammenstellung sichtbar, entscheidet die Eigenschaft **Sichtbarkeit** jedes Objektes, ob das Objekt angezeigt wird oder nicht.

![](images/Part_Visibility_off.png ) ![](images/Part_Visibility_on.png ) 
*Die Sichtbarkeitseigenschaft von 'Std Part' entscheidet, ob die Objekte, die unter der Zusammenstellung zusammengestellt sind, in der [3D-Ansicht](3D_view/de.md) angezeigt werden oder nicht. Links: die Zusammenstellung ist verborgen und keines der Objekte wird in der [3D-Ansicht](3D_view/de.md) angezeigt. Rechts: die Zusammenstellung ist sichtbar und jedes Objekt kontrolliert seine Sichtbarkeit selbst.*

## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md) und [Skriptgenerierte Objekte](Scripted_objects/de.md).

Zu allgemeinen Informationen zum Hinzufügen von Objekten in das Dokument, siehe [Part Formelement](Part_Feature/de.md).


<div class="mw-translate-fuzzy">

Eine \'Std Part\' ([Anwendung Teil](App_Part/de.md))-Zusammenstellung wird mit der `addObject()`-Methode des Dokumentes erstellt. Sobald eine Zusammenstellung existiert, können andere Objekte mit der `addObject()`- oder der `addObjects()`-Methode der Zusammenstellung hinzugefügt werden.


</div>


```python
import FreeCAD as App

doc = App.newDocument()
part = App.ActiveDocument.addObject("App::Part", "Part")

obj1 = App.ActiveDocument.addObject("PartDesign::Body", "Body")
obj2 = App.ActiveDocument.addObject("Part::Box", "Box")

part.addObjects([obj1, obj2])
App.ActiveDocument.recompute()
```

Ein mit einem Skript erzeugtes `App::Part` kann nicht erstellt werden. Es kann aber ein `App::Part`-Verhalten zu einem mit einem Skript erzeugten `Part::FeaturePython`-Objekt durch folgenden Codes hinzugefügt werden:


```python
class MyGroup(object):
    def __init__(self, obj=None):
        self.Object = obj
        if obj:
            self.attach(obj)

    def __getstate__(self):
        return

    def __setstate__(self, _state):
        return

    def attach(self, obj):
        obj.addExtension("App::OriginGroupExtensionPython")
        obj.Origin = FreeCAD.ActiveDocument.addObject("App::Origin", "Origin")

    def onDocumentRestored(self, obj):
        self.Object = obj

class ViewProviderMyGroup(object):
    def __init__(self, vobj=None):
        if vobj:
            vobj.Proxy = self
            self.attach(vobj)
        else:
            self.ViewObject = None

    def attach(self, vobj):
        vobj.addExtension("Gui::ViewProviderOriginGroupExtensionPython")
        self.ViewObject = vobj

    def __getstate__(self):
        return None

    def __setstate__(self, _state):
        return None

App.ActiveDocument.addObject("Part::FeaturePython",
                             "Group",
                             group.MyGroup(),
                             group.ViewProviderMyGroup(),
                             True)
```





{{Std_Base_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std Part/de
