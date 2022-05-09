---
- GuiCommand   */it
   Name   *Arch Panel Sheet
   Name/it   *Foglio di pannello
   MenuLocation   *Arch → Strumenti pannello → Foglio pannello
   Workbenches   *[Arch](Arch_Workbench/it.md)
   Shortcut   ***P** **S**
   SeeAlso   *[Pannello](Arch_Panel/it.md), [Sagoma pannello](Arch_Panel_Cut/it.md), [Nido](Arch_Nest/it.md)
---

# Arch Panel Sheet/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Questo strumento permette di costruire un foglio 2D con un numero qualsiasi di oggetti [Sagoma di pannello](Arch_Panel_Cut/it.md), o qualsiasi altri oggetti 2D come quelli prodotti da [Draft](Draft_Workbench/it.md) e [Sketcher](Sketcher_Workbench/it.md). Il Foglio pannello consiste tipicamente in un tracciato di tagli che devono essere eseguiti da una macchina CNC. Questi fogli possono poi essere esportati in un file [DXF](Draft_DXF.md).


</div>

<img alt="" src=images/Arch_Wikihouse_03.jpg  style="width   *1024px;">

<img alt="" src=images/Arch_Wikihouse_04.jpg  style="width   *1024px;">

*L\'immagine sopra mostra come appaiono i Fogli pannello quando sono esportati in DXF.*

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Facoltativamente, selezionare uno o più oggetti [Sagoma pannello](Arch_Panel_Cut/it.md) o qualsiasi altro oggetto 2D posizionato sul piano XY.
2.  Premere il pulsante **<img src="images/Arch_Panel_Sheet.svg" width=16px> [Foglio pannello](Arch_Panel_Sheet/it.md)**, o premere i tasti **P** e poi **S**.
3.  Regolare le proprietà desiderate.


</div>

## Opzioni

-   Dopo aver creato il foglio pannello, con o senza oggetti figlio, con un doppio clic su di esso nella vista ad albero si può aggiungere o rimuovere dal foglio pannello qualsiasi altro oggetto figlio aggiungendo o rimuovendo gli oggetti dalla sua cartella Group
-   Facendo doppio click sul pannello nella vista ad albero consente inoltre di spostare gli oggetti contenuti in questo foglio, o spostare il suo tag
-   È possibile creare automaticamente pannelli composti da più fogli di materiale, incrementando la sua proprietà Sheets
-   Fogli pannello in grado di visualizzare un margine, che è utile per garantire che ci sia sempre un certo spazio tra gli oggetti interni e il bordo del foglio
-   Quando i fogli pannello vengono esportati in DXF, i contorni, i fori interni, i tag dei loro figli interni sono collocati su layer diversi, come mostrato nell\'immagine sopra

## Proprietà

### Data


<div class="mw-translate-fuzzy">

### Dati

-    {{PropertyData/it|Height}}   * L\'altezza del foglio

-    {{PropertyData/it|Width}}   * La larghezza del foglio

-    {{PropertyData/it|Fill Ratio}}   * La percentuale della superficie foglio che viene riempito dalle sagome (automatica)

-    {{PropertyData/it|Tag Text}}   * Il testo da visualizzare

-    {{PropertyData/it|Tag Size}}   * La dimensione del testo tag

-    {{PropertyData/it|Tag Position}}   * La posizione del testo tag. Tenere (0,0,0) per la posizionarlo automaticamente nel centro

-    {{PropertyData/it|Tag Rotation}}   * La rotazione del testo tag

-    {{PropertyData/it|Font File}}   * Il carattere del testo tag

-    {{PropertyData/it|Make Face}}   * Se è True, il pannello è una Part Face, altrimenti è una Part Wire

-    {{PropertyData/it|Grain Direction}}   * Ciò consente di sapere la direzione principale della fibra del pannello (senso orario, 0 ° significa in alto)


</div>

### View


<div class="mw-translate-fuzzy">

### Vista

-    {{PropertyView/it|Margin}}   * Un margine che può essere visualizzato all\'interno del bordo del pannello

-    {{PropertyView/it|Show Margin}}   * Attiva o disattiva la visualizzazione del margine

-    {{PropertyView/it|Show Grain}}   * Mostra la struttura della fibra (Make Face deve essere impostata su True)


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche   ***

[Arch API](Arch_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Foglio pannello può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione   *


</div>


```python
Sheet = makePanelSheet(panels=[], name="PanelSheet")
```

-   Crea un oggetto `Sheet` dai `panels`, che sono una lista di oggetti [Pannello](Arch_Panel/it.md).

Esempio   *


```python
import FreeCAD, Draft, Arch

Rect = Draft.makeRectangle(500, 200)
Polygon = Draft.makePolygon(5, 750)

p1 = FreeCAD.Vector(1000, 0, 0)
p2 = FreeCAD.Vector(2000, 400, 0)
p3 = FreeCAD.Vector(1250, 800, 0)
Wire = Draft.makeWire([p1, p2, p3], closed=True)

Panel1 = Arch.makePanel(Rect, thickness=36)
Panel2 = Arch.makePanel(Polygon, thickness=36)
Panel3 = Arch.makePanel(Wire, thickness=36)
FreeCAD.ActiveDocument.recompute()

Cut1 = Arch.makePanelCut(Panel1)
Cut2 = Arch.makePanelCut(Panel2)
Cut3 = Arch.makePanelCut(Panel3)
Cut1.ViewObject.LineWidth = 3
Cut2.ViewObject.LineWidth = 3
Cut3.ViewObject.LineWidth = 3
FreeCAD.ActiveDocument.recompute()

Sheet = Arch.makePanelSheet([Cut1, Cut2, Cut3])
```

## Tutorial


<div class="mw-translate-fuzzy">

-   [Tutorial Wikihouse portabile](Wikihouse_porting_tutorial/it.md)


</div>


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Panel Sheet/it
