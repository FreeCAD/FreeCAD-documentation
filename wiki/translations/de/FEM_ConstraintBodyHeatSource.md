---
- GuiCommand:
   Name:FEM ConstraintBodyHeatSource
   Name/de:FEM RandbedingungKörperwärmequelle
   MenuLocation:Modell - Thermische Randbedingungen - Randbedingung Körperwärmequelle
   Workbenches:[FEM](FEM_Workbench/de.md)
   Version:0.19
   SeeAlso:[FEM Tutorium](FEM_tutorial/de.md)
---

# FEM ConstraintBodyHeatSource/de



## Beschreibung

Legt eine intern erzeugte Körperwärme fest, angegeben in W/kg.



## Anwendung

1.  Entweder die Schaltfläche **<img src="images/FEM_ConstraintBodyHeatSource.svg" width=16px> '''Randbedingung Körperwärmequelle'''** drücken oder den Menüeintrag **Modell → Thermische Randbedingungen → <img src="images/FEM_ConstraintBodyHeatSource.svg" width=16px> Randbedingung Körperwärmequelle** auswählen.
2.  Werte anpassen:
    -   
        {{VersionPlus/de|0.21}}
        
        : Für eine 3D-Analyse einen Festkörper (body) des modells auswählen, für eine 2D-Analyse eine Fläche auswählen.

    -   
        {{VersionMinus/de|0.20}}
        
        : Da die Randbedingung keinen Aufgaben-Dialog besitzt, wird der [Eigenschafteneditor](Property_editor.md) verwendet, um die {{PropertyData/de|Heat Source}} anzupassen.



## Einschränkungen


{{VersionMinus/de|0.20}}

: Die Körperwärmequelle wird auf das gesamte Modell angewendet, also alle Körper der Zusammenstellung. Es ist nicht möglich einen einzelnen Körper auszuwählen.



## Hinweise

-   Diese Randbedingung funktioniert nur mit dem Löser Elmer.
-   Für weitere Informationen siehe [Dieses Forumsthema](https://forum.freecadweb.org/viewtopic.php?f=18&t=44705&start=490#p422539) und folgende Posts. [Dieses Thema](https://forum.freecadweb.org/viewtopic.php?f=18&t=28926) kann auch nützlich sein.
-   Elmer Beispiele können auch unter [Elmer GUI Tutorials](https://www.nic.funet.fi/pub/sci/physics/elmer/doc/ElmerTutorials.pdf) gefunden werden.




{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintBodyHeatSource/de
