---
- GuiCommand:/it   Name:Std_FreezeViews   Name/it:Viste bloccate   Empty:1   MenuLocation:Visualizza → Viste bloccate → ...   Workbenches:Tutti   SeeAlso:[Pubblica la posizione della camera](Std_ViewIvIssueCamPos/it.md)---

## Introduzione


<div class="mw-translate-fuzzy">

FreeCAD può memorizzare le impostazioni della fotocamera in un massimo di 50 \"viste bloccate\". Le opzioni di menu che si occupano delle viste bloccate sono disponibili nel sottomenu {{MenuCommand|Visualizza → Viste bloccate}}. Le viste bloccate non vengono memorizzate nel documento e, se non salvate con l\'opzione **[Salva le viste\...](#Salva_le_viste....md)** del menu, andranno perse alla chiusura di FreeCAD.


</div>


<div class="mw-translate-fuzzy">

## Salva le viste\... {#salva_le_viste...}


</div>

### Descrizione

L\'opzione di menu **Salva le viste \...** salva tutte le viste bloccate esistenti in un file con l\'estensione \*.cam.

### Utilizzo

1.  Per utilizzare questa opzione devono esistere una o più viste bloccate. Una vista bloccata viene creata con l\'opzione **[Fissa la vista](#Fissa_la_vista.md)** del menu.
2.  Selezionare l\'opzione {{MenuCommand|Visualizza → Viste bloccate → Salva le viste...}} dal menu.
3.  Immettere un nome file nella finestra di dialogo.
4.  Premere il pulsante **Salva**.

### Opzioni

-   Premere il tasto **Esc** o il pulsante **Annulla** per annullare il comando.


<div class="mw-translate-fuzzy">

## Carica le viste\... {#carica_le_viste...}


</div>

### Descrizione {#descrizione_1}

L\'opzione del menu **Carica le viste\...** carica le viste bloccate da un file con l\'estensione \*.cam. Tutte le viste bloccate esistenti vengono eliminate.

### Utilizzo {#utilizzo_1}

1.  Selezionare l\'opzione {{MenuCommand|Visualizza → Viste blocate → Carica le viste...}} dal menu.
2.  Premere il pulsante **Si** nella finestra di dialogo Ripristina viste per confermare che si desidera perdere tutte le viste congelate esistenti.
3.  Selezionare un file.
4.  Premere il pulsante **Apri**.

### Opzioni {#opzioni_1}

-   Se viene visualizzata la finestra di dialogo Ripristina le viste: premere **Esc** o il pulsante **No** per interrompere il comando.
-   Se viene visualizzata la finestra di dialogo del file: premere **Esc** o il pulsante **Annulla** per interrompere il comando.

## Fissa la vista {#fissa_la_vista}

### Descrizione {#descrizione_2}


<div class="mw-translate-fuzzy">

L\'opzione del menu **Fissa la vista** memorizza le impostazioni correnti della camera in una nuova vista bloccata. Non è possibile creare più di 50 viste bloccate.


</div>

### Utilizzo {#utilizzo_2}

1.  There are several ways to invoke this option:
    -   Select the {{MenuCommand|View → Freeze display → Freeze view}} option from the menu.
    -   Use the keyboard shortcut: **Shift**+**F**.
2.  The new frozen view can be selected in the {{MenuCommand|View → Freeze display}} submenu.

## Pulisci le viste {#pulisci_le_viste}

### Descrizione {#descrizione_3}

The **Clear views** menu option deletes all existing frozen views.

### Utilizzo {#utilizzo_3}

1.  Select the {{MenuCommand|View → Freeze display → Clear views}} option from the menu.

## Ripristina la vista {#ripristina_la_vista}

### Descrizione {#descrizione_4}

For each frozen view a **Restore view** option is added with which it can be restored. The options are numbered: **Restore view 1** - **Restore view 50**.

### Utilizzo {#utilizzo_4}

1.  There are several ways to invoke this option:
    -   Select the correct {{MenuCommand|View → Freeze display → Restore view}} option from the menu.
    -   For the first 9 frozen views: use the keyboard shortcut: **Ctrl**+**1** - **Ctrl**+**9**.


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}  
