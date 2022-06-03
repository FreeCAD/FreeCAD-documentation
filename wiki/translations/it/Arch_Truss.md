---
- GuiCommand   */it
   Name   *Arch Truss
   Name/it   *Arch Truss
   Workbenches   *[Arch](Arch_Workbench/it.md)
   MenuLocation   *Arch → Travatura
   Version   *0.19
---

# Arch Truss/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento [Travatura](Arch_Truss/it.md) crea un oggetto [travatura](https   *//en.wikipedia.org/wiki/Truss), sia da un oggetto lineare selezionato (posta su una [Linea di Draft](Draft_Line/it.md) o uno \[\[Sketcher\_NewSketch/it\|Schizzo\] \]), o da zero se non viene selezionato alcun oggetto all\'avvio del comando.


</div>

<img alt="" src=images/Arch_Truss_example.png  style="width   *600px;">

## Utilizzo

### Creare da un oggetto selezionato 


<div class="mw-translate-fuzzy">

1.  Utilizzare un ambiente di lavoro a scelta per creare un\'unica linea
2.  Selezionare quella linea
3.  Premere il pulsante **<img src="images/Arch_Truss.svg" width=16px> [Travatura](Arch_Truss/it.md)
**
4.  Regolare le proprietà della capriata a proprio piacimento


</div>

### Creare dall\'inizio 


<div class="mw-translate-fuzzy">

1.  Assicurarsi che non sia selezionato nulla
2.  Premere il pulsante **<img src="images/Arch_Truss.svg" width=16px> [Travatura](Arch_Truss/it.md)
**
3.  Fare clic nella vista 3D per definire un primo punto o immettere manualmente le coordinate X, Y e Z.
4.  Fare clic nella vista 3D per definire il secondo punto o immettere manualmente le coordinate X, Y e Z.
5.  Regolare le proprietà della capriata a proprio piacimento


</div>

## Proprietà

### Dati

-    **TrussAngle**   * L\'angolo della capriata

-    **SlantType**   * Il tipo inclinato di questa capriata

-    **Normal**   * La direzione normale di questa capriata

-    **HeightStart**   * L\'altezza della capriata nel punto iniziale

-    **HeightEnd**   * L\'altezza della capriata nel punto finale

-    **StrutStartOffset**   * Un offset iniziale opzionale per il montante superiore

-    **StrutEndOffset**   * Un offset finale opzionale per il montante superiore

-    **StrutHeight**   * L\'altezza degli elementi superiori e inferiori principali della capriata

-    **StrutWidth**   * La larghezza degli elementi superiore e inferiore principali della capriata

-    **RodType**   * Il tipo di elemento centrale della capriata

-    **RodDirection**   * La direzione delle aste

-    **RodSize**   * Il diametro o il lato delle aste

-    **RodSections**   * Il numero di sezioni dell\'asta

-    **RodEnd**   * Se la capriata ha un\'asta al suo punto finale o no

-    **RodMode**   * Come disegnare le aste

## Script


<div class="mw-translate-fuzzy">

Lo strumento Travatura può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](FreeCAD_Scripting_Basics/it.md) tramite la seguente funzione   *


</div>


```python
Truss = makeFence([baseobj])
```

Esempio   *


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


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Truss/it
