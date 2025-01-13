---
 GuiCommand:
   Name: Draft OrthoArray
   Name/de: Draft RechtwinkligeAnordnung
   MenuLocation: Änderung , Anordnungswerkzeuge , Anordnung<br>Bearbeiten , Anordnung
   Workbenches: Draft_Workbench/de, BIM_Workbench/de
   Version: 0.19
   SeeAlso: Draft_PolarArray/de, Draft_CircularArray/de, Draft_PathArray/de, Draft_PathLinkArray/de, Draft_PointArray/de, Draft_PointLinkArray/de
---

# Draft OrthoArray/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_OrthoArray.svg  style="width:24px;"> **Draft RechtwinkligeAnordnung** erstellt eine (in 3 Achsen) rechtwinklige Anordnung von einem ausgewählten Objekt. Der Befehl kann wahlweise auch eine Verknüpfungsanordnung ([Link](App_Link/de.md)-Array) erstellen, die effizienter ist, als eine normale Anordnung.

Dieser Befehl kann für 2D-Objekte verwendet werden, die mit den Arbeitsbereichen [Draft](Draft_Workbench/de.md) oder [Sketcher](Sketcher_Workbench/de.md) erstellt wurden, aber auch für viele 3D-Objekte, die mit anderen Arbeitsbereichen wie [Part](Part_Workbench/de.md), [PartDesign](PartDesign_Workbench/de.md) oder [BIM](BIM_Workbench/de.md) erstellt wurden.

<img alt="" src=images/Draft_Array_example.png  style="width:300px;"> 
*Rechtwinklige Draft-Anordnung*



## Anwendung

1.  Wahlweise ein Objekt auswählen.
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_OrthoArray.svg" width=16px> [Anordnung](Draft_OrthoArray.md)** drücken.
    -   [Draft](Draft_Workbench/de.md): Den Menüeintrag **Änderung → Anordnungswerkzeuge → <img src="images/Draft_OrthoArray.svg" width=16px> Anordnung** auswählen.
    -   [BIM](BIM_Workbench/de.md): Den Menüeintrag **Bearbeiten → <img src="images/Draft_OrthoArray.svg" width=16px> Anordnung** auswählen.
3.  Der Aufgabenbereich **Rechtwinklige Anordnung** wird geöffnet. Siehe auch [Optionen](#Optionen.md).
4.  Ein Objekt auswählen, wenn noch keins ausgewählt wurde.
5.  Die erforderlichen Parameter im Aufgabenbereich eingeben.
6.  Eine der folgenden Möglichkeiten zum Fertigstellen auswählen:
    -   In die [3D-Ansicht](3D_view/de.md) klicken.

    -   
        **Enter**
        
        drücken.

    -   Die Schaltfläche **OK** drücken.



## Optionen

-   Die**Number of elements** für die X, Y and Z-Richtung eingeben. Die Zahl muss mindestens {{Value|1}} für jede Richtung sein.
-   Das **X-Interval** eingeben, um den Versatz der Elemente in X-Richtung festzulegen. Für ein rechteckiges Feld müssen die Werte für Y und Z {{Value|0}} sein.
-   Das **Y-Interval** eingeben, um den Versatz der Elemente in Y-Richtung festzulegen. Für ein rechteckiges Feld müssen die Werte für X und Z {{Value|0}} sein.
-   Das **Z-Interval** eingeben, um den Versatz der Elemente in Z-Richtung festzulegen. Für ein rechteckiges Feld müssen die Werte für X und Y {{Value|0}} sein.
-   Auf die **Reset X, Y oder Z**-Schaltfläche klicken, um den Versatz in der gegangenen Richtung zurück zu den Vorgabewerten zurück zu setzen.
-   Ist das **Fuse**-Kästchen angehakt, werden überlappende Elemente im Feld miteinander verschmolzen. Das funktioniert nicht bei Verknüpften Feldern (link arrays).
-   Ist das **Link array**-Kästchen angehakt, wird ein Verknüpftes Feld anstelle eines regulären Feldes erstellt. Ein Verknüpftes Feld ist effizienter, weil seine Elemente von [Anwendungsverknüpfungen](App_Link/de.md) Objekte sind.
-   Mit der **Esc**-Taste oder der **Cancel**-Schaltfläche kann die Ausführung abgebrochen werden.



## Hinweise

-   Eine Draft RechtwinkligeAnordnung kann in eine [Draft PolareAnordnung](Draft_PolarArray/de.md) oder eine [Draft KreisAnordnung](Draft_CircularArray/de.md) umgewandelt werden, indem ihre {{PropertyData/de|Array Type}} verändert wird.
-   Eine Verknüpfungsanordnung (Link-Array) kann nicht in eine normale Anordnung oder zurück umgewandelt werden. Diese Auswahl der Anordnungsart muss zum Erstellungszeitpunkt erfolgen.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Der Befehle Draft RechtwinkligeAnordnung, [Draft PolareAnordnung](Draft_PolarArray/de.md) und [Draft KreisAnordnung](Draft_CircularArray/de.md) erstellen dasselbe Objekt. Dieses Objekt ist von einem [Part-Formelement](Part_Feature/de.md)-Objekt abgeleitet und erbt alle seine Eigenschaften (mit Ausnahme einiger Ansicht-Eigenschaften die nicht an die Verknüpfungsanordnungen vererbt werden). Außerdem sind, wenn nicht anders angegeben, die folgenden zusätzlichen Eigenschaften vorhanden:



### Daten


{{TitleProperty|Verknüpfung}}

Die Eigenschaften dieser Gruppe gibt es nur für Vernüpfungsanordnungen (Link-Arrays). Siehe auch [Std VerknüpfungErstellen](Std_LinkMake/de#Eigenschaften.md).

-    **Scale|Float**
    

-    **Scale Vector|Vector|Hidden**
    

-    **Scale List|VectorList**
    

-    **Visibility List|BoolList|Hidden**
    

-    **Placement List|PlacementList|Hidden**
    

-    **Element List|LinkList|Hidden**
    

-    **_ Link Touched|Bool|Hidden**
    

-    **_ Child Cache|LinkList|Hidden**
    

-    **Colored Elements|LinkSubHidden|Hidden**
    

-    **Link Transform|Bool**
    


{{TitleProperty|Kreisanordnung}}

Die Eigenschaften dieser Gruppe werden für rechtwinklige und polare Anordnungen verborgen.

-    **Number Circles|Integer**: legt die Anzahl der umlaufenden Abschnitte fest. Muss mindestens {{Value|2}} sein.

-    **Radial Distance|Distance**: legt den Abstand zwischen zwei umlaufenden Abschnitten fest.

-    **Symmetry|Integer**: legt die Anzahl der Symmetrielinien fest. Diese Zahl ändert die Verteilung der Elemente im Array.

-    **Tangential Distance|Distance**: Legt den Abstand zwischen Elementen im gleichen umlaufenden Layer fest. Muss größer als Null sein.


{{TitleProperty|Objekte}}

-    {{PropertyData/de|Array Type|Enumeration}}: legt den Typ des Array fest, dieser kann {{value|ortho}}, {{value|polar}} oder {{value|circular}} sein.

-    {{PropertyData/de|Axis Reference|LinkGlobal}}: legt das Objekt und die Kante fest, die an Stelle der Eigenschaften **Axis** und {{PropertyData/de|Center}} verwendet werden. Wird bei rechtwinkeligen Arrays nicht verwendet.

-    {{PropertyData/de|Base|Link}}: legt das Objekt fest, welches im Array dupliziert wird.

-    {{PropertyData/de|Count|Integer}}: (nur lesen) legt die Gesamtzahl der Elemente im Array fest.

-    {{PropertyData/de|Expand Array|Bool}}: legt fest, ob es möglich ist das Array in der [Baumansicht](Tree_view/de.md) zu erweitern, sodass die Auswahl von einzelnen Elementen möglich wird. Nur bei verbundenen Arrays möglich.

-    {{PropertyData/de|Fuse|Bool}}: legt fest, ob einander überschneidende Elemente im Array verschmolzen werden oder nicht. Nicht verwendet bei verbundenen Arrays.


{{TitleProperty|Orthogonales Feld}}

Die Eigenschaften dieser Gruppe werden für Kreis-Anordnungen verborgen.

-    **Interval X|VectorDistance**: legt das Intervall zwischen Elementen in Richtung X fest.

-    **Interval Y|VectorDistance**: legt das Intervall zwischen Elementen in Richtung Y fest.

-    **Interval Z|VectorDistance**: legt das Intervall zwischen Elementen in Richtung Z fest.

-    **Number X|Integer**: legt die Anzahl der Elemente in Richtung X fest. Muss mindestens {{Value|1}} sein.

-    **Number Y|Integer**: legt die Anzahl der Elemente in Richtung Y fest. Muss mindestens {{Value|1}} sein.

-    **Number Z|Integer**: legt die Anzahl der Elemente in Richtung Z fest. Muss mindestens {{Value|1}} sein.


{{TitleProperty|Polares Feld}}

Die Eigenschaften dieser Gruppe werden für Kreis-Anordnungen und rechtwinklige Anordnungen verborgen.

-    **Angle|Angle**: legt den Öffnungswinkel des umlaufenden Bogens fest. Für einen Vollkreis {{value|360&#176;}} verwenden.

-    **Interval Axis|VectorDistance**: legt das Intervall zwischen Elementen in der **Axis** Richtung fest.

-    **Number Polar|Integer**: legt die Anzahl der Elemente in polarer Richtung fest.


{{TitleProperty|Polares/umlaufendes Array}}

Die Eigenschaften dieser Gruppe werden für rechtwinklige Anordnungen verborgen.

-    **Axis|Vector**: legt die Richtung der Achse des Array fest.

-    **Center|VectorDistance**: legt den Mittelpunkt des Array fest. Die Achse des Array geht durch diesen Punkt. Für umlaufende Arrays ist das der Abstand vom **Placement** des **Base** Objektes.



### Ansicht


{{TitleProperty|Verknüpfung}}

Die Eigenschaften dieser Gruppe, mit Ausnahme der ererbten Eigenschaften, stehen nur für Verknüpfungsanordnungen zur Verfügung. Siehe [Std VerknüpfungErstellen](Std_LinkMake/de#Eigenschaften.md) für weitere Informationen.

-    **Draw Style|Enumeration**
    

-    **Line Width|FloatConstraint**
    

-    **Override Material|Bool**
    

-    **Point Size|FloatConstraint**
    

-    **Selectable|Bool**: das ist eine geerbte Eigenschaft die in der Auswahlgruppe für andere Arrays aufscheint.

-    **Shape Material|Material**
    


{{TitleProperty|Basis}}

Die Eigenschaften dieser Gruppe, mit Ausnahme der ererbten Eigenschaften, stehen nur für Verknüpfungsanordnungen zur Verfügung. Siehe [Std VerknüpfungErstellen](Std_LinkMake/de#Eigenschaften.md) für weitere Informationen.

-    **Child View Provider|PersistentObject|Hidden**
    

-    **Material List|MaterialList|Hidden**
    

-    **Override Color List|ColorList|Hidden**
    

-    **Override Material List|BoolList|Hidden**
    

-    **Proxy|PythonObject|Hidden**: das ist eine geerbte Eigenschaft.


{{TitleProperty|Zeige Auswahlmöglichkeiten}}

Die Eigenschaften in dieser Gruppe sind ererbte Eigenschaften. Siehe auch [Part Formelement](Part_Feature/de#Eigenschaften.md).

-    **Bounding Box|Bool**: diese Eigenschaft ist nicht durch Verknüpfungsfelder vererbt.

-    **Display Mode|Enumeration**: für Verknüpfungsfelder kann es {{value|Link}} oder {{value|ChildView}} sein. Für andere Felder können es: {{value|Flat Lines}}, {{value|Shaded}}, {{value|Wireframe}} oder {{value|Points}} sein.

-    **Show In Tree|Bool**
    

-    **Visibility|Bool**
    


{{TitleProperty|Entwurf}}

-    **Pattern|Enumeration**: nicht verwendet.

-    **Pattern Size|Float**: nicht verwendet.


{{TitleProperty|Objectstil}}

Die Eigenschaften dieser Gruppe werden nicht an Verknüpfungsanordnungen vererbt.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).



### Parametrische Anordnung 

Zum Erstellen einer parametrischen rechteckigen Anordnung wird die Methode `make_array` des Draft-Moduls verwendet ({{Version/de|0.19}}). Diese Methode ersetzt die veraltete Methode `makeArray`. Die Methode `make_array` kann rechteckige Draft-Anordnungen, [Draft PolareAnordnungen](Draft_PolarArray/de.md) und [Draft KreisAnordnungen](Draft_CircularArray/de.md) erstellen. Für jede Anordnungsart stehen eine oder mehrere Wrapper-Methoden zur Verfügung.

Die Hauptmethode:


```python
array = make_array(base_object, arg1, arg2, arg3, arg4=None, arg5=None, arg6=None, use_link=True)
```

Die Verbinder (wrapper) für orthogonale Anordnungen sind:


```python
array = make_ortho_array(base_object,
                         v_x=App.Vector(10, 0, 0), v_y=App.Vector(0, 10, 0), v_z=App.Vector(0, 0, 10),
                         n_x=2, n_y=2, n_z=1,
                         use_link=True)
```


```python
array = make_ortho_array2d(base_object,
                           v_x=App.Vector(10, 0, 0), v_y=App.Vector(0, 10, 0),
                           n_x=2, n_y=2,
                           use_link=True)
```

Die Verbinder (wrapper) für rechteckige Anordnungen sind:


```python
array = make_rect_array(base_object,
                        d_x=10, d_y=10, d_z=10,
                        n_x=2, n_y=2, n_z=1,
                        use_link=True)
```


```python
array = make_rect_array2d(base_object,
                          d_x=10, d_y=10,
                          n_x=2, n_y=2,
                          use_link=True)
```

-    `base_object`ist das Objekt, aus dem ein Array gemacht werden soll. Es kann auch der `Label` (string) eines Objekts im aktuellen Dokument sein.

-    `v_x`, `v_y`, und `v_z`sind die Vektoren zwischen den Basispunkten der Elemente in den jeweiligen Richtungen.

-    `d_x`, `d_y`, und `d_z`sind die Abstände zwischen den Basispunkten der Elemente in den jeweiligen Richtungen.

-    `n_x`, `n_y`, und `n_z` ist die Anzahl der Elemente in den jeweiligen Richtungen.

-   Wenn `use_link` auf `True` ist, dann sind die erzeugten Elemente [App Links](App_Link/de.md) statt richtiger Kopien.

-    `array`wird mir dem erzeugten Array Element zurück gegeben.

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rect = Draft.make_rectangle(1500, 500)
v_x = App.Vector(1600, 0, 0)
v_y = App.Vector(0, 600, 0)

array = Draft.make_ortho_array2d(rect, v_x, v_y, 3, 4)
doc.recompute()
```



### Feste Anordnung (nicht parametrisch) 

Um eine feste, nicht parametrische Anordnung zu erstellen, verwendet man die `array`-Methode des Enwurfmoduls. Diese Methode gibt `None` aus.


```python
array(objectslist, xvector, yvector, xnum, ynum)
array(objectslist, xvector, yvector, zvector, xnum, ynum, znum)
```

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rect = Draft.make_rectangle(1500, 500)
v_x = App.Vector(1600, 0, 0)
v_y = App.Vector(0, 600, 0)

Draft.array(rect, v_x, v_y, 3, 4)
doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft OrthoArray/de
