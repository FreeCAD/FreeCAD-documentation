---
- GuiCommand:
   Name: Std LinkImport
   Name/de: Std VerknüpfungImportieren
   MenuLocation: None
   Workbenches: All
   Version: 0.19
   SeeAlso: [Std VerknüpfungErstellen](Std_LinkMake/de.md), [Std UnterverknüpfungErstellen](Std_LinkMakeRelative/de.md), [Std AlleVerknüpfungenImportieren](Std_LinkImportAll/de.md)
---

# Std LinkImport/de



## Beschreibung

Mit der Schaltfläche **[<img src=images/Std_LinkImport.svg style="width:16px"> [Std VerknüpfungImportieren](Std_LinkImport/de.md)** wird ein **Linked Object** aus einer Verknüpfung in das aktuelle Dokument importiert und der Anhang zu diesem Objekt geändert.

Das hilft beim Arbeiten mit Baugruppen ([Zusammenbau](assembly/de.md)) um Modelle aus anderen Dokumenten wieder zu verwenden.


**[<img src=images/Std_LinkImportAll.svg style="width:16px"> [Std AlleVerknüpfungenImportieren](Std_LinkImportAll/de.md)**

wird verwendet, um alle verknüpften Objekte zu importieren.



## Anwendung

1.  Make sure you have a \"source\" document with an original object, say, a **[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part.md)**, and a second \"target\" document with a Link to that object.
2.  Open the target document and select the Link to the object; its **Linked Object** should show something like {{Value|source#Part}}.
3.  Press **[<img src=images/Std_LinkImport.svg style="width:16px"> [Import link](Std_LinkImport.md)**.

A copy of the original **[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part.md)** must now be inside the current \"target\" document. The **Linked Object** property of the Link must now show {{Value|Part}}, indicating that the Link no longer points to {{Value|Part}} in \"source\", but to {{Value|Part}} in the current document (\"target\").

![](images/Std_Link_tree_import_1_example.png ) ![](images/Std_Link_tree_import_2_example.png )



*Left: a Link points to the object in the "source" document. Right: the original object was imported (copied) into the "target" document, and the existing Link was changed to point to this copy, so it no longer points to the object in "source".*





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std LinkImport/de
