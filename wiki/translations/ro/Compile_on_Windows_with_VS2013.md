


<div class="mw-translate-fuzzy">

Următoarea procedură va funcționa pentru Windows Vista / 7/8, pentru XP este necesar un set de instrumente alternative VS pentru VS 2012 și 2013, care a fost finalizat cu succes cu Libpacks actuale. Pentru a viza XP (ambele și x32 și x64), este recomandat să utilizați VS2008 și LibpackFreeCADLibs\_11.0\_x86\_VC9.7z


</div>

## **Condiții Prealabile** 

### Windows Libpack 

FreeCAD este construit pe o serie de biblioteci de la terțe părți. Pentru confortul utilizatorilor, FreeCAD furnizează Libpacks care conțin toate dependențele necesare, astfel încât să nu trebuie să le compilați singuri.


<div class="mw-translate-fuzzy">

Mai întâi va trebui să descărcați în Windows Libpack. FreeCAD Windows Libpacks sunt disponibile aici: <http://sourceforge.net/projects/free-cad/files/FreeCAD%20LibPack/>


</div>


<div class="mw-translate-fuzzy">

Libpacks sunt disponibile pentru x32 și x64 pentru VC12 (Visual Studio 2013), VC11(Visual Studio 2012), and VC9(Visual Studio 2008) Libpacks va lucra atât cu edițiile Professional și Express / Community din Visual Studio. Alegeți Libpack funcție de arhitectura de sistem și de Compilator.


</div>


<div class="mw-translate-fuzzy">

Presupunând că Win Vista sau ulterior, x64 și planificați să folosiți VS2013 Community Edition alegeți:


</div>


<div class="mw-translate-fuzzy">

FreeCADLibs\_11.0\_x64\_VC12.7z


</div>

Extrageți Libpackul într-un director de pe hard disk dvs.

Puteți descărca 7-zip dacă aveți nevoie de el aici: <http://www.7-zip.org/>

### Codul Soursă 

#### Utilizând Git(de preferat) 

Pasul următor, trebuie săinstalați git pentru a putea descărca codul sursă. Puteți luat Git de aici: <http://git-scm.com/downloads>

Some information how to set-up a local tracking branch and a working branch can be found here:


<div class="mw-translate-fuzzy">

<http://www.freecadweb.org/wiki/index.php?title=Source_code_management>


</div>

To create a local tracking branch and download the source code you need to open a terminal(command prompt) and cd to the directory you want the source, then type:

git clone <git://git.code.sf.net/p/free-cad/code> free-cad-code

Now you have the source code and the tools you\'ll need to compile FreeCAD on Windows.


<div class="mw-translate-fuzzy">

#### Download Snapshot .zip(Alternate)This is Source Cade Snapshot not Development Snapshot pre-compiled binaries. 

<http://sourceforge.net/p/free-cad/code/ci/master/tarball>


</div>

You will need to extract this to a directory using 7zip or Window\'s default .zip extractor.

**NOTE: In order for Cmake to properly update your \"About FreeCAD\" information git must be installed and be present in your PATH environment variable, Therefore downloading with git is preferred.**

### Cmake

Next you will need Cmake, you can get it here: <http://www.cmake.org/download/>

FreeCAD 0.15.xxxx master will configure and generate with Cmake 2.x.x or 3.x.x, you can download the latest version. Older versions of FreeCAD require Cmake 2.x.x You should choose the non-default option to add Cmake to your system PATH environment variable.

### Visual Studio 

Lastly you will need the C-compiler. MS VS 12 2013 Community Edition Update 4 is Free for personal and Open Source Projects. It can be downloaded here:

<http://www.visualstudio.com/en-us/news/vs2013-community-vs.aspx>

## **Configuring and Generating with Cmake** 

### First Pass 

Start the CMake GUI by double-clicking on the desktop icon created during installation.

Specify source folder (This is where you cloned or extracted the source code)

Specify build folder (This is where you want to build the source, if it doesn\'t exist Cmake will prompt you to create it)

Click Configure

Specify the generator as Visual Studio 12 x64(or the alternate C-Compiler you are using)

This will begin configuration and should fail because the location of FREECAD\_LIBPACK\_DIR is unset.

Expand the FREECAD category and set: 
```python
FREECAD_LIBPACK_DIR          "...\Path\to\Libpack" (Ex: C:\user\USERNAME\FreeCADLibs_11.0_x64_VC12)
FREECAD_USE_EXTERNAL_PIVY    (Check)
FREECAD_USE_FREETYPE         (Check)
``` FREETYPE is optional. It is necessary to take advantage of the DRAFT Work Bench\'s Shape String functionality. Under normal situations it is a desirable option.

### Configure and Generate 

Click Configure again (There should be no errors)

Click Generate (missing doxgen is OK, unless you are a developer and need the source documentation)

Close Cmake

## **Dependencies**

**Copy The Libpack\\bin folder into the new build folder CMake created.**

You could put the Libpack in your system PATH environment variable. but you still are required to copy some files?

## **Building with Visual Studio** 

Start Visual Studio 12 2013 by clicking on the desktop icon created at installation.

Open the project by: File -\> Open -\> Project/Solution

Open FreeCAD\_Trunk.sln from the build folder CMake created

Switch the Solutions Configuration drop down at the top to **Release** **X64**

Build -\> Build Solution

This will take a long time\...

Dacă nu primiți nici un mesaj de eroare. Ieșiți din Visual Studio și porniți FreeCAD făcând dublu clic pe pictograma FreeCAD din directorul directorului Build.




[Category:Developer\_Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Developer{{\#translation:}}](Category:Developer.md)
