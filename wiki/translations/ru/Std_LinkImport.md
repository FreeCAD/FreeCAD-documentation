---
- GuiCommand:
   Name:Std LinkImport
   MenuLocation:None
   Workbenches:All
   Version:0.19
   SeeAlso:[Std LinkMake](Std_LinkMake.md), [Std LinkMakeRelative](Std_LinkMakeRelative.md), [Std LinkImportAll](Std_LinkImportAll.md)
---

# Std LinkImport/ru

## Описание


**[<img src=images/Std_LinkImport.svg style="width:16px"> [Std LinkImport](Std_LinkImport.md)**

imports the **Linked Object** from a Link into the current document, and then changes the attachment to this object.

This operation is helpful when working with [assemblies](assembly.md) in order to organize re-usable models that may be located in other documents.

Use **[<img src=images/Std_LinkImportAll.svg style="width:16px"> [Std LinkImportAll](Std_LinkImportAll.md)** to import all linked objects.

## Применение

1.  Make sure you have a \"source\" document with an original object, say, a **[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part.md)**, and a second \"target\" document with a Link to that object.
2.  Open the target document and select the Link to the object; its **Linked Object** should show something like {{Value|source#Part}}.
3.  Press **[<img src=images/Std_LinkImport.svg style="width:16px"> [Std LinkImport](Std_LinkImport.md)**.

A copy of the original **[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part.md)** must now be inside the current \"target\" document. The **Linked Object** property of the Link must now show {{Value|Part}}, indicating that the Link no longer points to {{Value|Part}} in \"source\", but to {{Value|Part}} in the current document (\"target\").

![](images/Std_Link_tree_import_1_example.png ) ![](images/Std_Link_tree_import_2_example.png )



*Left: a Link points to the object in the "source" document. Right: the original object was imported (copied) into the "target" document, and the existing Link was changed to point to this copy, so it no longer points to the object in "source".*





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std LinkImport/ru
