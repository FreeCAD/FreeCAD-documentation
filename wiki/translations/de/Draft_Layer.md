---
 GuiCommand:
   Name: Draft Layer
   Name/de: Draft Layer
   MenuLocation: Dienstprogramme , Ebene
   Workbenches: Draft_Workbench/de
   Version: 0.19
   SeeAlso: Draft_AutoGroup/de, Draft_LayerManager/de
---

# Draft Layer/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_Layer.svg  style="width:24px;"> **Draft Layer** erstellt eine Draft-Ebene (Layer-Objekt - eine Zeichnungsebene, die einer Folienschicht bei mehrlagigen Zeichnungen entspricht). Eine Ebene ist eine besondere Art von Gruppe mit einigen [Darstellungseinstellungen](#Ansicht.md). Diese Einstellungen und alle Änderungen an ihnen werden an die Objekte auf dieser Ebene weitergegeben. Die Ebenen an sich werden in einer weiteren besonderen Gruppe abgelegt: dem Draft-Ebenen-Behälter (LayerContainer-Objekt).



## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_Layer.svg" width=16px> [Ebene](Draft_Layer.md)** drücken.
    -   Den Menüeintrag **Dienstprogramme → <img src="images/Draft_Layer.svg" width=16px> Ebene** auswählen oder die Menüoption im Kontextmenü der [Baumansicht](Tree_view/de.md) oder der [3D-Ansicht](3D_view/de.md) auswählen.
    -   Falls die Ebene schon vorhanden ist: Diese mit der rechten Maustaste in der [Baumansicht](Tree_view/de.md) anklicken und die Menüoption **<img src="images/Draft_NewLayer.svg" width=16px> Neue Ebene hinzufügen** aus dem Kontextmenü auswählen.
2.  Falls er noch nicht vorhanden ist, wird zuerst der Ebenen-Behälter erstellt.
3.  Eine Ebene wird erstellt und im Ebenen-Behälter abgelegt.
4.  Wahlweise die [Eigenschaften](#Eigenschaften.md) der Ebene anpassen.
5.  Wahlweise Objekte der Ebene zuordnen, indem sie in der [Baumansicht](Tree_view/de.md) auf die Ebene gezogen und abgelegt werden. Objekte können auch einer Ebene zugeordnet werden, indem man die {{PropertyData/de|Group}} der Ebene bearbeitet.
6.  Wahlweise die Ebene [aktivieren](#Ebenen-Optionen.md).



## Kontextmenü



### Optionen des Ebenen-Behälters 

Für ein Draft-Ebenen-Behälter sind diese zusätzlichen Optionen im Kontextmenü der [Baumansicht](Tree_view/de.md) vorhanden:

-    **<img src="images/Draft_Layer.svg" width=16px> Ebenenduplikate zusammenführen**: Führt alle Ebenen mit der gleichen Basisbezeichnung (base label) zusammen.

:   Die Basisbezeichnung einer Ebene ist ihre {{PropertyData/de|Label}} ohne nachgestellte Ziffern und Leerzeichen. Alle Ebenen mit derselben Basisbezeichnung werden zu einer einzigen Ebene zusammengeführt, deren {{PropertyData/de|Label}} auf diese Basisbezeichnung eingestellt ist.

-    **<img src="images/Draft_NewLayer.svg" width=16px> Neue Ebene hinzufügen**: fügt dem aktuellen Dokument eine neue Ebene hinzu.



### Optionen der Ebene 

Für eine Draft-Ebene sind diese zusätzlichen Optionen im Kontextmenü der [Baumansicht](Tree_view/de.md) verfügbar:

-    **<img src="images/button_right.svg" width=16px> [Diese Ebene aktivieren](Draft_AutoGroup/de.md)**: aktiviert die ausgewählte Ebene.

-    **<img src="images/Draft_SelectGroup.svg" width=16px> [Ebeneninhalt auswählen](Draft_SelectGroup/de.md)**: wählt die Objekte innerhalb der ausgewählten Ebene aus.



## Verhalten von Ziehen und Ablegen 


{{Version/de|0.21}}

Wenn ein Objekt aus einer [Std Gruppe](Std_Group/de.md) oder einem gruppenähnlichen Objekt, wie z. B. einem [Arch Gebäudeteil](Arch_BuildingPart/de.md), auf einer Ebene in der [Baumansicht](Tree_view/de.md) abgelegt wird, wird es nicht aus der Gruppe entfernt und umgekehrt. Um ein Objekt von einer Ebene zu entfernen, muss es auf einer anderen Ebene oder auf dem Dokumentenknoten abgelegt werden. Beim Ziehen von einer Ebene oder Ablegen auf einer Ebene muss die **Strg**-Taste nicht gedrückt werden.



## Hinweise

-   Eine neue Ebene kann auch mit dem Befehl [Draft AutoGruppieren](Draft_AutoGroup/de.md) erstellt werden.
-   Der Arbeitsbereich [BIM](BIM_Workbench/de.md) enthält ein komplettes [Werkzeug zum Verwalten von Ebenen](BIM_Layers/de.md), das später in den Arbeitsbereich [Draft](Draft_Workbench/de.md) integriert werden soll.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein Draft Layer-Objekt wird von einem [App FeaturePython](App_FeaturePython/de.md)-Objekt abgeleitet und erbt alle seine Eigenschaften. Außerdem besitzt es die folgenden zusätzlichen Eigenschaften:



### Daten


{{TitleProperty|Layer}}

-    {{PropertyData/de|Group|LinkList}}: Gibt die Objekte an, die der Ebene zugeordnet sind.



### Ansicht


{{TitleProperty|Layer}}

Die Eigenschaften in diesem Abschnitt werden auf Objekte angewendet, die sich innerhalb der Ebene befinden. Alle Änderungen an diesen Eigenschaften werden an sie weitergegeben. Für zwei Eigenschaften, die {{PropertyView/de|Line Color}} und die {{PropertyView/de|Shape Color}}, ist dieses Verhalten optional.

-    {{PropertyView/de|Draw Style|Enumeration}}: gibt den Zeichenstil der Ebene an: {{value|Solid}} (Vollinie), {{value|Dashed}} (Strichlinie), {{value|Dotted}} (Punktlinie) oder {{value|Dashdot}} Strich-Punkt-Linie

-    {{PropertyView/de|Line Color|Color}}: gibt die Linienfarbe der Ebene an.

-    {{PropertyView/de|Line Width|Float}}: gibt die Linienbreite der Ebene an.

-    {{PropertyView/de|Override Line Color Children|Bool}}: gibt an, ob Änderungen an der {{PropertyView/de|Line Color}} der Ebene auf die Objekte innerhalb der Ebene übertragen werden.

-    {{PropertyView/de|Override Shape Appearance Children|Bool}}: gibt an, ob Änderungen an der {{PropertyView/de|Shape Appearance}} der Ebene auf die Objekte innerhalb der Ebene übertragen werden. {{Version/de|1.0}}

-    {{PropertyView/de|Shape Appearance|MaterialList}}: gibt das Erscheinungsbild der zur Ebene gehörenden Formen an. {{Version/de|1.0}}

-    {{PropertyView/de|Shape Color|Color|hidden}}: gibt die Farbe der zur Ebene gehörenden Formen an. Sie wird mit der **Diffuse Color** (Streulichtfarbe) der {{PropertyView/de|Shape Appearance}} synchronisiert.

-    {{PropertyView/de|Transparency|Percent}}: gibt die Transparenz der Ebene an. Sie wird mit der **Transparenz** der {{PropertyView/de|Shape Appearance}} synchronisiert.


{{TitleProperty|Print}}

-    {{PropertyView/de|Line Print Color|Color}}: gibt die Liniendruckfarbe der Ebene an.

-    {{PropertyView/de|Use Print Color|Bool}}: gibt an, ob die {{PropertyView/de|Line Print Color|}} der Ebene verwendet wird, wenn eine [TechDraw DraftAnsicht](TechDraw_DraftView/de.md) aus den Objekten der Ebene erstellt wird.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Um eine Draft-Ebene zu erstellen, verwendet man die `make_layer` Methode des Draft-Moduls. Um Objekte zu einer Ebene hinzuzufügen oder daraus zu entfernen, wird ihre Eigenschaft `Group` geändert.


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

layer = Draft.make_layer(line_color=(1.0, 0.0, 0.0, 0.0),
                         shape_color=(1.0, 1.0, 0.0, 0.0))

polygon1 = Draft.make_polygon(5, radius=1000)
polygon2 = Draft.make_polygon(3, radius=500)
polygon3 = Draft.make_polygon(6, radius=220)
layer.Group = [polygon1, polygon2, polygon3]

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Layer/de
