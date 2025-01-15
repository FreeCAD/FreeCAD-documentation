# License/it
## Licenze utilizzate in FreeCAD 

FreeCAD utilizza due licenze diverse, una per l\'applicazione stessa e una per la documentazione:

**[GNU Lesser General Public License, versione 2 or superiore (LGPL2+)](https://it.wikipedia.org/wiki/GNU_Lesser_General_Public_License)** Per tutto il codice sorgente di FreeCAD trovato nell\'archivio [official Git repository](https://github.com/FreeCAD/FreeCAD). Il + significa che, a scelta, si può anche utilizzare FreeCAD secondo i termini di una versione successiva della licenza, come LGPL3

**[Creative Commons Attribution 3.0 License (CC-BY-3.0)](http://creativecommons.org/licenses/by/3.0/)** Per la [documentazione](https://wiki.freecad.org) e il [sito web](https://www.freecad.org).

Vedere la pagina [debian copyright file](https://github.com/FreeCAD/FreeCAD/blob/master/package/debian/copyright) di FreeCAD per maggiori dettagli sulle licenze utilizzate dai diversi componenti open-source utilizzati in FreeCAD



## Impatto delle licenze 

Di seguito è riportata una spiegazione più semplificata di cosa significa per te la licenza LGPL:



#### Tutti gli utenti 

Chiunque può **scaricare, utilizzare e ridistribuire FreeCAD gratuitamente**, senza alcuna restrizione. La propria copia di FreeCAD è veramente propria, così come i file che si producono con FreeCAD. Non si verrà obbligati ad aggiornare FreeCAD dopo un certo tempo, né a modificare l\'utilizzo di FreeCAD. L\'uso di FreeCAD non vincola ad alcun tipo di contratto o obbligo. Il codice sorgente di FreeCAD è pubblico e può essere ispezionato, quindi è possibile verificare che non faccia cose ad insaputa come ad esempio inviare i dati personali da qualche parte.



#### Utenti professionali 

FreeCAD può essere utilizzato **liberamente per qualsiasi tipo di scopo**, privato, commerciale o istituzionale. Qualsiasi versione di FreeCAD può essere distribuita e installata ovunque, qualsiasi numero di volte. Si può anche modificare e adattare FreeCAD per i propri scopi senza alcuna restrizione. Tuttavia, non è possibile rendere gli sviluppatori di FreeCAD responsabili per eventuali danni o perdite aziendali che potrebbero verificarsi dall\'utilizzo di FreeCAD.



#### Sviluppatori di software Open-source 

È possibile utilizzare FreeCAD come base per sviluppare la propria applicazione o semplicemente estenderla creando nuovi moduli per essa. Se FreeCAD è incorporato nella propria applicazione, si può scegliere la licenza GPL o LGPL, o qualsiasi altra licenza compatibile con LGPL, per consentire o meno l\'uso del proprio lavoro in software proprietario. Se si sta sviluppando un modulo da utilizzare come estensione e non si include alcun codice di FreeCAD in esso, si può scegliere qualsiasi licenza si desideri. Tuttavia, se un giorno si desiderasse vedere il proprio modulo integrato in FreeCAD, è una buona idea utilizzare la stessa licenza LGPL di FreeCAD stesso, poiché FreeCAD accetterà solo codice con licenze LGPL, MIT o BSD.



#### Sviluppatori di software Closed-source 

La licenza LGPL consente di utilizzare FreeCAD come componente per la propria applicazione e non si è obbligati a rendere l\'applicazione open source. Si riceverà supporto dagli sviluppatori di FreeCAD purché non si tratti di una \"strada a senso unico\". La licenza prevede tuttavia due condizioni importanti:

1\) Si deve **informare chiaramente gli utenti che l\'applicazione utilizza FreeCAD** e che FreeCAD è LGPL.

2\) La licenza LGPL prevede inoltre che gli utenti debbano essere in grado di scambiare il componente di FreeCAD modificato con l\'equivalente originale di FreeCAD. Ciò andrebbe ottenuto collegandosi dinamicamente ai componenti di FreeCAD, in modo che gli utenti possano modificarlo. Tuttavia, questo è spesso difficile da ottenere con le esigenze odierne. In FreeCAD, comprendiamo che il punto importante non è limitare la libertà data agli utenti di FreeCAD dalla licenza LGPL. Quindi un equivalente del collegamento dinamico è offrire la scelta ai propri utenti, **rendendo i propri utenti consapevoli della possibilità di utilizzare FreeCAD gratuitamente**. Questo può essere fatto in diversi modi.

Se una qualsiasi delle due condizioni di cui sopra è inaccettabile per se o non può essere implementata, allora si deve rendere LGPL anche il proprio componente di FreeCAD e rilasciare il codice sorgente con tutte le modifiche apportate ad esso.

Esiste un caso speciale chiamato **derivatives**, ovvero quando si pubblica fondamentalmente una versione \"rinominata\" di FreeCAD. I derivati ​​che non sono open source sono vietati dalla licenza LGPL. La comunità di FreeCAD è attiva ed efficiente nel trovare versioni rinominate, segnalandole alle piattaforme in cui sono state trovate ed esponendole finché non vengono rimosse.

#### Files

I modelli e gli altri file prodotti con FreeCAD non sono soggetti ad alcuna licenza di cui sopra, né vincolati ad alcun tipo di restrizione o proprietà. I propri file sono veramente propri. È possibile impostare il proprietario del file e specificare i propri termini di licenza per i file prodotti all\'interno di FreeCAD, tramite il menu File → Informazioni sul progetto.

## Logo

Il logo di FreeCAD è un [marchio di proprietà della FPA (associazione del progetto FreeCAD)](https://fpa.freecad.org/documents/Trademark.pdf). Ciò significa che la [FPA](https://fpa.freecad.org) è l\'unico organismo autorizzato a dire chi ha il diritto di utilizzare o meno il logo di FreeCAD. I file del logo, che fanno parte del codice sorgente di FreeCAD o sono disponibili altrove, ad esempio su questo wiki, sono tuttora sotto le stesse licenze del resto di FreeCAD (LGPL per il codice sorgente e Creative Commons per questo wiki). Si è comunque liberi di utilizzare il logo di FreeCAD ovunque, alle stesse condizioni del resto di FreeCAD, il che significa, fondamentalmente, che si deve usarlo per fare riferimento a FreeCAD e non usarlo, ad esempio, per il proprio prodotto, o in qualsiasi altro modo che non faccia riferimento a FreeCAD.



## Dichiarazione dello sviluppatore principale 

So che la discussione sulla licenza *\"giusta\"* per l\'open source occupava una parte significativa della larghezza di banda di Internet e quindi ecco il motivo per cui, a mio avviso, FreeCAD dovrebbe avere questa.

Ho scelto la [LGPL](https://it.wikipedia.org/wiki/GNU_Lesser_General_Public_License) per il progetto e conosco i pro e i contro della LGPL e ti darò alcune ragioni per questa decisione.

FreeCAD è un misto tra una libreria e un\'applicazione, quindi la GPL sarebbe un po\' forte per questo. Impedirebbe la scrittura di moduli commerciali per FreeCAD perché impedirebbe il collegamento con le librerie di base di FreeCAD. Potresti chiedere perché i moduli commerciali? Pertanto Linux è un buon esempio. Linux avrebbe così tanto successo se la libreria GNU C fosse GPL e quindi impedisse il collegamento con applicazioni non GPL? E anche se amo la libertà di Linux, voglio anche essere in grado di utilizzare l\'ottimo driver grafico 3D NVIDIA. Comprendo e accetto il motivo per cui NVIDIA non desidera divulgare il codice del driver. Lavoriamo tutti per le aziende e abbiamo bisogno di essere pagati o almeno di cibo. Quindi per me, una coesistenza di software open source e closed source non è una brutta cosa, quando obbedisce alle regole della LGPL. Mi piacerebbe vedere qualcuno scrivere un processore di importazione/esportazione Catia per FreeCAD e distribuirlo gratuitamente o per qualche soldo. Non mi piace costringerlo a dare via più di quello che vuole. Non andrebbe bene né per lui né per FreeCAD.

Tuttavia questa decisione viene presa solo per il sistema principale di FreeCAD. Ogni autore di un modulo applicativo può prendere la propria decisione.


{{Quote|Jürgen Riegel|15 Ottobre 2006}}



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > License/it
