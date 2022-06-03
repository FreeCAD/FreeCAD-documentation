# Source documentation/it
<div class="mw-translate-fuzzy">


{{docnav/it|[Moduli extra di Python](Extra_python_modules/it.md)|[Elenco dei comandi](List_of_Commands/it.md)}}


</div>


{{TOCright}}


<div class="mw-translate-fuzzy">

Il codice sorgente di FreeCAD è commentato per consentire la generazione automatica della documentazione html con [Doxygen](http   *//www.doxygen.org). Questo vale sia per la parte C++ che per la parte Python del codice sorgente di FreeCAD.


</div>


<div class="mw-translate-fuzzy">

La documentazione online del sorgente si trova in <http   *//www.freecadweb.org/api/>


</div>

Compiling the API documentation follows the same general steps as compiling the FreeCAD executable, as indicated in the [Compile on Linux](Compile_on_Linux.md) page.

<img alt="" src=images/FreeCAD_documentation_compilation_workflow.svg  style="width   *800px;">



*General workflow to compile FreeCAD's programming documentation. The Doxygen and Graphviz packages must be in the system, as well as the FreeCAD source code itself. CMake configures the system so that with a single make instruction the documentation for the the entire project is compiled into many HTML files with diagrams.*

## Costruire la documentazione del codice sorgente 

### Complete documentation 


<div class="mw-translate-fuzzy">

Se Doxygen è già installato, è molto facile costruire il doc (la documentazione). Andare nella propria directory di compilazione di FreeCAD, configurare il sorgente con CMake, eseguendo


</div>


```python
sudo apt install doxygen graphviz
```

Then follow the same steps you would do to compile FreeCAD, as described on the [compile on Linux](Compile_on_Linux.md) page, and summarized here for convenience.

-   Get the source code of FreeCAD and place it in its own directory `freecad-source`.
-   Create another directory `freecad-build` in which you will compile FreeCAD and its documentation.
-   Configure the sources with `cmake`, making sure you indicate the source directory, and specify the required options for your build.
-   Trigger the creation of the documentation using `make`.


```python
git clone https   *//github.com/FreeCAD/FreeCAD.git freecad-source
mkdir freecad-build
cd freecad-build
cmake -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 ../freecad-source
```

While you are inside the build directory issue the following instruction to create only the documentation. 
```python
make -j$(nproc --ignore=2) DevDoc
```


<div class="mw-translate-fuzzy">

si possono consultare i file HTML risultanti iniziando da Doc/SourceDocu/html/index.html


</div>


```python
freecad-build/doc/SourceDocu/html/
```

The point of entrance to the documentation is the `index.html` file, which you can open with a web browser   * 
```python
xdg-open freecad-build/doc/SourceDocu/html/index.html
```


<div class="mw-translate-fuzzy">

La DevDoc è molto ingombrante, se graphviz è installato sul sistema, genera un volume dei dati maggiore di 2Gb. Un\'alternativa, può invece essere generata una versione più piccola (\~ 500Mb), che è la versione utilizzata in <http   *//www.freecadweb.org/api/> e che si ottiene con   *


</div>

### Reduced documentation 

The complete documentation uses around 3Gb of disk space. An alternative, smaller version of the documentation which takes only around 600 MB can be generated with a different target. This is the version displayed on the [FreeCAD API website](https   *//freecad.github.io/SourceDoc/). 
```python
make -j$(nproc --ignore=2) WebDoc
```

The documentation on the [FreeCAD API website](https   *//freecad.github.io/SourceDoc/) is produced automatically from <https   *//github.com/FreeCAD/SourceDoc> . Anyone can rebuild it and submit a pull request   *

-   Fork the repo at <https   *//github.com/FreeCAD/SourceDoc>
-   on your machine   * clone the FreeCAD code (if you haven\'t yet), create a build dir for the doc, and clone the above SourceDoc repo inside. That SourceDoc will be updated when you rebuild the doc, and you\'ll be able to commit & push the results afterwards   *


```python
git clone https   *//github.com/FreeCAD/FreeCAD
cd FreeCAD
mkdir build
cd build
mkdir -p doc/SourceDocu/html
cd doc/SourceDocu/html
git clone your-fork-url
cd ../../..
cmake -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 ..
make WebDoc
cd doc/SourceDocu/html
git commit
git push
```

-   Go to your fork online, and create a pull request.


<div class="mw-translate-fuzzy">

In alternativa, la documentazione viene generata di volta in volta ed è accessibile su sourceforge [quí](http   *//free-cad.sf.net/SrcDocu/index.html)


</div>

## Integrare la documentazione di Coin3D 

Sui sistemi Unix, è possibile collegare la documentazione del codice sorgente di Coin3D con quella di FreeCAD. Questo consente una navigazione più agevole e diagrammi di ereditarietà completi per le classi derivate da Coin.


<div class="mw-translate-fuzzy">

-   Su Debian e sistemi derivati   *

   *   \- Installare il pacchetto libcoin60-doc
   *   \- Decomprimere il file /usr/share/doc/libcoin60-doc/html/coin.tag.gz
   *   \- Rigenerare la documentazione del codice sorgente
   *   E si è pronti per navigare offline.


</div>


<div class="mw-translate-fuzzy">

-   Quando non si vuole o non si può installare il pacchetto della documentazione di Coin, vengono generati i collegamenti per accedere alla documentazione online di Coin in doc.coin3D.org se i file di tag doxygen possono essere scaricati al momento della configurazione (wget).


</div>

## Usare Doxygen 

See the [Doxygen](Doxygen.md) page for an extensive explanation on how to comment C++ and Python source code so that it can be processed by Doxygen to automatically create the documentation.

Essentially, a comment block, starting with `/**` or `///` for C++, or `##` for Python, needs to appear before every class or function definition, so that it is picked up by Doxygen. Many [special commands](Doxygen#Doxygen_markup.md), which start with `\` or `@`, can be used to define parts of the code and format the output. [Markdown syntax](Doxygen#Markdown_support.md) is also understood within the comment block, which makes it convenient to emphasize certain parts of the documentation. 
```python
/**
 * Returns the name of the workbench object.
 */
std   *   *string name() const;

/**
 * Set the name to the workbench object.
 */
void setName(const std   *   *string&);

/// remove the added TaskWatcher
void removeTaskWatcher(void);
```


<div class="mw-translate-fuzzy">


{{docnav/it|[Moduli extra di Python](Extra_python_modules/it.md)|[Elenco dei comandi](List_of_Commands/it.md)}}


</div>


 

[Category   *Developer Documentation](Category_Developer_Documentation.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Source documentation/it
