# Python/it
**FreeCAD è stato originariamente progettato per funzionare con Python 2.x. Questa serie si è conclusa con il rilascio 2.7.18 datato 20 aprile 2020 ed è seguita da Python 3. L'ulteriore sviluppo di FreeCAD sarà effettuato esclusivamente con Python 3 e la compatibilità con le versioni precedenti non sarà supportata.**



## Descrizione




[Python](https://www.python.org) è un linguaggio di programmazione di alto livello per scopi generali, comunemente utilizzato in applicazioni di grandi dimensioni per automatizzare alcune attività creando script o [macro](macros/it.md).

In FreeCAD, il codice Python può essere utilizzato per creare vari elementi in modo programmatico, senza la necessità di fare clic sull\'interfaccia utente grafica. Inoltre, molti strumenti e ambienti di lavoro di FreeCAD sono programmati in Python.

Vedere [Introduzione a Python](Introduction_to_Python/it.md) per conoscere il linguaggio di programmazione Python, quindi [Guida agli Script Python](Python_scripting_tutorial/it.md) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md) per iniziare a creare script in FreeCAD .



## Leggibilità

La leggibilità del codice Python è uno degli aspetti più importanti di questo linguaggio. L\'uso di uno stile chiaro e coerente all\'interno della comunità Python facilita i contributi da parte di diversi sviluppatori, poiché i programmatori Python più esperti si aspettano che il codice sia formattato in un certo modo e segua determinate regole. Quando si scrive codice Python, è consigliabile seguire [PEP8: Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/) e [PEP257: Docstring Conventions](https://www.python.org/dev/peps/pep-0257/).

Questi documenti presentano le spiegazioni in modo più intuitivo:

-   [How to Write Beautiful Python Code With PEP 8](https://realpython.com/python-pep8/)
-   [Documenting Python Code: A Complete Guide](https://realpython.com/documenting-python-code/).

## Convenzioni

In questa documentazione dovrebbero essere seguite alcune convenzioni per gli esempi Python.

Questa è una tipica firma di funzione


```python
Wire = make_wire(pointslist, closed=False, placement=None, face=None, support=None)
```

-   Gli argomenti con coppie chiave-valore sono facoltativi, con il valore predefinito indicato nella firma. Ciò significa che le seguenti chiamate sono equivalenti:


```python
Wire = make_wire(pointslist, False, None, None, None)
Wire = make_wire(pointslist, False, None, None)
Wire = make_wire(pointslist, False, None)
Wire = make_wire(pointslist, False)
Wire = make_wire(pointslist)
```


:   In questo esempio il primo argomento non ha un valore predefinito quindi dovrebbe essere sempre incluso.

-   Quando gli argomenti vengono forniti con la chiave esplicita, gli argomenti opzionali possono essere forniti in qualsiasi ordine. Ciò significa che le seguenti chiamate sono equivalenti:


```python
Wire = make_wire(pointslist, closed=False, placement=None, face=None)
Wire = make_wire(pointslist, closed=False, face=None, placement=None)
Wire = make_wire(pointslist, placement=None, closed=False, face=None)
Wire = make_wire(pointslist, support=None, closed=False, placement=None, face=None)
```

-   Le linee guida di Python sottolineano la leggibilità del codice; in particolare, le parentesi dovrebbero seguire immediatamente il nome della funzione e uno spazio dovrebbe seguire una virgola.


```python
p1 = Vector(0, 0, 0)
p2 = Vector(1, 1, 0)
p3 = Vector(2, 0, 0)
Wire = make_wire([p1, p2, p3], closed=True)
```

-   Se è necessario suddividere il codice su più righe, ciò dovrebbe essere fatto con una virgola tra parentesi quadre o parentesi quadre; la seconda riga dovrebbe essere allineata con la precedente.


```python
a_list = [1, 2, 3,
          2, 4, 5]

Wire = make_wire(pointslist,
                False, None,
                None, None)
```

-   Le funzioni possono restituire un oggetto che può essere utilizzato come base di un\'altra funzione di disegno.


```python
Wire = make_wire(pointslist, closed=True, face=True)
Window = make_window(Wire, name="Big window")
```



## Importazione

Le funzioni Python sono archiviate in file chiamati moduli. Prima di utilizzare qualsiasi funzione in quel modulo, il modulo deve essere incluso nel documento con l\'istruzione `import`.

Questo crea funzioni con prefisso, ovvero `module.function()`. Questo sistema previene conflitti di nome con funzioni che hanno lo stesso nome ma che provengono da moduli diversi. Ad esempio, le due funzioni `Arch.make_window()` e `myModule.make_window()` possono coesistere senza problemi.

Gli esempi completi dovrebbero includere le importazioni necessarie e le funzioni prefissate.


```python
import FreeCAD as App
import Draft

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1, 1, 0)
p3 = App.Vector(2, 0, 0)
Wire = Draft.make_wire([p1, p2, p3], closed=True)
```


```python
import FreeCAD as App
import Draft
import Arch

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1, 0, 0)
p3 = App.Vector(1, 1, 0)
p4 = App.Vector(0, 2, 0)
pointslist = [p1, p2, p3, p4]

Wire = Draft.make_wire(pointslist, closed=True, face=True)
Structure = Arch.make_structure(Wire, name="Big pillar")
```



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [API](Category_API.md) > [Python Code](Category_Python Code.md) > [Glossary](Category_Glossary.md) > Python/it
