# Python scripting tutorial/ro



{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

[Python](http://en.wikipedia.org/wiki/Python_%28programming_language%29) este un limbaj de programare, foarte simplu de utilizat și foarte rapid de învățat. Este open-source, multi-platformă și poate fi folosit singur pentru o gamă largă de lucruri, de la programarea scripturilor simple shell la programele foarte complexe. Dar una dintre cele mai răspândite utilizări este ca un limbaj de scripting, deoarece este ușor de încorporat în alte aplicații. Exact așa este folosit în interiorul FreeCAD. Din consola Python sau din scripturile personalizate, puteți încerca FreeCAD și o puteți face să efectueze acțiuni foarte complexe pentru care nu există încă un instrument grafic de interfață cu utilizatorul.


</div>


<div class="mw-translate-fuzzy">

Dintr-un script Python, de exemplu, puteți:

-   crea obiecte noi
-   modifica obiectele existente
-   modifica reprezentarea 3D a acestor obiecte
-   modifica interfața FreeCAD


</div>


<div class="mw-translate-fuzzy">

Există, de asemenea, mai multe moduri diferite de a folosi Python în FreeCAD:

-   Din [FreeCAD python interpreter](FreeCAD_Scripting_Basics.md), unde puteți emite comenzi simple ca într-o interfață \"command line\"-style interface
-   Din [macros](macros.md), care sunt o modalitate convenabilă de a adăuga rapid o unealtă lipsă la interfața FreeCAD
-   De la scripturi externe, care pot fi folosite pentru a programa lucruri mult mai complexe. ca întreg sistemul de ateliere [Workbenches](Workbenches.md).


</div>


<div class="mw-translate-fuzzy">

În acest tutorial, vom lucra pentru început pe câteva exemple simple, dar există, de asemenea, mult mai multă [documentation about python scripting](Power_users_hub.md) disponibilă pe acest wiki. Dacă sunteți total novice în limbajul Python și doriți să înțelegeți cum funcționează, avem de asemenea o bază [introduction to Python](introduction_to_Python.md).


</div>


<div class="mw-translate-fuzzy">

**Important!** Înainte de a continua scriptul Python, mergeți la fereastra **Edit->Prefences->General->Output** și bifați 2 căsuțe:

-   Redirecționați ieșirea internă Python către vizualizarea raportului
-   Redirecționați erorile interne Python către vizualizarea raportului

Then go to **View->Panels** and check:

-   Report view

Acest lucru vă va feri de o mulțime de probleme grave!


</div>


<div class="mw-translate-fuzzy">

## Scrierea codului python 

Există două modalități ușoare de a scrie codul python în FreeCAD: Din consola python (disponibilă din View -\> Panels -\> Python console menu) ori din Macro editor (Tools -\> Macros). In consolă, scrieți comenzi python una câte una, care sunt executate atunci când apăsați retur de car (Enter), în timp ce macrocomenzile pot conține un script mai complex compus din mai multe linii care se execută numai când macro-ul este executat.


</div>

There are two ways to write Python code in FreeCAD. In the [Python console](Python_console.md) (select **View → Panels → Python console** from the menu) or in the [Macro editor](Std_DlgMacroExecute.md) (select **Macro → Macros...** from the menu). In the console you write Python commands one by one, executing them by pressing **Enter**, while macros can contain more complex code made up of several lines, executed only when the macro is executed.

![](images/Screenshot_pythoninterpreter.jpg )


<div class="mw-translate-fuzzy">

![The FreeCAD python console](images/Screenshot_pythoninterpreter.jpg )


</div>


<div class="mw-translate-fuzzy">

În acest tutorial, veți putea utiliza ambele metode fie prin copierea / lipirea fiecărei linii una câte una în consola python și apăsând **Return** după fiecare linie, ori prin copy/paste întregul cod într-o nouă fereastră Macro.


</div>

[top](#top.md)


<div class="mw-translate-fuzzy">

## Explorând FreeCAD 

Hai să începem prin crearea unui nou document vid:


</div>

Let\'s start by creating a new empty document:


```python
doc = FreeCAD.newDocument()
```


<div class="mw-translate-fuzzy">

Dacă introduceți acest lucru în consola Python FreeCAD, veți observa că, de îndată ce tastați \"FreeCAD.\", Se va afișa un fereastră, permițând rapid completarea automată a restului liniei. Chiar mai bine, fiecare intrare din lista de auto-complete are o sugestie care explică ce face. Acest lucru face foarte ușoară explorarea funcționalității disponibile. Înainte de a alege \"newDocument\", aruncați o privire asupra celorlalte opțiuni disponibile.


</div>

![](images/Screenshot_classbrowser.jpg )


<div class="mw-translate-fuzzy">

![The autocomplete mechanism of the FreeCAD python console](images/Screenshot_classbrowser.jpg )


</div>


<div class="mw-translate-fuzzy">

Acum, noul nostru document va fi creat. Acest lucru este similar cu apăsarea butonului \"document nou\" de pe bara de instrumente. De fapt, majoritatea butoanelor din FreeCAD nu fac decât să execute o linie sau două coduri Python. Chiar mai bine, puteți seta o opțiune în **Edit->Preferences->General->Macro** pentru a \"show script commands in python console\". Aceasta va afișa în consolă tot codul python executat când apăsați butoanele. Foarte util pentru a afla cum să reproduceți acțiunile în Python.


</div>


<div class="mw-translate-fuzzy">

Acum să ne întoarcem la documentul nostru. Să vedem ce putem face cu el:


</div>


```python
doc.
```


<div class="mw-translate-fuzzy">

Explorați opțiunile disponibile. De obicei, numele care încep cu o literă de capital sunt atribute, ele conțin o valoare, în timp ce numele care încep cu litera subliniată arată că sunt funcții (numite și metode), fac \"ceva\". Numele care încep cu un subliniere sunt de obicei acolo pentru funcționarea internă a modulului și nu ar trebui să le pese de ele. Să folosim una dintre metodele de adăugare a unui obiect nou în documentul nostru:


</div>


```python
box = doc.addObject("Part::Box", "myBox")
```


<div class="mw-translate-fuzzy">

Nu se întâmplă nimic. De ce? Deoarece FreeCAD este creat pentru imaginea de ansamblu. Într-o zi, va funcționa cu sute de obiecte complexe, toate depinzând unul de altul. Efectuarea unei mici schimbări ar putea avea un impact mare, ar putea să trebuiască să recalculați tot documentul, ceea ce ar putea dura mult timp/ Trebuie să o faceți manual:


</div>


```python
doc.recompute()
```


<div class="mw-translate-fuzzy">

Vedeți? Acum, caseta noastră a apărut! Multe dintre butoanele care adaugă obiecte în FreeCAD fac de fapt 2 lucruri: adăugă obiectul și recalculaează. Dacă ați activat opțiunea \"show script commands in python console\" \"comenzile scriptului de prezentare din consola python\" de mai sus, încercați acum să adăugați o sferă cu butonul GUI, veți vedea că cele două linii de cod python sunt executate una după alta.


</div>

Acum, să explorăm conținutul casetei noastre:


```python
box.
```

Veți vedea imediat câteva lucruri foarte interesante, cum ar fi:


```python
box.Height
```

Aceasta va tipări înălțimea curentă a casetei noastre. Acum, să încercăm să schimbăm acest lucru:


```python
box.Height = 5
```


<div class="mw-translate-fuzzy">

Dacă selectați o casetă cu mouse-ul, veți vedea că în panoul proprietăților, în fila \"Data\", apare proprietatea noastră \"Height\". Toate proprietățile unui obiect FreeCAD care apar acolo (și, de asemenea, în fila \"Vizualizare\", mai multe despre asta mai târziu), sunt direct accesibile și prin Python, prin numele lor, așa cum am făcut-o cu proprietatea \"Height\". Încercați să modificați celelalte dimensiuni ale căsuței.


</div>

[top](#top.md)


<div class="mw-translate-fuzzy">

## Vectori și Plasamente 

[Vectors](http://en.wikipedia.org/wiki/Euclidean_vector) sunt un concept foarte fundamental în orice aplicație 3D. Este o listă cu 3 numere (x, y și z), care descriu un punct sau o poziție în spațiul 3D. O mulțime de lucruri se pot face cu vectori, cum ar fi adăugiri, scăderi, proiecții și [much more](http://en.wikipedia.org/wiki/Vector_space). In FreeCAD vectorii lucrează cam așa:


</div>

[Vectors](https://en.wikipedia.org/wiki/Euclidean_vector) are a very fundamental concept in any 3D application. A vector is a list of 3 numbers (x, y and z), describing a point or position in 3D space. Many things can be done with vectors, such as additions, subtractions, projections and [much more](https://en.wikipedia.org/wiki/Vector_space). In FreeCAD vectors work like this:


```python
myvec = FreeCAD.Vector(2, 0, 0)
myvec.x
myvec.y
othervec = FreeCAD.Vector(0, 3, 0)
sumvec = myvec.add(othervec)
```


<div class="mw-translate-fuzzy">

O altă caracteristică comună a obiectelor FreeCAD este [placement](Placement.md). Fiecare obiect are atribute de plasare, care conține poziția (baza) și orientarea (rotirea) obiectului. Este ușor de manipulat, de exemplu pentru a ne mișca obiectul:


</div>


```python
box.Placement
box.Placement.Base
box.Placement.Base = sumvec
 
otherpla = FreeCAD.Placement()
box.Placement = otherpla
```

Acum trebuie să înțelegeți câteva concepte importante înainte de a ajunge mai departe.

[top](#top.md)


<div class="mw-translate-fuzzy">

## Apicații și Interfață grafică 

FreeCAD de la început a fost conceput pentru a funcționa ca o aplicație pe linie de comandă, fără interfața sa de utilizator. Ca rezultat, aproape totul este separat între o componentă \"geometrie\" și o componentă \"vizuală\". Când lucrați în modul de comandă, partea de geometrie este prezentă, dar toată partea vizuală este pur și simplu dezactivată. Aproape orice obiect din FreeCAD este compus din două părți, an Object and a ViewObject.


</div>

FreeCAD has been designed so that it can also be used without its user interface, as a command-line application. Almost every object in FreeCAD therefore consists of two parts: an `Object`, its \"geometry\" component, and a `ViewObject`, its \"visual\" component. When you work in command-line mode, the geometry part is present, but the visual part is disabled.


<div class="mw-translate-fuzzy">

Pentru a ilustra conceptul, a se vedea obiectul nostru cub, proprietățile geometrice ale cubului, cum ar fi dimensiunile, poziția etc., sunt stocate în obiect, în timp ce proprietățile sale vizuale, cum ar fi culoarea, grosimea liniei etc. sunt stocate în obiectul de vizualizare. Aceasta corespunde fișierelor \"Data\" și \"Vew\" din fereastra de proprietăți. Obiectul de vizualizare al unui obiect este accesat astfel:


</div>


```python
vo = box.ViewObject
```


<div class="mw-translate-fuzzy">

Acum, puteți schimba și proprietățile filei \"View\":


</div>


```python
vo.Transparency = 80
vo.hide()
vo.show()
```


<div class="mw-translate-fuzzy">

Când porniți FreeCAD, consola python are încarcate deja 2 module de bază: FreeCAD și FreeCADGui (care pot fi accesate și prin comenzile rapide App și Gui). Acestea conțin toate tipurile de funcții generice pentru a lucra cu documentele și obiectele acestora. Pentru a ilustra conceptul nostru, a se vedea că atât FreeCAD cât și FreeCADGui conțin un atribut ActiveDocument, care este documentul deschis în prezent. FreeCAD.ActiveDocument și FreeCADGui.ActiveDocument nu sunt același obiect. Acestea sunt cele două componente ale unui document FreeCAD și conțin atribute și metode diferite. De exemplu, FreeCADGui.ActiveDocument conține ActiveView, care este vizualizarea 3D curentă/actuală


</div>

[top](#top.md)


<div class="mw-translate-fuzzy">

## Module

Acum, ar trebui să te întrebi ce, se poate face cu \"Part::Box\"? Aplicația de bază FreeCAD este mai mult sau mai puțin un container gol. Fără modulele sale, acesta nu poate face decât să creeze noi documente goale. Adevărata putere a FreeCAD este în modulele sale credincioase. Fiecare dintre ele adaugă la interfață nu numai noi ateliere de lucru, ci și noi comenzi python și tipuri noi de obiecte. Ca rezultat, mai multe tipuri de obiecte diferite sau chiar total incompatibile pot coexista în același document. Cele mai importante module din FreeCAD, pe care le vom analiza în acest tutorial, sunt [Part](Part_Workbench.md), [Mesh](Mesh_Workbench.md), [Sketcher](Sketcher_Workbench.md) ori [Draft](Draft_Workbench.md).


</div>

The true power of FreeCAD lies in its faithful modules, with their respective workbenches. The FreeCAD base application is more or less an empty container. Without its modules it can do little more than create new, empty documents. Each module not only adds new workbenches to the interface, but also new Python commands and new object types. As a result several different, and even totally incompatible, object types can coexist in the same document. The most important modules in FreeCAD that we\'ll look at in this tutorial are: [Part](Part_Workbench.md), [Mesh](Mesh_Workbench.md), [Sketcher](Sketcher_Workbench.md) and [Draft](Draft_Workbench.md).


<div class="mw-translate-fuzzy">

[Sketcher](Sketcher_Workbench.md) și [Draft](Draft_Workbench.md) amândouă utilizează modulul [Part](Part_Workbench.md) pentru a crea și manipula geometria lor, care este Boundary Representation - BRep [Mesh](Mesh_Workbench.md) este total independentă și își ocupă propriile obiecte. Mai multe despre acestea sunt în cele de mai jos.


</div>

Puteți verifica toate tipurile de obiecte de bază disponibile pentru documentul curent, după cum urmează:


```python
doc.supportedTypes()
```


<div class="mw-translate-fuzzy">

Diferitele module FreeCAD, deși și-au adăugat tipurile de obiecte în FreeCAD, nu sunt încărcate automat în consola python. Aceasta este pentru a evita o pornire foarte lentă. Modulele sunt încărcate numai atunci când aveți nevoie de ele. De exemplu, pentru a explora ce se află în interiorul modulului Piese:


</div>


```python
import Part
Part.
```

Dar vom vorbi mai multe despre modulul Piese mai jos.

[top](#top.md)


<div class="mw-translate-fuzzy">

## Plase


</div>


<div class="mw-translate-fuzzy">

[Meshes](http://en.wikipedia.org/wiki/Polygon_mesh) sunt un tip foarte simplu de obiecte 3D, folosite de exemplu de [Sketchup](http://en.wikipedia.org/wiki/SketchUp), [Blender](http://en.wikipedia.org/wiki/Blender_%28software%29) or [3D studio Max](http://en.wikipedia.org/wiki/Autodesk_3ds_Max). Ele sunt compuse din 3 elemente: puncte (numite și vârfuri), linii (numite și margini) și fațete. În multe aplicații, inclusiv în FreeCAD, fațetele pot avea doar 3 noduri. Dar, desigur, nimic nu vă împiedică să aveți o față mai mare plană făcută din mai multe triunghiuri coplanare.


</div>


<div class="mw-translate-fuzzy">

Mesh-urile sunt simple, acest lucru poate fi un lucru rău, însă pentru multe aplicații, cum ar fi cele menționate mai sus, se dovedește a fi un avantaj, deoarece acestea sunt atât de simple încât puteți avea cu ușurință milioane dintr-un singur document. În FreeCAD, totuși, acestea au mai puțină utilizare și sunt mai mult acolo, astfel încât să puteți importa obiecte în formate de plasă (.stl, .obj) din alte aplicații. De asemenea, a fost utilizat extensiv ca modul principal de testare în prima lună a vieții FreeCAD.


</div>


<div class="mw-translate-fuzzy">

Obiectele tip Plasă/rețea de discretizare/meshes și obiectele FreeCAD sunt lucruri diferite. Puteți vedea obiectul FreeCAD ca un container pentru un obiect Mesh (cum ar fi, vom vedea mai jos, și pentru obiectele Piese de asemenea). Deci, pentru a adăuga un obiect tip plasă la FreeCAD, trebuie mai întâi să creăm un obiect FreeCAD și un obiect Mesh, apoi să adăugăm obiectul Mesh la obiectul FreeCAD:


</div>


```python
import Mesh
mymesh = Mesh.createSphere()
mymesh.Facets
mymesh.Points
 
meshobj = doc.addObject("Mesh::Feature", "MyMesh")
meshobj.Mesh = mymesh
doc.recompute()
```


<div class="mw-translate-fuzzy">

Acesta este un exemplu standard, care folosește metoda createSphere() pentru a crea automat o sferă, dar puteți crea foarte bine plase/mesh-uri personalizate de la zero, definindu-le vârfurile și fețele.


</div>

[Read more about mesh scripting\...](Mesh_Scripting.md)

[top](#top.md)


<div class="mw-translate-fuzzy">

## Piese

[Part Workbench](Part_Workbench.md) este modulul cel mai puternic din întregul FreeCAD. Permite crearea și manipularea obeictelor [BRep](http://en.wikipedia.org/wiki/Boundary_representation). Acest tip de obiect, spre deosebire de Plase cu ochiuri, poate avea o mare varietate de componente. Pentru a rezuma, Brep înseamnă Boundary Representation-Reprezentarea limitelor, ceea ce înseamnă că ele sunt definite de către suprafețele lor, care cuprind și definesc un volum interior. Aceste suprafețe pot fi o varietate de lucruri, cum ar fi fațetele plane sau suprafețele NURBS foarte complexe. Ele poartă, de asemenea, conceptul de volum.


</div>

The [Part](Part_Workbench.md) module is the most powerful module in the whole of FreeCAD. It allows you to create and manipulate [BRep](https://en.wikipedia.org/wiki/Boundary_representation) objects. BREP stands for \"Boundary Representation\". A BREP object is defined by surfaces that enclose and define an inner volume. Unlike meshes, BREP objects can have a wide variety of components from planar faces to very complex NURBS surfaces.


<div class="mw-translate-fuzzy">

Modulul /Atelierul Piese se bazeză pe putrnica bilbiotecă [OpenCasCade](http://en.wikipedia.org/wiki/Open_CASCADE_Technology) bibliotecă, care permite o gamă largă de operații complexe să fie ușor de realizat pe acele obiecte, cum ar fi operațiile booleene, filetarea, lofts etc.


</div>

Modulul Part/Piese funcționează la fel ca modulul Mesh/Plase: Creați un obiect FreeCAD, un obiect Part, apoi adăugați obiectul Part la obiectul FreeCAD:


```python
import Part
myshape = Part.makeSphere(10)
myshape.Volume
myshape.Area

shapeobj = doc.addObject("Part::Feature", "MyShape")
shapeobj.Shape = myshape
doc.recompute()
```


<div class="mw-translate-fuzzy">

Modulul Part (cum ar fi modulul Mesh) are, de asemenea, o comandă rapidă care creează automat un obiect FreeCAD și adaugă o formă pentru acesta, astfel încât să puteți sări peste cele trei linii de mai sus:


</div>


```python
Part.show(myshape)
```


<div class="mw-translate-fuzzy">

Prin explorarea conținutului myshape, veți observa multe subcomponente interesante cum ar fi Faces/Fațete, margini/muchii, vârfuri, solide sau forme coji și o gamă largă de operații de geometrie, cum ar fi substractivitatea (scăderea), comunitatea (intersecția) sau fuziunea (uniunea). Pagina cu [Scriptarea datelor topologice](Topological_data_scripting/ro.md) explică toate detaliile.


</div>


<div class="mw-translate-fuzzy">

[Read more about part scripting\...](Topological_data_scripting.md)


</div>

[top](#top.md)


<div class="mw-translate-fuzzy">

## Desen 2 D 

Careacteristicile FreeCAD features sunt în multe module, ca de exemplu [Sketcher](Sketcher_Workbench.md) ori [Draft](Draft_Workbench.md), care creează, de asemenea, obiecte Piese, dar adaugă parametri sau chiar abordează o nouă modalitate de a gestiona geometria pieselor în ele. Exemplul casetei de mai sus este un exemplu perfect de obiect parametric. Tot ce aveți nevoie, pentru a defini caseta, este să specificați câțiva parametri, cum ar fi înălțimea, lățimea și lungimea. Pe baza acestora, obiectul va calcula automat forma piesei sale. FreeCAD vă permite să [create such objects in python](Scripted_objects.md).


</div>

FreeCAD features many more modules, such as [Sketcher](Sketcher_Workbench.md) and [Draft](Draft_Workbench.md), that also create Part objects. These modules add additional parameters to the objects created, or even implement a whole new way to handle the Part geometry in them. Our box example above is a perfect example of a parametric object. All you need to define the box is to specify the parameters height, width and length. Based on those, the object will automatically calculate its Part shape. FreeCAD allows you to [create such objects in Python](Scripted_objects.md).


<div class="mw-translate-fuzzy">

[Draft Workbench](Draft_Workbench.md) adaugă câteva tipuri de obiecte parametrice 2D parametric (care sunt toate obiecte Part) ca de exemplu linile și cercurile, și oferă, de asemenea, câteva funcții generice care funcționează nu numai pe obiectele create de Draft, ci și pe orice obiect Part. Pentru a explora ceea ce este disponibil, pur și simplu faceți:


</div>


```python
import Draft
rec = Draft.makeRectangle(5, 2)
mvec = FreeCAD.Vector(4, 4, 0)
Draft.move(rec, mvec)
Draft.move(box, mvec)
```

[top](#top.md)


<div class="mw-translate-fuzzy">

## Interfață

Interfața user a FreeCAD este realizată cu [Qt](http://en.wikipedia.org/wiki/Qt_%28framework%29), un sistem puternic de interfață grafică, responsabil pentru desenarea și manipularea tuturor comenzilor, meniurilor, barelor de instrumente, butoanelor în jurul vizualizării 3D. Qt oferă un modul, numit PySide, care permite Python-ului să acceseze și să modifice interfețele Qt, cum ar fi FreeCAD. Să încercăm să modificăm interfața Qt și să producem un dialog simplu:


</div>

The FreeCAD user interface is made with [Qt](https://en.wikipedia.org/wiki/Qt_(software)), a powerful graphical interface system, responsible for drawing and handling all the controls, menus, toolbars and buttons around the [3D view](3D_view.md). Qt provides a module, [PySide](PySide.md), which allows Python to access and modify Qt interfaces such as FreeCAD\'s. Let\'s try to fiddle with the Qt interface and produce a simple dialog:


```python
from PySide import QtGui
QtGui.QMessageBox.information(None, "Apollo program", "Houston, we have a problem")
```


<div class="mw-translate-fuzzy">

Vedeți că dialogul care apare are pictograma FreeCAD din bara de instrumente, ceea ce înseamnă că Qt știe că ordinul a fost emis din interiorul aplicației FreeCAD. Prin urmare, putem manipula direct orice parte a interfeței FreeCAD.


</div>


<div class="mw-translate-fuzzy">

Qt este un sistem de interfață foarte puternic, care vă permite să faceți lucruri foarte complexe, dar are și câteva instrumente foarte ușor de folosit, cum ar fi designerul Qt, cu care puteți crea dialoguri grafic și apoi le puteți adăuga la interfața FreeCAD cu câteva linii de python.


</div>

[Read more about PySide here\...](PySide.md)

[top](#top.md)


<div class="mw-translate-fuzzy">

## Macro-uri 

Acum, că aveți o bună înțelegere a principiilor de bază, unde vom păstra scripturile noastre Python și cum le vom lansa cu ușurință de pe FreeCAD? Există un mecanism ușor pentru acesta, numit [Macros](Macros.md). O macrocomandă este pur și simplu un script python, care poate fi apoi adăugat la o bară de instrumente și poate fi lansat printr-un simplu click de mouse. FreeCAD vă oferă un editor simplu de text (Macro -\> Macros -\> Creare) unde puteți scrie sau lipi scripturi. După ce s-a terminat, Instrumentele -\> Customize -\> Macro-urile vă permit să definiți un buton pentru acesta, care poate fi adăugat la barele de instrumente.


</div>

Now that you have a good understanding of the basics, where are we going to keep our Python scripts, and how are we going to launch them inside FreeCAD? There is an easy mechanism for that, called [Macros](Macros.md). A macro is a Python script that can be added to a toolbar and launched via a mouse click. FreeCAD provides you with a simple text editor (**Macro → Macros... → Create**) where you can write or paste scripts. Once the script is done, use **Tools → Customize... → Macros** to define a button for it that can be added to toolbars.


<div class="mw-translate-fuzzy">

Acum sunteți gata pentru mai multă programare/script FreeCAD în profunzime. Deplasați-vă la [Power users hub](Power_users_hub.md)!


</div>

[top](#top.md)


{{Powerdocnavi

}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)
