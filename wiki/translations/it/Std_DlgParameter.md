---
- GuiCommand:
   Name: Std_DlgParameter
   Name/it: Modifica parametri
   MenuLocation: Strumenti - Modifica parametri...
   Workbenches: Tutti
   SeeAlso: [Editor delle preferenze](Preferences_Editor/it.md)
---

# Std DlgParameter/it



## Descrizione

Il comando **Modifica parametri** apre l\'editor dei parametri. Nell\'editor dei parametri i parametri che controllano il comportamento di FreeCAD e dei suoi ambienti di lavoro possono essere ispezionati e facoltativamente rimossi, aggiunti o modificati. I parametri sono memorizzati in un file chiamato **user.cfg**, la posizione di questo file dipende dal sistema operativo.

Lavorare con l\'editor dei parametri richiede una certa esperienza. Per i parametri più comuni conviene usare l\'[editor delle preferenze](Preferences_Editor/it.md).

![](images/Std_DlgParameter_dialog.png ) 
*La finestra di dialogo Editor dei parametri*



## Utilizzo

1.  Selezionare l\'opzione **Strumenti → <img src="images/Std_DlgParameter.svg" width=16px> Modifica parametri...** dal menu.
2.  Viene visualizzata la finestra di dialogo Editor parametri. Per ulteriori informazioni, vedere le [Opzioni](Std_DlgParameter/it#Opzioni.md).
3.  Opzionalmente premere il pulsante **Salva nel disco** per aggiornare immediatamente il file **user.cfg**. Ciò non è indispensabile in quanto FreeCAD aggiornerà automaticamente quel file alla chiusura dell\'applicazione.
4.  Premere il pulsante **Chiudi** per chiudere l\'editor dei parametri.



## Opzioni



### Pannello di sinistra 

Il pannello di sinistra mostra un albero con gruppi di parametri e sottogruppi.

*Nel menu di scelta rapida del pannello sono disponibili le seguenti opzioni:*



#### Espandi/Riduci

1.  Se un gruppo selezionato ha uno o più sottogruppi, può essere espanso o compresso scegliendo questa opzione dal menu contestuale. Ma si può anche espandere e comprimere l\'albero nel solito modo.



#### Aggiungi sottogruppo 

1.  Selezionare un gruppo.
2.  Selezionare l\'opzione **Aggiungi sottogruppo** nel menu contestuale.
3.  Immettere un nome per il nuovo sottogruppo nella finestra di dialogo che si apre.
4.  Premere il pulsante **OK**.



#### Rimuovi gruppo 

1.  Selezionare un gruppo.
2.  Selezionare l\'opzione **Rimuovi gruppo** nel menu contestuale.
3.  Premere il pulsante **Sì** nella finestra di dialogo che si apre per confermare che si desidera rimuovere il gruppo (inclusi tutti i suoi sottogruppi e tutti i parametri del gruppo e dei suoi sottogruppi).



#### Rinomina gruppo 

1.  Selezionare un gruppo.
2.  Selezionare l\'opzione **Rinomina gruppo** nel menu contestuale.
3.  Inserire un nuovo nome
4.  Un gruppo può anche essere rinominato facendo doppio clic su di esso.



#### Esporta parametro 

1.  Selezionare un gruppo.
2.  Selezionare l\'opzione **Esporta parametro** nel menu contestuale.
3.  Immettere un nome file nella finestra di dialogo.
4.  Premere il pulsante **Salva**.



#### Importa parametro 

1.  Selezionare un gruppo che non contiene alcun sottogruppo o rimuoverli prima. Tutti i parametri esistenti nel gruppo andranno persi.
2.  Selezionare l\'opzione **Importa parametro** nel menu contestuale.
3.  Selezionare un file \*.FCParam nella finestra di dialogo.
4.  Premere il pulsante **Apri**.



### Pannello di destra 

Il pannello di destra mostra i parametri nel gruppo selezionato nel pannello di sinistra. Se questo gruppo contiene solo sottogruppi, il pannello di destra è vuoto.

*Nel menu di scelta rapida del pannello sono disponibili le seguenti opzioni:*



#### Cambia valore 

1.  Selezionare un parametro
2.  Selezionare l\'opzione **Cambia valore** nel menu contestuale.
3.  Inserire un nuovo valore nella finestra di dialogo che si apre.
4.  Premere il pulsante **OK**.
5.  Il valore di un parametro può anche essere modificato facendo doppio clic sul suo campo \"Tipo\" o \"Valore\".



#### Rimuovi la chiave 

1.  Selezionare un parametro.
2.  Selezionare l\'opzione **Rimuovi la chiave** nel menu contestuale.



#### Rinomina la chiave 

1.  Selezionare un gruppo.
2.  Selezionare l\'opzione **Rinomina la chiave** nel menu contestuale.
3.  Inserire un nuovo nome
4.  Un parametro può anche essere rinominato facendo doppio clic sul suo campo \"Nome\".



#### Nuovo elemento string 

1.  Selezionare l\'opzione **Nuovo elemento string** o **Nuovo → Nuovo elemento string** dal menu contestuale.
2.  Inserire un nome nella finestra di dialogo che si apre.
3.  Premere il pulsante **OK**.
4.  Immettere un valore nella finestra di dialogo successiva.
5.  Premere il pulsante **OK**.



#### Nuovo elemento float 

1.  Selezionare l\'opzione **Nuovo elemento float** o **Nuovo → Nuovo elemento float** dal menu contestuale.
2.  I passaggi successivi sono simili a quelli per un [Nuovo elemento string](#Nuovo_elemento_string.md)



#### Nuovo elemento integer 

1.  Seleziona l\'opzione **Nuovo elemento integer** o **Nuovo → Nuovo elemento integer** dal menu contestuale.
2.  I passaggi successivi sono simili a quelli per un [Nuovo elemento string](#New_string_item/it.md)



#### Nuovo elemento unsigned 

1.  Seleziona l\'opzione **Nuovo elemento unsigned** o **Nuovo → Nuovo elemento unsigned** dal menu contestuale.
2.  I passaggi successivi sono simili a quelli per un [Nuovo elemento string](#Nuovo_elemento_string.md)



#### Nuovo elemento Boolean 

1.  Selezionare l\'opzione **Nuovo elemento Boolean** o **Nuovo → Nuovo elemento Boolean** dal menu contestuale.
2.  I passaggi successivi sono simili a quelli per un [Nuovo elemento string](#Nuovo_elemento_string.md)



### Ordinamento

Per impostazione predefinita, i gruppi in ogni livello dell\'albero nel pannello di sinistra sono ordinati alfabeticamente e anche i parametri nel pannello di destra sono ordinati alfabeticamente. Ma l\'ordine in ciascun pannello può essere invertito facendo clic rispettivamente sull\'intestazione \"Gruppo\" o \"Nome\".



### Ricerca veloce 

La digitazione di una stringa (parziale) in questa casella di immissione espanderà completamente l\'albero nel pannello di sinistra ed evidenzierà tutti i gruppi con nomi che corrispondono al valore immesso. Se non vengono trovate corrispondenze, lo sfondo della casella di input diventerà rosso.



### Trova

1.  Nel pannello di sinistra selezionare il gruppo dal quale iniziare la ricerca. La direzione di ricerca è verso il basso. La ricerca non è ristretta al gruppo e ai suoi sottogruppi, ma verrà effettuata nel gruppo selezionato e in tutto ciò che si trova sotto di esso nell\'albero.
2.  Premere il pulsante **Trova...**.
3.  Inserire una stringa nella casella di input **Trova**. La ricerca non fa distinzione tra maiuscole e minuscole.
4.  Selezionare una o più caselle di controllo {{CheckBox|TRUE|Gruppi}}, {{CheckBox|TRUE|Nomi}} e {{CheckBox|TRUE|Valori}}. Si noti che verranno cercati solo i valori stringa.
5.  Facoltativamente (de)selezionare la casella di controllo {{CheckBox|TRUE|Controlla solo stringa intera}}.
6.  Premere il pulsante **Trova successivo** per selezionare il primo gruppo con una corrispondenza. I parametri corrispondenti non sono evidenziati individualmente. Se lo si desidera, ripetere l\'operazione fino a quando non è possibile trovare ulteriori corrispondenze.
7.  È possibile iniziare una nuova ricerca senza chiudere la finestra di dialogo. Anche in questo caso, di solito è necessario selezionare il gruppo da cui iniziare la ricerca.
8.  Usare il pulsante **Annulla** per chiudere la finestra di dialogo.



## Note

-   La pagina [Ottimizzare l\'installazione](Fine-tuning/it.md) elenca una serie di parametri che potrebbero essere di interesse.



## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

È possibile accedere alle preferenze dagli script Python utilizzando il percorso corrispondente in [Modifica parametri](Std_DlgParameter/it.md). Ad esempio, la preferenza **Modifica → Preferenze → Importa-Esporta → DXF → Opzioni di importazione → Unisci geometria** appare in **Strumenti → Modifica parametri → BaseApp → Preferences → Mod → Draft → dxfCreatePart** che ha impostazione `Boolean`. È quindi possibile accedervi in ​​Python utilizzando il seguente codice: 
```python
# get:
App.ParamGet("User parameter:BaseApp/Preferences/Mod/Draft").GetBool('dxfCreatePart')
# set:
App.ParamGet("User parameter:BaseApp/Preferences/Mod/Draft").SetBool('dxfCreatePart', True)
```

Trovare quale parametro viene utilizzato per memorizzare quale opzione dall\'editor delle preferenze può richiedere un po\' di ricerca, ma l\'[Modifica parametri](Std_DlgParameter/it.md) offre una funzione di ricerca, che dovrebbe essere d\'aiuto.

Probabilmente è una cattiva idea modificare le preferenze di altre parti di FreeCAD a meno che non lo si faccia su richiesta dell\'utente. Il setter può tuttavia essere utilizzato per impostare i parametri per il proprio ambiente di lavoro e il getter può essere utilizzato per obbedire ai parametri esistenti.





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std DlgParameter/it
