---
 GuiCommand:
   Name: Arch Profile
   Name/de: Arch Profil
   MenuLocation: 3D/BIM , Generic 3D tools , Profil
   Workbenches: BIM_Workbench/de
   Version: 0.19
---

# Arch Profile/de



## Beschreibung

Das Werkzeug **ArchProfil** erstellt ein parametrisches 2D-Profil-Objekt. Dieses Objekt kann dann als Basis für verschiedene andere Werkzeuge verwendet werden, die Extrusionen durchführen, wie [Arch Rahmen](Arch_Frame/de.md), [Arch_Vorhangfassade](Arch_CurtainWall/de.md) oder [Part Extrudieren](Part_Extrude/de.md).

Siehe die [Liste von verfügbaren Voreinstellungen](https://github.com/FreeCAD/FreeCAD/blob/main/src/Mod/BIM/Presets/profiles.csv).

Das Werḱzeug Profil ist auch im Werkzeug [Arch Struktur](Arch_Structure.md) integriert; alle voreingestellten Profile sind auch dort verfügbar.



## Anwendung

1.  Die Schaltfläche **<img src="images/Arch_Profile.svg" width=16px> [Profil](Arch_Profile/de.md)** drücken.
2.  Eine Voreinstellung im Aufgaben-Bereich des Werkzeugs auswählen.
3.  Einen Punkt in der [3D-Ansicht](3D_view/de.md) auswählen, um das Profil zu positionieren.



## Eigenschaften



### Daten

-    {{PropertyData/de|Height}}: Die (Gesamt)-Höhe des Profils

-    {{PropertyData/de|Width}}: Die (Gesamt)-Breite des Profils

-    {{PropertyData/de|Diameter}}: Der Durchmesser des Profils (nur Rundprofile)

-    {{PropertyData/de|Thickness}}: Die Wandstärke des Rohrprofils (nur runde und rechteckige Hohlprofile)

-    {{PropertyData/de|Web Thickness}}: (Stregbreite) Die Wandstärke des Profilsteges (nur H- und I-Profile)

-    {{PropertyData/de|Flange Thickness}}: (Flanschstärke) Die Wandstärke der Profilflansche (nur H- und I-Profile)



## Benutzerdefinierte Profile hinzufügen 

Eine zusätzliche CSV-Datei kann durch den Benutzer erstellt werden, die selbsterstellte Profile (Umrisse) enthält. Sie muss **profiles.csv** heißen und hier gespeichert sein:


{{Code|lang=bash|code=
$FREECAD_USER_DIR/BIM/
}}

Der Wert für `$FREECAD_USER_DIR` kann über die [Python-Konsole](Python_console/de.md) ermittelt werden:


{{Code|lang=bash|code=
FreeCAD.getUserAppDataDir()
}}

Der Inhalt deiner **profiles.csv**-Datei muss den gleichen Regeln wie die Datei [profiles.csv](https://github.com/FreeCAD/FreeCAD/blob/main/src/Mod/BIM/Presets/profiles.csv) im Quell-Code entsprechen.

Die CSV-Datei muss eine Zeile für jedes verfügbare Profil enthalten, formatiert wie folgt:

-   Für C-Profile: Kategorie, Name, Profilklasse, Durchmesser, Wandstärke
-   Für H-, U- und T-Profile: Kategorie, Name, Profilklasse, Breite, Höhe, Stegbreite, Flanschstärke
-   Für L-Profile: Kategorie, Name, Profilklasse, Breite, Höhe, Wandstärke
-   Für R-Profile: Kategorie, Name, Profilklasse, Breite, Höhe
-   Für RH-Profile: Kategorie, Name, Profilklasse, Breite, Höhe, Wandstärke

Alle Abmessungen müssen in Millimetern angegeben werden. Mögliche Profilklassen sind:

-   C: Kreisförmiges Rohr
-   H: [H- oder I-Profil](https://de.wikipedia.org/wiki/Profilstahl)
-   R: Rechteckig
-   RH: Rechteckig hohl
-   U: U-Profil
-   L: L-Profil
-   T: T-Profil

Es können zusätzliche Profiltypen erstellt werden, aber zuerst muss in [ArchProfile.py](https://github.com/FreeCAD/FreeCAD/blob/main/src/Mod/BIM/ArchProfile.py) eine entsprechende Klasse definiert werden.



## Skripten

Das Profil-Werkzeug kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit folgender Funktion verwendet werden:


```python
profile = makeProfile(profile_list)
```

wobei {{Incode|profile_list}} die verschiedenen Elemente einer Liste in der CSV-Datei enthält.

Beispiel:


```python
import Arch
Arch.makeProfile([0, 'REC', 'REC100x100', 'R', 100, 100])
```

wobei das erste Element der Liste eine Bestellnummer (order number) ist, die bisher nicht verwendet wird.





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch Profile/de
