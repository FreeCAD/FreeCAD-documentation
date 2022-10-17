# Drawing Documentation/en
This page documents jcc242\'s understanding of the Drawing module. It includes files and features that he is currently working on and may not yet be in the master branch. The source for those files is on [his Github](https   *//github.com/jcc242/FreeCAD), but be careful as that is very unstable!

## Base (Mod/Drawing) 

### gdtsvg.py

Python script that generates svg snippets for things such as gd&t symbols, dimension symbols, and basic svg elements such as lines, circles, and paths.

It has several support files that don\'t really do much. Run DrawingTest.py to create a bunch of svg icons in the icon directory that previews various icons in the gdtsvg.py file. settingslist.py and dimesettings, and convert.py are all deprecated from older settings methods and should probably be removed as the Drawing branch approaches merging into master.

### DrawingAlgos.py

Creates svg lines from a list of vertices, supports both hidden and visible edges. Should probably be merged with gdtsvg.py as that file matures.

#### createSVG

Accepts part as an argument, projects the part into lines from the Drawing.project object and then draws creates the svg for each line.

## App

Contains the backend side of the drawing module.

### AppDrawing.cpp

Initializes the various namespaces and modules and stuff used in the drawing module. Will throw an error if it cannot load the Part module.

### DrawingExport.cpp

Two classes   * SVGOutput and DXFOutput. They both contain methods to put out the code in their respective language. Typically require an object of the appropriate typedef, and sometimes some additional identifier information.

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

Just #include \"PreCompiled.h\"

### ProjectionAlgos.cpp

The constructor just runs the execute() method to update it\'s stuff

invertY   * since SVG does its y-axis backwards to every other coordinate system in the world, we must invert it when converting from a FreeCAD part to an SVG projection for the Drawing view.

getSVG   * fetches the SVG code from the DrawingExport stuff. Formats depending on type of line (hidden or not and some other stuff I need to figure out).

getDXF   * same as getSVG except for DXF format.

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

Takes the input from the TaskOrthoViews gui and does stuff with it. Uses the single inheritance method talked about [on the qt website](http   *//doc.qt.digia.com/qt/designer-using-a-ui-file.html).

### ViewProviderPage.cpp

Constructor adds some properties for the view stuff. Destructor does nothing. Attaches something (attaches what? attaches the view to the page?) sets and gets display modes (what are display modes? what do they do and what are possible options?) Does something about updating some kind of data has a context menu that says \"Show drawing\", figure out what this means Has a thing for double clicking to select the view (I think?)

showDrawingView seems to do some work on settings things up   * gets the current document, sets the window icon and title, adds it to the main window (of FreeCAD?)

### ViewProviderView.cpp

Doesn\'t seem to do much, though I am sure it is important.

### Workbench.cpp

Adds the icons to the toolbars and stuff.

# Workflow

## Program Flow 

CanvasView is the actual QGraphicsScene object and DrawingView processes a list of FeatureView that are linked by reference in /App/FeatureViewPage. DrawingView then chooses the appropriate QGraphicsItem class (QGraphicsItemViewPart or QGraphicsItemViewDimension) and then calls a function in CanvasView to create this and add it to the scene.

## Adding commands to the Drawing Workbench 

4 simple steps   *

1.  Add a class to Command.cpp. Follow the others for an example of the formatting.
2.  Add a title, icon, tooltip, etc., again, follow the existing classes in command.cpp
3.  Add your class to the bottom of Command.cpp
4.  Add your information to Workbench.cpp, this will tell FreeCAD/Drawing module where to place the icons defined in command.cpp in the actual freecad interface (the toolbars, dropdowns, etc.)

{{Drawing Tools navi}} 

[Category   *Developer_Documentation](Category_Developer_Documentation.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Drawing](Category_Drawing.md) > Drawing Documentation/en
