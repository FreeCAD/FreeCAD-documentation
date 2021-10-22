# Source documentation/ja
{{TOCright}}


<div class="mw-translate-fuzzy">

FreeCADのソースコードは、[Doxygen](http://www.doxygen.org)を使ってHTMLドキュメントを自動生成するようにコメントされています。これは、FreeCADソースコードのC ++部分とPython部分の両方に当てはまります。


</div>


<div class="mw-translate-fuzzy">

オンラインのソースドキュメントはhttp://www.freecadweb.org/api/にあります。


</div>

Compiling the API documentation follows the same general steps as compiling the FreeCAD executable, as indicated in the [Compile on Linux](Compile_on_Linux.md) page.

<img alt="" src=images/FreeCAD_documentation_compilation_workflow.svg  style="width:800px;">



*General workflow to compile FreeCAD's programming documentation. The Doxygen and Graphviz packages must be in the system, as well as the FreeCAD source code itself. CMake configures the system so that with a single make instruction the documentation for the the entire project is compiled into many HTML files with diagrams.*


<div class="mw-translate-fuzzy">

#### ソースドキュメントのビルド


</div>

### Complete documentation 


<div class="mw-translate-fuzzy">

Doxygenをインストールしてあればドキュメントのビルドは非常に簡単です。FreeCADビルド用のディレクトリに移動してCMakeでソースを設定した上で次のコマンドを実行します：


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

その後でDoc/SourceDocu/html/index.htmlから始まる結果のhtmlファイルを調べてください。


</div>


```python
freecad-build/doc/SourceDocu/html/
```

The point of entrance to the documentation is the `index.html` file, which you can open with a web browser: 
```python
xdg-open freecad-build/doc/SourceDocu/html/index.html
```


<div class="mw-translate-fuzzy">

（注意：DevDocターゲットは自動ツールビルドでは有効になっていません）その性質上、ソースドキュメントは常に作業進行中状態にあります。よく起きることですが必要がある時にはためらわずに再ビルドを行なってください。 それはhttp://www.freecadweb.org/api/で使用されているバージョンも代わりに発行することによって生成することができます：


</div>

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

またこれとは別にこのドキュメントは折を見て生成されては、sourceforgeの[ここ](http://free-cad.sf.net/SrcDocu/index.html)でアクセス可能な状態で置かれています。


</div>


<div class="mw-translate-fuzzy">

#### Coin3Dドキュメントの統合


</div>


<div class="mw-translate-fuzzy">

UNIX系ではCoin3DのソースドキュメントをFreeCADのものとリンクすることが可能です。 これを行うと移動が楽になり、またCoin派生クラスの継承ダイアグラムを作成できます。


</div>


<div class="mw-translate-fuzzy">

-   Debianとそこから派生したシステムの場合：

:   \- パッケージlibcoin60-docをインストール
:   \- ファイル /usr/share/doc/libcoin60-doc/html/coin.tag.gzを展開
:   \- ソースドキュメントを再生成
:   オフラインでのブラウジングができます。


</div>


<div class="mw-translate-fuzzy">

-   もしCoinのドキュメントパッケージをインストールしたくない/できない場合、設定時(wget)にDoxygenタグファイルがダウンロード可能であればdoc.coin3D.orgにあるオンラインのCoinドキュメントへのリンクが生成されます。


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


{{docnav|Extra python modules|List of Commands}}


</div>


 

_

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Source documentation/ja
