---
- GuiCommand:
   Name: Path ToolLibraryEdit
   MenuLocation: Path -> Tool Manager
   Workbenches: Path_Workbench
   Shortcut: **P** **T**
   SeeAlso: 
---

# Path ToolLibraryEdit/de



## Beschreibung

Der **<img src="images/Path_ToolLibraryEdit.svg" width=16px> [Werkzeug Manager/Editor](Path_ToolLibraryEdit/de.md)** erlaubt es, die verschiedenen Werkzeuge der im Maschinenobjekt eines **<img src="images/Path_Job.svg" width=16px> [Pfad Auftrag](Path_Job/de.md)** zu bearbeiten. Diese Werkzeugtabelle wird von den verschiedenen im Projekt enthaltenen Arbeitsgängen verwendet, um notwendige Informationen über das aktuelle Werkzeug zu erhalten.

It serves for the selection of a tool which you want to use in your job as well.

![](images/Path-Tooltable.png )

The handling is straight forward:

-   Import\...: Imports a tooltable from an XML-file. {{Note|Warning|This is currently partly broken and does not work if you have never had an xml file before.}}
-   Export\...: Exports the tooltable to an XML-file.
-   New Tool: opens a dialog where you can enter the parameters of your tool.
-   Delete: deletes the currently selected lines.{{Note|Warning|The tools are deleted from your tooltable even if you cancel the dialog}}
-   Move up: You cannot edit the tool number, instead you can move the selected line up to decrease it\'s tool number
-   Move down: You can move the selected line down to increase it\'s tool number

-   Create Tool Controller(s): If you check one or more of the checkboxes to the left in the tools list, this button becomes active. If you click it, the selected tools will be inserted in your current job.

## Usage

1.  Select a **<img src="images/Path_Job.svg" width=16px> [Path Job](Path_Job.md)
**
2.  Invoke the Tool Manager using several methods:
    -   Press the **<img src="images/Path_ToolLibraryEdit.svg" width=16px> [Tool Manager](Path_ToolLibraryEdit.md)** button in the toolbar.
    -   Using the **P** then **T** keyboard shortcut.
    -   Using the **Path → Tool Manager** entry from the top menu.
3.  Create new tools or adjust the properties of existing tools.
    Set at least the diameter, FreeCAD needs it to calculate the radius compensation. As of <small>(v0.17)</small>  this is the only value used for path creation. However, if you wish to use the simulation tool later, add cutting edge angle and cutting edge height as well.
    ![](images/Path-ToolAdd.gif )

## Options

-   The tools can be reordered by using the move up/move down buttons
-   Complete tooltables can be imported from XML files (FreeCAD\'s own tooltable format) or from HeeksCAD tooltables





{{Path_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Path](Path_Workbench.md) > Path ToolLibraryEdit/de
