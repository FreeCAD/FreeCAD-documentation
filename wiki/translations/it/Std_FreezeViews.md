---
- GuiCommand:/it
   Name:Std_FreezeViews
   Name/it:Viste bloccate
   MenuLocation:Visualizza → Viste bloccate → ...
   Workbenches:Tutti
   SeeAlso:[Memorizza vista di lavoro](Std_StoreWorkingView/it.md), [Richiama vista di lavoro](Std_RecallWorkingView/it.md), [Pubblica la posizione della camera](Std_ViewIvIssueCamPos/it.md)
---

# Std FreezeViews/it



## Introduzione

FreeCAD può memorizzare le impostazioni della fotocamera in un massimo di 50 \"viste bloccate\". Le opzioni di menu che si occupano delle viste bloccate sono disponibili nel sottomenu **Visualizza → Viste bloccate**. Le viste bloccate non vengono memorizzate nel documento e, se non salvate con l\'opzione **[Salva le viste\...](#Salva_le_viste....md)** del menu, andranno perse alla chiusura di FreeCAD.



## Salva le viste 



### Descrizione

L\'opzione di menu **Salva le viste \...** salva tutte le viste bloccate esistenti in un file con l\'estensione \*.cam.



### Utilizzo

1.  Per utilizzare questa opzione devono esistere una o più viste bloccate. Una vista bloccata viene creata con l\'opzione **[Fissa la vista](#Fissa_la_vista.md)** del menu.
2.  Selezionare l\'opzione **Visualizza → Viste bloccate → Salva le viste...** dal menu.
3.  Immettere un nome file nella finestra di dialogo.
4.  Premere il pulsante **Salva**.



### Opzioni

-   Premere il tasto **Esc** o il pulsante **Annulla** per annullare il comando.



## Carica le viste 



### Descrizione 

L\'opzione del menu **Carica le viste\...** carica le viste bloccate da un file con l\'estensione \*.cam. Tutte le viste bloccate esistenti vengono eliminate.



### Utilizzo 

1.  Selezionare l\'opzione **Visualizza → Viste blocate → Carica le viste...** dal menu.
2.  Premere il pulsante **Si** nella finestra di dialogo Ripristina viste per confermare che si desidera perdere tutte le viste congelate esistenti.
3.  Selezionare un file.
4.  Premere il pulsante **Apri**.



### Opzioni 

-   Se viene visualizzata la finestra di dialogo Ripristina le viste: premere **Esc** o il pulsante **No** per interrompere il comando.
-   Se viene visualizzata la finestra di dialogo del file: premere **Esc** o il pulsante **Annulla** per interrompere il comando.



## Fissa la vista 



### Descrizione 

L\'opzione del menu **Fissa la vista** salva le impostazioni correnti della telecamera (direzione, zoom, ecc.) della [Vista 3D](3D_view/it.md) in una nuova voce nell\'elenco delle viste bloccate. L\'elenco delle viste bloccate può contenere fino a 50 viste bloccate.



### Utilizzo 

1.  Esistono diversi modi per invocare questa opzione:
    -   Selezionare l\'opzione **Visualizza → Viste bloccate → Fissa la vista** dal menu.
    -   Usare la scorciatoia da tastiera: **Shift**+**F**.
2.  La nuova visualizzazione bloccata può essere selezionata nel sottomenu **Visualizza → Viste bloccate**.



## Pulisci le viste 



### Descrizione 

L\'opzione di menu **Pulisci le viste** elimina tutte le visualizzazioni bloccate esistenti.



### Utilizzo 

1.  Selezionare l\'opzione **Visualizza → Viste bloccate → Pulisci le viste** dal menu.



## Ripristina la vista 



### Descrizione 

Per ogni vista bloccata viene aggiunta un\'opzione **Ripristina vista** con la quale può essere ripristinata. Le opzioni sono numerate: **Ripristina vista 1** - **Ripristina vista 50**.



### Utilizzo 

1.  Esistono diversi modi per invocare questa opzione:
    -   Selezionare l\'opzione corretta **Visualizza → Viste bloccate → Ripristina la vista** dal menu.
    -   Per le prime 9 visualizzazioni bloccate: utilizzare la scorciatoia da tastiera: **Ctrl**+**1** - **Ctrl**+**9**.





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std FreezeViews/it
