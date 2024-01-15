# Wrapping a Cplusplus class in Python/pl
**Ten artykuł to jedynie zalążek. Prosimy o uzupełnienie wiedzy!**






## Kontekst

FreeCAD używa niestandardowego systemu opartego na XML do tworzenia opakowania Pythona dla klasy C++. Aby opakować klasę C++ do użytku w środowisku Python, należy ręcznie utworzyć dwa pliki, a dwa pliki są automatycznie generowane przez system kompilacji CMake *(oprócz plików nagłówkowych i implementacyjnych C++ dla klasy)*.

Musisz utworzyć:

-    `[YourClass]Py.xml`
    

-    `[YourClass]PyImp.cpp`.

Edytuj odpowiedni plik **CMakeLists.txt**, aby dodać odniesienia do tych dwóch plików. Z pliku XML system kompilacji utworzy następnie:

-    `[YourClass]Py.cpp`
    

-    `[YourClass]Py.h`.



## Opis klasy Plik XML 

Plik XML `[YourClass]Py.xml` zawiera informacje o funkcjach i atrybutach, które implementuje klasa Python, a także dokumentację użytkownika dla tych elementów, która wyświetla się w [konsoli FreeCAD](Python_console/pl.md).

W tym przykładzie przyjrzymy się wrapperowi dla klasy Axis C++. Plik opisu XML zaczyna się od:


{{Code|lang=xml|code=
<?xml version="1.0" encoding="UTF-8"?>
<GenerateModel xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="generateMetaModel_Module.xsd">
    <PythonExport
        Father="PyObjectBase"
        Name="AxisPy"
        Twin="Axis"
        TwinPointer="Axis"
        Include="Base/Axis.h"
        FatherInclude="Base/PyObjectBase.h"
        Namespace="Base"
        Constructor="true"
        Delete="true"
        FatherNamespace="Base">
    <Documentation>
        <Author Licence="LGPL" Name="Juergen Riegel" EMail="FreeCAD@juergen-riegel.net" />
        <UserDocu>User documentation here
          
        </UserDocu>
        <DeveloperDocu>Developer documentation here</DeveloperDocu>
    </Documentation>
}}

Po tej preambule podana jest lista metod i atrybutów. Format metody jest następujący:


{{Code|lang=xml|code=
<Methode Name="move">
    <Documentation>
        <UserDocu>
        move(Vector)
        Move the axis base along the vector
        </UserDocu>
    </Documentation>
</Methode>
}}

Format atrybutu jest następujący:


{{Code|lang=xml|code=
<Attribute Name="Direction" ReadOnly="false">
    <Documentation>
        <UserDocu>Direction vector of the Axis</UserDocu>
    </Documentation>
    <Parameter Name="Direction" Type="Object" />
</Attribute>
}}

W przypadku atrybutu, jeśli \"ReadOnly\" ma wartość false, należy podać zarówno funkcję pobierającą, jak i ustawiającą. Jeśli natomiast ma wartość true, dozwolona jest tylko funkcja getter. W tym przypadku będziemy musieli dostarczyć dwie funkcje w pliku implementacji C++:


{{Code|lang=cpp|code=
Py::Object AxisPy::getDirection(void) const
}}

oraz:


{{Code|lang=cpp|code=
void AxisPy::setDirection(Py::Object arg)
}}



## Implementacja pliku Cplusplus 

Plik implementacji C++ `[YourClass]PyImp.cpp` zapewnia \"klej\", który łączy ze sobą struktury C++ i Python, skutecznie tłumacząc z jednego języka na drugi. System FreeCAD C++-to-Python zapewnia szereg klas C++, które mapują się na odpowiadające im typy Pythona. Najbardziej podstawową z nich jest klasa `Py::Object` - rzadko tworzona bezpośrednio, klasa ta stanowi podstawę drzewa dziedziczenia i jest używana jako typ zwracany dla każdej funkcji zwracającej dane z języka Python.



### Dołączanie plików 

Twój plik implementacyjny C++ będzie zawierać następujące pliki:


{{Code|lang=cpp|code=
#include "PreCompiled.h"

#include "[YourClass].h"

// Inclusion of the generated files (generated out of [YourClass]Py.xml)
#include "[YourClass]Py.h"
#include "[YourClass]Py.cpp"
}}

Oczywiście można dołączyć wszelkie inne nagłówki C++, których kod wymaga do działania.



### Konstruktor

Twoja implementacja C++ musi zawierać definicję funkcji PyInit: na przykład dla wrappera klasy Axis jest to:


{{Code|lang=cpp|code=
int AxisPy::PyInit(PyObject* args, PyObject* /*kwd*/)
}}

W ramach tej funkcji najprawdopodobniej będziesz musiał przeanalizować argumenty przychodzące do konstruktora: najważniejszą funkcją do tego celu jest dostarczona przez środowisko Python `PyArg_ParseTuple`. Przyjmuje ona przekazaną listę argumentów, deskryptor oczekiwanych argumentów, które powinna przeanalizować, oraz informacje o typie i lokalizacje przechowywania przeanalizowanych wyników. Na przykład:


{{Code|lang=cpp|code=
    PyObject* d;
    if (PyArg_ParseTuple(args, "O!O", &(Base::VectorPy::Type), &o,
                                      &(Base::VectorPy::Type), &d)) {
        // NOTE: The first parameter defines the base (origin) and the second the direction.
        *getAxisPtr() = Base::Axis(static_cast<Base::VectorPy*>(o)->value(),
                                   static_cast<Base::VectorPy*>(d)->value());
        return 0;
    }
}}

Pełna lista specyfikatorów formatu znajduje się na stronie [dokumentacja Python C API](https://docs.python.org/3/c-api/arg.html). Należy pamiętać, że zdefiniowano również kilka powiązanych funkcji, które pozwalają na użycie słów kluczowych itp. Kompletny zestaw to:


{{Code|lang=cpp|code=
PyAPI_FUNC(int) PyArg_Parse (PyObject *, const char *, ...);
PyAPI_FUNC(int) PyArg_ParseTuple (PyObject *, const char *, ...);
PyAPI_FUNC(int) PyArg_ParseTupleAndKeywords (PyObject *, PyObject *, const char *, char **, ...);
PyAPI_FUNC(int) PyArg_VaParse (PyObject *, const char *, va_list);
PyAPI_FUNC(int) PyArg_VaParseTupleAndKeywords (PyObject *, PyObject *, const char *, char **, va_list);
}}



## Odnośniki internetowe 

-   [Udostępnianie Cplusplus w środowisku Python](Exposing_Cplusplus_to_Python.md)
-   [Commit 20b86e5, eksponujący precyzyjne metody OCC w środowisku Python](https://github.com/FreeCAD/FreeCAD/commit/20b86e55b8dd1873f4c19e036d047528c9ff7f4e).



---
⏵ [documentation index](../README.md) > [Developer](Category_Developer.md) > [Developer Documentation](Category_Developer Documentation.md) > Wrapping a Cplusplus class in Python/pl
