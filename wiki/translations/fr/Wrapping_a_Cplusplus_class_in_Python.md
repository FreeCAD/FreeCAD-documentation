# Wrapping a Cplusplus class in Python/fr
**Cet article est un article en cours. Merci d'y apporter vos connaissances!**


{{TOCright}}

## Contexte

FreeCAD utilise un système personnalisé basé sur XML pour créer le wrapper Python d\'une classe C++. Pour encapsuler une classe C++ afin de l\'utiliser dans Python, deux fichiers doivent être créés manuellement, et deux fichiers sont automatiquement générés par le système de construction CMake (en plus des fichiers d\'en-tête et d\'implémentation C++ de la classe).

Vous devez créer :

-    `[YourClass]Py.xml`
    

-    `[YourClass]PyImp.cpp`
    

Editez le fichier approprié {{FileName|CMakeLists.txt}} pour ajouter des références à ces deux fichiers. A partir du fichier XML, le système de construction créera alors :

-    `[YourClass]Py.cpp`
    

-    `[YourClass]Py.h`
    

## Fichier XML de description des classes 

Le fichier XML `[YourClass]Py.xml` fournit des informations sur les fonctions et attributs que la classe Python implémente ainsi que la documentation utilisateur pour ces éléments qui s\'affiche dans la [Console Python](Python_console/fr.md) de FreeCAD.

Pour cet exemple, nous allons examiner le wrapper de la classe Axis C++. Le fichier de description XML commence par:


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
        <UserDocu>Axis
}}

Et définit une direction et une position (base) dans l\'espace 3D.

Les constructeurs suivants sont pris en charge :

-   Axis() \-- constructeur vide
-   Axis(Axis) \-- copie le constructeur
-   Axis(Base, Direction) \-- définit la position et la direction


{{Code|lang=xml|code= 
    </UserDocu>
    <DeveloperDocu>Axis</DeveloperDocu>
</Documentation>
}}

Après ce préambule, une liste de méthodes et d\'attributs est donnée. Le format d\'une méthode est le suivant :


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

Le format d\'un attribut est :


{{Code|lang=xml|code=
<Attribute Name="Direction" ReadOnly="false">
    <Documentation>
        <UserDocu>Direction vector of the Axis</UserDocu>
    </Documentation>
    <Parameter Name="Direction" Type="Object" />
</Attribute>
}}

Pour un attribut, si \"ReadOnly\" est faux, vous devez fournir une fonction getter et une fonction setter. Si elle est vraie, seule une fonction getter est autorisée. Dans ce cas, nous devrons fournir deux fonctions dans le fichier C++ d\'implémentation :


{{Code|lang=cpp|code=
Py::Object AxisPy::getDirection(void) const
}}

et :


{{Code|lang=cpp|code=
void AxisPy::setDirection(Py::Object arg)
}}

## Mise en œuvre du fichier Cplusplus 

Le fichier d\'implémentation C++ `[YourClass]PyImp.cpp` fournit la \"colle\" qui relie les structures C++ et Python ensemble, effectuant la traduction efficacement d\'un langage à l\'autre. Le système FreeCAD C++ vers Python fournit un certain nombre de classes C++ qui correspondent à leur type Python. La plus fondamentale de ces classes est la classe `Py::Object` \-- rarement créée directement, cette classe fournit la base de l\'arbre d\'héritage et est utilisée comme type de retour pour toute fonction qui retourne des données Python.

### Fichiers inclus 

Votre fichier d\'implémentation C++ comprendra les fichiers suivants :


{{Code|lang=cpp|code=
#include "PreCompiled.h"

#include "[YourClass].h"

// Inclusion of the generated files (generated out of [YourClass]Py.xml)
#include "[YourClass]Py.h"
#include "[YourClass]Py.cpp"
}}

Bien entendu, vous pouvez inclure tous les autres en-têtes C++ dont votre code a besoin pour fonctionner.

### Constructeur

Votre implémentation C++ doit contenir la définition de la fonction PyInit : par exemple, pour le wrapper de la classe Axis, c\'est


{{Code|lang=cpp|code=
int AxisPy::PyInit(PyObject* args, PyObject* /*kwd*/)
}}

Dans cette fonction, vous aurez probablement besoin d\'analyser les arguments entrants du constructeur : la fonction la plus importante à cet effet est la fonction fournie par Python `PyArg_ParseTuple`. Elle prend en compte la liste des arguments passés, un descripteur pour les arguments attendus qu\'elle doit analyser, ainsi que les informations de type et les emplacements de stockage pour les résultats analysés. Par exemple :


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

Pour une liste complète des spécificateurs de format, voir [documentation de l\'API Python C](https://docs.python.org/3/c-api/arg.html). Notez que plusieurs fonctions connexes sont également définies pour permettre l\'utilisation de mots-clés etc\... L\'ensemble complet est le suivant :


{{Code|lang=cpp|code=
PyAPI_FUNC(int) PyArg_Parse (PyObject *, const char *, ...);
PyAPI_FUNC(int) PyArg_ParseTuple (PyObject *, const char *, ...);
PyAPI_FUNC(int) PyArg_ParseTupleAndKeywords (PyObject *, PyObject *, const char *, char **, ...);
PyAPI_FUNC(int) PyArg_VaParse (PyObject *, const char *, va_list);
PyAPI_FUNC(int) PyArg_VaParseTupleAndKeywords (PyObject *, PyObject *, const char *, char **, va_list);
}}


{{Powerdocnavi

}}

[<img src="images/Property.png" style="width:16px"> Developer](Category_Developer.md) [<img src="images/Property.png" style="width:16px"> Developer Documentation](Category_Developer_Documentation.md)

---
[documentation index](../README.md) > [Developer](Category_Developer.md) > Wrapping a Cplusplus class in Python/fr
