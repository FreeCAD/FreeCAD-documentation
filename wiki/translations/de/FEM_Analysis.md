---
- GuiCommand:/de
   Name:FEM Analysis
   Name/de:FEM Analyse
   MenuLocation:Modell → Analysecontainer‏‎
   Workbenches:[FEM](FEM_Workbench/de.md)
   Shortcut:**N** **A**
   SeeAlso:[FEM Tutorium](FEM_tutorial/de.md)
---

# FEM Analysis/de


</div>

## Beschreibung


<div class="mw-translate-fuzzy">

Die FEM Analyse könnte als ein Behälter gesehen werden, der alle Objekte einer Finite Element Analyse aufnimmt. Es ist obligatorisch, einen Analysecontainer zu haben, der alle benötigten Objekte enthält. Mindestens eines der folgenden Objekte wird für eine mechanische Analyse benötigt:

-   [Material](FEM_MaterialSolid/de.md)
-   [ festgelegte Beschränkung](FEM_ConstraintFixed/de.md)
-   [ Kraftbeschränkung](FEM_ConstraintForce/de.md) oder [ Druckbeschränkung](FEM_ConstraintPressure/de.md)


</div>

## Anwendung


<div class="mw-translate-fuzzy">

1.  Drücke die**<img src="images/FEM_Analysis.png" width=24px> [Analysis container](FEM_Analysis/de.md)** Schaltfläche oder drücke die **N** und dann **A** Tasten. Eine neue Analyse wird erstellt und auf aktiv gesetzt.
2.  Andere Objekte können dem Analysecontainer durch Ziehen und Ablegen hinzugefügt oder entfernt werden.
3.  Um dem Dokument neue FEM Objekte hinzuzufügen, muss die Analyse aktiv sein. Doppelklicke auf die Analyse, um die Analyse zu aktivieren.


</div>

## Optionen

-   Bislang gibt es keine Option zur Auswahl.
-   Eine Häufigkeitsanalyse ist in Entwicklung. Siehe [1](http://forum.freecadweb.org/viewtopic.php?f=18&t=12189) für weitere Informationen.

## Eigenschaften

-    **OutpuDir**: Gibt das Arbeitsverzeichnis der Analyse an

## Skripten

der Großteil des Codes hier ist in 0.17 abgeschrieben.

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


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM Analysis/de
