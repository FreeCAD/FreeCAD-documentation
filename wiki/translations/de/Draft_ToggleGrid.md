---
- GuiCommand:/de
   Name:Draft ToggleGrid
   Name/de:Entwurf UmschaltenGitter
   MenuLocation:Entwurf → Dienstprogramme → Umschalten Gitter
   Workbenches:[Entwurf](Draft_Workbench/de.md), [Arch](Arch_Workbench/de.md)
   Shortcut:**G** **R**
   SeeAlso:[Entwurf Fang](Draft_Snap/de.md)
---

# Draft ToggleGrid/de


</div>

## Beschreibung


<div class="mw-translate-fuzzy">

Dieses Werkzeug erlaubt dir das Gitter, definiert in den [Entwurf Einstellungen](Draft_Preferences/de.md) oder mit dem [Entwurf WähleEbene](Draft_SelectPlane/de.md) Werkzeug anzuzeigen und auszublenden .


</div>

In FreeCAD version 0.19 the grid is always displayed when a command becomes active and toggling the grid while a command is active does not work.

## Anwendung

For general information about snapping see [Draft Snap](Draft_Snap.md).


<div class="mw-translate-fuzzy">

1.  Definiere das Aussehen des Gitters in den [Entwurfseinstellungen](Draft_Preferences/de.md); gehe zum Menü **Bearbeiten → Einstellungen → Entwurf → Gitter und Fang**; lege die \"Gittergröße\", \"Gitterabstand\" und \"Hauptlinie alle\" Optionen fest und drücke dann **OK**.
2.  Rechtsklicke dann auf ein Entwurfsobjekt und wähle **Dientsprogramme → <img src="images/Draft_Grid.svg" width=16px> UmschaltenGitter**.




1.  Oder rechtsklicke auf eine leere Stelle in einer Werkzeugleiste, oder gehe zum Menü **Ansicht → Werkzeugleisten**, und klicke auf das [Entwurf Fang](Draft_Snap/de.md) Auswahlkästchen.
2.  Es gibt mehrere Möglichkeiten, das Gitter sichtbar zu machen:
    -   Drücke die **<img src="images/Draft_Grid.svg" width=16px> [Entwurf UmschaltenGitter](Draft_ToggleGrid/de.md)** Schaltfläche in der Entwurf Werkzeugleiste
    -   Verwende **G** dann **R** Tastaturkürzel


</div>

## Preferences

See [Draft Snap](Draft_Snap#Preferences.md).

-   To use the grid select: **Edit → Preferences... → Draft → Grid and snapping → Grid → Use grid**. After changing this preference you must restart FreeCAD.
-   Several other grid preferences are also available: **Edit → Preferences... → Draft → Grid and snapping → Grid**.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft ToggleGrid/de
