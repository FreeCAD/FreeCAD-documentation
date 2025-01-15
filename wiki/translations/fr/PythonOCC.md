# PythonOCC/fr
## Description

[PythonOCC](PythonOCC/fr.md) est un projet qui vise à fournir toute la gamme des fonctions [OpenCASCADE Technology](OpenCASCADE/fr.md) (OCCT) via le module [Python](Python/fr.md) `OCC`. C\'est une approche différente de celle de FreeCAD, où seuls certains composants d\'OCCT sont exposés via l\'[atelier Part](Part_Workbench/fr.md).

PythonOCC, d\'autre part, donne accès à toutes les classes et fonctions OCCT, ce qui est complexe mais aussi très puissant. Par conséquent, lorsque vous êtes limité par la fonctionnalité OCCT de FreeCAD, l\'utilisation de `pythonOCC` est une bonne alternative.

## Utilisation

l\'[Atelier Part](Part_Workbench/fr.md) a les méthodes `Part.__toPythonOCC__()` et `Part.__fromPythonOCC__()` pour échanger des entités `TopoDS_Shape` ([Part TopoShape](Part_TopoShape/fr.md)) vers et depuis PythonOCC. Ces méthodes nous permettent d\'utiliser toute la puissance d\'OCCT en Python, puis de remettre les formes résultantes dans des objets FreeCAD.

PythonOCC est utilisé en interne par le visualiseur [IFC](Arch_IFC/fr.md) inclus avec les bibliothèques [IfcOpenShell](IfcOpenShell/fr.md). IfcOpenShell est utilisé pour lire et écrire des documents [IFC](Arch_IFC/fr.md) avec FreeCAD. PythonOCC n\'est nécessaire que pour lancer le visualiseur intégré d\'IfcOpenShell, sinon il n\'est pas nécessaire.

## Installation

PythonOCC doit être compilé à partir des sources. Pour cela, vous devez obtenir les fichiers de développement correspondants pour [OpenCASCADE Technology](OpenCASCADE/fr.md) (OCCT) et SWIG. L\'ancienne version de PythonOCC était destinée à envelopper OCE 0.18, l\'édition communautaire d\'OCCT 6.9.x, qui n\'est plus maintenue. La dernière version de PythonOCC est désormais conçue pour fonctionner avec la récente version officielle OCCT 7.4.

Avec OCCT 7.4, PythonOCC nécessite des dépendances assez récentes comme Python 3.7, CMake 3.12 et SWIG 3.0.11. Python 2 n\'est plus pris en charge.

Il est également possible d\'installer des bibliothèques PythonOCC pré-compilées en utilisant [Conda](Conda/fr.md). Pour plus d\'informations et des instructions de compilation, consultez le dépôt du projet principal, [tpaviot/pythonocc-core](https://github.com/tpaviot/pythonocc-core).

## Compilation

Vous pouvez également compiler vous-même pythonOCC (voir [instructions](https://github.com/tpaviot/pythonocc-core/blob/master/INSTALL.md)). Voici la procédure à suivre pour Debian/Ubuntu en utilisant les paquets opencascade fournis par la distribution :

    git clone git://github.com/tpaviot/pythonocc-core.git pythonocc
    cd pythonocc
    mkdir build
    cd build
    cmake -DOCE_INCLUDE_PATH=/usr/include/opencascade -DOCE_LIB_PATH=/usr/lib/x86_64-linux-gnu ..
    make

## Plus d\'informations 

-   Page du projet: [pythonocc.org](http://www.pythonocc.org/)
-   Nouvelle version compatible avec OCCT 7.4, [tpaviot/pythonocc-core](https://github.com/tpaviot/pythonocc-core).
-   Ancienne version compatible avec OCE 0.18, l\'édition communautaire d\'OCCT 6.9.x, [tpaviot/pythonocc](https://github.com/tpaviot/pythonocc).
-   [IfcPlusPlus compilé sur Gentoo - questions et alternatives?](https://forum.freecadweb.org/viewtopic.php?f=39&t=33254)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > PythonOCC/fr
