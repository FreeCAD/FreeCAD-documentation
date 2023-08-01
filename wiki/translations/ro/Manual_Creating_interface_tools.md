# Manual:Creating interface tools/ro
{{Manual:TOC/ro}}

În ultimele două capitole, am văzut cum să [create Part geometry](Manual_Creating_and_manipulating_geometry.md) și [create parametric objects](Manual_Creating_parametric_objects.md). O ultimă piesă lipsește pentru a obține un control deplin peste FreeCAD: Creați instrumente care vor interacționa cu utilizatorul.

În multe situații, nu este foarte ușor să construim un obiect cu valori zero, așa cum am făcut-o cu dreptunghiul din capitolul precedent, și apoi să cerem utilizatorului să completeze valorile Înălțime și Lățime din panoul Proprietăți. Aceasta funcționează pentru un număr foarte mic de obiecte, dar va deveni foarte obositoare dacă aveți multe dreptunghiuri. O modalitate mai bună ar fi să puteți da deja înălțimea și lățimea la crearea dreptunghiului.

Python oferă un instrument de bază pentru ca utilizatorul să introducă text pe ecran:

text = raw_input("Height of the rectangle?")
print("The entered height is ",text)

Totuși, aceasta necesită o consolă Python care rulează, iar atunci când executăm codul dintr-o macrocomandă, nu suntem întotdeauna siguri că avem Consola Python va fi activată pe mașina utilizatorului.

Interfața utilizatorului grafic [Graphical User Interface](https://en.wikipedia.org/wiki/Graphical_user_interface), sau GUI, adică întreaga parte a programului FreeCAD care este afișat pe ecran (meniul, barele de instrumente, vizualizarea 3D etc.), este acolo în acest scop: interacționați cu utilizatorul. Interfața FreeCAD este construită cu [Qt](https://en.wikipedia.org/wiki/Qt_(software)), o trusă de instrumente GUI foarte variate, care oferă o gamă largă de instrumente, cum ar fi casete, butoane, etichete, casete de introducere a textului sau meniuri derulante. Acestea sunt numite generic "widget-uri".

Instrumentele Qt sunt foarte ușor de utilizat din Python, datorită unui modul Python numit Pyside [Pyside](https://en.wikipedia.org/wiki/PySide) (Există și alte module Python care comunică cu Qt de la Python). Acest modul vă permite să creați și să interacționați cu widget-uri, să citiți ce a făcut utilizatorul cu ele sau să faceți lucruri atunci când, de exemplu, a fost apăsat un buton.

Qt furnizează de asemenea un alt instrument numit [Qt Designer](http://doc.qt.io/qt-4.8/designer-manual.html), care astăzi este încorporată într-o aplicație mai mare numită Qt Creator [Qt Creator](https://en.wikipedia.org/wiki/Qt_Creator).Permite crearea grafică a casetelor de dialog și a panourilor de interfață, în loc să le codeze manual. In acest capitol,vom folosi Qt Creator pentru a proiecta un widget pe care îl vom folosi în panoul de Sarcini **Task** al FreeCAD. Prin urmare, va trebui să descărcați și să instalați Qt Creator de pe [official page](https://www.qt.io/ide/) dacă sunteți pe Windows sau Mac (sub Linux, va fi de obicei disponibilă din aplicația dvs. de manager de software).

În exercițiul următor, vom crea mai întâi un panou cu Qt Creator care solicită valorile de lungime, lățime și înălțime, apoi vom crea în jurul lui o clasă Python care va citi valorile introduse de utilizator din panou și va crea o casetă cu dimensiunile date. Acest Python va fi folosit de FreeCAD pentru afișarea și controlul panoului de sarcini:

![](images/Exercise_python_07.jpg )


<div class="mw-translate-fuzzy">

Să începem prin crearea unui widget. Start Qt Creator, apoi meniul **File -\> New File or Project -\> Files and Classes -\> Qt -\> Qt Designer Form -\> Dialog without buttons**. Click **Next**, dați-i un nume de fișier pentru a-l salva, click **Next**, lăsați toate câmpurile de proiect la valoarea lor implicită (\"\"), și **Create**. Sistemul de sarcini FreeCAD va adăuga automat butoanele OK / Anulare, așa că am ales aici o casetă de dialog fără butoane.


</div>

![](images/Exercise_python_06.jpg )


<div class="mw-translate-fuzzy">

-   Găsiți **Label** din lista din panoul din stânga și glisați-o pe panza widget-ului nostru. Faceți dublu clic pe eticheta locației recente și modificați textul sau la **Lungime**.
-   Faceți clic dreapta pe pânza widget și alegeți **Lay out-\> Lay out in a Grid**. Acest lucru va pune widgetul nostru într-o rețea cu o singură celulă, ocupată de prima noastră etichetă. Acum putem adăuga următoarele elemente la stânga, la dreapta, în partea de sus sau în partea de jos a primei noastre etichete, iar grilă se va extinde automat.
-   Adăugați încă două etichete la prima și schimbați textul la Lățime și înălțime:


</div>

![](images/Exercise_python_08.jpg )


<div class="mw-translate-fuzzy">

-   Acum plasați 3 **Double Spin Box** widgets lângă etichetele Lungime, Lățime și Înălțime. Pentru fiecare dintre ele, în panoul din stânga jos, care arată toate setările disponibile pentru widgetul selectat, localizați **Suffix** și definiți sufixul în **mm**. FreeCAD are un widget mai avansat, care poate gestiona unități diferite, dar acest lucru nu este disponibil în mod implicit în Creator Qt (dar poate fi compilat [compiled](Compile_on_Linux#Qt_designer_plugin.md)), așa că vom folosi o Double Spin Box standard și vom adăuga sufixul \"mm\" pentru a ne asigura că utilizatorul știe în ce unități lucrează:


</div>

![](images/Exercise_python_09.jpg )

-   Acum widget-ul nostru s-a terminat, trebuie doar să ne asigurăm de ultimul lucru. Din moment ce FreeCAD va trebui să acceseze acel widget și să citească valorile Lungime, Lățime și Înălțime, trebuie să le dăm nume potrivite widget-urilor, astfel încât să le putem recupera cu ușurință din interiorul FreeCAD. Faceți clic pe fiecare dintre Double Spin Boxes și în fereastra din partea dreaptă sus, faceți dublu clic pe Objedt Name și schimbați-le la ceva ușor de memorat, de exemplu: BoxLength, BoxWidth și BoxHeight:

![](images/Exercise_python_10.jpg )


<div class="mw-translate-fuzzy">

-   Salvează fișierul, puteți închide cum Qt Creator, restul va fi făcut în Python.
-   Deschideți FreeCAD și creați un nou macro din meniul **Macro -\> Macros -\> Create**
-   Lipiți următorul cod. Asigurați-vă că schimbați calea fișierului pentru a se potrivi de unde ați salvat fișierul .ui creat în QtCreator:


</div>


```python
import FreeCAD,FreeCADGui,Part
 
# CHANGE THE LINE BELOW
path_to_ui = "C:\Users\yorik\Documents\dialog.ui"
 
class BoxTaskPanel:
   def __init__(self):
       # this will create a Qt widget from our ui file
       self.form = FreeCADGui.PySideUic.loadUi(path_to_ui)
 
   def accept(self):
       length = self.form.BoxLength.value()
       width = self.form.BoxWidth.value()
       height = self.form.BoxHeight.value()
       if (length == 0) or (width == 0) or (height == 0):
           print("Error! None of the values can be 0!")
           # we bail out without doing anything
           return
       box = Part.makeBox(length,width,height)
       Part.show(box)
       FreeCADGui.Control.closeDialog()
        
panel = BoxTaskPanel()
FreeCADGui.Control.showDialog(panel)
```

În codul de mai sus, am folosit o funcție convenabilă (PySideUic.loadUi) din modulul FreeCADGui. Această funcție încarcă un fișier .ui, creează un widget Qt din acesta și scrie numele, astfel încât să putem accesa cu ușurință subspațiul după nume (ex: self.form.BoxLength).

Funcția \"accept\" este, de asemenea, o facilitate oferită de Qt. Atunci când există un buton \"OK\" într-o casetă de dialog (care este cazul în mod implicit când se utilizează panoul Task FreeCAD) \"accept\" va fi executat automat când apăsați butonul \"OK\". În mod similar, puteți adăuga o funcție de \"respingere\" care se execută atunci când apăsați butonul \"Cancel\". În cazul nostru, am eliminat această funcție, așa că apăsând \"Cancel\" va cauza comportamentul implicit (nu faceți nimic și închideți caseta de dialog).

Dacă implementăm oricare dintre funcțiile de acceptare sau de respingere, comportamentul implicit (nu face nimic și închide) nu va mai avea loc. Așa că trebuie noi înșine trebuie să închidem panoul de sarcini . Acest lucru se face cu:


```python
FreeCADGui.Control.closeDialog() 
```

Odată ce avem BoxTaskPanel, care are un widget numit \"self.form\" și 2 - dacă este necesar, funcțiile Acceptă și Respinge, putem deschide panoul de sarcini cu acesta, ceea ce se face cu aceste două linii :


```python
panel = BoxTaskPanel()
 FreeCADGui.Control.showDialog(panel)
```

Rețineți că widget-ul creat de PySideUic.loadUi nu este specific pentru FreeCAD, este un widget standard Qt care poate fi utilizat cu alte instrumente Qt. De exemplu, am fi arătat o casetă de dialog separată cu ea. Încercați acest lucru în Consola Python a FreeCAD (folosind calea corectă spre fișierul .ui, desigur):


```python
from PySide import QtGui
 w = FreeCADGui.PySideUic.loadUi("C:\Users\yorik\Documents\dialog.ui")
 w.show()
```

Bineînțeles noi nu am adăugat butonul \"OK\" sau \"Cancel\" în caseta nostră de dialog, deoarece a fost făcut pentru a fi utilizat de panoul sarcini(Task) FreeCAD, care oferă deja astfel de butoane. Deci, nu există nicio modalitate de a închide dialogul(altul decât apăsarea butonului de închidere a ferestrei). Dar funcția show () creează o casetă de dialog nemodal, ceea ce înseamnă că aceasta nu blochează restul interfeței. Deci, în timp ce dialogul este încă deschis, putem citi valorile câmpurilor:


```python
w.BoxHeight.value() 
```

Aceasta este foarte util de a fi încercat.

În cele din urmă, nu uitați că există mult mai multe despre widgeturile QT pe FreeCAD Wiki, în secțiunea [Python Scripting](Power_users_hub.md), care conține [dialog creation tutorial](Dialog_creation.md), o parte terță specială [PySide tutorial](PySide.md) care acoperă în mode extins subiectul.


<div class="mw-translate-fuzzy">

-   [Qt Creator](https://en.wikipedia.org/wiki/Qt_Creator)
-   [Installing Qt Creator](https://www.qt.io/ide/)
-   [Python scripting documentation](Power_users_hub.md)
-   [Dialog creation tutorial](Dialog_creation.md)
-   [PySide tutorials](PySide.md)
-   [PySide documentation](http://srinikom.github.io/pyside-docs/index.html)


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Manual:Creating interface tools/ro
