# Localization Older Methods/de
{{docnav/de
|[Markenbindung](Branding/de.md)
|[Zusätzliche Python Module](Extra_python_modules/de.md)
}}

Dies ist eine Sammlung alter Lokalisierungstechniken, die von FreeCAD in der Vergangenheit verwendet wurden. Sie zeigen einige der Internas des Prozesses, **aber die Techniken auf der Seite [Lokalisierung](Lokalisation/de.md) sollten von nun an verwendet werden.**.

### Übersetzen mit Qt-Linguist (alte Methode) 

Die folgenden Informationen müssen nicht mehr verwendet werden und werden wahrscheinlich veraltet sein. Es wird hier aufbewahrt, damit sich Programmierer mit der Funktionsweise vertraut machen können. -

-   Öffne alle Sprachordner von FreeCAD, die unten gezeigt werden.
-   Vergewissere Dich, dass keine .ts-Datei mit Deinem Sprachcode existiert (\"fr\" für Französisch, \"de\" für Deutsch, etc\....).
-   Wenn es existiert, kannst du diese Datei herunterladen, wenn du die Übersetzung ändern, überprüfen oder verbessern möchtest (klicke auf die Datei und lade sie herunter).
-   Wenn es nicht existiert, lade die.ts-Datei ohne Sprachcode herunter (oder jede andere verfügbare.ts, es wird auch funktionieren).
-   Benenne diese Datei mit deinem Sprachcode um.
-   Öffne es mit dem Qt-Linguist Programm.
-   Beginne mit der Übersetzung (Qt Linguist ist sehr einfach zu bedienen).
-   Sobald es vollständig erledigt ist, speichere Deine Datei.
-   [sende die Dateien an uns](http://www.freecadweb.org/tracker/main_page.php), damit wir sie in den Freecad-Quellcode aufnehmen können, damit sie auch anderen Benutzern zugute kommen.

\'\'\' Verfügbare Übersetzungsdateien \'\'\'

-   The following links all direct to the sourceforge which is no longer used by FreeCAD. The code is hosted at <https://github.com/FreeCAD/FreeCAD>.
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
-   There is a very good Forum post about the old way of translation, but it is in German. See <http://forum.freecadweb.org/viewtopic.php?f=13&t=19496&start=60#p152655>

## Preparing your own modules/applications for translation 

### Prerequisites

To localise your application module your need to helpers that come with *Qt*. You can download them from the [Trolltech-Website](http://www.trolltech.com/products/qt/downloads), but they are also contained in the [LibPack](Third_Party_Libraries.md):

qmake: Generates project files
lupdate: Extracts or updates the original texts in your project by scanning the source code
Qt-Linguist: The *Qt-Linguist* is very easy to use and helps you translating with nice features like a phrase book for common sentences.

### Project Setup 

To start the localisation of your project go to the GUI-Part of you module and type on the command line:


```python
qmake -project
```

This scans your project directory for files containing text strings and creates a project file like the following example:


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

You can manually add files here. The section TRANSLATIONS contains a list of files with the translation for each language. In the above example *MyMod\_de.ts* is the german translation.

Now you need to run lupdate to extract all string literals in your GUI. Running lupdate after changes in the source code is allways safe since it never deletes strings from your translations files. It only adds new strings.

Now you need to add the .ts-files to your VisualStudio project. Specifiy the following custom build method for them:


```python
 python ..\..\..\Tools\qembed.py "$(InputDir)\$(InputName).ts"
                 "$(InputDir)\$(InputName).h" "$(InputName)"
```

Note: Enter this in one command line, the line break is only for layout purpose.

By compiling the Gui.cpp*. In our example this would be *AppMyModGui.cpp*. There you add the line


```python
new Gui::LanguageProducer("Deutsch", <Modul>_de_h_data, <Modul>_de_h_len);
```

to publish your translation in the application.

### Setting up python files for translation 

To ease localization for the py files you can use the tool \"pylupdate4\" which accepts one or more py files. With the -ts option you can prepare/update one or more .ts files. For instance to prepare a .ts file for French simply enter into the command line:


```python
pylupdate4 *.py -ts YourModule_fr.ts 
```

the pylupdate tool will scan your .py files for translate() or tr() functions and create a YourModule\_fr.ts file. That file can the be translated with QLinguist and a YourModule\_fr.qm file produced from QLinguist or with the command


```python
lrelease YourModule_fr.ts
```

Beware that the pylupdate4 tool is not very good at recognizing translate() functions, they need to be formatted very specifically ( see the Draft module files for examples). Inside your file, you can then setup a translator like this (after loading your QApplication but BEFORE creating any qt widget):


```python
translator = QtCore.QTranslator()
translator.load("YourModule_"+languages[ln])
QtGui.QApplication.installTranslator(translator)
```

Optionally, you can also create the file XML Draft.qrc with this content:


```python
<RCC>
<qresource prefix="/translations" > 
<file>Draft_fr.qm</file> 
</qresource> 
</RCC> 
```

and running pyrcc4 Draft.qrc -o qrc\_Draft.py creates a big Python containing all resources. BTW this approach also works to put icon files in one resource file


{{docnav
|[Branding](Branding.md)
|[Extra python module](Extra_python_modules.md)
}}


 

[Category:Developer Documentation](Category:Developer_Documentation.md)

---
[documentation index](../README.md) > [Developer Documentation](Category:Developer Documentation.md) > Localization Older Methods/de
