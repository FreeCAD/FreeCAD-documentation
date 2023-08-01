# Compiling (Speeding up)/fr
{{TOCright}}



## Présentation

FreeCAD est une application relativement lourde dont la compilation complète à partir des sources peut prendre entre 10 minutes et une heure. Cela dépend principalement du processeur dont vous disposez et du nombre de cœurs utilisés dans le processus de compilation. Voici quelques conseils pour raccourcir ce processus et raccourcir les temps de construction.

## CCache

Installez `ccache` pour mettre en cache les builds.

[Ccache](https://ccache.dev/) accélère la recompilation en mettant en cache les compilations précédentes et en détectant quand la même compilation est effectuée à nouveau. Ccache est un logiciel libre, publié sous licence GPLv3 ou ultérieure.

Sur la plupart des systèmes, ccache sera automatiquement détecté et activé, vous pouvez utiliser l\'option `FREECAD_USE_CCACHE` `cmake` pour contrôler ce comportement.



## Désactiver des modules 

Lorsque vous utilisez `cmake` pour configurer le build, vous pouvez désactiver la compilation de certains ateliers dont vous n\'avez peut-être pas besoin pour le moment. Ceci est utile si vous n\'avez besoin que de tester quelques ateliers.

Par exemple, pour éviter de compiler les ateliers FEM et Mesh :


```python
cmake -DBUILD_FEM=OFF -DBUILD_MESH=OFF ../freecad-source
```

Utilisez `cmake-gui`, `cmake-curses-gui` ou `cmake-qt-gui` pour afficher toutes les variables possibles pouvant être éditées lors de la configuration. En utilisant ces interfaces, vous pouvez facilement activer ou désactiver différents ateliers.



## Plusieurs actions en parallèle 

Après avoir configuré avec `cmake`, le programme `make` lance le compilateur C ++ à proprement dit pour qu\'il fonctionne sur les fichiers de code source. Vous pouvez accélérer la compilation en travaillant sur plusieurs fichiers en même temps. Ceci est réalisé avec l\'option `-j` de `make` qui indique le nombre de \"travaux\" ou de commandes de compilation exécutés simultanément. Cette option est un nombre entier.

Exécutez quatre commandes de compilation en parallèle :


```python
make -j4
```

Compilez autant de fichiers en parallèle que le nombre de cœurs de processeur de votre système. Ceci est utile si vous avez plusieurs cœurs et souhaitez tous les utiliser pour compiler le logiciel.


{{code|code=
make -j$(nproc)
}}

Compilez autant de fichiers en parallèle que le nombre de cœurs de processeur de votre système, moins deux. Utilisez cette option pour que votre système réponde toujours à une autre tâche. Par exemple, deux cœurs vous permettront d\'utiliser un navigateur, tandis que les autres cœurs continueront à compiler le logiciel en arrière-plan.


{{code|code=
make -j$(nproc --ignore=2)
}}

## distcc

Le programme `distcc` peut être utilisé pour effectuer une compilation distribuée de codes C et C ++ sur plusieurs machines d\'un réseau.

[Distcc](https://www.distcc.org/) devrait toujours produire les mêmes résultats qu\'une compilation locale. Il est gratuit, simple à installer et à utiliser, et souvent deux fois ou plus rapide que la compilation locale.

Le développeur FreeCAD \"etrombly\" a publié une courte explication sur [comment installer distcc pour compiler FreeCAD sur un réseau d\'ordinateurs en utilisant Docker](https://forum.freecadweb.org/viewtopic.php?f=4&t=50810&p=459142#p458614).



---
![](images/Button_right.svg) [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > Compiling (Speeding up)/fr
