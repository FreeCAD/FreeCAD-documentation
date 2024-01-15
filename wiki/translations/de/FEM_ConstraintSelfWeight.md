---
 GuiCommand:
   Name: FEM ConstraintSelfWeight
   Name/de: FEM RandbedingungEigengewicht
   MenuLocation: Modell , Mechanische Randbedingungen und Lasten , Schwerkraft-Last
   Workbenches: FEM_Workbench/de
   SeeAlso: FEM_tutorial/de
---

# FEM ConstraintSelfWeight/de



## Beschreibung

RandbedingungEigengewicht legt fest, dass die Erdbeschleunigung mit 9,81 m/s\^2 in der voreingestellten Richtung auf das gesamte Modell wirkt.



## Anwendung

1.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/FEM_ConstraintSelfWeight.svg" width=16px> [Schwerkraft-Last](FEM_ConstraintSelfWeight/de.md)** drücken.
    -   Den Menüeintrag **Modell → Mechanische Randbedingungen und Lasten → <img src="images/FEM_ConstraintSelfWeight.svg" width=16px> Schwerkraft-Last** auswählen.
2.  Die Richtung der Erdanziehungskraft kann durch Ändern der Vektorkoordinaten im Eigenschafteneditor des neu erstellten ConstraintSelfWeight-Objekts angepasst werden.



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

## Solver CalculiX 



### Einschränkungen

-   Zum Ändern der Erdbeschleunigung muss die .inp-Datei bearbeitet werden.
-   Eigengewicht wird auf die Menge der Elemente Eall angewendet, die das gesamte Modell enthält.



### Die CalculiX-input-Datei bearbeiten 

Die Beschleunigungskonstante kann nach Erstellung der CalculiX-input-Datei manuell geändert werden.

Beispielzeilen in der .inp-Datei:


```python
*DLOAD
Eall,GRAV,9810,0.0,0.0,-1.0
```

wobei 9810 der Wert der Erdbeschleunigung in \[mm/s\^2\] ist und 0,0,-1 den Richtungsvektor beschreibt. Der Wert kann als Vielfaches der (standardisierten) Erdbeschleunigung eingegeben werden um eine Belastung von z.B. 4g zu simulieren.

## Solver Z88 

-   Currently, not implemented in the Z88 solver.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintSelfWeight/de
