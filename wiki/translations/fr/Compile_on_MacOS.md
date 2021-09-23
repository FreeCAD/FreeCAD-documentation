# Compile on MacOS/fr






**Il existe un conteneur Docker FreeCAD expérimental qui est testé pour le développement FreeCAD. En savoir plus à ce sujet sur [Compiler sur Docker](Compile_on_Docker/fr.md)**


{{TOCright}}

## Présentation

Cette page décrit comment compiler le code source FreeCAD sur MacOS X. Pour les autres plates-formes, voir [Compiler](Compiling/fr.md).

Ces instructions ont été testées sur macOS Catalina avec le XCode 11.6 standard. Il est connu pour fonctionner sur macOS BigSur Beta avec XCode 12.0 beta. Si vous prévoyez d\'utiliser XCode Beta, assurez-vous de télécharger le module complémentaire Outils de ligne de commande via un package dmg pour contourner certains problèmes de dépendance libz.

Cette page sert de point de départ et n'a pas vocation à être exhaustive en ce qui concerne la description de toutes les options disponibles de build.

Si vous souhaitez simplement évaluer la dernière version de FreeCAD en version préliminaire, vous pouvez télécharger les fichiers binaires pré-construits [ici](https://github.com/FreeCAD/FreeCAD/releases).

## Conditions préalables à l\'installation 

Les logiciels suivants doivent être installés pour prendre en charge le processus de compilation.

### Gestionnaire de paquets Homebrew 

Homebrew est un gestionnaire de paquets basé sur la ligne de commande pour macOS. La [page d\'accueil de Homebrew](https://brew.sh/) fournit une ligne de commande d\'installation que vous collez simplement dans une fenêtre de terminal.

### CMake

CMake est un outil de build qui génère une configuration de build basée sur les variables que vous spécifiez. Vous lancez ensuite la commande \'make\' pour construire cette configuration. La version en ligne de commande de CMake est automatiquement installée dans le cadre de l\'installation de Homebrew, ci-dessus. Si vous préférez utiliser une version graphique de CMake, vous pouvez la télécharger à partir de [ici](https://www.cmake.org/downloadDownload).

## Installation des dépendances 

FreeCAD maintient un \'tap\' Homebrew qui installe les formules et dépendances requises. Exécutez les commandes de préparation suivantes dans votre terminal.


```python
brew tap freecad/freecad
brew install eigen
brew install --only-dependencies freecad --with-packaging-utils
```

Remarques :

1.  \'brew install\' peut prendre un certain temps, l\'occasion de prendre un verre.
2.  Homebrew est actuellement livré avec Boost 1.73 qui contient un bogue pour compiler FreeCAD. Veuillez éditer le fichier /usr/local/opt/boost/include/boost/geometry/index/detail/rtree/visitors/insert.hpp et en ligne 265 déclarer MembersHolder::visitor comme étant une valeur publique en remplaçant : MembersHolder::visitor with : public MembersHolder::visitor

## Obtenir les sources 

Dans les instructions suivantes, les dossiers source et de build sont créés côte à côte sous


```python
/Users/username/FreeCAD
```

mais vous pouvez utiliser les dossiers de votre choix.


```python
mkdir ~/FreeCAD
cd ~/FreeCAD
```

La commande suivante clone le référentiel FreeCAD git dans un répertoire appelé FreeCAD-git.


```python
git clone https://github.com/FreeCAD/FreeCAD FreeCAD-git
```

Créez le dossier build.


```python
mkdir ~/FreeCAD/build
```

## Lancer CMake 

Ensuite, nous allons lancer CMake pour générer la configuration de construction. Plusieurs options doivent être transmises à CMake. Le tableau suivant décrit les options et donne un aperçu.

### Les options de CMake 

  Nom                           Valeur                                     Remarques
  ----------------------------- ------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  CMAKE\_BUILD\_TYPE            Release (STRING)                           Release ou Debug. Le débogage est généralement utilisé pour les tests au niveau développeur mais peut également être requis pour des tests et le dépannage au niveau utilisateur.
  BUILD\_QT5                    1 (BOOL)                                   Nécessaire pour un build avec Qt5.
  CMAKE\_PREFIX\_PATH           \"/usr/local/opt/qt5152;\" \... (Chemin)   Nécessaire pour un build avec Qt5. Voir la remarque ci-dessous. Vous devez également ajouter le chemin d\'accès au fichier de configuration cmake des librairies VTK et NGLIB.
  FREECAD\_CREATE\_MAC\_APP     1 (BOOL)                                   Crée un paquet FreeCAD.app à l\'emplacement spécifié dans CMAKE\_INSTALL\_PREFIX lorsque la commande \'make install\' a été émise.
  CMAKE\_INSTALL\_PREFIX        \"./..\" (PATH)                            Chemin où vous souhaitez générer le paquet FreeCAD.app.
  FREECAD\_USE\_EXTERNAL\_KDL   1 (BOOL)                                   Nécessaire.
  BUILD\_FEM\_NETGEN            1 (BOOL)                                   Requis si vous choisissez de construire les outils FEM.

Remarque : ligne de commande pour générer CMAKE\_PREFIX\_PATH :

ls -d $(brew list -1 | grep qt | tail -1 | xargs brew --cellar)/*/lib/cmake

### Interface graphique CMake 

Ouvrez l\'application CMake, et remplissez les champs source et dossier de compilation. Dans cet exemple, il s\'agirait de **/Users/username/FreeCAD/FreeCAD-git** pour les sources et */Users/username/FreeCAD/build*\' pour le dossier de build.

Ensuite, cliquez sur le bouton **Configure** pour remplir la liste des options de configuration. Cela affichera une boîte de dialogue vous demandant de spécifier quel générateur utiliser. Laissez la valeur par défaut **Unix Makefiles**. La configuration échouera pour la première fois car certaines options doivent être changées. Remarque: vous devrez cocher la case à cocher **Advanced** pour obtenir toutes les options.

Définissez les options du tableau ci-dessus, puis cliquez à nouveau sur **Configure** puis sur **Generate**.

### CMake en lignes de commande 

Entrez ce qui suit dans le terminal.


```python
export PREFIX_PATH="/usr/local/opt/qt5152;\
/usr/local/Cellar/nglib/v6.2.2007/Contents/Resources;\
/usr/local/Cellar/vtk@8.2/8.2.0_1/lib/cmake;"
```


```python
$cd ~/FreeCAD/build
$cmake \
  -DCMAKE_BUILD_TYPE="Release"   \
  -DBUILD_QT5=1                  \
  -DWITH_PYTHON3=1               \
  -DCMAKE_PREFIX_PATH="$PREFIX_PATH" \
  -DPYTHON_EXECUTABLE="/usr/local/bin/python3" \
  -DFREECAD_USE_EXTERNAL_KDL=1   \
  -DCMAKE_CXX_FLAGS='-std=c++14' \
  -DBUILD_FEM_NETGEN=1           \
  -DFREECAD_CREATE_MAC_APP=1     \
  -DCMAKE_INSTALL_PREFIX="./.."  \
  ../FreeCAD-git/

```

## Exécuter make 

Enfin, à partir d'un terminal, exécutez **make** pour compiler et lier FreeCAD et générer le paquet applicatif.


```python
cd ~/FreeCAD/build
make -j5 install
```

L\'option -j spécifie le nombre de processus de création à exécuter simultanément. Prendre le nombre de cœurs de processeur et ajouter un est généralement le bon nombre à utiliser. Cependant, si la compilation échoue pour une raison quelconque, il est utile de réexécuter make sans l\'option -j afin de pouvoir voir exactement où l\'erreur s\'est produite.

Voir aussi [Compilation (accélération)](Compiling_(Speeding_up)/fr.md).

Si make se termine sans erreur, vous pouvez maintenant lancer FreeCAD en double-cliquant sur l\'exécutable dans le Finder.

## Mise à jour depuis Github 

Le développement de FreeCAD est rapide ; chaque jour ou presque, il y a des corrections de bugs ou de nouvelles fonctionnalités. Pour obtenir les dernières modifications, utilisez git pour mettre à jour le répertoire source (voir [Gestion du code source](Source_code_management/fr.md)), puis réexécutez CMake et suivez les étapes ci-dessus. Dans ce cas, il n'est généralement pas nécessaire de commencer par un répertoire de build vierge et les compilations suivantes iront généralement beaucoup plus vite que la première.

## Faire une compilation avec Qt4 et Python 2.7 

FreeCAD est passé de Qt 4 à Qt 5 comme homebrew. Qt 4 n\'est plus disponible en option pour une nouvelle version sur macOS après la transition Qt 5. Python 2.7 est obsolète dans homebrew et macOS à venir et nous ne le supportons plus non plus pour la version macOS.

## Dépannage

### Un segfault sur le lancement de Qt5 

Si Qt4 a été précédemment installé via Homebrew et que vous faites un build ensuite avec Qt5, vous pouvez obtenir une exception EXC\_BAD\_ACCESS (SEGSEGV) lors du lancement de la nouvelle version de Qt5. Le correctif consiste à désinstaller manuellement Qt4.


```python
brew uninstall --ignore-dependencies --force cartr/qt4/shiboken@1.2 cartr/qt4/pyside@1.2 cartr/qt4/pyside-tools@1.2 cartr/qt4/qt-legacy-formula
```

### Fortran

*\"No CMAKE\_Fortran\_COMPILER could be found.\"* (Aucun CMAKE\_Fortran\_COMPILER n\'a pu être trouvé) lors de la configuration - Les anciennes versions de FreeCAD nécessiteront l\'installation d\'un compilateur Fortran. Avec Homebrew, faites \"brew install gcc\" et essayez à nouveau de configurer cmake en donnant le chemin à Fortran, c\'est-à-dire -DCMAKE\_Fortran\_COMPILER=/opt/local/bin/gfortran-mp-4.9, ou utilisez de préférence une version plus récente de la source FreeCAD!

### OpenGL

Voir [OpenGL sur MacOS](OpenGL_on_MacOS.md) pour les problèmes OpenGL lorsque Qt 4.8 et versions antérieures sont utilisées sous MacOS.

### FreeType

Si vous utilisez des versions de CMake antérieures à la version 3.1.0, il est nécessaire de définir la variable CMake FREETYPE\_INCLUDE\_DIR\_freetype2 manuellement, par exemple /usr/local/include/freetype2.

### Instructions de compilation supplémentaires 

FreeCAD peut être construit à partir du dernier master git hébergé sur github et lancé à partir d\'une CLI en utilisant les bibliothèques fournies par le tap homebrew-freecad. Pour une liste complète des instructions de construction, voir [ici](https://github.com/ipatch/homebrew-us-05/tree/dev/freecad#building-freecad-for-macos-by-macos).







[Category:Developer\_Documentation](Category:Developer_Documentation.md) [Category:Developer](Category:Developer.md)
