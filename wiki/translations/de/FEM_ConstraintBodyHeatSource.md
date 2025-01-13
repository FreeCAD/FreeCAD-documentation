---
 GuiCommand:Container|
{{GuiCommand/de
   Name: FEM ConstraintBodyHeatSource
   Name/de: FEM RandbedingungKörperwärmequelle
   MenuLocation: Modell , Thermische Randbedingungen und Lasten , Körperwärmequelle
   Workbenches: FEM_Workbench/de
   Version: 0.19
   SeeAlso: FEM_tutorial/de
}}
{{GuiCommandFemInfo/de
   Solvers: CalculiX, Elmer
}}
---

# FEM ConstraintBodyHeatSource/de



## Beschreibung

Legt eine intern erzeugte Körperwärme fest, angegeben in W/kg.


{{VersionPlus/de|1.0}}

: Kann die Wärmequelle auch in W festlegen.



## Anwendung

1.  Die Schaltfläche **<img src="images/FEM_ConstraintBodyHeatSource.svg" width=16px> '''Körperwärmequelle'''** drücken oder den Menüeintrag **Modell → Thermische Randbedingungen und Belastungen → <img src="images/FEM_ConstraintBodyHeatSource.svg" width=16px> Körperwärmequelle** auswählen.

2.  
    {{VersionPlus/de|0.21}}: Die Schaltfläche **Hinzufügen** drücken. Für eine 3D-Analyse einen Festkörper (body) des Modells auswählen, für eine 2D-Analyse eine Fläche auswählen.

3.  Den Wert eingeben:
    -   
        {{VersionMinus/de|0.20}}
        
        : Da das Werkzeug keinen Aufgaben-Dialog besitzt, wird der [Eigenschafteneditor](Property_editor.md) verwendet, um die {{PropertyData/de|Heat Source}} anzupassen.

    -   
        {{Version/de|0.21}}
        
        : Die Körperwärme in W/kg eingeben.

    -   
        {{VersionPlus/de|1.0}}
        
        : Modus auswählen:

        -   *Dissipation Rate* - die Wärmeverlustleistung in W/kg eingeben.
        -   *Total Power* - die Gesamtleistung in W eingeben.



## Einschränkungen

-    {{VersionMinus/de|0.20}}: Die Körperwärmequelle wird auf das gesamte Modell angewendet, also alle Körper der Zusammenstellung. Es ist nicht möglich einen einzelnen Körper auszuwählen.

-    {{VersionMinus/de|0.21}}: Diese Funktion arbeitet nur mit dem Gleichungslöser Elmer zusammen.



## Hinweise

-   Für weitere Informationen siehe [dieses Thema im Forum](https://forum.freecadweb.org/viewtopic.php?f=18&t=44705&start=490#p422539) und folgende Posts. [Dieses Thema](https://forum.freecadweb.org/viewtopic.php?f=18&t=28926) kann auch nützlich sein.

-   Elmer-Beispiele können auch unter [Elmer-GUI-Tutorials](https://www.nic.funet.fi/pub/sci/physics/elmer/doc/ElmerTutorials.pdf) gefunden werden.

-    {{VersionPlus/de|1.0}}: Diese Funktion verwendet die [\*DFLUX Karte in CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node188.html).

-    {{VersionPlus/de|1.0}}: Da CalculiX die Eingabe des Körperwärmestroms in W/mm\^3 erwartet, während Elmer sie in W/kg benötigt, erfolgt die Umwandlung des angegebenen Wertes (in W oder W/kg) intern im jeweiligen Gleichungslöser unter Verwendung desVolumes des ausgewählten Festkörpers und der Dichte des ihm zugeordneten Materials, wenn erforderlich.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintBodyHeatSource/de
