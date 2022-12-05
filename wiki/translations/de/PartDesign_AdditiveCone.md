---
- GuiCommand:/de
   Name:PartDesign AdditiveCone
   Name/de:PartDesign Additiver Kegel
   MenuLocation:Part Design → Erzeugen eines zusätzlichen Grundelements → Additiver Kegel
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   Version:0.17
   SeeAlso:[PartDesign CompAdditivesGrundelement](PartDesign_CompPrimitiveAdditive/de.md)
---

# PartDesign AdditiveCone/de


</div>

## Beschreibung

Fügt einen Kegel in den aktiven Körper (body) als Basisformelement ein oder vereinigt ihn mit den bereits bestehenden Formelementen.

<img alt="" src=images/PartDesign_AdditiveCone_example.png  style="width:200px;">

## Anwendung


<div class="mw-translate-fuzzy">

1.  Drücke die **<img src="images/PartDesign_AdditiveCone.svg" width=24px> '''Additiver Kegel'''** Schaltfläche. **Hinweis**: der Additive Kegel ist Teil eines Symbolmenüs mit der Bezeichnung *Erstellen eines additiven Grundelements*. Nach dem Start von FreeCAD wird der Additiv Quader in der Werkzeugleiste angezeigt. Um zur Schaltfläche Kegel zu gelangen, klicke auf den Abwärtspfeil neben dem sichtbaren Symbol und wähle Additiv Kegel im Menü.
2.  Stelle die Grundelement Parameter und [Anhang](Part_EditAttachment/de.md) ein.
3.  Klicke **OK**.
4.  Eine Kegelfunktion wird unter dem aktiven Körper angezeigt.


</div>

## Optionen

Der Kegel kann auf zwei verschiedene Wege bearbeitet werden:

-   Durch Doppelklick in der Baumstruktur oder durch Rechtsklick und Auswahl von **Grundkörper bearbeiten** im Kontextmenü. Dies öffnet den Dialog „Parameter des Grundkörpers" in dem Aufgabenpaneel.
-   Mittels der [Eigenschaften-Palette](Property_editor/de.md) im Reiter Daten.

## Eigenschaften

-    **Attachment**: Bestimmt den Befestigungsmodus und den Befestigungsversatz. Siehe [Part Anhang](Part_EditAttachment/de.md).

-    **Label**: Die vom Benutzer vergebene Bezeichung für das Kegel-Objekt. Dies kann nach Bedarf geändert werden.

-    **Radius1**: Der Wert des Radius an der Kegelbasis.

-    **Radius2**: Der Wert des Radius an der Kegeloberspitze. Ein von Null verschiedener Wert erzeugt einen stumpfen Kegel.

-    **Height**: Die Höhe des Kegels entlang seiner Achse.

-    **Angle**: Der Rotationswinkel des halben Querschnitts (360° ergeben einen vollen Kegel).


<div class="mw-translate-fuzzy">





</div>


{{PartDesign_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveCone/de
