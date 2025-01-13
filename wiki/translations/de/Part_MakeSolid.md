---
 GuiCommand:
   Name: Part MakeSolid
   Name/de: Part UmwandelnFestkörper
   MenuLocation: Part , In Festkörper umwandeln
   Workbenches: Part_Workbench/de
   SeeAlso: Part_ShapeFromMesh/de
---

# Part MakeSolid/de



## Beschreibung

Der Befehl <img alt="" src=images/Part_MakeSolid.svg  style="width:24px;"> **Part FestkörperErstellen** erstellt Festkörper aus Formobjekten.

This command is typically used as one of the steps to create a solid from a mesh. See [Part ShapeFromMesh](Part_ShapeFromMesh#Usage.md) for more information.



## Anwendung

1.  Ein oder mehrere Formobjekte auswählen.
2.  Den Menüeintrag **Part → <img src="images/Part_MakeSolid.svg" width=16px> In Festkörper umwandeln** auswählen.
3.  Für jedes ausgewählte Objekt wird ein separates neues Objekt erstellt.



## Hinweise

-   Die ausgewählten Formobjekte werden nicht analysiert oder validiert.
-   Es wird empfohlen, vor dem Umwandeln in einen Festkörper [Part FormAufbereiten](Part_RefineShape/de.md) einzusetzen.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

The created objects are [Part Feature](Part_Feature.md) objects with no additional properties.





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part MakeSolid/de
