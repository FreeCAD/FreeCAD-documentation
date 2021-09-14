# PySide/fr




{{TOCright}}

## Introduction

La bibliothèque [PySide](PySide/fr.md) donne accès à la boîte à outils d\'interface utilisateur graphique (GUI) Qt de [Python](Python/fr.md). Qt est une collection de bibliothèques C++, mais avec l\'aide de PySide, les mêmes composants peuvent être utilisés à partir de [Python](Python/fr.md). Chaque interface graphique qui peut être créée en C++, peut également être créée et modifiée en Python. Un avantage de l\'utilisation de Python est que les interfaces Qt peuvent être développées et testées en direct, car nous n\'avons pas besoin de compiler les fichiers source.

Lorsque vous [installez](Installing/fr.md) FreeCAD, vous devriez obtenir à la fois Qt et PySide dans le package. Si vous [compilez](Compiling/fr.md) vous-même, vous devez vérifier que ces deux bibliothèques sont installées pour que FreeCAD fonctionne correctement. Bien sûr, PySide ne fonctionnera que si Qt est présent.

Dans le passé, FreeCAD utilisait PyQt, une autre liaison Qt pour Python, mais en 2013 ([1dc122dc9a](https://github.com/FreeCAD/FreeCAD/commit/1dc122dc9a)) le projet a migré vers PySide car il a une [licence](licence/fr.md) plus permissible.

Pour plus d\'informations, consultez:

-   [Wikipédia: PySide](https://fr.wikipedia.org/wiki/PySide)
-   [Différences entre PySide et PyQt](http://qt-project.org/wiki/Differences_Between_PySide_and_PyQt)

![](images/PySideScreenSnapshot1.jpg ) ![](images/PySideScreenSnapshot2.jpg ) *Exemples créés avec PySide. À gauche: un simple dialogue. À droite: un dialogue plus complexe avec des graphiques.*

## PySide dans FreeCAD avec Qt5 

FreeCAD a été développé pour être utilisé avec Python 2 et Qt4. Comme ces deux bibliothèques sont devenues obsolètes, FreeCAD est passé à Python 3 et Qt5. Dans la plupart des cas, cette transition s\'est faite sans qu\'il soit nécessaire de rompre la rétrocompatibilité.

Normalement, le module `PySide` fournit un support pour Qt4, tandis que `PySide2` fournit un support pour Qt5. Cependant, dans FreeCAD, il n\'est pas nécessaire d\'utiliser directement `PySide2` car un module spécial `PySide` est inclus pour gérer Qt5.

Ce module `PySide` est situé dans le répertoire `Ext/` d\'une installation de FreeCAD compilée pour Qt5. 
```python
/usr/share/freecad/Ext/PySide
```

Ce module importe simplement les classes nécessaires depuis `PySide2` et les place dans l\'espace de noms `PySide`. Cela signifie que dans la plupart des cas, le même code peut être utilisé avec Qt4 et Qt5, tant que nous utilisons l\'unique module `PySide`. 
```python
PySide2.QtCore -> PySide.QtCore
PySide2.QtGui -> PySide.QtGui
PySide2.QtSvg -> PySide.QtSvg
PySide2.QtUiTools -> PySide.QtUiTools
```

Le seul aspect inhabituel est que les classes `PySide2.QtWidgets` sont placées dans l\'espace de noms `PySide.QtGui`. 
```python
PySide2.QtWidgets.QCheckBox -> PySide.QtGui.QCheckBox
```

[En haut](#top.md)

## Exemples d\'utilisation de PySide 

-   [Exemples PySide Débutant](PySide_Beginner_Examples/fr.md), bonjour le monde, annonces, entrez du texte, entrez un numéro.
-   [Exemples intermédiaires PySide](PySide_Intermediate_Examples/fr.md), dimensionnement de la fenêtre, masquage des widgets, menus contextuels, position de la souris, événements de la souris.
-   [Exemples avancés de PySide](PySide_Advanced_Examples/fr.md), de nombreux widgets.

Les exemples de PySide sont divisés en 3 parties, différenciées par niveau d\'exposition à PySide, Python et les composants internes de FreeCAD. La première page a un aperçu sur PySide; les deuxième et troisième pages sont pour la plupart des exemples de code à différents niveaux.

On s\'attend à ce que ces exemples soient utiles pour commencer et par la suite l\'utilisateur peut consulter d\'autres ressources en ligne ou la documentation officielle.

[En haut](#top.md)

## Documentation

Il existe quelques différences dans la gestion des widgets dans Qt4 (PySide) et Qt5 (PySide2). Le programmeur doit être conscient de ces incompatibilités et consulter la documentation officielle si quelque chose ne semble pas fonctionner comme prévu sur une plateforme donnée. Néanmoins, Qt4 est considéré comme obsolète, donc la plupart des développements devraient cibler Qt5 et Python 3.

La documentation PySide fait référence aux classes de style Python; cependant, puisque Qt est à l\'origine une bibliothèque C++, les mêmes informations devraient être disponibles dans la référence C++ correspondante.

-   [Modules Qt](https://doc.qt.io/qtforpython/modules.html) disponibles sur PySide2 (Qt5).
-   [Toutes les classes Qt par module](https://doc.qt.io/qt-5/modules-cpp.html) dans Qt5 pour C++.
-   [Modules Qt](https://deptinfo-ensip.univ-poitiers.fr/ENS/pyside-docs/index.html) disponibles auprès de PySide (Qt4).

[En haut](#top.md)


{{Powerdocnavi

}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)
