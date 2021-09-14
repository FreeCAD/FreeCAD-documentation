# Interface Customization/it




<div class="mw-translate-fuzzy">





</div>


{{TOCright}}

## Introduzione

L\'interfaccia di FreeCAD è basata sul moderno toolkit [Qt](http://en.wikipedia.org/wiki/Qt_(toolkit)), e dispone di una organizzazione ottimale. Alcuni aspetti dell\'interfaccia possono essere personalizzati. Ad esempio, è possibile aggiungere barre degli strumenti personalizzate, con strumenti di diversi ambienti di lavoro o strumenti definiti nelle macro e creare le proprie scorciatoie da tastiera. Ma i menu e le barre degli strumenti predefinite fornite con FreeCAD e i suoi ambienti di lavoro non possono essere modificati.

![](images/Std_DlgCustomize_tab_Toolbars.png ) *La finestra di dialogo Personalizza*

## Utilizzo

1.  The commands available in the Customize dialog box depend on the workbenches that have been loaded in the current FreeCAD session. So you should first load all workbenches whose commands you want to have access to.
2.  There are several ways to invoke the <img alt="" src=images/Std_DlgCustomize.svg  style="width:16px;"> [Std DlgCustomize](Std_DlgCustomize.md) command:
    -   Select the **Tools → <img src="images/Std_DlgCustomize.svg" width=16px> Customize...** option from the menu.
    -   Right-click a toolbar area and choose **<img src="images/Std_DlgCustomize.svg" width=16px> Customize...** from the context menu.
3.  The Customize dialog box opens. For more information see [Options](#Options.md).
4.  The **Help** button does not work at this time.
5.  Press the **Close** button to close the dialog box.

## Opzioni

Nella finestra di dialogo Personalizza sono disponibili le seguenti schede:

### Comandi

![](images/Std_DlgCustomize_tab_Commands.png ) *La scheda Comandi*

In questa scheda è possibile sfogliare i comandi disponibili.

#### Sfogliare i comandi 

1.  Selezionare una categoria di comandi nel pannello **Categoria** a sinistra. Alcune categorie corrispondono alle voci del menu.
2.  Gli strumenti disponibili nella categoria selezionata sono mostrati nel pannello a destra.
3.  Passa il mouse su un comando: appare la descrizione del comando.
4.  Selezionare un comando: il testo della sua barra di stato viene visualizzato sotto i due pannelli.


{{Top}}

### Tastiera

![](images/Std_DlgCustomize_tab_Keyboard.png ) *La scheda Tastiera*

In questa scheda è possibile definire le scorciatoie da tastiera personalizzate. I collegamenti per i comandi delle macro possono essere definiti nella scheda [Macro](#Macros.md).

#### Aggiungere una scorciatoia personalizzata 

1.  Selezionare una categoria di comando dall\'elenco a discesa **Categoria**.
2.  Selezionare un comando dal pannello **Comandi**.
3.  La casella **Scorciatoia corrente** visualizza la scorciatoia corrente, se disponibile.
4.  Inserire una nuova scorciatoia nella casella di input **Digita la nuova scorciatoia**. La scorciatoia accetta fino a 4 input. Ogni input è un singolo carattere, una combinazione di uno o più tasti speciali o una combinazione di uno o più tasti speciali e un carattere. Usare **Backspace** per correggere gli errori.
5.  Se la scorciatoia è già in uso, una finestra di dialogo chiede se si desidera sostituirla e il comando a cui è assegnata la scorciatoia viene visualizzato nel pannello **Attualmente assegnata a**.
6.  Premere il pulsante **Assegna** per assegnare la nuova scorciatoia.
7.  Premere il pulsante **Cancella** per rimuovere il collegamento immesso. Questo rimuove anche il contenuto della casella **Collegamento corrente**. Notare che i collegamenti predefiniti non vengono rimossi in modo permanente. Sono ripristinati al riavvio di FreeCAD.

#### Rimuovere una scorciatoia personalizzata 

1.  Selezionare una categoria di comando dall\'elenco a discesa **Categoria**.
2.  Selezionare un comando dal pannello **Comandi**.
3.  Premere il pulsante **Ripristina**.

#### Rimuovere tutte le scorciatoie personalizzate 

1.  Premere il pulsante **Ripristina tutto**.

#### Note (Tastiera) 


<div class="mw-translate-fuzzy">

-   Le scorciatoie funzionano solo se i loro comandi vengono visualizzati nel menu standard o nel menu di un ambiente di lavoro che è stato caricato nella sessione corrente di FreeCAD o se i loro comandi vengono visualizzati su una barra degli strumenti \"visibile\".

-   In V0.19 c\'è un problema con alcuni comandi Draft. Le loro scorciatoie predefinite non funzionano e/o le scorciatoie personalizzate non possono essere assegnate.


</div>


{{Top}}

### Ambienti di lavoro 

![](images/Std_DlgCustomize_tab_Workbenches.png ) *La scheda Ambienti*

In questa scheda si può modificare l\'ordine dell\'elenco del [selettore degli ambienti](Std_Workbench/it.md). L\'elenco **Ambienti abilitati** mostra gli ambienti così come appaiono nel selettore.

#### Disabilitare un ambiente 

1.  Selezionare un ambiente nell\'elenco **Ambienti di lavoro abilitati**.
2.  Premere il pulsante **<img src="images/Button_left.svg" width=16px>**.
3.  L\'ambiente viene spostato nell\'elenco **Ambienti di lavoro disabilitati**

#### Riabilitare un ambiente 

1.  Selezionare un ambiente nell\'elenco **Ambienti di lavoro disabilitati**.
2.  Premere il pulsante **<img src="images/Button_right.svg" width=16px>**.
3.  L\'ambiente viene spostato nell\'elenco **Ambienti di lavoro abilitati**

#### Riabilitare tutti gli ambienti 

1.  Premere il pulsante **<img src="images/Button_add_all.svg" width=16px>**.

#### Cambiare la posizione di un ambiente 

1.  Selezionare un ambiente nell\'elenco **Ambienti di lavoro abilitati**.
2.  Premere il pulsante **<img src="images/Button_up.svg" width=16px>** o il pulsante **<img src="images/Button_down.svg" width=16px>**.
3.  Ripetere fino a quando l\'ambiente non si trova nella posizione desiderata.

#### Ambienti in ordine alfabetico 

1.  Premere il pulsante **<img src="images/Button_sort.svg" width=16px>**.


{{Top}}

### Barre degli strumenti 

![](images/Std_DlgCustomize_tab_Toolbars.png ) *La scheda Barre degli strumenti*

In questa scheda è possibile creare e modificare barre degli strumenti personalizzate.

#### Selezionare l\'ambiente 

1.  Nell\'elenco a discesa a destra selezionare l\'ambiente di cui si desidera modificare le barre degli strumenti personalizzate. L\'opzione {{Value|Global}} è disponibile per le barre degli strumenti personalizzate che dovrebbero essere disponibili in tutti gli ambienti.

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

1.  Selezionare la barra degli strumenti corretta nel pannello a destra. Se non viene selezionata alcuna barra degli strumenti, il comando viene aggiunto alla prima barra degli strumenti nell\'elenco.
2.  Selezionare una categoria dall\'elenco a discesa a sinistra. I comandi delle macro che sono stati impostati nella scheda [Macro](#Macros.md) vengono visualizzati nella categoria \"Macro\".
3.  Selezionare un comando dal pannello a sinistra.
4.  Oppure selezionare \'\' per aggiungere un separatore (una linea tra due pulsanti della barra degli strumenti).
5.  Premere il pulsante **<img src="images/Button_right.svg" width=16px>**.


</div>

#### Rimuovere un comando 

1.  Se necessario, espandere la barra degli strumenti nel riquadro a destra.
2.  Selezionare un comando.
3.  Premere il pulsante **<img src="images/Button_left.svg" width=16px>**.

#### Cambiare la posizione di un comando 

1.  Se necessario, espandere la barra degli strumenti nel riquadro a destra.
2.  Selezionare un comando.
3.  Premere il pulsante **<img src="images/Button_up.svg" width=16px>** o il pulsante **<img src="images/Button_down.svg" width=16px>**.
4.  Ripetere fino a quando l\'ambiente non si trova nella posizione desiderata.

#### Note (Barre degli strumenti) 

-   Le barre degli strumenti appartenenti all\'ambiente corrente vengono aggiornate immediatamente, ma dopo aver disabilitato o riattivato una barra degli strumenti è necessario cambiare ambiente (passare a un ambiente diverso e quindi tornare indietro).
-   Per aggiornare le barre degli strumenti globali è necessario cambiare ambiente (se i comandi sono stati aggiunti o rimossi) o riavviare (se l\'ordine di una barra degli strumenti è cambiato o una barra degli strumenti è stata rinominata).

-   In V0.19 c\'è un problema con alcuni comandi di Draft. Dopo averli aggiunti a una barra degli strumenti personalizzata ed essere usciti dall\'applicazione FreeCAD, il file {{FileName|user.cfg}} deve essere modificato manualmente per questi comandi. Cercare il nome della barra degli strumenti personalizzata e in quella sezione modificare il contenuto degli elementi `FCText` che iniziano con `gui_` in `DraftTools`.


{{Top}}

### Macro

![](images/Std_DlgCustomize_tab_Macros.png ) *La scheda Macro*

On this tab user macro commands can be set up. Once set up, they can be added to custom toolbars. FreeCAD uses a dedicated folder for user macros and only macros in that folder can be set up. Use the <img alt="" src=images/Std_DlgMacroExecute.svg  style="width:16px;"> [Std DlgMacroExecute](Std_DlgMacroExecute.md) command to find this folder on your system.

If you download a macro with the <img alt="" src=images/Std_AddonMgr.svg  style="width:16px;"> [Addon Manager](Std_AddonMgr.md) then make sure that you also download its icon image file. Most macros have an image link on the information page that appears in the Addon Manager. You can for example put this image file in the user macros folder.

If you want to use a macro downloaded from a different source you will have to install it manually. See [How to install macros](How_to_install_macros.md) for more information.

#### Add a macro command 

1.  In the **Macro** dropdown list select a macro.
2.  Enter a **Menu text**. This will be the name used to identify the macro command and will also appear in the toolbar if there is no icon.
3.  Optionally enter a **Tool tip**. This text will appear near the location of the mouse when you hover the toolbar icon.
4.  Optionally enter a **Status text**. This text will appear in the [status bar](Status_bar.md) when you hover the toolbar icon.
5.  Optionally enter the wiki page for the macro, if available, in the **What\'s this** input box. Enter the page name, not the full URL.
6.  Optionally enter a shortcut in the **Accelerator** input box. See [Keyboard](#Keyboard.md) for more information.
7.  To add an icon:
    1.  Press the **Pixmap** **...** button.
    2.  The Choose Icon dialog box opens.
    3.  If required press the **Icon folders...** button to add an icon folder.
    4.  Select an icon from the panel. The Choose Icon dialog box closes automatically.
8.  Press the **Add** button.
9.  The macro command appears in the panel on the left.
10. The macro command can now be selected on the [Toolbars](#Toolbars.md) tab.

#### Remove a macro command 

1.  Select the macro command in the panel on the left.
2.  Press the **Remove** button.

#### Change a macro command 

1.  Double-click the macro command in the panel on the left.
2.  Make the required changes. Note that you cannot remove the icon, you can only replace it.
3.  Press the **Replace** button.


{{Top}}

### Spaceball Motion 

This tab is blank if no Spaceball is detected. See: [3Dconnexion input devices](3Dconnexion_input_devices.md). {{Top}}

### Spaceball Buttons 

This is tab is blank if no Spaceball is detected. See: [3Dconnexion input devices](3Dconnexion_input_devices.md). {{Top}}

## Themes

FreeCAD supports complete theming of the interface, via .qss stylesheets. The [qss format](https://doc.qt.io/qt-5/stylesheet-syntax.html) is very similar to the [css format](https://en.wikipedia.org/wiki/CSS) used in web pages, it basically adds methods to reference the different widgets and elements of the Qt interface. You can change the default theme (which simply takes the style defined by your desktop system) by selecting a **style sheet** in the [FreeCAD preferences](Preferences_Editor#General.md).

You can also create your own theme if you are not satisfied with the themes that are bundled with FreeCAD, for example by editing an [existing style sheet](https://github.com/FreeCAD/FreeCAD/tree/master/src/Gui/Stylesheets). Your new style must be placed in a specific folder for it to be found by FreeCAD:

-    {{FileName|%APPDATA%/FreeCAD/Gui/Stylesheets}}(on Windows). The {{FileName|%APPDATA%}} folder can be retrieved by entering {{Incode|App.getUserAppDataDir()}} in the [Python console](Python_console.md).

-    {{FileName|$HOME/.FreeCAD/Gui/Stylesheets}}(on Linux).

-    {{FileName|$HOME/Library/Preferences/FreeCAD/Gui/Stylesheets}}(on MacOS).


{{Top}}

## Componenti aggiuntivi 

I componenti aggiuntivi offrono ancora un altro modo per personalizzare l\'interfaccia utente. Di seguito sono riportati alcuni componenti aggiuntivi creati dagli utenti nella comunità di FreeCAD. Possono essere scaricati tramite <img alt="" src=images/_Std_AddonMgr.svg  style="width:16px;"> [Addon Manager](Std_AddonMgr/it.md) (nota: essi sono elencati nella scheda Ambienti).

### CubeMenu

-   Github repository: <https://github.com/triplus/CubeMenu>

### Glass

-   Github repository: <https://github.com/triplus/Glass>.

### IconThemes

-   Github repository: <https://github.com/triplus/IconThemes>

### Launcher

-   Github repository: <https://github.com/triplus/Launcher>

### PieMenu

-   Github repository: <https://github.com/triplus/PieMenu>

### RemBench

-   Github repository: <https://github.com/triplus/RemBench>

### ShortCut

-   Github repository: <https://github.com/triplus/ShortCuts>


{{Top}}


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}} {{Interface navi}} 
