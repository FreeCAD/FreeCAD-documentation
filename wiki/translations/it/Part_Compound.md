---
 GuiCommand:
   Name: Part Compound‏‎
   Name/it: Part crea un composto
‏‎   MenuLocation: Parte , Crea un composto
   Workbenches: Part Workbench/it
   Version: 0.14
   SeeAlso: Part_Fuse/it, Part CompoundFilter/it, Part ExplodeCompound/it
---

# Part Compound/it



## Descrizione

Questo comando crea un composto di oggetti con forma topologica come oggetti solidi e altri oggetti con facce e/o bordi. Non può gestire le mesh poiché non hanno una forma topologica.



## Utilizzo

1.  Contrassegnare le forme topologiche da aggiungere al composto nella [vista ad albero](Tree_view/it.md)
2.  Scegliere la voce **Parte → Composto → Crea composto** nel menu Parte o fare clic sul pulsante <img alt="" src=images/Part_Compound.svg  style="width:24px;">.



## Note

Un composto contenente pezzi che si intersecano o si toccano non è **valido** per le operazioni booleane. A causa di problemi di prestazioni, il controllo se i pezzi si intersecano non viene eseguito per impostazione predefinita. Il controllo automatico della geometria (disponibile per le operazioni booleane) è disabilitato anche per il composto di parti.

Per attivare questo controllo andare su **Strumenti → Modifica parametri → Preferences... → Mod → Part → CheckGeometry → RunBOPCheck** e impostare il parametro su `true`.





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Compound/it
