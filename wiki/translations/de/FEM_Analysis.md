---
 GuiCommand:
   Name: FEM Analysis
   Name/de: FEM Analyse
   MenuLocation: Modell , Analysebehälter
   Workbenches: FEM_Workbench/de
   Shortcut: **S** **A**
   SeeAlso: FEM_tutorial/de
---

# FEM Analysis/de



## Beschreibung

Das FEM Analysis(-Objekt) könnte als ein Behälter gesehen werden, der alle Objekte einer Finite-Elemente-Analyse aufnimmt. Es muss ein Analysebehälter vorhanden sein, der alle benötigten Objekte aufnehmen kann. Mindestens eines der folgenden Objekte (außer dem Netz) wird für eine mechanische Analyse benötigt:

-   Ein [Festkörper-Material](FEM_MaterialSolid/de.md),
-   Eine Randbedingung für eine [Befestigung](FEM_ConstraintFixed/de.md) (Einspannung), eine [Auslenkung](FEM_ConstraintDisplacement/de.md) (Verschiebung), oder einen [starren Körper](FEM_ConstraintRigidBody/de.md).



## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/FEM_Analysis.svg" width=16px> [Analysebehälter](FEM_Analysis/de.md)** drücken.
    -   Den Menüeintrag **Modell → <img src="images/FEM_Analysis.svg" width=16px> Analysebehälter** auswählen.
    -   Das Tastaturkürzel **S** dann **A**.
2.  Eine neue Analyse (ein Analysis-Objekt) wird erstellt und aktiviert.
3.  Andere Objekte können dem Analysebehälter durch Ziehen und Ablegen hinzugefügt oder entfernt werden.
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
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM Analysis/de
