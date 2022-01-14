# Drawing Documentation/ro
Această pagină documentează înțelegerea de către jcc242 a modulului Desen. Acesta include fișiere și caracteristici pe care le lucrează în prezent și este posibil să nu fie încă în ramura master. Sursa pentru aceste fișiere este pe [lui Github](https://github.com/jcc242/FreeCAD), dar aveți grijă, deoarece este foarte instabilă!

## Baza (Mod/Drawing) 

### gdtsvg.py

Python script care generează svg snippets pentru lucruri care sunt simboluri gd&t , simboluri de cotă, și elemente de bază svg ca linii, cercuri și traiectorii.

Are mai multe fișiere de suport care nu fac prea mult. Rulați DrawingTest.py pentru a crea o mulțime de pictograme svg în directorul de pictograme care previzualizează diverse pictograme din fișierul gdtsvg.py. settingslist.py și dimesettings și convert.py sunt toate în curs de deprecire/abandonare din metodele de setare mai vechi și ar trebui să fie eliminate, probabil, când se apropie ramura Drawing va atinge nivelul corespunzător.

### DrawingAlgos.py

Creates svg lines from a list of vertices, supports both hidden and visible edges. Should probably be merged with gdtsvg.py as that file matures.

#### createSVG

Accepts part as an argument, projects the part into lines from the Drawing.project object and then draws creates the svg for each line.

## App

Contains the backend side of the drawing module.

### AppDrawing.cpp

Initializes the various namespaces and modules and stuff used in the drawing module. Will throw an error if it cannot load the Part module.

### DrawingExport.cpp

Two classes: SVGOutput and DXFOutput. They both contain methods to put out the code in their respective language. Typically require an object of the appropriate typedef, and sometimes some additional identifier information.

### FeatureClip.cpp

Callback (?) methods for the feature clipping gui, so it would seem. Called alone it will create the clip path, if ShowFrame.getValue is TRUE set it will show the frame border as well.

### FeaturePage.cpp

Manages the views.

onChanged() for doing stuff when properties get changed.

execute() for recalculating a feature view, or so it claims. It seems to have stuff for checking for editable texts and saving drawings. Need to investigate further.

getEditableTextsFromTemplate() for retrieving text that can be edited by FreeCAD from an SVG file.

### FeatureProjection.cpp

Flattens object to a 2D image?

### FeatureView.cpp

Defines the properties for views.

### FeatureViewAnnotation.cpp

Defines properties for annotations (right now just text), has an execute method to update the text if changed/moved.

### FeatureViewPart.cpp

Constructor to add properties. Gets appearance stuff for projected parts.

### PageGroup.cpp

Just adds a property for a list of pages, does not much else.

### Precompiled.cppp

Just \#include \"PreCompiled.h\"

### ProjectionAlgos.cpp

The constructor just runs the execute() method to update it\'s stuff

invertY: since SVG does its y-axis backwards to every other coordinate system in the world, we must invert it when converting from a FreeCAD part to an SVG projection for the Drawing view.

getSVG: fetches the SVG code from the DrawingExport stuff. Formats depending on type of line (hidden or not and some other stuff I need to figure out).

getDXF: same as getSVG except for DXF format.

## Gui

### AppDrawingGui.cpp

Initializes the drawing gui.

### AppDrawingGuiPy.cpp

Provides opening, importing, and exporting interfaces? Looks like it is python accessible.

### Command.cpp

Handles commands (from the toolbar?) such as creating new drawings and stuff. It looks like this handles QT calls from clicking the button to whatever command it needs to go to e.g. clicking the CmdDrawingOrthoViews button will show the Ortho views gui in the task dialog spot.

### DrawingView.cpp

Does a bunch of qt gui stuff, need to read more on it.

### TaskDialog.cpp

Creates the task dialog thing on the side and probably switches to it from the tree view, as appropriate.

### TaskOrthoViews.cpp

Creates the task dialog for placing the orthographic views!

Does a lot of the calculations for where to position stuff (automatic calculations as well, it seems).

Takes the input from the TaskOrthoViews gui and does stuff with it. Uses the single inheritance method talked about [on the qt website](http://doc.qt.digia.com/qt/designer-using-a-ui-file.html).

### ViewProviderPage.cpp

Constructor adds some properties for the view stuff. Destructor does nothing. Attaches something (attaches what? attaches the view to the page?) sets and gets display modes (what are display modes? what do they do and what are possible options?) Does something about updating some kind of data has a context menu that says \"Show drawing\", figure out what this means Has a thing for double clicking to select the view (I think?)

showDrawingView seems to do some work on settings things up: gets the current document, sets the window icon and title, adds it to the main window (of FreeCAD?)

### ViewProviderView.cpp

Doesn\'t seem to do much, though I am sure it is important.

### Workbench.cpp

Adds the icons to the toolbars and stuff.

# Workflow

## Program Flow 

CanvasView is the actual QGraphicsScene object and DrawingView processes a list of FeatureView that are linked by reference in /App/FeatureViewPage. DrawingView then chooses the appropriate QGraphicsItem class (QGraphicsItemViewPart or QGraphicsItemViewDimension) and then calls a function in CanvasView to create this and add it to the scene.

## Adăugarea de comenzi la Drawing Workbench 

4 pași simpli:

1.  Adăugați o clasă la Command.cpp. Urmați-i pe ceilalți pentru un exemplu de formatare.
2.  Adăugați din nou un titlu, o pictogramă, o sugestie, etc., urmați clasele existente în command.cpp
3.  Adăugați clasa în partea de jos a Command.cpp
4.  Adăugați informațiile dvs. la Workbench.cpp, acest lucru va indica modulului FreeCAD / Drawing unde să plasați pictogramele definite în command.cpp în interfața reală freecad (barele de instrumente, dropdown-urile etc.)

{{Drawing Tools navi}} 

[<img src="images/Property.png" style="width:16px"> Developer\_Documentation](Category_Developer_Documentation.md)

---
[documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Drawing](Drawing_Workbench.md) > Drawing Documentation/ro
