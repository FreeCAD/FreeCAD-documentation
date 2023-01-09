# Licence/it
{{TOCright}}

## Licenze utilizzate in FreeCAD 

FreeCAD utilizza due licenze diverse, una per l\'applicazione stessa e una per la documentazione:

**[GNU Lesser General Public License, versione 2 or superiore (LGPL2+)](https://it.wikipedia.org/wiki/GNU_Lesser_General_Public_License)** Per tutto il codice sorgente di FreeCAD trovato nell\'archivio [official Git repository](https://github.com/FreeCAD/FreeCAD)

**[Creative Commons Attribution 3.0 License (CC-BY-3.0)](http://creativecommons.org/licenses/by/3.0/)** Per la documentazione su <https://www.freecadweb.org>

Vedere la pagina [debian copyright file](https://github.com/FreeCAD/FreeCAD/blob/master/package/debian/copyright) di FreeCAD per maggiori dettagli sulle licenze utilizzate dai diversi componenti open-source utilizzati in FreeCAD

## Impatto delle licenze 

Di seguito è riportata una spiegazione più semplificata di cosa significa per te la licenza LGPL:

#### Tutti gli utenti 

Chiunque può scaricare, utilizzare e ridistribuire FreeCAD gratuitamente, senza alcuna restrizione. La tua copia di FreeCAD è veramente tua, così come i file che produci con FreeCAD. Non sarai obbligato ad aggiornare FreeCAD dopo un certo tempo, né a modificare il tuo utilizzo di FreeCAD. L\'uso di FreeCAD non ti vincola ad alcun tipo di contratto o obbligo. Il codice sorgente di FreeCAD è pubblico e può essere ispezionato, quindi è possibile verificare che non faccia cose a tua insaputa come inviare i tuoi dati privati da qualche parte.

#### Utenti professionali 

FreeCAD può essere utilizzato liberamente per qualsiasi tipo di scopo, privato, commerciale o istituzionale. Qualsiasi versione di FreeCAD può essere distribuita e installata ovunque, qualsiasi numero di volte. Puoi anche modificare e adattare FreeCAD per i tuoi scopi senza alcuna restrizione. Tuttavia, non è possibile rendere gli sviluppatori di FreeCAD responsabili per eventuali danni o perdite aziendali che potrebbero verificarsi dall\'utilizzo di FreeCAD.

#### Sviluppatori di software open source 

È possibile utilizzare FreeCAD come base per sviluppare la propria applicazione o semplicemente estenderla creando nuovi moduli per essa. Se FreeCAD è incorporato nella tua applicazione, puoi scegliere la licenza GPL o LGPL, o qualsiasi altra licenza compatibile con LGPL, per consentire o meno l\'uso del tuo lavoro in software proprietario. Se stai sviluppando un modulo da utilizzare come estensione e non includi alcun codice di FreeCAD in esso, puoi scegliere qualsiasi licenza desideri. Tuttavia, se desideri vedere il tuo modulo utilizzato il più possibile, è una buona idea utilizzare la stessa licenza LGPL di FreeCAD stesso, in modo che parti del tuo codice possano essere riutilizzate più facilmente in altri moduli futuri o anche nello stesso FreeCAD.

#### Sviluppatori di software closed-source 

Puoi utilizzare FreeCAD come base per la tua applicazione e non sei obbligato a rendere la tua applicazione open source. La licenza LGPL, tuttavia, richiede due cose fondamentali: 1) informare chiaramente gli utenti che la propria applicazione utilizza FreeCAD e che FreeCAD è concesso in licenza LGPL e 2) separare chiaramente la propria applicazione dai componenti di FreeCAD. Questo di solito viene fatto collegandosi dinamicamente ai componenti di FreeCAD, in modo che gli utenti possano modificarlo, o rendendo disponibile agli utenti il codice sorgente di FreeCAD, insieme alle modifiche apportate. Otterrai supporto dagli sviluppatori di FreeCAD purché non sia una \"strada a senso unico\".

#### File

I modelli e gli altri file prodotti con FreeCAD non sono soggetti ad alcuna licenza di cui sopra, né vincolati ad alcun tipo di restrizione o proprietà. I tuoi file sono veramente tuoi. È possibile impostare il proprietario del file e specificare i propri termini di licenza per i file prodotti all\'interno di FreeCAD, tramite il menu File → Informazioni sul progetto.

## Dichiarazione dello sviluppatore principale 

So che la discussione sulla licenza *\"giusta\"* per l\'open source occupava una parte significativa della larghezza di banda di Internet e quindi ecco il motivo per cui, a mio avviso, FreeCAD dovrebbe avere questa.

Ho scelto la [LGPL](https://it.wikipedia.org/wiki/GNU_Lesser_General_Public_License) per il progetto e conosco i pro e i contro della LGPL e ti darò alcune ragioni per questa decisione.

FreeCAD è un misto tra una libreria e un\'applicazione, quindi la GPL sarebbe un po\' forte per questo. Impedirebbe la scrittura di moduli commerciali per FreeCAD perché impedirebbe il collegamento con le librerie di base di FreeCAD. Potresti chiedere perché i moduli commerciali? Pertanto Linux è un buon esempio. Linux avrebbe così tanto successo se la libreria GNU C fosse GPL e quindi impedisse il collegamento con applicazioni non GPL? E anche se amo la libertà di Linux, voglio anche essere in grado di utilizzare l\'ottimo driver grafico 3D NVIDIA. Comprendo e accetto il motivo per cui NVIDIA non desidera divulgare il codice del driver. Lavoriamo tutti per le aziende e abbiamo bisogno di essere pagati o almeno di cibo. Quindi per me, una coesistenza di software open source e closed source non è una brutta cosa, quando obbedisce alle regole della LGPL. Mi piacerebbe vedere qualcuno scrivere un processore di importazione/esportazione Catia per FreeCAD e distribuirlo gratuitamente o per qualche soldo. Non mi piace costringerlo a dare via più di quello che vuole. Non andrebbe bene né per lui né per FreeCAD.

Tuttavia questa decisione viene presa solo per il sistema principale di FreeCAD. Ogni autore di un modulo applicativo può prendere la propria decisione.


{{Quote|Jürgen Riegel|15 Ottobre 2006}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Licence/it
