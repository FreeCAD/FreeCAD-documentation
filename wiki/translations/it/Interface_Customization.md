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


<div class="mw-translate-fuzzy">

1.  Selezionare una categoria di comandi dall\'elenco a discesa **Categoria**.
2.  Selezionare un comando dal pannello **Comandi**.
3.  La casella **Scorciatoia corrente** visualizza la scorciatoia corrente, se disponibile.
4.  Inserire una nuova scorciatoia nella casella di input **Digita la nuova scorciatoia**. La scorciatoia accetta fino a 4 input. Ogni input è un singolo carattere, una combinazione di uno o più tasti speciali o una combinazione di uno o più tasti speciali e un carattere. Usare **Backspace** per correggere gli errori.
5.  Se la scorciatoia è già in uso, una finestra di dialogo chiede se si desidera sostituirla e il comando a cui è assegnata la scorciatoia viene visualizzato nel pannello **Attualmente assegnata a**.
6.  Premere il pulsante **Assegna** per assegnare la nuova scorciatoia.
7.  Premere il pulsante **Cancella** per rimuovere il collegamento immesso. Questo rimuove anche il contenuto della casella **Scorciatoia corrente**. Notare che i collegamenti predefiniti non vengono rimossi in modo permanente. Sono ripristinati al riavvio di FreeCAD.


</div>



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

-   Le scorciatoie funzionano solo per i comandi attivi. I comandi attivi sono comandi che appaiono nel menu standard, o nel menu di un ambiente di lavoro che è stato caricato nella sessione corrente di FreeCAD, o i comandi che appaiono su una barra degli strumenti *visibile*.


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


<div class="mw-translate-fuzzy">

1.  È richiesta almeno una barra degli strumenti personalizzata. Vedi [Creare una barra degli strumenti](#Creare_una_barra_degli_strumenti.md).
2.  Selezionare la barra degli strumenti corretta nel pannello a destra. Se non viene selezionata alcuna barra degli strumenti, il comando viene aggiunto alla prima barra degli strumenti nell\'elenco.
3.  Selezionare una categoria dall\'elenco a discesa a sinistra. I comandi delle macro che sono stati impostati nella scheda [Macro](#Macro.md) vengono visualizzati nella categoria \"Macro\".
4.  Selezionare un comando dal pannello a sinistra.
5.  Oppure selezionare \'\' per aggiungere un separatore (una linea tra due pulsanti della barra degli strumenti).
6.  Premere il pulsante **<img src="images/Button_right.svg" width=16px>**.


</div>



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


<div class="mw-translate-fuzzy">

-   Le barre degli strumenti appartenenti all\'ambiente corrente vengono aggiornate immediatamente, ma dopo aver disabilitato o riattivato una barra degli strumenti è necessario cambiare ambiente (passare a un ambiente diverso e quindi tornare indietro).
-   Per aggiornare le barre degli strumenti globali è necessario cambiare ambiente (se i comandi sono stati aggiunti o rimossi) o riavviare (se l\'ordine di una barra degli strumenti è cambiato o una barra degli strumenti è stata rinominata).

-   In V0.19 c\'è un problema con alcuni comandi di Draft. Dopo averli aggiunti a una barra degli strumenti personalizzata ed essere usciti dall\'applicazione FreeCAD, il file **user.cfg** deve essere modificato manualmente per questi comandi. Cercare il nome della barra degli strumenti personalizzata e in quella sezione modificare il contenuto degli elementi `FCText` che iniziano con `gui_` in `DraftTools`.


</div>


{{Top}}



### Macro

![](images/Std_DlgCustomize_tab_Macros.png ) 
*La scheda Macro*

On this tab macro commands can be set up. Once set up, they can be added to custom toolbars. Macros installed with the <img alt="" src=images/Std_AddonMgr.svg  style="width:16px;"> [Addon Manager](Std_AddonMgr.md) are set up automatically, and added to a {{Value|Global}} toolbar (see [Toolbars](#Toolbars.md)), if you confirm the **Add button** popup during the installation process.

If you want to use a macro downloaded from a different source you will have to install it manually. See [How to install macros](How_to_install_macros.md) for more information. Note that FreeCAD uses a dedicated folder for macros and only macros in that folder can be set up. Use the <img alt="" src=images/Std_DlgMacroExecute.svg  style="width:16px;"> [Std DlgMacroExecute](Std_DlgMacroExecute.md) command to find this folder on your system.



#### Aggiungere un comando macro 


<div class="mw-translate-fuzzy">

1.  Nell\'elenco a discesa **Macro** selezionare una macro.
2.  Immettere un **Testo di menu**. Questo sarà il nome utilizzato per identificare il comando macro e apparirà anche nella barra degli strumenti se non è presente l\'icona.
3.  Facoltativamente, inserire un **Suggerimento**. Questo testo apparirà vicino alla posizione del mouse quando si passa il mouse sull\'icona della barra degli strumenti.
4.  Facoltativamente, inserire un **Testo di stato**. Questo testo apparirà nella [barra di stato](Status_bar/it.md) quando si passa con il mouse sull\'icona della barra degli strumenti.
5.  Facoltativamente, inserire la pagina wiki per la macro, se disponibile, nella casella di inserimento **Che cos\'è questo**. Inserire il nome della pagina, non l\'URL completo.
6.  Facoltativamente, inserire una scorciatoia nella casella d\'immissione **Acceleratore**. Vedere [Tastiera](#Tastiera.md) per maggiori informazioni.
7.  Per aggiungere un\'icona:
    1.  Premere il pulsante **Pixmap** **...**.
    2.  Si apre la finestra di dialogo Scegli Icona.
    3.  Se necessario, premere il pulsante **Cartella icone...** per aggiungere una cartella di icone.
    4.  Selezionare un\'icona dal pannello. La finestra di dialogo Scegli Icona si chiude automaticamente.
8.  Premere il pulsante **Aggiungi**.
9.  Il comando macro appare nel pannello a sinistra.
10. È ora possibile selezionare il comando macro nella scheda [Barre degli strumenti](#Barre_degli_strumenti.md).


</div>



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


<div class="mw-translate-fuzzy">

Questa scheda è vuota se non viene rilevata alcuna Spaceball. Vedere: [3Dconnexion input devices](3Dconnexion_input_devices/it.md).


</div>


{{Top}}



## Temi

FreeCAD supporta i temi completi dell\'interfaccia, tramite fogli di stile .qss. Il [formato qss](https://doc.qt.io/qt-5/stylesheet-syntax.html) è molto simile al [formato css](https://it.wikipedia.org/wiki/CSS) utilizzato nelle pagine Web, aggiunge fondamentalmente metodi per fare riferimento ai diversi widget ed elementi dell\'interfaccia Qt. Puoi cambiare il tema predefinito (che prende semplicemente lo stile definito dal tuo sistema desktop) selezionando un **foglio di stile** nel menu [Preferenze di FreeCAD](Preferences_Editor#General.md).

Puoi anche creare il tuo tema se non sei soddisfatto dei temi forniti con FreeCAD, ad esempio modificando un [foglio di stile esistente](https://github.com/FreeCAD/FreeCAD/tree/master/src/Gui/Stylesheets). Il tuo nuovo foglio di stile deve essere posizionato in una cartella specifica per essere trovato da FreeCAD:

-    **%APPDATA%/FreeCAD/Gui/Stylesheets**(per Windows). La cartella **%APPDATA%** può essere trovata inserendo {{Incode|App.getUserAppDataDir()}} dalla [console di Python](Python_console/it.md).

-    **$HOME/.FreeCAD/Gui/Stylesheets**(per Linux).

-    **$HOME/Library/Application Support/FreeCAD/Gui/Stylesheets**(per macOS).


{{Top}}



## Componenti aggiuntivi 


<div class="mw-translate-fuzzy">

I componenti aggiuntivi offrono ancora un altro modo per personalizzare l\'interfaccia utente. Di seguito sono riportati alcuni componenti aggiuntivi creati dagli utenti nella comunità di FreeCAD. Possono essere scaricati tramite <img alt="" src=images/_Std_AddonMgr.svg  style="width:16px;"> [Addon Manager](Std_AddonMgr/it.md) (nota: essi sono elencati nella scheda Ambienti).


</div>

In the Workbenches category of the Addon Manager some addons by user triplus can be found:

-   <https://github.com/triplus/CubeMenu> (for {{VersionMinus|0.20}})
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
