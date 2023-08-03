---
 GuiCommand:
   Name: Arch Truss
   Name/it: Travatura
   MenuLocation: Arch , Travatura
   Workbenches: Arch_Workbench/it
   Version: 0.19
---

# Arch Truss/it



## Descrizione

Lo strumento [Travatura](Arch_Truss/it.md) crea un oggetto [travatura](https://en.wikipedia.org/wiki/Truss), sia da un oggetto lineare selezionato (posta su una [Linea di Draft](Draft_Line/it.md) o uno \[\[Sketcher_NewSketch/it\|Schizzo\] \]), o da zero se non viene selezionato alcun oggetto all\'avvio del comando.

<img alt="" src=images/Arch_Truss_example.png  style="width:600px;">



## Utilizzo



### Creare da un oggetto selezionato 

1.  Utilizzare un ambiente di lavoro a scelta per creare un\'unica linea
2.  Selezionare quella linea
3.  Premere il pulsante **<img src="images/Arch_Truss.svg" width=16px> [Travatura](Arch_Truss/it.md)
**
4.  Regolare le proprietà della capriata a proprio piacimento



### Creare dall\'inizio 

1.  Assicurarsi che non sia selezionato nulla
2.  Premere il pulsante **<img src="images/Arch_Truss.svg" width=16px> [Travatura](Arch_Truss/it.md)
**
3.  Fare clic nella vista 3D per definire un primo punto o immettere manualmente le coordinate X, Y e Z.
4.  Fare clic nella vista 3D per definire il secondo punto o immettere manualmente le coordinate X, Y e Z.
5.  Regolare le proprietà della capriata a proprio piacimento



## Proprietà



### Dati

-    **TrussAngle**: L\'angolo della capriata

-    **SlantType**: Il tipo inclinato di questa capriata

-    **Normal**: La direzione normale di questa capriata

-    **HeightStart**: L\'altezza della capriata nel punto iniziale

-    **HeightEnd**: L\'altezza della capriata nel punto finale

-    **StrutStartOffset**: Un offset iniziale opzionale per il montante superiore

-    **StrutEndOffset**: Un offset finale opzionale per il montante superiore

-    **StrutHeight**: L\'altezza degli elementi superiori e inferiori principali della capriata

-    **StrutWidth**: La larghezza degli elementi superiore e inferiore principali della capriata

-    **RodType**: Il tipo di elemento centrale della capriata

-    **RodDirection**: La direzione delle aste

-    **RodSize**: Il diametro o il lato delle aste

-    **RodSections**: Il numero di sezioni dell\'asta

-    **RodEnd**: Se la capriata ha un\'asta al suo punto finale o no

-    **RodMode**: Come disegnare le aste



## Script

Lo strumento Travatura può essere utilizzato nelle [macro](Macros/it.md) e dalla console [Python](FreeCAD_Scripting_Basics/it.md) tramite la seguente funzione:


```python
Truss = makeFence([baseobj])
```

Esempio:


```python
import FreeCAD
import Draft
import Arch

p1 = FreeCAD.Vector(0,0,0)
p2 = FreeCAD.Vector(2000,0,0)
baseline = Draft.makeLine(p1,p2)
truss = Arch.makeTruss(baseline)
truss.HeightStart = 200
truss.HeightEnd = 400
# adjust other needed properties
```



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Truss/it
