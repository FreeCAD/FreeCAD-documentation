---
- GuiCommand   */de
   Name   *Std AddonMgr
   Name/de   *Std ErweiterungVerw
   MenuLocation   *Werkzeuge → ErweiterungsVerwalter
   Workbenches   *Alle
   Version   *0.17
   SeeAlso   *[Externe Arbeitsbereiche](External_workbenches/de.md), [Makros](Macros/de.md)
---

# Std AddonMgr/de

## Beschreibung


<div class="mw-translate-fuzzy">

Der **Std ErweiterungVerw** Befehl öffnet den Erweiterungsverwalter. Mit dem Erweiterungsverwalter kannst du [externe Arbeitsbereiche](external_workbenches/de.md) und [Makros](macros/de.md), die von der FreeCAD Gemeinschaft bereitgestellt werden, installieren und verwalten. Die verfügbaren Arbeitsbereiche und Makros stammen aus zwei Repositorien, [FreeCAD-addons](https   *//github.com/FreeCAD/FreeCAD-addons/) und [FreeCAD-macros](https   *//github.com/FreeCAD/FreeCAD-macros/), sowie von der [Makrosrezepte](Macros_recipes/de.md) Seite.


</div>


<div class="mw-translate-fuzzy">

Aufgrund von Änderungen an der GitHub Plattform im Jahr 2020 funktioniert der Erweiterungsverwalter nicht mehr, wenn du FreeCAD Version 0.17 oder früher verwendest. Du musst auf die Version [0.18.5](https   *//github.com/FreeCAD/FreeCAD/releases/tag/0.18.5) oder eine neuere Version [0.19](https   *//github.com/FreeCAD/FreeCAD/releases/tag/0.19_pre) aktualisieren. Alternativ kannst du Erweiterungen auch manuell installieren, siehe [Hinweise](#Hinweise.md) unten.


</div>

## Anwendung


<div class="mw-translate-fuzzy">

1.  Wähle die **Werkzeuge → <img src="images/Std_AddonMgr.svg" width=16px> Erweiterungsverwalter** Option aus dem Menü.
2.  Wenn du den Erweiterungsverwalter zum ersten Mal verwendest, wird ein Dialogfeld geöffnet, das dich darauf hinweist, dass die Erweiterungen im Erweiterungsverwalter nicht offiziell Teil von FreeCAD sind. Drücke die **OK** Schaltfläche, um zu bestätigen und fortzufahren.
3.  Das Dialogfeld des Erweiterungsverwalters öffnet sich. Für weitere Informationen siehe [Optionen](#Options/de.md).
4.  Die **<img src="images/Button_valid.svg" width=16px> Alles aktualisieren** Schaltfläche funktioniert zur Zeit nicht.
5.  Drücke die **<img src="images/Process-stop.svg" width=16px> Schließen** Schaltfläche, um das Dialogfeld zu schließen.
6.  Wenn du einen Arbeitsbereich installiert oder aktualisiert hast, wird ein neues Dialogfeld geöffnet, das dich darauf hinweist, dass du FreeCAD neu starten musst, damit die Änderungen wirksam werden.


</div>

## Optionen

<img alt="" src=images/AddonManager_Main.png  style="width   *600px;">

1.  The Addon manager provides two view layouts   * \"Condensed\" and \"Expanded\". In \"Condensed\" view, each addon takes a single line, and its description is truncated to fit the available space. \"Expanded\" shows additional details, including more of the description text as well as maintainer information, more installation details, etc.
2.  Three different types of addons are supported   * [workbenches](external_workbenches.md), [macros](macros.md), and [preference packs](Preference_Packs.md). You can choose to show just one type, or all of them in a single list.
3.  The list can be limited to show just installed packages, just packages with available updates, or just packages that are not yet installed.
4.  The list can be filtered, searching for a keyword in the title, description, and tags (description and tags must be specified by the addon developer in their addon\'s metadata). The filter can even be a regular expression, for fine-grained control of the exact search term.
5.  The expanded view shows available version information, description, maintainer information, and installation version information, for packages that provide a [package metadata](Package_Metadata.md) file (or for macros with embedded metadata).
6.  Addon data is cached locally, with a variable cache update frequency set in the user preferences.
7.  At any time you can choose to manually update your local cache to see the latest updates available for each addon.
8.  Update checks may be set up to be automatic, or done manually via a button click (configured in user preferences). If GitPython and git are installed on your system then update information is fetched using git. If not, then update information is obtained from any present metadata file.

Clicking on an addon in this view brings up the addon\'s Details page   *

<img alt="" src=images/AddonManager_Details.png  style="width   *600px;">

The details page shows buttons allowing installing, uninstalling, updating, and temporarily disabling an addon. For installed addons it lists the currently installed version and the installation date, and whether that is the most recent version available. Below is an embedded web browser window showing the addon\'s README page (for workbenches and preference packs), or Wiki page (for macros).

## Preferences

The preferences for the Addon manager can be found in the [Preferences Editor](Preferences_Editor#Addon_Manager.md). <small>(v0.20)</small> 

## Hinweise


<div class="mw-translate-fuzzy">

-   Die Verwendung von Erweiterungen ist nicht auf die FreeCAD Version beschränkt, aus der sie installiert wurden. Du kannst sie auch in jeder anderen FreeCAD Version verwenden, die von der Erweiterung unterstützt wird und die du möglicherweise auf deinem System hast.
-   Die im Erweiterungsverwalter verfügbaren Erweiterungen sind nicht Teil des offiziellen FreeCAD Programms und werden vom FreeCAD Kernentwicklungsteam nicht unterstützt. Du solltest die bereitgestellten Informationen sorgfältig lesen, um sicherzustellen, daß du weißt, was du installierst.
-   Fehlerberichte und Funktionenanfragen sollten direkt an den Ersteller der Erweiterung gerichtet werden, durch Besuch der angegebene Webseite. Viele Erweiterungsentwickler sind regelmäßige Nutzer des [FreeCAD Forums](https   *//forum.freecadweb.org), und können dort auch kontaktiert werden.
-   Wenn das [GitPython](https   *//github.com/gitpython-developers/GitPython) Paket auf deinem Computer installiert ist, wird der Erweiterungsverwalter davon Gebrauch machen, was das Herunterladen beschleunigt.
-   Du kannst Erweiterungen auch manuell installieren. Siehe [Wie man zusätzliche Arbeitsbereiche installiert](How_to_install_additional_workbenches/de.md) und [Wie man Makros installiert](How_to_install_macros/de.md).


</div>

## Informationen für Entwickler 

See [Addon](Addon#Information_for_developers.md).





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std AddonMgr/de
