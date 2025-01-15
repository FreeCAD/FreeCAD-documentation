# Manual:Creating parametric objects/ro
{{Manual:TOC}}


<div class="mw-translate-fuzzy">

În [previous chapter](Manual_Creating_and_manipulating_geometry.md), Am văzut cum este creată geometrie Pieselor și cum este afișată aceasta pe ecran, atașând-o la un documente obeict \"dumb\" (non-parametric). Acest lucru este obositor când vrem să schimbăm forma acestui obiect. Va trebui să creăm o nouă formă, apoi să o atribuim din nou obiectului nostru.


</div>


<div class="mw-translate-fuzzy">

Cu toate acestea, am văzut, de asemenea, în toate capitolele anterioare ale acestui manual cât de puternice sunt obiectele parametrice. Trebuie doar să schimbăm o proprietate, iar forma se recalculează în timp real.


</div>


<div class="mw-translate-fuzzy">

Pe plan intern, obiectele parametrice nu fac nimic diferit de ceea ce am făcut: ele recalculează conținutul proprietății Shape, în mod repetat, de fiecare dată când o altă proprietate a fost modificată.


</div>

-   Declares the necessary properties for the object.
-   Defines the behavior when any of these properties are modified.

The structure of such a parametric object is as simple as this:


```python
class myParametricObject:

    def __init__(self, obj):
        obj.Proxy = self
        obj.addProperty("App::PropertyFloat", "MyLength")
        ...

    def execute(self,obj):
        print ("Recalculating the shape...")
        print ("The value of MyLength is:")
        print (obj.MyLength)
        ...
```


<div class="mw-translate-fuzzy">

FreeCAD oferă un sistem foarte convenabil pentru crearea a unor astfel de obiecte parametrice complet în în Python. Ele constau dintr-o clasă Python simplă, care definește toate proprietățile de care are nevoie obiectul și ce se va întâmpla când se schimbă una dintre aceste proprietăți. Structura obiectului parametric este la fel de simplă:


</div>

-   Store the class itself in the **Proxy** attribute of the FreeCAD document object:

By assigning **self** to the **Proxy** attribute of the FreeCAD document object, we link the logic of our Python class to the FreeCAD object. This means the document object will \"carry\" the Python class code inside itself, allowing it to behave according to the logic defined in the class. This connection enables FreeCAD to know how to interact with and recalculate the parametric object.

-   Create all the properties the object needs:

Using the **addProperty** method, we define the custom properties required by the object. Properties act as parameters or variables for the object and can be accessed, modified, and displayed in FreeCAD\'s property editor. In the example, we add a floating-point property named **MyLength**. This property will later influence the shape or behavior of the object.

class myParametricObject:

  def __init__(self,obj):
    obj.Proxy = self
    obj.addProperty("App::PropertyFloat","MyLength")
    ...
       
  def execute(self,obj):
    print ("Recalculating the shape...")
    print ("The value of MyLength is:")
    print (obj.MyLength)
    ...


```python
FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "dummy").supportedProperties()
```


<div class="mw-translate-fuzzy">

Toate clasele Python au de obicei o metodă \_\_init\_\_. Ceea ce este în interiorul acestei metode este executat atunci când clasa este instanțiată (ceea ce înseamnă că, în argoul de programare, că un obiect Python este creat din această clasă. Înțelegem o clasă ca pe un \"șablon\" pentru crearea de copii în direct ale acestui șablon). Aici, în funcția noastră de inițializare (funcția \_\_init\_\_), facem două lucruri importante: 1 - pentru a stoca clasa însăși în atributul \"Proxy\" al obiectului în documentul nostru FreeCAD, adică documentul obiect FreeCAD va purta acest cod în sine și 2 - va crea toate proprietățile pe care le are obiectul nostru. Există multe tipuri de proprietăți disponibile, puteți obține lista completă introducând acest cod:


</div>

FreeCAD.ActiveDocument.addObject(\"Part::FeaturePython\",\"dummy\").supportedProperties()

-   The **execute** method is called whenever the object needs to be updated.
-   It is responsible for recalculating the shape and assigning it to the object\'s **Shape** attribute.
-   The **obj** argument gives access to the FreeCAD document object, enabling you to make changes programmatically.

With this system, FreeCAD handles the rest---ensuring that the object is properly updated in the document and displayed correctly in the graphical interface.


<div class="mw-translate-fuzzy">

Apoi, a doua parte importantă este metoda de executare. Orice cod din această metodă va fi executat atunci când obiectul este marcat pentru a fi recalculat, ceea ce se va întâmpla când o proprietate a fost schimbată. Acesta este tot ceea ce este de făcut. În interiorul execuției, trebuie să faceți tot ce trebuie făcut, adică să calculați o nouă formă și să atribuiți obiectului în sine ceva asemănător cu obj.Shape = myNewShape. Acesta este motivul pentru care metoda execută ia un argument \"obj\", care va fi obiectul documentului FreeCAD în sine, astfel încât să îl putem manipula în codul nostru python.


</div>


<div class="mw-translate-fuzzy">

Un ultim lucru este important de reținut: Când creați astfel de obiecte parametrice într-un document FreeCAD, atunci când salvați fișierul, codul python de mai sus nu este stocat în interiorul fișierului. Din motive de securitate, dacă un fișier FreeCAD conține cod, ar fi posibil ca cineva să distribuie fișiere FreeCAD care conțin cod malitios care ar putea dăuna computerelor altor persoane. Deci, dacă distribuiți un fișier care conține obiecte făcute cu codul de mai sus, un astfel de cod trebuie să fie prezent și pe computerul care va deschide fișierul. Cea mai ușoară modalitate de a realiza acest lucru este de a salva codul de mai sus într-o macrocomandă și de a distribui macro-ul împreună cu fișierul FreeCAD sau de a vă distribui macrocomanda în depozitul de macrocomanzi a FreeCAD [ FreeCAD repository](Macros_recipes.md) de unde oricine îl poate descărca.


</div>

Mai jos, vom face un exercițiu mic, construind un obiect parametric care este o simplă fațetă parametrică dreptunghiulară. Exemple mai complexe sunt disponibile pe [parametric object example](Scripted_objects.md) și în chiar însuși [FreeCAD source code](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/TemplatePyMod/FeaturePython.py) .


<div class="mw-translate-fuzzy">

Vom da obiectului nostru două proprietăți: lungimea și lățimea, pe care le vom folosi pentru a construi un dreptunghi. Apoi, deoarece obiectul nostru va avea deja o proprietate de plasament predefinită (orice obiect geometric are una implicită, nu este nevoie să-l adăugăm noi înșine), vom deplasa dreptunghiul nostru la locația / orientarea setată în Placement, astfel încât utilizatorul să poată muta dreptunghiul oriunde editând proprietatea de plasare.


</div>


```python
class ParametricRectangle:

    def __init__(self,obj):
        obj.Proxy = self
        obj.addProperty("App::PropertyFloat", "Length")
        obj.addProperty("App::PropertyFloat", "Width")

    def execute(self, obj):
        # We need to import the FreeCAD module here too, because we might be running out of the Console
        # (in a macro, for example) where the FreeCAD module has not been imported automatically:
        import FreeCAD
        import Part

        # First we need to make sure the values of Length and Width are not 0
        # otherwise Part.LineSegment will complain that both points are equal:
        if (obj.Length == 0) or (obj.Width == 0):
            # If yes, exit this method without doing anything:
            return

        # We create 4 points for the 4 corners:
        v1 = FreeCAD.Vector(0, 0, 0)
        v2 = FreeCAD.Vector(obj.Length, 0, 0)
        v3 = FreeCAD.Vector(obj.Length,obj.Width, 0)
        v4 = FreeCAD.Vector(0, obj.Width, 0)

        # We create 4 edges:
        e1 = Part.LineSegment(v1, v2).toShape()
        e2 = Part.LineSegment(v2, v3).toShape()
        e3 = Part.LineSegment(v3, v4).toShape()
        e4 = Part.LineSegment(v4, v1).toShape()

        # We create a wire:
        w = Part.Wire([e1, e2, e3, e4])

        # We create a face:
        f = Part.Face(w)

        # All shapes have a Placement too. We give our shape the value of the placement
        # set by the user. This will move/rotate the face automatically.
        f.Placement = obj.Placement

        # All done, we can attribute our shape to the object!
        obj.Shape = f
```


<div class="mw-translate-fuzzy">

În loc să lipiți (dela copy&paste) codul de mai sus în consolă Python, ar trebui să îl salvăm undeva, așa că îl putem reutiliza și modifica mai târziu. De exemplu într-o macrocomandă nouă (meniul Tools -> Macros -> Create). Denumiți-o, de exemplu, "ParamRectangle". Cu toate acestea, macrocomenzile FreeCAD sunt salvate cu o extensie .FCMro, pe care Python nu o recunoaște la import. Deci, înainte de a utiliza codul de mai sus, va trebui să redenumiți fișierul din ParamRectangle.FCMacro în ParamRectangle.py. Acest lucru se face simplu din file explorer, prin navigarea spre folderul Macro afișat în meniul Tools -> Macros.


</div>

Odată acesta terminată, putem scrie în consola Python.


```python
import ParamRectangle
```

Prin explorarea conținutului ParamRectangle, putem verifica dacă acesta conține clasa noastră ParametricRectangle.


<div class="mw-translate-fuzzy">

Pentru a crea un obiect parametric nou folosind clasa ParametricRectangle, vom folosi următorul cod. Observați că folosim Part::FeaturePython în loc de Part::Feature pe care am folosit-o în capitolele anterioare (versiunea Python ne permite să definim propriul nostru comportament parametric):


</div>


```python
myObj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "Rectangle")
ParamRectangle.ParametricRectangle(myObj)
myObj.ViewObject.Proxy = 0 # This is mandatory unless we code the ViewProvider too.
FreeCAD.ActiveDocument.recompute()
```

myObj = FreeCAD.ActiveDocument.addObject(\"Part::FeaturePython\",\"Rectangle\")

ParamRectangle.ParametricRectangle(myObj)
myObj.ViewObject.Proxy = 0 # this is mandatory unless we code the ViewProvider too
FreeCAD.ActiveDocument.recompute()

-   **myObj = FreeCAD.ActiveDocument.addObject(\"Part::FeaturePython\", \"Rectangle\")**: Creates a new **Part::FeaturePython** object named **Rectangle** in the active FreeCAD document. This object is specifically designed for custom parametric behavior, allowing Python-defined logic to manage its properties and behavior.

-   **ParamRectangle.ParametricRectangle(myObj)**: Initializes the object by associating it with the **ParametricRectangle** class from the **ParamRectangle** module or script. This links the custom Python-defined logic to the object, enabling it to act as a parametric object.

-   **myObj.ViewObject.Proxy = 0**: Resets the **ViewObject.Proxy** attribute to 0, ensuring that the object uses FreeCAD's default view handling. This step is required unless you define a custom ViewProvider to manage the visual representation of the object.

-   **FreeCAD.ActiveDocument.recompute()**: Recomputes the document to update the geometry and reflect changes in the FreeCAD graphical interface, making the new object fully visible and functional


<div class="mw-translate-fuzzy">

Nimic nu va apărea pe ecran încă, deoarece proprietățile Lungime și Lățime sunt 0, ceea ce va declanșa condiția \"Do-nothing\" în interiorul execuției. Trebuie doar să schimbăm valorile Lungimii și Lățimii și obiectul nostru va apărea în mod magic și va fi recalculat din zbor.


</div>


<div class="mw-translate-fuzzy">

Desigur, ar fi obositor să trebuiască să tastați aceste 4 linii de cod Python de fiecare dată când dorim să creăm un nou dreptunghi parametric. O modalitate foarte simplă de a rezolva aceasta este plasarea celor 4 linii de mai sus în fișierul ParamRectangle.py, la final, după terminarea clasei ParametricRectange (putem face acest lucru din editorul Macro).


</div>


<div class="mw-translate-fuzzy">

Acum, când introducem import ParamRectangle, se va crea automat un nou dreptunghi parametric. Chiar mai bine, putem adăuga un buton al barei de instrumente care va face exact așa:


</div>


<div class="mw-translate-fuzzy">

-   Deschideți meniul **Tools -\> Customize**
-   Sub tab-ul \"Macros\", selectați macroul nostru ParamRectangle.py, completați detaliile după cum doriți și apăsați pe \"Add\":

![](images/Exercise_python_04.jpg )


</div>

![](images/FreeCAD_python_macroRec.png )

-   Sub tab-ul Toolbars, creați o nouă bara de instrumente personalizată într-un atelierul de lucru la alegere dvs (sau la modul general), selectați macro-ul și adăugați-l în bara de instrumente:

![](images/FreeCAD_python_toolbarCus.png )

-   Asta este, acum avem un nou buton al barei de instrumente care, atunci când se face clic, va crea un dreptunghi parametric.


<div class="mw-translate-fuzzy">

Rețineți că, dacă doriți să distribuiți fișiere create cu acest nou instrument altor persoane, trebuie să aibă și macrocomanda ParamRectangle.py instalat pe computerul lor.


</div>

**De citit în plus**

-   [The FreeCAD macros repository](Macros_recipes.md)
-   [Parametric object example](Scripted_objects.md)
-   [More examples in the FreeCAD code](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/TemplatePyMod/FeaturePython.py)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Manual:Creating parametric objects/ro
