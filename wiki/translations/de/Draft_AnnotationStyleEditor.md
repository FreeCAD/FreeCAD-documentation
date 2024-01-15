---
 GuiCommand:
   Name: Draft AnnotationStyleEditor
   Name/de: Draft BeschriftungsstilEditor
   MenuLocation: Anmerkung , Beschriftungsstile...
   Workbenches: Draft_Workbench/de
   SeeAlso: Draft_Text/de, Draft_Label/de, Draft_Dimension/de
   Version: 0.19
---

# Draft AnnotationStyleEditor/de



## Beschreibung

Das Werkzeug **<img src="images/Draft_AnnotationStyleEditor.svg" width=24px> [BeschriftungsstilEditor](Draft_AnnotationStyleEditor/de.md)**ermöglicht Stile festzulegen, die die visuellen Eigenschaften von Beschriftungsobjekten beeinflussen, die durch die Befehle [Draft Text](Draft_Text/de.md), [Draft Maß](Draft_Dimension/de.md) und [Draft Hinweis](Draft_Label/de.md) erstellt werden.

![](images/Draft_AnnotationStyleEditor_Dialog.png ) 
*Das Dialogfenster Anmerkungsstil-Editor*



## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_AnnotationStyleEditor.svg" width=16px> [Beschriftungsstile...](Draft_AnnotationStyleEditor/de.md)** drücken.
    -   Den Menüeintrag **Anmerkung → <img src="images/Draft_AnnotationStyleEditor.svg" width=16px> Beschriftungsstile...** auswählen.
2.  Das Dialogfenster **Anmerkungsstil-Editor** wird geöffnet.
3.  Einen Stil aus der Aufklappliste **Stil-Name** auswählen oder {{Value|Neu hinzufügen...}} auswählen, um einen neuen Stil zu definieren.
4.  Wahlweise die Eigenschaften des Stils anpassen.
5.  Wahlweise die Schaltläche **[<img src=images/Accessories-text-editor.svg style="width:16px"> Umbenennen** drücken, um den Stil umzubenennen.
6.  Wahlweise die Schaltläche **[<img src=images/Edit_Cancel.svg style="width:16px"> Löschen** drücken, um den Stil zu löschen.
7.  Wahlweise die Schaltläche **[<img src=images/Std_Import.svg style="width:16px">** drücken, um alle Stile aus einer **.json**-Datei zu importieren. Dies wird bestehende Stile mit dem gleichen Namen überschreiben.
8.  Wahlweise die Schaltläche **[<img src=images/Std_Export.svg style="width:16px">** drücken, um alle Stile in eine **.json**-Datei zu exportieren.
9.  Die Schaltfläche **OK** drücken, um das Dialogfenster zu schließen und den Befehl zu beenden.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Die Beschriftungsstile werden als geordnete Wörterbücher im `Meta`-Attribut des Dokuments gespeichert. Dieses Attribut wird vom Beschriftungsstil-Editor gelesen, wenn er geöffnet wird.


```python
>>> print(App.ActiveDocument.Meta["Draft_Style_Text red"])
{"ArrowSize": 2.0, "ArrowType": 0, "Decimals": 2, "DimOvershoot": 4.0, "ExtLines": 0.0, "ExtOvershoot": 4.0, "FontName": "DejaVu Sans", "FontSize": 10.0, "LineColor": 255, "LineSpacing": 1.0, "LineWidth": 2, "ScaleMultiplier": 1.0, "ShowLine": true, "ShowUnit": false, "TextColor": 4278190335, "TextSpacing": 3.0, "UnitOverride": ""}
```

Jeder Stil, der im Editor angezeigt wird, wird intern mit dem Stilnamen und vorangestelltem `Draft_Style_` gespeichert; dies verhindert Namenskonflikte mit anderen Schlüsseln, die in `Meta` gespeichert sein können, die beliebige Informationen enthalten können.

Du könntest jeden neuen Stil festlegen, durch hinzufügen der notwendigen Informationen zu einem Schlüssel, der mit `Draft_Style_` beginnt. Der entsprechende Wert dieses Schlüssels muss ein serialisiertes Wörterbuch das mit `json` verwendet.


```python
import json

meta = App.ActiveDocument.Meta
props = {"ArrowSize": 7.0, "LineWidth": 6}
meta["Draft_Style_Thick_lines"] = json.dumps(props)
App.ActiveDocument.Meta = meta
```

Die nicht eingegebenen Werte werden automatisch ausgefüllt, wenn dieser Stil im Stileditor ausgewählt ist und die Schaltfläche **OK** gedrückt wird.

Auf ähnliche Weise kann jedes serialisierte Wörterbuch für die Bearbeitung entpackt werden.


```python
import json

meta = App.ActiveDocument.Meta
new_dict = json.loads(meta["Draft_Style_Thick_lines"])
```

Die Eigenschaften müssen folgenden Typen entsprechen:

Zeichenfolgen:


```python
props = {
    "FontName": "DejaVu Sans",
    "UnitOverride": ""
}
```

Fließkommazahlen (müssen mit einem Punkt als Dezimaltrennzeichen angegeben werden):


```python
props = {
    "ArrowSize": 2.0,
    "DimOvershoot": 4.0,
    "ExtLines": 0.0,
    "ExtOvershoot": 4.0
    "FontSize": 10.0,
    "LineSpacing": 1.0,
    "ScaleMultiplier": 1.0,
    "TextSpacing": 3.0
}
```

Integer (Ganzzahlen):


```python
props = {
    "ArrowType": 0,
    "Decimals": 2,
    "LineColor": 255,
    "LineWidth": 2,
    "TextColor": 4278190335
}
```

Die Werte für {{Incode|TextColor}} und {{Incode|LineColor}} entsprechen einer 32-Bit-Ganzzahl, aus der die einzelnen RGBA-Werte entnommen werden können. {{Incode|ArrowType}} ist der Index einer Aufzählung.

Boolesche Werte:


```python
props = {
    "ShowLine": true
    "ShowUnit": false,
}
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft AnnotationStyleEditor/de
