---
 GuiCommand:
   Name: Draft PointArray
   Name/de: Draft PunktAnordnung
   MenuLocation: Änderung , Anordnungwerkzeuge , Punkt-Anordnung<br>Bearbeiten ,  Punkt-Anordnung
   Workbenches: Draft_Workbench/de, BIM_Workbench/de
   Version: 0.18
   SeeAlso: Draft_OrthoArray/de, Draft_PolarArray/de, Draft_CircularArray/de, Draft_PathArray/de, Draft_PathLinkArray/de, Draft_PointLinkArray/de
---

# Draft PointArray/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_PointArray.svg  style="width:24px;"> **Draft Punkt-Anordnung** erstellt eine regelmäßige Anordnung aus einem ausgewählten Basisobjekt, indem er Kopien auf den Punkten eines Punktobjekts positioniert. Der Befehl [Draft PunktVerknüpfungsanordnung](Draft_PointLinkArray/de.md) erstellt alternativ eine effizientere Verknüpfungsanordnung ([Link](App_Link/de.md)-Array). Außer der Art der Anordnung die erstellt wird, normale Anordnung oder Verknüpfungsanordnung, ist der Befehl [Draft PunktVerknüpfungsanordnung](Draft_PointLinkArray/de.md) identisch mit diesem Befehl.

Das Basisobjekt kann ein 2D-Objekt sein, das mit den Arbeitsbereichen [Draft](Draft_Workbench/de.md) oder [Sketcher](Sketcher_Workbench.md) erstellt wurde, aber auch ein 3D-Objekt, das mit den Arbeitsbereichen [Part](Part_Workbench/de.md), [PartDesign](PartDesign_Workbench/de.md) oder [BIM](BIM_Workbench/de.md) erstellt wurde.

Das Punktobjekt kann ein beliebiges Objekt mit einer Form und Knotenpunkten sein (einschließlich einem [Std Part](Std_Part/de.md), das ein oder mehrere solcher Objekte enthält), ein [Netz-Objekt](Mesh_Workbench/de.md) oder eine [Punktwolke](Points_Workbench/de.md). Doppelte Punkte im Punktobjekt werden herausgefiltert.

<img alt="" src=images/Draft_PointArray_Example.png  style="width:400px;"> 
*Draft Punkt-Anordnung*



## Anwendung

1.  Das Objekt auswählen, das angeordnet werden soll.
2.  Das Punkt-Objekt zur Auswahl hinzufügen.
3.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_PointArray.svg" width=16px> [Punkt-Anordnung](Draft_PointArray/de.md)** drücken.
    -   [Draft](Draft_Workbench/de.md): Den Menüeintrag **Änderung → Anordnungswerkzeuge → <img src="images/Draft_PointArray.svg" width=16px> Punkt-Anordnung** auswählen.
    -   [BIM](BIM_Workbench/de.md): Den Menüeintrag **Bearbeiten → <img src="images/Draft_PointArray.svg" width=16px> Punkt-Anordnung** auswählen.
4.  Die Anordnung wird erstellt.
5.  Wahlweise die [Eigenschaften](#Eigenschaften.md) der Anordnung im [Eigenschafteneditor](Property_editor/de.md) anpassen.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](property_editor/de.md).

Eine Punkt-Anordnung (PointArray-Objekt) ist von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften (mit Ausnahme einiger Ansicht-Eigenschaften, die nicht an die Verknüpfungsanordnungen vererbt werden). Außerdem sind, wenn nicht anders angegeben, die folgenden zusätzlichen Eigenschaften vorhanden:



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
    


{{TitleProperty|Objects}}

-    {{PropertyData/de|Base|Link}}: gibt das Objekt an, das in der Anordnung dupliziert werden soll.

-    {{PropertyData/de|Count|Integer}}: (nur Lesezugriff) gibt die Anzahl der Elemente in der Anordnung an. Diese Zahl wird durch die Anzahl der Punkte im {{PropertyData/de|Point Object}} bestimmt.

-    {{PropertyData/de|Expand Array|Bool}}: gibt an, ob die Anordnung in der [Baumansicht](Tree_view/de.md) erweitert werden soll, um die Auswahl der einzelnen Elemente zu ermöglichen. Nur für Verknüpfungsanordnung verfügbar.

-    {{PropertyData/de|Extra Placement|Placement}}: gibt für jedes Element in der Anordnung eine zusätzliche [Positionierung](Placement/de.md), Verschiebung und Drehung an.

-    {{PropertyData/de|Fuse|Bool}}: gibt an, ob die Kopien vereinigt werden sollen, wenn sie einander berühren oder nicht. Wird nicht für Verknüpfungsanordnungen verwendet. {{Version/de|1.0}}

-    {{PropertyData/de|Point Object|Link}}: gibt das Objekt an, dessen Punkte zur Positionierung der Elemente in der Anordnung verwendet werden.



### Ansicht


{{TitleProperty|Link}}

Die Eigenschaften dieser Gruppe, mit Ausnahme der ererbten Eigenschaften, stehen nur für Verknüpfungsanordnungen zur Verfügung. Siehe [Std VerknüpfungErstellen](Std_LinkMake/de#Eigenschaften.md) für weitere Informationen.

-    {{PropertyView/de|Draw Style|Enumeration}}
    

-    {{PropertyView/de|Line Width|FloatConstraint}}
    

-    {{PropertyView/de|Override Material|Bool}}
    

-    {{PropertyView/de|Point Size|FloatConstraint}}
    

-    {{PropertyView/de|Selectable|Bool}}: das ist eine übernommene Eigenschaft, die in der Auswahlgruppe für andere Anordnungen erscheint.

-    {{PropertyView/de|Shape Material|Material}}
    


{{TitleProperty|Basis}}

Die Eigenschaften dieser Gruppe, mit Ausnahme der ererbten Eigenschaften, stehen nur für Verknüpfungsanordnungen zur Verfügung. Siehe [Std VerknüpfungErstellen](Std_LinkMake/de#Eigenschaften.md) für weitere Informationen.

-    **Child View Provider|PersistentObject|Hidden**
    

-    **Material List|MaterialList|Hidden**
    

-    **Override Color List|ColorList|Hidden**
    

-    **Override Material List|BoolList|Hidden**
    

-    **Proxy|PythonObject|Hidden**: das ist eine geerbte Eigenschaft.


{{TitleProperty|Display Options}}

Die Eigenschaften in dieser Gruppe sind ererbte Eigenschaften. Siehe auch [Part Formelement](Part_Feature/de#Eigenschaften.md).

-    {{PropertyView/de|Bounding Box|Bool}}: diese Eigenschaft wird bei Verknüpfungsanordnungen nicht vererbt.

-    {{PropertyView/de|Display Mode|Enumeration}}: kann für Verknüpfungsanordnungen {{value|Link}} oder {{value|ChildView}} sein. Für andere Anordnung kann es: {{value|Flat Lines}}, {{value|Shaded}}, {{value|Wireframe}} oder {{value|Points}} sein.

-    {{PropertyView/de|Show In Tree|Bool}}
    

-    {{PropertyView/de|Visibility|Bool}}
    


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: nicht verwendet.

-    **Pattern Size|Float**: nicht verwendet.


{{TitleProperty|Object style}}

Die Eigenschaften dieser Gruppe werden nicht an Verknüpfungsanordnungen vererbt.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Zum Erstellen einer Punkt-Anordnung wird die Methode ` make_point_array` des Draft-Moduls verwendet ({{Version/de|0.19}}). Diese Methode ersetzt die veraltete Methode `makePointArray`.


```python
point_array = make_point_array(base_object, point_object, extra=None, use_link=True)
```

-    `base_object`ist das anzuordnende Objekt. Es kann auch die `Label` (-Zeichenkette) eines Objekts im aktuellen Dokument sein.

-    `point_object`ist das Objekt, das die Punkte enthält. Es kann auch die `Label` (-Zeichenkette) eines Objekts im aktuellen Dokument sein. Es sollte eine Eigenschaft `Geometry`, `Links` oder `Components` haben, die Punkte enthält.

-    `extra`ist ein `App.Placement`, ein `App.Vector` oder eine `App.Rotation`, die jedes Element verschiebt.

-   Wenn `use_link` auf `True` gesetzt ist, sind die erstellten Elemente [App-Links](App_Link/de.md) anstelle von regulären Kopien.

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

polygon = Draft.make_polygon(3, radius=500.0)

p1 = Draft.make_point(App.Vector(1500, 0, 0))
p2 = Draft.make_point(App.Vector(2500, 0, 0))
p3 = Draft.make_point(App.Vector(2000, 1000, 0))

compound = doc.addObject("Part::Compound", "Compound")
compound.Links = [p1, p2, p3]

point_array = Draft.make_point_array(polygon, compound)
doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft PointArray/de
