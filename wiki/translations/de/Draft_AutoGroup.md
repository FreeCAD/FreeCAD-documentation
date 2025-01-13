---
 GuiCommand:
   Name: Draft AutoGroup
   Name/de: Draft AutoGruppieren
   Empty: 1
   Workbenches: Draft_Workbench/de, BIM_Workbench/de
   Version: 0.17
   SeeAlso: Draft_Layer/de, Std_Group/de
---

# Draft AutoGroup/de



## Beschreibung

Der Befehl **Draft AutoGruppieren** ändert die aktive [Draft-Ebene](Draft_Layer/de.md) oder [wahlweise](#Einstellungen.md) die aktive [Std Gruppe](Std_Group/de.md) bzw. gruppenartige [BIM](BIM_Workbench/de.md)-Objekte. Neue [Draft-](Draft_Workbench/de.md) und [BIM](BIM_Workbench/de.md)-Objekte werden automatisch auf dieser Ebene bzw. in dieser Gruppe eingefügt.

Dieser Befehl war ursprünglich für Gruppen gedacht, daher sein Name, wurde aber in FreeCAD-Version 0.19 überarbeitet als ein Ebenen-System eingeführt wurde. Da der Umgang mit Ebenen jetzt die Standardaufgabe des Befehls ist, liegt der Fokus dieser Seite im folgenden haupfsächlich auf Ebenen.

![](images/Draft_tray_menu.png ) 
*Das Ebenen-Menü im Draft-Fach*



## Anwendung

1.  Ebene auswählen(Optional), die in der [Baumansicht](Tree_view/de.md) aktiviert werden soll.
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Im [Draft Fach](Draft_Tray/de.md) die ![](images/Draft_tray_button_layer.png ) Schaltfläche auswählen. Diese Schaltfläche kann unterschiedlich aussehen. Wenn es eine aktive Ebene gibt, zeigt sie den Namen der Ebene und ein Ebenen-Symbol mit der Linien- und Flächenfarbe der Ebene.
    -   Ebene auswählen: Im Kontextmenü der [Baumansicht](Tree_view/de.md) die Option **<img src="images/button_right.svg" width=16px> Diese Ebene aktivieren** wählen.
3.  Wenn keine Ebene ausgewählt wurde, wird das Ebenen-Menü geöffnet. Einen der folgenden Schritte wählen:
    -   
        **Keine**
        
        , um ohne aktive Ebene zu arbeiten.

    -   Vorhandene Ebene auswählen, um sie zu aktivieren.

    -   
        **Neue Ebene hinzufügen**
        
        , um eine neue Ebene zu erstellen. Durch die Auswahl dieser Option wird die aktive Ebene nicht geändert.
4.  Wenn die aktive Ebene geändert wurde, wird die Schaltfläche im [Draft Fach](Draft_Tray.md) aktualisiert.



## Hinweise

-   Eine neue [Ebene](Draft_Layer/de.md) kann auch erstellt werden, indem mit der rechten Maustaste auf den Ebenen-Container in der [Baumansicht](Tree_view/de.md) geklickt und im Kontextmenü die Option **<img src="images/Draft_NewLayer.svg" width=16px> Neue Ebene hinzufügen** ausgewählt wird.
-   Wenn der [Konstruktionsmodus](Draft_ToggleConstructionMode/de.md) eingeschaltet ist, wird die aktive [Ebene](Draft_Layer/de.md) ignoriert.



## Einstellungen

Siehe auch: [Voreinstellungseditor](Preferences_Editor/de.md) und [Draft Einstellungen](Draft_Preferences/de.md).

-   Dieser Befehl kann optional auch Gruppen verarbeiten: **Bearbeiten → Einstellungen... → Draft → Allgemein → Gruppen in Ebenenliste einbeziehen**.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Ist der Arbeitsbereich [Draft](Draft_Workbench/de.md) aktiv, hat das FreeCADGui-Objekt eine Eigenschaft `draftToolBar`. Dieses `draftToolBar`-Objekt hat eine Eigenschaft `autogroup`, die den Namen der aktiven Autogruppe enthält oder `None` ist, wenn keine Autogruppe aktiv ist. Um die aktive Autogruppe zu ändern, wird die Methode `setAutoGroup` des `draftToolBar`-Objekts verwendet. Um Objekte in die aktive Autogruppe aufzunehmen, wird die Methode `autogroup` des Draft-Moduls verwendet.


```python
# This code only works if the Draft Workbench is active!

import FreeCAD as App
import FreeCADGui as Gui
import Draft

doc = App.newDocument()

polygon1 = Draft.make_polygon(5, radius=1000)
polygon2 = Draft.make_polygon(3, radius=500)
polygon3 = Draft.make_polygon(6, radius=220)

layer = Draft.make_layer()
Gui.draftToolBar.setAutoGroup(layer.Name)

Draft.autogroup(polygon1)
Draft.autogroup(polygon2)
Draft.autogroup(polygon3)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft AutoGroup/de
