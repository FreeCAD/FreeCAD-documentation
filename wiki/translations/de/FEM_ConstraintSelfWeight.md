---
- GuiCommand:/de
   Name:FEM ConstraintSelfWeight
   Name/de:FEM RandbedingungEigengewicht
   MenuLocation:Modell → Mechanische Randbedingungen → Randbedingung Eigengewicht
   Workbenches:[FEM](FEM_Workbench/de.md)
   SeeAlso:[FEM Tutorium](FEM_tutorial/de.md)
---

# FEM ConstraintSelfWeight/de

## Beschreibung

Die Randbedingung Eigengewicht legt fest, dass die Erdbeschleunigung von 9,81 m/s\^2 auf das gesamte Modell in der voreingestellten Richtung wirkt.

## Anwendung

1.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/FEM_ConstraintSelfWeight.svg" width=16px> [Randbedingung Eigengewicht](FEM_ConstraintSelfWeight.md)** drücken.
    -   Den Menüeintrag **Modell → Mechanische Randbedingungen → <img src="images/FEM_ConstraintSelfWeight.svg" width=16px> Randbedingung Eigengewicht** auswählen.
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

### Limitations

-   Zum Ändern der Erdbeschleunigung muss die .inp-Datei bearbeitet werden.
-   Self weight is applied to the element set Eall means to the whole model.

### Die CalculiX-input-Datei bearbeiten 

Die Beschleunigungskonstante kann nach Erstellung der CalculiX-input-Datei von Hand geändert werden.

Beispielzeilen in der .inp-Datei:


```python
*DLOAD
Eall,GRAV,9810,0.0,0.0,-1.0
```

wobei 9810 der Wert der Erdbeschleunigung in \[mm/s\^2\] ist und 0,0,-1 den Richtungsvektor beschreibt.

## Solver Z88 

-   not implemented in Z88 solver (March 2017)





{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintSelfWeight/de
