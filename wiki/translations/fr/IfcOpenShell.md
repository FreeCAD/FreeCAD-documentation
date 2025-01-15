# IfcOpenShell/fr
## Description




[IfcOpenShell](IfcOpenShell/fr.md) est une bibliothèque de logiciels open source (LGPL 3) qui aide les développeurs à travailler avec les classes de base de l\'industrie [1](http://www.buildingsmart-tech.org/specifications/ifc-overview) ([Format de fichier IFC](Arch_IFC/fr.md)). Le format de fichier IFC peut être utilisé pour décrire les données de bâtiment et de construction. Le format est couramment utilisé pour la [Building Information Modeling](https://fr.wikipedia.org/wiki/Building_information_modeling) (BIM), par exemple, l\'analyse des charges mécaniques et les études d\'efficacité thermique et énergétique. IfcOpenShell est principalement une collection de bibliothèques C ++, cependant, comme elle a des liaisons [Python](Python/fr.md), elle peut être intégrée à des programmes comme FreeCAD et Blender.

IfcOpenShell utilise [OpenCASCADE](OpenCASCADE/fr.md) en interne pour convertir la géométrie implicite des fichiers IFC en une géométrie explicite que d\'autres packages de CAO peuvent comprendre, par exemple, STEP, [OBJ](Arch_OBJ/fr.md) et [DAE](Arch_DAE/fr.md).

Depuis la version 0.19, FreeCAD est capable d\'importer des fichiers IFC tant que le module `ifcopenshell` [Python](Python/fr.md) est disponible dans le système. De même, les ateliers [Arch](Arch_Workbench/fr.md) et [BIM](BIM_Workbench/fr.md) peuvent exporter un modèle de bâtiment au format IFC afin qu\'il puisse être utilisé dans d\'autres applications.

Pour vérifier que IfcOpenShell est installé sur votre système, essayez de l\'importer depuis la [console Python](Python_console/fr.md). La bibliothèque est correctement installée si aucun message d\'erreur n\'est renvoyé.


```python
import ifcopenshell
```

## Installation

IfcOpenShell peut être installé de différentes manières en fonction de votre système d\'exploitation et de votre environnement Python. Dans le passé, IfcOpenShell était un peu difficile à installer car il devait être compilé pour votre système spécifique; Cependant, au moment d\'écrire ces lignes (2020), il est plus facile de commencer à l\'utiliser, car il est maintenant inclus avec FreeCAD dans de nombreuses distributions FreeCAD. En général, il est conseillé d\'utiliser l\'une de ces distributions précompilées et de ne la compiler vous-même que si vous êtes un utilisateur avancé.



### A partir de BlenderBIM 

[BlenderBIM](https://blenderbim.org) est un autre projet qui utilise IfcOpenShell. Ils fournissent des paquets IfcOpenShell à jour pour plusieurs plateformes. C\'est la meilleure façon de s\'assurer que vous avez une version récente d\'IfcOpenShell.

Page d\'installation de BlenderBIM IfcOpenShell : <https://blenderbim.org/docs-python/ifcopenshell-python/installation.html>

### Pip

La manière la plus simple d\'installer IfcOpenShell est d\'utiliser [pip](https://pypi.org/project/pip/). Une fois que pip est installé sur votre système, vous pouvez [installer](https://datatofish.com/install-package-python-using-pip/) IfcOpenShell facilement à partir d\'une fenêtre de terminal :


```python
pip install ifcopenshell
```

### Conda

Pour les systèmes Windows et MacOS, les distributions FreeCAD associées au gestionnaire de packages [Conda](Conda.md) incluent généralement IfcOpenShell et donc aucune autre installation n\'est nécessaire. Prenez la distribution appropriée sur la page [Téléchargements](Download/fr.md).

[AppImage](AppImage/fr.md) pour Linux est également basé sur [Conda](Conda.md) et inclut également IfcOpenShell.

### Linux

S\'il est disponible, vous pouvez installer IfcOpenShell à l\'aide du gestionnaire de packages de votre distribution.


```python
sudo apt install ifcopenshell
```

Cependant, veuillez noter que les packages fournis par plusieurs dépôts Linux ont tendance à être anciens et peuvent ne pas contenir les derniers développements du logiciel. Si vous voulez être sûr que vous utilisez le logiciel le plus récent, utilisez une distribution de FreeCAD basée sur [Conda](Conda.md), une distribution IfcOpenShell précompilée, ou compilez IfcOpenShell vous-même.



### Utilisation d\'un package IfcOpenShell pré-compilé 

Il existe un dépôt spécial du projet IfcOpenShell qui compile régulièrement les bibliothèques IfcOpenShell pour différents systèmes (Linux, Windows, MacOS), architectures (32 bits et 64 bits) et versions Python (2.7, 3.x). Pour utiliser ces bibliothèques pré-compilées, vous devez choisir la bonne version qui correspond à votre système d\'exploitation, à votre architecture et aux nombres majeurs et mineurs pour le [Python](Python/fr.md) utilisé avec FreeCAD. Cela signifie que les deux premiers nombres doivent correspondre (Python 3.6 et 3.7 sont considérés comme des versions distinctes) tandis que le troisième (micro) n\'a pas d\'importance (Python 3.6.5 et 3.6.12 sont considérés comme identiques à des fins de compatibilité).

1.  Dirigez-vous vers le dépôt build [IfcOpenBot/IfcOpenShell](https://github.com/IfcOpenBot/IfcOpenShell). Ce dépôt n\'est pas destiné au développement, il ne contient qu\'une copie du dépôt principal ainsi que des packages précompilés.
2.  Au moment d\'écrire ces lignes (2020), la branche master du projet IfcOpenShell ne contient pas le dernier code, nous devons donc sélectionner la branche souhaitée, par exemple, `v0.6.0`.
3.  Cliquez sur le numéro de commit qui vous mènera à la liste des commits pour la branche, par exemple, `IfcOpenBot/IfcOpenShell/commits/v0.6.0`.
4.  Revenez dans l\'historique jusqu\'à ce que vous trouviez un commit contenant un commentaire. Cela indiquera le moment où les bibliothèques pré-compilées ont été publiées.
5.  Cliquez sur le commit. Vous verrez un commentaire d\'IfcOpenBot montrant un tableau des combinaisons de système d\'exploitation, d\'architecture et de version de Python. Choisissez le bon lien pour \"Python\" pour correspondre à votre [version de FreeCAD](Std_About/fr.md). Les packages \"Blender\", \"IfcConvert\" et \"IfcGeomServer\" ne sont pas nécessaires pour l\'utilisation de FreeCAD.
6.  Le package téléchargé doit être extrait et le répertoire extrait doit être placé dans le chemin de recherche Python afin de trouver les nouveaux modules.


**Remarque:**

les exemples suivants supposent un système basé sur Debian/Ubuntu mais la procédure générale devrait fonctionner pour d\'autres systèmes d\'exploitation.

  - La décompression du package téléchargé crée un dossier `ifcopenshell/`. 
```python
unzip ifcopenshell-python-36-v0.6.0-4baec57-linux64.zip
```

  - Le chemin de recherche peut être trouvé en inspectant la variable `sys.path` dans la [console Python](Python_console/fr.md). 
```python
import sys
print(sys.path)
```

  - Si vous souhaitez installer la bibliothèque IfcOpenShell uniquement pour vous même et ne pas affecter les répertoires système, vous devez placer le dossier extrait `ifcopenshell/` dans votre répertoire personnel d\'utilisateur. 
```python
mv -t $HOME/.local/lib/python3.6/site-packages/ ifcopenshell/
```

  - Si vous souhaitez installer la bibliothèque IfcOpenShell à l\'échelle du système, vous avez généralement besoin des privilèges de superutilisateur pour écrire dans les répertoires système; il s\'agit généralement d\'un répertoire `site-packages/` ou d\'un répertoire `dist-packages/` pour les distributions Debian/Ubuntu. 
```python
sudo mv -t /usr/local/lib/python3.6/dist-packages/ ifcopenshell/
```

Si le répertoire est correctement déplacé, vérifiez que le module `ifcopenshell` est accessible depuis la [console Python](Python_console/fr.md). 
```python
>>> import ifcopenshell
>>> print(ifcopenshell.version)
0.6.0b0
>>> print(ifcopenshell.__path__)
['/home/user/.local/lib/python3.6/site-packages/ifcopenshell']
```

Pour supprimer la bibliothèque installée, supprimez simplement le répertoire correspondant avec tous les modules à l\'intérieur. 
```python
rm -rf $HOME/.local/lib/python3.6/site-packages/ifcopenshell/
sudo rm -rf /usr/local/lib/python3.6/dist-packages/ifcopenshell/
```



### Compiler

La compilation d\'IfcOpenShell n\'est recommandée que pour les utilisateurs avancés. Le processus est similaire à [compiler FreeCAD sous Linux](Compile_on_Linux/fr.md), donc si vous l\'avez déjà fait, alors vous pouvez déjà avoir les prérequis nécessaires comme les fichiers de développement [OpenCASCADE](OpenCASCADE/fr.md). Le processus utilise l\'outil de configuration CMake pour produire un `Makefile` personnalisé à utiliser avec l\'outil Make.

Les instructions générales sont décrites dans le [dépôt IfcOpenShell](https://github.com/IfcOpenShell/IfcOpenShell) et sont les suivantes:

1.  Récupérez le code source d\'IfcOpenShell depuis son dépôt principal.
2.  Rassemblez toutes les dépendances pour la compilation, y compris un compilateur C ++, CMake et Make, et les fichiers de développement pour Boost, libxml2, [OpenCASCADE](OpenCASCADE/fr.md), SWIG, Python et OpenCOLLADA (facultatif). La plupart de ces composants sont strictement facultatifs, cependant, pour une utilisation avec FreeCAD, ils doivent tous être installés. OpenCOLLADA est facultatif car il ne fournit que le support [DAE](Arch_DAE/fr.md) du binaire `IfcConvert`.
3.  Exécutez `cmake` pour générer un `Makefile`, puis démarrez la compilation en exécutant `make`.
4.  Installez le module `ifcopenshell` [Python](Python/fr.md) dans le répertoire `site-packages/` approprié afin qu\'il soit trouvé par FreeCAD.


**Remarque:**

les exemples suivants supposent un système basé sur Debian/Ubuntu, mais la procédure générale devrait fonctionner pour d\'autres systèmes d\'exploitation. Par exemple, dans Debian, les bibliothèques partagées se trouvent normalement dans `/usr/lib/x86_64-linux-gnu/` alors que dans d\'autres distributions, cela peut être `/usr/lib64/` donc les chemins devraient être ajusté en conséquence.



### Prérequis

Installez les outils de compilation de base. 
```python
sudo apt install git cmake gcc g++ libboost-all-dev
```

Obtenez le code source du projet et placez-le dans un répertoire personnalisé auquel vous avez un accès en écriture complet.

Au moment d\'écrire ces lignes (2020), la branche principale du projet IfcOpenShell ne contient pas le dernier code, nous devons donc cloner une branche spécifique. 
```python
git clone https://github.com/IfcOpenShell/IfcOpenShell -b v0.6.0 IfcOpenShell-source
```

### OpenCASCADE

Installez les fichiers de développement de [OpenCASCADE](OpenCASCADE/fr.md). 
```python
sudo apt install libocct*-dev
```

Qui s\'étend à 
```python
sudo apt install libocct-data-exchange-dev libocct-draw-dev libocct-foundation-dev libocct-modeling-algorithms-dev libocct-modeling-data-dev libocct-ocaf-dev libocct-visualization-dev
```

Vous pouvez également utiliser l\'édition communautaire (OCE) d\'OpenCASCADE, cependant, veuillez noter que cette version est ancienne et n\'est plus recommandée par FreeCAD à partir de 2020.

### OpenCOLLADA

Installez les fichiers de développement d\'OpenCOLLADA. 
```python
sudo apt install opencollada-dev
```

Si les fichiers sont trop anciens dans votre distribution, vous pouvez également compiler les bibliothèques vous-même. La procédure est décrite dans le dépôt principal, [KhronosGroup/OpenCOLLADA](https://github.com/KhronosGroup/OpenCOLLADA). Elle est très simple car elle ne nécessite que les fichiers de développement `libpcre3` et `libxml2`.


```python
sudo apt install libpcre3-dev libxml2-dev
git clone https://github.com/KhronosGroup/OpenCOLLADA OpenCOLLADA-source

mkdir -p OpenCOLLADA-build
cd OpenCOLLADA-build
cmake ../OpenCOLLADA-source

make -j 3
sudo make install
```



### Wrapper Python 

Pour une utilisation avec FreeCAD, vous avez besoin du wrapper [Python](Python/fr.md) qui utilise SWIG pour générer les interfaces appropriées à partir des classes C ++.


```python
sudo apt-get install python-all-dev swig
```



### Configuration de CMake 

Il est recommandé d\'effectuer la configuration et la compilation dans un répertoire build spécifique séparé du répertoire source.


```python
mkdir -p IfcOpenShell-build
cd IfcOpenShell-build

cmake ../IfcOpenShell-source/cmake/
```

Notez que le fichier `CMakeLists.txt` qui pilote CMake se trouve dans le sous-répertoire `cmake/` du répertoire source.

En fonction de votre distribution Linux et de la façon dont vous avez installé les dépendances, vous devrez peut-être définir certaines variables CMake afin que les bibliothèques soient trouvées correctement.



#### Spécification des bibliothèques OpenCASCADE 

Si vous avez compilé manuellement OpenCASCADE, ou si les bibliothèques ne sont pas dans un répertoire standard, vous devrez peut-être définir les variables appropriées.


```python
cmake \
    -DOCC_INCLUDE_DIR=/usr/include/opencascade \
    -DOCC_LIBRARY_DIR=/usr/lib/x86_64-linux-gnu \
    ../IfcOpenShell-source/cmake/
```

Par défaut, le système build attend l\'édition communautaire (OCE) d\'OpenCASCADE (`/usr/include/oce /`), cependant, veuillez noter que cette version est ancienne et n\'est plus recommandée par FreeCAD à partir de 2020. C\'est pourquoi l\'installation des fichiers de développement de la version principale de [OpenCASCADE](OpenCASCADE/fr.md) (OCCT) est recommandée.



#### Sans OpenCOLLADA 

Si vous n\'avez pas besoin du support OpenCOLLADA (fichiers [DAE](Arch_DAE/fr.md)), vous devez le désactiver explicitement avec la variable `COLLADA_SUPPORT`.


```python
cmake \
    ...
    -DCOLLADA_SUPPORT=FALSE \
    ../IfcOpenShell-source/cmake/
```



#### Avec OpenCOLLADA 

Si vous avez compilé manuellement OpenCOLLADA, ou si les bibliothèques ne sont pas dans un répertoire standard, vous devrez peut-être définir les variables appropriées pour OpenCOLLADA et pour la bibliothèque `libpcre`.


```python
cmake \
    ...
    -DOPENCOLLADA_INCLUDE_DIR=/usr/include/opencollada \
    -DOPENCOLLADA_LIBRARY_DIR=/usr/lib/opencollada \
    -DPCRE_LIBRARY_DIR=/usr/lib/x86_64-linux-gnu \
    ../IfcOpenShell-source/cmake/
```



#### Spécification des bibliothèques libxml2 

Si les bibliothèques `libxml2` ne sont pas trouvées pendant la compilation et la liaison, ou si les bibliothèques ne sont pas dans un répertoire standard, vous devrez peut-être définir les variables appropriées.


```python
cmake \
    ...
    -DLIBXML2_INCLUDE_DIR=/usr/include/libxml2 \
    -DLIBXML2_LIBRARIES=/usr/lib/x86_64-linux-gnu/libxml2.so \
    ../IfcOpenShell-source/cmake/
```



#### Spécification de l\'installation dans le répertoire personnel de l\'utilisateur 

Par défaut, le module Python `ifcopenshell` sera installé dans un répertoire système `site-packages/`. Il nécessite donc des privilèges de superutilisateur. En définissant la variable `USERSPACE_PYTHON_PREFIX`, l\'installation du module Python se fera dans le répertoire personnel de l\'utilisateur.


```python
cmake \
    ...
    -DUSERSPACE_PYTHON_PREFIX=ON \
    ../IfcOpenShell-source/cmake/
```



#### Spécification de la version Python 

Si vous souhaitez générer une liaison pour une version particulière de Python, définissez la variable `PYTHON_EXECUTABLE` sur l\'exécutable spécifique. N\'oubliez pas que cette version doit être la même version de Python avec laquelle FreeCAD a été compilé. 
```python
cmake \
    ...
    -DPYTHON_EXECUTABLE=/usr/bin/python3.6 \
    ../IfcOpenShell-source/cmake/
```



#### Ligne de configuration unique 

Dans un système Debian/Ubuntu typique, vous pouvez utiliser cette ligne pour configurer la compilation. Ajustez-le si nécessaire. 
```python
cmake -DOCC_INCLUDE_DIR=/usr/include/opencascade -DOCC_LIBRARY_DIR=/usr/lib/x86_64-linux-gnu -DLIBXML2_INCLUDE_DIR=/usr/include/libxml2 -DLIBXML2_LIBRARIES=/usr/lib/x86_64-linux-gnu/libxml2.so -DUSERSPACE_PYTHON_PREFIX=ON ../IfcOpenShell-source/cmake/
```

Sans OpenCOLLADA: 
```python
cmake -DOCC_INCLUDE_DIR=/usr/include/opencascade -DOCC_LIBRARY_DIR=/usr/lib/x86_64-linux-gnu -DCOLLADA_SUPPORT=FALSE -DLIBXML2_INCLUDE_DIR=/usr/include/libxml2 -DLIBXML2_LIBRARIES=/usr/lib/x86_64-linux-gnu/libxml2.so -DUSERSPACE_PYTHON_PREFIX=ON ../IfcOpenShell-source/cmake/
```



### Compilation réelle 

S\'il n\'y avait pas de message d\'erreur lors de la configuration avec CMake, un `Makefile` aurait dû être créé dans le répertoire build, vous pouvez donc procéder à la compilation des bibliothèques en exécutant `make`. 
```python
make -j N
```


`N`

est le nombre de processeurs que vous attribuez au processus de compilation; choisissez au moins un de moins que le nombre total de cœurs de processeur dont vous disposez.



### Dépannage et autres options 

Toutes les options de configuration sont disponibles dans le fichier `CMakeLists.txt` situé dans le répertoire `IfcOpenShell-source/cmake/`. S\'il y a des problèmes lors de l\'exécution de CMake ou Make, recherchez ici d\'autres options qui peuvent devoir être définies.

Dans toutes les instructions ci-dessus, au lieu de `cmake`, l\'interface graphique `cmake-gui` peut être utilisée. Cela montrera rapidement les options disponibles dans la configuration.


```python
cmake-gui ../IfcOpenShell-source/cmake/
```



### Test de la compilation dans le répertoire build 

Si la compilation réussit, vous devriez avoir un sous-répertoire `examples/` avec l\'exécutable `IfcOpenHouse` nouvellement compilé. Exécutez cet utilitaire à partir du répertoire de compilation pour générer un exemple de fichier IFC. 
```python
example/IfcOpenHouse
```

L\'exemple de fichier [IFC](Arch_IFC/fr.md) doit apparaître dans le répertoire build et peut être utilisé comme entrée dans l\'exécutable `IfcConvert` également récemment compilé. Cet utilitaire prend en entrée un fichier IFC et produit en sortie un format différent comprenant [OBJ](Arch_OBJ/fr.md), [DAE](Arch_DAE/fr.md) si le support OpenCOLLADA était activé, STEP, IGS, XML, \[\[Draft_SVG/fr\|SVG\] \] ou un autre [IFC](Arch_IFC/fr.md). 
```python
./IfcConvert IfcOpenHouse.ifc
```

Si aucun fichier de sortie n\'est spécifié, il créera par défaut un fichier [OBJ](Arch_OBJ/fr.md) et sa table de matériaux d\'accompagnement (MTL).



### Installation des bibliothèques compilées 

Si la compilation ne signale aucune erreur, vous pouvez exécuter `make install` pour copier les en-têtes, les bibliothèques compilées et les binaires dans leurs répertoires d\'installation correspondants.


```python
sudo make install
```

Par défaut, `CMAKE_INSTALL_PREFIX` est `/usr/local/`, donc tous les fichiers compilés seront mis sous ce répertoire, qui nécessite normalement des privilèges élevés. 
```python
/usr/local/bin/IfcConvert
/usr/local/bin/IfcGeomServer
/usr/local/include/ifcparse/*.h
/usr/local/include/ifcgeom/*.h
/usr/local/include/ifcgeom_schema_agnostic/*.h
/usr/local/include/serializers/{*.h,*.cpp}
/usr/local/include/serializers/schema_dependent/{*.h,*.cpp}
/usr/local/lib/libIfcGeom*.a
/usr/local/lib/libIfcParse.a
/usr/local/lib/libSerializers*.a
```

Le module Python `ifcopenshell` requis pour FreeCAD n\'est pas réellement présent dans le répertoire de construction; ce package est créé uniquement lorsque `make install` est exécuté. Le package résultant est placé dans un répertoire `site-packages/` ou dans un répertoire `dist-packages/` pour les distributions Debian/Ubuntu. 
```python
/usr/lib/python3/dist-packages/ifcopenshell/
```

Si la variable `USERSPACE_PYTHON_PREFIX` a été définie lors de l\'étape de configuration de CMake, `ifcopenshell` sera placé dans le répertoire `site-packages/` de l\'utilisateur. 
```python
$HOME/.local/lib/python3.6/site-packages/ifcopenshell/
```



### Suppression des bibliothèques compilées 

Pour supprimer les bibliothèques installées, supprimez simplement les fichiers correspondants qui ont été installés et le répertoire `ifcopenshell/` avec tous les modules à l\'intérieur. 
```python
sudo rm -rf /usr/local/bin/IfcConvert
sudo rm -rf /usr/local/bin/IfcGeomServer
sudo rm -rf /usr/local/include/ifcparse/
sudo rm -rf /usr/local/include/ifcgeom/
sudo rm -rf /usr/local/include/ifcgeom_schema_agnostic/
sudo rm -rf /usr/local/lib/libIfcGeom*
sudo rm -rf /usr/local/lib/libIfcParse*
sudo rm -rf /usr/local/lib/libSerializers*
```


```python
sudo rm -rf /usr/lib/python3/dist-packages/ifcopenshell/
```

Ou si la variable `USERSPACE_PYTHON_PREFIX` a été définie. 
```python
sudo rm -rf $HOME/.local/lib/python3.6/site-packages/ifcopenshell/
```



### Installation manuelle 

La compilation de toute la distribution IfcOpenShell produit des binaires comme `IfcConvert` et `IfcGeomServer` ainsi que de nombreuses bibliothèques statiques (`lib*.a`) dans le répertoire de construction. Cependant, pour FreeCAD, nous n\'avons besoin que du module Python `ifcopenshell`. Ce module n\'est pas un fichier unique mais un \"package\", c\'est-à-dire un répertoire contenant divers fichiers. Ce package `ifcopenshell` est assemblé à partir des wrappers Python créés à l\'intérieur de `IfcOpenShell-build/ifcwrap/` et des modules Python dans le répertoire source d\'origine `IfcOpenShell-source/src/ifcopenshell-python/ifcopenshell/`.

-   Produit par le processus de compilation:


```python
../IfcOpenShell-build/ifcwrap/ifcopenshell_wrapper.py
../IfcOpenShell-build/ifcwrap/_ifcopenshell_wrapper.so
```

-   Existant dans le répertoire source:


```python
../IfcOpenShell-source/src/ifcopenshell-python/ifcopenshell/
```

Le module `ifcopenshell` est créé en copiant le répertoire source d\'origine et en y ajoutant les deux fichiers `*ifcopenshell_wrapper*`.


```python
cp -rt . ../IfcOpenShell-source/src/ifcopenshell-python/ifcopenshell/
cp -t ifcopenshell/ ifcwrap/ifcopenshell_wrapper.py ifcwrap/_ifcopenshell_wrapper.so
```

Désormais, ce répertoire peut être déplacé vers le système `site-packages/` (`dist-packages/` pour Debian/Ubuntu) spécifique à l\'utilisateur pour le rendre disponible pour toutes les applications Python. 
```python
mv -t $HOME/.local/lib/python3.6/site-packages/ ifcopenshell/
```

Ou pour une installation à l\'échelle du système: 
```python
sudo mv -t /usr/lib/python3/dist-packages/ ifcopenshell/
```

Maintenant, le module `ifcopenshell` devrait être disponible pour être importé depuis une [console Python](Python_console/fr.md). 
```python
>>> import ifcopenshell
>>> print(ifcopenshell.version)
0.6.0b0
>>> print(ifcopenshell.__path__)
['/home/user/.local/lib/python3.6/site-packages/ifcopenshell']
```



## Application de visualisation IFC 

La bibliothèque IfcOpenShell comprend en fait une petite visionneuse graphique pour les fichiers IFC qui utilise PyQt5 et PythonOCC.

Pour lancer ce visualiseur depuis la console Python, la classe `application` doit être instanciée et démarrée: 
```python
from ifcopenshell.geom.app import application
application().start()
```

Si la bibliothèque est déjà installée, l\'ensemble du module peut également être exécuté à partir du terminal: 
```python
python3 /home/user/.local/lib/python3.6/site-packages/ifcopenshell/geom/app.py
```

Au moment de la rédaction de cet article (2020), seule la version [PythonOCC](PythonOCC/fr.md) compilée pour l\'édition communautaire (OCE) [OpenCASCADE](OpenCASCADE/fr.md) était prise en charge.



## Visionneuse en ligne IFC 

Le projet IfcOpenShell a également développé \"IFC Pipeline\", un programme de traitement et de visualisation IFC auto-hébergé. Il fournit également une petite application Web qui accepte les téléchargements de fichiers, que tout le monde peut utiliser. Cela signifie que pour visualiser les données IFC, vous n\'avez pas besoin d\'installer localement IfcOpenShell ou d\'autres visionneuses. Vous pouvez simplement charger votre fichier IFC dans ce système pour voir le résultat.

-   Visionneuse en ligne: <https://view.ifcopenshell.org/>
-   Dépôt: [AECgeeks/ifc-pipeline](https://github.com/AECgeeks/ifc-pipeline)



## Plus d\'informations 

-   Site Web: [ifcopenshell.org](http://ifcopenshell.org/)
-   Dépôt de code: [IfcOpenShell/IfcOpenShell](https://github.com/IfcOpenShell/IfcOpenShell)
-   Académie avec exemples et articles: [academy.ifcopenshell.org](http://academy.ifcopenshell.org/)
-   [Visionneuse en ligne IfcOpenShell](https://view.ifcopenshell.org/)
-   Communauté OSArch avec des ressources pour l\'architecture open source: [wiki.OSArch.org](https://wiki.osarch.org/index.php?title=Main_Page)
-   [Installation d\'IfcOpenShell](https://forum.freecadweb.org/viewtopic.php?f=39&t=48971); discussion principale du forum.
-   [Installation IFC](https://forum.freecadweb.org/viewtopic.php?f=39&t=12368&start=10#p117883); ancienne discussion du forum.
-   [IfcPlusPlus compilé sur Gentoo - questions et alternatives?](https://forum.freecadweb.org/viewtopic.php?f=39&t=33254)
-   [Compilation IfcOpenShell pour MacOS](Import/Export_IFC_-_compiling_IfcOpenShell/fr.md); un guide qui décrit le processus général. Cela peut ne plus être nécessaire car IfcOpenShell est maintenant distribué avec FreeCAD grâce à [Conda](Conda/fr.md).
-   Quelles pages sont liées à [cette page](Special:WhatLinksHere/IfcOpenShell.md).


 {{FEM_Tools_navi}}



---
⏵ [documentation index](../README.md) > [3rd_Party](Category_3rd_Party.md) > [BIM](Category_BIM.md) > [FEM](Category_FEM.md) > IfcOpenShell/fr
