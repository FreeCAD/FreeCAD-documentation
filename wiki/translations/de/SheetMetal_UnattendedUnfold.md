---
 GuiCommand:
   Name: SheetMetal UnattendedUnfold
   Name/de: SheetMetal AbwickelnOhneEingabe
   MenuLocation: SheetMetal , Unattended Unfold
   Workbenches: SheetMetal_Workbench/de
   Shortcut: **U**

---

# SheetMetal UnattendedUnfold/de



## Beschreibung

Der Befehl <img alt="" src=images/SheetMetal_UnattendedUnfold.svg  style="width:24px;"> [Abwickeln ohne Eingaben](SheetMetal_UnattendedUnfold/de.md) wickelt ein Blechobjekt ab.

Dieser Befehl steht nicht standardmäßig zur Verfügung, siehe [Hinweise](#Hinweise.md).

Wenn der Elternkörper einer ausgewählten ebenen Fläche schon zuvor von einer Abwicklung betroffen war, überspringt dieses Werkzeug das Menü im Aufgaben-Fenster. Andernfalls zeigt es eine Fehlermeldung, die auffordert einen K-Faktor anzugeben (\"set a Manual K-factor\") oder ein Materialdatenblatt zu verwenden (\"use a Material Definition Sheet\").

Mit der ersten Benutzung des Befehls <img alt="" src=images/SheetMetal_Unfold.svg  style="width:16px;"> [Abwickeln](SheetMetal_Unfold/de.md) erhält das **Label** des übergeordneten Körpers einen Zusatz (wie z.B. *\_material_0.5din*) und ist danach bereit für die Benutzung mit diesem Befehl.



## Anwendung

1.  Eine ebene Fläche eines SheetMetal-Objekts auswählen.
2.  Den Befehl <img alt="" src=images/SheetMetal_UnattendedUnfold.svg  style="width:16px;"> [Unattended Unfold](SheetMetal_UnattendedUnfold/de.md) aktivieren durch:
    -   Die Schaltfläche **<img src="images/_SheetMetal_UnattendedUnfold.svg_" width=16px> [Unattended Unfold](SheetMetal_UnattendedUnfold.md)
**
    -   Den Menüeintrag **SheetMetal → <img src="images/SheetMetal_UnattendedUnfold.svg" width=16px> [Unattended Unfold](SheetMetal_UnattendedUnfold.md)
**
    -   Das Tastenkürzel: **U**



## Hinweise

Damit dieser Befehl zur Verfügung steht, muss zuerst der Engineering Mode in den Voreinstellungen aktiviert werden. Zu **Bearbeiten → Einstellungen... → SheetMetal → Allgemeine Einstellungen** wechseln und **Engineering UX Mode** auf {{Value|Enabled}} setzen. Das Ändern dieser Voreinstellung erfordert einen Neustart von FreeCAD.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Das SheetMetal-**Unfold**-Objekt, wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Es hat keine zusätzlichen Eigenschaften, aber sein Label hat einen Standardwert:



### Daten


{{Properties_Title/de|Basis}}

-    **Label|String**: Standardwert: Der vom Benutzer änderbare Name dieses Objekts, der aus einer beliebigen UTF8-Zeichenkette bestehen kann.



## Einschränkungen

Siehe <img alt="" src=images/SheetMetal_Unfold.svg  style="width:16px;"> [Abwicklung](SheetMetal_Unfold/de.md) für Einschränkungen.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal UnattendedUnfold/de
