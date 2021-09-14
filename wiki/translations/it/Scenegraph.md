# Scenegraph/it




{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

Le geometrie che appaiono nelle viste 3D di FreeCAD sono visualizzate (renderizzate) dalla libreria [Coin3d](http://en.wikipedia.org/wiki/Coin3D). Coin3D è un\'implementazione delle funzionalità standard di [OpenInventor](http://en.wikipedia.org/wiki/Open_Inventor). Anche il software [openCascade](http://en.wikipedia.org/wiki/Open_CASCADE) fornisce queste funzionalità, ma, fin dagli inizi dello sviluppo di FreeCAD, è stato deciso di non utilizzare il visualizzatore di OpenCascade e di sostituirlo con il software Coin3D in quanto più performante. Un buon modo per conoscere questa libreria è quello di consultare il manuale [Open Inventor Mentor](http://www-evasion.imag.fr/Membres/Francois.Faure/doc/inventorMentor/sgi_html/).


</div>

## Description


<div class="mw-translate-fuzzy">

[OpenInventor](http://en.wikipedia.org/wiki/Open_Inventor) è in realtà un linguaggio di descrizione della scena 3D. La scena descritta in OpenInventor viene renderizzata (visualizzata) sul vostro schermo con OpenGL. Coin3D si occupa di questo processo, quindi non è necessario che il programmatore tratti complesse chiamate a OpenGL, ma deve solo fornire un codice OpenInventor valido. Il principale vantaggio è che OpenInventor è uno standard molto conosciuto e ben documentato.


</div>


<div class="mw-translate-fuzzy">

Sostanzialmente, uno dei lavori più importanti che FreeCAD esegue per noi consiste nel tradurre le informazioni sulla geometria OpenCascade in linguaggio OpenInventor.


</div>


<div class="mw-translate-fuzzy">

OpenInventor descrive una scena 3D in forma di [scena grafica](http://en.wikipedia.org/wiki/Scene_graph) (Scenegraph), come quello seguente:


</div>

![](images/Scenegraph.gif )


<div class="mw-translate-fuzzy">

![](images/Scenegraph.gif ) immagine da [Inventor mentor](http://www-evasion.imag.fr/~Francois.Faure/doc/inventorMentor/sgi_html/index.html)


</div>


<div class="mw-translate-fuzzy">

Un grafo di scena di OpenInventor è una struttura di tipo \"grafico ad albero\" e descrive tutto ciò che fa parte di una scena 3D, come ad esempio la geometria, i colori, i materiali, le luci, ecc, e organizza tutti i dati in una struttura gerarchica, pratica e chiara. Tutto può essere raggruppato in sotto-strutture (nodi-figlio), il che consente di organizzare i contenuti della scena più o meno nel modo desiderato. Ecco un esempio di un file di OpenInventor:


</div>


{{Code|lang=bash|code=
#Inventor V2.0 ascii
 
Separator { 
    RotationXYZ {   
       axis Z
       angle 0
    }
    Transform {
       translation 0 0 0.5
    }
    Separator { 
       Material {
          diffuseColor 0.05 0.05 0.05
       }
       Transform {
          rotation 1 0 0 1.5708
          scaleFactor 0.2 0.5 0.2
       }
       Cylinder {
       }
    }
}
}}


<div class="mw-translate-fuzzy">

Come si vede, la struttura è molto semplice. Si utilizzano i nodi (separator) per organizzare i dati in blocchi, un po\' come si fa per organizzare i file in cartelle e sottocartelle. Ogni dichiarazione riguarda ciò che viene in seguito, per esempio, i primi due elementi del nostro nodo radice (root separator) sono una rotazione e una traslazione e agiscono entrambi sull\'elemento successivo, che è un nodo (separator). In tale nodo sono definiti un materiale e una ulteriore trasformazione. Pertanto, il nostro cilindro sarà influenzato da entrambe le trasformazioni, da quella che è stata applicata direttamente ad esso e da quella che è stata applicata al suo nodo (separator) genitore.


</div>


<div class="mw-translate-fuzzy">

Per organizzare la una scena, sono disponibili molti altri tipi di elementi, come gruppi, commutatori o annotazioni. Per gli oggetti si possono definire dei materiali molto complessi, con colori, texture, modalità di ombreggiatura e trasparenza. Si possono anche definire luci, punti di vista (camera) e perfino il movimento. È anche possibile incorporare parti di script nei file di OpenInventor, per definire comportamenti più complessi.


</div>


<div class="mw-translate-fuzzy">

Se siete interessati a saperne di più su OpenInventor, consultate direttamente il suo manuale più famoso: il libro [Inventor mentor](http://www-evasion.imag.fr/~Francois.Faure/doc/inventorMentor/sgi_html/index.html).


</div>


<div class="mw-translate-fuzzy">

Normalmente, in FreeCAD, non è necessario interagire direttamente con il grafo della scena di OpenInventor. Ogni oggetto in un documento di FreeCAD, sia che si tratti di un Mesh, di una forma Parte o di qualsiasi altra cosa, viene automaticamente convertito in codice OpenInventor e inserito nel grafo della scena principale che appare in una vista 3D. Questo grafo di scena viene costantemente aggiornato tutte le volte che si apportano delle modifiche, oppure si aggiungono o si rimuovono degli oggetti nel documento. In realtà, ogni oggetto (nell\'ambito App) ha un fornitore di vista (un corrispondente oggetto nell\'ambito Gui), responsabile del rilascio del codice OpenInventor.


</div>


<div class="mw-translate-fuzzy">

Potere accedere al direttamente al grafico di scena presenta comunque molti vantaggi. Ad esempio, si può modificare temporaneamente la visualizzazione di un oggetto, oppure si possono aggiungere alla scena oggetti che nel documento di FreeCAD non hanno esistenza reale, come la geometria di costruzione, i riferimenti, i suggerimenti grafici oppure strumenti quali i manipolatori oppure informazioni sullo schermo.


</div>

FreeCAD dispone di diversi strumenti per visualizzare o modificare il codice OpenInventor. Ad esempio, il seguente codice Python mostra la rappresentazione OpenInventor di un oggetto selezionato: 
```python
obj = FreeCAD.ActiveDocument.ActiveObject
viewprovider = obj.ViewObject
print viewprovider.toString()

``` Inoltre, c\'è anche un modulo Python che consente l\'accesso completo a tutto quello che è gestito da Coin3D, come il grafico di scena di FreeCAD. Continuate quindi la lettura in [Pivy](Pivy/it.md).

## Coding examples 

See [Coin3d snippets](Coin3d_snippets.md) courtesy of MariwanJ\'s research for the [Design456 Workbench](Design456_Workbench.md). The code repository of said examples can be found at <https://github.com/MariwanJ/COIN3D_Examples>.

[top](#top.md)


{{Powerdocnavi

}} 

[Category:Developer Documentation](Category:Developer_Documentation.md)
