# Macro Loft/it
{{Macro/it
|Name=Macro Loft
|Translate=Loft
|Icon=FCCreaLoft.png
|Description=Crea un loft con i contorni selezionati.
|Author=Mario52
|Version=00.04
|Date=2019-07-03
|Download=[https://www.freecadweb.org/wiki/images/2/29/FCCreaLoft.png ToolBar Icon]
|SeeAlso= [32px|FCTexture](File:FCTexture.png.md) [Macro Texture](Macro_Texture/it.md)
|FCVersion=Tutte versione
}}

## Descrizione

Questa macro è stata scritta appositamente per facilitare il lofting con le linee generate dalla [Macro Texture](Macro_Texture/it.md) (ma può essere utilizzata anche per i loft comuni)
{{Codeextralink|https://gist.githubusercontent.com/mario52a/c477f892233d6abe02df5e97af828ff4/raw/d633193c577e8257ef458b8c1824d1047c3c6613/Macro_FCCreaLoft.FCMacro}}

<img alt="" src=images/Texture_001_Logo.png  style="width:480px;"> 
*Texture_001_Logo*


<div class="mw-translate-fuzzy">

## Uso

Copiare la macro e l\'icona nella cartella macro.


</div>

-   ****Sort**** : Ordina i dati in ingresso.
-   ****Reverse**** : Inverte l\'ordine dei dati.
-   ****Reset** / **Upgrade****: Questo pulsante ha molte funzioni:
    1.  Se non c\'è nessuna selezione nella vista 3D viene mostrato il pulsante **Upgrade**.
        Selezionare un oggetto nella vista 3D, o nella vista combinata e fare clic su questo pulsante per aggiornare i dati nella macro, il pulsante si trasforma in **Reset**.
    2.  Se uno o più oggetti sono selezionati prima dell\'avvio della macro viene mostrato il pulsante **Reset**.
        Tutti gli oggetti selezionati vengono visualizzati nella finestra della macro.
        Dopo aver ordinato con **Sort** o **Reverse** i dati visualizzati, si può usare il pulsante **Reset** per ripristinare l\'ordine originale.
        Se si fa clic nella vista 3D o si deselezionano tutti gli oggetti, questo pulsante serve per il reset della macro.
        Se alla lista si aggiunge uno o più oggetti questo pulsante serve per aggiornare i dati.
-   ****Select all**** : Seleziona tutti gli oggetti del documento.
-   **SpinBox** : Questa casella permette di \"saltare\" x linee (di default =1, vengono utilizzati tutti gli oggetti).
-   ****Quit**** : Esce dalla macro.
-   **CheckBox** Se questa casella viene attivata, lo stato dell\'elaborazione è visibile in tempo reale, se non è attivata si vede solo l\'avanzamento sulla barra (in questo è più veloce) (selezionata per impostazione predefinita).
-   ****Launch the Lofting**** : Avvia il Lofting e ripristina la macro. Il numero indica la quantità di elementi selezionati che saranno effettivamente trattati quando si utilizza lo spinBox \"salta\"

### L\'interfaccia

<img alt="FCCreaLoft002" src=images/Macro_FCCreaLoft_01.png  style="width:400px;"> 

## Script

L\'icona per la barra degli strumenti <img alt="" src=images/FCCreaLoft.png  style="width:64px;">

Scaricare la macro da Gist [**Macro\_FCCreaLoft.FCMacro**](https://gist.github.com/mario52a/c477f892233d6abe02df5e97af828ff4)

## Link

La discussione nel forum [Texture](http://forum.freecadweb.org/viewtopic.php?f=24&t=5893&start=10)

La [Macro Texture](Macro_Texture/it.md)

## Version

ver 00.00 : 06/02/2016

ver 00.02 : 09/02/2016 : Add button \"Select all\" and little option displayed in the button Launch (number selections) and (real number loft)

ver 00.03 : 09/02/2016 : minor (display on button)

ver 00.04 : 03/07/2019 : adapt to Python 3

---
[documentation index](../README.md) > Macro Loft/it
