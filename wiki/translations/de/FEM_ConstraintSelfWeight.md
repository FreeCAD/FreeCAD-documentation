---
 GuiCommand:Container|
{{GuiCommand/de
   Name: FEM ConstraintSelfWeight
   Name/de: FEM RandbedingungEigengewicht
   MenuLocation: Modell , Mechanische Randbedingungen und Lasten , Schwerkraft-Last
   Workbenches: FEM_Workbench/de
   SeeAlso: FEM_tutorial/de
}}
{{GuiCommandFemInfo/de
   Solvers: CalculiX, Elmer
}}
---

# FEM ConstraintSelfWeight/de



## Beschreibung

RandbedingungEigengewicht legt fest, dass die Erdbeschleunigung in der voreingestellten Richtung auf das gesamte Modell wirkt.


{{VersionMinus/de|0.21}}

: Die Beschleunigung hat einen unveränderlichen Wert von 9.81 m/s\^2.



## Anwendung

1.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/FEM_ConstraintSelfWeight.svg" width=16px> [Schwerkraft-Last](FEM_ConstraintSelfWeight/de.md)** drücken.
    -   Den Menüeintrag **Modell → Mechanische Randbedingungen und Lasten → <img src="images/FEM_ConstraintSelfWeight.svg" width=16px> Schwerkraft-Last** auswählen.

2.  Ein ConstraintSelfWeight-Objekt wird erstellt.

3.  
    {{Version/de|1.0}}: Wahlweise kann seine {{PropertyData/de|Gravity Acceleration}} geändert werden.

4.  Wahlweise seine {{PropertyData/de|Gravity Direction}} anpassen.



## Skripten

Neues Objekt:


```python
import ObjectsFem
ObjectsFem.makeConstraintSelfWeight(name)
```

Ein Objekt zum Analysis genannten Analyse-Container hinzufügen:


```python
App.ActiveDocument.Analysis.Member = App.ActiveDocument.Analysis.Member + [(object)]
```

Beispiel:


```python
import ObjectsFem
selfweight_obj = ObjectsFem.makeConstraintSelfWeight("MySelfWeightObject")
App.ActiveDocument.Analysis.Member = App.ActiveDocument.Analysis.Member + [selfweight_obj]
```



## Löser CalculiX 



### Einschränkungen

-    {{VersionMinus/de|0.21}}: Zum Ändern der Erdbeschleunigung muss die .inp-Datei bearbeitet werden.

-   Eigengewicht wird auf die Menge der Elemente Eall angewendet, die das gesamte Modell enthält.



### Die CalculiX-input-Datei bearbeiten 

Die Beschleunigungskonstante kann nach Erstellung der CalculiX-input-Datei manuell geändert werden.

Beispielzeilen in der .inp-Datei:


```python
*DLOAD
Eall,GRAV,9810,0.0,0.0,-1.0
```

wobei 9810 der Wert der Erdbeschleunigung in \[mm/s\^2\] ist und 0,0,-1 den Richtungsvektor beschreibt. Der Wert kann als Vielfaches der (standardisierten) Erdbeschleunigung eingegeben werden um eine Belastung von z.B. 4g zu simulieren.



## Löser Z88 

-   Zurzeit nicht im Löser Z88 implementiert.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintSelfWeight/de
