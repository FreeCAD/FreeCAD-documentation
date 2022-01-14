# FreeCAD development model project/it
**
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
**


{{TOCright}}

Questa pagina tratta del trasferimento del codice di FreeCAD in un repositorio GIT e in un Modello di sviluppo più capace. Il progetto segue le regole del processo \[<http://en.wikipedia.org/wiki/GTD#GTD_methodology>\| Getting things done\] (metodo per l\'organizzazione delle proprie azioni, per la gestione del tempo e dei progetti per \'fare in modo che le cose vengano fatte\'). I progetti sono raccolti nel [Piano di sviluppo](Development_roadmap/it.md) (Development roadmap).

## Finalità e principi 

Questo progetto mira a definire un nuovo modello di sviluppo e di amministrazione per FreeCAD. Siamo arrivati al punto in cui un repository SVN è difficile da gestire. Per i collaboratori disposti a contribuire al codice, lavorare con le patch è fastidioso e complicato. Dare a chiunque l\'accesso in scrittura al repo SVN è pericoloso. Qualcuno potrebbe involontariamente rovinare qualcosa nel sistema di base o forzare le decisioni.

Guardo perciò al processo di sviluppo di Linux, che forse al momento è troppo grande per noi. Esso utilizza Git come sistema di controllo delle versioni distribuite (DVCS), mailing list e subgestori (lieutenants).

## Risultati

## Riflessioni

### Git

-   Utilizzare Git come nuovo sistema di controllo di versione
-   Mantenere SVN (almeno per il momento)
    -   usarlo come una sorta di repository di rilascio per mantenere i flussi di lavoro dei ppa e i numeri delle revisioni migliori
    -   limitare la scrittura in SVN a Werner, Yorik e Jurgen (ramo ufficiale)
    -   tutte le altre cose, come lo sviluppo, i rami e gli esperimenti farli in Git!
    -   **Opzioni:** passare completamente a Git
        -   darebbe dare alcuni effetti collaterali nella numerazione delle versioni e nella costruzione dei ppa \....
-   Dare i diritti di scrittura (push) a chiunque sia interessato

### Sviluppo con mailing list 

Il forum ha le sue limitazioni, vorrei utilizzare una o più mailing list per gestire i rami e accogliere le proposte. Questo modo offre dei vantaggi:

-   può funzionare off-line
-   utilizza ricerche più potenti nel cliente di mail
-   non ci sono restrizione negli allegati e nelle dimensioni

### Chiarire le responsabilità 

Noi sviluppatori saremo sempre più numerosi e gli utenti faranno richieste di funzionalità contrastanti. Dobbiamo avere una struttura e la responsabilità per filtrarle e decidere in merito a tali richieste e al codice in arrivo.

#### Volontari

Adrian Przekwas:
Publicity - G+, Youtube,
Tutorials - [http://freecad-tutorial.blogspot.com](http://freecad-tutorial.blogspot.com)
Translation (unsure) - Polish (Wiki, Crowdin)

Yorik van Havre:
Software: arch module, draft module, artwork
Documentation: general wiki organization and design
Translation: french, dutch, brazilian portuguese
Publicity: articles on [http://yorik.uncreated.net/guestblog.php](http://yorik.uncreated.net/guestblog.php), G+, facebook

## Organizzazione

Le regole adottate e le informazioni sono contenute nel documento [Modello di sviluppo di FreeCAD](FreeCAD_development_model/it.md).

## Azioni successive 



[<img src="images/Property.png" style="width:16px"> Roadmap](Category_Roadmap.md)

---
[documentation index](../README.md) > [Roadmap](Category_Roadmap.md) > FreeCAD development model project/it
