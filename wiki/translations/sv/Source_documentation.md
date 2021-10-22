# Source documentation/sv
{{TOCright}}


<div class="mw-translate-fuzzy">

FreeCADs källkod är kommenterad för att tillåta automatisk generering av html dokumentation med [Doxygen](http://www.doxygen.org).


</div>

The documentation is hosted online at the [FreeCAD API website](https://freecad.github.io/SourceDoc/). Please note that this documentation may not always be up to date; if you need more details, download FreeCAD\'s latest source code and compile the documentation yourself. If you have pressing questions about the code please ask in the developer section of the [FreeCAD forum](https://forum.freecadweb.org/index.php).

Compiling the API documentation follows the same general steps as compiling the FreeCAD executable, as indicated in the [Compile on Linux](Compile_on_Linux.md) page.

<img alt="" src=images/FreeCAD_documentation_compilation_workflow.svg  style="width:800px;">



*General workflow to compile FreeCAD's programming documentation. The Doxygen and Graphviz packages must be in the system, as well as the FreeCAD source code itself. CMake configures the system so that with a single make instruction the documentation for the the entire project is compiled into many HTML files with diagrams.*


<div class="mw-translate-fuzzy">

#### Bygga källkodsdokumentation 


</div>

### Complete documentation 


<div class="mw-translate-fuzzy">

Om du har Doxygen installerat, så är det mycket enkelt att bygga dokumentationen. Gå till din FreeCAD byggkatalog, konfigurera din källkod med CMake, skriv


</div>


```python
sudo apt install doxygen graphviz
```

Then follow the same steps you would do to compile FreeCAD, as described on the [compile on Unix](Compile_on_Linux/Unix.md) page, and summarized here for convenience.

-   Get the source code of FreeCAD and place it in its own directory `freecad-source`.
-   Create another directory `freecad-build` in which you will compile FreeCAD and its documentation.
-   Configure the sources with `cmake`, making sure you indicate the source directory, and specify the required options for your build.
-   Trigger the creation of the documentation using `make`.


```python
git clone https://github.com/FreeCAD/FreeCAD.git freecad-source
mkdir freecad-build
cd freecad-build
cmake -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 ../freecad-source
```

While you are inside the build directory issue the following instruction to create only the documentation. 
```python
make -j$(nproc --ignore=2) DevDoc
```


<div class="mw-translate-fuzzy">

och konsultera de resulterande html filerna med start i Doc/SourceDocu/html/index.html (Notera: DevDoc målet är inte giltigt för autotools byggningar)


</div>


```python
freecad-build/doc/SourceDocu/html/
```

The point of entrance to the documentation is the `index.html` file, which you can open with a web browser: 
```python
xdg-open freecad-build/doc/SourceDocu/html/index.html
```

The `DevDoc` target will generate a significant amount of data, around 5 GB of new files, particularly due to the diagrams created by Graphviz.

### Reduced documentation 

The complete documentation uses around 3Gb of disk space. An alternative, smaller version of the documentation which takes only around 600 MB can be generated with a different target. This is the version displayed on the [FreeCAD API website](https://freecad.github.io/SourceDoc/). 
```python
make -j$(nproc --ignore=2) WebDoc
```

The documentation on the [FreeCAD API website](https://freecad.github.io/SourceDoc/) is produced automatically from <https://github.com/FreeCAD/SourceDoc> . Anyone can rebuild it and submit a pull request:

-   Fork the repo at <https://github.com/FreeCAD/SourceDoc>
-   on your machine: clone the FreeCAD code (if you haven\'t yet), create a build dir for the doc, and clone the above SourceDoc repo inside. That SourceDoc will be updated when you rebuild the doc, and you\'ll be able to commit & push the results afterwards:


```python
git clone https://github.com/FreeCAD/FreeCAD
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

Som ett alternativ, så genereras dokumentationen då och då och finns [här](http://free-cad.sf.net/SrcDocu/index.html)


</div>


<div class="mw-translate-fuzzy">

#### Integrera Coin3D dokumentationen 


</div>


<div class="mw-translate-fuzzy">

På unix system, så är det möjligt att länka Coin3D\'s källk0dsdokumentation med FreeCAD\'s. Det innebär lättare navigering och kompletta släktträd för Coin relaterade klasser.


</div>


<div class="mw-translate-fuzzy">

-   På Debian och relaterade system:

:   \- Installera paketet libcoin60-doc
:   \- Packa upp filen /usr/share/doc/libcoin60-doc/html/coin.tag.gz
:   \- Generera om källkodsdokumentationen
:   Du är klar för offline läsning.


</div>


<div class="mw-translate-fuzzy">

-   Om du inte vill eller inte kan installera Coin dokumentationspaketet, så kommer länkar att genereras för att komma åt coindokumentationen online på doc.coin3D.org, om doxygen tag filen kan laddas ned under konfigureringen (wget).


</div>

## Using Doxygen 

See the [Doxygen](Doxygen.md) page for an extensive explanation on how to comment C++ and Python source code so that it can be processed by Doxygen to automatically create the documentation.

Essentially, a comment block, starting with `/**` or `///` for C++, or `##` for Python, needs to appear before every class or function definition, so that it is picked up by Doxygen. Many [special commands](Doxygen#Doxygen_markup.md), which start with `\` or `@`, can be used to define parts of the code and format the output. [Markdown syntax](Doxygen#Markdown_support.md) is also understood within the comment block, which makes it convenient to emphasize certain parts of the documentation. 
```python
/**
 * Returns the name of the workbench object.
 */
std::string name() const;

/**
 * Set the name to the workbench object.
 */
void setName(const std::string&);

/// remove the added TaskWatcher
void removeTaskWatcher(void);
```


<div class="mw-translate-fuzzy">


{{docnav/sv|Extra python modules/sv|List of Commands/sv}}


</div>


 

_

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Source documentation/sv
