# Assembly Preferences/de
Die Einstellungen für den Arbeitsbereich <img alt="" src=images/Workbench_Assembly.svg  style="width:24px;"> [Assembly](Assembly_Workbench.md) befinden sich im [Voreinstellungseditor](Preferences_Editor/de.md). Den Menüeintrag **Bearbeiten → Einstellungen...** auswählen und dann **<img src="images/Workbench_Assembly.svg" width=16px> Assembly**. Diese Gruppe steht nur dann zur Verfügung, wenn der Arbeitsbereich Assembly in der aktuellen FreeCAD-Sitzung geladen wurde.

Es gibt nur eine Seite: Allgemein.

![](images/Preferences_Assembly_Page_General.png )

Auf dieser Seite kann Folgendes festgelegt werden:


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| Name                                 | Description                                                                                                                                                                                                                                                                                                                |
+======================================+============================================================================================================================================================================================================================================================================================================================+
|                       | If checked, pressing the **Esc** key leaves Assembly edit mode.                                                                                                                                                                                                                                          |
| **Esc leaves edit mode** |                                                                                                                                                                                                                                                                                                                            |
|                                   |                                                                                                                                                                                                                                                                                                                            |
+++
|                       | If checked, the dragging steps of the solver are logged. Useful if you want to report a bug. The files are named **runPreDrag.asmt** and **dragging.log** and are located in the default directory of {{Incode|std::ofstream}} (on Windows it\'s the desktop). |
| **Log dragging steps**   |                                                                                                                                                                                                                                                                                                                            |
|                                   |                                                                                                                                                                                                                                                                                                                            |
+++
|                       | When you [insert](Assembly_InsertLink.md) the first part in the assembly, you can choose to ground the part automatically. The options are:                                                                                                                                                                        |
| **Ground first part**    |                                                                                                                                                                                                                                                                                                                            |
|                                   | -   *Ask*                                                                                                                                                                                                                                                                                                                  |
|                                      | -   *Always*                                                                                                                                                                                                                                                                                                               |
|                                      | -   *Never*                                                                                                                                                                                                                                                                                                                |
+++


</div>





{{Assembly_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Preferences](Category_Preferences.md) > [Assembly](Assembly_Workbench.md) > Assembly Preferences/de
