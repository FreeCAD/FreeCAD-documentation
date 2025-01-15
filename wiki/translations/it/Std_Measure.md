---
 GuiCommand:
   Name: Std Measure
   Name/it: Misurare
   MenuLocation: Strumenti , Misurare
   Workbenches: Tutti
   Version: 1.0
   SeeAlso: Draft_Dimension/it
---

# Std Measure/it



## Descrizione

Il comando **Misurare** dà accesso al Unified Measurement Facility. Esso ha sostituito alcuni precedenti comandi di misurazione, fornendo una funzionalità di misurazione versatile.



## Utilizzo

1.  Opzionalmente preselezionare le entità da misurare.
2.  Esistono diversi modi per richiamare il comando:
    -   Premere il pulsante **<img src="images/Std_Measure.svg" width=16px> [Misurare](Std_Measure/it.md)**.
    -   Selezionare l\'opzione **Strumenti → <img src="images/Std_Measure.svg" width=16px> Misurare** dal menu.
3.  Si apre il pannello delle attività **Misurazione**. Vedere [Opzioni](#Opzioni.md) per ulteriori informazioni.
4.  Se non è stata preselezionata alcuna entità geometrica, eseguire una delle seguenti operazioni:
    -   Selezionare le entità geometriche lasciando la *Modalità* su *Auto* in modo che la modalità venga determinata automaticamente in base alla selezione.
    -   Scegliere una *Modalità* diversa da *Auto* e poi seleziona le entità geometriche (cliccando nuovamente su di esse saranno deselezionate):
        -   *Distanza* - la distanza più breve tra le entità selezionate, se vengono selezionati bordi circolari viene misurata la distanza tra i centri dei cerchi,
        -   *Distanza libera* - distanza tra due punti liberamente selezionati (appartenenti a entità diverse - bordi, facce),
        -   *Angolo* - angolo tra le entità selezionate,
        -   *Lunghezza* - lunghezza del bordo selezionato,
        -   *Posizione* - coordinate del vertice selezionato,
        -   *Area* - area del volto selezionato,
        -   *Raggio* - raggio del bordo circolare selezionato,
        -   *Centro di massa* - CdM del bordo, faccia o solido selezionato (solo se preselezionato nell\'albero).
5.  Il risultato della misurazione verrà mostrato nel campo *Risultato* e su un\'etichetta visualizzata nella [Vista 3D](3D_view/it.md). Tale etichetta includerà anche un\'icona che indica il tipo di misurazione. Le etichette possono essere personalizzate nell\'[Editor Preferenze](Preferences_Editor/it.md). Possono essere spostate nella vista 3D trascinandole con un cursore.
6.  Premere il pulsante **Reset** per eliminare la misurazione o il pulsante **Salva** per conservarla. Le misurazioni salvate vengono inserite in un [gruppo](Std_Group/it.md) di misurazioni nella [Vista ad albero](Tree_view/it.md).
7.  Premere **Esc** o il pulsante **Close** per terminare il comando.



## Opzioni

-    {{Version/it|1.1}}Premere il pulsante **<img src="images/Preferences-system.svg" width=x16px> <img src="images/Toolbar_flyout_arrow.svg" width=x16px>** per modificare le impostazioni:

    -   *Salvataggio automatico* - se selezionato, l\'ultima misurazione viene salvata quando si avvia una nuova misurazione (tenendo premuto **Shift** è possibile disattivare temporaneamente questo comportamento),
    -   *Selezione additiva* - se selezionato, cliccando sulle entità geometriche successive le aggiunge come selezioni per la stessa misura, altrimenti è necessario premere **Ctrl** per farlo.

-   Per le modalità *Distanza* e *Distanza libera* viene visualizzata la casella di controllo **Mostra Delta**. Se questa casella di controllo è selezionata, la proprietà **Mostra Delta** della misurazione è impostata su `True` e 3 misurazioni proiettate aggiuntive vengono mostrate nella [Vista 3D](3D_view/it.md).



## Proprietà



### Dati


{{TitleProperty|Measurement}}


<div class="mw-translate-fuzzy">

-    **Element1|LinkSub**: Primo elemento della misurazione.

-    **Element2|LinkSub**: Secondo elemento della misurazione.

-    **Distance|Distance**: Distanza tra i due elementi.

-    **Distance X|Distance**: Distanza nella direzione X (solo per misurazioni *Distanza* e *Distanza libera*).

-    **Distance Y|Distance**: Distanza nella direzione Y (stessa).

-    **Distance Z|Distance**: Distanza nella direzione Z (stessa).

-    **Position1|Vector|Hidden**: Posizione del primo punto misurato (sola lettura).

-    **Position2|Vector|Hidden**: Posizione del secondo punto misurato (sola lettura).


</div>



### Vista


{{TitleProperty|Appearance}}

-    **Font Size|Integer**: Definisce la dimensione del carattere per l\'etichetta della dimensione salvata.

-    **Line Color|Color**: Definisce il colore delle linee di quota visualizzate nella vista 3D.

-    **Show Delta|Bool**: Se `True`, le misurazioni della distanza proiettata vengono visualizzate nella vista 3D (solo per le misurazioni *Distanza* e *Distanza libera*).

-    **Text Background Color|Color**: Definisce il colore di sfondo dell\'etichetta della dimensione.

-    **Text Color|Color**: Definisce il colore del testo e del simbolo dell\'etichetta della quota.



## Note

-   Questo comando è il risultato di un [Progetto GSoC 2023](Unified_Measurement_Facility.md).



---
⏵ [documentation index](../README.md) > Std Measure/it
