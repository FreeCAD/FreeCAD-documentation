---
- GuiCommand:
   Name: Part RefineShape
   Name/de: Part FormAufbereiten
   MenuLocation: Formteil -> Kopie erstellen -> Form aufbereiten
   Workbenches: Part_Workbench/de
   SeeAlso: Part_SimpleCopy/de, Part_TransformedCopy/de, Part_ElementCopy/de, OpenSCAD_RefineShapeFeature/de
---

# Part RefineShape/de



## Beschreibung

Die **<img src="images/Part_RefineShape.svg" width=16px> [Part FormAufbereiten](Part_RefineShape/de.md)** erzeugt eine nichtparametrische Kopie mit aufbereiteter Form, also einer mit bereinigten Kanten und Flächen.

Nach bestimmten booleschen Operationen, wie [Part Vereinigen](Part_Fuse/de.md), bleiben einige Linien aus den vorherigen Formen sichtbar. Dieses Werkzeug erzeugt eine Kopie dieses booleschen Ergebnisses und bereinigt diese Nähte.

**Alternativ**, um andere nicht-parametrische Kopien zu erstellen, verwende **<img src="images/Part_SimpleCopy.svg" width=16px> [Einfache Kopie](Part_SimpleCopy/de.md)
**, **<img src="images/Part_TransformedCopy.svg" width=16px>[TransformierteKopie](Part_TransformedCopy/de.md)**, und **<img src="images/Part_ElementCopy.svg" width=16px> [ElementKopie](Part_ElementCopy/de.md)**

![](images/PartRefineShape_it.png ) 
*Ursprüngliches boolesches Ergebnis mit 11Flächen (links) und aufbereitete Formkopie mit 7 Flächen (rechts).*



## Anwendung

1.  Ein Objekt auswählen, das aufbereitet und kopiert werden soll.
2.  Den Menüeintrag **Part → Kopie erstellen → <img src="images/Part_RefineShape.svg" width=16px> Form aufbereiten** auswählen.
3.  Eine bereinigte, unabhängige Kopie des Originalobjekts wird erstellt; das Originalobjekt wird ausgeblendet.

Ab {{VersionPlus/de|0.19}} ist das Ergebnis standardmäßig eine parametrische (verknüpfte) Kopie.

Dieses Verhalten kann im <img alt="" src=images/Std_DlgParameter.svg  style="width:24px;"> [Parametereditor](Std_DlgParameter/de.md) geändert werden:

1.  Gehe zur Untergruppe: `BaseApp/Preferences/Mod/Part`
2.  Ändere `ParametricRefine` vom Typ `Boolean` in `False`, um das alte Verhalten (unabhängige Kopie) zu erhalten.

Siehe weitere Parameter unter [Feinabstimmung](Fine-tuning/de.md).



## Hinweise

-   Diese Funktion kann als letzter Schritt in der Modellierungsarbeit verwendet werden, um Formen in einem herkömmlichen [konstruktive Solidgeometrie](constructive_solid_geometry/de.md) Arbeitsablauf zu bereinigen.
-   Diese Funktion kann helfen, das Modell zu bereinigen, bevor andere Funktionen wie z.B. ein [Part Verrundung](Part_Fillet/de.md) angewendet werden.
-   Diese Bereinigung kann 3D Drucker davon abhalten, unerwünschte Kanten zu drucken, sobald das Volumenmodell in ein Mesh Format exportiert wird.
-   Diese Funktion kann auch nach der Umwandlung eines Netzes in eine Form ([ShapeFromMesh](Part_ShapeFromMesh/de.md)) verwendet werden, um die Restkanten auf ebenen Flächen zu bereinigen.
-   Einige interessante Informationen darüber, was mit Positionierungen passiert und wie man mit Python auf sie zugreift, findet man in diesem [Forum-Post](https://forum.freecad.org/viewtopic.php?t=77568#p675456).



## Einschränkungen

-   Der Verfeinerungsalgorithmus funktioniert nur bei Schalen. Daher iteriert er über die Schalen der Eingabeform und erzeugt dann für jede Schale eine neue Schale mit verbundenen Flächen, wo immer möglich. Das bedeutet, dass der Algorithmus nichts tut, wenn Ihre Eingabeform nur eine Fläche, ein Draht, eine Kante oder ein Knoten ist.
-   Im Gegensatz zum <img alt="" src=images/OpenSCAD_RefineShapeFeature.svg  style="width:24px;"> [OpenSCAD RefineShapeFeature](OpenSCAD_RefineShapeFeature.md)-Anweisung

<img alt="" src=images/Part_RefineShape.svg  style="width:24px;"> [Part_FormAufbereiten](Part_RefineShape/de.md) wird nicht aktualisiert, wenn die vorhergehenden Formen geändert werden.



## Skripten

Der Python-Befehl zum Aufbereiten einer Form lautet wie folgt:


```python
shape.removeSplitter()
```



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part RefineShape/de
