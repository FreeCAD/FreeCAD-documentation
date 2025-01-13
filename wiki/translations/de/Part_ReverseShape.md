---
 GuiCommand:
   Name: Part ReverseShape
   Name/de: Part FormUmkehren
   MenuLocation: Part , Formen umkehren
   Workbenches: Part_Workbench/de
---

# Part ReverseShape/de



## Beschreibung

Der Befehl <img alt="" src=images/Part_ReverseShape.svg  style="width:24px;"> **Part FormUmkehren** erstellt aus ausgewählten Objekten parametrische Kopien mit umgekehrten Flächennormalen.



## Anwendung

1.  Eine oder mehrere Formen auswählen.
2.  Den Menüeintrag **Part → <img src="images/Part_ReverseShape.svg" width=16px> Formen umkehren** auswählen.
3.  Zu jedem ausgewählten Objekt wird eine umgekehrte Form erstellt.



## Hinweise

-   [App Link](App_Link.md)-Objekte, die mit dem passenden Objekttyp verbunden sind und [App Part](App_Part.md)-Behälter mit den passenden, sichtbaren Objekten darin, können ebenfalls als Quellobjekte verwendet werden. {{Version/de|0.20}}
-   Die Auswirkung der Anweisung kann man sehen, wenn die **Lighting**eigenschaft der umgekehrten Form nach {{Value|On side}} und gegebenenfalls **Bearbeiten → Einstellungen... → Anzeige → 3D-Viewer → Rendern → Farbe der Hintergrundbeleuchtung** geändert wird.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein Part ReverseShape-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem besitzt es die folgende zusätzliche Eigenschaft:



### Daten


{{TitleProperty|Reverse}}

-    **Source|Link**: Gibt die verknüpfte Ausgangsform an.





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part ReverseShape/de
