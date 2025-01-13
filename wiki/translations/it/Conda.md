# Conda/it
## Introduzione




Questa pagina ha lo scopo di presentare Conda come gestore di pacchetti, dipendenze e ambienti per FreeCAD.

Attualmente questa pagina cataloga principalmente i collegamenti alle discussioni pertinenti del forum di FreeCAD e ad altri luoghi sul web, ma l\'intenzione è di documentare i punti salienti di questi collegamenti in questa pagina.

Vedere anche questo [video tutorial](https://www.youtube.com/watch?v=sCs8xlrw2nM) sui contenuti di questa pagina



## Motivazione

Le motivazioni per l\'utilizzo di Conda sono molteplici, così come lo scopo di Conda.

Analizziamole.



### Conda come gestore di pacchetti 

Innanzitutto, Conda è un gestore di pacchetti, simile a apt o pip.

Ciò significa che possiamo installare **pacchetti** con un semplice conda install da vari [canali](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html#what-is-a-conda-channel) come [conda-forge](https://conda-forge.org/).

Conda Forge è analogo a [Python Package Index (PyPI)](https://pypi.org/), un canale comunitario composto da migliaia di contributori e serve [freecad](https://anaconda.org/conda-forge/freecad) come pacchetto conda.



### Conda come gestore delle dipendenze 

Inoltre, Conda è un gestore delle dipendenze, anch\'esso simile a apt o pip.

Conda può gestire le dipendenze ed installarle per un progetto come FreeCAD.

Perché non usare semplicemente pip? pip funziona molto bene per gestire le dipendenze di progetti che utilizzano *solo* Python.

Conda funziona per più linguaggi ed è quindi più adatto per gestire le dipendenze di progetti come FreeCAD che hanno dipendenze in una varietà di linguaggi come C/C++ e Python.



### Conda come gestore dell\'ambiente 

Conda ha il concetto di un [ambiente](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html) che è la combinazione unica di pacchetti e versioni necessarie per eseguire una parte di software. Ad esempio, un ambiente di lavoro di FreeCAD.

Per gli ambienti è possibile \"attivarli\" e \"disattivarli\" facilmente oppure passare da una versione all\'altra dei pacchetti necessari per particolari software.

Ciò è utile per testare il comportamento di un ambiente con un particolare set di pacchetti. Ad esempio, come si comporta un ambiente di lavoro in FreeCAD 18.4 rispetto a 19?

Gli ambienti Conda ti consentono di riprodurre lo stesso esatto ambiente su macchine diverse.

Ad esempio, più macchine di sviluppo locali o un server di build remoto ospitato da Travis CI.



## Installazione di Conda 

1\. [Install Miniconda](https://docs.conda.io/en/latest/miniconda.html).

2.Verificare che l\'installazione sia riuscita e acquisisci familiarità con l\'interfaccia a riga di comando di 

## Installazione di FreeCAD utilizzando Conda 

Per prima cosa è necessario decidere se si desidera installare una versione **stable** di FreeCAD o sperimentare l\'ultimo codice main **unstable** di FreeCAD.

Le versioni stabili di FreeCAD sono disponibili sul canale conda-forge, mentre le ultime novità main di FreeCAD sono disponibili sul canale freecad/label/dev.

  Canale Conda          Stabile?
   
  conda-forge         Sì ✔️
  freecad/label/dev   No ❌

In secondo luogo, poiché è possibile creare facilmente ambienti dedicati in conda, si consiglia di crearne uno per FreeCAD.

Il comando create consente di creare un ambiente da un elenco di pacchetti specificati. Nel nostro caso, si vuole creare un ambiente chiamato \"fcenv\" (abbreviazione di ambiente FreeCAD) dal pacchetto freecad e dire a conda di cercare il pacchetto freecad utilizzando il comando del canale conda-forge. 
```python
conda create --name fcenv --channel conda-forge freecad
``` **Suggerimento:** In alternativa su può dire a conda di cercare sempre conda-forge durante l\'installazione dei pacchetti con il seguente comando: 
```python
conda config --add channels conda-forge
``` Le build settimanali possono essere installate dal canale freecad/label/dev in questo modo: 
```python
conda create --name fcenv-dev --channel freecad/label/dev freecad
```



## Discussione nel forum di FreeCAD 

-   [Let\'s talk about Conda](https://forum.freecadweb.org/viewtopic.php?t=39656)
-   [Packaging solution: (ana)conda](https://forum.freecadweb.org/viewtopic.php?f=10&t=15197)
-   [FreeCAD Conda Distribution](https://forum.freecadweb.org/viewtopic.php?f=8&t=45582)



## Vedere anche 

-   <https://docs.conda.io/en/latest/>
-   <https://conda-forge.org/docs/>
-   <https://docs.conda.io/projects/conda-build/en/latest/>
-   <https://anaconda.org/conda-forge/freecad>
-   <https://anaconda.org/freecad/freecad>
-   <https://github.com/FreeCAD/FreeCAD_Conda>
-   <https://github.com/FreeCAD/FreeCAD-AppImage>



---
⏵ [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > Conda/it
