---
 GuiCommand:
   Name: FEM_ConstraintSelfWeight
   Name/it: Vincolo peso proprio
   MenuLocation: Modello , Vincoli meccanici , Vincolo peso proprio
   Workbenches: FEM_Workbench/it
   Shortcut: **C** **W**
   SeeAlso: FEM_tutorial/it
---

# FEM ConstraintSelfWeight/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Il vincolo peso proprio definisce l\'accelerazione di gravità di 9,81 m/s\^2 che agisce su tutto il modello nella direzione prescritta.


</div>


{{VersionMinus|0.21}}

: The acceleration has a fixed value of 9.81 m/s\^2.



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Cliccare su <img alt="" src=images/FEM_ConstraintSelfWeight.png  style="width:32px;">, o scegliere **Modello** → **Vincoli meccanici** → **<img src="images/FEM_ConstraintSelfWeight.png" width=32px> Vincolo peso proprio** dal menu principale, o usare i tasti **C** e poi **W**.
2.  È possibile modificare la direzione della gravità, modificando le coordinate del suo vettore nelle proprietà del nuovo oggetto Vincolo peso proprio.


</div>



## Script


<div class="mw-translate-fuzzy">

**Nuovo oggetto**


</div>


```python
import ObjectsFem
ObjectsFem.makeConstraintSelfWeight(name)
```


<div class="mw-translate-fuzzy">

**Aggiungere all\'analisi un oggetto di nome Analisi**


</div>


```python
App.ActiveDocument.Analysis.Member = App.ActiveDocument.Analysis.Member + [(object)]
```


<div class="mw-translate-fuzzy">

**Esempio**


</div>


```python
import ObjectsFem
selfweight_obj = ObjectsFem.makeConstraintSelfWeight("MySelfWeightObject")
App.ActiveDocument.Analysis.Member = App.ActiveDocument.Analysis.Member + [selfweight_obj]
```

## Solver CalculiX 

### Limitations


<div class="mw-translate-fuzzy">

## Solver CalculiX 

### Limitazioni

-   È necessario modificare il file .inp modificare l\'accelerazione di gravità.
-   Applicare Peso proprio all\'elemento impostato Wall significa applicarlo all\'intero modello.


</div>

### Editing CalculiX input file 


<div class="mw-translate-fuzzy">

### Editare il file di input CalculiX 

La costante dell\'accelerazione può essere modificata a mano dopo la generazione del file di input CalculiX.


</div>


<div class="mw-translate-fuzzy">

Esempio di righenel file .inp: 
```python
*DLOAD
Eall,GRAV,9810,0.0,0.0,-1.0
``` dove 9810 è l\'accelerazione di gravità in \[mm/s\^2\], e 0,0,-1 è la direzione del vettore.


</div>


```python
*DLOAD
Eall,GRAV,9810,0.0,0.0,-1.0
```

where 9810 is a gravity acceleration magnitude in \[mm/s\^2\], and 0,0,-1 is the direction vector. The value can be set as a multiple of standard gravity acceleration to simulate loading of e.g. 4g.

## Solver Z88 


<div class="mw-translate-fuzzy">

## Solver Z88 

-   non implementato nel solver Z88 (Marzo 2017)


</div>


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintSelfWeight/it
