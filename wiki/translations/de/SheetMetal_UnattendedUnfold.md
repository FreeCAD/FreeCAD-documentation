---
- GuiCommand:/de
   Name:SheetMetal UnattendedUnfold
   Name/de:SheetMetal AbwickelnOhneEingabe
   MenuLocation:SheetMetal → Unattended Unfold
   Workbenches:[Blech (SheetMetal)](SheetMetal_Workbench/de.md)
   Shortcut:**U**
|[SheetMetal Abwickeln](SheetMetal_Unfold/de.md)
---

# SheetMetal UnattendedUnfold/de

## Beschreibung

Der Befehl <img alt="" src=images/SheetMetal_UnattendedUnfold.svg  style="width:24px;"> [Abwickeln ohne Eingaben](SheetMetal_UnattendedUnfold/de.md) wickelt ein Blechobjekt ab.

Wenn der Elternkörper einer ausgewählten ebenen Fläche schon zuvor von einer Abwicklung betroffen war, überspringt dieses Werkzeug das Menü im Aufgaben-Fenster. Andernfalls zeigt es eine Fehlermeldung, die auffordert einen K-Faktor anzugeben (\"set a Manual K-factor\") oder ein Materialdatenblatt zu verwenden (\"use a Material Definition Sheet\").

:   Mit der ersten Benutzung des <img alt="" src=images/SheetMetal_Unfold.svg  style="width:16px;"> [Abwickeln](SheetMetal_Unfold.md)-Befehls erhält das **Label** des Elternkörpers einen Zusatz (wie z.B. *\_material\_0.5din*) und ist danach bereit für die Benutzung mit diesem Werkzeug.

## Anwendung

1.  Eine ebene Fläche eines SheetMetal-Objekts auswählen. **Hinweis**: Die Fläche sollte eben und mit konstanter Wandstärke sein.
2.  Den Befehl <img alt="" src=images/SheetMetal_UnattendedUnfold.svg  style="width:16px;"> [Unattended Unfold](SheetMetal_UnattendedUnfold.md) aktivieren durch:
    -   Die Schaltfläche **<img src="images/_SheetMetal_UnattendedUnfold.svg_" width=16px> [Unattended Unfold](SheetMetal_UnattendedUnfold.md)
**
    -   Den Menüeintrag **SheetMetal → <img src="images/SheetMetal_UnattendedUnfold.svg" width=16px> [Unattended Unfold](SheetMetal_UnattendedUnfold.md)
**
    -   Das Tastenkürzel: **U**

## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Dieses Werkzeug erzeugt ein Unfold-Objekt und hat keine eigene Darstellung in der [Baumansicht](Tree_view/de.md) oder anderswo und hat daher auch keine Eigenschaften.

Das **Unfold**-Objeckt, andererseits, wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Es hat keine zusätzlichen Eigenschaften, aber sein Label hat einen Standardwert:

### Daten


{{Properties_Title/de|Basis}}

-    **Label|String**: Standardwert: Der vom Benutzer änderbare Name dieses Objekts, der aus einer beliebigen UTF8-Zeichenkette bestehen kann.

## Einschränkungen

Siehe <img alt="" src=images/SheetMetal_Unfold.svg  style="width:16px;"> [Abwicklung](SheetMetal_Unfold/de.md) für Einschränkungen.




[<img src="images/Property.png" style="width:16px"> SheetMetal](Category_SheetMetal.md) [<img src="images/Property.png" style="width:16px"> Addons](Category_Addons.md) [<img src="images/Property.png" style="width:16px"> External Command Reference](Category_External_Command_Reference.md)

---
[documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > SheetMetal UnattendedUnfold/de
