# <img alt="" src=images/Power_user_hub.png  style="width:64px;"> Power users hub/ro

------------------------------------------------------------------------




<div class="mw-translate-fuzzy">

Acesta este locul unde veți veni dacă doriți să aveți o viziune mai profundă în FreeCAD. Aici puteți afla despre personalizarea programului FreeCAD pentru nevoile dvs.


</div>


<div class="mw-translate-fuzzy">

Una dintre cele mai interesante posibilități ale FreeCad este să puteți crea scripturi de programare foarte complexe fără a trebui să compilați nimic sau să trebuiască să atingeți codul sursă. Toate scripturile sunt făcute în limbajul [Python](http://en.wikipedia.org/wiki/Python_(programming_language)), care este un limbaj de scriere simplu și foarte puternic. Folosind comenzi simple aveți acces complet la toate părțile FreeCad. Puteți, de exemplu:

 * **Create and modify geometry**:  există un obiect care nu este disponibil în biblioteca originală FreeCad? Puteți crea acest nou obiect de la zero sau puteți adapta un șablon existent după cum este necesar.

-   **Create custom tools and commands**: În prezent, FreeCad are multe caracteristici, dar există încă o mulțime de instrumente și controale care sunt utile pentru utilizatorul final. Puteți crea cu ușurință propriile instrumente sau comenzi.
-   **Modify the interface**: Interfața FreeCad este încă foarte simplă. Dar totul ce este acolo pentru se poate extinde și adapta la nevoile dvs. De exemplu, puteți să creați bara de instrumente și să inserați instrumentele.
-   **Modify the scene representation**: FreeCad are procese separate pentru construirea și calcularea formelor geometrice și afișarea figurilor pe ecran. Aveți control complet asupra modului în care este afișată geometria pe ecran, puteți schimba reprezentarea, puteți interacționa cu aceasta sau puteți adăuga tot felul de comportamente personalizate și widget-uri de pe ecran, cum ar fi informații, trasaje, ancore sau entități temporare.


</div>


<div class="mw-translate-fuzzy">

Aceste pagini sunt în stadiu incipient de dezvoltare. Dacă nu găsiți informațiile pe care le căutați sau ați găsit informații utile undeva la care nu ne-am conectat, vă rugăm să lăsați un comentariu cu privire la _


</div>

## personalizare FreeCAD 


<div class="mw-translate-fuzzy">

-   [Interface Customization](Interface_Customization.md): Pornind de la început: Bare de instrumente și comenzi rapide
-   [Working with Macros](Macros.md): Înregistrați cu ușurință sarcini repetate adesea sau cod Python
-   [Macros recipes](Macros_recipes.md)
-   [Customize Toolbars](Customize_Toolbars.md)
-   [Installing more workbenches](Installing_more_workbenches.md)
-   [Plugin Loader](http://forum.freecadweb.org/viewtopic.php?t=10556)
-   [Addons installer.FCMacro](https://github.com/FreeCAD/FreeCAD-addons)


</div>

## Scripting in FreeCAD 

### General


<div class="mw-translate-fuzzy">

### General 

-   [Introduction to Python](Introduction_to_Python.md) - Vezi și alte tutoriale Python din partea de jos a acestei pagini.
-   [FreeCAD scripting tutorial](Python_scripting_tutorial.md) - O privire generală asupra scripting-ului Python în FreeCAD
-   [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md): Bazele scriptului de programare în Python\...
-   [Gui Command](Gui_Command.md) : Adăugarea de comenzi personalizate în GUI
-   Utilizarea de unități [Units](Units.md) de măsură diverse în FreeCAD


</div>

### Module


<div class="mw-translate-fuzzy">

Deoarece funcționalitatea FreeCAD este separată în module care se ocupă cu tipuri și aplicații speciale de date. FreeCAD are module încorporate și module de extensie (plug-in-uri). După instalarea modulelor de plugin-uri, acestea devin disponibile pentru dvs. la fel de ușor ca modulele încorporate. Modulele descrise mai jos sunt modulele implicite, incluse în fiecare instalare FreeCAD.


</div>


<div class="mw-translate-fuzzy">

-   Modulele [Builtin modules](Builtin_modules.md) sunt principalele module FreeCAD. Acestea conțin instrumente pentru manipularea configurațiilor generale FreeCAD, a documentelor și a conținutului acestora.
-   [Workbench creation](Workbench_creation.md) vă arată cum să vă creați un atelier de lucru propriu


</div>

#### Working with Meshes 


<div class="mw-translate-fuzzy">

### Working with Meshes 

-   _


</div>

#### Working with Parts 


<div class="mw-translate-fuzzy">

### Lucrul cu formele geometrice Part 

-   [The Part Workbench](Part_Workbench.md): How [Open CASCADE Technology](http://en.wikipedia.org/wiki/Open_CASCADE) instrumente și structuri utilizate în în FreeCAD
-   [Topological data scripting](Topological_data_scripting.md): Cum să interacționați cu Part Workbench
-   [PythonOCC](PythonOCC.md): Cum să delănțuiți întreaga putere a Open CASCADE
-   [Mesh to Part](Mesh_to_Part.md): conversia între tipurile de obiecte


</div>

#### Accessing the Coin scenegraph 


<div class="mw-translate-fuzzy">

### Accesul la scene grafice cu Coin 

-   Poți cu FreeCad să reprezinte scene de lucru datorită [The Coin/Inventor scenegraph](Scenegraph.md)
-   [Pivy](Pivy.md) Accesați și modificați scena grafică mulțumită lui Pivy, care este poarta de acces pentru a accesa Coin


</div>

### Controlling the Qt interface 


<div class="mw-translate-fuzzy">

### Controlarea interfeței Qt 

-   [PySide](PySide.md): Dispune de instrumentele necesare pentru a construi, a accesa și a modifica conținutul unei interfețe de utilizator
-   [Using the FreeCAD GUI](Embedding_FreeCADGui.md) într-o altă aplicație Qt cu PyQt


</div>


<div class="mw-translate-fuzzy">

### Lucrul cu obiecte parametrice 

-   [Scripted objects](Scripted_objects.md): Cum se fac obiecte 100% Python scripted în FreeCAD
-   [Drawing Workbench](Drawing_Workbench.md): Automatizarea procesului 3D-la-2D


</div>

-   [Scripted objects](Scripted_objects.md): how to make 100% Python-scripted objects.
    -   [Scripted objects with attachment](Scripted_objects_with_attachment.md): how to make scripted objects attachable to other objects.
    -   [Scripted objects saving attributes](Scripted_objects_saving_attributes.md): how to save and restore attributes of the proxy class with `__getstate__` and `__setstate__`.
    -   [Scripted objects migration](Scripted_objects_migration.md): how to migrate old scripted objects to a new class.

### Examples


<div class="mw-translate-fuzzy">

### Example

-   [Code snippets](Code_snippets.md) : O colecție de piese de cod FreeCAD Python, pentru a servi ca ingrediente în scripturile dvs. \...
-   [Line drawing function](Line_drawing_function.md): Scriind un script python care va desena o linie, întreaga procedură este descrisă pas cu pas
-   [Dialog creation](Dialog_creation.md): Cum să construiți dialoguri cu Qt Designer și să le folosiți în FreeCAD
-   [Embedding FreeCAD](Embedding_FreeCAD.md): Cum să importați FreeCAD ca modul Python în alte aplicații
-   The [Draft Workbench](Draft_Workbench.md) adaugă funcții de bază de desen 2d la Freecad. Este scris în întregime în Python, deci poate fi un bun exemplu dacă doriți să vă scrieți propriile module.
-   [FreeCAD vector math library](FreeCAD_vector_math_library.md) : Câteva funcții la îndemână pentru manipularea vectorilor FreeCAD. Această bibliotecă este, de asemenea, inclusă în modulul de proiect.


</div>

## API Functions 

Descrierea completă a API-urilor FreeCad se află pe această pagină <http://www.freecadweb.org/api/> . Pagina conține atât C++ și Python APIs, și nu este încă bine formatat, ceea ce poate fi confuz atunci când cauți cod de tip Python. O versiune mai ușor de navigat poate fi găsită la _. Rețineți că este posibil să fie incompletă, dar nu am găsit încă o modalitate de a include în mod automat pe acest wiki. Pentru mai multe informații, răsfoiți modulele direct în FreeCad.

Related: [Exposing C++ to Python](Exposing_C%2B%2B_to_Python.md)

## Advanced modification 


<div class="mw-translate-fuzzy">

-   [Start up and Configuration](Start_up_and_Configuration.md): Opțiunile de pornire și linia de comandă pentru FreeCad
-   [Installing\_on\_Windows](Installing_on_Windows.md): instalarea sub Windows
-   [Compiling FreeCAD on Windows](Compile_on_Windows.md) and [Compiling FreeCAD on Unix](Compile_on_Linux.md)
-   [Branding](Branding.md): Modificări simple pe care le puteți face la codul sursă pentru a schimba unele aspecte ale FreeCAD
-   [Extra python modules](Extra_python_modules.md) : Extindeți interpretorul Python FreeCAD cu aceste module puternice!


</div>

## Python tutorials 

Acestea sunt tutoriale generice bune, nu specifice aplicației FreeCAD, care ar putea fi interesante pentru dvs. dacă sunteți complet nou în Python.


<div class="mw-translate-fuzzy">

**Python**

-   [Official python tutorial](https://docs.python.org/2.7/tutorial/index.html) - Un tutorial foarte simplu pentru a descoperi python
-   [Non-programmer tutorial for python](http://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python) - un excelent wikibook
-   [Python for newbies](http://npt.cc.rsu.ru/user/wanderer/ODP/Python_for_Newbies.htm) - un tutorial extraordinar care acoperă principiile de bază


</div>

**PySide** - Cum se creează și se gestionează interfața Qt UI a FreeCAD de la Python

-   [PySide tutorial](http://zetcode.com/gui/pysidetutorial/) : Un tutorial platformă-agnostic care arată utilizarea PySide cu exemple
-   [PySide/PyQt tutorial](http://www.pythoncentral.io/series/python-pyside-pyqt-tutorial/) : Un tutorial ușor de citit care acoperă PySide și PyQt cu exemple
-   [PySide documentation](http://qt-project.org/wiki/PySideDocumentation) : de la Proiectul Qt (cei care au scris totul)
-   [Using QtCreator in PySide](http://qt-project.org/wiki/QtCreator_and_PySide) : de asemenea de la proiectul Qt Project
-   [PySide reference](http://srinikom.github.io/pyside-docs/index.html) : detalii nesfârșite asupra detaliilor PySide și Qt, o sursă de referință fiabilă
-   [PySide code snippets](http://nullege.com/codes/search?cq=PySide) : o bază de date căutată de fragmente de cod PySide


<div class="mw-translate-fuzzy">

Următoarele două referințe sunt PyQt specifice (nu PySide), dar pot oferi unele informații de utilizare:

-   [Basic PyQt tutorial](http://www.cs.usfca.edu/~afedosov/qttut/) : Un tutorial simplu și scurt bazat pe linux care va explica cum să lucrați cu PyQt și Qt Designer
-   [Programming Qt applications in python](http://vizzzion.org/?id=pyqt) : Un tutorial mai aprofundat care acoperă întregul proces de lucru cu Qt și Python.


</div>


<div class="mw-translate-fuzzy">

**Pivy** - Cum să interacționați cu scenele 3D ale FreeCAD

-   [Basic Pivy tutorial](http://pivy.coin3d.org/documentation/pycon) : Un tutorial foarte simplu de la site-ul oficial Pivy
-   [Introducing Pivy into studierstube](http://www.google.com.br/url?sa=U&start=3&q=http://studierstube.icg.tu-graz.ac.at/doc/pdf/PivyStudierstubeTutorial.pdf&ei=XyC1Sc2wOeCKmQem_eHnBQ&usg=AFQjCNEYhb-0DcUc6OxFVijAe1epBb-4aA) : Un document care nu este într-adevăr un tutorial, dar care arată cât de bine funcționează Pivy


</div>

## Community projects 


<div class="mw-translate-fuzzy">

Pe pagina [Community portal](FreeCAD_Community_Portal.md), puteți căuta alte proiecte bazate pe FreeCad gestionate de comunitate. Dacă ați început un nou proiect FreeCad, asigurați-vă că îl veți informa despre portalul comunitar. Dacă doriți să participați la dezvoltarea programului FreeCAD, puteți vizita această pagină și puteți vedea ce puteți face[Help FreeCAD](Help_FreeCAD.md).


</div>

-   [Scientific literature](Scientific_literature.md): articles that reference or use the FreeCAD system in different ways.


{{Powerdocnavi

}}

_

---
[documentation index](../README.md) > [Hubs](Category_Hubs.md) > Power users hub/ro
