# Help Module/de
## Beschreibung

Das Modul Hilfe ist verantwortlich für die Bearbeitung aller Anfragen zur Dokumentation und deren Darstellung in passender Weise. Bis zur FreeCAD-Version 0.21 stand das Modul Hilfe als [Addon](Std_AddonMgr/de.md) zur Verfügung, danach ist es in FreeCAD selbst enthalten. Es ist kein Problem, das Addon nach der Version 0.21 installiert zu lassen.

Das Modul Hilfe stellt eine Seite mit Voreinstellungen unter dem Menüeintrag **Bearbeiten → Einstellungen → Allgemein → Hilfe** zur Verfügung, die folgende Einstellungen ermöglicht:

-   Die Quelle der Dokumentation: Die Dokumentation kann online geholt werden, z.B. vom [official FreeCAD-Wiki](https://wiki.freecad.org) (Standardeinstellung) oder von der [Markdown-Umwandlung](https://github.com/FreeCAD/FreeCAD-documentation) oder offline von einem anderen Ort, wie z.B. einem Ordner, wo die Dokumentation mit dem [Addon-Manager](Std_AddonMgr.md) heruntergeladen werden kann.

-   Auf welche Weise die Dokumentation angezeigt wird: im Desktop-Browser, in einem separaten andockbaren Dialogfenster, das ermöglicht z.B. die Dokumentation angezeigt zu lassen, während man weiterarbeitet (Dies ist nützlich, wenn man nach Anleitung arbeitet) oder ein neuer FreeCAD-Reiter. Man beachte, das in der Version 1.0 die zweite und dritte Möglichkeit PySide-Web-Components erfordern. Wenn diese fehlen, wird stattdessen die erste Variante eigesetzt.

-   Eine alternative css-Datei: Dies wird nur dann eingesetzt, wenn die obigen Markdown- oder Offline-Quellen verwendet werden und ermöglicht, das Erscheinungsbild der Dokumentation anzupassen.



## Skripten

Das Modul Hilfe besteht grundsätzlich aus einem [einzigen Python-Modul](https://github.com/FreeCAD/FreeCAD/blob/main/src/Mod/Help/Help.py). Sein Haupteinsatz ist die Verwendung der Funktion {{Incode|show}}. Es kann eine URL empfangen, eine lokale Datei (Markdown oder html) oder findet eine Seite automatisch anhand der Einstellungen unter **Einstellungen → Allgemein → Hilfe**.

Es spielt keine Rolle, was man auswählt, das System erkennt, ob die Inhalte in HTML oder Markdown vorliegen und stellt sie entsprechend dar.

Grundlegende Anwendung:


```python
import Help
Help.show("Draft Line")
Help.show("Draft_Line")  # works with spaces or underscores
Help.show("https://wiki.freecadweb.org/Draft_Line")
Help.show("https://gitlab.com/freecad/FreeCAD-documentation/-/raw/main/wiki/Draft_Line.md")
Help.show("/home/myUser/.FreeCAD/Documentation/Draft_Line.md")
Help.show("http://myserver.com/myfolder/Draft_Line.html")
```



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External%20Workbenches.md) > [Help](Help_Workbench.md) > Help Module/de
