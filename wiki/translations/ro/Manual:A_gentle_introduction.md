 


{{Manual:TOC/ro}}

[Python](https://en.wikipedia.org/wiki/Python_%28programming_language%29) este un limbaj de programare popular, open source, foarte adesea încorporat în aplicații ca limbaj de scripting, ca în cazul FreeCAD. Are o serie de caracteristici care îl fac potrivite pentru utilizatorii noștri de pe FreeCAD: este foarte ușor de învățat, mai ales pentru cei care nu au programat niciodată înainte și este încorporat în multe alte aplicații. Acest lucru face ca acesta să fie un instrument valoros pentru a învăța, așa cum îl veți putea folosi în alte programe, cum ar fi [Blender](http://www.blender.org), [Inkscape](http://www.inkscape.org) ori [GRASS](http://grass.osgeo.org/).

FreeCAD folosește extensiv Python. Cu aceasta, puteți accesa și controla aproape orice caracteristică a FreeCAD. De exemplu, puteți să creați obiecte noi, să modificați geometria, să analizați conținutul acestora sau chiar să creați noi controale de interfață, instrumente și panouri. Unele ateliere de lucru FreeCAD și majoritatea atelierelor addon sunt programate total în Python. FreeCAD are o consolă avansată Python, disponibilă din meniu**View-\>Panels-\>Python console**. Este adesea util să efectuați operații pentru care nu există încă buton pentru bara de unelte sau să verificați formele pentru probleme sau să efectuați sarcini repetitive:

![](images/Exercise_python_01.jpg )

Dar consola Python are și o altă utilizare foarte importantă: de fiecare dată când apăsați un buton al barei de instrumente sau efectuați alte operații în FreeCAD, fragmente de cod Python sunt tipărite în consola și executate. Lăsând deschisă consola Python, puteți vedea în mod literal codul Python care se desfășoară în timp ce lucrați și, în cel mai scurt timp, aproape fără a ști asta, veți învăța limbajul Python.

FreeCAD are de asememene un [macros system](Macros.md), care vă permite să vă înregistrați acțiunile pentru a fi reluate mai târziu. Acest sistem utilizează, de asemenea, consola Python, care înregistrează pur și simplu tot ceea ce se face în interior.

În acest capitol, vom descoperi într-un mod foarte general limbajul Python. Dacă doriți să aflați mai multe, documentația wiki din FreeCAD are o secțiune extensivă despre programarea Python.[Python programming](Power_users_hub.md).

### Scrierea de cod Python 

Sunt două maniere facile de a scrie cod Python în FreeCAD: de la consola Python (menu **View -\> Panels -\> Python Console**), sau de la editorul Macro (menu **Tools -\> Macros -\> New**). În consolă, scrieți comenzi Python una câte una, ele sunt executate atunci când apăsați retur de car (Enter), în timp ce macrocomenzile pot conține un script mai complex compus din mai multe linii care se execută numai când macroul este lansat din aceeași fereastră Macros (faceți click pe triunghiul verde).

În acest capitol, veți putea utiliza ambele metode, dar este foarte recomandat să utilizați Consola Python, deoarece vă va informa imediat despre eventualele erori pe care le faceți în timp ce tastați.

Dacă este prima dată când utilizați Python, luați în considerare citirea acestei scurte introduceri în programarea Python înainte de a merge mai departe [introduction to Python programming](Introduction_to_Python.md). Acest lucru va face conceptele de baza ale Python sa vă fie mai clare.

### Manipularea obiectelor FreeCAD 

Începem prin a crea un document vid:

doc = FreeCAD.newDocument()

Dacă introduceți acest lucru în consola FreeCAD Python, veți observa că de îndată ce tastați \"FreeCAD.\" (cuvântul FreeCAD urmat de un punct), se deschide un fereastră, permițând să finalizați rapid restul liniei. Chiar mai bine, fiecare intrare din lista de autocompletare are o sugestie care explică ce face. Acest lucru face foarte ușor pentru a explora funcționalitatea disponibilă. Înainte de a alege \"newDocument\", aruncați o privire asupra celorlalte opțiuni disponibile.

![](images/Exercise_python_02.jpg )

De îndată ce apăsați **Enter**, noul nostru document va fi creat. Acest lucru este similar cu apăsarea butonului \"document nou\" de pe bara de instrumente. În Python, punctul este folosit pentru a indica ceva care este conținut în altceva (newDocument este o funcție care este în interiorul modulului FreeCAD). Fereastra care apare, prin urmare, vă arată tot ce este conținut în interiorul \"FreeCAD\". Dacă ați adăuga un punct după newDocument, în loc de paranteze, vă va arăta tot ce este conținut în interiorul funcției newDocument. Parantezele sunt obligatorii atunci când apelați o funcție Python, cum ar fi aceasta. Vom exemplifica mai bine mai jos.

Acum întoarceți-vă la documentul nostru. Să vedem ce putem face cu acest lucru:

doc.

Explorați opțiunile disponibile. De obicei, numele care încep cu o literă majusculă sunt atribute, ele conțin o valoare, în timp ce numele care încep cu o literă mică sunt funcții (numite și metode), fac \"ceva\". Numele care încep cu o subliniere sunt de obicei acolo pentru funcționarea interioară a modulului și nu trebuie să vă faceți griji despre asta. Să folosim una dintre metodele de adăugare a unui obiect nou în documentul nostru:

box = doc.addObject("Part::Box","myBox")

Caseta noastră este adăugată în vederea arborescentă, dar nu se întâmplă nimic în vizualizarea 3D, deoarece atunci când lucrați cu Python, documentul nu este niciodată recalculat automat. Trebuie să o facem manual, ori de câte ori avem nevoie:

doc.recompute()

Acum, caseta noastră a apărut în vizualizarea 3D. Multe dintre butoanele din bara de instrumente care adaugă obiecte în FreeCAD fac de fapt două lucruri: adăugați obiectul și recalculează. Dacă ați activat opțiunea \"show script commands in Python console\" de mai sus, încercați acum să adăugați o sferă cu butonul corespunzător din Atetlierul Part și veți vedea că cele două linii de cod Python sunt executate unul după altul.

Puteți obține o listă cu toate tipurile de obiecte posibile cum ar fi Part::Box:

doc.supportedTypes()

Acum, să explorăm conținutul casetei noastre:

box.

Veți vedea imediat câteva lucruri foarte interesante, cum ar fi:

box.Height 

Aceasta va tipări înălțimea curentă a casetei noastre. Acum, să încercăm să schimbăm acest lucru:

box.Height = 5 

Dacă selectați caseta dvs. cu mouse-ul, veți vedea că în panoul proprietăților, în fila **Data**, proprietatea \'\' Height \'\' \'apare cu noua valoare. Toate proprietățile unui obiect FreeCAD care apar în tab urile **Data** and **View** sunt accesibile direct și de Python prin apelarea numelor lor, așa cum am făcut cu proprietatea Height. Proprietățile de date sunt accesibile direct de la obiectul însuși, de exemplu:

box.Length 

Proprietățile de vizualizare sunt stocate în interiorul unui **ViewObject**. Fiecare obiect FreeCAD posedă un ViewObject, care stochează proprietățile de vizualizare ale obiectului. Atunci când rulați FreeCAD fără interfața sa grafică (de exemplu când o lansați dintr-un terminal cu opțiunea de linie de comandă -c sau o utilizați dintr-un alt script Python), ViewObject nu este disponibil, deoarece nu există nici o vizualizare.

De exemplu, pentru a accesa culoarea liniei casetei noastre:

box.ViewObject.LineColor 

### Vectori și Plasament 

Vectorii reprezintă un concept fundamental în orice aplicație 3D. Este o listă cu 3 numere (x, y și z), care descriu un punct sau o poziție în spațiul 3D. O mulțime de lucruri se pot face cu vectori, cum ar fi adăugiri, scăderi, proiecții și multe altele. În FreeCAD vectorii funcționează astfel:

myvec = FreeCAD.Vector(2,0,0)
print(myvec)
print(myvec.x)
print(myvec.y)
othervec = FreeCAD.Vector(0,3,0)
sumvec = myvec.add(othervec)

O altă caracteristică comună a FreeCAD este plasarea **Placement**. Proprietate de plasare, care conține poziția (Base) și orientarea (Rotation) obiectului. Aceste proprietăți sunt ușor de manipulat de la Python, de exemplu pentru a muta obiectul nostru:

print(box.Placement)
print(box.Placement.Base)
box.Placement.Base = sumvec
otherpla = FreeCAD.Placement()
otherpla.Base = FreeCAD.Vector(5,5,0)
box.Placement = otherpla

**De citit în plus**


<div class="mw-translate-fuzzy">

-   [Python](https://www.python.org)
-   [Working with Macros](Macros.md)
-   [Introduction to Python scripting](Introduction_to_Python.md)
-   [Using Python in FreeCAD](Python_scripting_tutorial.md)
-   [The Python scripting wiki hub](Power_users_hub.md)


</div>





{{Powerdocnavi

}} 

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Python Code{{\#translation:}}](Category:Python_Code.md)
