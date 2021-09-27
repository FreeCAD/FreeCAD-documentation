# Manual:Creating parametric objects/ro
{{Manual:TOC/ro}}

În _, Am văzut cum este creată geometrie Pieselor și cum este afișată aceasta pe ecran, atașând-o la un documente obeict \"dumb\" (non-parametric). Acest lucru este obositor când vrem să schimbăm forma acestui obiect. Va trebui să creăm o nouă formă, apoi să o atribuim din nou obiectului nostru.

Cu toate acestea, am văzut, de asemenea, în toate capitolele anterioare ale acestui manual cât de puternice sunt obiectele parametrice. Trebuie doar să schimbăm o proprietate, iar forma se recalculează în timp real.

Pe plan intern, obiectele parametrice nu fac nimic diferit de ceea ce am făcut: ele recalculează conținutul proprietății Shape, în mod repetat, de fiecare dată când o altă proprietate a fost modificată.

FreeCAD oferă un sistem foarte convenabil pentru crearea a unor astfel de obiecte parametrice complet în în Python. Ele constau dintr-o clasă Python simplă, care definește toate proprietățile de care are nevoie obiectul și ce se va întâmpla când se schimbă una dintre aceste proprietăți. Structura obiectului parametric este la fel de simplă:

class myParametricObject:
  def __init__(self,obj):
    obj.Proxy = self
    obj.addProperty("App::PropertyFloat","MyLength")
    ...
       
  def execute(self,obj):
    print ("Recalculating the shape...")
    print ("The value of MyLength is:")
    print (obj.MyLength)
    ...

Toate clasele Python au de obicei o metodă \_\_init\_\_. Ceea ce este în interiorul acestei metode este executat atunci când clasa este instanțiată (ceea ce înseamnă că, în argoul de programare, că un obiect Python este creat din această clasă. Înțelegem o clasă ca pe un \"șablon\" pentru crearea de copii în direct ale acestui șablon). Aici, în funcția noastră de inițializare (funcția \_\_init\_\_), facem două lucruri importante: 1 - pentru a stoca clasa însăși în atributul \"Proxy\" al obiectului în documentul nostru FreeCAD, adică documentul obiect FreeCAD va purta acest cod în sine și 2 - va crea toate proprietățile pe care le are obiectul nostru. Există multe tipuri de proprietăți disponibile, puteți obține lista completă introducând acest cod:

FreeCAD.ActiveDocument.addObject("Part::FeaturePython","dummy").supportedProperties() 

Apoi, a doua parte importantă este metoda de executare. Orice cod din această metodă va fi executat atunci când obiectul este marcat pentru a fi recalculat, ceea ce se va întâmpla când o proprietate a fost schimbată. Acesta este tot ceea ce este de făcut. În interiorul execuției, trebuie să faceți tot ce trebuie făcut, adică să calculați o nouă formă și să atribuiți obiectului în sine ceva asemănător cu obj.Shape = myNewShape. Acesta este motivul pentru care metoda execută ia un argument \"obj\", care va fi obiectul documentului FreeCAD în sine, astfel încât să îl putem manipula în codul nostru python.

Un ultim lucru este important de reținut: Când creați astfel de obiecte parametrice într-un document FreeCAD, atunci când salvați fișierul, codul python de mai sus nu este stocat în interiorul fișierului. Din motive de securitate, dacă un fișier FreeCAD conține cod, ar fi posibil ca cineva să distribuie fișiere FreeCAD care conțin cod malitios care ar putea dăuna computerelor altor persoane. Deci, dacă distribuiți un fișier care conține obiecte făcute cu codul de mai sus, un astfel de cod trebuie să fie prezent și pe computerul care va deschide fișierul. Cea mai ușoară modalitate de a realiza acest lucru este de a salva codul de mai sus într-o macrocomandă și de a distribui macro-ul împreună cu fișierul FreeCAD sau de a vă distribui macrocomanda în depozitul de macrocomanzi a FreeCAD [ FreeCAD repository](Macros_recipes.md) de unde oricine îl poate descărca.

Mai jos, vom face un exercițiu mic, construind un obiect parametric care este o simplă fațetă parametrică dreptunghiulară. Exemple mai complexe sunt disponibile pe [parametric object example](Scripted_objects.md) și în chiar însuși [FreeCAD source code](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/TemplatePyMod/FeaturePython.py) .

Vom da obiectului nostru două proprietăți: lungimea și lățimea, pe care le vom folosi pentru a construi un dreptunghi. Apoi, deoarece obiectul nostru va avea deja o proprietate de plasament predefinită (orice obiect geometric are una implicită, nu este nevoie să-l adăugăm noi înșine), vom deplasa dreptunghiul nostru la locația / orientarea setată în Placement, astfel încât utilizatorul să poată muta dreptunghiul oriunde editând proprietatea de plasare.

class ParametricRectangle:
 def __init__(self,obj):
   obj.Proxy = self
   obj.addProperty("App::PropertyFloat","Length")
   obj.addProperty("App::PropertyFloat","Width")
 def execute(self,obj):
   # we need to import the FreeCAD module here too, because we might be running out of the Console
   # (in a macro, for example) where the FreeCAD module has not been imported automatically
   import Part,FreeCAD
   
   # first we need to make sure the values of Length and Width are not 0
   # otherwise the Part.Line will complain that both points are equal
   if (obj.Length == 0) or (obj.Width == 0):
     # if yes, exit this method without doing anything
     return
     
   # we create 4 points for the 4 corners
   v1 = FreeCAD.Vector(0,0,0)
   v2 = FreeCAD.Vector(obj.Length,0,0)
   v3 = FreeCAD.Vector(obj.Length,obj.Width,0)
   v4 = FreeCAD.Vector(0,obj.Width,0)
   
   # we create 4 edges
   e1 = Part.Line(v1,v2).toShape() # Warning. Since FC v0.17, use Part.LineSegment instead of Part.Line
   e2 = Part.Line(v2,v3).toShape()
   e3 = Part.Line(v3,v4).toShape()
   e4 = Part.Line(v4,v1).toShape()
   
   # we create a wire
   w = Part.Wire([e1,e2,e3,e4])
   
   # we create a face
   f = Part.Face(w)
   
   # All shapes have a Placement too. We give our shape the value of the placement
   # set by the user. This will move/rotate the face automatically.
   f.Placement = obj.Placement
   
   # all done, we can attribute our shape to the object!
   obj.Shape = f

În loc să lipiți (dela copy&paste) codul de mai sus în consolă Python, ar trebui să îl salvăm undeva, așa că îl putem reutiliza și modifica mai târziu. De exemplu într-o macrocomandă nouă (meniul Tools -> Macros -> Create). Denumiți-o, de exemplu, "ParamRectangle". Cu toate acestea, macrocomenzile FreeCAD sunt salvate cu o extensie .FCMro, pe care Python nu o recunoaște la import. Deci, înainte de a utiliza codul de mai sus, va trebui să redenumiți fișierul din ParamRectangle.FCMacro în ParamRectangle.py. Acest lucru se face simplu din file explorer, prin navigarea spre folderul Macro afișat în meniul Tools -> Macros.

Odată acesta terminată, putem scrie în consola Python.

import ParamRectangle 

Prin explorarea conținutului ParamRectangle, putem verifica dacă acesta conține clasa noastră ParametricRectangle.

Pentru a crea un obiect parametric nou folosind clasa ParametricRectangle, vom folosi următorul cod. Observați că folosim Part::FeaturePython în loc de Part::Feature pe care am folosit-o în capitolele anterioare (versiunea Python ne permite să definim propriul nostru comportament parametric):

myObj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython","Rectangle")
ParamRectangle.ParametricRectangle(myObj)
myObj.ViewObject.Proxy = 0 # this is mandatory unless we code the ViewProvider too
FreeCAD.ActiveDocument.recompute()

Nimic nu va apărea pe ecran încă, deoarece proprietățile Lungime și Lățime sunt 0, ceea ce va declanșa condiția \"Do-nothing\" în interiorul execuției. Trebuie doar să schimbăm valorile Lungimii și Lățimii și obiectul nostru va apărea în mod magic și va fi recalculat din zbor.

Desigur, ar fi obositor să trebuiască să tastați aceste 4 linii de cod Python de fiecare dată când dorim să creăm un nou dreptunghi parametric. O modalitate foarte simplă de a rezolva aceasta este plasarea celor 4 linii de mai sus în fișierul ParamRectangle.py, la final, după terminarea clasei ParametricRectange (putem face acest lucru din editorul Macro).

Acum, când introducem import ParamRectangle, se va crea automat un nou dreptunghi parametric. Chiar mai bine, putem adăuga un buton al barei de instrumente care va face exact așa:

-   Deschideți meniul **Tools -\> Customize**
-   Sub tab-ul \"Macros\", selectați macroul nostru ParamRectangle.py, completați detaliile după cum doriți și apăsați pe \"Add\":

![](images/Exercise_python_04.jpg )

-   Sub tab-ul Toolbars, creați o nouă bara de instrumente personalizată într-un atelierul de lucru la alegere dvs (sau la modul general), selectați macro-ul și adăugați-l în bara de instrumente:

![](images/Exercise_python_05.jpg )

-   Asta este, acum avem un nou buton al barei de instrumente care, atunci când se face clic, va crea un dreptunghi parametric.

Rețineți că, dacă doriți să distribuiți fișiere create cu acest nou instrument altor persoane, trebuie să aibă și macrocomanda ParamRectangle.py instalat pe computerul lor.

**De citit în plus**

-   [The FreeCAD macros repository](Macros_recipes.md)
-   [Parametric object example](Scripted_objects.md)
-   [More examples in the FreeCAD code](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/TemplatePyMod/FeaturePython.py)





{{Powerdocnavi

}} 

_ _

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Manual:Creating parametric objects/ro
