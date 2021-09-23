# Part Compound/it
---
- GuiCommand:/it   Name:Part Compound‏‎   Name/it:Crea un composto‏‎   MenuLocation:Parte → Crea un composto   Workbenches:[Version:0.14   SeeAlso:[[Part Union/it|Unione](Part_Workbench/it___Part]].md), [Filtra composto](Part_CompoundFilter/it.md), [Esplodi composto](Part_ExplodeCompound/it.md)---


</div>

## Introduzione

Questo comando crea un composto di qualsiasi tipo di forme topologiche. Questi possono essere solidi o mesh o qualsiasi altro tipo di forme topologiche.

Un composto è un insieme di forme raggruppate in un unico oggetto.


<div class="mw-translate-fuzzy">

## Utilizzo

Selezionare le forme topologiche da aggiungere al composto nella vista ad albero e poi usare il comando **Parte → Composto → Crea composto**


</div>

## Note

Un composto che contiene pezzi che si intersecano o si toccano **non è valido** per le operazioni booleane. A causa dei problemi di prestazioni per la Parte composta il controllo automatico sull\'intersezione delle parti non viene eseguito di default. Anche il controllo automatico delle geometrie disponibile per le operazioni booleane nel caso di parti composte non viene eseguito.

Per attivare questo controllo, andare in **Strumenti → Modifica parametri → Preferenze ... → Mod → Parte → CheckGeometry → RunBOPCheck** e impostare il parametro su `true`.


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Compound/it
