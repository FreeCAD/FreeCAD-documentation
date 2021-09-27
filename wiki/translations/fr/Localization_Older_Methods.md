# Localization Older Methods/fr
{{docnav/fr
|[Branding](Branding/fr.md)
|[Extra python module](Extra_python_modules/fr.md)
}}

Ceci est un regroupement d\'anciennes méthodes de localisation utilisées par FreeCAD par le passé. Elles montrent une partie des processus internes, **mais les techniques de la page [Localisation](Localisation/fr.md) doivent être utilisées à partir de maintenant.**

### Translation avec Qt-Linguist (ancienne voie) 

Les informations suivantes ne doivent plus être utilisées et deviendront probablement obsolètes. Ces informations sont conservées ici afin que les programmeurs puissent se familiariser avec leur fonctionnement. -

-   Ouvrez tous les dossiers de langue de FreeCAD indiqués ci-dessous
-   Vérifiez qu'il n'existe pas de fichier .ts avec votre code de langue (\"fr\" pour le français, \"de\" pour l'allemand, etc \...)
-   S\'il existe, vous pouvez télécharger ce fichier si vous souhaitez modifier/réviser/améliorer la traduction (cliquez sur le fichier, puis téléchargez-le)
-   S\'il n\'existe pas, téléchargez le fichier .ts sans code de langue (ou tout autre fichier .ts disponible, cela fonctionnera aussi)
-   Renommez ce fichier avec votre code de langue
-   Ouvrez-le avec le programme Qt-Linguist
-   Commencez à traduire (Qt Linguist est très facile à utiliser)
-   Une fois que c\'est complètement fait, sauvegardez votre fichier
-   [envoyez-nous les fichiers](http://www.freecadweb.org/tracker/main_page.php) afin que nous puissions les inclure dans le code source de freecad afin que les autres utilisateurs en bénéficient également.

**Fichiers de traduction disponibles**

-   Les liens suivants mènent tous directement à la sourceforge qui n'est plus utilisée par FreeCAD. Le code est hébergé à l\'adresse <https://github.com/FreeCAD/FreeCAD>.
-   [FreeCAD main GUI](http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Gui/Language/)
-   [Complete Workbench](http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Mod/Complete/Gui/Resources/translations/)
-   [Drawing Workbench](http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Mod/Drawing/Gui/Resources/translations/)
-   [Draft Workbench](http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Mod/Draft/Resources/translations/)
-   [Reverse Engineering Workbench](http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Mod/ReverseEngineering/Gui/Resources/translations/)
-   [FEM Workbench](http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Mod/Fem/Gui/Resources/translations/)
-   [Robot Workbench](http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Mod/Robot/Gui/Resources/translations/)
-   [Image Workbench](http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Mod/Image/Gui/Resources/translations/)
-   [Sketcher Workbench](http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Mod/Sketcher/Gui/Resources/translations/)
-   [Mesh Workbench](http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Mod/Mesh/Gui/Resources/translations/)
-   [Test Workbench](http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Mod/Test/Gui/Resources/translations/)
-   [Points Workbench](http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Mod/Points/Gui/Resources/translations/)
-   [Raytracing Workbench](http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Mod/Raytracing/Gui/Resources/translations/)
-   [Part Workbench](http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Mod/Part/Gui/Resources/translations/)
-   [PartDesign Workbench](http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Mod/PartDesign/Gui/Resources/translations/)
-   [Assembly Workbench](http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Mod/Assembly/Gui/Resources/translations/)
-   [MeshPart Workbench](http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Mod/MeshPart/Gui/Resources/translations/)
-   Voici un très bon article du Forum sur l'ancien mode de traduction, mais il est en allemand. Voir <http://forum.freecadweb.org/viewtopic.php?f=13&t=19496&start=60#p152655>

## Préparer vos propres modules/applications pour la traduction 

### Prérequis

Pour localiser votre module d'application, vous avez besoin de l'aide de *Qt*. Vous pouvez le télécharger à partir du _ :

qmake: génère des fichiers de projet.
lupdate: extrait ou met à jour les textes originaux de votre projet en scannant le code source.
Qt-Linguist: Le *Qt-Linguist* est très facile à utiliser et vous aide à traduire avec de jolies fonctionnalités telles qu\'un livre de phrases pour les phrases courantes.

### Projet Setup 

Pour démarrer la localisation de votre projet, allez à la partie graphique de votre module et tapez sur la ligne de commande:


```python
qmake -project
```

Ceci analyse votre répertoire de projet pour les fichiers contenant des chaînes de texte et crée un fichier de projet comme dans l\'exemple suivant:


```python
 ######################################################################
 # Automatically generated by qmake (1.06c) Do 2. Nov 14:44:21 2006
 ######################################################################
 
 TEMPLATE = app
 DEPENDPATH += .\Icons
 INCLUDEPATH += .
 
 # Input
 HEADERS += ViewProvider.h Workbench.h
 SOURCES += AppMyModGui.cpp \
            Command.cpp \
            ViewProvider.cpp \
            Workbench.cpp
 TRANSLATIONS += MyMod_de.ts
```

Vous pouvez ajouter manuellement des fichiers ici. La section TRANSLATIONS contient une liste de fichiers avec la traduction pour chaque langue. Dans l\'exemple ci-dessus, *MyMod\_de.ts* est la traduction allemande.

Vous devez maintenant exécuter lupdate pour extraire tous les littéraux de chaîne de votre interface graphique. L\'exécution de lupdate après des modifications du code source est toujours sûre, car elle ne supprime jamais les chaînes de vos fichiers de traduction. Il ajoute seulement de nouvelles chaînes.

Vous devez maintenant ajouter les fichiers .ts à votre projet Visual Studio. Spécifiez la méthode de construction personnalisée suivante pour eux:


```python
 python ..\..\..\Tools\qembed.py "$(InputDir)\$(InputName).ts"
                 "$(InputDir)\$(InputName).h" "$(InputName)"
```

Remarque: Entrez ceci sur une ligne de commande, le saut de ligne n'est utilisé que pour la présentation.

En compilant le fichier  Gui.cpp*. Dans notre exemple, il s\'agirait de *AppMyModGui.cpp*. Là vous ajoutez la ligne


```python
new Gui::LanguageProducer("Deutsch", <Modul>_de_h_data, <Modul>_de_h_len);
```

publier votre traduction dans l\'application.

### Configuration des fichiers Python pour la traduction 

Pour faciliter la localisation des fichiers py, vous pouvez utiliser l\'outil \"pylupdate4\" qui accepte un ou plusieurs fichiers py. Avec l\'option -ts, vous pouvez préparer/mettre à jour un ou plusieurs fichiers .ts. Par exemple, pour préparer un fichier .ts en français, entrez simplement dans la ligne de commande:


```python
pylupdate4 *.py -ts YourModule_fr.ts 
```

l\'outil pylupdate analysera vos fichiers .py à la recherche des fonctions translate() ou tr() et créera un fichier YourModule\_fr.ts. Ce fichier peut être traduit avec QLinguist et un fichier YourModule\_fr.qm produit à partir de QLinguist ou avec la commande


```python
lrelease YourModule_fr.ts
```

Attention, l\'outil pylupdate4 n\'est pas très performant pour la reconnaissance des fonctions translate(), elles doivent être formatées de manière très spécifique (voir les fichiers du module Draft pour des exemples). Dans votre fichier, vous pouvez ensuite configurer un traducteur comme ceci (après avoir chargé votre QApplication mais AVANT de créer un widget qt):


```python
translator = QtCore.QTranslator()
translator.load("YourModule_"+languages[ln])
QtGui.QApplication.installTranslator(translator)
```

Vous pouvez également créer le fichier XML Draft.qrc avec le contenu suivant:


```python
<RCC>
<qresource prefix="/translations" > 
<file>Draft_fr.qm</file> 
</qresource> 
</RCC> 
```

et exécutant pyrcc4 Draft.qrc -o qrc\_Draft.py crée un grand fichier Python contenant toutes les ressources. BTW cette approche fonctionne également pour mettre des fichiers d\'icônes dans un fichier de ressources


{{docnav/fr
|[Branding](Branding/fr.md)
|[Extra python modules](Extra_python_modules/fr.md)
}}


 

_

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Localization Older Methods/fr
