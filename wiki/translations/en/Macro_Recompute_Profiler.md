# Macro Recompute Profiler/en
{{Macro
|Name=Macro Recompute Profiler
|icone=Macro_Recompute_Profiler.png
|Description=This macro is to help you find, what features cause long delays in updates to the project. It performs a recompute, measuring the time it takes to recompute each feature.
|Author=DeepSOIC
|Version=0.1
|Date=2017-04-03
|FCVersion=0.17.10644 and above
|Download=[https://www.freecadweb.org/wiki/images/c/ca/Macro_Recompute_Profiler.png ToolBar Icon]
}}

## Description

This macro is to help you find, what features cause long delays in updates to the project. It performs a recompute, measuring the time it takes to recompute each feature.

## Usage

This macro requires FreeCAD no less than 0.17.10644

Save the macro to a file.

1\. Open your project

2\. Right-click an object in model tree, pick \"Mark to recompute\"

3\. Run this macro.

A progress bar will appear. As each object is recomputed, a line is printed to Report View, containing the time and the label of the object. If any object fails to recompute, the macro will display an error message and terminate the process.

## Macro

ToolBar Icon ![](images/Macro_Recompute_Profiler.png )

**RecomputeProfiler.FCMacro**


{{MacroCode|code=
__Title__="Macro Recompute Profiler"
__Author__ = "DeepSOIC"
__Version__ = "0.1"
__Date__    = "03.04.2017"

__Comment__ = "Measures time it takes to recmpute features in a project"
__Wiki__ = "https://www.freecadweb.org/wiki/index.php?title=Macro_Recompute_Profiler"
__Help__ = "Right-click an object, and pick 'Mark to recompute', then run this macro. This will only profile recomputing the subgraph. To profile the whole project, right-click the project in tree view, and pick 'Mark to recompute', then run this macro. Results will be printed to report view."
__Status__ = "experimental"
__Requires__ = "freecad 0.17.10644"
__Communication__ = "https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=3888" 

import FreeCAD as App

import FreeCADGui as Gui

class ExecutionError(Exception):
    pass

class CancelError(Exception):
    pass

def execute(feature):
    feature.recompute()
    if 'Invalid' in feature.State:
        raise ExecutionError("Feature '{label}' failed to recompute".format(label= feature.Label))

def msgbox(title, text):
    from PySide import QtGui
    mb = QtGui.QMessageBox()
    mb.setIcon(mb.Icon.Information)
    mb.setText(text)
    mb.setWindowTitle(title)
    mb.exec_()

def log(string):
    App.Console.PrintWarning(string+"\n")

def getAllDependent(feat_list):
    '''getAllDependent(feat_list): gets all features that depend on features in feat_list, directly or indirectly.
    Returns a set. Features from feat_list are not included, unless there are interdependencies between them.'''

    list_traversing_now = feat_list
    set_of_deps = set()
    list_of_deps = []

    while len(list_traversing_now) > 0:
        list_to_be_traversed_next = []
        for feat in list_traversing_now:
            for dep in feat.InList:
                if not (dep in set_of_deps):
                    set_of_deps.add(dep)
                    list_of_deps.append(dep)
                    list_to_be_traversed_next.append(dep)

        list_traversing_now = list_to_be_traversed_next

    return set_of_deps


def run():
    touched = [obj for obj in App.ActiveDocument.Objects if 'Touched' in obj.State]

    if len(touched) == 0:
        App.ActiveDocument.RecomputesFrozen = True
        msgbox("Macro Recompute Profiler", "Project was switched to suspend recomputes. Please modify an object that triggers a recompute, and run this macro again. The macro will perform a step-by-step recompute, and measure the time it takes to recompute features.")
        return

    log("{n} features are touched".format(n= len(touched)))

    log("Generating execution order...")

    to_be_executed = set.union(getAllDependent(touched), set(touched))
    log("Number of features to execute: {n}".format(n= len(to_be_executed)))

    exec_list = []
    for obj in App.ActiveDocument.TopologicalSortedObjects[::-1]:
        if obj in to_be_executed:
            exec_list.append(obj)
    assert(len(exec_list) == len(to_be_executed))
    n = len(exec_list)

    log("Execution order:")
    for obj in exec_list:
        log("    "+obj.Label)


    import PySide
    progress = PySide.QtGui.QProgressDialog(u"Preparing to recompute....", u"Abort", 0, n+1)
    progress.setModal(True)
    progress.show()try:
        log("Recomputing... (time in seconds, label)")
        import time
        for obj in exec_list:
            progress.setValue(progress.value()+1)
            progress.setLabelText("Recomputing {feature}...".format(feature= obj.Label))
            if progress.wasCanceled():
                raise CancelError()

            time_start = time.time()
            try:
                execute(obj)
            finally:
                exec_time = time.time()-time_start
                log("\t{time}\t{label}".format(time= exec_time, label= obj.Label))

        progress.setValue(n+1)
        msgbox("Macro Recompute Profiler", "Recompute completed. Results are in report view.")

        for obj in exec_list:
            obj.purgeTouched()

    except Exception as err:
        msgbox("Macro Recompute Profiler", "An error occured: {err}".format(err= str(err)))
    finally:
        progress.hide()
        App.ActiveDocument.RecomputesFrozen = False

run()
}}

## Post-processing results 

The output of the macro will be interleaved with general messages produced by recomputing features. It generally looks like this:


{{code|code=
Recomputing... (time in seconds, label)
Sketcher::setUpSketch()-T:0
Sketcher::Solve()-DogLeg-T:0
    0.00999999046326    Sketch - master section
    0.0199999809265 Clone of Sketch - master section (2D)001
Sketcher::setUpSketch()-T:0
Sketcher::Solve()-DogLeg-T:0
    0.00999999046326    Sketch013
Sketcher::setUpSketch()-T:0
Sketcher::Solve()-DogLeg-T:0
    0.00999999046326    Sketch011
    0.0 Clone of Sketch - master section (2D)
Sketcher::setUpSketch()-T:0
Sketcher::Solve()-DogLeg-T:0
    0.0 Sketch008
    0.130000114441  LinearArray
Sketcher::setUpSketch()-T:0
Sketcher::Solve()-DogLeg-T:0
...
}}

The result lines have an easy signature to separate them off: they start with a tab. So, if you copy-paste the whole chunk to a spreadsheet program, generic messages will end up in column 1, while the results are in columns 2 and 3. So, you can sort by column 2, to get a nice table like that:


{{code|code=
0.59100008  Slice
0.352999926 Populate LinearArray with Compound
0.160000086 CompoundFilter
0.138999939 Cut
0.130000114 LinearArray
0.108999968 Fusion
0.069999933 Moved CompoundFilter
0.067000151 Module - spokes
0.029999971 Sweep
0.019999981 Clone of Sketch - master section (2D)001
0.010999918 ArrayFilter003
...
}}

(For MS-Excel, pasting right after copying text from report view doesn\'t split it into columns, don\'t know why\... pasting the text to Notepad and re-copying it from Notepad and pasting to excel helps.)

## FreeCAD version 

This macro requires FreeCAD no less than 0.17.10644, which was the version where App.ActiveDocument.RecomputesFrozen became available. It might be functional with a bit older FreeCAD, but certainly won\'t work with v0.16.

This macro was created using this version of FreeCAD:


```python
OS: Windows 10
Word size of OS: 64-bit
Word size of FreeCAD: 64-bit
Version: 0.17.10665 (Git)
Build type: Release
Branch: master
Hash: 47847513a85ff6615774ef628230f79e37471daf
Python version: 2.7.8
Qt version: 4.8.7
Coin version: 4.0.0a
OCC version: 7.0.0
```



---
![](images/Button_right.svg) [documentation index](../README.md) > Macro Recompute Profiler/en
