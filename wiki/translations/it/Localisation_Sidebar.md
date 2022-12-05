# Localisation Sidebar/it
[Localizzazione](Localisation/it.md) è il processo che permette di fornire un software con un\'interfaccia utente in più lingue. La wiki della documentazione può anche essere localizzata, come descritto in [Tradurre il wiki di FreeCAD](Localisation/it#Tradurre_il_wiki.md).

In un wiki, la sidebar (barra di navigazione laterale) è uno strumento molto importante, come documentato in [Manual:Interface/Sidebar](http://www.mediawiki.org/wiki/Manual:Interface/Sidebar).

## Tradurre la sidebar 

Ora la barra laterale è pienamente traducibile con lo stesso [Strumento di traduzione](http://www.mediawiki.org/wiki/Help:Extension:Translate) utilizzabile per tutte le pagine del wiki.

Nella wiki di FreeCAD, la barra laterale viene implementata utilizzando i modelli, che cambiano il testo in base alla lingua selezionata. I dettagli tecnici su come questa funzionalità è stata implementata sono descritti nella discussione del forum [Wiki navigation / translation](http://forum.freecadweb.org/viewtopic.php?f=21&t=9687&start=10#p80441).

### Instruzioni

Per iniziare la traduzione, aprire la pagina speciale [Special:Translate/wiki-sidebar](Special:Translate/wiki-sidebar.md).

C\'è un bug con la pagina Download. Non è possibile reindirizzare il link \"Download/lang\". Il link punta automaticamente a una pagina il cui nome è la vera traduzione di \"Download\" nella lingua corrispondente. Ad es. in italiano punta alla pagina \"Scarica\" e non è modificabile.

Il modo migliore per aggirare il problema è quello di creare questa nuova pagina e poi reindirizzarla alla pagina giusta. Per altre informazioni sul reindirizzamento vedere la pagina [Help:Editing](Help:Editing/it.md).

## Note importanti 

La maggior parte delle volte ci saranno due stringhe per ogni oggetto della barra laterale.

** {{int:sidebar-faq-target}}|sidebar-faq

Quello di sinistra rappresenta l\'obiettivo del link e quello di destra rappresenta il testo che verrà visualizzato nella barra laterale.

Si può vedere la differenza tra la due, guardando nella parte superiore del \'rettangolo di traduzione\' in cui viene visualizzato il nome della variabile. Quando il nome della variabile termina con \"-target\", significa che si sta traducendo un link. Serve per permettere al traduttore di reindirizzare le voci alle pagine tradotte aggiungendo un codice lingua alla fine del nome della pagina, ad esempio, aggiungendo \"/fr\" dopo il nome della pagina per creare un collegamento alla traduzione in francese.

Non aggiungere i codici lingua \"/ fr\", \"/ de\", \"/ es\", \"/ ru\", ecc., se la pagina tradotta non esiste in quella lingua, si interrompe il collegamento. In questo caso, non scrivere nient\'altro che il nome della pagina, altrimenti si interrompe il collegamento.

![Dove guardare](images/Translate-sidebar-instruction.png )



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Wiki](Category_Wiki.md) > Localisation Sidebar/it
