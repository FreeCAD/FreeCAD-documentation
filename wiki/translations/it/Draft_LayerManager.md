---
 GuiCommand:
   Name: Draft LayerManager
   Name/it: Draft Gestore dei layer
   MenuLocation: Utilità , Gestione layer...
   Workbenches: Draft_Workbench/it
   Version/it: 0.21
   SeeAlso: BIM_Workbench/it, Draft_Layer/it
---

# Draft LayerManager/it



## Descrizione

Il gestore dei layer consente di gestire i [layer](Draft_Layer/it.md). I layer sono un tipo speciale di gruppo che controlla le proprietà visive degli oggetti posizionati al suo interno. Modificando le proprietà del Layer, come spessore della linea, colore della linea, colore della forma e trasparenza, le modifiche vengono propagate ai suoi oggetti figli. I layer non interferiscono con nessun\'altra struttura di FreeCAD come [gruppi](Std_Group/it.md) o [Parti edificio](Arch_BuildingPart/it.md), quindi qualsiasi oggetto può essere allo stesso tempo parte di un layer e parte di un gruppo. I layer vengono sempre mantenuti automaticamente in uno speciale gruppo \"Layer\".

<img alt="" src=images/BIM_layers_screenshot.png  style="width:400px;">

I layer vengono importati ed esportati da/a [IFC](Arch_IFC/it.md) e [DXF/DWG](Draft_DXF/it.md).

Il gestore dei layer consente di gestire i layer, aggiungerli e rimuoverli o modificare le loro proprietà visive. Per aggiungere oggetti a un layer, trascinarli semplicemente nel layer nella vista ad albero. Per rimuoverli, trascinarli dal layer e rilasciali nella radice del documento.



## Utilizzo

Da completare



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft LayerManager/it
