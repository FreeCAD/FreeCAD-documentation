---
 GuiCommand:
   Name: Draft LayerManager
   Name/it: Draft Gestore dei livelli
   MenuLocation: Utilità , Gestione livelli...
   Workbenches: Draft_Workbench/it, Arch_Workbench/it
   Version/it: 0.21
   SeeAlso: BIM_Workbench/it, Draft_Layer/it
---

# Draft LayerManager/it



## Descrizione

Il gestore dei livelli consente di gestire i [livelli](Draft_Layer/it.md) (layer). I livelli sono un tipo speciale di gruppo che controlla le proprietà visive degli oggetti posizionati al suo interno. Modificando le proprietà del Livello, come larghezza della linea, colore della linea, colore della forma e trasparenza, le modifiche vengono propagate ai suoi oggetti figli. I livelli non interferiscono con nessun\'altra struttura di FreeCAD come [gruppi](Std_Group/it.md) o [Parti edificio](Arch_BuildingPart/it.md), quindi qualsiasi oggetto può essere allo stesso tempo parte di un livello e parte di un gruppo. I livelli vengono sempre mantenuti automaticamente in uno speciale gruppo \"Livelli\".

<img alt="" src=images/BIM_layers_screenshot.png  style="width:400px;">

I livelli vengono importati ed esportati da/a [IFC](Arch_IFC/it.md) e [DXF/DWG](Draft_DXF/it.md).

Il gestore dei livello consente di gestire i livelli, aggiungerli e rimuoverli o modificare le loro proprietà visive. Per aggiungere oggetti a un livello, trascinarli semplicemente nel livello nella vista ad albero. Per rimuoverli, trascinarli dal livello e rilasciali nella radice del documento.



## Utilizzo

Da completare



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft LayerManager/it
