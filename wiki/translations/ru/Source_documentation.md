# Source documentation/ru
<div class="mw-translate-fuzzy">





</div>


{{TOCright}}

## Обзор

Исходный код FreeCAD снабжен комментариями, что позволяет автоматически создавать документацию по программированию с использованием [Doxygen](Doxygen/ru.md), популярной системы документирования исходного кода. Doxygen может документировать написанные как на C ++, так на и Python части FreeCAD, в результате чего создаются HTML-страницы с гиперссылками на каждую задокументированную функцию и класс.

The documentation is hosted online at the [FreeCAD API website](https://freecad.github.io/SourceDoc/). Please note that this documentation may not always be up to date; if you need more details, download FreeCAD\'s latest source code and compile the documentation yourself. If you have pressing questions about the code please ask in the developer section of the [FreeCAD forum](https://forum.freecadweb.org/index.php).

Compiling the API documentation follows the same general steps as compiling the FreeCAD executable, as indicated in the [Compile on Linux](Compile_on_Linux.md) page.

<img alt="" src=images/FreeCAD_documentation_compilation_workflow.svg  style="width:800px;">



*General workflow to compile FreeCAD's programming documentation. The Doxygen and Graphviz packages must be in the system, as well as the FreeCAD source code itself. CMake configures the system so that with a single make instruction the documentation for the the entire project is compiled into many HTML files with diagrams.*

## Сборка документации исходных кодов 

### Complete documentation 

Если у вас установлен Doxygen, то собрать документацию очень просто. Также установите [Graphviz](https://www.graphviz.org/), чтобы иметь возможность создавать диаграммы, показывающие отношения между различными классами и библиотеками в коде FreeCAD. Graphviz также используется FreeCAD [ графом зависимостей](Std_DependencyGraph.md) для отображения взаимосвязей между различными объектами. 
```python
sudo apt install doxygen graphviz
```

Then follow the same steps you would do to compile FreeCAD, as described on the [compile on Linux](Compile_on_Linux.md) page, and summarized here for convenience.

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
``` Как упоминалось в [компиляция (ускорение)](Compiling_(Speeding_up)/ru.md), параметр `-j` устанавливает количество ядер ЦП, используемых для компиляции. Полученные файлы документации появятся в каталоге 
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

## Другие версии 

[Документация FreeCAD 0.12](http://free-cad.sf.net/SrcDocu/index.html), размещенная на Sourceforge.


</div>

## Объединение с документацией Coin3D 

В системах UNIX возможно связать документацию исходников Coin3D с FreeCAD-овской. Это даёт упрощение навигации и завершение диаграммы наследования для классво, производных от Coin.

-   Установите `libcoin-doc`, `libcoin80-doc` или аналогично названный пакет
-   Распакуйте архив `coin.tar.gz`, расположенный на `/usr/share/doc/libcoin-doc/html`, файлы уже могут быть распакованы в Вашей системе.
-   Повторите генерацию документации по исходным кодам.

-   Если вы установили пакет документации Coin, ссылки будут сгенерированы для доступа онлайновой документации по адресу [BitBucket](https://coin3d.bitbucket.io/Coin/). Это произойдет, если файл тега Doxygen можно загрузить во время настройки с помощью `wget`.

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





</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Source documentation/ru
