---
- GuiCommand:
   Name: Std_DuplicateSelection
   Name/it: Duplica la selezione
   MenuLocation: Modifica - Duplica la selezione
   Workbenches: Tutti
   SeeAlso: [Taglia](Std_Cut/it.md), [Copia](Std_Copy/it.md), [Incolla](Std_Paste/it.md)
---

# Std DuplicateSelection/it



## Descrizione

Il comando **Duplica la selezione** duplica gli oggetti all\'interno del documento attivo.



## Utilizzo

1.  Selezionare uno o più oggetti.
2.  Selezionare l\'opzione **Modifica → Duplica la selezione** dal menu.
3.  Se gli oggetti hanno delle dipendenze che non sono state selezionate, una finestra di dialogo chiede di specificare quali devono essere incluse.



## Note

-   FreeCAD cambia automaticamente i nomi interni e, a seconda delle preferenze, le etichette degli oggetti per evitare conflitti di nomi.



## Preferenze

-   Le etichette duplicate sono consentite se **Strumenti → Modifica parametri ... → BaseApp → Preferenze → Documento → DuplicateLabels** è impostato su `True`. Questa impostazione può essere modificata anche nell\'[editor delle preferenze](Preferences_Editor/it#Documento.md).





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std DuplicateSelection/it
