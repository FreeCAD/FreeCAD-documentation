---
 GuiCommand:
   Name: Arch Panel
   Name/it: Pannello
   MenuLocation: Arch , Strumenti pannello , Pannello
   Workbenches: Arch_Workbench/it
   Shortcut: **P** **A**
   Version: 0.15
   SeeAlso: Arch_Panel_Cut/it, Arch_Panel_Sheet/it
---

# Arch Panel/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Questo strumento consente di creare tutti i tipi di elementi simil-pannelli, in genere per le costruzioni di pannelli come nei progetti [WikiHouse](http://www.wikihouse.cc/), ma anche per tutti i tipi di oggetti che si basano su un profilo piatto.


</div>

<img alt="" src=images/Arch_Panel_example.jpg  style="width:700px;">

*L\'immagine precedente mostra una serie di oggetti pannello, semplicemente ottenuti da profili 2D importati da un file DXF. Possono essere ruotati e assemblati per creare strutture.*

Dalla versione 0.17, il Pannello Arch può anche essere usato per creare dei profili ondulati o trapezoidali:

<img alt="" src=images/Arch_panel_wave.jpg  style="width:700px;">



## Utilizzo


<div class="mw-translate-fuzzy">

-   Selezionare una forma 2D (oggetto di Draft, faccia o schizzo) - opzionale.
-   Premere il pulsante **<img src="images/Arch_Panel.svg" width=16px> [Pannello](Arch_Panel/it.md)**, oppure premere i tasti **P** e **A**.
-   Regolare le proprietà come desiderate.


</div>



### Limitazioni

-   Attualmente non esiste un sistema automatico per creare tagli 2D nei fogli usando oggetti pannello, ma tale caratteristica è prevista e sarà aggiunta in futuro.



## Opzioni

-   Gli elementi Pannello condividono le proprietà e i comportamenti comuni di tutti i [Componenti Arch](Arch_Component/it.md).
-   Lo spessore di un pannello può essere regolato dopo la creazione.
-   Premere il tasto **Esc** o **Cancel** per uscire dal corrente comando.
-   Facendo doppio click sul pannello nella vista ad albero dopo che è stato creato consente di entrare in modalità modifica e accedere alla modifica delle sue addizioni e sottrazioni.
-   È possibile creare automaticamente dei pannelli composti da più fogli di materiale, incrementando la sua proprietà Sheets (fogli).
-   I Pannelli possono utilizzare i <img alt="" src=images/Arch_MultiMaterial.svg  style="width:24px;"> [ Multi-Materiali](Arch_MultiMaterial/it.md). Quando si utilizza un multi-materiale, il pannello diventa multistrato, utilizzando gli spessori specificati nel multi-materiale. A qualsiasi strato con uno spessore pari a zero viene assegnato lo spessore definito automaticamente dallo spazio rimanente definito dal valore dello spessore del pannello meno gli altri strati.



## Proprietà

-    {{PropertyData/it|Length}}: La lunghezza del pannello

-    {{PropertyData/it|Width}}: La larghezza del pannello

-    {{PropertyData/it|Thickness}}: Lo spessore del pannello

-    {{PropertyData/it|Area}}: L\'area del pannello (automatica)

-    {{PropertyData/it|Sheets}}: Il numero di fogli di materiale che compongono il pannello

-    {{PropertyData/it|Wave Length}}: La lunghezza d\'onda per pannelli ondulati

-    {{PropertyData/it|Wave Height}}: L\'altezza dell\'onda per pannelli ondulati

-    {{PropertyData/it|Wave Type}}: Il tipo di onda per pannelli ondulati, curvi, trapezoidali o triangolari

-    {{PropertyData/it|Wave Direction}}: L\'orientamento delle onde per pannelli ondulati

-    **Bottom Wave**: Se l\'onda inferiore del pannello è piatta o no



## Script


**Vedere anche:**

[API di Arch](Arch_API/it.md) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).


<div class="mw-translate-fuzzy">

Lo strumento Pannello può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione:


</div>


```python
Panel = makePanel(baseobj=None, length=0, width=0, thickness=0, placement=None, name="Panel")
```

-   Crea un oggetto `Panel` dal `baseobj` dato, che è un profilo chiuso, e l\'estrusione `thickness` data.
    -   Se non viene fornito nessun `baseobj`, si possono fornire i valori numerici per `length`, `width`, e `thickness` per creare un blocco pannello.
-   Se viene fornito un `placement`, esso viene utilizzato.

Esempio:


```python
import FreeCAD, Draft, Arch

Rect = Draft.makeRectangle(1000, 400)
Panel = Arch.makePanel(Rect, thickness=36)
```



## Tutorial

-   [Wikihouse porting tutorial](Wikihouse_porting_tutorial/it.md)


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > Arch Panel/it
