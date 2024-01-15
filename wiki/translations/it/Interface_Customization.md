# Interface Customization/it
## Introduzione

L\'interfaccia di FreeCAD è basata sul moderno toolkit [Qt](https://it.wikipedia.org/wiki/Qt_(toolkit)), e dispone di una organizzazione ottimale. Alcuni aspetti dell\'interfaccia possono essere personalizzati. Ad esempio, è possibile aggiungere barre degli strumenti personalizzate, con strumenti di diversi ambienti di lavoro o strumenti definiti nelle macro e creare le proprie scorciatoie da tastiera. Ma i menu e le barre degli strumenti predefinite fornite con FreeCAD e i suoi ambienti di lavoro non possono essere modificati.


{{Version/it|0.21}}

: La scheda degli Ambienti non è più disponibile. La sua funzionalità è stata spostata nella scheda [Ambienti Disponibili](Preferences_Editor/it#Ambienti_Disponibili.md) nella sezione Ambienti di lavoro dell\'[Editor delle preferenze](Preferences_Editor/it.md).

![](images/Std_DlgCustomize_tab_Toolbars.png ) 
*La finestra di dialogo Personalizza*



## Utilizzo

1.  I comandi disponibili nella finestra di dialogo Personalizza dipendono dagli ambienti di lavoro che sono stati caricati nella sessione corrente di FreeCAD. Quindi dovresti prima caricare tutti gli ambienti ai cui comandi vuoi avere accesso.
2.  Esistono diversi modi per invocare il comando <img alt="" src=images/Std_DlgCustomize.svg  style="width:16px;"> [Personalizza](Std_DlgCustomize/it.md):
    -   Selezionare l\'opzione dal menu **Strumenti → <img src="images/Std_DlgCustomize.svg" width=16px> Personalizza...**.
    -   Cliccare col tasto destro sull\'area della barra strumenti e selezionare **<img src="images/Std_DlgCustomize.svg" width=16px> Personalizza...** dal menu contestuale.
3.  Si apre la finestra di dialogo Personalizza. Per ulteriori informazioni, vedere [Opzioni](#Opzioni.md).
4.  Il bottone **Aiuto** avvia il comando <img alt="" src=images/Std_WhatsThis.svg  style="width:16px;"> [Cos\'è questo](Std_WhatsThis/it.md)..
5.  Premere il bottone **Chiudi** per chiudere la finestra di dialogo.



## Opzioni

Nella finestra di dialogo Personalizza sono disponibili le seguenti schede:



### Tastiera

![](images/Std_DlgCustomize_tab_Keyboard.png ) 
*La scheda Tastiera*

In questa scheda è possibile definire le scorciatoie da tastiera personalizzate. I collegamenti per i comandi delle macro possono essere definiti nella scheda [Macro](#Macro.md).



#### Cercare

Puoi cercare i comandi inserendo almeno 3 caratteri del testo del menu o del nome nel campo di ricerca. La ricerca non fa distinzione tra maiuscole e minuscole.

È anche possibile cercare le scorciatoie:

-   Nel campo di ricerca i tasti speciali nelle scorciatoie devono essere inseriti come stringhe. Ad esempio, per cercare i comandi che utilizzano **Ctrl** nella loro scorciatoia, inserire {{Value|ctrl}} (4 lettere).
-   Aggiungere le parentesi per cercare le scorciatoie a carattere singolo, ad esempio: {{Value|(c)}}.
-   Aggiungere una virgola e uno spazio tra i caratteri delle scorciatoie multi-carattere, ad esempio: {{Value|g, b, b}}.



#### Aggiungere una scorciatoia 

1.  Selezionare una categoria di comandi dall\'elenco a discesa **Categoria**.
2.  Selezionare un comando dal pannello **Comandi**.
    -   Facoltativamente, fare clic sulle intestazioni di colonna {{Value|Comando}}, {{Value|Scelta rapida}} o {{Value|Predefinito}} per riordinare l\'elenco.
    -   Facoltativamente, trascinare lo splitter a destra del pannello per ridimensionarlo.
3.  La casella **Scorciatoia corrente** visualizza la scorciatoia corrente, se disponibile.
4.  Inserire una nuova scorciatoia nella casella di input **Nuova scorciatoia**. La scorciatoia accetta fino a 4 input. Ogni input è un singolo carattere, una combinazione di uno o più tasti speciali o una combinazione di uno o più tasti speciali e un carattere. Usare **Backspace** per correggere gli errori.
5.  Altri comandi attivi (vedi le [Note](#Note.md)) che già usano la scorciatoia saranno elencati nella **Lista priorità scorciatoia**.
6.  Premere il pulsante **Assegna** per assegnare la nuova scorciatoia.
7.  Se la **Lista priorità scorciatoia** contiene più di un comando: facoltativamente cambia il suo ordine selezionando i singoli comandi e premendo il pulsante **Su** o il pulsante **Giù**. Se i comandi attivi condividono la stessa scorciatoia, la scorciatoia attiverà quella più in alto nell\'elenco.



#### Rimuovere una scorciatoia 

1.  Selezionare una categoria di comando dall\'elenco a discesa **Categoria**.
2.  Selezionare un comando dal pannello **Comandi**.
3.  Premere il pulsante **Cancella**.



#### Ripristinare una scorciatoia predefinita 

1.  Selezionare una categoria di comando dall\'elenco a discesa **Categoria**.
2.  Selezionare un comando dal pannello **Comandi**.
3.  Premere il pulsante **Ripristina**.



#### Ripristinare tutte le scorciatoie predefinite 

1.  Premere il pulsante **Ripristina tutto**.



#### Note

-   Le scorciatoie funzionano solo per i comandi attivi. I comandi attivi sono comandi che appaiono nel menu standard, o nel menu dell\'ambiente attivo, o comandi che appaiono in una barra degli strumenti *visibile*.


{{Top}}



### Barre degli strumenti 

![](images/Std_DlgCustomize_tab_Toolbars.png ) 
*La scheda Barre degli strumenti*

In questa scheda è possibile creare e modificare barre degli strumenti personalizzate.



#### Cercare 

Vedere [Tastiera](#Cercare.md)



#### Selezionare l\'ambiente 

1.  Nell\'elenco a discesa a destra selezionare l\'ambiente di cui si desidera modificare le barre degli strumenti personalizzate. L\'opzione {{Value|Globale}} è disponibile per le barre degli strumenti personalizzate che dovrebbero essere disponibili in tutti gli ambienti.



#### Creare una barra degli strumenti 

1.  Premere il pulsante **Nuovo ...**.
2.  Inserire un nome nella finestra di dialogo che si apre.
3.  Premere il pulsante **OK**.
4.  La nuova barra degli strumenti appare nel pannello a destra.



#### Rinominare una barra degli strumenti 

1.  Selezionare una barra degli strumenti nel pannello a destra.
2.  Premere il pulsante **Rinomina...**.
3.  Inserire un nuovo nome nella finestra di dialogo che si apre.
4.  Premere il pulsante **OK**.



#### Eliminare una barra degli strumenti 

1.  Selezionare una barra degli strumenti nel pannello a destra.
2.  Premere il pulsante **Elimina**.



#### Disabilitare una barra degli strumenti 

1.  Deselezionare la casella di controllo davanti al nome della barra degli strumenti nel pannello a destra.
2.  Una barra degli strumenti disabilitata è invisibile nell\'interfaccia di FreeCAD.



#### Aggiungere un comando 

1.  È richiesta almeno una barra degli strumenti personalizzata. Vedi [Creare una barra degli strumenti](#Creare_una_barra_degli_strumenti.md).
2.  Selezionare la barra degli strumenti corretta nel pannello a destra. Se non viene selezionata alcuna barra degli strumenti, il comando viene aggiunto alla prima barra degli strumenti nell\'elenco.
3.  Selezionare una categoria di comando dall\'elenco a discesa **Categoria**. I comandi macro impostati nella scheda [Macro](#Macro.md) vengono visualizzati nella categoria {{Value|Macro}}.
4.  Selezionare un comando dal pannello **Comandi**, oppure selezionare {{Value|<Separatore>}} per aggiungere un separatore (una linea tra due pulsanti della barra degli strumenti).
    -   Facoltativamente, trascinare lo splitter a destra del pannello per ridimensionarlo.
5.  Premere il pulsante **<img src="images/Button_right.svg" width=16px>**.



#### Rimuovere un comando 

1.  Se necessario, espandere la barra degli strumenti nel riquadro a destra.
2.  Selezionare un comando.
3.  Premere il pulsante **<img src="images/Button_left.svg" width=16px>**.



#### Cambiare la posizione di un comando 

1.  Se necessario, espandere la barra degli strumenti nel riquadro a destra.
2.  Selezionare un comando.
3.  Premere il pulsante **<img src="images/Button_up.svg" width=16px>** o il pulsante **<img src="images/Button_down.svg" width=16px>**.
4.  Ripetere fino a quando il comando non si trova nella posizione desiderata.



#### Note 

-   Le barre degli strumenti appartenenti all\'ambiente corrente vengono aggiornate immediatamente, ma dopo aver disabilitato o riattivato una barra degli strumenti è necessario cambiare ambiente (passare a un ambiente diverso e quindi tornare indietro).
-   Per aggiornare le barre degli strumenti globali è necessario cambiare ambiente (se i comandi sono stati aggiunti o rimossi) o riavviare (se l\'ordine di una barra degli strumenti è cambiato o una barra degli strumenti è stata rinominata).


{{Top}}



### Macro

![](images/Std_DlgCustomize_tab_Macros.png ) 
*La scheda Macro*

In questa scheda è possibile impostare i comandi macro. Una volta configurati, possono essere aggiunti alle barre degli strumenti personalizzate. Le macro installate con <img alt="" src=images/Std_AddonMgr.svg  style="width:16px;"> [Addon Manager](Std_AddonMgr/it.md) vengono impostate automaticamente e aggiunte a una barra degli strumenti {{Value|Global}} (vedere [Barre degli strumenti](#Barre_degli_strumenti.md) ), se si conferma il popup **Aggiungi pulsante** durante il processo di installazione.

Se si desidera utilizzare una macro scaricata da una fonte diversa, si dovrà installarla manualmente. Vedi [Come installare le macro](How_to_install_macros/it.md) per maggiori informazioni. Si noti che FreeCAD utilizza una cartella dedicata per le macro e solo le macro in quella cartella possono essere impostate. Usare il comando <img alt="" src=images/Std_DlgMacroExecute.svg  style="width:16px;"> [Macro](Std_DlgMacroExecute/it.md) per trovare questa cartella sul proprio sistema.



#### Aggiungere un comando macro 

1.  Nell\'elenco a discesa **Macro** selezionare una macro.
2.  Immettere un **Testo di menu**. Questo sarà il nome utilizzato per identificare il comando macro e apparirà anche nella barra degli strumenti se non è presente l\'icona.
3.  Facoltativamente, inserire un **Suggerimento**. Questo testo apparirà vicino alla posizione del mouse quando si passa il mouse sull\'icona della barra degli strumenti.
4.  Facoltativamente, inserire un **Testo di stato**. Questo testo apparirà nella [barra di stato](Status_bar/it.md) quando si passa con il mouse sull\'icona della barra degli strumenti.
5.  Facoltativamente, inserire la pagina wiki per la macro, se disponibile, nella casella di inserimento **Che cos\'è questo**. Inserire il nome della pagina, non l\'URL completo.
6.  Facoltativamente, inserire una scorciatoia nella casella d\'immissione **Acceleratore**. Vedere [Tastiera](#Tastiera.md) per maggiori informazioni.
7.  Per aggiungere un\'icona:
    1.  Premere il pulsante **Pixmap** **...**.
    2.  Si apre la finestra di dialogo **Scegli Icona**.
    3.  Se necessario, premere il pulsante **Cartella icone...** per aggiungere una cartella di icone.
    4.  Selezionare un\'icona dal pannello. La finestra di dialogo **Scegli Icona** si chiude automaticamente.
8.  Premere il pulsante **Aggiungi**.
9.  Il comando macro appare nel pannello a sinistra.
10. È ora possibile selezionare il comando macro nella scheda [Barre degli strumenti](#Barre_degli_strumenti.md).



#### Rimuovere un comando macro 

1.  Selezionare il comando macro nel pannello a sinistra.
2.  Premere il pulsante **Elimina**.



#### Cambiare un comando macro 

1.  Fare doppio clic sul comando macro nel pannello a sinistra.
2.  Apportare le modifiche richieste. Notare che non si può rimuovere l\'icona, la si può solo sostituire.
3.  Premere il pulsante **Sostituisci**.


{{Top}}



### Movimenti Spaceball 

Questa scheda è vuota se non viene rilevata alcuna Spaceball. Vedere: [3Dconnexion input devices](3Dconnexion_input_devices/it.md). 

### Pulsanti Spaceball 

Questa scheda è vuota se non viene rilevata alcuna Spaceball. Vedere: [3Dconnexion input devices](3Dconnexion_input_devices/it.md). 

## Temi

FreeCAD supporta i temi completi dell\'interfaccia, tramite fogli di stile .qss. Il [formato qss](https://doc.qt.io/qt-5/stylesheet-syntax.html) è molto simile al [formato css](https://it.wikipedia.org/wiki/CSS) utilizzato nelle pagine Web, aggiunge fondamentalmente metodi per fare riferimento ai diversi widget ed elementi dell\'interfaccia Qt. Puoi cambiare il tema predefinito (che prende semplicemente lo stile definito dal tuo sistema desktop) selezionando un **foglio di stile** nel menu [Preferenze di FreeCAD](Preferences_Editor#General.md).

Puoi anche creare il tuo tema se non sei soddisfatto dei temi forniti con FreeCAD, ad esempio modificando un [foglio di stile esistente](https://github.com/FreeCAD/FreeCAD/tree/master/src/Gui/Stylesheets). Il tuo nuovo foglio di stile deve essere posizionato in una cartella specifica per essere trovato da FreeCAD:

-    **%APPDATA%/FreeCAD/Gui/Stylesheets**(per Windows). La cartella **%APPDATA%** può essere trovata inserendo {{Incode|App.getUserAppDataDir()}} dalla [console di Python](Python_console/it.md).

-    **$HOME/.FreeCAD/Gui/Stylesheets**(per Linux).

-    **$HOME/Library/Application Support/FreeCAD/Gui/Stylesheets**(per macOS).


{{Top}}



## Componenti aggiuntivi 

I componenti aggiuntivi di <img alt="" src=images/Std_AddonMgr.svg  style="width:16px;"> [Addon Manager](Std_AddonMgr.md) offrono un altro modo per personalizzare l\'interfaccia utente. Sono disponibili diversi [Preference Packs](Preference_Packs/it.md) per cambiare il [tema](#Temi.md).

Nella categoria Ambienti di Lavoro dell\'Addon Manager si possono trovare alcuni addons dell\'utente triplus:

-   <https://github.com/triplus/CubeMenu> (per {{VersionMinus/it|0.20}})
-   <https://github.com/triplus/Glass>.
-   <https://github.com/triplus/IconThemes>
-   <https://github.com/triplus/Launcher>
-   <https://github.com/triplus/PieMenu>
-   <https://github.com/triplus/RemBench>
-   <https://github.com/triplus/ShortCuts>


{{Top}}





{{Std Base navi

}} {{Interface navi}}



---
⏵ [documentation index](../README.md) > Interface Customization/it
