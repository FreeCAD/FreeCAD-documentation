---
- GuiCommand:
   Name:PartDesign Migrate
   Name/de:PartDesign Migrieren
   MenuLocation:Part Design → Migrieren
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   Version:0.17
---

# PartDesign Migrate/de

## Beschreibung

Der PartDesign Arbeitsbereich in FreeCAD v0.17 enthält neue Werkzeuge und Elemente, die von älteren FreeCAD-Versionen (0.16 und älter) nicht erkannt werden. FreeCAD Dokumente, die in älteren Versionen erstellt wurden, können weiterhin geöffnet und bearbeitet werden. Um von den neuen Funktionen zu profitieren, müssen sie über das Menü PartDesign → Migrieren migriert werden.


{{Version/de|0.17}}

## Anwendung

1.  Öffne ein älteres FreeCAD Dokument {{VersionMinus/de|0.16}}
2.  Wechsle zum **<img src="images/Workbench_PartDesign.svg" width=16px> [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md)**.
3.  Gehe zum **PartDesign** → **Migrieren** Menü.
4.  Wenn die Migration funktioniert, wird eine <img alt="" src=images/Std_Part.svg  style="width:24px;"> [Part Behälter](Std_Part/de.md) erstellt, welche eine oder mehrere ![ 24px](images/_PartDesign_Body.png ) [Körper](PartDesign_Body/de.md) enthält, die jeweils eine Reihe von Formelementen enthalten.

## Begrenzungen

-   Überprüfe vor dem Start des Migrationsprozesses, ob das Modell mit aktivierten automatischen Verfeinerungsoptionen erstellt wurde (unter **Bearbeiten → Voreinstellungen → Part Design → Allgemein**) und lege deine Einstellungen entsprechend fest. Dies kann leicht bestimmt werden, indem nacheinander die Sichtbarkeit der Merkmale in der Modellstruktur umgeschaltet wird. Wenn keine verbleibenden Kanten zwischen Formelementen wie Polster und Taschen verbleiben, wurden die automatischen Verfeinerungsoptionen deaktiviert.
-   Wenn ein zu migrierendes Dokument nur Skizzen und PartDesign Formelemente enthält, ist der Migrationsprozess wahrscheinlich erfolgreich. Einige Funktionen wie Fasen und Verrundungen müssen möglicherweise neu erstellt werden.
-   Wenn das zu migrierende Dokument einen gemischten Teil- / Teileentwurf / Entwurf Arbeitsablauf aufweist, wird die Konvertierung wahrscheinlich fehlschlagen oder bestenfalls zu unerwarteten Ergebnissen führen und muss manuell migriert werden.





{{PartDesign Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Migrate/de
