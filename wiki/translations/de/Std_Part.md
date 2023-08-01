---
- GuiCommand:/de
   Name:Std Part
   Name/de:Std Teil
   MenuLocation:Keine
   Workbenches:Alle
   Version:0.17
   SeeAlso:[Std Gruppe](Std_Group/de.md), [PartDesign Körper](PartDesign_Body/de.md)
---

# Std Part/de



## Beschreibung


**[<img src=images/Std_Part.svg style="width:16px"> [Std Teil](Std_Part/de.md)**

, intern [App-Part](App_Part/de.md) genannt, ist ein Sammelbehälter zur allgemeinen Verwendung, der eine Gruppe von Objekten (Baugruppe) zusammenhält, so dass sie zusammen als Einheit in der [3D-Ansicht](3D_view/de.md) bewegt werden können.

Das \'Std Part\'-Element wurde entwickelt, um als Grundbaustein zur Zusammenstellung von mechanischen [Zusammenbauten](assembly/de.md) (Baugruppen) zu dienen. Es dient zum Anordnen von Objekten, die eine [Part TopoForm](Part_TopoShape/de.md) haben, wie [Part Grundkörper](Part_Primitives/de.md), [PartDesign Körper](PartDesign_Body/de.md) und andere [Part Formelement](Part_Feature/de.md). Das \'Std Part\' stellt ein [Ursprungsobjekt](#Ursprung.md) mit lokalen X-, Y- und Z-Achsen und Standardebenen zur Verfügung, die als Bezug für die Positionierung der enthaltenen Objekte dienen können. Zusätzlich können \'Std Parts\' in andere \'Std Parts\' eingebettet werden, um eine Gesamtbaugruppe aus kleineren Unterbaugruppen zu erstellen.

Obwohl es hauptsächlich für Festkörper gedacht ist, kann das \'Std Part\' zur Handhabung aller Objekte verwendet werden, die die Eigenschaft [Placement](Placement/de.md) besitzen. Daher kann es auch [Mesh Formelemente](Mesh_Feature/de.md), [Skizzen](Sketch/de.md) und andere Objekte enthalten, die von der Klasse [App-GeoFeature](App_GeoFeature/de.md) abgeleitet werden.

Ein **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Körper](PartDesign_Body/de.md)** darf nicht mit einem **[<img src=images/Std_Part.svg style="width:16px"> [Std Teil](Std_Part/de.md)** verwechselt werden. Das erste ist ein entsprechendes Objekt aus dem Arbeitsbereich <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/de.md), zum Erstellen [einteiliger, zusammenhängender Festkörper](PartDesign_Body/de#Einzeln_zusammenhängender_Körper.md) aus [PartDesign Formelementen](PartDesign_Feature/de.md). Das [Std Teil](Std_Part/de.md) wird im Gegensatz dazu nicht zur Erstellung von Objekten verwendet, sondern um unterschiedliche Objekte im Raum anzuordnen, mit der Absicht [Baugruppen](assembly/de.md) zu erstellen.

Das Werkzeug **[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part/de.md)** wird nicht durch einen bestimmten Arbeitsbereich festgelegt, sondern durch das Grundsystem. Daher befindet es sich in der **structure toolbar**, die es in allen [Arbeitsbereichen](Workbenches/de.md) gibt. Mit der Schaltfläche **[<img src=images/Std_Group.svg style="width:16px"> [Std Gruppe](Std_Group/de.md)** können Objekte in der Baumansicht frei gruppiert werden, ohne ihre Position zu berücksichtigen. Dieses Objekt beeinflußt die Positionen seiner Elemente nicht. Es ist im wesentlichen nur ein Ordner mit dem die [Baumansicht](Tree_view/de.md) geordnet werden kann.

![](images/Std_Part-tree.png )![](images/Std_Part_example.png )



*Links: Elemente innerhalb eines Std Teils (Part-Objekt) in der [Baumansicht](Tree_view/de.md). Rechts: Objekte im Raum positioniert, bezogen auf den Ursprung des Std Teils.*



## Anwendung

1.  Die Schaltfläche **[<img src=images/Std_Part.svg style="width:16px"> [Baugruppe erstellen](Std_Part/de.md)** betätigen.
2.  Ein leeres Teil wird erzeugt und wird automatisch *[aktiv](Std_Part#Active_status.md)*.
3.  In der [Baumansicht](Tree_view/de.md) Objekte wählen und durch Drag & Drop auf dieses Teil ziehen, um sie zum Teil hinzuzufügen.
4.  Um Objekte aus einem Teil zu entfernen, zieht man es per Drag & Drop aus dem Teil auf die Dokumentenbeschriftung oben in der [Baumansicht](Tree_view/de.md).
5.  Objekte können durch Bearbeiten der {{PropertyData/de|Group}} Teileigenschaft auch hinzugefügt oder entfernt werden.



## Hinweise

-   Ein Objekt kann nur zu einem einzigen Std Teil (Baugruppe) gehören.
-   3D-Bearbeitungen, wie [Part Boolean](Part_Boolean/de.md) können nicht auf Std Teile angewendet werden. Beispielsweise können keine zweit Std Teile markiert und [Part Vereinigung](Part_Fuse/de.md) oder [Part Differenz](Part_Cut/de.md) angewendet werden.



## Eigenschaften

Ein [Std Teil](Std_Part/de.md) wird intern [App Part](App_Part/de.md)(Klasse `App::Part`) genannt und ist von einem [App GeoFeature](App_GeoFeature/de.md) (Klasse `App::GeoFeature`) abgeleitet und erbt alle seiner Eigenschaften. Es hat weitere zusätzliche Eigenschaften, vor allem Eigenschaften die ihm helfen, Informationen im Zusammenhang mit Baugruppen/Zusammenbauten zu verwalten, z.B. die {{PropertyData/de|Type}}, {{PropertyData/de|Id}}, {{PropertyData/de|License}}, {{PropertyData/de|LicenseURL}} und {{PropertyData/de|Group}}.

Diese Eigenschaften stehen im [Eigenschafteneditor](property_editor/de.md) zur Verfügung. Versteckte Eigenschaften werden durch den Befehl **Alle anzeigen** im Kontextmenü des [Eigenschafteneditors](property_editor/de.md) angezeigt.



### Daten


{{TitleProperty|Basis}}

-    {{PropertyData/de|Type|String}}: eine Beschreibung für dieses Objekt. Standardmäßig ist es eine leere Zeichenfolge {{value|""}}.

-    {{PropertyData/de|Material|Link}}: das Material für dieses Objekt.

-    {{PropertyData/de|Meta|Map|Hidden}}: Zuordnung zusätzlicher Meta-Informationen. Standardmäßig ist sie leer {}.

-    {{PropertyData/de|Id|String}}: eine Identifikations- oder Teilenummer für dieses Objekt. Standardmäßig ist es eine leere Zeichenfolge {{value|""}}.

-    **Uid|UUID|Hidden**: Die eindeutige Kennung ([universally unique identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier), kurz UUID) (128-bit-Zahl) des Objekts. Diese wird zur Erstellungszeit vergeben.

-    {{PropertyData/de|License|String}}: ein Feld zur Angabe der Lizenz für dieses Objekt. Standardmäßig ist es eine leere Zeichenfolge {{value|""}}.

-    {{PropertyData/de|LicenseURL|String}}: ein Feld zur Angabe einer Webadresse zur Lizenz oder zum Vertrag für dieses Objekt. Standardmäßig ist es eine leere Zeichenfolge {{value|""}}.

-    {{PropertyData/de|Color|Color}}: ein Tupel von vier RGBA-Fließkommawerten white color angezeigt wird.

-    {{PropertyData/de|Placement|Placement}}: die Position des Objekts in der [3D-Ansicht](3D_view/de.md). Die Positionierung wird durch einen Punkt (Ortsvektor)`Base` und eine Drehung `Rotation`, bestehend aus Richtungsvektor (Axis) und Winkel (Angle), festgelegt. Siehe [Positionierung](Placement/de.md).

    -   
        {{PropertyData/de|Angle}}
        
        : der Drehwinkel um die {{PropertyData/de|Axis}}. Standardmäßig ist er {{value|0°}} (Null Grad).

    -   
        {{PropertyData/de|Axis}}
        
        : der Einheitsvektor, der die Drehachse für die Positionierung festlegt. Jede Komponente ist eine Fließkommazahl zwischen {{value|0}} und {{value|1}}. Wenn irgendein Wert über {{value|1}} liegt, wird der Vektor so normiert, dass der Betrag des Vektors {{value|1}} ist. Standardmäßig ist dies die positive Z Achse, {{value|(0, 0, 1)}}.

    -   
        {{PropertyData/de|Position}}
        
        : ein Vektor mit den 3D-Koordinaten des Basispunkts (Ortsvektor). Standardmäßig ist dies der Ursprung {{value|(0, 0, 0)}}.

-    **Label|String**: die vom Benutzer editierbare Bezeichnung dieses Objekts, sie ist eine beliebige UTF8-Zeichenfolge.

-    {{PropertyData/de|Label2|String|Hidden}}: eine längere vom Benutzer editierbare Bezeichnung dieses Objekts, sie ist eine beliebige UTF8-Zeichenfolge, die Zeilenumbrüche enthalten kann. Standardmäßig ist sie eine leere Zeichenfolge {{value|""}}.

-    {{PropertyData/de|Expression Engine|ExpressionEngine|Hidden}}: eine Liste von Ausdrücken. Standardmäßig ist sie leer {{value|[]}}.

-    {{PropertyData/de|Visibility|Bool|Hidden}}: legt fest, ob das Objekt angezeigt wird oder nicht.

-    {{PropertyData/de|Origin|Link|Hidden}}: das [App Origin](App_OriginGroupExtension/de.md)-Objekt, das als Positionierungsreferenz aller in der {{PropertyData/de|Group}} enthaltenen Elemente dient.

-    {{PropertyData/de|Group|LinkList}}: eine Liste der verknüpften Objekte. Standardmäßig ist sie leer {{value|[]}}.

-    {{PropertyData/de|_ Group Touched|Bool|Hidden}}: legt fest, ob die Gruppe berührt(?) ist/wird oder nicht.



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

Der Ursprung besteht aus den drei Standardachsen (X, Y, Z) und drei Standardebenen (XY, XZ und YZ). An diese können [Skizzen](Sketch/de.md) und andere Objekte angehängt werden, wenn sie erstellt werden.

![](images/Part_Origin_tree.png ) ![](images/Part_Origin_view.png )



*Links: Teil Ursprung in der [Baumansicht](Tree_view/de.md). Rechts: Ansicht der Ursprungselemente in der [3D-Ansicht](3D_view/de.md).*


**Hinweis:**

der Ursprung ist ein [App-Origin](App_OriginGroupExtension/de.md)-Objekt (Klasse `App::OriginGroupExtension`), während die Achsen und Ebenen Objekte des Typs `App::Line` bzw. `App::Plane` sind. Jedes dieser Elemente kann mit der **Leertaste** individuell ausgeblendet und wieder angezeigt werden. Damit kann sicher die korrekte Referenz gewählt werden, wenn andere Objekte erzeugt werden.


**Hinweis 2:**

alle Elemente innerhalb einer Baugruppe beziehen sich auf den Ursprung der Baugruppe. Das bedeutet, dass die Baugruppe bezogen auf das globale Koordinatensystem verschoben oder gedreht werden kann, ohne die Positionierung der Elemente innerhalb der Baugruppe zu beeinflussen.



### Anzeigeverwaltung

Die Sichtbarkeit der Baugruppe überlagert die Sichtbarkeit jedes darin enthaltenen Objekts. Wenn die Baugruppe ausgeblendet ist, werden auch die darin enthaltenen Objekte ausgeblendet, auch wenn ihre jeweilige {{PropertyView/de|Sichtbarkeit}} auf `True` (wahr) gesetzt ist. Ist die Baugruppe sichtbar, entscheidet die {{PropertyView/de|Sichtbarkeit}} des jeweiligen Objekts, ob das Objekt angezeigt wird oder nicht.

![](images/Part_Visibility_off.png ) ![](images/Part_Visibility_on.png ) 
*Die Sichtbarkeit des Std Teils (Part-Objekt) bestimmt, ob die Objekte, die in der Baugruppe zusammengestellt sind, in der [3D-Ansicht](3D_view/de.md) angezeigt werden oder nicht. Links: die Baugruppe ist ausgeblendet und keines der Objekte wird in der [3D-Ansicht](3D_view/de.md) angezeigt. Rechts: die Baugruppe ist sichtbar und jedes Objekt bestimmt seine Sichtbarkeit selbst.*



## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md) und [Skriptgenerierte Objekte](Scripted_objects/de.md).

Siehe [Part Formelement](Part_Feature/de.md) für allgemeine Informationen zum Hinzufügen von Objekten zu einem Dokument.

Ein Std Teil ([App Part](App_Part/de.md)) wird mit der Methode `addObject()` des Dokuments erstellt. Sobald eine Baugruppe (Part-Objekt) existiert, können andere Objekte mit den Methoden `addObject()` oder `addObjects()` zur Baugruppe hinzugefügt werden.


```python
import FreeCAD as App

doc = App.newDocument()
part = App.ActiveDocument.addObject("App::Part", "Part")

obj1 = App.ActiveDocument.addObject("PartDesign::Body", "Body")
obj2 = App.ActiveDocument.addObject("Part::Box", "Box")

part.addObjects([obj1, obj2])
App.ActiveDocument.recompute()
```

Es kann kein skriptgeneriertes `App::Part` erstellt werden. Es kann aber das Verhalten eines `App::Parts` zu einem skriptgenerierten `Part::FeaturePython`-Objekt durch folgende Codes hinzugefügt werden:


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
![](images/Button_right.svg) [documentation index](../README.md) > Std Part/de
