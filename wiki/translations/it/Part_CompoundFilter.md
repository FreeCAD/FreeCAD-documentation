---
- GuiCommand:/it
   Name:Part Compound‏‎Filter
   Name/it:Filtra composto
   MenuLocation:Part → Filtra composto
   Workbenches:[Part](Part_Workbench/it.md)
   Version:0.17
---

# Part CompoundFilter/it


</div>

![](images/CompoundFilter.png )

## Descrizione


<div class="mw-translate-fuzzy">

Il CompoundFilter può essere utilizzato per estrarre i singoli pezzi del risultato, ad es. di un\'operazione [Affetta di Part](Part_Slice/it.md), con cui è stato diviso un oggetto.


</div>

Può estrarre i figli dai loro indici, testare i figli per le collisioni con la forma dello matrice e filtrare i figli in base alle loro proprietà, come lunghezza, area, volume.

Se c\'è un solo figlio nel risultato, l\'output è il figlio. Se è presente più di un figlio, l\'output è un nuovo composto.

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare l\'oggetto affettato
2.  Applicare **Menu → Parte → Composto → Filtra composto**
3.  Selezionare il CompoundFilterObject nell\'albero
4.  Nella scheda delle proprietà impostare \"Filter Type\" su \"specific items\"
5.  Impostare le voci per gli elementi che si vuole estrarre
    1.  Per un singolo pezzo questo è un numero che inizia con 0, cioè se si vuole estrarre il primo elemento inserire 0 in questo campo, 1 per il successivo elemento \...
    2.  Se si desidera estrarre più di un pezzo alla volta, separare i numeri con \";\", ad es. un valore di \"0; 2\" estrae il primo e il terzo elemento
    3.  Il caso generale - che comprende anche le possibilità sopra menzionate - è un elenco di intervalli di indici, specificato in notazione Python, ma senza parentesi. Gli intervalli possono essere concatenati con punto e virgola. Per esempio:
        -   7:10 prende i figli degli indici 7, 8 e 9 (gli indici partono da zero, il limite superiore è escluso).
        -   1;2 prende i figli 1 e 2 (il primo intervallo è il figlio 1, il secondo intervallo è il figlio 2, gli intervalli sono uniti da punto e virgola)
        -   0;-1 prende il primo figlio (indice 0) e l\'ultimo (l\'indice -1 significa ultimo figlio, -2 significa l\'ultimo meno uno e così via)
        -   1: prende tutto tranne il primo figlio (l\'indice mancante significa \"fino alla fine\").
        -   ::-1 prende tutti i figli in ordine inverso
        -   ::2 prende tutti i figli con indicizzazione dispari, cioè gli indici, 1,3,5, \..., che sono gli elementi 2,4,6, \...
        -   :;: ripete due volte il composto di ingresso
6.  Se si vuole estrarre un altro pezzo selezionare nuovamente l\'oggetto affettato. Ora è posizionato sotto il CompoundFilter nell\'albero
7.  Ripetere dall\'inizio la procedura di selezione. La sezione e i suoi sottoelementi sono visualizzati in entrambi i CompoundFilters; naturalmente, non sono ripetuti nel modello. Un modo molto veloce per estrarre un nuovo pezzo è copiare il CompoundFilter. Ma **stare attenti**: viene chiesto se si vuole copiare gli elementi anche sotto il CompoundFilter, al che si deve rispondere con **no**, se non si vuole copiarli, ma fare solo riferimento.


</div>

## Proprietà

-    **Base**: oggetto da filtrare.

-    **Filter Type**opzioni selezionabili:

    -   bypass; senza Filtro. Viene emesso il composto originale, invariato.
    -   specific items; estrae gli oggetti elencati nella proprietà \"items\"
    -   collision-pass; estrae i pezzi che si toccano o intersecano con la forma \'Stencil\'.
    -   window-volume (default); estrae tutti i pezzi che hanno un volume compreso tra \"Window From\" e \"Window To\" dove 100% è il pezzo più grande - e non l\'oggetto non affettato. Il valore di 100% è un valore di riferimento che può essere sovrascritto in \"OverrideMaxVal\".
    -   window-area; lo stesso di window-volume, ma è l\'area affettata che determina la selezione anziché il volume.
    -   window-length; lo stesso di window-volume, ma è la lunghezza dei bordi che determina la selezione anziché il volume.
    -   window-distance; estrae i figli la cui distanza dalla forma \'Stencil\' è all\'interno della finestra dei valori, definita dalle proprietà \"WindowFrom\", \"WindowTo\", \"OverrideMaxVal\".

-    **Invert**: Se impostato su true, l\'elenco come sopra descritto è escluso anziché incluso.

-    **Override Max Val**: L\'intervallo della finestra di valori è definito in percentuale del valore massimo. Il valore massimo è calcolato in base al seguente insieme di regole:

    -   se \'OverrideMaxVal\' è diverso da zero - lo usa.
    -   altrimenti, se è fornito un collegamento a \'Stencil\' - calcola il valore corrispondente della forma dello stencil (non applicabile a \"FilterType\" window-distance)
    -   altrimenti, prende il massimo valore dai figli nel composto da filtrare.

-    **Stencil**: link a una forma stencil. Per i FilterType collision-pass e window-distance, lo stencil è l\'oggetto per testare la collisione o distanza. Per altri tipi di filtri \"window - \*\*\*\", lo stencil viene utilizzato per fornire un valore di riferimento per le percentuali delle finestre (valore massimo ignorato). In tutte le altre modalità, \"Stencil\" viene ignorato.

-    **Window From**: percentuale di soglia superiore per la selezione dei pezzi, 100% è relativo al pezzo più grande.

-    **Window To**: percentuale di soglia inferiore per la selezione dei pezzi, 100% è relativo al pezzo più grande.

-    **items**: Elenco o intervallo di elementi da selezionare se Filter Type è \"specific items\".



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part CompoundFilter/it
