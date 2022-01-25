---
- GuiCommand:/it
   Name:FEM_Analysis
   Name/it:Analisi FEM
   MenuLocation:Modello → Contenitore analisi
   Workbenches:[FEM](FEM_Workbench/it.md)
   Shortcut:**S** **A**
   SeeAlso:[Tutorial FEM](FEM_tutorial/it.md)
---

# FEM Analysis/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Analisi FEM può essere visto come il contenitore di tutti gli oggetti di una Analisi agli elementi finiti. È obbligatorio avere un contenitore Analisi che contenga tutti gli oggetti necessari. Per poter eseguire un\'analisi meccanica serve almeno uno dei seguenti oggetti:

-   [ materiale](FEM_MaterialSolid/it.md)
-   [ vincolo fissaggio](FEM_ConstraintFixed/it.md)
-   [ vincolo forza](FEM_ConstraintForce/it.md) oppure [ vincolo pressione](FEM_ConstraintPressure/it.md)


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/FEM_Analysis.png" width=24px> [Analisi](FEM_Analysis/it.md)**, oppure i tasti **N** e **A**. Viene creata e attivata una nuova Analisi.
2.  Nel contenitore Analisi si possono aggiungere o rimuovere gli oggetti con azioni drag and drop.
3.  Per aggiungere nuovi oggetti FEM al documento l\'analisi deve essere attiva. Fare doppio clic sull\'analisi per attivarla.


</div>

## Opzioni

-   Per ora non ci sono opzioni.
-   L\'analisi in frequenza è in sviluppo. Vedere [1](http://forum.freecadweb.org/viewtopic.php?f=18&t=12189) per maggiori informazioni.

## Proprietà

-    **OutpuDir**: Specifica la directory di lavoro di Analisi

## Script

La maggior parte di questo codice è deprecato nella versione 0.17.

-   nuova analisi


```python
MechanicalAnalysis.makeMechanicalAnalysis( name )
```

-   aggiungere un oggetto all\'analisi


```python
App.ActiveDocument.MechanicalAnalysis.Member = App.ActiveDocument.MechanicalAnalysis.Member + [ (object) ]
```

-   rimuovere un oggetto dall\'analisi


```python
member = App.ActiveDocument.MechanicalAnalysis.Member
member.remove( documentobject )
 App.ActiveDocument.MechanicalAnalysis.Member = member
```

Esempio: 
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
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM Analysis/it
