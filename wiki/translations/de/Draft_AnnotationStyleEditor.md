---
- GuiCommand:/de
   Name:Draft AnnotationStyleEditor
   Name/de:Entwurf AnmerkungsStilEditor
   MenuLocation:Anmerkung → Anmerkungsstile...
   Workbenches:[Entwurf](Draft_Workbench/de.md)
   SeeAlso:[Entwurf Text](Draft_Text/de.md), [Entwurf Beschriftung](Draft_Label/de.md), [Entwurf Abmessung](Draft_Dimension/de.md)
   Version:0.19
---

# Draft AnnotationStyleEditor/de



## Beschreibung

Das **<img src="images/Draft_AnnotationStyleEditor.svg" width=24px> [Anmeldungsstileditor](Draft_AnnotationStyleEditor/de.md)**-Werkzeug ermöglicht es dir, Stile zu definieren, die die visuellen Eigenschaften von anmerkungsähnlichen Objekten beeinflussen, wie z.B. jene, die durch [Text](Draft_Text/de.md)-, [Abmessung](Draft_Dimension/de.md)- und [Beschriftung](Draft_Label/de.md)-Befehle erstellten.


<small>(v1.0)</small> 

: Several bugs have been fixed and a separate Text color button has been added.

![](images/Draft_AnnotationStyleEditor_Dialog.png ) 
*Die AnmerkungsStileditor-Dialog-Box.*



## Anwendung

1.  Es gibt mehrere Wege, den Befehl aufzurufen:
    -   Drücke die **<img src="images/Draft_AnnotationStyleEditor.svg" width=16px> [Draft Anmerkungsstil-Editor](Draft_AnnotationStyleEditor/de.md)**-Schaltfläche.
    -   Wähle die **Annotation → <img src="images/Draft_AnnotationStyleEditor.svg" width=16px> Anmerkungs Stile...**-Option aus dem Menü.
2.  Die **Anmerkungsstil-Editor**-Dialog-Box öffnet sich.
3.  Wähle einen Stil aus der **Stil-Name** Aufklappliste oder wähle {{Value|Neu hinzufügen...}}, um einen neuen Stil zu definieren.
4.  Passe wahlweise die Eigenschaften des Stils an.
5.  Drücke wahlweise die **[<img src=images/Accessories-text-editor.svg style="width:16px"> Umbenennen**-Schaltläche, um den Stil umzubenennen.
6.  Drücke wahlweise die **[<img src=images/Edit_Cancel.svg style="width:16px"> Löschen**-Schaltfläche, um den Stil zu löschen.
7.  Drücke wahlweise die **[<img src=images/Std_Import.svg style="width:16px">**-Schaltfläche, um alle Stile aus einer **.json**-Datei zu importieren. Dies wird bestehende Stile mit dem gleichen Namen überschreiben.
8.  Drücke wahlweise die **[<img src=images/Std_Export.svg style="width:16px">**-Schaltfläche, um alle Stile in eine **.json**-Datei zu exportieren.
9.  Drücke die **OK**-Schaltfläche, um die Dialog-Box zu schließen und den Befehl zu beenden.



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).


<small>(v1.0)</small> 

: The information in this paragraph has been updated and reflects FreeCAD version 1.0.

Die Anmerkungsstile werden als serialisierte Wörterbücher im `Meta` Attribut des Dokuments gespeichert. Dieses Attribut wird vom Anmerkungsstileditor überprüft, wenn er geöffnet wird.


```python
>>> print(App.ActiveDocument.Meta["Draft_Style_Text red"])
{"FontName": "DejaVu Sans", "FontSize": 10.0, "LineSpacing": 1.0, "TextColor": 4278190335, "ScaleMultiplier": 1.0, "ShowUnit": false, "UnitOverride": "", "Decimals": 2, "ShowLine": true, "LineWidth": 2, "ArrowType": 0, "ArrowSize": 2.0, "LineColor": 255, "DimOvershoot": 0.0, "ExtLines": 0.0, "ExtOvershoot": 4.0}
```

Jeder Stil, der im Editor angezeigt wird, wird intern mit dem Stilnamen mit dem Präfix `Draft_Style_` gespeichert; dies verhindert Namenskonflikte mit anderen Schlüsseln, die in `Meta` gespeichert sein können, die beliebige Informationen enthalten können.

Du könntest jeden neuen Stil festlegen, durch hinzufügen der notwendigen Informationen zu einem Schlüssel, der mit `Draft_Style_` beginnt. Der entsprechende Wert dieses Schlüssels muss ein serialisiertes Wörterbuch das mit `json` verwendet.


```python
import json

meta = App.ActiveDocument.Meta
props = {"LineWidth": 6, "ArrowSize": 7.0}
meta["Draft_Style_Thick_lines"] = json.dumps(props)
App.ActiveDocument.Meta = meta
```


<div class="mw-translate-fuzzy">

Die nicht eingegebenen Werte werden automatisch ausgefüllt, wenn dieser Stil im Stileditor ausgewählt wird.


</div>

Auf ähnliche Weise kann jedes serialisierte Wörterbuch für die Ausgabe entpackt werden.


```python
import json

meta = App.ActiveDocument.Meta
new_dict = json.loads(meta["Draft_Style_Thick_lines"])
```

The properties must have the following types:

Zeichenfolgen:


```python
props = {
    "FontName": "DejaVu Sans",
    "UnitOverride": ""
}
```

Floats (must be supplied with a decimal point):


```python
props = {
    "FontSize": 10.0,
    "LineSpacing": 1.0,
    "ScaleMultiplier": 1.0,
    "ArrowSize": 2.0,
    "DimOvershoot": 0.0,
    "ExtLines": 0.0,
    "ExtOvershoot": 4.0
}
```

Integers:


```python
props = {
    "TextColor": 4278190335,
    "Decimals": 2,
    "LineWidth": 2,
    "ArrowType": 0,
    "LineColor": 255
}
```


<div class="mw-translate-fuzzy">

Die Linienfarbe entspricht der 32-Bit Ganzzahl, aus der die einzelnen RGBA Werte extrahiert werden können.


</div>


<div class="mw-translate-fuzzy">

Boolesch:


</div>


```python
props = {
    "ShowUnit": false,
    "ShowLine": true
}
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft AnnotationStyleEditor/de
