---
 GuiCommand:
   Name: Draft Layer
   Name/it: Draft Layer
   Workbenches: Draft_Workbench/it
   MenuLocation: Draft , Utilità , Layer
   Version: 0.19
   See also: Draft_AutoGroup/it, Draft_LayerManager/it
---

# Draft Layer/it



## Descrizione

Il comando <img alt="" src=images/Draft_Layer.svg  style="width:24px;"> **Draft Layer** crea un layer Draft. Un layer è un tipo speciale di gruppo con un numero di [proprietà visive](#View.md). Queste proprietà e qualsiasi modifica apportata ad esse vengono propagate agli oggetti posizionati all\'interno del layer. I layer stessi vengono inseriti in un altro gruppo speciale: Draft LayerContainer.



## Utilizzo

1.  Esistono diversi modi per richiamare il comando:
    -   Premere il pulsante **<img src="images/Draft_Layer.svg" width=16px> [Layer](Draft_Layer/it.md)**.
    -   Selezionare l\'opzione **Utilità → <img src="images/Draft_Layer.svg" width=16px> Layer** dal menu, o dalla [Vista ad albero](Tree_view/it.md) o dal menu contestuale della [Vista 3D](3D_view/it.md).
    -   Se il contenitore del layer esiste già: fare clic con il tasto destro del mouse nella [Vista ad albero](Tree_view/it.md) e selezionare l\'opzione **<img src="images/Draft_NewLayer.svg" width=16px> Aggiungi nuovo layer** dal menu contestuale .
2.  Se non esiste, viene creato prima il contenitore del layer.
3.  Viene creato un layer e inserito nel contenitore del layer.
4.  Facoltativamente modificare le [proprietà](#Properties.md) del layer.
5.  Facoltativamente, inserire gli oggetti nel layer trascinandoli sul layer nella [Vista ad albero](Tree_view/it.md). Gli oggetti possono anche essere inseriti in un layer modificando la proprietà **Group** del layer.
6.  Facoltativamente [attivare](#Layer_options.md) il layer.



## Menù contestuale 



### Opzioni del contenitore dei layer 

Per un Draft LayerContainer queste opzioni aggiuntive sono disponibili nel menu contestuale [Vista ad albero](Tree_view/it.md):

-    **<img src="images/Draft_Layer.svg" width=16px> Unisci layer duplicati**: unisce tutti i layer con la stessa etichetta di base.

:   L\'etichetta di base di un layer è la sua **Label** privata delle cifre finali e degli spazi. Tutti i layer con la stessa etichetta di base vengono uniti in un singolo layer con **Label** impostato su quell\'etichetta di base.

-    **<img src="images/Draft_NewLayer.svg" width=16px> Aggiungi nuovo layer**: aggiunge un nuovo layer al documento corrente.



### Opzioni dei layer 

Per un layer Draft queste opzioni aggiuntive sono disponibili nel menu contestuale [Vista ad albero](Tree_view/it.md):

-    **<img src="images/button_right.svg" width=16px> [Attiva questo layer](Draft_AutoGroup/it.md)**: attiva il layer selezionato.

-    **<img src="images/Draft_SelectGroup.svg" width=16px> [Seleziona contenuto layer](Draft_SelectGroup/it.md)**: seleziona gli oggetti all\'interno del layer selezionato.



## Comportamento trascina e rilascia 


{{Version/it|0.21}}

Se si rilascia un oggetto da un [ Gruppo](Std_Group/it.md), o un oggetto simile a un gruppo come un [Parte di edificio Arch](Arch_BuildingPart/it.md), su un layer nella [Vista ad albero](Tree_view/it.md), è non rimosso dal gruppo e viceversa. Per rimuovere un oggetto da un layer è necessario rilasciarlo su un altro layer o sul nodo del documento. Non è necessario tenere premuto il tasto **Ctrl** durante il trascinamento o il rilascio su un layer.



## Note

-   È anche possibile creare un nuovo layer con il comando [Draft Gruppo automatico](Draft_AutoGroup/it.md).
-   L\'[Ambiente BIM](BIM_Workbench/it.md) offre uno [strumento di gestione dei layer](BIM_Layers/it.md) completo che verrà eventualmente incluso nell\'[Ambiente Draft](Draft_Workbench/it.md).



## Proprietà

Vedere anche: [Editor delle proprietà](Property_editor/it.md).

Un oggetto Draft Layer deriva da un oggetto [App FeaturePython](App_FeaturePython/it.md) e ne eredita tutte le proprietà. Ha inoltre le seguenti proprietà aggiuntive:



### Dati


{{TitleProperty|Layer}}

-    **Group|LinkList**: specifica gli oggetti che si trovano all\'interno del layer.



### Vista


{{TitleProperty|Layer}}

Le proprietà in questa sezione vengono applicate agli oggetti inseriti all\'interno del layer. Qualsiasi modifica a queste proprietà gli viene propagata. Per due proprietà, **Line Color** e **Shape Color**, questo comportamento è facoltativo.

-    **Draw Style|Enumeration**: specifica lo stile di disegno del layer: {{value|Solid}}, {{value|Dashed}}, {{value|Punteggiato}} o {{value|Dashdot}}

-    **Line Color|Color**: specifica il colore della linea del layer.

-    **Line Width|Float**: specifica la larghezza della linea del layer.

-    **Override Shape Appearance Children|Bool**: specifica se le modifiche a **Shape Appearance** del layer vengono propagate agli oggetti all\'interno del layer, {{Version/it|1.0}}.

-    **Override Shape Color Children|Bool**: specifica se le modifiche a **Shape Color** del layer vengono propagate agli oggetti all\'interno del layer.

-    **Shape Appearance|MaterialList**: specifica l\'aspetto della forma del layer, {{Version/it|1.0}}.

-    **Shape Color|Color|hidden**: specifica il colore della forma del layer. Viene mantenuto sincronizzato con **Diffuse Color** di **Shape Appearance**.

-    **Transparency|Percent**: specifica la trasparenza del layer. Viene mantenuto sincronizzato con **Transparency** di **Shape Appearance**.


{{TitleProperty|Print}}

-    **Line Print Color|Color**: specifica il colore di stampa della linea del layer.

-    **Use Print Color|Bool**: specifica se il **Line Print Color|** del layer viene utilizzato quando una [TechDraw Vista di Draft](TechDraw_DraftView/it.md) viene creata dagli oggetti interni al layer.



## Script

Vedere anche: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Per creare un Layer Draft utilizzare il metodo `make_layer` del modulo Draft. Per aggiungere o rimuovere oggetti da un layer, modificare la sua proprietà `Group`.


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

layer = Draft.make_layer(line_color=(1.0, 0.0, 0.0, 0.0),
                         shape_color=(1.0, 1.0, 0.0, 0.0))

polygon1 = Draft.make_polygon(5, radius=1000)
polygon2 = Draft.make_polygon(3, radius=500)
polygon3 = Draft.make_polygon(6, radius=220)
layer.Group = [polygon1, polygon2, polygon3]

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Layer/it
