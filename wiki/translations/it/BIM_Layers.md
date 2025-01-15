---
 GuiCommand:Addon/it
   Name: BIM Layers
   Name/it: Strati BIM
   Workbenches: BIM Workbench/it
   Addon: BIM
   MenuLocation: Gestione , Strati
---

# BIM Layers/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Il gestore dei layer ti permette di gestire i [layer](Draft_Layer/it.md). I layer sono un tipo speciale di gruppo che controlla le proprietà visive degli oggetti posizionati al suo interno. Modificando le proprietà del layer, come la larghezza della linea, il colore della linea, il colore della forma e la trasparenza, le modifiche vengono propagate ai suoi oggetti figlio. I layer non interferiscono con nessun\'altra struttura di FreeCAD come [gruppi](Std_Group/it.md) o [Parti di edificio](Arch_BuildingPart/it.md), quindi qualsiasi oggetto può essere allo stesso tempo parte di un layer e parte di un gruppo.


</div>

<img alt="" src=images/BIM_layers_screenshot.png  style="width:600px;"> 
*Layers manager*


<div class="mw-translate-fuzzy">

I layer vengono importati ed esportati da/a [IFC](Arch_IFC/it.md) e [DXF/DWG](Draft_DXF/it.md).


</div>


<div class="mw-translate-fuzzy">

Il gestore dei layer consente di gestire i tuoi layer, aggiungerli e rimuoverli o modificare le loro proprietà visive. Per aggiungere oggetti a un layer, trascinali semplicemente nel layer nella vista ad albero. Per rimuoverli, trascinali dal layer e rilasciali nella radice del documento.


</div>

## NativeIFC

This tool is the exact same as the [Draft LayerManager](Draft_LayerManager.md) tool, and creates the same layer object. There is only one difference: It has support for [NativeIFC](NativeIFC.md) objects:

-   An IFC icon will indicate if a layer is part of an IFC project or not
-   An **Assign IFC** button allows to move a layer to an IFC project and with that turn it into an IFC layer



---
⏵ [documentation index](../README.md) > [BIM](BIM_Workbench.md) > BIM Layers/it
