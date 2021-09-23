# Line drawing function/ro



{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

Această pagină arată modul în care se poate construi cu ușurință o funcționalitatea avansată în Python. În acest exercițiu, vom construi un nou instrument care atrage o linie. Acest instrument poate fi apoi legat la o comandă FreeCAD și această comandă poate fi apelată de orice element al interfeței, cum ar fi un element de meniu sau un buton din bara de unelte.


</div>


<div class="mw-translate-fuzzy">

## Scriptul Principal 

Mai întâi vom scrie un script care conține toate funcționalitățile noastre. Apoi, vom salva acest lucru într-un fișier și îl vom importa în FreeCAD, astfel încât toate clasele și funcțiile pe care le scriem vor fi disponibile pentru FreeCAD. Deci, lansați editorul de text preferat și tastați următoarele rânduri:


</div>

First we will write a script containing all our functionality. Then we will save this in a file and import it in FreeCAD to make all its classes and functions available. Launch your favorite code editor and type the following lines:


```python
import FreeCADGui, Part
from pivy.coin import *

class line:

    """This class will create a line after the user clicked 2 points on the screen"""

    def __init__(self):
        self.view = FreeCADGui.ActiveDocument.ActiveView
        self.stack = []
        self.callback = self.view.addEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.getpoint)

    def getpoint(self, event_cb):
        event = event_cb.getEvent()
        if event.getState() == SoMouseButtonEvent.DOWN:
            pos = event.getPosition()
            point = self.view.getPoint(pos[0], pos[1])
            self.stack.append(point)
            if len(self.stack) == 2:
                l = Part.LineSegment(self.stack[0], self.stack[1])
                shape = l.toShape()
                Part.show(shape)
                self.view.removeEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.callback)
```


{{Top}}

## Explicații detaliate 


```python
import Part, FreeCADGui
from pivy.coin import *
```


<div class="mw-translate-fuzzy">

În Python, atunci când doriți să utilizați funcții dintr-un alt modul, trebuie să-l importați. În cazul nostru, vom avea nevoie de funcții de la [Part Workbench](Part_Workbench.md), pentru crearea liniei și de la modulul Gui (FreeCADGui), pentru a accesa vizualizarea 3D. De asemenea, avem nevoie de conținutul complet al bibliotecii de monede, astfel încât să putem folosi direct toate obiectele precum coin, SoMouseButtonEvent, (eveniment mouse) etc \...


</div>


```python
class line:
```

Aici definim clasa noastră principală. De ce folosim o clasă și nu o funcție? Motivul este că avem nevoie ca instrumentul nostru să rămână \"în viață\" în timp ce așteptăm ca utilizatorul să facă clic pe ecran. O funcție se termină atunci când sarcina sa a fost făcută, dar un obiect (o clasă definește un obiect) rămâne în viață până când este distrus.


```python
"""This class will create a line after the user clicked 2 points on the screen"""
```


<div class="mw-translate-fuzzy">

În Python, fiecare clasă sau funcție poate avea o descriere. Acest lucru este util în particular în FreeCAD, deoarece atunci când veți apela acea clasă în interpret, descrierea va fi afișată ca o sugestie .


</div>


```python
def __init__(self):
```


<div class="mw-translate-fuzzy">

Clasele Python întotdeauna trebuie să conțină o funcție \_\_init\_\_function, care este executată atunci când clasa este apelată să creeze un obiect. Deci, vom pune aici tot ce vrem să se întâmple atunci când instrumentul nostru de linie începe(este apelat).


</div>


```python
self.view = FreeCADGui.ActiveDocument.ActiveView
```


<div class="mw-translate-fuzzy">

Într-o clasă, de obicei, este de dorit să adăugați \"self\" înaintea unui nume de variabilă, astfel încât să fie ușor accesibilă tuturor funcțiilor din interiorul și din afara clasei respective. Aici vom folosi self.view pentru a accesa și manipula vizualizarea 3D activă.


</div>


```python
self.stack = []
```


<div class="mw-translate-fuzzy">

Aici vom crea o listă goală care va conține punctele în 3D trimise de funcția getpoint.


</div>


```python
self.callback = self.view.addEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.getpoint)
```


<div class="mw-translate-fuzzy">

Acesta este un punct/parte importantă: Deoarece că este vorba de o o scenă [coin3D](http://www.coin3d.org/), FreeCAD folosește mecanismul de apel invers, care permite unei funcții să fie apelată de fiecare dată când se întâmplă un anumit eveniment scenă. În cazul nostru, creăm un apel invers pentru evenimentele [SoMouseButtonEvent](http://doc.coin3d.org/Coin/group__events.html) și îl legăm la funcția getpoint. Acum, de fiecare dată când este apăsat sau eliberat un buton mouse-ului, funcția GetPoint va fi executată.


</div>


<div class="mw-translate-fuzzy">

Rețineți că există, de asemenea, o alternativă la addEventCallbackPivy() numită addEventCallback() care exclude utilizarea pivy. Dar, din moment ce pivu este o modalitate foarte eficientă și naturală de a accesa orice parte a scenei coin, este mult mai bine să o utilizați cât de mult puteți!


</div>


{{Top}}


```python
def getpoint(self, event_cb):
```


<div class="mw-translate-fuzzy">

Acum definim funcția GetPoint, care va fi executată atunci când un buton al mouse-ului este apăsat într-o vizualizare 3D. Această funcție va primi un argument, pe care îl vom numi event\_cb. De la acest apel al evenimentului, putem accesa obiectul eveniment, care conține mai multe informații -mai multe informații pe această pagină (modul info[here](Code_snippets#Observing_mouse_events_in_the_3D_viewer_via_Python.md)).


</div>


```python
if event.getState() == SoMouseButtonEvent.DOWN:
```


<div class="mw-translate-fuzzy">

Funcția GetPoint va fi apelată când un buton al mouse-ului este apăsat sau eliberat. Dar vrem să alegem un punct 3D numai atunci când este presat (altfel am obține două puncte foarte aproape unul de celălalt). Așa că trebuie să verificăm asta


</div>


```python
pos = event.getPosition()
```


<div class="mw-translate-fuzzy">

Aici găsim coordonatele cursorului mouse-ului pe ecran


</div>


```python
point = self.view.getPoint(pos[0], pos[1])
```


<div class="mw-translate-fuzzy">

Această funcție ne dă un vector FreeCAD (x, y, z) ale punctului care se află pe planul focal, chiar sub cursorul mouse-ului. Dacă vă aflați într-o vizualizare a camerei foto, imaginați-vă camera trece prin cursorul mouse-ului și atinge planul focal. Acesta este punctul nostru 3D. Dacă suntem în vedere ortogonală, raza este paralelă cu direcția de vizualizare.


</div>


```python
self.stack.append(point)
```


<div class="mw-translate-fuzzy">

Noi adăugăm elementul nostru nou în stivă/morman


</div>


```python
if len(self.stack) == 2:
```

Avem toate punctele necesare? dacă da, atunci să tragem linia!


```python
l = Part.LineSegment(self.stack[0], self.stack[1])
```


<div class="mw-translate-fuzzy">

Aici folosim funcția line() din [Part Workbench](Part_Workbench.md) care a creat o linie din două vectori FreeCAD. Tot ceea ce creăm și modificăm în interiorul modulului Part, rămâne în modulul Part. Deci, până acum, am creat o piesă tip linie. Nu este legat de niciun obiect al documentului nostru activ, deci nu apare nimic pe ecran.


</div>


```python
shape = l.toShape()
```


<div class="mw-translate-fuzzy">

Documentul FreeCAD poate accepta decât forme din modulul Part Module. Formele sunt cel mai generic tip al Part Module. Deci, trebuie să convertim linia noastră într-o formă înainte de a o adăuga la document.


</div>


```python
Part.show(shape)
```


<div class="mw-translate-fuzzy">

Modulul Part Module are o funcție foarte utilă show(), care creează un obiect nou în document și se leagă la o formă. De asemenea, am putea să avem un nou obiect în primul document, apoi să-l legăm manual la formă.


</div>


```python
self.view.removeEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.callback)
```


<div class="mw-translate-fuzzy">

Deoarece am terminat cu linia noastră, să eliminăm mecanismul de apel invers, care consumă cicluri CPU prețioase.


</div>


{{Top}}


<div class="mw-translate-fuzzy">

## Testing & Using the script 

Acum, hai să salvăm scriptul într-un loc unde interpretul Python de la FreeCAD îl va găsi. Când importați module, interpretorul va căuta în următoarele locuri: căile de instalare python, directorul bin FreeCAD și toate directoarele modulelor FreeCAD. Deci, cea mai bună soluție este să creați un director nou într-unul din FreeCAD [ Mod directories](Installing_more_workbenches.md) și să salvați scriptul în el. De exemplu, să facem un director \"MyScripts\" și să salvăm scriptul nostru ca \"exercise.py\".


</div>

Now let\'s save our script in a folder where the FreeCAD Python interpreter can find it. When importing modules, the interpreter will look in the following places: the Python installation paths, the FreeCAD {{FileName|bin}} folder, and all FreeCAD {{FileName|Mod}} (module) folders. So the best solution is to create a new folder in one of the {{FileName|Mod}} folders. Let\'s create a {{FileName|MyScripts}} folder there and save our script in it as {{FileName|exercise.py}}.


<div class="mw-translate-fuzzy">

Acum, totul este gata, să începem FreeCAD, să creăm un nou document și, în interpretorul python, să tastăm:


</div>


```python
import exercise
```


<div class="mw-translate-fuzzy">

Dacă nu apare niciun mesaj de eroare, înseamnă că scriptul nostru de exerciții **exercise** a fost încărcat. Acum îi putem verifica conținutul cu:


</div>


```python
dir(exercise)
```


<div class="mw-translate-fuzzy">

Comanda **dir()** este o comandă python încorporată care listează/enumeră conținutul unui modul. Putem vedea că clasa noastră **class line()** este aici, așteptându-ne. Acum, să o testăm:


</div>


```python
'line' in dir(exercise)
```

Now let\'s test it:


```python
exercise.line()
```


<div class="mw-translate-fuzzy">

Apoi, faceți dublu clic în vizualizarea 3D, și bingo, aici este linia noastră! Pentru a face din nou, doar tastați **exercise.line()** din nou, și din nou și din nou \... Vă simțiți minunat, nu-i așa?


</div>


{{Top}}


<div class="mw-translate-fuzzy">

## Înregistrarea scriptului în interfața FreeCAD 

Acum, pentru ca noul nostru instrument de trasat linii să fie foarte cool, ar trebui să aibă un buton pe interfață, deci să nu trebuiescă să tastăm toate acele lucruri de fiecare dată. Cea mai ușoară cale este să ne transformăm noul director MyScripts într-un atelier de lucru complet FreeCAD. Este ușor, tot ce este necesar este să plasați un fișier numit **InitGui.py** în directorul MyScripts. InitGui.py va conține instrucțiunile pentru a crea un nou atelier de lucru și va adăuga noul instrument. În plus, va trebui să transformăm un pic codul nostru de exerciții, astfel încât instrumentul line() este recunoscut ca o comandă oficială FreeCAD. Să începem prin a face un fișier InitGui.py și scrieți următorul cod în el:


</div>

For our new line tool to be really useful, and to avoid having to type all that stuff, it should have a button in the interface. One way to do this is to transform our new {{FileName|MyScripts}} folder into a full FreeCAD workbench. This is easy, all that is needed is to put a file called {{FileName|InitGui.py}} inside the {{FileName|MyScripts}} folder. {{FileName|InitGui.py}} will contain the instructions to create a new workbench, and add our new tool to it. Besides that we will also need to change our exercise code a bit, so the `line()` tool is recognized as an official FreeCAD command. Let\'s start by creating an {{FileName|InitGui.py}} file, and writing the following code in it:


```python
class MyWorkbench (Workbench):

    MenuText = "MyScripts"

    def Initialize(self):
        import exercise
        commandslist = ["line"]
        self.appendToolbar("My Scripts", commandslist)

Gui.addWorkbench(MyWorkbench())
```


<div class="mw-translate-fuzzy">

Până acum, ar fi trebuit să fi înțeles deja scriptul de mai sus, mă gândesc eu: Creați o nouă clasă pe care o numiți MyWorkbench. Îi vom da un titlu (MenuText) și vom defini o funcție Initialize() care va fi executată atunci când atelierul de lucru este încărcat în FreeCAD. În această funcție, încărcăm conținutul fișierului de exerciții și adăugăm comenzile FreeCAD găsite în interiorul unei liste de comenzi. Apoi, facem o bară de instrumente numită \"Scripturile mele\" și îi atribuim comenzile noastre. În prezent, desigur, avem doar un singur instrument, astfel că lista noastră de comenzi conține doar un singur element. Apoi, odată ce atelierul nostru de lucru este gata, îl adăugăm la interfața principală.


</div>


<div class="mw-translate-fuzzy">

Dar acest lucru nu va funcționa, deoarece o comandă FreeCAD trebuie să fie formatată într-un anumit mod de lucru. Deci, va trebui să transformăm puțin instrumentul nostru **line()**. Noul nostu script **exercise.py** va arăta cam așa:


</div>


```python
import FreeCADGui, Part
from pivy.coin import *

class line:

    """This class will create a line after the user clicked 2 points on the screen"""

    def Activated(self):
        self.view = FreeCADGui.ActiveDocument.ActiveView
        self.stack = []
        self.callback = self.view.addEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.getpoint)

    def getpoint(self, event_cb):
        event = event_cb.getEvent()
        if event.getState() == SoMouseButtonEvent.DOWN:
            pos = event.getPosition()
            point = self.view.getPoint(pos[0], pos[1])
            self.stack.append(point)
            if len(self.stack) == 2:
                l = Part.LineSegment(self.stack[0], self.stack[1])
                shape = l.toShape()
                Part.show(shape)
                self.view.removeEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.callback)

    def GetResources(self):
        return {'Pixmap': 'path_to_an_icon/line_icon.png', 'MenuText': 'Line', 'ToolTip': 'Creates a line by clicking 2 points on the screen'}

FreeCADGui.addCommand('line', line())
```


<div class="mw-translate-fuzzy">

Ceea ce am făcut aici? noi am transformat funcția noastră \_\_init\_\_() function într-o funcție **Activated()**, deoarece atunci când comenzile FreeCAD sunt executate, ele execută automat funcția **Activated()**. Am adăugat, de asemenea, o funcție GetResources (), care informează FreeCAD unde poate găsi o pictogramă pentru instrument și care va fi numele și sugestia/indicația instrumentului nostru. Orice imagine jpg, png sau svg va funcționa ca o pictogramă/iconiță, poate fi orice dimensiune, dar este mai bine să utilizați o dimensiune care este aproape de aspectul final, cum ar fi 16x16, 24x24 sau 32x32. Apoi, adăugăm **class line()** ca o comandă oficială FreeCAD cu metoda **addCommand()**.


</div>


<div class="mw-translate-fuzzy">

Asta este, vrem să reporniți FreeCAD și vom avea un nou atelier de lucru cu noul nostru instrument linie **line**!


</div>


{{Top}}

## Deci vrei mai mult? 


<div class="mw-translate-fuzzy">

Dacă ți-a plăcut acest exercițiu, de ce să nu încerci să îmbunătățești acest mic instrument? Sunt multe lucruri care pot fi făcute, ca de exemplu:

-   Adăugați comentarii utilizatorilor: până acum am făcut un instrument foarte subțire îmbrăcat, utilizatorul ar putea fi un pic pierdut atunci când îl utilizează. Așadar, am putea adăuga comentarii, spunându-i ce să facă în continuare. De exemplu, puteți emite mesaje către consola FreeCAD. "Aruncați o privire" în modulul FreeCAD.Console
-   Adăugați posibilitatea de a introduce manual coordonatele punctelor 3D. Uitați-vă la funcția python input(), de exemplu,
-   Adăugați posibilitatea de a adăuga mai mult de 2 puncte
-   Adăugați evenimente pentru alte lucruri: Acum verificăm doar evenimentele butonului mouse-ului, dacă am face și ceva când mouse-ul este mutat, cum ar fi afișarea coordonatelor curente?
-   Dați un nume obiectului creat și multe alte lucruri.

Nu ezitați să vă scrieți întrebările sau ideile pe [forum](http://forum.freecadweb.org/)!


</div>

Don\'t hesitate to ask questions or share ideas on the [forum](https://forum.freecadweb.org/)! {{Top}} {{Powerdocnavi}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)
