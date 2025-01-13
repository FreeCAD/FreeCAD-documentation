---
 GuiCommand:
   Name: Part RefineShape
   Name/de: Part FormAufbereiten
   MenuLocation: Part , Kopie erstellen , Form aufbereiten
   Workbenches: Part_Workbench/de
   SeeAlso: 
---

# Part RefineShape/de



## Beschreibung

Der Befehl <img alt="" src=images/Part_RefineShape.svg  style="width:24px;"> **Part FormAufbereiten** erstellt aus ausgewählten Objekten parametrische Kopien mit einer aufbereiteten Form. Er entfernt unnötige Kanten auf ebenen und zylindrischen Flächen.

![](images/PartRefineShape_it.png ) 
*Original mit 11 Flächen (links) und aufbereitete Kopie mit 7 Flächen (rechts).*



## Anwendung

1.  Ein oder mehrere Objekte auswählen.
2.  Den Menüeintrag **Part → Kopie erstellen → <img src="images/Part_RefineShape.svg" width=16px> Form aufbereiten** auswählen.
3.  Für jedes Objekt wird eine bereinigte parametrische Kopie erstellt.
4.  Das Originalobjekt wird ausgeblendet.



## Hinweise

-   Dieser Befehl kann als letzter Schritt in einem herkömmlichen Arbeitsablauf für [konstruktive Festkörpergeometrie](constructive_solid_geometry/de.md) eingesetzt werden.
-   Es kann helfen, das Modell zu bereinigen, bevor andere Formelemente wie z.B. eine [Part-Verrundung](Part_Fillet/de.md) eingesetzt werden.
-   Ein Objekt zu bereinigen kann 3D-Drucker davor bewahren, unerwünschte Kanten zu drucken, sobald das Objekt in ein Netzformat exportiert wird.
-   Dieser Befehl kann auch nach der Umwandlung eines Netzes in eine Form ([Part FormAusNetz](Part_ShapeFromMesh/de.md)) verwendet werden.
-   Standardmäßig erstellt dieser Befehl parametrische (verknüpfte) Kopien. Es gibt [Feinabstimmung](Fine-tuning/de.md)-Parameter zum Ändern dieser nicht parametrischen Kopien. Weitere Informationen über das Verhalten von parametrischem bzw. nicht parametrischem Kopieren kann man hier finden: [Forum-Post](https://forum.freecad.org/viewtopic.php?t=42993).
-   Einige interessante Informationen darüber, was mit Positionierungen passiert und wie man mit Python auf sie zugreift, findet man in diesem [Forum-Post](https://forum.freecad.org/viewtopic.php?t=77568#p675456).



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein Part RefineShape-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem besitzt es die folgende zusätzliche Eigenschaft:



### Daten


{{TitleProperty|Refine}}

-    **Source|Link**: Gibt die verknüpfte Ausgangsform an.



## Skripten

Der Python-Befehl zum Aufbereiten einer Form lautet wie folgt:


```python
shape.removeSplitter()
```





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part RefineShape/de
