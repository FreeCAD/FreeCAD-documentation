# Manual:A gentle introduction/ro
{{Manual:TOC}}


<div class="mw-translate-fuzzy">

[Python](https://en.wikipedia.org/wiki/Python_%28programming_language%29) este un limbaj de programare popular, open source, foarte adesea încorporat în aplicații ca limbaj de scripting, ca în cazul FreeCAD. Are o serie de caracteristici care îl fac potrivite pentru utilizatorii noștri de pe FreeCAD: este foarte ușor de învățat, mai ales pentru cei care nu au programat niciodată înainte și este încorporat în multe alte aplicații. Acest lucru face ca acesta să fie un instrument valoros pentru a învăța, așa cum îl veți putea folosi în alte programe, cum ar fi [Blender](http://www.blender.org), [Inkscape](http://www.inkscape.org) ori [GRASS](http://grass.osgeo.org/).


</div>


<div class="mw-translate-fuzzy">

FreeCAD folosește extensiv Python. Cu aceasta, puteți accesa și controla aproape orice caracteristică a FreeCAD. De exemplu, puteți să creați obiecte noi, să modificați geometria, să analizați conținutul acestora sau chiar să creați noi controale de interfață, instrumente și panouri. Unele ateliere de lucru FreeCAD și majoritatea atelierelor addon sunt programate total în Python. FreeCAD are o consolă avansată Python, disponibilă din meniu**View-\>Panels-\>Python console**. Este adesea util să efectuați operații pentru care nu există încă buton pentru bara de unelte sau să verificați formele pentru probleme sau să efectuați sarcini repetitive:


</div>


<div class="mw-translate-fuzzy">

![](images/Exercise_python_01.jpg )


</div>

In FreeCAD, Python scripting enables you to:

-   Automate repetitive tasks to save time and reduce errors.
-   Create custom parametric objects that dynamically adapt to changes.
-   Develop personalized macros and tools tailored to specific workflows.
-   Interact with FreeCAD's Application Programming Interface (API) to access and manipulate geometry, scenes, and user interface elements programmatically.

By leveraging Python, FreeCAD users can unlock the full potential of the software, transforming it into a powerful and flexible tool tailored to their unique needs.


<div class="mw-translate-fuzzy">

Dar consola Python are și o altă utilizare foarte importantă: de fiecare dată când apăsați un buton al barei de instrumente sau efectuați alte operații în FreeCAD, fragmente de cod Python sunt tipărite în consola și executate. Lăsând deschisă consola Python, puteți vedea în mod literal codul Python care se desfășoară în timp ce lucrați și, în cel mai scurt timp, aproape fără a ști asta, veți învăța limbajul Python.


</div>


<div class="mw-translate-fuzzy">

FreeCAD are de asememene un [macros system](Macros.md), care vă permite să vă înregistrați acțiunile pentru a fi reluate mai târziu. Acest sistem utilizează, de asemenea, consola Python, care înregistrează pur și simplu tot ceea ce se face în interior.


</div>

În acest capitol, vom descoperi într-un mod foarte general limbajul Python. Dacă doriți să aflați mai multe, documentația wiki din FreeCAD are o secțiune extensivă despre programarea Python.[Python programming](Power_users_hub.md).



### Scrierea de cod Python 


<div class="mw-translate-fuzzy">

Sunt două maniere facile de a scrie cod Python în FreeCAD: de la consola Python (menu **View -\> Panels -\> Python Console**), sau de la editorul Macro (menu **Tools -\> Macros -\> New**). În consolă, scrieți comenzi Python una câte una, ele sunt executate atunci când apăsați retur de car (Enter), în timp ce macrocomenzile pot conține un script mai complex compus din mai multe linii care se execută numai când macroul este lansat din aceeași fereastră Macros (faceți click pe triunghiul verde).


</div>

Dacă este prima dată când utilizați Python, luați în considerare citirea acestei scurte introduceri în programarea Python înainte de a merge mai departe [introduction to Python programming](Introduction_to_Python.md). Acest lucru va face conceptele de baza ale Python sa vă fie mai clare.



### Manipularea obiectelor FreeCAD 

Începem prin a crea un document vid:


```python
doc = FreeCAD.newDocument()
```


<div class="mw-translate-fuzzy">

Dacă introduceți acest lucru în consola FreeCAD Python, veți observa că de îndată ce tastați \"FreeCAD.\" (cuvântul FreeCAD urmat de un punct), se deschide un fereastră, permițând să finalizați rapid restul liniei. Chiar mai bine, fiecare intrare din lista de autocompletare are o sugestie care explică ce face. Acest lucru face foarte ușor pentru a explora funcționalitatea disponibilă. Înainte de a alege \"newDocument\", aruncați o privire asupra celorlalte opțiuni disponibile.


</div>


<div class="mw-translate-fuzzy">

![](images/Exercise_python_02.jpg )


</div>


<div class="mw-translate-fuzzy">

De îndată ce apăsați **Enter**, noul nostru document va fi creat. Acest lucru este similar cu apăsarea butonului \"document nou\" de pe bara de instrumente. În Python, punctul este folosit pentru a indica ceva care este conținut în altceva (newDocument este o funcție care este în interiorul modulului FreeCAD). Fereastra care apare, prin urmare, vă arată tot ce este conținut în interiorul \"FreeCAD\". Dacă ați adăuga un punct după newDocument, în loc de paranteze, vă va arăta tot ce este conținut în interiorul funcției newDocument. Parantezele sunt obligatorii atunci când apelați o funcție Python, cum ar fi aceasta. Vom exemplifica mai bine mai jos.


</div>


<div class="mw-translate-fuzzy">

Acum întoarceți-vă la documentul nostru. Să vedem ce putem face cu acest lucru:


</div>

Now let\'s get back to our document. Let\'s see what we can do with it. Type the following and explore the available options:


```python
doc.
```


<div class="mw-translate-fuzzy">

Explorați opțiunile disponibile. De obicei, numele care încep cu o literă majusculă sunt atribute, ele conțin o valoare, în timp ce numele care încep cu o literă mică sunt funcții (numite și metode), fac \"ceva\". Numele care încep cu o subliniere sunt de obicei acolo pentru funcționarea interioară a modulului și nu trebuie să vă faceți griji despre asta. Să folosim una dintre metodele de adăugare a unui obiect nou în documentul nostru:


</div>

-   Names that begin with an upper-case letter are typically attributes, which store values or data, such as properties of an object.
-   Names that begin with a lower-case letter are usually functions (also called methods), which perform actions or operations, such as creating or modifying objects.
-   Names that begin with an underscore (\_) are generally intended for internal use within the module and can usually be ignored.

This distinction helps you navigate FreeCAD's API and select the appropriate command for your needs. For example, you might use a method to add a new object to a document. The method performs the action of creating and adding the object, while attributes store the object\'s properties. Understanding this structure makes it easier to explore the functionality available, especially when using the autocomplete feature or reading tooltips. Let\'s add a box.


```python
box = doc.addObject("Part::Box", "myBox")
```


<div class="mw-translate-fuzzy">

Caseta noastră este adăugată în vederea arborescentă, dar nu se întâmplă nimic în vizualizarea 3D, deoarece atunci când lucrați cu Python, documentul nu este niciodată recalculat automat. Trebuie să o facem manual, ori de câte ori avem nevoie:


</div>

-   **doc.addObject**: This tells FreeCAD to add a new object to the document.
-   **Part::Box**: This specifies the type of object to create, in this case, a 3D box.
-   **myBox**: This assigns a name to the new object, making it easier to identify and reference later.

The result of this command is that a box appears in the active document, and the variable box stores a reference to it so you can modify or interact with it later. Our box is added in the tree view, but nothing happens in the 3D view yet, because when working from Python, the document is never recomputed automatically. We must do that manually, whenever required:


```python
doc.recompute()
```


<div class="mw-translate-fuzzy">

Acum, caseta noastră a apărut în vizualizarea 3D. Multe dintre butoanele din bara de instrumente care adaugă obiecte în FreeCAD fac de fapt două lucruri: adăugați obiectul și recalculează. Dacă ați activat opțiunea \"show script commands in Python console\" de mai sus, încercați acum să adăugați o sferă cu butonul corespunzător din Atetlierul Part și veți vedea că cele două linii de cod Python sunt executate unul după altul.


</div>


<div class="mw-translate-fuzzy">

Puteți obține o listă cu toate tipurile de obiecte posibile cum ar fi Part::Box:


</div>


<div class="mw-translate-fuzzy">

doc.supportedTypes()


</div>


```python
doc.supportedTypes()
```


<div class="mw-translate-fuzzy">

box.


</div>


```python
box.
```


<div class="mw-translate-fuzzy">

box.Height


</div>


```python
box.Height
```


<div class="mw-translate-fuzzy">

box.Height = 5


</div>


```python
box.Height = 5
```


<div class="mw-translate-fuzzy">

box.Length


</div>


```python
box.Length
```


<div class="mw-translate-fuzzy">

De exemplu, pentru a accesa culoarea liniei casetei noastre:


</div>


<div class="mw-translate-fuzzy">

box.ViewObject.LineColor


</div>


```python
box.ViewObject.LineColor
```




<div class="mw-translate-fuzzy">

Vectorii reprezintă un concept fundamental în orice aplicație 3D. Este o listă cu 3 numere (x, y și z), care descriu un punct sau o poziție în spațiul 3D. O mulțime de lucruri se pot face cu vectori, cum ar fi adăugiri, scăderi, proiecții și multe altele. În FreeCAD vectorii funcționează astfel:


</div>


<div class="mw-translate-fuzzy">

myvec = FreeCAD.Vector(2,0,0)

print(myvec)
print(myvec.x)
print(myvec.y)
othervec = FreeCAD.Vector(0,3,0)
sumvec = myvec.add(othervec)


</div>


<div class="mw-translate-fuzzy">

O altă caracteristică comună a FreeCAD este plasarea **Placement**. Proprietate de plasare, care conține poziția (Base) și orientarea (Rotation) obiectului. Aceste proprietăți sunt ușor de manipulat de la Python, de exemplu pentru a muta obiectul nostru:


</div>


<div class="mw-translate-fuzzy">

print(box.Placement)

print(box.Placement.Base)
box.Placement.Base = sumvec
otherpla = FreeCAD.Placement()
otherpla.Base = FreeCAD.Vector(5,5,0)
box.Placement = otherpla


</div>


<div class="mw-translate-fuzzy">

**De citit în plus**


</div>


```python
myvec = FreeCAD.Vector(2, 0, 0)
print(myvec)
print(myvec.x)
print(myvec.y)
othervec = FreeCAD.Vector(0, 3, 0)
sumvec = myvec.add(othervec)
```

Here is a short breakdown of the above commands:

-   **myvec = FreeCAD.Vector(2,0,0)**: Creates a vector myvec with X = 2, Y = 0, Z = 0.
-   **print(myvec)**: Prints the vector myvec with its components (X, Y, Z).
-   **print(myvec.x)**: Prints the X-component of myvec.
-   **print(myvec.y)**: Prints the Y-component of myvec.
-   **othervec = FreeCAD.Vector(0,3,0)**: Creates a second vector othervec with X = 0, Y = 3, Z = 0.
-   **sumvec = myvec.add(othervec)**: Adds myvec and othervec to create a new vector sumvec containing the sum of their components.

Another common feature of FreeCAD objects is their **Placement**. As we saw in earlier chapters, each object has a Placement property, which contains the position (Base) and orientation (Rotation) of the object. These properties are easy to manipulate from Python, for example, to move our object:


```python
print(box.Placement)
print(box.Placement.Base)
box.Placement.Base = sumvec
otherpla = FreeCAD.Placement()
otherpla.Base = FreeCAD.Vector(5, 5, 0)
box.Placement = otherpla
```

Here is a short breakdown of the above commands:

-   **print(box.Placement)**: Prints the placement of the box, which includes its position, rotation, and orientation in 3D space.
-   **print(box.Placement.Base)**: Prints the position (Base) of the box, which is a vector representing its location in 3D space.
-   **box.Placement.Base = sumvec**: Sets the base position (location) of the box to the vector sumvec, effectively moving the box to this new position.
-   **otherpla = FreeCAD.Placement()**: Creates a new placement object named otherpla.
-   **otherpla.Base = FreeCAD.Vector(5,5,0)**: Sets the base position of otherpla to a vector at coordinates (5, 5, 0).
-   **box.Placement = otherpla**: Applies otherpla to the box, updating its placement to the new position and orientation defined by otherpla.

**Read more**

-   [Python](https://www.python.org)
-   [Macros](Macros.md)
-   [Introduction to Python](Introduction_to_Python.md)
-   [Python scripting tutorial](Python_scripting_tutorial.md)
-   [Power users hub](Power_users_hub.md)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Manual:A gentle introduction/ro
