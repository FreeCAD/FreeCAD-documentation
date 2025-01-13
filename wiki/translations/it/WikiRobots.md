# WikiRobots/it
**I robot sono intrinsecamente pericolosi in quanto possono causare automaticamente molti danni. Usalo con estrema cura!**



## Panoramica

Le attività ripetitive possono essere automatizzate utilizzando robot o bot, ovvero programmi software che operano sul wiki da soli.

I robot naturali e più comunemente usati per i siti wiki sono forniti da MediaWiki, sotto il nome del pacchetto Pywikibot. Vedere [Manuale:Pywikibot](http://www.mediawiki.org/wiki/Manual:Pywikibot) per informazioni complete.

In poche parole, Pywikibot è una raccolta di script Python in grado di utilizzare l\'API wiki nativa per agire sui siti wiki. Per visualizzare l\'elenco delle API per la wiki di FreeCAD, visitare <http://www.freecadweb.org/wiki/api.php>

Per utilizzare Pywikibot è necessario:

1.  installare il pacchetto Pywikibot
2.  configurare Pywikibot per lavorare sul Wiki di FreeCAD
3.  avviare gli script necessari per l\'attività da svolgere

Sono disponibili numerose informazioni su come installare, configurare e utilizzare Pywikibot. Tuttavia, tenere presente che queste informazioni, sebbene utili, possono essere fuorvianti, poiché mescolano istruzioni relative a due diverse basi di codice Pywikibot e diverse versioni della raccolta di script Pywikibot.

Di seguito si troveranno le istruzioni di base per configurare e utilizzare Pywikibot sul wiki di FreeCAD. Ciò consentirà di eseguire le attività più comuni. Per un utilizzo avanzato, fare riferimento al [Manual:Pywikibot](http://www.mediawiki.org/wiki/Manual:Pywikibot) e al codice sorgente Python.



## Installazione

Andare su <http://tools.wmflabs.org/pywikibot/> e scaricare **package/pywikipedia/core.zip** (il progetto è anche sotto github, gerrit, ecc. ma questo è un modo semplice per ottenere un pacchetto completo e autonomo).

Decomprimi il contenuto in una directory preferita.

A meno che non si voglia installare le librerie all\'interno proprie librerie Python, si ha finito (se si vuol ancora installarle, controllare il file **INSTALL** nella directory di base).

Pywikibot funziona con Python 2.6 e 2.7 senza problemi. Python 3 non è stato testato finora con FreeCAD wiki funziona altrettanto bene.



## Configurazione

Si deve salvare il seguente codice Python come file con il nome **user-config.py** nella directory di base in cui si ha decompresso **package/pywikipedia/core.zip** (per essere chiari, all\'interno della stessa directory in cui è presente già un file chiamato **user-config.py.sample**).


```python
# -*- coding: cp437  -*-
family = 'freecadwiki'
mylang = 'en'
usernames['freecadwiki']['en'] = u'<<yourWikiUserName>>'
#usernames['freecadwiki']['freecadwiki'] = u'<<yourWikiUserName>>'
console_encoding = 'cp437'
```

Nel codice sopra:

-   sostituire *\<\>* con il proprio nome utente Wiki
-   sostituire *cp437* con il proprio *console_encoding*. Per scoprire qual è la codifica della propria console, per Windows e Linux, avviare l\'interprete Python, inserire {{SystemInput|import sys}} seguito da {{SystemInput|print sys.stdout.encoding}}. Python scriverà il proprio {{SystemOutput|console_encoding}} sullo schermo.

Quindi si deve salvare il seguente codice Python come file con il nome **freecadwiki_family.py** nella sottodirectory **/pywikibot/families** (insieme agli altri **family_xxx.py ** file).


```python
# -*- coding: utf-8  -*-

__version__ = '$Id: 7f3891c3bbbfbd69c0b005de953514803d783d92 $'

dalla famiglia di importazione pywikibot


# The MediaWiki family
# user-config.py: usernames['mediawiki']['mediawiki'] = 'User name'
class Family(family.WikimediaFamily):
    def __init__(self):
        super(Family, self).__init__()
        self.name = 'freecadwiki'

        self.langs = {
            'en': 'www.freecadweb.org',
        }

    def scriptpath(self, code):
        return 'wiki'

    def path(self, code):
        return '/index.php' #The path of index.php, look at your wiki address. 
     
    def apipath(self, code):
        return '/api.php' #The path of api.php

    def version(self, code):
        # Replace with the actual version being run on your wiki
        return '1.20.3'

    def protocol(self, code):
        """
        Can be overridden to return 'https'. Other protocols are not supported.
        """
        return 'http'
        #return 'https' # My server uses https
```



## Utilizzo

Ora si è pronti per avviare gli script Pywikibot. Gli script stessi sono contenuti nella sottodirectory **/scripts**, dalla quale si può conoscere i nomi.

Per avviare gli script, aprire una shell e spostarsi nella directory di base (quella di installazione, NON la sottodirectory **/scripts**) e scrivere


{{SystemInput|python pwb.py <<scriptname>>.py -<<parameter>>}}

dove ovviamente si deve sostituire *\<\>* con il nome dello script che interessa e *\<\>* con i parametri richiesti per lo script specificato.

Per avere una descrizione dell\'utilizzo e dei parametri di qualsiasi script, utilizzare semplicemente il parametro *-help*. Ad esempio, per avere una descrizione dello script **replace.py** (uno dei più utili), digitare


{{SystemInput|python pwb.py replace.py -help}}

C\'è un altro parametro molto utile, valido per tutti gli script, chiamato *-simulate*, che permette di testare i comandi senza danneggiare il Wiki. Si consiglia di usarlo prima di andare \"dal vivo\".



## Esempi

Questo comando permetterà di accedere al wiki


{{SystemInput|pwb.py login.py}}

Questo comando stamperà un elenco di tutte le pagine contenenti un collegamento a SourceForge


{{SystemInput|pwb.py listpages.py -weblink:sourceforge.net}}

Questo comando sostituirà tutti i collegamenti al vecchio forum di SourceForge con un collegamento al nuovo forum ospitato da freecad.org


{{SystemInput|pwb.py replace.py -weblink:sourceforge.net/apps/phpbb/free-cad "sourceforge.net/apps/phpbb/free-cad" "forum.freecad.org"}}

Questo comando stamperà un elenco di tutte le pagine contenenti la parola \'PartDesign\', iniziando con la pagina intitolata \"2d Drafting Module\" e proseguendo in ordine alfabetico


{{SystemInput|pwb.py listpages.py -start:"2d Drafting Module" -grep:PartDesign}}

Questo comando sostituirà tutti i collegamenti certi al vecchio forum di SourceForge con un collegamento al nuovo forum ospitato da freecad.org nelle pagine tradotte


{{SystemInput|pwb.py replace.py -start:Translations:! "https://sourceforge.net/apps/phpbb/free-cad" "http://forum.freecad.org"}}

## Comandi correlati a FreeCAD Wiki 

Conta tutte le pagine in cui viene utilizzato un modello wiki specifico


{{SystemInput|python3 pwb.py templatecount -count GuiCommand}}

Elenca tutte le pagine in cui viene utilizzato un modello wiki specifico


{{SystemInput|python3 pwb.py templatecount -list GuiCommand}}

Sostituisci una stringa in tutte le pagine elencate nella categoria Arch


{{SystemInput|python3 pwb.py replace.py -cat:Arch}}



---
⏵ [documentation index](../README.md) > [Administration](Category_Administration.md) > [Developer](Category_Developer.md) > WikiRobots/it
