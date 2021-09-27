# Draft API/ro
<div class="mw-translate-fuzzy">

Aceste funcții fac parte din modulul Draft-Desen 2D și pot fi utilizate în scripturi și macrocomenzi sau de la interpretorul python, odată ce modulul Draft a fost importat.


</div>

These functions are part of the [Draft Workbench](Draft_Workbench.md) and can be used in [macros](macros.md) and from the [Python](Python.md) console once the `Draft` module has been imported.

Example: 
```python
import FreeCAD, Draft

myrect = Draft.makeRectangle(4, 3)
mydistance = FreeCAD.Vector(2, 2, 0)
Draft.move(myrect, mydistance)
```


{{APIFunction | cut | FreeCAD.Object, FreeCAD.Object | Returnează un obiect tăiat făcut din diferența dintre cele 2 obiecte date. Obiectele originale se ascund. | Un obiect nou creat}}

{{APIFunction | extrude | FreeCAD.Object, Vector | Extrudeaza obiectul dat in directia data de vector. Obiectul inițial devine ascuns | Un obiect nou creat}}

{{APIFunction | formatObject | FreeCAD.Object, [FreeCAD.Object] | Această funcție se aplică obiectului țintă dat, ținând cont de proprietăților curente setate pe bara de instrumente Draft (culoarea liniei și lățimea liniei) sau copiază proprietățile unui al doilea obiect dacă sunt furnizate. De asemenea, plasează obiectul în grupul de construcție dacă este apăsat butonul de construcție. | Nimic}}

{{APIFunction | fuse | FreeCAD.Object, FreeCAD.Object | Returnează un obiect făcut din unirea celor două obiecte date. În cazul în care obiectele sunt coplanare, se folosește o schemă specială, în caz contrar obiectul final este o siguranță standard a părții. | Un obiect nou creat}} 


{{APIFunction | getDraftPath | [string] | Returnează calea de accesa a utilizatorului sau a sistemului de la  care modulul Draft rulează. Dacă este furnizat o sub cale sau un nume de fișier, este furnizat  returnează calea completă la sub-calea din modulul Schiță. | O cale de fișier}}


{{APIFunction | getGroupContents | list | Scanează recursiv lista dată pentru grupuri. În cazul în care grupurile sunt întâlnite, conținutul acestora este adăugat la listă. | O listă a obiectelor FreeCAD}}


{{APIFunction|getRealName|string|Separă numărul din numele unui obiect .| Numele obiectului astfel dezbrăcat}}

{{APIFunction|getSelection| |Returnează selecția curentă FreeCAD.| Secțiunea curentă FreeCAD }}


{{APIFunction|makeCircle|radius, [placement], [facemode], [startangle], [endangle]| Creează un obiect de cerc cu o rază dată. Dacă este oferită o destinație de plasare, este utilizată. Dacă facemodul este Fals, cercul este afișat ca un filament (polilinie), alfel ca o fațetă. În cazul în care  '''startAngle''' și '''endAngle''' sunt date (în grade), ele sunt folosite și obiectul apare ca un arc de cerc. | Obiectul nou creat.}}


{{APIFunction | makeDimension | Vector, Vector, [Vector] sau FreeCAD.Object, int, [Vector] | Creează un obiect '''Cotă''' care măsoară distanța dintre primul și al doilea vector, cu linia de cotă care trece prin cel de-al treilea vector, dacă este prevăzută. Se va utiliza lățimea curentă a liniei și culoarea din bara de instrumente Draft. În loc de 2 vectori, puteți trece și un obiect FreeCAD și două numere întregi (și opțional un vector) unde trebuie să treacă linia de dimensiuni. În acest caz, dimensiunea va fi asociată cu obiectul și va măsura două dintre vârfurile sale, indicate de cele două numere de index date. | Un nou obiect va fi creat.}}

{{APIFunction | makeLine | Vector, Vector | Creează o linie între cei doi vectori dat. Se va utiliza lățimea curentă a liniei și culoarea din bara de instrumente Draft. | Un nou obiect va fi creat.}} 


{{APIFunction | makeRectangle | lungime, lățime, [plasare], [facemode] | Creează un obiect Rectangular cu lungimea în direcția X și înălțime în direcția Y. Dacă este oferită o destinație de plasare, este utilizată. Dacă '''facemodul este Fals''', dreptunghiul este afișat ca un cadru de sârmă, altfel ca o față. Se va utiliza lățimea curentă a liniei și culoarea din bara de instrumente Draft. | Un obiect nou este creat.}}


{{APIFunction | makeText | șir sau listă, [Vector], [screenmode] | Creează un obiect Text, un vector este furnizat, care conține șirul sau șirurile date în listă, un șir după linie. Culoarea curentă din bara de instrumente Draft și înălțimea textului și fontul specificat în preferințe sunt utilizate. Dacă textul de ecran este True, textul se află întotdeauna în direcția vizualizării, altfel se află pe planul XY.| Un obiect nou este creat.}}


{{APIFunction | makeWire | list sau Part.Wire, [closed], [placement] [facemode] | Creează un obiect DWire din lista dată de vectori sau din sirul dat. Dacă obiectul este închis (True), sau dacă primul și ultimul punct sunt identice, firul este închis. Dacă '''facemode''' este adevărat (și firul este închis), firul va apărea umplut. Se va folosi lățimea curentă a liniei și culoarea currentă din bara de instrumente Draft .|  Un nou obiect Draft DWire este creat (nu o Part Wire).}}


{{APIFunction | move | FreeCAD.Object sau listă, Vector, [copymode]|Mută obiectul dat sau obiectele conținute în lista dată în direcția și distanța indicată de vectorul dat. Dacă '''CopyMode''' este True, obiectele reale nu sunt mutate, spre deosebire de copiile lor care  sunt create în schimb.|Obiectul (obiectele) (sau copiile lor dacă  '''CopyMode''' a fost True)}}

{{APIFunction | precision | Returneaza valoarea de precizie din Proiectarea setarilor utilizatorului. | Un intreg.}} 


{{APIFunction | rotate | FreeCAD.Object sau lista, unghiul, [center], [axis], [copymode] | Rotește obiectul/obeictele conținute în lista dată, cu unghiul dat, în jurul centrului dat, Dacă axa este omisă, rotația va fi în jurul axei  '''Z''' verticale. În cazul în care '''CopyMode''' este True, obiectele reale nu sunt mutate, dar copiile sunt create în loc de obiecte. | Obiecte (sau copii ale acestora).}}

{{APIFunction | scale | FreeCAD.Object sau listă, vector, [center], [copymode] | REdimensionează/Scalează obiectul dat sau obiectele conținute în lista dată cu factorii de scalare definiți de vectorul dat (pe direcțiile ‚'''X, Y și Z''') în jurul centrului dat, dacă există. În cazul în care '''CopyMode''' este True, obiectele reale nu sunt mișcate, ci vor fi create în schimb copii .| Obiectele (sau copiile lor).}}

{{APIFunction | select | FreeCAD.Object | Deselectează totul și selectează numai obiectul trecut | Nimic.}} 


{{APIFunction | shapify | FreeCAD.Object | Transformă un obiect de formă parametric în non-parametric. | Obiectul nou.}}


{{APIFunction | draftify | FreeCAD.Object sau listă | Transformă obiectul dat sau fiecare obiect în filamente parametric al.|Nimic }}


{{APIFunction | getSVG | FreeCAD.Object, [linemodifier], [textmodifier], [(u, v)] | Creează o reprezentare SVG a obiectului dat. Atributul linemodifier este un factor de scalare (în procente) pentru lățimea liniei și textmodifier pentru dimensiunea textului. De asemenea, puteți furniza opțional o tuplă de vectori pentru a defini un plan de proiecție, altfel geometria va fi proiectată pe planul XY. | Un șir care conține o reprezentare SVG a obiectului dat.}}


 




_ _

---
[documentation index](../README.md) > [API](Category_API.md) > [Draft](Draft_Workbench.md) > Draft API/ro
