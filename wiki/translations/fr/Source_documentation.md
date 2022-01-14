# Source documentation/fr
{{TOCright}}

## Présentation

Le code source de FreeCAD est commenté pour permettre la génération automatique de documentation HTML à l\'aide de [Doxygen](Doxygen/fr.md), un système de documentation de code source populaire. Doxygen peut documenter les parties C++ et Python de FreeCAD, générant ainsi des pages HTML avec des hyperliens vers chaque fonction et classe documentées.

La documentation est hébergée en ligne sur le [site web de l\'API FreeCAD](https://freecad.github.io/SourceDoc/). Veuillez noter que cette documentation n\'est pas toujours maintenue à jour. Si vous avez besoin de plus de détails, téléchargez le dernier code source de FreeCAD et compilez vous-même la documentation. Si vous avez des questions urgentes sur le code, veuillez les poser dans la section développeurs du [FreeCAD forum](https://forum.freecadweb.org/index.php).

La compilation de la documentation de l\'API suit les mêmes étapes générales que la compilation de l\'exécutable FreeCAD, comme indiqué dans la page de [compilation sous Linux](Compile_on_Linux/fr.md).

<img alt="" src=images/FreeCAD_documentation_compilation_workflow.svg  style="width:800px;">



*Flux de travail général pour compiler la documentation de programmation de FreeCAD. Les packages Doxygen et Graphviz doivent être dans le système, ainsi que le code source FreeCAD lui-même. CMake configure le système de telle sorte qu'avec une seule instruction make, la documentation de l'ensemble du projet soit compilée dans de nombreux fichiers HTML avec des diagrammes.*

## Compilation de la documentation 

### Documentation complète 

Si vous avez installé Doxygen, il est très facile de construire la documentation. Installez également [Graphviz](https://www.graphviz.org/) pour pouvoir produire des diagrammes montrant les relations entre différentes classes et bibliothèques dans le code FreeCAD. Graphviz est également utilisé par le [graphe de dépendance](Std_DependencyGraph/fr.md) de FreeCAD pour montrer les relations entre différents objets. 
```python
sudo apt install doxygen graphviz
```

Suivez ensuite les mêmes étapes que pour compiler FreeCAD, comme décrit à la page [Compiler sous Linux](Compile_on_Linux/fr.md), et résumées ici pour plus de commodité.

-   Récupérez le code source de FreeCAD et placez-le dans son propre répertoire `freecad-source`.
-   Créez un autre répertoire `freecad-build` dans lequel vous compilerez FreeCAD et sa documentation.
-   Configurez les sources avec `cmake`, en vous assurant d\'indiquer le répertoire source et de spécifier les options requises pour votre compilation.
-   Lancer la création de la documentation avec `make`.


```python
git clone https://github.com/FreeCAD/FreeCAD.git freecad-source
mkdir freecad-build
cd freecad-build
cmake -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 ../freecad-source
```

Pendant que vous êtes dans le répertoire de compilation, émettez les instructions suivantes pour ne créer que la documentation. 
```python
make -j$(nproc --ignore=2) DevDoc
``` Comme mentionné dans [Compilation (Accélération)](Compiling_(Speeding_up)/fr.md), l\'option `-j` définit le nombre de cœurs de processeur utilisés pour la compilation. Les fichiers de documentation résultants apparaîtront dans le répertoire 
```python
freecad-build/doc/SourceDocu/html/
```

Le point d'entrée de la documentation est le fichier `index.html`, que vous pouvez ouvrir avec un navigateur Web: 
```python
xdg-open freecad-build/doc/SourceDocu/html/index.html
```

La cible `DevDoc` générera une quantité importante de données, environ 5 Go de nouveaux fichiers, en raison notamment des diagrammes créés par Graphviz.

### Documentation réduite 

La documentation complète utilise environ 3 Gb d\'espace disque. Une autre version plus petite de la documentation, qui ne nécessite qu\'environ 600 MB, peut être générée avec une cible différente. Ceci est la version affichée sur le [site Web de l\'API FreeCAD](https://freecad.github.io/SourceDoc/). 
```python
make -j$(nproc --ignore=2) WebDoc
```

La documentation sur le [site Web de l\'API FreeCAD](https://freecad.github.io/SourceDoc/) est produite automatiquement à partir de <https://github.com/FreeCAD/SourceDoc>. Tout le monde peut le reconstruire et soumettre un pull request :

-   forkez le repo sur <https://github.com/FreeCAD/SourceDoc>
-   sur votre machine: clonez le code FreeCAD (si vous ne l\'avez pas encore fait), créez un répertoire de construction pour le document et clonez le référentiel SourceDoc ci-dessus à l\'intérieur. Ce SourceDoc sera mis à jour lorsque vous reconstruirez le document et vous pourrez valider et pousser les résultats par la suite:


```python
git clone https://github.com/FreeCAD/FreeCAD
cd FreeCAD
mkdir build
cd build
mkdir -p doc/SourceDocu/html
cd doc/SourceDocu/html
git clone your-fork-url
cd ../../..
cmake -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 ..
make WebDoc
cd doc/SourceDocu/html
git commit
git push
```

-   Accédez à votre fork en ligne et créez un pull request.

## Autres versions 

Documentation de la [version développement FreeCAD 0.19](https://iesensor.com/FreeCADDoc/0.19/) construite par [qingfeng.xia](http://forum.freecadweb.org/viewtopic.php?t=12613).

## Intégrer la documentation Coin3D 

Sur les systèmes Unix, il est possible de lier la documentation source Coin3D avec FreeCAD. Cela facilite la navigation et complète les diagrammes d\'héritage pour les classes dérivées de Coin.

-   Installez le `libcoin-doc`, `libcoin80-doc`, ou un paquetage similaire.
-   Décompressez l\'archive `coin.tar.gz` située dans `/usr/share/doc/libcoin-doc/html`; les fichiers sont peut-être déjà décompressés dans votre système.
-   Générez à nouveau la documentation source.

Si vous n\'installez pas le package de documentation pour Coin, les liens seront générés pour accéder à la documentation en ligne à l\'adresse [BitBucket](https://coin3d.bitbucket.io/Coin/). Cela se produira si un fichier de balise Doxygen peut être téléchargé au moment de la configuration avec `wget`.

## Utiliser Doxygen 

Voir la page [Doxygen](Doxygen/fr.md) pour une explication détaillée sur la façon de commenter le code source C++ et Python afin qu\'il puisse être traité par Doxygen pour créer automatiquement la documentation.

Basiquement, un bloc de commentaires commençant par `/**` ou `///` pour C++, ou `##` pour Python, doit apparaître avant chaque définition de classe ou de fonction, afin qu'elle soit sélectionnée par Doxygen. De [nombreuses commandes spéciales](Doxygen/fr#Balisage_Doxygen.md), commençant par `\` ou `@`, peuvent être utilisées pour définir des parties du code et formater la sortie. La [syntaxe Markdown](Doxygen/fr#Support_de_Markdown.md) est également comprise dans le bloc de commentaires, ce qui facilite la mise en évidence de certaines parties de la documentation. 
```python
/**
 * Returns the name of the workbench object.
 */
std::string name() const;

/**
 * Set the name to the workbench object.
 */
void setName(const std::string&);

/// remove the added TaskWatcher
void removeTaskWatcher(void);
```





 

[<img src="images/Property.png" style="width:16px"> Developer Documentation](Category_Developer_Documentation.md)

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Source documentation/fr
