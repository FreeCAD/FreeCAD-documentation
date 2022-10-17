---
- GuiCommand   */de
   Name   *Arch Profile
   Name/de   *Arch Profil
   MenuLocation   *Arch → Profil
   Workbenches   *[Arch](Arch_Workbench/de.md)
   Version   *0.19
---

# Arch Profile/de

## Beschreibung

Das Profil-Werkzeug erstellt ein parametrisches 2D-Profil-Objekt. Dieses Objekt kann dann als eine Basis in verschiedenen anderen Werkzeugen werden, die Extrusion durchführen, wie [Arch Rahmen](Arch_Frame/de.md), [Arch Vorhangfassade](Arch_CurtainWall/de.md) oder [Part Extrudieren](Part_Extrude/de.md).

Siehe die [Liste von verfügbaren Voreinstellungen](https   *//github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Arch/Presets/profiles.csv).

Das Profil-Werḱzeug ist auch im [Arch Struktur](Arch_Structure.md)-Werkzeug integriert, alle voreingestellten Profile sind auch dort verfügbar.

## Anwendung

1.  Drücke die **<img src="images/Arch_Profile.svg" width=16px> [Arch Profil](Arch_Profile/de.md)**-Schaltfläche
2.  Wähle eine Voreinstellung im Werkzeug-Aufgaben-Reiter
3.  Klicke einen Punkt in der [3D-Ansicht](3D_view/de.md), um das Profil zu platzieren

## Eigenschaften

### Daten

-    **Height**   * Die (Gesamt)-Höhe des Profils

-    **Width**   * Die (Gesamt)-Breite des Profils

-    **Diameter**   * Der Durchmesser des Profils (nur Rundprofile)

-    **Thickness**   * Die Wandstärke (nur runde/rechteckige Hohlprofile)

-    **Web Thickness**   * Die Dicke der Profilbahnen (nur H- und I-Profile)

-    **Flange Thickness**   * Die Dicke des Flanschprofil (nur H- und I-Profile)

## Hinzufügen von benutzerdefinierten Profilen 

Eine zusätzliche CSV-Datei kann durch den Benutzer erstellt werden, die benutzerdefinierte Definitionen enthält. Sie muss **profiles.csv** heißen und in {{Code|lang=bash|code=
$FREECAD_USER_DIR/Arch/
}}

Der Wert für `$FREECAD_USER_DIR` kann über die [Python-Konsole](Python_console/de.md) ermittelt werden   * {{Code|lang=bash|code=
FreeCAD.getUserAppDataDir()
}}

Der Inhalt deiner **profiles.csv**-Datei muss den gleichen Regeln wie die Datei [profiles.csv](https   *//github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Arch/Presets/profiles.csv) im Quell-Code entsprechen.

Die CSV-Datei muss eine Zeile für jedes verfügbare Profil enthalten, formatiert wie folgt   *


<div class="mw-translate-fuzzy">

-   Für C-Profile   * Kategorie, Name, Klasse, Durchmesser, Dicke
-   Für H- und U-Profile   * Kategorie, Name, Klasse, Breite, Höhe, Stegdicke (/-breite), Flanschdicke (/-stärke)
-   Für R-Profile   * Kategorie, Name, Klasse, Breite, Höhe
-   Für RH-Profile   * Kategorie, Name, Klasse, Breite, Höhe, Dicke


</div>

Alle Maße müssen in Millimetern angegeben werden. Mögliche Profilklassen sind   *


<div class="mw-translate-fuzzy">

-   C   * Kreisförmiges Rohr
-   H   * H- oder I-Profil
-   R   * Rechteckig
-   RH   * Rechteckig hohl
-   U   * U-Profil


</div>

Zusätzliche Profiltypen können erstellt werden, aber eine entsprechende Klasse muss zuerst definiert werden in [ArchProfile.py](https   *//github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Arch/ArchProfile.py).

## Skripten

Das Profil-Werkzeug kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit folgender Funktion verwendet werden   *


```python
profile = makeProfile(profile_list)
```

wobei {{Incode|profile_list}} die verschiedenen Elemente einer Liste in der CSV-Datei enthält.

Beispiel   *


```python
import Arch
Arch.makeProfile([0, 'REC', 'REC100x100', 'R', 100, 100])
```

wobei das erste Element der Liste eine Bestellnummer (order number) ist, die bisher nicht verwendet wird.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Profile/de
