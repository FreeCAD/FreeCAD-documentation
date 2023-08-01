---
- GuiCommand:/de
   Name:FEM Analysis
   Name/de:FEM Analyse
   MenuLocation:Modell → Analyse-Container‏‎
   Workbenches:[FEM](FEM_Workbench/de.md)
   Shortcut:**S** **A**
   SeeAlso:[FEM Tutorium](FEM_tutorial/de.md)
---

# FEM Analysis/de

## Beschreibung

Das FEM Analysis(-Objekt) könnte als ein Behälter gesehen werden, der alle Objekte einer Finite Element Analyse aufnimmt. Es ist obligatorisch, einen Analysecontainer zu haben, der alle benötigten Objekte enthält. Mindestens eines der folgenden Objekte wird für eine mechanische Analyse benötigt:

-   Ein [Material](FEM_MaterialSolid/de.md)
-   Randbedingungen zur [Befestigung](FEM_ConstraintFixed/de.md) (Einspannung)
-   Randbedingungen zur [Krafteinleitung](FEM_ConstraintForce/de.md) oder [Druckbeaufschlagung](FEM_ConstraintPressure/de.md)

## Anwendung

1.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/FEM_Analysis.svg" width=16px> [Analyse-Container](FEM_Analysis/de.md)** drücken.
    -   Den Menüeintrag **Modell → <img src="images/FEM_Analysis.svg" width=16px> Analyse-Container‏‎** auswählen.
    -   Das Tastaturkürzel **S** dann **A**.
2.  Eine neue Analyse (ein Analysis-Objekt) wird erstellt und aktiviert.
3.  Andere Objekte können dem Analysecontainer durch Ziehen und Ablegen hinzugefügt oder entfernt werden.
4.  Um dem Dokument neue FEM-Objekte hinzuzufügen, muss die Analyse aktiv sein. Ein Doppelklick auf das Analysis-Objekt aktiviert die Analyse.

## Optionen

-   Bislang gibt es keine Option zur Auswahl.

## Eigenschaften

-    **OutpuDir**: Gibt das Arbeitsverzeichnis der Analyse an

## Skripten

Der Großteil des Codes hier ist seit 0.17 veraltet.

-   neue Analyse


```python
MechanicalAnalysis.makeMechanicalAnalysis( name )
```

-   Objekt zur Analyse hinzufügen


```python
App.ActiveDocument.MechanicalAnalysis.Member = App.ActiveDocument.MechanicalAnalysis.Member + [ (object) ]
```

-   Objekt aus der Analyse entfernen


```python
member = App.ActiveDocument.MechanicalAnalysis.Member
member.remove( documentobject )
 App.ActiveDocument.MechanicalAnalysis.Member = member
```

Beispiele: 
```python
import MechanicalAnalysis
analysis = MechanicalAnalysis.makeMechanicalAnalysis("MechanicalAnalysis")
FemGui.setActiveAnalysis(analysis)

addobj = App.ActiveDocument.getObject("MechanicalMaterial")
App.ActiveDocument.MechanicalAnalysis.Member = App.ActiveDocument.MechanicalAnalysis.Member + [addobj]

removeobj = App.ActiveDocument.getObject("MechanicalMaterial")
member = App.ActiveDocument.MechanicalAnalysis.Member
member.remove(removeobj)
App.ActiveDocument.MechanicalAnalysis.Member = member
```





{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM Analysis/de
