---
- TutorialInfo:/ro
   Topic: 
   Level: 
   Time: 
   Author:[M42kus](User_M42kus.md)
   FCVersion:
   Files:
---

# Add FEM equation tutorial/ro





## Introduction

În acest tutorial vom adăuga ecuația de flux la FreeCAD și vom implementa suport pentru Elmer FEM Solver. Asigurați-vă că ați citit și ați înțeles [ Extend FEM Module](Extend_FEM_Module.md) înainte de a citi acest tutorial.

Sarcina poate fi împărțită în patru părți. Primul pas este de a face bancul de lucru FEM conștient de un nou tip de ecuație. Această etapă ar trebui efectuată numai dacă ecuația nu există în fluxul FreeCAD (spre deosebire de ecuația care există deja în FreeCAD, dar nu este suportată de solverul țintă). Al doilea pas este de a adăuga un obiect tip document concret la ecuația specifică a lui Elmer FEM Solver. Al treilea pas este să adăugăm sprijin pentru noua ecuație obiectului solver al lui Elmer. După ce analiza Elmer trebuie extinsă pentru a susține noul tip de ecuație.

## Nou tip de Equation 

In this step we are going to modify the following file:

-    {{FileName|src/Mod/Fem/femsolver/equationbase.py}}
    

The equation type is shared among all equation objects of the different solver. Each type has a string specifier (e.g. \"Heat\") and a dedicated command that adds the equation to the selected solver. This allows for a simpler GUI where we have only one button for the heat equation which is used for all supported solver.

First add the new equation to the {{Incode|equationbase.py}} module. Each equation requires two classes. A document proxy and a view proxy. Those two classes will later be used as base classes for the Elmer specific equation classes. Just copy-paste them from an existing equation type and adjust the icon path inside {{Incode|getIcon(self)}} of the view proxy.


```python
class FlowProxy(BaseProxy):
    pass

class FlowViewProxy(BaseViewProxy):
    def getIcon(self):
        return ":/icons/FEM_EquationFlow.svg"
```

## Obiectul Elmers FEM Solver Equation 

În acest pas vom modifica următoarele fișiere:

-    {{FileName|src/Mod/Fem/femsolver/elmer/equations/flow.py}}
    

și adăugați următorul fișier nou:

-    {{FileName|src/Mod/Fem/ObjectsFem.py}}
    

-    {{FileName|src/Mod/Fem/CMakeLists.txt}}
    

Să începem cu modulul care implementează obiectul documentului. In poate fi copiat dintr-o ecuație existentă. Dacă noua ecuație acceptă numai cuvintele cheie pentru sistemele liniare FemSolver/Elmer/Equations/Elasticity.py module. În cazul în care acceptă cuvinte cheie neliniare prea copiate FemSolver/Elmer/Equations/Heat.py. Ecuația de curgere este o posibilă ecuație neliniară. Aceasta înseamnă că ne vom baza munca Heat.py.

### Keywords

-   If the new equation only supports keywords for **linear** systems copy the {{Incode|femsolver/elmer/equations/elasticity.py}} module.
-   If the new equation supports keywords for both **linear** and **non-linear** systems, copy {{Incode|femsolver/elmer/equations/heat.py}}.

The flow equation in Elmer is a potentially non-linear equation. This means that we are going to base our work on {{Incode|heat.py}}.

### Editing files 

După copiere Heat.py to Flow.py adjust - argumentul de nume al funcției de creare a modulului, - atributul Type al clasei Proxy, - - clasele de bază ale proxy - ului și ale ViewProxy classes, - și proprietățile adăugate prin funcția obj.addProperty(..) de cele necesare ecuației.


```python
def create(doc, name="'''Flow'''"):
    return femutils.createObject(
        doc, name, Proxy, ViewProxy)

class Proxy(nonlinear.Proxy, equationbase.'''Flow'''Proxy):

    Type = "Fem::EquationElmer'''Flow'''"

    def __init__(self, obj):
        super(Proxy, self).__init__(obj)
        obj.Priority = 10

class ViewProxy(nonlinear.ViewProxy, equationbase.'''Flow'''ViewProxy):
    pass
```

Then you need to change the properties added via the {{Incode|obj.addProperty(..)}} function to those needed by the equation.

În momentul în care scrieți acest tutorial Consultați ecuația de elasticitate Elmer FEM Solver pentru un exemplu cu proprietăți.

Finally one has to register a **makeEquationFlow** definition in {{Incode|src/Mod/Fem/ObjectsFem.py}} by duplicating an available entry.

Nu în ultimul rând, înregistrați noul fișier modul (Flow.py) în ambele fișiere CMakeLists.txt modul descris în [Extend FEM Module](https://www.freecadweb.org/wiki/Extend_FEM_Module). Listele potrivite pot fi găsite prin căutarea fișierelor de module de ecuație existente ale lui Elmer FEM Solver.

## Extinderea Obiectului Solver 

În acest pas vom modifica următorul fișier:

-    {{FileName|src/Mod/Fem/femsolver/elmer/solver.py}}
    

Pentru moment, FreeCAD a realizat că există un nou tip de ecuație și a adăugat o comandă care adaugă această ecuație obiectului solver selectat. Am implementat, de asemenea, un obiect de ecuații concrete pentru Elmer.Ceea ce trebuie să facem acum pentru a face legătura dintre elmer și ecuația de curgere. Acesta trebuie să se facă direct în obeictul Elmer FEM solver.

Înregistrați modulul în care am introdus noul nostru obiect de ecuații (Flow.py) wcu ecuația specificată din pasul 1(\"Flow\") în lista Proxy.\_EQUATIONS în Elmer/Object.py.


```python
from .equations import electrostatic
+from .equations import flow

...

_EQUATIONS = {
    "Heat": heat,
    "Elasticity": elasticity,
+    "Flow": flow,
}
```

## Extensia Analizei Export 

În acest pas vom modifica următorul fișier:

-    {{FileName|src/Mod/Fem/femsolver/elmer/writer.py}}
    

Aceasta este cea mai pretențioasă parte a implementării unei noi ecuații. Acest fișier conține o clasă Writer care exportă analiza în format Elmer FEM Solver sif.

Pentru fiecare ecuație suportată există o serie de metode de manipulare a exportului ecuației respective. Trebuie doar să copiați toate ecuațiile existente și să le ajustați la nevoile dvs. Ecuația fluxului nostru folosește următoarele metode:

-    {{Incode|_getFlowSolver}}
    

-    {{Incode|_handleFlow}}
    

You need to register the {{Incode|_handleFlow}} method inside the {{Incode|Writer}} class:


```python
class Writer(object):
...
    def write(self):
...
        self._handleFlow()

...

```


{{Incode|_handleFlow}}

can control a series of other detailed methods. Our flow equation uses the following detailed methods:

-    {{Incode|_handleFlowConstants}}
    

-    {{Incode|_handleFlowMaterial}}
    

-    {{Incode|_handleFlowInitialVelocity}}
    

-    {{Incode|_handleFlowBndConditions}}
    

-    {{Incode|_handleFlowEquation}}
    

We now finished the function part of the new equation. Next we\'ll connect the new equation through the GUI.

## Gui tool to create an equation 

We have just created a new equation class. To access it from the FEM GUI, we need to create a button and link it to the new equation class. Here is a tutorial: [Add Button to FEM Toolbar Tutorial](Add_Button_to_FEM_Toolbar_Tutorial.md).



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > [Developer Documentation](Category_Developer Documentation.md) > Add FEM equation tutorial/ro
