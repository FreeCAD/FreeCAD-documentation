---
- GuiCommand   */it
   Name   *Arch Panel Cut
   Name/it   *Arch Panel Cut
   MenuLocation   *Arch → Strumenti pannello → Sagoma pannello
   Workbenches   *[Arch](Arch_Workbench/it.md)
   Shortcut   ***P** **C**
   SeeAlso   *[Pannello](Arch_Panel/it.md), [Foglio pannello](Arch_Panel_Sheet/it.md), [Nido](Arch_Nest/it.md), [Ambiente Path](Path_Workbench/it.md)
---

# Arch Panel Cut/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Questo strumento crea, nel documento 3D, una vista piana, 2D di un [pannello](Arch_Panel/it.md), da inserire in un [Foglio pannello](Arch_Panel_Sheet/it.md) o da esportare direttamente in [DXF](Draft_DXF/it.md). Gli oggetti Sagoma pannello sono anche supportati dall\'ambiente [Path](Path_Workbench/it.md).


</div>

<img alt="" src=images/Arch_Wikihouse_02.jpg  style="width   *1024px;">

## Uso


<div class="mw-translate-fuzzy">

1.  Selezionare uno o più oggetti [Pannello](Arch_Panel/it.md)
2.  Premere il pulsante **<img src="images/Arch_Panel_Cut.svg" width=16px> [Sagoma pannello](Arch_Panel_Cut/it.md)
**, o premere i tasti **P** e poi **C**
3.  Regolare le proprietà desiderate


</div>

## Opzioni


<div class="mw-translate-fuzzy">

-   Se il pannello non è piatto, ma, per esempio è ondulato il rilievo non appare nella Sagoma del pannello. Questo strumento è utile soprattutto per i pannelli piatti
-   Sagoma del pannello può visualizzare un tag. Questo tag può essere una linea di testo personalizzata o può mostrare automaticamente il tag, l\'etichetta o la descrizione del pannello a cui è collegato.
-   Per essere utilizzato nelle lavorazioni CNC, il tag deve essere scritto con un font \"appiccicoso\", in cui le lettere sono semplici polilinee che la macchina possa seguire facilmente. Alla creazione, l\'oggetto Sagoma del pannello utilizza automaticamente il carattere specificato in Modifica → Preferenze → Draft → Testi e Dimensioni → Font ShapeString
-   Facendo doppio click su Sagoma del pannello nella vista ad albero dopo che essa è stata creata permette di entrare nella modalità di modifica e modificare la posizione del tag
-   Quando è necessario posizionare insieme diverse sagome di pannelli, Sagoma pannello può visualizzare un margine, che è utile per assicurare che tra di loro sia sempre presente un certo spazio


</div>

## Proprietà

### Data


<div class="mw-translate-fuzzy">

### Dati

-    {{PropertyData/it|Source}}   * L\'oggetto [Pannello](Arch_Panel/it.md) mostrato da questa sagoma

-    {{PropertyData/it|Tag Text}}   * Il testo da visualizzare. Può essere %tag%, %label% or %description% per visualizzare il tag del pannello o l\'etichetta

-    {{PropertyData/it|Tag Size}}   * La dimensione del testo tag

-    {{PropertyData/it|Tag Position}}   * La posizione del testo tag. Tenere (0,0,0) per la posizionarlo automaticamente nel centro

-    {{PropertyData/it|Tag Rotation}}   * La rotazione del testo tag

-    {{PropertyData/it|Font File}}   * Il carattere del testo tag

-    {{PropertyData/it|Make Face}}   * Se è True, il pannello è una Part Face, altrimenti è una Part Wire


</div>

### View


<div class="mw-translate-fuzzy">

### Vista

-    {{PropertyView/it|Margin}}   * Un margine che può essere visualizzato all\'esterno della sagoma del pannello

-    {{PropertyView/it|Show Margin}}   * Attiva o disattiva la visualizzazione del margine


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche   ***

[Arch API](Arch_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Sagoma pannello può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione   *


</div>


```python
View = makePanelCut(panel, name="PanelView")```

-   Crea un oggetto `View` (proiezione 2D) dal `panel` esistente.

Esempio   * 
```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(500, 0, 0)
p3 = FreeCAD.Vector(500, 50, 0)
p4 = FreeCAD.Vector(550, 50, 0)
p5 = FreeCAD.Vector(600, 0, 0)
p6 = FreeCAD.Vector(1000, 0, 0)
p7 = FreeCAD.Vector(1000, 400, 0)
p8 = FreeCAD.Vector(600, 400, 0)
p9 = FreeCAD.Vector(600, 350, 0)
p10 = FreeCAD.Vector(550, 350, 0)
p11 = FreeCAD.Vector(500, 400, 0)
p12 = FreeCAD.Vector(0, 400, 0)

Wire = Draft.makeWire([p1, p2, p3, p4, p5, p6,
                       p7, p8, p8, p9, p10, p11, p12], closed=True)
Panel = Arch.makePanel(Wire, thickness=36)
FreeCAD.ActiveDocument.recompute()

View = Arch.makePanelCut(Panel)
View.ViewObject.LineWidth = 3
FreeCAD.ActiveDocument.recompute()
```

## Tutorial


<div class="mw-translate-fuzzy">

-   [Tutorial Wikihouse portabile](Wikihouse_porting_tutorial/it.md)


</div>


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Panel Cut/it
