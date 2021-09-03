


{{TOCright}}


<div class="mw-translate-fuzzy">

## Programarea script Python in FreeCAD 

FreeCAD este construit de la zero pentru a fi controlat total de scripturile Python. Aproape toate componentele FreeCAD, cum ar fi interfața, conținutul scenelor și chiar reprezentarea acestui conținut în vizualizările 3D, sunt accesibile din interpretorul Python încorporat sau din propriile dvs. scripturi. Drept urmare, FreeCAD este probabil una dintre aplicațiile de inginerie cele mai profunde disponibile astăzi.


</div>

FreeCAD is built from scratch to be totally controlled by Python scripts. Almost all parts of FreeCAD, such as the interface, the scene contents, and even the representation of this content in the 3D views, are accessible from the built-in Python interpreter or from your own scripts. As a result, FreeCAD is probably one of the most deeply customizable engineering applications available today.


<div class="mw-translate-fuzzy">

Dacă nu sunteți familiarizat cu Python, vă recomandăm să căutați tutoriale pe internet și să vă aruncați o privire rapidă asupra structurii sale. Python este un limbaj de programare foarte ușor de învățat, mai ales pentru că poate fi rulat în interiorul unui interpretor, unde comenzile simple, chiar până la finalizarea programelor, pot fi executate în zbor fără a fi nevoie să compilați nimic. FreeCAD are un interpretor Python încorporat. Dacă nu vedeți fereastra etichetată \"Consola Python\" așa cum se arată mai jos, o puteți activa sub consola View -\> Panels -\> Python pentru a deschide interpretorul.


</div>


<div class="mw-translate-fuzzy">

### Interpretorul

Din interpretor, puteți accesa toate modulele Python instalate de sistem, precum și modulele FreeCAD încorporate și toate modulele FreeCAD suplimentare instalate ulterior. Imaginea de mai jos prezintă interpretorul Python:


</div>

From the interpreter, you can access all your system-installed Python modules, as well as the built-in FreeCAD modules, and all additional FreeCAD modules you installed later. The screenshot below shows the Python interpreter:

![The FreeCAD Python interpreter](images/screenshot_pythoninterpreter.jpg )


<div class="mw-translate-fuzzy">

Din interpretor, puteți executa codul Python și puteți naviga prin clasele și funcțiile disponibile. FreeCAD oferă un browser al claselor foarte util pentru explorarea noii tale lumi FreeCAD: Când introduceți numele unei clase cunoscute, urmată de un punct (adică doriți să adăugați ceva din acea clasă), se deschide o fereastră de browser de clasă, unde puteți naviga între subclasele și metodele disponibile. Când selectați ceva, este afișat un text de ajutor asociat (dacă există):


</div>

![The FreeCAD class browser](images/screenshot_classbrowser.jpg )


<div class="mw-translate-fuzzy">

Așa că, începeți aici tastând **App.** ori **Gui.** și priviți ce e tâmplă. O altă modalitate mai generală de a explora conținutul modulelor și claselor este utilizarea comenenzii Python\'print dir()\'. De exemplu, tastați **print dir()** și veți obține o listă a tuturor modulelor încărcat curent în FreeCAD. **print dir(App)** vă va arăta tot ceea ce este în interiorul modulelro App, etc.


</div>


<div class="mw-translate-fuzzy">

O altă caracteristică utilă a interpretului este posibilitatea de a reveni prin istoria comenzilor și de a recupera o linie de cod pe care ați introdus-o deja mai devreme. Pentru a naviga prin istoricul comenzilor, trebuie doar să le utilizați CTRL+UP or CTRL+DOWN.


</div>

Dacă faceți clic dreapta în fereastra interpretului, aveți și alte câteva opțiuni, cum ar fi copierea întregului istoric (util atunci când doriți să experimentați lucrurile înainte de a face un script complet al acestora) sau introduceți un nume de fișier cu cale completă.

[top](#top.md)


<div class="mw-translate-fuzzy">

### Python Help 

În meniul de ajutor al FreeCAD veți găsi o intrare intitulată \"Ajutor Python\", care va deschide o fereastră de browser care conține o documentație completă, generată în timp real, a tuturor modulelor Python disponibile pentru interpretorul FreeCAD, inclusiv modulele Python și FreeCAD încorporate , modulele instalate în sistem și modulele suplimentare FreeCAD. Documentația disponibilă depinde de efortul fiecărui dezvoltator de module în documentarea codului său, dar, de obicei, modulele Python au o reputație de a fi destul de bine documentate. Fereastra FreeCAD trebuie să rămână deschisă pentru ca acest sistem de documentare să funcționeze.


</div>

In the FreeCAD **Help** menu, you\'ll find an entry labeled **Automatic python modules documentation**, which will open a browser window containing a complete, realtime-generated documentation of all Python modules available to the FreeCAD interpreter, including Python and FreeCAD built-in modules, system-installed modules, and FreeCAD additional modules. The documentation available there depends on how much effort each module developer put into documenting his code, but Python modules have a reputation for being fairly well documented. Your FreeCAD window must stay open for this documentation system to work. The entry **Python scripting documentation** will give you a quick link to the [Power users hub](Power_users_hub.md) wiki section.

[top](#top.md)


<div class="mw-translate-fuzzy">

## Module integrate 

Deoarece FreeCAD este proiectat să ruleze fără o interfață grafică de utilizator (GUI), aproape toate funcționalitățile sale sunt separate în două grupuri: funcționalitatea Core, numită \"App\", și funcționalitatea GUI, numită \"Gui\". Deci, cele două module principale FreeCAD încorporate se numesc App și Gui. Aceste două module pot fi accesate, de asemenea, din scripturile din afara interpretului, prin numele \"FreeCAD\" și respectiv \"FreeCADGui\".


</div>

Since FreeCAD is designed so that it can also be run without a Graphical User Interface (GUI), almost all its functionality is separated into two groups: Core functionality, named `App`, and GUI functionality, named `Gui`. These two modules can also be accessed from scripts outside of the interpreter, by the names `FreeCAD` and `FreeCADGui` respectively.


<div class="mw-translate-fuzzy">

-   In **App module**, veți găsi totul în legătură cu aplicația în sine, cum ar fi metodele de deschidere sau închidere a fișierelor și documentelor, cum ar fi setarea documentului activ sau listarea conținutului acestuia.


</div>


<div class="mw-translate-fuzzy">

-   In **Gui module**, veți găsi instrumente pentru accesarea și gestionarea elementelor Gui, cum ar fi Atelierele de lucru și barele lor de instrumente și, mai interesant, reprezentarea grafică a conținutului FreeCAD.


</div>


<div class="mw-translate-fuzzy">

Afișarea întregului conținut al acestor module este o sarcină puțin contraproductivă, deoarece acestea cresc destul de repede cu dezvoltarea FreeCAD. Dar cele două instrumente de navigare furnizate (browserul de clasă și Python help) vă vor oferi, în orice moment, o documentație completă și actualizată a acestor module.


</div>

[top](#top.md)


<div class="mw-translate-fuzzy">

### Obiectele App și Gui 

Așa cum am spus, în FreeCAD, totul este separat între nucleu și reprezentare. Aceasta include și obiectele 3D. Puteți accesa definirea proprietăților obiectelor (numite funcții în FreeCAD) prin modulul App și modificați modul în care sunt reprezentate pe ecran prin modulul Gui. De exemplu, un cub are proprietăți care îl definesc (cum ar fi lățimea, lungimea, înălțimea) stocate într-un obiect App și proprietăți de reprezentare (cum ar fi culoarea fețetelor, modul de desenare) stocate într-un obiect Gui corespunzător.


</div>

As already mentioned, in FreeCAD everything is separated into core and representation. This includes the 3D objects. You can access defining properties of objects (called features in FreeCAD) via the `App` module, and change the way they are represented on screen via the `Gui` module. For example, a cube has properties that define it (like width, length, height) that are stored in an `App` object, and representation properties (like faces color, drawing mode) that are stored in a corresponding `Gui` object.

Acest mod de a face lucrurile permite o gamă largă de utilizări, cum ar fi ca algoritmii să funcționeze numai pe partea de definire a caracteristicilor, fără a avea nevoie să aibă grijă de nicio parte vizuală sau chiar să redirecționeze conținutul documentului la o aplicație non-grafică ca liste, foi de calcul sau analiza elementului finit.


<div class="mw-translate-fuzzy">

Pentru fiecare obiect App din document, există un obiect Gui corespunzător. De fapt documentul în sine are atât obiecte App cât și obiecte Gui. Acest lucru, desigur, este valabil numai când rulați FreeCAD cu interfața sa completă. În versiunea de linie de comandă nu există nici o interfață grafică, astfel încât numai obiectele App sunt disponibile. Rețineți că partea Gui a obiectelor este re-generată de fiecare dată când un obiect App este marcat ca fiind \"pentru a fi recalculat\" (de exemplu, când unul dintre parametrii lui se modifică), astfel încât modificările pe care le-ați fi putut face direct la obiectul Gui pot fi pierdute.


</div>


<div class="mw-translate-fuzzy">

Pentru a acesa partea App a unui obiect oarecare, scrieți:


</div>


```python
myObject = App.ActiveDocument.getObject("ObjectName")
```


<div class="mw-translate-fuzzy">

unde \"ObjectName\" este numele obiectului dvs. Puteți de asemenea tasta:


</div>


```python
myObject = App.ActiveDocument.ObjectName
```


<div class="mw-translate-fuzzy">

Pentru a accesa partea Gui a aceluiași obiect, scrieți:


</div>


```python
myViewObject = Gui.ActiveDocument.getObject("ObjectName")
```


<div class="mw-translate-fuzzy">

unde \"ObjectName\" este numele obeictului duvs. Puteți de asemena tasta:


</div>


```python
myViewObject = App.ActiveDocument.ObjectName.ViewObject
```


<div class="mw-translate-fuzzy">

Dacă nu aveți nici un GUI (de exemplul sunten în modul linie-de-comandă), ultima linie va returna \'None\'.


</div>

[top](#top.md)


<div class="mw-translate-fuzzy">

### Obiectele Documentului 

În FreeCAD, toată munca dvs. se află în interiorul Documentelor. Un document conține geometria și poate fi salvat într-un fișier. Mai multe documente pot fi deschise în același timp. Documentul, ca geometria conținută în interior, are obiecte App și Gui. Obiectul App conține definițiile de geometrie reale, în timp ce obiectul Gui conține vederile diferite ale documentului. Puteți deschide mai multe ferestre, fiecare vizionând munca dvs. cu un alt factor de zoom sau unghi de vedere diferit. Aceste viziuni fac parte din obiectul Gui al documentului dvs.


</div>

In FreeCAD all your work resides inside documents. A document contains your geometry and can be saved to a file. Several documents can be opened at the same time. The document, like the geometry contained inside, has `App` and `Gui` objects. The `App` object contains your actual geometry definitions, while the `Gui` object contains the different views of your document. You can open several windows, each one viewing your work with a different zoom factor or from a different direction. These views are all part of your document\'s `Gui` object.


<div class="mw-translate-fuzzy">

Pentru a accesa partea App a documentului curent deschis (activ), scrieți:


</div>


```python
myDocument = App.ActiveDocument
```

Pentru a crea un nou documente, scrieți:


```python
myDocument = App.newDocument("Document Name")
```


<div class="mw-translate-fuzzy">

Pentru a accesa partea Gui documentul deschis (activ), tastați:


</div>


```python
myGuiDocument = Gui.ActiveDocument
```

Pentru a accesa vederea curentă, scrieți:


```python
myView = Gui.ActiveDocument.ActiveView
```

[top](#top.md)


<div class="mw-translate-fuzzy">

## Utilizarea de module adiționale 

Modulele FreeCAD și FreeCADGui sunt singurele responsabile pentru crearea și gestionarea obiectelor din documentul FreeCAD. Ele nu fac de fapt nimic, cum ar fi crearea sau modificarea geometriei. Aceasta deoarece această geometrie poate fi de mai multe tipuri și astfel este gestionată de module suplimentare, fiecare responsabil pentru gestionarea unui anumit tip de geometrie. De exemplu, [Part Workbench](Part_Workbench.md) utilizează kernelul OpenCascade și, prin urmare, este capabil să creeze și să manipuleze [B-rep](http://en.wikipedia.org/wiki/Boundary_representation) type geometry, ceea ce este construit pentru OpenCascade. Modul [Mesh Workbench](Mesh_Workbench.md) poate construi și modifica obiecte tip plase. În acest fel, FreeCAD este capabil să gestioneze o mare varietate de tipuri de obiecte, care pot coexista în același document, iar noi tipuri pot fi adăugate cu ușurință în viitor.


</div>

The `FreeCAD` and `FreeCADGui` modules are only responsible for creating and managing objects in the FreeCAD document. They don\'t actually do anything more such as creating or modifying geometry. This is because that geometry can be of several types, and therefore requires additional modules, each responsible for managing a certain geometry type. For example, the [Part Workbench](Part_Workbench.md), using the OpenCascade kernel, is able to create and manipulate [BRep](http://en.wikipedia.org/wiki/Boundary_representation) type geometry. Whereas the [Mesh Workbench](Mesh_Workbench.md) is able to build and modify mesh objects. In this manner FreeCAD is able to handle a wide variety of object types, that can all coexist in the same document, and new types can easily be added in the future.

[top](#top.md)


<div class="mw-translate-fuzzy">

### Crearea obiectelor 

Fiecare modul are propriul mod de a trata geometria sa, dar un lucru pe care, de obicei, pot să-l facă este să creeze obiecte în document. Dar documentul FreeCAD este, de asemenea, conștient de tipurile de obiecte disponibile furnizate de module:


</div>

Each module has its own way of dealing with geometry, but one thing they usually all can do is create objects in the document. But the FreeCAD document is also aware of the available object types provided by the modules:


```python
FreeCAD.ActiveDocument.supportedTypes()
```


<div class="mw-translate-fuzzy">

vă va lista toate obiectele posibile pe care le puteți crea. De exemplu, să creăm o plasă (tratată de modulul Mesh/Plasă) și o Piesă (tratată de modulul Part/Piesă):


</div>


```python
myMesh = FreeCAD.ActiveDocument.addObject("Mesh::Feature", "myMeshName")
myPart = FreeCAD.ActiveDocument.addObject("Part::Feature", "myPartName")
```


<div class="mw-translate-fuzzy">

Primul argument este tipul de obiect, al doilea este numele obiectului. Cele două obiecte arată aproape la fel: nu conțin încă nicio geometrie și majoritatea proprietăților lor sunt aceleași când le inspectați cu dir(myMesh) și dir(myPart). Cu o excepție, myMesh are o proprietate \"Mesh\" și \"Part\" are o proprietate \"Shape\". Acesta este locul în care sunt stocate datele de Plasă și Piesă. De exemplu, să creăm un cub Part și să îl stocăm în obiectul myPart:


</div>


```python
import Part
cube = Part.makeBox(2, 2, 2)
myPart.Shape = cube
```


<div class="mw-translate-fuzzy">

Puteți încerca să stocați cubul în interiorul proprietății Mesh-ului obiectului myMesh, va veni o eroare în care se plânge despre tipul greșit. Aceasta se datorează faptului că aceste proprietăți sunt făcute pentru a stoca numai un anumit tip. În proprietatea MyMesh a Mesh, puteți salva numai chestii create cu modulul Mesh. Rețineți că majoritatea modulelor au, de asemenea, o comandă rapidă pentru a adăuga geometria lor la document:


</div>


```python
import Part
cube = Part.makeBox(2, 2, 2)
Part.show(cube)
```

[top](#top.md)


<div class="mw-translate-fuzzy">

### Modificarea obiectelor 

Modificarea unui obiect este făcută în același mod:


</div>

Modifying an object is done in the same way:


```python
import Part
cube = Part.makeBox(2, 2, 2)
myPart.Shape = cube
```

Acum, să schimbăm forma printr-o formă mai mare:


```python
biggercube = Part.makeBox(5, 5, 5)
myPart.Shape = biggercube
```

[top](#top.md)


<div class="mw-translate-fuzzy">

### Interogarea obiectelor 

Puteți să vă uitați mereu la tipul de obiect ca acesta:


</div>

You can always look at the type of an object like this:


```python
myObj = FreeCAD.ActiveDocument.getObject("myObjectName")
print(myObj.TypeId)
```


<div class="mw-translate-fuzzy">

sau să știm dacă un obiect este derivat dintr-unul dintre cele de bază (Part Feature, Mesh Feature, etc):


</div>


```python
print(myObj.isDerivedFrom("Part::Feature"))
```


<div class="mw-translate-fuzzy">

Acum puteți începe să jucați cu FreeCAD! Pentru a vedea ce puteți face cu [Part Workbench](Part_Workbench.md), citiți pagina [ Pare scripting](Topological_data_scripting.md), sau pagina [Mesh Scriptingpentru](Mesh_Scripting.md) a lucra cu [Mesh Workbench](Mesh_Workbench.md).Rețineți că, deși modulele Parte și Mesh sunt cele mai complete și utilizate pe scară largă, alte module cum ar fi [Draft Workbench](Draft_Workbench.md) au, de asemenea, [scripting](Draft_API.md) APIs care vă pate fi utili.Pentru o listă completă a fiecărui modul și a instrumentelor disponibile, vizitați secțiunea [:Category:API](:Category:API.md).


</div>

[top](#top.md)


{{Powerdocnavi

}} 

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Python Code{{\#translation:}}](Category:Python_Code.md)
