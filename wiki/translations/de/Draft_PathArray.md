---
 GuiCommand:
   Name: Draft PathArray
   Name/de: Draft PfadAnordnung
   MenuLocation: Änderung , Anordnungswerkzeuge , Pfad-Anordnung<br>Bearbeiten , Pfad-Anordnung
   Workbenches: Draft_Workbench/de, BIM_Workbench/de
   Version: 0.14
   SeeAlso: Draft_OrthoArray/de, Draft_PolarArray/de, Draft_CircularArray/de, Draft_PathLinkArray/de, Draft_PointArray/de, Draft_PointLinkArray/de
---

# Draft PathArray/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_PathArray.svg  style="width:24px;"> **Draft PfadAnordnung** erstellt eine regelmäßige Anordnung aus einem ausgewählten Objekt, indem er Kopien entlang eines Pfades positioniert. Der Befehl [Draft PfadVerknüpfungsanordnung](Draft_PathLinkArray/de.md) erstellt alternativ eine effizientere Verknüpfungsanordnung ([Link](App_Link.md)-Array). Außer der Art der Anordnung die erstellt wird, normale Anordnung oder Verknüpfungsanordnung, ist der Befehl [Draft PfadVerknüpfungsanordnung](Draft_PathLinkArray/de.md) identisch mit diesem Befehl.

Beide Befehle können für 2D-Objekte verwendet werden, die mit den Arbeitsbereichen [Draft](Draft_Workbench/de.md) oder [Sketcher](Sketcher_Workbench/de.md) erstellt wurden, aber auch für viele 3D-Objekte, die mit anderen Arbeitsbereichen wie [Part](Part_Workbench/de.md), [PartDesign](PartDesign_Workbench/de.md) oder [BIM](BIM_Workbench/de.md) erstellt wurden.

<img alt="" src=images/Draft_PathArray_Example.png  style="width:400px;"> 
*Draft PfadAnordnung*



## Anwendung

1.  Ein Objekt auswählen, das angeordnet werden soll.
2.  Ein Pfadobjekt zur Auswahl hinzufügen. Es ist auch möglich stattdessen Kanten auszuwählen. Die Kanten müssen zu demselben Objekt gehören und miteinander verbunden sein.
3.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_PathArray.svg" width=16px> [Pfad-Anordnung](Draft_PathArray.md)** drücken.
    -   [Draft](Draft_Workbench/de.md): Den Menüeintrag **Änderung → Anordnungswerkzeuge → <img src="images/Draft_PathArray.svg" width=16px> Pfad-Anordnung** auswählen.
    -   [BIM](BIM_Workbench/de.md): Den Menüeintrag **Bearbeiten → <img src="images/Draft_PathArray.svg" width=16px> Pfad-Anordnung** auswählen.
4.  Die Anordnung wird erstellt.
5.  Wahlweise die [Eigenschaften](#Eigenschaften.md) der Anordnung im [Eigenschafteneditor](property_editor/de.md) ändern.



## Ausrichtung

Die Anordnung der Elemente in einer Draft PfadAnordnung ist von den Eigenschaften des Array und der Orientierung des Quellobjektes abhängig. Die Position des Quellobjektes wird ignoriert: für den Zweck des Array werden {{Value|x}}, {{Value|y}} und {{Value|z}} auf {{Value|0}} gesetzt. Wenn die Eigenschaft **Align** des Array auf false gesetzt ist, dann ist die Orientierung der Array Elemente gleich wie beim Quellelement. Wenn sie auf `True` gesetzt ist, dann wird die X Achse des lokalen Koordinatensystems jedes Element Placements die Tangente an den Pfad. Die Y und Z Achsen des lokalen Koordinatensystems hängen von der **Align Mode** Eigenschaft des Array ab. Andere Eigenschaften die an der Anordnung des **Tangent Vector** beteiligt sind, sind **Force Vertical** und **Vertical Vector**.

<img alt="" src=images/Draft_PathArray_example2.png  style="width:600px;"> 
*3 Anordnungen die auf demselben nicht ebenen Pfad basieren. Von links nach rechts:  '''Align''' ist ''false'', '''Align''' ist ''true'' mit '''Align Mode''' ''Original'' und '''Align''' ist ''true'' mit '''Align Mode''' ''Frenet''*.



### Ausrichtungsmodus

Es gibt drei Ausrichtungsmodi

#### Original

Dieser Modus kommt dem einfachen **Ausrichtungsmodus** der in Version 0.18 verfügbar ist am Nächsten. Er basiert auf einem festen Normalvektor. Wenn der Pfad eben ist, dann ist dieser Vektor im rechten Winkel zur Ebene des Pfades, sonst wird ein Standard Vektor, die positive Z Achse, verwendet. Aus diesem Normalvektor und dem lokalen Tangentenvektor (der lokalen X Achse) wird das [Kreuzprodukt](https://en.wikipedia.org/wiki/Cross_product) gebildet. Dieser neue Vektor wird als lokale Z Achse verwendet. Die Orientierung der lokalen Y Achse wird von der lokalen X und Z Achse festgelegt.

#### Frenet

Dieser Modus verwendet den lokalen Normalvektor der aus dem Pfad an jeder Element Plazierung abgeleitet wird. Wenn dieser Vektor nicht festgelegt werden kann (zum Beispiel bei einem geraden Segment) dann wird stattdessen an ein Standard Vektor, wieder die Positive Z Achse verwendet. Mit diesem Vektor und dem lokalen Tangentenvektor wird das Koordinatensystem nach dem gleichen Verfahren wie im vorigen Abschnitt festgelegt.



#### Tangente

Dieser Modus ist ähnlich dem **Ausrichtungsmodus** {{Value|Original}} , bietet aber die Möglichkeit das Quellobjekt durch Festlegen eines **Tangenvektors** vorab zu drehen.



### Erzwingen der Vertikalen und des vertikalen Vektors 

Diese Eigenschaften sind nur verfügbar wenn der **Align Mode** {{Value|Original}} oder {{Value|Tangent}} ist. Wenn **Force Vertical** auf `True` gesetzt ist, dann wird das Koordinatensystem auf eine andere Art berechnet. Der **Vertical Vector** wird wie ein fester Normalvektor verwendet. Aus diesem Normalvektor und dem lokalen Tangentenvektor (die lokale X Achse) wird wieder das Kreuzprodukt gebildet. Aber dieser Vektor wird als lokale Y Achse verwendet. Die Orientierung der lokalen Z Achse wird von den Lokalen X und Y Achsen festgelegt.

Die Verwendung dieser Eigenschaften kann notwendig werden, wenn eine Kante des Pfades (fast) parallel zur Standard Normalen des Pfades wird.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](property_editor/de.md).

Eine [Pfad-Anordnung](Draft_PathArray/de.md) (Path-Array-Objekt) ist von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften (mit Ausnahme einiger Ansicht-Eigenschaften, die nicht an die Verknüpfungsanordnungen vererbt werden). Außerdem sind, wenn nicht anders angegeben, die folgenden zusätzlichen Eigenschaften vorhanden:



### Daten


{{TitleProperty|Link}}

Die Eigenschaften dieser Gruppe stehen nur für Verknüpfungsanordnungen zur Verfügung. Siehe [Std VerknüpfungErstellen](Std_LinkMake/de#Eigenschaften.md) für weitere Informationen.

-    {{PropertyData/de|Scale|Float}}
    

-    {{PropertyData/de|Scale Vector|Vector|Hidden}}
    

-    {{PropertyData/de|Scale List|VectorList}}
    

-    {{PropertyData/de|Visibility List|BoolList|Hidden}}
    

-    {{PropertyData/de|Placement List|PlacementList|Hidden}}
    

-    {{PropertyData/de|Element List|LinkList|Hidden}}
    

-    {{PropertyData/de|_ Link Touched|Bool|Hidden}}
    

-    {{PropertyData/de|_ Child Cache|LinkList|Hidden}}
    

-    {{PropertyData/de|Colored Elements|LinkSubHidden|Hidden}}
    

-    {{PropertyData/de|Link Transform|Bool}}
    


{{TitleProperty|Anordnung}}

-    {{PropertyData/de|Align|Bool}}: Legt fest, ob die Elemente der Anordnung entlang des Pfades ausgerichtet werden oder nicht. Ist sie `False`, sind alle anderen Eigenschaften in dieser Gruppe, außer {{PropertyData/de|Extra Translation}} nicht anwendbar und werden ausgeblendet.

-    {{PropertyData/de|Align Mode|Enumeration}}: Legt das Ausrichtungsverfahren fest; zur Auswahl stehen {{Value|Original}}, {{Value|Frenet}} oder {{Value|Tangent}}.

-    {{PropertyData/de|End Offset|Length}}: Legt die Länge vom Ende des Pfades bis zur letzten Kopie fest. Muss kleiner sein als die Länge des Pfades abzüglich der {{PropertyData/de|Start Offset}}. {{Version/de|0.21}}

-    {{PropertyData/de|Extra Translation|VectorDistance}}: Legt einen zusätzlichen Versatz für jedes Element entlang des Pfades fest.

-    {{PropertyData/de|Force Vertical|Bool}}: Legt fest, ob die vorgegebene Ausrichtung der Normale mit dem Wert der {{PropertyData/de|Vertical Vector}} überschrieben wird. Wird nur verwendet, wenn die {{PropertyData/de|Align Mode}} auf {{Value|Original}} oder {{Value|Tangent}} gesetzt ist.

-    {{PropertyData/de|Start Offset|Length}}: Legt die Länge vom Startpunkt des Pfades bis zur ersten Kopie fest. Muss kleiner als die Länge des Pfades sein. {{Version/de|0.21}}

-    {{PropertyData/de|Tangent Vector|Vector}}: Legt den Ausrichtungsvektor fest. Wird nur verwendet, wenn die {{PropertyData/de|Align Mode}} auf {{Value|Tangent}} gesetzt ist.

-    {{PropertyData/de|Vertical Vector|Vector}}: Legt den Vektor zum Überschreiben der Richtung der Normale fest. Wird nur verwendet, wenn die {{PropertyData/de|Vertical Vector}} auf `True` gesetzt ist.


{{TitleProperty|Objekte}}

-    **Base|LinkGlobal**: legt das Objekt fest, welches im Array vervielfacht wird.

-    **Count|Integer**: legt die Anzahl der Elemente im Array fest.

-    **Expand Array|Bool**: legt fest, ob das Array in der [Baumansicht](Tree_view/de.md) ausgeklappt wird, um die Auswahl einzelner individueller Elemente zu ermöglichen. Nur bei verbundenen Arrays möglich.

-    **Fuse|Bool**: legt fest, ob einander überlappende Elemente im Array vereinigt werden oder nicht. Wird bei verbundenen Arrays nicht verwendet. <small>(v1.0)</small> 

-    **Path Object|LinkGlobal**: legt fest, welches Objekt als Pfad verwendet wird. Es muss {{Value|Kanten}} in seinem [Part TopoForm](Part_TopoShape/de.md) enthalten.

-    **Path Subelements|LinkSubListGlobal**: legt eine Liste mit Kanten des **Path Object** fest. Wenn geliefert, dann werden nur diese Kanten für den Pfad verwendet.



### Ansicht


{{TitleProperty|Verknüpfung}}

Die Eigenschaften dieser Gruppe, mit Ausnahme der ererbten Eigenschaften, stehen nur für Verknüpfungsanordnungen zur Verfügung. Siehe [Std VerknüpfungErstellen](Std_LinkMake/de#Eigenschaften.md) für weitere Informationen.

-    **Draw Style|Enumeration**
    

-    **Line Width|FloatConstraint**
    

-    **Override Material|Bool**
    

-    **Point Size|FloatConstraint**
    

-    **Selectable|Bool**: das ist eine geerbte Eigenschaft welche in der Auswahl Gruppe für andere Arrays aufscheint

-    **Shape Material|Material**
    


{{TitleProperty|Basis}}

Die Eigenschaftzen dieser Gruppe sind mit Ausnahme der geerbten Eigenschaft nur bei verbundenen Arrays verfügbar. Siehe [Std VerknüpfungErstellen](Std_LinkMake/de#Properties.md) für weitere Informationen.

-    **Child View Provider|PersistentObject|Hidden**
    

-    **Material List|MaterialList|Hidden**
    

-    **Override Color List|ColorList|Hidden**
    

-    **Override Material List|BoolList|Hidden**
    

-    **Proxy|PythonObject|Hidden**: das ist eine geerbte Eigenschaft.


{{TitleProperty|Anzeige Optionen}}

Die Eigenschaften in dieser Gruppe sind ererbte Eigenschaften. Siehe auch [Part Formelement](Part_Feature/de#Eigenschaften.md).

-    **Bounding Box|Bool**: diese Eigenschaft wird bei verbundenen Arrays nicht vererbt.

-    **Display Mode|Enumeration**: kann für verbundene Arrays {{value|Link}} oder {{value|ChildView}} sein. Für andere Arrays kann es: {{value|Flat Lines}}, {{value|Shaded}}, {{value|Wireframe}} oder {{value|Points}} sein.

-    **Show In Tree|Bool**
    

-    **Visibility|Bool**
    


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: nicht verwendet.

-    **Pattern Size|Float**: nicht verwendet.


{{TitleProperty|Objekt Stil}}

Die Eigenschaften dieser Gruppe werden nicht an Verknüpfungsanordnungen vererbt.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Zum Erstellen einer Pfad-Anordnung wird die Methode `make_path_array` des Draft-Moduls verwendet ({{Version/de|0.19}}). Diese Methode ersetzt die veraltete Methode `makePathArray`.


```python
path_array = make_path_array(base_object, path_object,
                             count=4, extra=App.Vector(0, 0, 0), subelements=None,
                             align=False, align_mode="Original", tan_vector=App.Vector(1, 0, 0),
                             force_vertical=False, vertical_vector=App.Vector(0, 0, 1),
                             use_link=True)
```

-    `base_object`ist das Objekt, das angeordnet werden soll. Es kann auch die Benennung (die Zeichenkette `Label`) eines Objekts im aktuellen Dokument sein.

-    `path_object`: Ist das Pfadobjekt (path object). Es kann auch die Benennung (die Zeichenkette `Label`) eines Objekts im aktuellen Dokument sein.

-    `count`ist die Anzahl der Elemente einer Anordnung.

-    `extra`ist ein Vektor, der jedes Element versetzt.

-    `subelements`ist eine Liste von Kanten im `path_object`, z.B. `["Edge1", "Edge2"]`. Wenn vorhanden, werden nur diese Kanten für den Pfad verwendet.

-   Ist `align` auf `True` gestzt, werden die Elemente abhängig von der Eigenschaft `align_mode`, die die Werte `"Original"`, `"Frenet"` oder `"Tangent"` annehmen kann, entlang des Pfades ausgerichtet.

-    `tan_vector`ist ein Einheitsvektor, der die örtliche Tangentenrichtung der Elemente entlang des Pfades festlegt. Er wird verwendet, wenn `align_mode` auf `"Tangent"` gesetzt ist.

-   Ist `force_vertical` auf `True` gsetzt, wird `vertical_vector` für die lokale Z-Achse der Elemente entlang des Pfades verwendet. Es wird verwendet, wenn `align_mode` auf `"Original"` oder `"Tangent"` gesetzt ist.

-   Ist `use_link` auf `True` gesetzt, werden [App-Links](App_Link/de.md) anstatt normaler Kopien erstellt.

-    `path_array`wird mit der erstellten Anordnung zurückgegeben.

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(500, -1000, 0)
p2 = App.Vector(1500, 1000, 0)
p3 = App.Vector(3000, 500, 0)
p4 = App.Vector(4500, 100, 0)
spline = Draft.make_bspline([p1, p2, p3, p4])
obj = Draft.make_polygon(3, 500)

path_array = Draft.make_path_array(obj, spline, 6)
doc.recompute()

wire = Draft.make_wire([p1, -p2, -p3, -p4])
path_array2 = Draft.make_path_array(obj, wire, count=3, extra=App.Vector(0, -500, 0), subelements=["Edge2", "Edge3"], align=True, force_vertical=True)
doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft PathArray/de
