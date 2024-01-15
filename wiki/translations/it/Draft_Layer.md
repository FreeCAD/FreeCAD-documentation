---
 GuiCommand:
   Name: Draft Layer
   Name/it: Livello
   Workbenches: Draft_Workbench/it, Arch_Workbench/it
   MenuLocation: Draft , Utilità , Livello
   Version: 0.19
   See also: Draft_AutoGroup/it
---

# Draft Layer/it



## Descrizione

Il comando <img alt="" src=images/Draft_Layer.svg  style="width:24px;"> **Draft Livello** crea un livello Draft (Layer). Un livello è un tipo speciale di gruppo con un numero di [proprietà visive](#View.md). Queste proprietà e qualsiasi modifica apportata ad esse vengono propagate agli oggetti posizionati all\'interno del livello. I livelli stessi vengono inseriti in un altro gruppo speciale: Draft LayerContainer.



## Utilizzo

1.  Esistono diversi modi per richiamare il comando:
    -   Premere il pulsante **<img src="images/Draft_Layer.svg" width=16px> [Livello](Draft_Layer/it.md)**.
    -   Selezionare l\'opzione **Utilità → <img src="images/Draft_Layer.svg" width=16px> Livello** dal menu.
    -   Se il contenitore del livello esiste già: fare clic con il tasto destro del mouse nella [Vista ad albero](Tree_view/it.md) e selezionare l\'opzione **<img src="images/Draft_NewLayer.svg" width=16px> Aggiungi nuovo livello** dal menu contestuale .
2.  Se non esiste, viene creato prima il contenitore del livello.
3.  Viene creato un livello e inserito nel contenitore del livello.
4.  Facoltativamente modificare le [proprietà](#Properties.md) del livello.
5.  Facoltativamente, inserire gli oggetti nel livello trascinandoli sul livello nella [Vista ad albero](Tree_view/it.md). Gli oggetti possono anche essere inseriti in un livello modificando la proprietà **Group** del livello.
6.  Facoltativamente [attivare](#Layer_options.md) il livello.



## Menu contestuale 



### Opzioni del contenitore di livelli 

Per un Draft LayerContainer queste opzioni aggiuntive sono disponibili nel menu contestuale [Vista ad albero](Tree_view/it.md):

-    **<img src="images/Draft_Layer.svg" width=16px> Unisci livelli duplicati**: unisce tutti i livelli con la stessa etichetta di base.

:   L\'etichetta di base di un livello è la sua **Label** privata delle cifre finali e degli spazi. Tutti i livelli con la stessa etichetta di base vengono uniti in un singolo livello con **Label** impostato su quell\'etichetta di base.

-    **<img src="images/Draft_NewLayer.svg" width=16px> Aggiungi nuovo livello**: aggiunge un nuovo livello al documento corrente.



### Opzioni dei livelli 

Per un livello Draft queste opzioni aggiuntive sono disponibili nel menu contestuale [Vista ad albero](Tree_view/it.md):

-    **<img src="images/button_right.svg" width=16px> [Attiva questo livello](Draft_AutoGroup/it.md)**: attiva il livello selezionato.

-    **<img src="images/Draft_SelectGroup.svg" width=16px> [Seleziona contenuto livello](Draft_SelectGroup/it.md)**: seleziona gli oggetti all\'interno del livello selezionato.



## Comportamento trascina e rilascia 


{{Version/it|0.21}}

Se si rilascia un oggetto da un [ Gruppo](Std_Group/it.md), o un oggetto simile a un gruppo come un [Parte di edificio Arch](Arch_BuildingPart/it.md), su un livello nella [Vista ad albero](Tree_view/it.md), è non rimosso dal gruppo e viceversa. Per rimuovere un oggetto da un livello è necessario rilasciarlo su un altro livello o sul nodo del documento. Non è necessario tenere premuto il tasto **Ctrl** durante il trascinamento o il rilascio su un livello.



## Note

-   È anche possibile creare un nuovo livello con il comando [Draft Gruppo automatico](Draft_AutoGroup/it.md).
-   L\'[Ambiente BIM](BIM_Workbench/it.md) offre uno [strumento di gestione dei livelli](BIM_Layers/it.md) completo che verrà eventualmente incluso nell\'[Ambiente Draft](Draft_Workbench/it.md).



## Proprietà

Vedere anche: [Editor delle proprietà](Property_editor/it.md).

Un oggetto Draft Livello deriva da un oggetto [App FeaturePython](App_FeaturePython/it.md) e ne eredita tutte le proprietà. Ha inoltre le seguenti proprietà aggiuntive:



### Dati


{{TitleProperty|Layer}}

-    **Group|LinkList**: specifica gli oggetti che si trovano all\'interno del livello.



### Vista


{{TitleProperty|Layer}}

Le proprietà in questa sezione vengono applicate agli oggetti inseriti all\'interno del livello. E qualsiasi modifica a queste proprietà viene propagata a loro. Per due proprietà, **Line Color** e **Shape Color**, questo comportamento è facoltativo.

-    **Draw Style|Enumeration**: specifica lo stile di disegno del livello: {{value|Solid}}, {{value|Dashed}}, {{value|Punteggiato}} o {{value|Dashdot} }
    * **Line Color|Color**: specifica il colore della linea del livello.
    * **Line Width|Float**: specifica la larghezza della linea del livello.
    * **Override Line Color Children|Bool**: specifica se le modifiche al **Line Color** del livello vengono propagate agli oggetti all'interno del livello.
    * **Override Shape Color Children|Bool**: specifica se le modifiche a **Shape Color** del livello vengono propagate agli oggetti all'interno del livello.
    * **Shape Color|Color**: specifica il colore della forma del livello.
    * **Transparency|Percent**: specifica la trasparenza del livello.

    {{TitleProperty|Print}}

    * **Line Print Color|Color**: specifica il colore di stampa della linea del livello.
    * **Use Print Color|Bool**: specifica se il **Line Print Color|** del livello viene utilizzato quando una [TechDraw Vista di Draft](TechDraw_DraftView/it.md) viene creata dagli oggetti interni al livello.

    <span id="Scripting"></span>
    ==Script==

    Vedere anche: [https://freecad.github.io/SourceDoc/ Autogenerated API documentation] e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

    Per creare un livello Draft utilizzare il metodo `make_layer` del modulo Draft. Per aggiungere o rimuovere oggetti da un livello, modificare la sua proprietà `Group`.

    
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
