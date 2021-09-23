# Console API/it
 **(Ottobre 2019) Non modificare queste pagine. Le informazioni sono incomplete e obsolete. Per l'API più recente, consultare la [https://www.freecadweb.org/api documentazione API autogenerata] o generare la documentazione autonomamente. Vedere [Documentazione del codice sorgente](Source_documentation/it.md).**

Questo modulo è contenuto all\'interno del modulo di FreeCAD e contiene i metodi per inviare messaggi di testo per l\'output della console di FreeCAD e della barra di stato. I messaggi hanno colore diverso secondo se sono messaggio di avviso o di errore.

Esempio: 
```python
import FreeCAD
FreeCAD.Console.PrintMessage("Hello World!\n")
```


{{APIFunction/it|GetStatus|"Log" o "Msg" o "Wrn" o "Err"|Ottiene lo stato di Log, Msg, Wrn o Error per un osservatore|una stringa di stato.}}


{{APIFunction/it|PrintError|string|Stampa un messaggio di errore nell'output|nulla}}


{{APIFunction/it|PrintLog|string|Stampa un messaggio di log nell'output|nulla}}


{{APIFunction/it|PrintMessage|string|Stampa un messaggio nell'output|nulla}}


{{APIFunction/it|PrintWarning|string|Stampa un messaggio di avviso nell'output|nulla}}


{{APIFunction/it|SetStatus|string|Imposta lo stato di Log, Msg, Wrn o Error per un osservatore| }}


 

[Category:API](Category:API.md) [Category:Poweruser Documentation](Category:Poweruser_Documentation.md)
