---
 GuiCommand:
   Name: Arch_MultiMaterial
   Name/it: Arch MultiMaterial
   MenuLocation: Arch , Strumenti materiale , Multi-materiale
   Workbenches: Arch_Workbench/it, BIM Workbench/it
   SeeAlso: Arch SetMaterial/it, Arch CompSetMaterial/it
---

# Arch MultiMaterial/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento Multi-materiale definisce una lista di [materiali](Material.md) con un nome e un valore di spessore per ogni materiale. Quindi, questo elenco di multi-materiali può essere aggiunto a un oggetto [Arch](Arch_Workbench/it.md) al posto di un [Materiale di Arch](Arch_SetMaterial/it.md) .


</div>

![](images/Arch_multimaterial_example.png )

Non tutti gli oggetti Arch possono utilizzare i multi-materiali, e l\'utilizzo che ne fanno è diverso. Attualmente:

-   <img alt="" src=images/Arch_Wall.svg  style="width:24px;"> [Muro](Arch_Wall/it.md) con una Multi-materiale utilizza le definizioni dei materiali e gli spessori per creare una parete multistrato
-   <img alt="" src=images/Arch_Window.svg  style="width:24px;"> [Finestra](Arch_Window/it.md) con un Multi-materiale attribuisce i materiali con un nome specificato all\'interno del Multi-materiale ai componenti della finestra con lo stesso nome, o dello stesso tipo (vedere sotto). Lo spessore del materiale non viene considerato.
-   <img alt="" src=images/Arch_Panel.svg  style="width:24px;"> [Pannello](Arch_Panel/it.md) con una Multi-materiale utilizza le definizioni dei materiali e gli spessori per creare un pannello multistrato

## Uso

1.  Creare prima la serie di <img alt="" src=images/Arch_SetMaterial.svg  style="width:16px;"> [Materiali Arch](Arch_SetMaterial/it.md) che sono necessari nel Multi-materiale
2.  Facoltativamente, selezionare un oggetto Arch a cui si desidera attribuire il nuovo Multi-materiale
3.  Premere il pulsante **<img src="images/Arch_MultiMaterial.svg" width=16px> [Multi-materiale](Arch_MultiMaterial/it.md)
**
4.  Impostare gli strati di materiale desiderati

## Opzioni

![](images/Arch_multimaterial_panel.png )

Quando si crea o si modifica un multi-materiale facendo doppio clic sull\'albero, sono disponibili le seguenti opzioni:

-   **Duplicate** un altro Multi-materiale esistente dello stesso documento. Questo copia solo i valori dall\'originale e non lega i due multi-materiali in alcun modo.
-   Il campo **Name** imposta anche l\'etichetta dell\'oggetto materiale
-   **Composition** è l\'elenco dei diversi strati di materiali che compongono questo multi-materiale. Ogni strato ha un nome, un materiale e un valore di spessore.
-   Cliccare **Add** per aggiungere un nuovo strato, **Up** per spostare in alto uno strato selezionato, **Down** per spostare in basso uno strato selezionato, o **Del** per eliminare uno strato selezionato.
-   Facendo doppio-click sul **name** di uno strato per modificarlo, il materiale offre un elenco a discesa dei [Materiali Arch](Arch_SetMaterial/it.md) disponibili nello stesso documento, e lo spessore può essere impostato su qualsiasi valore in qualsiasi unità
-   I campi del nome e del materiale sono obbligatori. Lo spessore può essere lasciato vuoto (adotta quindi un valore di 0).
-   Quando un multi-materiale contiene strati con uno spessore di zero, lo spessore è considerato variabile. Gli oggetti Arch che utilizzano il multi-materiale, come i muri e i pannelli, lo trattano di conseguenza e danno a tale strato lo spazio rimanente disponibile, data la propria larghezza o spessore.
-   Se si nominano i diversi componenti di un multi-materiale \"Telaio\", \"Pannello solido\", \"Pannello vetro\" o \"Persiana\" e si applica quel materiale a una finestra, i materiali assegnati vengono applicati ai corrispondenti componenti della finestra.

## Relazione con IFC 


<div class="mw-translate-fuzzy">

Ciò corrisponde approssimativamente a una combinazione di [IfcMaterialLayerSet](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/link/ifcmateriallayerset.htm) e [IfcMaterialLayer](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/link/ifcmateriallayer.htm).


</div>

## Limitazioni

## Script


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch MultiMaterial/it
