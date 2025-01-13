# <img alt="Icona dell\'Ambiente Fasteners" src=images/Fasteners_workbench_icon.svg  style="width:64px;"> Fasteners Workbench/it






## Introduzione

<img alt="" src=images/Fasteners_workbench_icon.svg  style="width:24px;"> [L\'Ambiente Fasteners](Fasteners_Workbench.md) è un [ambiente di lavoro complementare](External_workbench.md) con cui aggiungere vari elementi di fissaggio alle parti.

<img alt="" src=images/Fasteners_Toolbars.png  style="width:500px;"> 
*Il layout opzionale della barra singola dell'ambiente di lavoro.<br>
Gli elementi di fissaggio con dimensioni metriche hanno icone arancioni.<br>
Gli elementi di fissaggio con dimensioni in pollici hanno icone verdi.*



## Installazione

1.  Installare l\'Ambiente Fasteners tramite <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr/it.md). Per l\'installazione manuale vedere [Installare ulteriori ambienti di lavoro](Installing_more_workbenches/it.md).
2.  Riavviare FreeCAD.
3.  Selezionare <img alt="" src=images/Fasteners_workbench_icon.svg  style="width:24px;"> [Fasteners Workbench](Fasteners_Workbench/it.md) dall\'elenco a discesa degli [Ambienti di lavoro](Std_Workbench/it.md).
4.  Facoltativamente, modificare la barra degli strumenti e il layout del menu:
    1.  Andare su: **Modifica → Preferenze... → Fasteners → General settings**.
    2.  Selezionare una delle opzioni disponibili di **Toolbar screw icons grouping**:
        -   
            **None**
            
            : tutti gli elementi di fissaggio vengono visualizzati in un\'unica barra degli strumenti. Per vedere tutti i pulsanti disponibili, utilizzare il pulsante **&gt;&gt;** per mostrarli.

        -   
            **Separate toolbars**
            
            : gli elementi di fissaggio sono raggruppati in diverse barre degli strumenti. Questo è il layout predefinito.

        -   
            **Dropdown buttons**
            
            : gli elementi di fissaggio sono raggruppati in barre degli strumenti con spunte.
    3.  Facoltativamente deselezionare una o più opzioni **Fastener standards shown in toolbars**. I componenti standard non selezionati saranno ancora disponibili nel menu.
    4.  Riavviare FreeCAD.



## Utilizzo

Gli elementi di fissaggio possono essere attaccati o staccati. Gli elementi di fissaggio attaccati hanno un **Base Object**, un bordo circolare e il loro **Placement** è collegato dinamicamente a quell\'oggetto. Il comando <img alt="" src=images/Fasteners_Move.svg  style="width:16px;"> [Muovi di Fasteners](Fasteners_Move/it.md) può essere utilizzato per attaccare o staccare un elemento di fissaggio.



### Elementi di fissaggio staccati 

1.  Selezionare l\'elemento di fissaggio desiderato facendo clic sul relativo pulsante o selezionandolo dal menu.
2.  Un elemento di fissaggio viene creato all\'origine.
3.  Facoltativamente modificare le dimensioni e altre proprietà dell\'elemento di fissaggio:
    1.  Selezionare il dispositivo di fissaggio.
    2.  Andare alla scheda **Data** dell\'[Editor delle proprietà](Property_editor/it.md).
    3.  Modificare le proprietà ai valori richiesti.



### Elementi di fissaggio attaccati 

<img alt="" src=images/Fasteners_Attached_Selected.png  style="width:200px;"> <img alt="" src=images/Fasteners_Attached_Created.png  style="width:200px;"> 
*A sinistra i due bordi circolari selezionati. A destra gli elementi di fissaggio attaccati.*

1.  Specificare se i fori selezionati sono fori filettati o fori passanti selezionando <img alt="" src=images/Fasteners_MatchTypeInner.svg  style="width:16px;"> [Fasteners MatchTypeInner](Fasteners_MatchTypeInner/it.md) o <img alt="" src=images/Fasteners_MatchTypeOuter.svg  style="width:16px;"> [Fasteners MatchTypeOuter](Fasteners_MatchTypeOuter/it.md) rispettivamente (non utilizzato per viti a testa svasata).
2.  Selezionare uno o più bordi circolari e/o facce con bordi circolari. Per le viti a testa svasata è necessario selezionare il bordo superiore del foro smussato.
3.  Selezionare l\'elemento di fissaggio desiderato facendo clic sul relativo pulsante o selezionandolo dal menu.
4.  Un elemento di fissaggio è attaccato a ciascuno dei bordi circolari selezionati.
5.  Le dimensioni predefinite di ciascun elemento di fissaggio dipendono dal raggio del bordo circolare a cui è attaccato. Le viti a testa svasata sono abbinate al diametro della testa, gli altri elementi di fissaggio sono abbinati al diametro dell\'albero.
6.  Facoltativamente modificare le dimensioni e altre proprietà degli elementi di fissaggio. Vedere sopra.
7.  Gli elementi di fissaggio che appaiono capovolti possono essere invertiti con il comando <img alt="" src=images/Fasteners_Flip.svg  style="width:16px;"> [Fasteners Flip](Fasteners_Flip/it.md) o modificando la loro proprietà **Invert**.
8.  Facoltativamente, modificare la proprietà **Offset** per creare spazio tra gli elementi di fissaggio e i bordi a cui sono attaccati.



## Note

-   Per generare le filettature, la proprietà **Thread** di un elemento di fissaggio deve essere modificata in `True`. La generazione di thread è onerosa. Il ricalcolo richiede molto più tempo se in un documento sono presenti molti elementi di fissaggio con filettature.
-   La proprietà **Invert** e la proprietà **Offset** vengono ignorate per gli elementi di fissaggio non attaccati.



## Comandi

-   <img alt="" src=images/Fasteners_Flip.svg  style="width:32px;"> [Invert fastener](Fasteners_Flip/it.md): Inverte l\'orientamento degli elementi di fissaggio attaccati.

-   <img alt="" src=images/Fasteners_Move.svg  style="width:32px;"> [Move fastener](Fasteners_Move/it.md): Sposta e attacca un elemento di fissaggio a un bordo circolare. Può essere utilizzato anche per staccare un elemento di fissaggio.

-   <img alt="" src=images/Fasteners_Simplify.svg  style="width:32px;"> [Simplify shape](Fasteners_Simplify/it.md): Crea copie non parametriche degli elementi di fissaggio.

-   <img alt="" src=images/Fasteners_MatchTypeInner.svg  style="width:32px;"> [Match for tap hole](Fasteners_MatchTypeInner/it.md): Considera i bordi circolari come fori maschiati quando ad essi vengono attaccati nuovi elementi di fissaggio.

-   <img alt="" src=images/Fasteners_MatchTypeOuter.svg  style="width:32px;"> [Match for pass hole](Fasteners_MatchTypeOuter/it.md): Considera i bordi circolari come fori passanti quando ad essi vengono attaccati nuovi elementi di fissaggio.

-   <img alt="" src=images/Fasteners_BOM.svg  style="width:32px;"> [Generate BOM](Fasteners_BOM/it.md): Crea un foglio di calcolo con una distinta materiali per gli elementi di fissaggio nel documento.

-   <img alt="" src=images/Fasteners_ScrewCalculator.svg  style="width:32px;"> [Screw calculator](Fasteners_ScrewCalculator/it.md): Mostra una calcolatrice per determinare la dimensione del preforo delle viti.

-   <img alt="" src=images/Fasteners_ChangeParameters.svg  style="width:32px;"> [Change fastener parameters](Fasteners_ChangeParameters/it.md): Modifica i parametri degli elementi di fissaggio.



## Elementi di fissaggio 

Gli elementi di fissaggio con dimensioni metriche hanno icone arancioni. Gli elementi di fissaggio con dimensioni in pollici hanno icone verdi.



### Viti e bulloni a testa esagonale 

-   <img alt="" src=images/Fasteners_ASMEB18.2.1.6.svg  style="width:32px;"> **ASME B18.2.1.6** vite a testa esagonale UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.2.1.8.svg  style="width:32px;"> **ASME B18.2.1.8** vite a testa esagonale flangiata UNC.

-   <img alt="" src=images/Fasteners_DIN571.svg  style="width:32px;"> **DIN 571** Vite per legno a testa esagonale.

-   <img alt="" src=images/Fasteners_DIN933.svg  style="width:32px;"> **DIN 933** Vite a testa esagonale con gambo interamente filettato.

-   <img alt="" src=images/Fasteners_DIN961.svg  style="width:32px;"> **DIN 961** Vite a testa esagonale con gambo interamente filettato -- passo fine.

-   <img alt="" src=images/Fasteners_EN1662.svg  style="width:32px;"> **EN 1662** Vite a testa esagonale con flangia - serie leggera.

-   <img alt="" src=images/Fasteners_EN1665.svg  style="width:32px;"> **EN 1665** Vite a testa esagonale flangiata con o senza zigrinatura sottotesta - serie pesante.

-   <img alt="" src=images/Fasteners_ISO4014.svg  style="width:32px;"> 
**ISO 4014** Bullone a testa esagonale con gambo parzialmente filettato. *Prodotto di categoria A e B.*

-   <img alt="" src=images/Fasteners_ISO4015.svg  style="width:32px;"> **ISO 4015** Vite a testa esagonale con gambo parzialmente filettato e ridotto.

-   <img alt="" src=images/Fasteners_ISO4016.svg  style="width:32px;"> 
**ISO 4016** Vite a testa esagonale con gambo parzialmente filettato - *Prodotto di categoria C.*

-   <img alt="" src=images/Fasteners_ISO4017.svg  style="width:32px;"> 
**ISO 4017** Vite a testa esagonale con gambo interamente filettato. *Prodotto di categoria A e B.*

-   <img alt="" src=images/Fasteners_ISO4018.svg  style="width:32px;"> 
**ISO 4018** Vite a testa esagonale con gambo interamente filettato . *Prodotto di categoria C.*

-   <img alt="" src=images/Fasteners_ISO4162.svg  style="width:32px;"> 
**ISO 4162** Vite esagonale con flangia, serie leggera. *Prodotto di categoria A con funzionalità di guida di prodotto di categoria B.*

-   <img alt="" src=images/Fasteners_ISO8676.svg  style="width:32px;"> 
**ISO 8676** Viti a testa esagonale con gambo interamente filettato e con filettatura metrica a passo fine. *Prodotto di categoria A e B.*

-   <img alt="" src=images/Fasteners_ISO8765.svg  style="width:32px;"> **ISO 8765** Bulloni a testa esagonale con gambo parzialmente filettato -- passo fine.

-   <img alt="" src=images/Fasteners_ISO15071.svg  style="width:32px;"> 
**ISO 15071** Vite a testa esagonale con flangia, serie leggera. *Prodotto di categoria A.*

-   <img alt="" src=images/Fasteners_ISO15072.svg  style="width:32px;"> 
**ISO 15072** Viti a testa esagonale flangiate con filettatura metrica a passo fine, serie leggera. *Prodotto di categoria A.*



### Viti a esagono incassato 

-   <img alt="" src=images/Fasteners_ASMEB18.3.1A.svg  style="width:32px;"> **ASME B18.3.1A** Vite a testa cilindrica con esagono incassato UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.3.1G.svg  style="width:32px;"> **ASME B18.3.1G** Vite a testa cilindrica con cava esagonale a testa bassa UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.3.2.svg  style="width:32px;"> **ASME B18.3.2** Vite a testa svasata con cava esagonale UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.3.3A.svg  style="width:32px;"> **ASME B18.3.3A** Vite a testa tonda con cava esagonale UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.3.3B.svg  style="width:32px;"> **ASME B18.3.3B** Vite a testa tonda con cava esagonale e flangia UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.3.4.svg  style="width:32px;"> **ASME B18.3.4** Vite con spallamento a testa esagonale UNC.

-   <img alt="" src=images/Fasteners_DIN6912.svg  style="width:32px;"> **DIN 6912** Vite a testa cilindrica bassa con esagono incassato e con foro guida.

-   <img alt="" src=images/Fasteners_DIN7984.svg  style="width:32px;"> **DIN 7984** Vite a testa cilindrica bassa con cava esagonale.

-   <img alt="" src=images/Fasteners_ISO2936.svg  style="width:32px;"> **ISO 2936** Chiave a brugola.

-   <img alt="" src=images/Fasteners_ISO4762.svg  style="width:32px;"> **ISO 4762** Viti a testa cilindrica con cava esagonale.

-   <img alt="" src=images/Fasteners_ISO7379.svg  style="width:32px;"> **ISO 7379** Viti a testa cilindrica con cava esagonale, gambo rettificato e codolo filettato

-   <img alt="" src=images/Fasteners_ISO7380-1.svg  style="width:32px;"> **ISO 7380-1** Vite a testa bombata con cava esagonale.

-   <img alt="" src=images/Fasteners_ISO7380-2.svg  style="width:32px;"> **ISO 7380-2** Vite a testa bombata con cava esagonale con flangia.

-   <img alt="" src=images/Fasteners_ISO10642.svg  style="width:32px;"> **ISO 10642** Vite a testa svasata con cava esagonale.



### Viti a testa cava esalobata 

-   <img alt="" src=images/Fasteners_ISO14579.svg  style="width:32px;"> **ISO 14579** Vite a testa cilindrica con cava esalobata.

-   <img alt="" src=images/Fasteners_ISO14580.svg  style="width:32px;"> **ISO 14580** Vite a testa cilindrica con cava esalobata.

-   <img alt="" src=images/Fasteners_ISO14581.svg  style="width:32px;"> **ISO 14581** Vite a testa svasata piana con cava esalobata.

-   <img alt="" src=images/Fasteners_ISO14582.svg  style="width:32px;"> **ISO 14582** Vite a testa svasata con cava esalobata, testa alta.

-   <img alt="" src=images/Fasteners_ISO14583.svg  style="width:32px;"> **ISO 14583** Vite a testa cilindrica con cava esalobata.

-   <img alt="" src=images/Fasteners_ISO14584.svg  style="width:32px;"> **ISO 14584** Vite a testa svasata rialzata con cava esalobata.



### Viti a testa con intaglio 

-   <img alt="" src=images/Fasteners_ASMEB18.6.1.2.svg  style="width:32px;"> **ASME B18.6.1.2** Vite per legno a testa svasata piana con intaglio.

-   <img alt="" src=images/Fasteners_ASMEB18.6.1.4.svg  style="width:32px;"> **ASME B18.6.1.4** Vite per legno a testa svasata ovale con intaglio.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.1A.svg  style="width:32px;"> **ASME B18.6.3.1A** Vite UNC a testa piatta svasata con intaglio.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.4A.svg  style="width:32px;"> **ASME B18.6.3.4A** Vite UNC a testa svasata ovale con intaglio.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.9A.svg  style="width:32px;"> **ASME B18.6.3.9A** Vite UNC a testa cilindrica con intaglio.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.10A.svg  style="width:32px;"> **ASME B18.6.3.10A** Vite UNC a testa cilindrica con intaglio.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.12A.svg  style="width:32px;"> **ASME B18.6.3.12A** Viti UNC a testa tonda con intaglio.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.16A.svg  style="width:32px;"> **ASME B18.6.3.16A** Vite UNC a testa tonda con intaglio.

-   <img alt="" src=images/Fasteners_DIN84.svg  style="width:32px;"> 
**DIN 84 (superseded by ISO 1207)** Vite a testa cilindrica con intaglio. *Prodotto di categoria A.*

-   <img alt="" src=images/Fasteners_DIN96.svg  style="width:32px;"> **DIN 96** Vite per legno a testa semitonda con intaglio.

-   <img alt="" src=images/Fasteners_GOST1144-1.svg  style="width:32px;"> **GOST 1144-1** Vite per legno a testa semitonda con intaglio.

-   <img alt="" src=images/Fasteners_GOST1144-2.svg  style="width:32px;"> **GOST 1144-2** Vite per legno a testa a calotta con intaglio.

-   <img alt="" src=images/Fasteners_ISO1207.svg  style="width:32px;"> 
**ISO 1207** Vite a testa cilindrica con intaglio. *Prodotto di categoria A.*

-   <img alt="" src=images/Fasteners_ISO1580.svg  style="width:32px;"> 
**ISO 1580** Vite a testa cilindrica con intaglio. *Prodotto di categoria A.*

-   <img alt="" src=images/Fasteners_ISO2009.svg  style="width:32px;"> 
**ISO 2009** Vite a testa svasata piana con intaglio. *Prodotto di categoria A.*

-   <img alt="" src=images/Fasteners_ISO2010.svg  style="width:32px;"> 
**ISO 2010** Vite a testa svasata bombata con intaglio. *Prodotto di categoria A.*



### Viti con testa a croce 

-   <img alt="" src=images/Fasteners_ASMEB18.6.1.3.svg  style="width:32px;"> **ASME B18.6.1.3** Vite per legno a testa svasata piana.

-   <img alt="" src=images/Fasteners_ASMEB18.6.1.5.svg  style="width:32px;"> **ASME B18.6.1.5** Vite per legno a testa svasata ovale.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.1B.svg  style="width:32px;"> **ASME B18.6.3.1B** Vite UNC a testa svasata piana.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.4B.svg  style="width:32px;"> **ASME B18.6.3.4B** Vite UNC a testa svasata ovale.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.9B.svg  style="width:32px;"> **ASME B18.6.3.9B** Vite UNC a testa cilindrica.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.10B.svg  style="width:32px;"> **ASME B18.6.3.10B** Vite UNC a testa cilindrica.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.12C.svg  style="width:32px;"> **ASME B18.6.3.12C** Vite UNC a testa tonda.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.16B.svg  style="width:32px;"> **ASME B18.6.3.16B** Vite UNC a testa tonda.

-   <img alt="" src=images/Fasteners_DIN967.svg  style="width:32px;"> **DIN 967** Vite a testa bombata flangiata con impronta a croce.

-   <img alt="" src=images/Fasteners_DIN7996.svg  style="width:32px;"> **DIN 7996** Viti per legno a testa tonda e impronta a croce.

-   <img alt="" src=images/Fasteners_GOST1144-3.svg  style="width:32px;"> **GOST 1144-3** Vite per legno a testa cilindrica.

-   <img alt="" src=images/Fasteners_GOST1144-4.svg  style="width:32px;"> **GOST 1144-4** Vite per legno a testa cilindrica.

-   <img alt="" src=images/Fasteners_ISO7045.svg  style="width:32px;"> 
**ISO 7045** Vite a testa cilindrica. *Prodotto di categoria A.*

-   <img alt="" src=images/Fasteners_ISO7046.svg  style="width:32px;"> 
**ISO 7046** Vite a testa svasata piana. *Prodotto di categoria A.*

-   <img alt="" src=images/Fasteners_ISO7047.svg  style="width:32px;"> 
**ISO 7047** Vite a testa svasata rialzata. *Prodotto di categoria A.*

-   <img alt="" src=images/Fasteners_ISO7048.svg  style="width:32px;"> **ISO 7048** Viti a testa cilindrica con impronta croce

-   <img alt="" src=images/Fasteners_ISO7049-C.svg  style="width:32px;"> **ISO 7049-C** Viti autofilettanti a testa cilindrica con impronta a croce.

-   <img alt="" src=images/Fasteners_ISO7049-F.svg  style="width:32px;"> **ISO 7049-F** Viti autofilettanti a testa bombata con punta piatta.

-   <img alt="" src=images/Fasteners_ISO7049-R.svg  style="width:32px;"> **ISO 7049-R** Viti autofilettanti a testa bombata con punta arrotondata.



### Bulloni con altre teste 

-   <img alt="" src=images/Fasteners_ASMEB18.2.1.1.svg  style="width:32px;"> **ASME B18.2.1.1** Bullone UNC a testa quadra.

-   <img alt="" src=images/Fasteners_ASMEB18.5.2.svg  style="width:32px;"> **ASME B18.5** Bullone UNC a testa tonda e colletto quadro.

-   <img alt="" src=images/Fasteners_DIN478.svg  style="width:32px;"> **DIN 478** Bullone a testa quadra con collare

-   <img alt="" src=images/Fasteners_DIN603.svg  style="width:32px;"> **DIN 603** Vite a testa tonda con quadro sotto testa.

-   <img alt="" src=images/Fasteners_ISO2342.svg  style="width:32px;"> **ISO 2342** Vite senza testa con intaglio parzialmente filettata.



### Grani

-   <img alt="" src=images/Fasteners_ASMEB18.3.5A.svg  style="width:32px;"> **ASME B18.3.5A** Grano UNC con cava esagonale ed estremità piatta.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5B.svg  style="width:32px;"> **ASME B18.3.5B** Grano UNC con cava esagonale ed estremità conica.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5C.svg  style="width:32px;"> **ASME B18.3.5C** Grano UNC con esagono incassato ed estremità cilindrica.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5D.svg  style="width:32px;"> **ASME B18.3.5D** Grano UNC con cava esagonale ed estremità a coppa.

-   <img alt="" src=images/Fasteners_ISO4026.svg  style="width:32px;"> **ISO 4026** Vite senza testa con esagono incassato ed estremità piana smussata.

-   <img alt="" src=images/Fasteners_ISO4027.svg  style="width:32px;"> **ISO 4027** Vite senza testa con cava esagonale ed estremità conica.

-   <img alt="" src=images/Fasteners_ISO4028.svg  style="width:32px;"> **ISO 4028** Vite senza testa con cava esagonale ed estremità piana cilindrica.

-   <img alt="" src=images/Fasteners_ISO4029.svg  style="width:32px;"> **ISO 4029** Vite senza testa con cava esagonale ed estremità a coppa.

-   <img alt="" src=images/Fasteners_ISO4766.svg  style="width:32px;"> **ISO 4766** Vite senza testa con intaglio ed estremità piana.

-   <img alt="" src=images/Fasteners_ISO7434.svg  style="width:32px;"> **ISO 7434** Vite senza testa con intaglio ed estremità conica.

-   <img alt="" src=images/Fasteners_ISO7435.svg  style="width:32px;"> **ISO 7435** Vite senza testa con intaglio ed estremità cilindrica.

-   <img alt="" src=images/Fasteners_ISO7436.svg  style="width:32px;"> **ISO 7436** Vite senza testa con intaglio ed estremità a coppa.



### Viti a testa zigrinata 

-   <img alt="" src=images/Fasteners_DIN464.svg  style="width:32px;"> **DIN 464** Viti a testa cilindrica zigrinata con colletto alto.

-   <img alt="" src=images/Fasteners_DIN465.svg  style="width:32px;"> **DIN 465** Viti a testa cilindrica zigrinata con colletto alto ad intaglio.

-   <img alt="" src=images/Fasteners_DIN653.svg  style="width:32px;"> **DIN 653** Viti a testa cilindrica bassa zigrinata.



### Dadi

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.1A.svg  style="width:32px;"> **ASME B18.2.2.1A** Dado esagonale UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.1B.svg  style="width:32px;"> **ASME B18.2.2.1B** Dado quadrato UNC per macchinari.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.2.svg  style="width:32px;"> **ASME 18.2.2.2** Dado quadrato UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.4A.svg  style="width:32px;"> **ASME B18.2.2.4A** Dado esagonale UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.4B.svg  style="width:32px;"> **ASME B18.2.2.4B** Dado esagonale sottile UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.5.svg  style="width:32px;"> **ASME 18.2.2.5** Dado esagonale a corona UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.12.svg  style="width:32px;"> **ASME 18.2.2.12** Dado esagonale UNC con flangia.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.13.svg  style="width:32px;"> **ASME 18.2.2.13** Dado distanziale esagonale UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.6.9A.svg  style="width:32px;"> **ASME 18.6.9A** Dado ad alette, tipo A.

-   <img alt="" src=images/Fasteners_DIN315.svg  style="width:32px;"> **DIN 315** Dado ad alette.

-   <img alt="" src=images/Fasteners_DIN557.svg  style="width:32px;"> **DIN 557** Dado quadro.

-   <img alt="" src=images/Fasteners_DIN562.svg  style="width:32px;"> **DIN 562** Dado quadro sottile.

-   <img alt="" src=images/Fasteners_DIN917.svg  style="width:32px;"> **DIN 917** Dado esagonale cieco forma bassa.

-   <img alt="" src=images/Fasteners_DIN928.svg  style="width:32px;"> **DIN 928** Dado a saldare chiave quadra .

-   <img alt="" src=images/Fasteners_DIN929.svg  style="width:32px;"> **DIN 929** Dado a saldare.

-   <img alt="" src=images/Fasteners_DIN934.svg  style="width:32px;"> 
**DIN 934 (sostituito da ISO 4035 e ISO 8673)** Dado esagonale sottile cianfrinato. *Prodotto di categoria A e B.*

-   <img alt="" src=images/Fasteners_DIN935.svg  style="width:32px;"> **DIN 935** Dado esagonale a corona tipo alto.

-   <img alt="" src=images/Fasteners_DIN985.svg  style="width:32px;"> **DIN 985** Dado autobloccante basso con inserto in nylon.

-   <img alt="" src=images/Fasteners_DIN1587.svg  style="width:32px;"> **DIN 1587** Dado esagonale cieco con calotta sferica.

-   <img alt="" src=images/Fasteners_DIN6330.svg  style="width:32px;"> **DIN 6330** Dado esagonale alto con estremità sferica.

-   <img alt="" src=images/Fasteners_DIN6331.svg  style="width:32px;"> **DIN 6331** Dado esagonale alto flangiato con estremità sferica.

-   <img alt="" src=images/Fasteners_DIN6334.svg  style="width:32px;"> **DIN 6334** Dado esagonale di giunzione.

-   <img alt="" src=images/Fasteners_DIN7967.svg  style="width:32px;"> **DIN 7967** Controdado elastico di sicurezza.

-   <img alt="" src=images/Fasteners_EN1661.svg  style="width:32px;"> **EN 1661** Dado esagonale con flangia.

-   <img alt="" src=images/Fasteners_GOST11860-1.svg  style="width:32px;"> **GOST 11860-1** Dado cieco.

-   <img alt="" src=images/Fasteners_ISO4032.svg  style="width:32px;"> 
**ISO 4032** Dado esagonale, tipo 1. *Prodotto di categoria A e B.*

-   <img alt="" src=images/Fasteners_ISO4033.svg  style="width:32px;"> 
**ISO 4033** Dado esagonale alto, tipo 2. *Prodotto di categoria A e B.*

-   <img alt="" src=images/Fasteners_ISO4034.svg  style="width:32px;"> **ISO 4034** Dado esagonale, tipo 1.

-   <img alt="" src=images/Fasteners_ISO4035.svg  style="width:32px;"> 
**ISO 4035** Dado esagonale basso cianfrinato, tipo 0. *Prodotto di categoria A e B.*

-   <img alt="" src=images/Fasteners_ISO4161.svg  style="width:32px;"> **ISO 4161** Dado esagonale con flangia zigrinata.

-   <img alt="" src=images/Fasteners_ISO7040.svg  style="width:32px;"> **ISO 7040** Dado autobloccante alto con inserto non metallico.

-   <img alt="" src=images/Fasteners_ISO7041.svg  style="width:32px;"> **ISO 7041** Dado esagonale autobloccante (con inserto non metallico), tipo 2.

-   <img alt="" src=images/Fasteners_ISO7043.svg  style="width:32px;"> **ISO 7043** Dado esagonale autobloccante con flangia (con inserto non metallico).

-   <img alt="" src=images/Fasteners_ISO7044.svg  style="width:32px;"> **ISO 7044** Dado esagonale autobloccante interamente metallico con flangia.

-   <img alt="" src=images/Fasteners_ISO7719.svg  style="width:32px;"> **ISO 7719** Dado esagonale autobloccante interamente metallico.

-   <img alt="" src=images/Fasteners_ISO7720.svg  style="width:32px;"> **ISO 7720** Dado esagonale autobloccante interamente metallico, tipo 2.

-   <img alt="" src=images/Fasteners_ISO8673.svg  style="width:32px;"> 
**ISO 8673** Dado esagonale a passo fine, tipo 1. *Prodotto di categoria A e B.*

-   <img alt="" src=images/Fasteners_ISO8674.svg  style="width:32px;"> 
**ISO 8674** Dado esagonale alto con filettatura metrica a passo fine, tipo 2. *Prodotto di categoria A e B.*

-   <img alt="" src=images/Fasteners_ISO8675.svg  style="width:32px;"> 
**ISO 8675** Dado esagonale basso con filettatura metrica a passo fine tipo 0. *Prodotto di categoria A e B.*

-   <img alt="" src=images/Fasteners_ISO10511.svg  style="width:32px;"> **ISO 10511** Dado esagonale autofrenante basso (con inserto non metallico).

-   <img alt="" src=images/Fasteners_ISO10512.svg  style="width:32px;"> **ISO 10512** Dado esagonale autofrenante normale (con inserto non metallico) con filettatura metrica a passo fine.

-   <img alt="" src=images/Fasteners_ISO10513.svg  style="width:32px;"> **ISO 10513** Dado esagonale alto autofrenante interamente metallico con filettatura metrica a passo fine.

-   <img alt="" src=images/Fasteners_ISO10663.svg  style="width:32px;"> **ISO 10663** Dado esagonale con flangia e filettatura metrica a passo fine.

-   <img alt="" src=images/Fasteners_ISO12125.svg  style="width:32px;"> **ISO 12125** Dado esagonale autobloccante con flangia (con inserto non metallico), filettatura metrica passo fine.

-   <img alt="" src=images/Fasteners_ISO12126.svg  style="width:32px;"> **ISO 12126** Dado esagonale autobloccante, interamente metallico, con flangia, con filettatura metrica fine.

-   <img alt="" src=images/Fasteners_ISO21670.svg  style="width:32px;"> **ISO 21670** Dado esagonale flangiato da saldare.

-   <img alt="" src=images/Fasteners_SAEJ483a1.svg  style="width:32px;"> **SAE J483a 1** Dado a calotta bassa.

-   <img alt="" src=images/Fasteners_SAEJ483a2.svg  style="width:32px;"> **SAE J483a 2** Dado a calotta alta.



### Elementi di fissaggio per cave a T 

-   <img alt="" src=images/Fasteners_DIN508.svg  style="width:32px;"> **DIN 508** Dado per cave a T.

-   <img alt="" src=images/Fasteners_GN505.svg  style="width:32px;"> **GN 505** Dado per cave a T a quarto di giro zigrinato.

-   <img alt="" src=images/Fasteners_GN505.4.svg  style="width:32px;"> **GN 505.4** Bullone per cave a T zigrinato.

-   <img alt="" src=images/Fasteners_GN506.svg  style="width:32px;"> **GN 506** Tassello per cave a T con gradino guida.

-   <img alt="" src=images/Fasteners_GN507.svg  style="width:32px;"> **GN 507** Tassello per cave a T.

-   <img alt="" src=images/Fasteners_ISO299.svg  style="width:32px;"> **ISO 299** Tassello per cave a T.



### Rondelle

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12A.svg  style="width:32px;"> **ASME B18.21.1.12A** Rondella UN, serie stretta.

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12B.svg  style="width:32px;"> **ASME B18.21.1.12B** Rondella UN, serie normale.

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12C.svg  style="width:32px;"> **ASME B18.21.1.12C** Rondella UN, serie larga.

-   <img alt="" src=images/Fasteners_DIN6319C.svg  style="width:32px;"> **DIN 6319C** Rondella sferica.

-   <img alt="" src=images/Fasteners_DIN6319D.svg  style="width:32px;"> **DIN 6319D** Rondella conica.

-   <img alt="" src=images/Fasteners_DIN6319G.svg  style="width:32px;"> **DIN 6319G** Rondella conica.

-   <img alt="" src=images/Fasteners_DIN6340.svg  style="width:32px;"> **DIN 6340** Rondella per dispositivi di bloccaggio.

-   <img alt="" src=images/Fasteners_ISO7089.svg  style="width:32px;"> 
**ISO 7089** Rondella piana, serie normale. *Prodotto di categoria A.*

-   <img alt="" src=images/Fasteners_ISO7090.svg  style="width:32px;"> 
**ISO 7090** Rondelle piane smussate, serie normale. *Prodotto di categoria A.*

-   <img alt="" src=images/Fasteners_ISO7092.svg  style="width:32px;"> 
**ISO 7092** Rondella piana, serie stretta. *Prodotto di categoria A.*

-   <img alt="" src=images/Fasteners_ISO7093-1.svg  style="width:32px;"> 
**ISO 7093-1** Rondella piana, serie larga. *Prodotto di categoria A.*

-   <img alt="" src=images/Fasteners_ISO7094.svg  style="width:32px;"> 
**ISO 7094** Rondella piana, serie extra larga. *Prodotto di categoria C.*

-   <img alt="" src=images/Fasteners_ISO8738.svg  style="width:32px;"> **ISO 8738** Rondella piana per perni a cerniera.

-   <img alt="" src=images/Fasteners_NFE27-619.svg  style="width:32px;"> **NFE27-619** Rondella svasata.



### Barre, maschi e filiere 

-   <img alt="" src=images/Fasteners_ScrewTapInch.svg  style="width:32px;"> Maschio per filettatura interna in pollici.

-   <img alt="" src=images/Fasteners_ScrewDieInch.svg  style="width:32px;"> Filiera per filettatura esterna in pollici.

-   <img alt="" src=images/Fasteners_ThreadedRodInch.svg  style="width:32px;"> Barra filettata UNC in pollici.

-   <img alt="" src=images/Fasteners_ThreadedRod.svg  style="width:32px;"> DIN 975 Barra filettata metrica.

-   <img alt="" src=images/Fasteners_ScrewTap.svg  style="width:32px;"> Maschio per filettatura interna metrica.

-   <img alt="" src=images/Fasteners_ScrewDie.svg  style="width:32px;"> Filiera per filettatura esterna metrica.



### Inserti

-   <img alt="" src=images/Fasteners_IUTHeatInsert.svg  style="width:32px;"> Inserto ribadito a caldo.

-   <img alt="" src=images/Fasteners_PEMPressNut.svg  style="width:32px;"> Dado autoagganciante.

-   <img alt="" src=images/Fasteners_PEMStandoff.svg  style="width:32px;"> Distanziale autoagganciante

-   <img alt="" src=images/Fasteners_PEMStud.svg  style="width:32px;"> Perno autoagganciante.

-   <img alt="" src=images/Fasteners_PCBSpacer.svg  style="width:32px;"> Distanziale PCB femmina/femmina.

-   <img alt="" src=images/Fasteners_PCBStandoff.svg  style="width:32px;"> Distanziale PCB femmina/maschio.

-   <img alt="" src=images/Fasteners_4PWTI.svg  style="width:32px;"> Inserto in legno filettato a 4 poli (dadi a T DIN 1624).



### Anelli di sicurezza 

-   <img alt="" src=images/Fasteners_DIN471.svg  style="width:32px;"> **DIN 471** Anello elastico esterno.

-   <img alt="" src=images/Fasteners_DIN472.svg  style="width:32px;"> **DIN 472** Anello elastico interno.

-   <img alt="" src=images/Fasteners_DIN6799.svg  style="width:32px;"> **DIN 6799** Anello elastico radiale.



### Chiodi

-   <img alt="" src=images/Fasteners_DIN1143.svg  style="width:32px;"> **DIN 1143** Chiodo a testa tonda piatta per chiodatrici automatiche.

-   <img alt="" src=images/Fasteners_DIN1144-A.svg  style="width:32px;"> **DIN 1144-A** Chiodo per l\'installazione di pannelli compositi in truciolare di legno, testa tonda da 20 mm.

-   <img alt="" src=images/Fasteners_DIN1151-A.svg  style="width:32px;"> **DIN 1151-A** Chiodo a filo tondo a testa liscia.

-   <img alt="" src=images/Fasteners_DIN1151-B.svg  style="width:32px;"> **DIN 1151-B** Chiodo a filo tondo a testa svasata.

-   <img alt="" src=images/Fasteners_DIN1152.svg  style="width:32px;"> **DIN 1152** Chiodo a filo tondo testa a gruppino.

-   <img alt="" src=images/Fasteners_DIN1160-A.svg  style="width:32px;"> **DIN 1160-A** Chiodo per legno o ardesia.

-   <img alt="" src=images/Fasteners_DIN1160-B.svg  style="width:32px;"> **DIN 1160-B** Chiodo a testa larga di grosso spessore per ardesia.



### Spine

-   <img alt="" src=images/Fasteners_ISO1234.svg  style="width:32px;"> **ISO 1234** Copiglia.

-   <img alt="" src=images/Fasteners_ISO2338.svg  style="width:32px;"> **ISO 2338** Spina cilindrica.

-   <img alt="" src=images/Fasteners_ISO2339.svg  style="width:32px;"> **ISO 2339** Spina conica.

-   <img alt="" src=images/Fasteners_ISO2340A.svg  style="width:32px;"> **ISO 2340A** Perno senza testa.

-   <img alt="" src=images/Fasteners_ISO2340B.svg  style="width:32px;"> **ISO 2340B** Perno senza testa (con fori per copiglie).

-   <img alt="" src=images/Fasteners_ISO2341A.svg  style="width:32px;"> **ISO 2341A** Perno con testa.

-   <img alt="" src=images/Fasteners_ISO2341B.svg  style="width:32px;"> **ISO 2341B** Perno con testa (con foro per copiglia).

-   <img alt="" src=images/Fasteners_ISO8733.svg  style="width:32px;"> **ISO 8733** Spina cilindrica con foro filettato, non temprata.

-   <img alt="" src=images/Fasteners_ISO8734.svg  style="width:32px;"> **ISO 8734** Spina di centraggio.

-   <img alt="" src=images/Fasteners_ISO8735.svg  style="width:32px;"> **ISO 8735** Spina cilindrica con filettatura interna, temprata.

-   <img alt="" src=images/Fasteners_ISO8736.svg  style="width:32px;"> **ISO 8736** Spina conica con foro filettato, non temprata.

-   <img alt="" src=images/Fasteners_ISO8737.svg  style="width:32px;"> **ISO 8737** Spina conica con gambo filettato, non temprata.

-   <img alt="" src=images/Fasteners_ISO8739.svg  style="width:32px;"> **ISO 8739** Spina cilindrica con intagli su tutta la lunghezza ed estremità d\'invito.

-   <img alt="" src=images/Fasteners_ISO8740.svg  style="width:32px;"> **ISO 8740** Spina cianfrinata per tutta la lunghezza.

-   <img alt="" src=images/Fasteners_ISO8741.svg  style="width:32px;"> **ISO 8741** Spina con intagli conici a mezza lunghezza invertita.

-   <img alt="" src=images/Fasteners_ISO8742.svg  style="width:32px;"> **ISO 8742** Spina ad intagli centrali su un terzo della lunghezza.

-   <img alt="" src=images/Fasteners_ISO8743.svg  style="width:32px;"> **ISO 8743** Spina ad intagli centrali su metà lunghezza.

-   <img alt="" src=images/Fasteners_ISO8744.svg  style="width:32px;"> **ISO 8744** Spina ad intagli conici su tutta la lunghezza.

-   <img alt="" src=images/Fasteners_ISO8745.svg  style="width:32px;"> **ISO 8745** Spina ad intagli conici su metà lunghezza con diametro di forzamento ad una estremità.

-   <img alt="" src=images/Fasteners_ISO8746.svg  style="width:32px;"> **ISO 8746** Spina intagliata a testa tonda.

-   <img alt="" src=images/Fasteners_ISO8747.svg  style="width:32px;"> **ISO 8747** Spina ad intagli con testa svasata.

-   <img alt="" src=images/Fasteners_ISO8748.svg  style="width:32px;"> **ISO 8748** Spina elastica a spirale - Serie pesante.

-   <img alt="" src=images/Fasteners_ISO8750.svg  style="width:32px;"> **ISO 8750** Spina elastica a spirale - Serie media.

-   <img alt="" src=images/Fasteners_ISO8751.svg  style="width:32px;"> **ISO 8751** Spina elastica a spirale - Serie leggera.

-   <img alt="" src=images/Fasteners_ISO8752.svg  style="width:32px;"> **ISO 8752** Spina elastica con fenditura - Serie pesante.

-   <img alt="" src=images/Fasteners_ISO13337.svg  style="width:32px;"> **ISO 13337** Spina elastica con fenditura serie leggera.



## Obsoleti

-   <img alt="" src=images/Fasteners_ChamferHole.svg  style="width:32px;"> [Smusso per foro](Fasteners_ChamferHole/it.md): Fori smussati per viti a testa svasata. Non disponibile dalla {{VersionPlus/it|0.5.13}}.



## Riferimenti

-   Autore: [shaise](http://theseger.com/projects/author/shaise/)
    -   Creatore di viti: Ulrich Brammer
    -   Wrapper per l\'ambiente: Shai Seger
-   Source code: <https://github.com/shaise/FreeCAD_FastenersWB>
-   Segnalazioni di bug e richieste di funzionalità: <https://github.com/shaise/FreeCAD_FastenersWB/issues>
-   Topic nel Forum: <https://forum.freecadweb.org/viewtopic.php?t=11429>



## Collegamenti

-   [BOLTS](https://github.com/jreinhardt/BOLTS): Una libreria open per le specifiche tecniche.


{{Fasteners_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [User_Documentation](Category_User_Documentation.md) > [External_Workbenches](Category_External_Workbenches.md) > Fasteners Workbench/it
