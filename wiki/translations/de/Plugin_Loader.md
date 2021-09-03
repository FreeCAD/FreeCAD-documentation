---
- GuiCommand:/de
   Name:Std AddonMgr
   Name/de:Std ErweiterungVerw
   MenuLocation:Werkzeuge → ErweiterungsVerwalter
   Workbenches:Alle
   Version:0.17
   SeeAlso:[Externe Arbeitsbereiche](External_workbenches/de.md), [Makros](Macros/de.md)
---

## Beschreibung

Der **Std ErweiterungVerw** Befehl öffnet den Erweiterungsverwalter. Mit dem Erweiterungsverwalter kannst du [externe Arbeitsbereiche](external_workbenches/de.md) und [Makros](macros/de.md), die von der FreeCAD Gemeinschaft bereitgestellt werden, installieren und verwalten. Die verfügbaren Arbeitsbereiche und Makros stammen aus zwei Repositorien, [FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons/) und [FreeCAD-macros](https://github.com/FreeCAD/FreeCAD-macros/), sowie von der [Makrosrezepte](Macros_recipes/de.md) Seite.

Erweiterungen, die als {{emphasis|Nur Python 2}} markiert sind, funktionieren nicht in FreeCAD Version 0.19 oder höher.

Aufgrund von Änderungen an der GitHub Plattform im Jahr 2020 funktioniert der Erweiterungsverwalter nicht mehr, wenn du FreeCAD Version 0.17 oder früher verwendest. Du musst auf die Version [0.18.5](https://github.com/FreeCAD/FreeCAD/releases/tag/0.18.5) oder eine neuere Version [0.19](https://github.com/FreeCAD/FreeCAD/releases/tag/0.19_pre) aktualisieren. Alternativ kannst du Erweiterungen auch manuell installieren, siehe [Hinweise](#Hinweise.md) unten.

![](images/Std_AddonMgr_dialog.png ) *Das Dialogfeld des Erweiterungsverwalters*

## Anwendung

1.  Wähle die **Werkzeuge → <img src="images/Std_AddonMgr.svg" width=16px> Erweiterungsverwalter** Option aus dem Menü.
2.  Wenn du den Erweiterungsverwalter zum ersten Mal verwendest, wird ein Dialogfeld geöffnet, das dich darauf hinweist, dass die Erweiterungen im Erweiterungsverwalter nicht offiziell Teil von FreeCAD sind. Drücke die **OK** Schaltfläche, um zu bestätigen und fortzufahren.
3.  Das Dialogfeld des Erweiterungsverwalters öffnet sich. Für weitere Informationen siehe [Optionen](#Options/de.md).
4.  Die **<img src="images/Button_valid.svg" width=16px> Alles aktualisieren** Schaltfläche funktioniert zur Zeit nicht.
5.  Drücke die **<img src="images/Process-stop.svg" width=16px> Schließen** Schaltfläche, um das Dialogfeld zu schließen.
6.  Wenn du einen Arbeitsbereich installiert oder aktualisiert hast, wird ein neues Dialogfeld geöffnet, das dich darauf hinweist, dass du FreeCAD neu starten musst, damit die Änderungen wirksam werden.

## Optionen

Das Dialogfeld des Erweiterungsverwalters hat zwei Reiter auf der linken Seite, eine mit den verfügbaren Arbeitsbereichen und die andere mit den verfügbaren Makros. Das Informationsfeld auf der rechten Seite zeigt die Startseite der ausgewählten Erweiterung an.

### Deinstallieren

1.  Wähle eine installiertes Erweiterung auf der Seite <img alt="" src=images/Folder.svg  style="width:16px;"> Reiter **Arbeitsbereiche** oder den <img alt="" src=images/Applications-python.svg  style="width:16px;"> **Makros** Reiter.
2.  Drücke die **<img src="images/Delete.svg" width=16px> Ausgewähltes deinstallieren** Schaltfläche.

### Installieren/Aktualisieren

1.  Wähle eine Erweiterung auf dem <img alt="" src=images/Folder.svg  style="width:16px;"> **Arbeitsbereiche** Reiter oder dem <img alt="" src=images/Applications-python.svg  style="width:16px;"> **Makros** Reiter.
2.  Drücke die **<img src="images/Edit_OK.svg" width=16px>  Installieren/Aktualisieren ausgewählt** Schaltfläche .
3.  Wenn du ein Makro zu einer benutzerdefinierten Werkzeugleiste hinzufügen möchtest, vergiss nicht, die Symbol Bilddatei, falls verfügbar, manuell herunterzuladen, indem du auf den Verweis auf der Homepage im Informationsfenster klickst. Siehe [Schnittstellenanpassung](Interface_Customization/de#Werkzeugleisten.md).
4.  Um die Position eines Erweiterungsarbeitsbereichs in der Liste [Arbeistbereichswähler](Std_Workbench/de.md) zu ändern, siehe [Oberflächenanpassung](Interface_Customization/de#Arbeitsbereiche.md).

### Konfiguration

1.  Drücke die **<img src="images/Preferences-general.svg" width=16px> Konfigurieren... ** Schaltfläche.
2.  Das Dialogfeld Erweiterungsverwalteroptionen wird geöffnet.
3.  Prüfe wahlweise die {{CheckBox|TRUE|Automatisch beim Start nach Updates suchen (erfordert GitPython)}} Kontrollkästchen.
4.  Wahlweise Repositorien zur Liste **Benutzerdefinierte Repositorien** hinzufügen. Erweiterungen von diesen Repositorien werden auf dem <img alt="" src=images/Folder.svg  style="width:16px;"> **Arbeitsbereiche** Reiter oder die <img alt="" src=images/Applications-python.svg  style="width:16px;"> **Makros** Reiter hinzugefügt.
5.  Wähle optional Proxy Einstellungen.
6.  Drücke die **OK** Schaltfläche oder die **Abbrechen** Schaltfläche, um das Dialogfeld zu schließen.

## Hinweise

-   Die Verwendung von Erweiterungen ist nicht auf die FreeCAD Version beschränkt, aus der sie installiert wurden. Du kannst sie auch in jeder anderen FreeCAD Version verwenden, die von der Erweiterung unterstützt wird und die du möglicherweise auf deinem System hast.
-   Die im Erweiterungsverwalter verfügbaren Erweiterungen sind nicht Teil des offiziellen FreeCAD Programms und werden vom FreeCAD Kernentwicklungsteam nicht unterstützt. Du solltest die bereitgestellten Informationen sorgfältig lesen, um sicherzustellen, daß du weißt, was du installierst.
-   Fehlerberichte und Funktionenanfragen sollten direkt an den Ersteller der Erweiterung gerichtet werden, durch Besuch der angegebene Webseite. Viele Erweiterungsentwickler sind regelmäßige Nutzer des [FreeCAD Forums](https://forum.freecadweb.org), und können dort auch kontaktiert werden.
-   Wenn das [GitPython](https://github.com/gitpython-developers/GitPython) Paket auf deinem Computer installiert ist, wird der Erweiterungsverwalter davon Gebrauch machen, was das Herunterladen beschleunigt.
-   Du kannst Erweiterungen auch manuell installieren. Siehe [Wie man zusätzliche Arbeitsbereiche installiert](How_to_install_additional_workbenches/de.md) und [Wie man Makros installiert](How_to_install_macros/de.md).

## Informationen für Entwickler 

Wenn du einen Arbeitsbereich oder ein Makro entwickelt hast und es im Erweiterungsverwalter sehen möchtest, lies auf den Repositoriumsseiten ([FreeCAD-Erweiterungen](https://github.com/FreeCAD/FreeCAD-addons/) und [FreeCAD-Makros](https://github.com/FreeCAD/FreeCAD-macros/)), was zu tun ist. Wenn du dein Makro zu den [Makro Rezepte](Macros_recipes/de.md) Seiten hinzufügst, ist nichts weiteres tun, denn es wird automatisch vom Erweiterungsverwalter ausgewählt.

### Python Arbeitsbereiche 

Für Python Arbeitsbereiche benötigst du keine besondere Genehmigung, damit dein Arbeitsbereich zum Erweiterungsverwalter hinzugefügt wird, und da sie außerhalb des FreeCAD Quellcodes liegen, kannst du die gewünschte Lizenz wählen. Wenn du darum anfragst, dass dein Arbeitsbereich in die Liste aufgenommen wird (wir werden keine neuen Arbeitsnbereich ohne eine Anfrage der Autoren hinzufügen), entweder durch eine entsprechende Anfrage im Forum oder durch das Öffnen einer Ausgabe im [FreeCAD-Erweiterungs](https://github.com/FreeCAD/FreeCAD-addons/) Repositorium, bleibt dein Code in deinem eigenen git Repositorium, wir fügen ihn einfach als Untermodul zum [FreeCAD-Erweiterungs](https://github.com/FreeCAD/FreeCAD-addons/) Repositorium hinzu. Natürlich werden wir, bevor wir deinen Arbeitsbereich hinzufügen, einen Blick darauf werfen und sicherstellen, dass es keine potentiellen Probleme damit gibt.

### C++ Arbeitsbereiche 

Wenn du einen Arbeitsbereich in C++ entwickelst, kann er nicht direkt durch Benutzer ausgeführt, sondern muss zuerst kompiliert werden. Du hast zwei Optionen, entweder stellst du vorkompilierte Versionen deines Arbeitsbereichs für die verschiedenen Betriebssysteme zur Verfügung oder du solltest anfragen, dass dein Code in den FreeCAD Quellcode integriert wird. Dafür solltest du die LGPL Lizenz (oder vollkompatible wie MIT oder BSD) verwenden, und du musst deine neuen Werkzeuge der Gemeinschaft im [FreeCAD Forum](https://forum.freecadweb.org) zur Überprüfung vorstellen. Sobald dein Code getestet und genehmigt wurde, solltest du, falls noch nicht geschehen, einen Fork für das FreeCAD Repositorium durchführen, einen neuen Zweig erstellen, deinen Code dorthin schieben und eine Pull Anfrage öffnen, so dass dein Zweig mit dem Haupt Repositorium zusammengeführt wird.





{{Std Base navi

}}  
