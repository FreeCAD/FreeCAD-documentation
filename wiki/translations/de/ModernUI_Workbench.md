# ModernUI Workbench/de
}

<img alt="Modern UI workbench icon" src=images/ModernUI_workbench_icon.svg  style="width:128px;">


{{TOCright}}

## Einführung

The [ModernUI Workbench](ModernUI_Workbench.md) is an [external workbench](External_workbenches.md) that replaces the standard user interface. It has modern features such as:

-   Each workbench has its ribbon tab.
-   **Modern UI** ribbon tab replaces the top-level menu.
-   Activating a workbench\'s ribbon tab shows groups of the workbench\'s tools.
-   Panels such as **Combo View** are collapsed/expanded upon mouse-over.

## Referenzen

-   Author: Hakan Seven
-   Source code on github: <https://github.com/HakanSeven12/Modern-UI>

## Begrenzungen und Problembehebung 

-   If you experience unexpected behavior, always first try to uninstall and then reinstall the ModernUI workbench.
-   The workbench is primarily tested with English and may exhibit unexpected behavior in other languages.
-   Installing more workbenches after installing ModernUI may cause problems.

## Installieren

Install with the <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Addon Manager](Addon_Manager.md).

Note: To uninstall, you have to create a macro and execute it. If you do not feel confident about this, consider to not install.

### Running Modern UI in a self-contained directory 

To easily test Modern UI without interfering with your standard configuration, you can contain it in a separate directory. Uninstalling Modern UI is then simply accomplished by deleting the directory. <small>(v0.19)</small> 

#### Linux

Zum Beispiel:

    $ mkdir modernUI  # new directory that contains Modern UI
    $ cd modernUI
    $ HOME="$PWD" FREECAD_USER_HOME="$PWD" FreeCAD_0.19.AppImage

When starting FreeCAD like this for the first time, you have a new default configuration. Now install (and configure) Modern UI. This is essentially a [*portable* FreeCAD version](Download#Notes_for_GNU.2FLinux_users.md).

Instead of using the command line, you can also [create a dedicated desktop icon](Start_up_and_Configuration#Starting_FreeCAD_from_the_desktop.md).

#### Windows

There are not dedicated instructions for Windows yet, however, it is very similar to [creating a portable version of FreeCAD on a USB medium](Start_up_and_Configuration#Starting_FreeCAD_from_a_portable_USB_medium.md).

## Uninstall

Detailed instructions can be found on [GitHub](https://github.com/HakanSeven12/Modern-UI#uninstallation).

The uninstall sequence is as follows:

1.  Uninstall with the <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Addon Manager](Addon_Manager.md).
2.  Restart FreeCAD.
3.  Create a macro with this code:```python
    from PySide2 import QtCore, QtGui, QtWidgets
    mw = FreeCADGui.getMainWindow()
    mw.menuBar().show()
     
    WBList = FreeCADGui.listWorkbenches()
    for WB in WBList:
        FreeCADGui.activateWorkbench(WB)
        for tb in mw.findChildren(QtWidgets.QToolBar):
            tb.show()
    
```
4.  Führe das Makro aus.
5.  FreeCAD neu starten.

## Verweise

-   FreeCAD Forum: <https://forum.freecadweb.org/viewtopic.php?f=34&t=44937>
-   Report bugs: <https://github.com/HakanSeven12/Modern-UI>
-   Patreon (to support the author): <https://www.patreon.com/HakanSeven12>




[Category:External\_Workbenches](Category:External_Workbenches.md) [Category:Addons](Category:Addons.md)

---
[documentation index](../README.md) > ModernUI Workbench/de
