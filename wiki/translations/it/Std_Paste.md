---
 GuiCommand:
   Name: Std_Paste
   Name/it: Incolla
   MenuLocation: Modifica , Incolla
   Shortcut: **Ctrl**+**V**
   Workbenches: Tutti
   SeeAlso: Std_Cut/it, Std_Copy/it, Std_DuplicateSelection/it
---

# Std Paste/it



## Descrizione

Il comando **Incolla** incolla gli oggetti dagli Appunti nel documento attivo.



## Utilizzo

1.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Std_Paste.svg" width=16px> [Incolla](Std_Paste/it.md)**.
    -   Selezionare l\'opzione **Modifica → <img src="images/Std_Paste.svg" width=16px> Incolla** dal menu.
    -   Selezionare l\'opzione **<img src="images/Std_Paste.svg" width=16px> Incolla** dal menu contestuale della [vista ad albero](Tree_view/it.md). Questa opzione è disponibile solo quando è stato selezionato un oggetto esistente.
    -   Usare la scorciatoia da tastiera: **Ctrl**+**V**.



## Note

-   FreeCAD cambia automaticamente i nomi interni e, a seconda delle preferenze, le etichette degli oggetti per evitare conflitti di nomi.
-   Un alias di cella di foglio di calcolo già esistente nel foglio di calcolo non viene incollato.
-   Quando si lavora in una finestra di testo di FreeCAD, in una casella di input o in un foglio di calcolo, la scorciatoia da tastiera standard **Ctrl** + **V**, in quasi tutti i casi, non chiama questo comando ma utilizza invece la funzione Incolla dal sistema operativo.
-   Non è possibile copiare e incollare oggetti nativi tra FreeCAD e altre applicazioni.



## Preferenze

Vedere anche: [Editor delle Preferenze](Preferences_Editor/it.md).

-   Per consentire etichette duplicate selezionare l\'opzione **Modifica → Preferenze... → Generale → Documento → Consenti la duplicazione delle etichette degli oggetti in uno stesso documento**. Ma questo non è raccomandato.



---
⏵ [documentation index](../README.md) > Std Paste/it
