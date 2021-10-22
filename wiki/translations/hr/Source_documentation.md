# Source documentation/hr
{{TOCright}}

## Overview

The FreeCAD source code is commented to allow automatic programming documentation generation using [Doxygen](Doxygen.md), a popular source code documentation system. Doxygen can document both the C++ and Python parts of FreeCAD, resulting in HTML pages with hyperlinks to each documented function and class.

The documentation is hosted online at the [FreeCAD API website](https://freecad.github.io/SourceDoc/). Please note that this documentation may not always be up to date; if you need more details, download FreeCAD\'s latest source code and compile the documentation yourself. If you have pressing questions about the code please ask in the developer section of the [FreeCAD forum](https://forum.freecadweb.org/index.php).

Compiling the API documentation follows the same general steps as compiling the FreeCAD executable, as indicated in the [Compile on Linux](Compile_on_Linux.md) page.

<img alt="" src=images/FreeCAD_documentation_compilation_workflow.svg  style="width:800px;">



*General workflow to compile FreeCAD's programming documentation. The Doxygen and Graphviz packages must be in the system, as well as the FreeCAD source code itself. CMake configures the system so that with a single make instruction the documentation for the the entire project is compiled into many HTML files with diagrams.*

## Build source documentation 

### Complete documentation 

If you have Doxygen installed, it is very easy to build the documentation. Also install _ to show the relationships between different objects. 
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
``` As mentioned in [compiling (speeding up)](Compiling_(Speeding_up).md), the `-j` option sets the number of CPU cores used for compilation. The resulting documentation files will appear in the directory 
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

## Other versions 

[FreeCAD 0.19 development](https://iesensor.com/FreeCADDoc/0.19/) documentation built by [qingfeng.xia](http://forum.freecadweb.org/viewtopic.php?t=12613).

## Integrate Coin3D documentation 

On Unix systems it is possible to link Coin3D source documentation with FreeCAD\'s. This allows for easier navigation and complete inheritance diagrams for Coin derived classes.

-   Install the `libcoin-doc`, `libcoin80-doc`, or similarly named package.
-   Unpack the archive `coin.tar.gz` located in `/usr/share/doc/libcoin-doc/html`; the files may be already unpacked in your system.
-   Generate again the source documentation.

If you don\'t install the documentation package for Coin, the links will be generated to access the online documentation at [BitBucket](https://coin3d.bitbucket.io/Coin/). This will happen if a Doxygen tag file can be downloaded at configure time with `wget`.

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


{{docnav/hr|Extra python modules/hr|List of Commands/hr}}


</div>


 

_

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Source documentation/hr
