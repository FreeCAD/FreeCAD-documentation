

## Description


{{TOCright}}

[IFC++](IfcPlusPlus/fr.md) ou [IfcPlusPlus](IfcPlusPlus/fr.md) est une bibliothèque C++ open source (licence MIT) du projet [IfcQuery](IfcPlusPlus/fr.md) pour la lecture, l\'écriture et la visualisation de fichiers [IFC](Arch_IFC/fr.md) .

La bibliothèque IFC++ peut être utilisée à des fins générales et comprend également un exemple d\'application de visualisation IFC. Cette visionneuse est basée sur Qt 5 et OpenSceneGraph (OSG) et peut charger de gros fichiers IFC très rapidement. Elle peut donc être utilisée pour comparer les performances d\'autres visionneuses IFC, comme Blender et FreeCAD, qui utilisent en interne la bibliothèque [IfcOpenShell](IfcOpenShell/fr.md).

<img alt="" src=images/IfcQuery_viewer_example.png  style="width:600px;">


*L'exemple de visionneuse IFC inclus dans la distribution source des bibliothèques IfcQuery/IFC ++.*


**Remarque:**

dans l\'usage courant, les noms \"IfcQuery\", \"IFC++\" et \"IfcPlusPlus\" peuvent être utilisés de manière interchangeable pour désigner la même chose, la bibliothèque C++, ou plus spécifiquement le visualiseur IFC gratuit.

## Installation

La distribution IFC++ est fournie sous forme de code source, donc pour utiliser la bibliothèque et le visualiseur, le code doit être compilé.

IFC ++ est développé principalement sur une plate-forme Windows aussi il inclut des fichiers solution (`.snl`) et projet (`.vcxproj`) pour compiler la bibliothèque dynamique `IfcPlusPlus.dll` à l\'aide de Visual Studio. Une bibliothèque statique `libIfcPlusPlus.a` peut également être produite pour Linux en utilisant CMake.


**Remarque:**

il existe un visualiseur plus complet qui utilise des bibliothèques IFC++ précompilées destinées à Windows. Cette visionneuse est gratuite mais n\'est pas open source. Il est disponible en téléchargeant le package `SimpleViewerExampleQt.zip` depuis {{URL|http://www.ifcquery.com/}} et en exécutant `SimpleViewerExampleQt.exe`. Ce visualiseur est autonome, tout ce dont il a besoin pour s\'exécuter est inclus dans l\'archive `.zip`.

## Compilation sous Windows {#compilation_sous_windows}

Suivez les instructions du dépôt officiel [ifcplusplus](https://github.com/ifcquery/ifcplusplus).

## Compilation sous Linux {#compilation_sous_linux}

Les instructions générales sont les suivantes:

1.  Récupérez le code source d\'IFC ++ depuis son dépôt principal.
2.  Rassemblez toutes les dépendances pour la compilation, y compris un compilateur C++, CMake et Make, et les fichiers de développement pour Boost, Qt 5, ainsi que la bibliothèque OpenSceneGraph (OSG) pour la visualisation.
3.  Exécutez `cmake` pour générer un `Makefile`, puis démarrez la compilation en exécutant `make`.
4.  Installez les bibliothèques `libIfcPlusPlus.a` et `libcarve.so` dans le chemin de bibliothèque approprié afin qu\'elles soient trouvées par le visualiseur d\'exemples IFC++.

### Prérequis

Dans une distribution basée sur Debian/Ubuntu, obtenir les fichiers de développement requis est généralement simple. 
```python
sudo apt install git cmake gcc g++ libboost-all-dev
sudo apt install qt5-qmake qtbase5-dev qttools5-dev libqt5widgets5 libqt5opengl5-dev
```

Obtenez le code source du projet et placez-le dans un répertoire personnalisé auquel vous avez un accès en écriture complet. 
```python
git clone https://github.com/ifcquery/ifcplusplus ifcplusplus-source
```

### OpenSceneGraph

[OpenSceneGraph](http://www.openscenegraph.org/) (OSG) est une collection de bibliothèques C++ qui utilise OpenGL pour la visualisation 3D. Elle il peut être utilisée dans les jeux, la réalité virtuelle, la visualisation scientifique et la modélisation.


```python
sudo apt install libopenscenegraph-3.4-dev
```

Si les fichiers sont trop anciens dans votre distribution, vous pouvez également compiler les bibliothèques vous-même. La procédure est décrite dans le dépôt principal, [openscenegraph/OpenSceneGraph](https://github.com/openscenegraph/OpenSceneGraph). La compilation est simple, bien que vous puissiez avoir besoin de diverses dépendances telles que Qt 5, Freetype, Inventor, OpenEXR, COLLADA, ZLIB, GDAL, FFmpeg, Gstreamer, SDL, Cairo et Poppler.


```python
git clone https://github.com/openscenegraph/OpenSceneGraph OpenSceneGraph-source

mkdir -p OpenSceneGraph-build
cd OpenSceneGraph-build
cmake ../OpenSceneGraph-source

make -j 3
sudo make install
```

### Carve

Carve est une bibliothèque C++ [Géométrie Solide Constructive](constructive_solid_geometry/fr.md) (CSG) conçue pour effectuer des opérations booléennes entre deux maillages polygonaux arbitraires. Avec la bibliothèque IFC++, `libIfcPlusPlus.a`, Carve est utilisé par le visualiseur d\'exemples IFC++ pour ouvrir et afficher les fichiers IFC.

-   Dépôt d\'origine: [carve](https://code.google.com/archive/p/carve/), GPL2, de 2009 à 2011.
-   Nouveau dépôt: [folded / carve](https://github.com/folded/carve), à partir de 2011; le projet est passé à la licence MIT à partir d\'octobre 2015.

Le projet étant désormais sous licence MIT, des copies des fichiers source Carve sont désormais incluses dans le référentiel IFC++. Cela signifie que lors de la compilation IFC++, `libcarve.so` sera également compilé. Cette bibliothèque doit être disponible dans le système pour que la visionneuse d\'exemples IFC++ fonctionne correctement.

### Configuration de CMake {#configuration_de_cmake}

Il est recommandé d\'effectuer la configuration et la compilation dans un répertoire build spécifique séparé du répertoire source.


```python
mkdir -p ifcplusplus-build
cd ifcplusplus-build

cmake ../ifcplusplus-source/
```

Par défaut, le type de compilation est `Release` mais il peut également être défini sur `Debug`. 
```python
cmake -DCMAKE_BUILD_TYPE=Debug ../ifcplusplus-source/
```

### Compilation réelle {#compilation_réelle}

S\'il n\'y avait pas de message d\'erreur lors de la configuration avec CMake, un `Makefile` aurait dû être créé dans le répertoire build, vous pouvez donc procéder à la compilation des bibliothèques en exécutant `make`.


```python
make -j N
```


`N`

est le nombre de processeurs que vous attribuez au processus de compilation; choisissez au moins un de moins que le nombre total de cœurs de processeur dont vous disposez.

### Test de la compilation dans le répertoire build {#test_de_la_compilation_dans_le_répertoire_build}

Si la compilation réussit, vous devriez avoir un sous-répertoire `Release/` avec les bibliothèques nouvellement compilées. 
```python
Release/libcarve.so
Release/libIfcPlusPlus.a
Release/SimpleViewerExample
```

Vous pouvez lancer l\'exécutable `SimpleViewerExample` avec un fichier [IFC](Arch_IFC/fr.md) comme entrée. 
```python
Release/SimpleViewerExample IfcOpenHouse.ifc
```

Si le type de build a été défini sur `Debug`, alors les bibliothèques compilées apparaîtront dans le sous-répertoire `Debug/` à la place.

### Installation des bibliothèques compilées {#installation_des_bibliothèques_compilées}

Si la compilation ne signale aucune erreur, vous pouvez exécuter `make install` pour copier les en-têtes, les bibliothèques compilées et les binaires dans leurs répertoires d\'installation correspondants. 
```python
sudo make install
```

Par défaut, `CMAKE_INSTALL_PREFIX` est `/usr/local/`, donc tous les fichiers compilés seront mis sous ce répertoire, qui nécessite normalement des privilèges élevés. {{Code|lang=sh|code=
/usr/local/bin/SimpleViewerExample
/usr/local/lib/libcarve.so
/usr/local/lib/libIfcPlusPlus.a
/usr/local/include/carve/*.{h, hpp}
/usr/local/include/ifcpp/geometry/*.h
/usr/local/include/ifcpp/geometry/Carve/*.h
/usr/local/include/ifcpp/geometry/OCC/*.h
/usr/local/include/ifcpp/IFC4/*.h
/usr/local/include/ifcpp/IFC4/include/*.h
/usr/local/include/ifcpp/model/*.h
/usr/local/include/ifcpp/reader/*.h
/usr/local/include/ifcpp/writer/*.h
/usr/local/share/IFCPP/cmake/*.cmake
}}

### Chemin de la bibliothèque {#chemin_de_la_bibliothèque}

Une fois `SimpleViewerExample` placé dans `/usr/local/bin`, l\'exécutable sera disponible dans tout le système. Cependant, sur certaines plates-formes, `libcarve.so` peut ne pas être trouvé s\'il est installé dans le répertoire par défaut `/usr/local/lib`. {{Code|lang=md|code=
SimpleViewerExample: error while loading shared libraries: libcarve.so: cannot open shared object file: No such file or directory
}}

Si tel est le cas, il peut suffire de mettre à jour le cache du chargeur de bibliothèque `ld.so` en appelant `ldconfig`: 
```python
sudo ldconfig
```

Ou vous devrez peut-être d\'abord déplacer la bibliothèque vers le bon répertoire: 
```python
sudo mkdir -p /usr/local/lib/x86_64-linux-gnu/
sudo mv /usr/local/lib/libcarve.so /usr/local/lib/x86_64-linux-gnu/libcarve.so
sudo ldconfig
```

Vous pouvez également définir la variable `LD_LIBRARY_PATH` sur le répertoire contenant `libcarve.so`, avant de lancer l\'exécutable: 
```python
LD_LIBRARY_PATH=/usr/local/lib SimpleViewerExample
```

Pour rendre cet effet persistant, cette variable d\'environnement peut être définie dans le fichier de ressources du shell, par exemple, `.bashrc`, afin qu\'elle soit propagée à toutes les instances de terminal au démarrage: 
```python
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
```

### Suppression des bibliothèques compilées {#suppression_des_bibliothèques_compilées}

Pour supprimer les bibliothèques installées, supprimez simplement les fichiers correspondants qui ont été installés. {{Code|lang=sh|code=
sudo rm -rf /usr/local/bin/SimpleViewerExample
sudo rm -rf /usr/local/lib/libcarve.so
sudo rm -rf /usr/local/lib/libIfcPlusPlus.a
sudo rm -rf /usr/local/include/carve
sudo rm -rf /usr/local/include/ifcpp
sudo rm -rf /usr/local/share/IFCPP/cmake/
}}

## Corrections pour Linux {#corrections_pour_linux}

La bibliothèque IFC++ est développée par son auteur sur un système Windows. Cela signifie que même si le code dépend de bibliothèques multiplateformes telles que Boost, Qt et OpenSceneGraph, le code est principalement testé pour être compilé et exécuté sous Windows. Néanmoins, au fil des ans, d\'autres développeurs ont fourni des correctifs au projet afin que IFC++ puisse être compilé et exécuté sur des distributions Linux.

En particulier, un fork du projet principal est maintenu avec de petits correctifs pour mieux compiler et mieux fonctionner dans Debian.

-   [berndhahnebach/ifcplusplus](https://github.com/berndhahnebach/ifcplusplus/)

Si le code du dépôt officiel ne fonctionne pas ou semble avoir des problèmes sous Linux, essayez de suivre les mêmes instructions de compilation mais en utilisant les sources de ce dépôt alternatif. Ce dépôt contient souvent des commits derrière la distribution principale, mais il vise à rester à jour et en même temps à fournir des correctifs spécifiques à Linux. Ces améliorations sont normalement renvoyées au dépôt principal afin de permettre à la branche officielle de se compiler sous Linux sans problème.

Le développeur principal d\'IFC++ ne prend pas en charge Linux directement, les développeurs Linux doivent donc être prêts à résoudre les problèmes et à soumettre des correctifs lors de l\'utilisation d\'IFC++ sous Linux.

### Icônes invisibles {#icônes_invisibles}

Pour `SimpleViewerExample`, il y a deux boutons dans l\'interface principale qui sont invisibles si la feuille de style personnalisée n\'est pas trouvée. {{Code|lang=cpp|code=
QIODevice::read (QFile, ":styles.css"): device not open
}}

Le style doit être inclus dans la configuration de CMake dans la section consacrée aux bibliothèques Qt: {{Code|lang=cmake|code=
# ifcplusplus-source/examples/SimpleViewerExampleQt/CMakeLists.txt
...
ADD_DEFINITIONS(${Qt5Widgets_DEFINITIONS})

SET(viewer_dir ${IFCPP_SOURCE_DIR}/examples/SimpleViewerExampleQt)
SET(RESOURCES ${viewer_dir}/Resources/ifcplusplus.qrc)
QT5_ADD_RESOURCES(SimpleViewerExample_RESOURCES_RCC ${RESOURCES})
}}

## Plus d\'informations {#plus_dinformations}

-   [projet IFC++](https://www.ifcquery.com/)
-   [ifcquery/ifcplusplus](https://github.com/ifcquery/ifcplusplus) dépôt
-   Dépôt alternatif, en particulier pour Debian: [berndhahnebach/ifcplusplus](https://github.com/berndhahnebach/ifcplusplus/)
-   Fil du forum: [IFC Viewer ifcplusplus](https://forum.freecadweb.org/viewtopic.php?f=39&t=5101) (2013 to 2020)
-   [IfcPlusPlus compilé sur Gentoo - questions et alternatives?](https://forum.freecadweb.org/viewtopic.php?f=39&t=33254)
-   Fil allemand: [IfcQuery / IfcPlusPlus selber kompilieren](https://forum.freecadweb.org/viewtopic.php?f=13&t=48648)


 {{FEM Tools navi}}  
