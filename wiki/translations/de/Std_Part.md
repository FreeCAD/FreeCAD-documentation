---
- GuiCommand:/de
   Name:Std Part
   Name/de:Std Baugruppe
   MenuLocation:None
   Workbenches:All
   Version:0.17
   SeeAlso:[Std Group](Std_Group/de.md), [PartDesign Body](PartDesign_Body/de.md)
---

# Std Part/de

## Beschreibung


**[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part/de.md)**

, intern [Anwendung Teil](App_Part/de.md) genannt, ist ein Sammelbehälter zur allgemeinen Verwendung, der eine Gruppe von Objekten zusammenhält, so dass sie zusammen als Einheit in der [3D Ansicht](3D_view/de.md) bewegt werden können.

Das \'Std Part\'-Element wurde entwickelt, um als Fundament zur Zusammenstellung von mechanischen [Baugruppen](assembly/de.md) zu dienen. Es dient zum Anordnen von Objekten, die eine [Part Topo-Form](Part_TopoShape/de.md) haben, wie [Part Grundkörper](Part_Primitives/de.md), [PartDesign Körper](PartDesign_Body/de.md) und andere [Part Formelement](Part_Feature/de.md). Das \'Std Part\' stellt ein [Bezugsobjekt](#Origin.md) mit lokalen x-, y- und z-Achsen und Standardebenen zur Verfügung. Sie dienen als Bezug und zur Positionierung der enthaltenen Objekte. Zusätzlich können \'Std Parts\' in andere \'Std Part\'s eingebettet werden, um eine Gesamtbaugruppe aus kleineren Unterbaugruppen zu erstellen.

Obwohl es vorläufig für Festkörper gedacht ist, kann \'Std Part\' zur Handhabung jedes Objektes verwendet werden, das eine [Positionierungseigenschaft](Placement/de.md) hat. Deshalb kann es auch [Polygonnetz Formelement](Mesh_Feature/de.md), [Skizzen](Sketch/de.md) und andere Objekte enthalten, die aus [App GeoFeature](App_GeoFeature.md) kommen.

Die **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Körper](PartDesign_Body/de.md)**-Schaltfläche darf nicht mit der **[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part/de.md)**-Schaltfläche verwechselt werden. Das erste ist ein entsprechendes Objekt aus dem <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md), um ein [einzeln zusammenhängenden Körper](PartDesign_Body/de#Einzeln_zusammenhängender_Körper.md) als [PartDesign Formelemente](PartDesign_Feature/de.md) zu erstellen. Beim anderen wird [Standard Teil](Std_Part/de.md) nicht zur Erstellung von Objekten verwendet, sondern um unterschiedliche Objekte zur Erzeugung von [Baugruppen](assembly/de.md) im Raum zu positionieren.

Das Werkzeug **[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part/de.md)** wird nicht durch einen bestimmten Arbeitsbereich festgelegt, sondern durch das Grundsystem. Daher befindet es sich in der **structure toolbar**, die es in allen [Arbeitsbereichen](Workbenches/de.md) gibt. Mit der Schaltfläche **[<img src=images/Std_Group.svg style="width:16px"> [Std Gruppe](Std_Group/de.md)** können Objekte in der Baumansicht frei gruppiert werden, ohne ihre Position zu berücksichtigen. Dieses Objekt beeinflußt die Positionen seiner Elemente nicht. Es ist im wesentlichen nur ein Ordner mit dem die [Baumansicht](tree_view/de.md) geordnet werden kann.

![](images/Std_Part-tree.png )![](images/Std_Part_example.png )



*Links: Elemente innerhalt eines 'Std Part's in der [Baumansicht](tree_view/de.md). Rechts: Objekte im Raum, positioniert bezogen auf den Ursprung von 'Std Part'.*

## Anwendung

1.  Die Schaltfläche **[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part/de.md)** betätigen. Ein leeres Teil wird erzeugt und ist automatisch *[aktiv](Std_Part#Active_status.md)*.
2.  In der [Baumansicht](tree_view/de.md) ein Objekt wählen und durch Drag & Drop auf dieses Teil ziehen, um es zum Teil hinzuzufügen.
3.  Um Objekte aus einem Teil zu entfernen, zieht man es per Drag & Drop aus dem Teil auf die Dokumentenbeschriftung oben in der [Baumansicht](tree_view/de.md).

### Hinweise

-   Ab Version v0.19 kann ein bestimmtes Objekt nur zu einer einzigen Baugruppe gehören.
-   Durch einen Doppelklick auf die Baugruppe in der [Baumansicht](tree_view/de.md) oder über das Kontextmenü mit einem Rechtsklick und der Wahl von **Toggle active part** kann eine Baugruppe aktiviert oder deaktiviert werden. Ist eine andere Baugruppe aktiv, wird sie deaktiviert, siehe auch [Aktiver Status](Std_Part/de#Active_status.md)

### Grenzen

-   Zu diesem Zeitpunkt können [Entwurf Fang](Draft_Snap/de.md) Methoden nicht auf ausgewählte Teilebehälter oder auf Objekte innerhalb derer angewandt werden.
-   Ein Teil hat keine [topologische Form](Part_TopoShape/de.md). Es ist daher nicht möglich, 3D Operationen, wie [Part Boolean](Part_Boolean/de.md) auf ein Teil selbst anzuwenden. Zum Beispiel können nicht zwei Teile ausgewählt und mit ihnen einen [Teilverbund](Part_Fuse/de.md) oder [Teilschnitt](Part_Cut/de.md) durchgeführt werden.
    -   Diese booleschen Anwendungen können nur auf die enthaltenen Objekte angewendet werden, solange diese aus [Part Formelement](Part_Feature/de.md) abgeleitet und eine [topologische Form](Part_TopoShape/de.md) haben.

## Eigenschaften

Ein [Std Teil](Std_Part/de.md) wird intern [App Part](App_Part.md)(`App::Part` Klasse) genannt und stammt aus einer [App GeoFeature](App_GeoFeature.md) (`App::GeoFeature` Klasse). Deshalb hat es die meisten Eigenschaften mit letzterem gemein.

Zusätzlich zu den Eigenschaften, die in [App GeoFeature](App_GeoFeature.md) beschrieben sind, hat die \'App Part Klasse\' einige Eigenschaften, die helfen, Informationen im Zusammenhang mit dem Zusammenbau zu verwalten, z.B. **Type**, **Id**, **License**, **LicenseURL**, **Color** und **Group**.

Diese Eigenschaften stehen im [Eigenschaftseditor](property_editor/de.md) zur Verfügung. Versteckte Eigenschaften werden durch den Befehl **Alle anzeigen** im Kontextmenü des [Eigenschaftseditors](property_editor/de.md) angezeigt.

### Daten


{{TitleProperty|Basis}}

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

#### Ausgeblendete Dateneigenschaften 

-    **Material|Map**: Karte mit Materialeigenschaften. Ein leerer Code {} ist vorgegeben.

-    **Meta|Map**: Karte mit zusaätzlichen Metadaten. Ein leerer Code {} ist vorgegeben.

-    **Uid|UUID**: die [1](https://de.wikipedia.org/wiki/Universally_Unique_Identifier) (UUID) (128-bit Zahl) des Objektes. Diese wird zur Erstellungszeit zugewiesen.

-    **Beschriftung2|String**: eine lange Beschreibung des Objektes, die der Benutzer bearbeiten kann. Es ist eine beliebige UTF8-Zeichenkette, die Zeilenumbrüche enthalten kann. Ein leerer String (Text) {{value|""}} ist vorgegeben.

-    **Ausdrucksverarbeitung|ExpressionEngine**: eine Liste von Ausdrücken. Ein leerer Wert {{value|[]}} ist vorgegeben.

-    **Sichtbarkeit|Bool**: Objekt zeigen oder nicht.

-    **Ursprung|Link**: das [App Ursprungsobjekt](App_Origin.md) ist die Positionierungsreferenz für alle Elemente, in der **Group**.

-    **_ Group Touched|Bool**: wird die Gruppe berührt oder nicht.

### Ansicht

Die Anwendung Teil hat nur die fünf Eigenschaften der grundlegenden Anwendung [FormelementPython](App_FeaturePython.md) und sie hat keine ausgeblendeten Eigenschaften.


{{TitleProperty|Basis}}

-    **Anzeigemodus|Enumeration**: {{value|Group}}.

-    **oben, wenn ausgewählt|Enumeration**: {{value|Disabled}} (Standard), {{value|Enabled}}, {{value|Object}}, {{value|Element}}.

-    **Auswahlstil|Enumeration**: {{value|Form}} (default), {{value|BoundBox}}. Wenn die Wahl {{value|Form}} ist, wird die ganze Form (Punkte, Kanten und Oberflächen) in der [3D-Ansicht](3D_view.md) hervorgehoben. Ist der Wert {{value|BoundBox}}, wird nur die gebundene Box hervorgehoben.

-    **Im Baum anzeigen|Bool**: ist dies `True`, erscheint das Objekt in der [Baumansicht](Tree_view.md). Sonst ist die Wahl \'unsichtbar\'.

-    **Sichtbarkeit|Bool**: ist es `True`, erscheint das Objekt in der [3D-Ansicht](3D_view.md). Sonst ist die Wahl \'unsichtbar\'. Diese Eigenschaft kann mit der **Leertaste** ein- und ausgeschaltet werden.

## Konzept einer Zusammenstellung 

\'Std Part\' stellt das grundlegende Fundament für eine Zusammenstellung dar. Anders als [PartDesign Körper](PartDesign_Body/de.md) soll eine Zusammenstellung eine Ansammlung von einzelnen, unterscheidbaren Elementen darstellen, die auf irgendeine Weise in der physischen Welt miteinander verbunden sind, z.B. durch Druck, Schrauben oder Klebstoff.

Beispiele, die eine Zusammenstellung sein können:

-   Ein Holztisch, der aus verschiedenen Holzteilen, wie Beine oder Tischplatte besteht und die mit Leim oder Metallschrauben zusammengebaut sind.
-   Ein Kugellager, das aus mehreren Stahlkugeln, einem inneren Ring, einem Käfig, einer Dichtung und einem äußerem Ring besteht.
-   Einer Zusammenstellung aus einer Schraube mit einer Beilagscheibe und einer passenden Mutter besteht.

<img alt="" src=images/PartDesign_Body_contiguous_separate.png  style="width:" height="200px;"> <img alt="" src=images/PartDesign_Body_contiguous_assembly.png  style="width:" height="200px;"> 
*Links: drei einzelne, aneinandergrenzende Körper, jeder von ihnen durch [PartDesign Körper](PartDesign_Body/de.md) erstellt. Rechts: die einzelnen Körper innerhalb von 'Std Part' zu einer Zusammenstellung zusammengestellt.*

Im Allgemeinen werden beim Importieren einer STEP-Datei in das Programm die Hauptbaugruppe und ihre Unterbaugruppen als Zusammenstellungsbehälter importiert, wobei jede von ihnen ein einfaches [Part Formelement](Part_Feature/de.md) enthält.

## Detaillierte Beschreibung 

### Aktiver Status 

Ein geöffnetes Dokument kann mehrere Zusammenstellungen enthalten. Eine aktive Zusammenstellung wird in der [Baumansicht](Tree_view/de.md) mit einem im Menü **Aktiver Behälter** angegebenen Wert zur Hintergrundfarbe angezeigt. Der Wert kann im [Voreinstellungseditor](Preferences_Editor/de#Farben.md) geändert werden. Der voreingestellte Wert ist hellblau. Eine aktive Zusammenstellung wird auch mit der Schrifteigenschaft \'fett\' angezeigt.

Eine Zusammenstellung aktivieren oder deaktivieren:

-   Doppelklick auf die Zusammenstellung in der [Baumansicht](Tree_view/de.md) oder
-   das Kontextmenü mit einem Rechtsklick öffnen und **Toggle active part** wählen.


**Hinweise:**

-   Der {{emphasis|Aktivstatus}} für Zusammenstellungen wurde zur Version v0.17 parallel mit de {{emphasis|Aktivstatus}} der [PartDesign Körper](PartDesign_Body/de.md) entwickelt; allerdings ab Version v0.19 erfüllt dieser Status keinen wirklichen Zweck für Zusammenstellungen.
-   Selbst wenn eine Zusammenstellung aktiv ist, werden neu erstellte Objekte nicht automatisch in diese Zusammenstellung eingefügt. In diesem Fall zieht man diese neuen Objekte einfach per Drag & Drop auf die gewünschte Zusammenstellung.
-   Es kann nur eine Zusammenstellung aktiv sein.

![](images/Std_Part_active.png )



*Dokument mit zwei Std Teilen, in der das zweite aktiv ist.*

### Ursprung

Der Ursprung besteht aus den drei Standardachsen (X, Y, Z) und drei Standardebenen (XY, XZ und YZ). An diese können [Skizzen](Sketch/de.md) und andere Ojekte angehängt werden, wenn sie erstellt werden.

![](images/Part_Origin_tree.png ) ![](images/Part_Origin_view.png )



*Links: Teil Ursprung in der [Baumansicht](tree_view/de.md). Rechts: Ansicht der Ursprungselemente in der [3D-Ansicht](3D_view/de.md).*


**Hinweis:**

der Ursprung ist ein [App Origin](App_Origin.md) Objekt (`App::Origin` Klasse), während die Achsen und Ebenen Objekte des Typs `App::Line` bzw. `App::Plane` sind. Jedes dieser Elemente kann mit der **Leertaste** individuell versteckt und wieder angezeigt werden. Damit kann sicher die korrekte Referenz gewählt werden, wenn andere Objekte erzeugt werden.


**Hinweis 2:**

alle Elemente innerhalb einer Zusammenstellung beziehen sich auf den Ursprung der Zusammenstellung. Das bedeutet, dass die Zusammenstellung bezogen auf das globale Koordinatensystem verschoben oder gedreht werden kann, ohne Auswirkung auf die Positionierung der Elemente in der Zusammenstellung.

### Anzeigeverwaltung

Die Sichtbarkeit der Zusammenstellung verdrängt die Sichtbarkeit jedes darin enthaltenen Objekts. Wenn die Zusammenstellung ausgeblendet ist, werden auch die darin enthaltenen Objekte ausgeblendet, auch wenn ihre jeweilige Eigenschaft **Sichtbarkeit** auf `True` (wahr) gesetzt ist. Ist die Zusammenstellung sichtbar, entscheidet die Eigenschaft **Sichtbarkeit** jedes Objektes, ob das Objekt angezeigt wird oder nicht.

![](images/Part_Visibility_off.png ) ![](images/Part_Visibility_on.png ) 
*Die Sichtbarkeitseigenschaft von 'Std Part' entscheidet, ob die Objekte, die unter der Zusammenstellung zusammengestellt sind, in der [3D-Ansicht](3D_view/de.md) angezeigt werden oder nicht. Links: die Zusammenstellung ist verborgen und keines der Objekte wird in der [3D-Ansicht](3D_view/de.md) angezeigt. Rechts: die Zusammenstellung ist sichtbar und jedes Objekt kontrolliert seine Sichtbarkeit selbst.*

### Vererbung

[Std Part](Std_Part.md) ist formell eine Instanz der Klasse `App::Part`, deren Elternteil die Basisklasse [App GeoFeature](App_GeoFeature.md)(`App::GeoFeature`) ist und um eine Origin-Erweiterung erweitert wird.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Vereinfachtes Diagramm der Beziehungen zwischen den Kernobjekten im Programm. Die`App::Part* Klasse ist ein einfacher Behälter der im 3D-Raum positioniert ist und der einen Ursprung zur Steuerung der Positionierung der Objekte hat, die in ihm gruppiert sind.`

## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md) und [Skriptgenerierte Objekte](scripted_objects/de.md).

Zu allgemeinen Informationen zum Hinzufügen von Objekten in das Dokument, siehe [Part Formelement](Part_Feature/de.md).

Eine \'Std Part\' ([Anwendung Teil](App_Part/de.md))-Zusammenstellung wird mit der `addObject()`-Methode des Dokumentes erstellt. Sobald eine Zusammenstellung existiert, können andere Objekte mit der `addObject()`- oder der `addObjects()`-Methode der Zusammenstellung hinzugefügt werden.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::Part", "Part")

bod1 = App.ActiveDocument.addObject("PartDesign::Body", "Body")
bod2 = App.ActiveDocument.addObject("Part::Box", "Box")

obj.addObjects([bod1, bod2])
App.ActiveDocument.recompute()
```

Du kannst kein geskriptetes {{Incode|App::Part}} erstellen. Du kannst aber {{Incode|App::Part}}-Verhalten zu einem geskripteten {{Incode|Part::FeaturePython}}-Objekt durch Verwenden des folgenden Codes hinzufügen:


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
        obj.addExtension('App::OriginGroupExtensionPython')
        obj.Origin = FreeCAD.ActiveDocument.addObject('App::Origin', 'Origin')

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
        vobj.addExtension('Gui::ViewProviderOriginGroupExtensionPython')
        self.ViewObject = vobj

    def __getstate__(self):
        return None

    def __setstate__(self, _state):
        return None

App.ActiveDocument.addObject('Part::FeaturePython', 'Group', group.MyGroup(), group.ViewProviderMyGroup(), True)
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std Part/de
