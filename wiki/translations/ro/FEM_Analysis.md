# FEM Analysis/ro
---
 GuiCommand:   Name: FEM Analysis   Name/ro: FEM Analysis   MenuLocation: Model , Analysis container‏‎   ---


</div>



## Descriere


<div class="mw-translate-fuzzy">

Analiza MEF poate fi văzută ca un Container care cuprinde toate obiectele Finite Element Analysis. Este obligatoriu să facem o analiză a containerului care cuprinde toate obiectele necesare. Cel puțin unul dintre următoarele obeicte este necesar pentru analiza mecanică:

-   [ material](FEM_MaterialSolid.md)
-   [ fixed constraint](FEM_ConstraintFixed.md)
-   [ force constraint](FEM_ConstraintForce.md) or [ pressure constraint](FEM_ConstraintPressure.md)


</div>




<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Apăsați butonul **<img src="images/FEM_Analysis.png" width=24px> [Analysis container](FEM_Analysis.md)** , sau apăsați tasta **N** apoi tasta**A** . O nouă analiză este creată și setată ca fiind activă.
2.  alte obiecte pot fi adăugate sau retrase din analiza containerului prin glisare și fixare -drag and drop.
3.  Pentru a adăuga obiecte noi MEF la documentul de analizat trebuie să fie activ. Dublu click on pe analiză trebuie să activeze analiza.


</div>



## Opțiuni


<div class="mw-translate-fuzzy">

-   Până în prezent nu există opțiune de alegere.
-   O analiză de frecvență în dezvoltare. A se vedea[1](http://forum.freecadweb.org/viewtopic.php?f=18&t=12189) for more informations.


</div>



## Proprietăți

-    **OutpuDir**: Specifică directorul de lucru a analizei



## Programare-Script 


<div class="mw-translate-fuzzy">

cea mai mare parte a codului a fost abandonat în versiunea 0.17.

-   o nouă analiză


</div>


```python
MechanicalAnalysis.makeMechanicalAnalysis( name )
```

-   adaugă un obiect la analiză


```python
App.ActiveDocument.MechanicalAnalysis.Member = App.ActiveDocument.MechanicalAnalysis.Member + [ (object) ]
```

-   suprimă un obiect din analiză


```python
member = App.ActiveDocument.MechanicalAnalysis.Member
member.remove( documentobject )
 App.ActiveDocument.MechanicalAnalysis.Member = member
```

Exempluː 
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
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM Analysis/ro
