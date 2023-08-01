---
- TutorialInfo:   Topic:Kinematic controller created with Python
   Level:Basic skills of Python are helpful
   FCVersion:0.20 and later
   Time:1 hour
   Author:[FBXL5](User_FBXL5.md)
---

# Tutorial KinematicController/en





## Introduction

This tutorial describes how to generate a simple kinematic controller to use with assemblies created with the [Assembly3 Workbench](Assembly3_Workbench.md) out of some lines of Python code.

Any text editor can be used to code. My choice is Atom, but FreeCAD\'s built-in editor works well, too.

The following code examples can be copied and pasted into an empty text file and then saved under a name of your choice as a ***.py** or ***.FCMacro** file.

## Macro sections 

### Basic structure 


```python
#! python
# -*- coding: utf-8 -*-
# (c) 2022 Your name LGPL

def main():
    pass

if __name__ == "__main__":
    # This will be true only if the file is "executed"
    # but not if imported as a module
    main()
```

The basic structure consists of a {{Incode|main()}} function and a switch to check if the macro is used as a container for classes, methods etc. or if it is run on its own. Only the second option will start the {{Incode|main()}} function. The function is empty for now.

### Find driving constraints 

The driving constraints are objects within a FreeCAD document. They need to be marked so that they can be found.

For this controller the suffix {{Incode|"Driver"}} has to be attached to the label of a driving constraint. It may be separated by a {{Incode|"."}} or {{Incode|"-"}} for clarity, as we will only check if the label ends with {{Incode|"Driver"}}.

A function that receives a document object and returns a list of driving constraints (the names in this case) will do the job.


```python
def findTheDrivingConstraints(document_object):
    # search through the Objects and find the driving constraint
    driver_list = []
    for each in document_object.Objects:
        if each.Label.endswith("Driver"):
            driving_constraint = each.Name
            driver_list.append(driving_constraint)
    return driver_list
```

The {{Incode|main()}} function loads the active document into the variable {{Incode|kin_doc}} and then calls the function {{Incode|findTheDrivingConstraints()}} and hands over the content of {{Incode|kin_doc}}. The returned list is loaded into {{Incode|drivers}} which is then checked to contain at least one item. If that is the case the list is finally printed to the [Report view](Report_view.md).


```python
def main():
    kin_doc = App.ActiveDocument # Kinematic Document
    drivers = findTheDrivingConstraints(kin_doc)
    if len(drivers) < 1:
        print("No driver found!")
    else:
        print(drivers)
```


<div class="mw-collapsible mw-collapsed">

**The macro so far\...**


<div class="mw-collapsible-content">


```python
#! python
# -*- coding: utf-8 -*-
# (c) 2021 Your name LGPL

def findTheDrivingConstraints(document_object):
    # search through the Objects and find the driving constraint
    driver_list = []
    for each in document_object.Objects:
        if each.Label.endswith("Driver"):
            driving_constraint = each.Name
            driver_list.append(driving_constraint)
    return driver_list

def main():
    kin_doc = App.ActiveDocument # Kinematic Document
    drivers = findTheDrivingConstraints(kin_doc)
    if len(drivers) < 1:
        print("No driver found!")
    else:
        print(drivers)

if __name__ == "__main__":
    # This will be true only if the file is "executed"
    # but not if imported as a module
    main()
```


</div>


</div>


{{Top}}

### Control panel 

The control panel is built from Qt widgets, one main window containing several input/output widgets.

Each widget has to be imported before it can be used, but they can be imported as a single set. The import line is placed near the top of the file.

#### Main window 

For the main window the import line looks like this:


```python
from PySide2.QtWidgets import (QDialog)
```

The main window called {{Incode|ControlPanel}} is a class object instantiated from the {{Incode|QDialog}} widget.

It has two init methods. {{Incode|__init__()}} initializes the new class object, handles incoming arguments, and starts {{Incode|initUI()}} which manages all widgets within the main window.


```python
class ControlPanel(QDialog):
    """
    docstring for ControlPanel.
    """
    def __init__(self, document, actuator):
        super(ControlPanel, self).__init__()
        self.initUI(document, actuator)

    def initUI(self, document, actuator):
        # Setting up class parameters
        # the window has 640 x 480 pixels and is centered by default
        # now make the window visible
        self.show()
```

To launch a single control panel an instance, called {{Incode|panel}}, of this class will be created with {{Incode|kin_doc}} (the document object) and {{Incode|drivers[0]}} (the first in the list of driving constraints) transferred to this instance. Finally the {{Incode|exec_()}} method of the class opens the dialog window.


```python
panel = ControlPanel(kin_doc, drivers[0])
panel.exec_()
```

To handle more than one driver, we have to check the drivers list and create an instance for each item in the list and transfer the current item.


```python
panel_list = []
for each_driver in drivers:
    panel = ControlPanel(kin_doc, each_driver)
    panel_list.append(panel)
panel.exec_()
```

These lines replace the {{Incode|print()}} command in the else branch of the {{Incode|main()}} function.

Note: Collecting a {{Incode|panel_list}} allows us to launch all panels at once. (I cannot explain this behaviour yet\...)

Running the macro will display a clean empty dialog window waiting for widgets:

<img alt="An empty dialog window" src=images/Tutorial_KinCon-01.png  style="width:300px;">


<div class="mw-collapsible mw-collapsed">

**And the macro so far\...**


<div class="mw-collapsible-content">


```python
#! python
# -*- coding: utf-8 -*-
# (c) 2021 Your name LGPL

# imports and constants
from PySide2.QtWidgets import (QDialog)

class ControlPanel(QDialog):
    """
    docstring for ControlPanel.
    """
    def __init__(self, document, actuator):
        super(ControlPanel, self).__init__()
        self.initUI(document, actuator)

    def initUI(self, document, actuator):
        # Setting up class parameters
        # the window has 640 x 480 pixels and is centered by default
        # now make the window visible
        self.show()


def findTheDrivingConstraints(document_object):
    # search through the Objects and find the driving constraint
    driver_list = []
    for each in document_object.Objects:
        if each.Label.endswith("Driver"):
            driving_constraint = each.Name
            driver_list.append(driving_constraint)
    return driver_list

def main():
    kin_doc = App.ActiveDocument # Kinematic Document
    drivers = findTheDrivingConstraints(kin_doc)
    if len(drivers) < 1:
        print("No driver found!")
    else:
        panel_list = []
        for each_driver in drivers:
            panel = ControlPanel(kin_doc, each_driver)
            panel_list.append(panel)
        panel.exec_()

if __name__ == "__main__":
    # This will be true only if the file is "executed"
    # but not if imported as a module
    main()
```


</div>


</div>


{{Top}}

#### Setting parameters 

Now it is time to fill the {{Incode|initUI()}} method:


```python
...
    def initUI(self, document, actuator):
        # Setting up class parameters
        self.actuator = document.getObject(actuator)
        self.driver_type = self.getDriverType(self.actuator)
        # the window has 640 x 480 pixels and is centered by default
        # now make the window visible
        self.show()
...
```


{{Incode|self.actuator}}

represents the driving constraint and {{Incode|self.driver_type}} stores a keyword for its type. The latter is used to choose the correct property with each constraint.

##### Method getDriverType() 

For later use we need the driver type (Angle, Distance, Length) and so a {{Incode|getDriverType()}} method has to be defined:


```python
...
    def getDriverType(self, constraint):
        ANGLE_CONSTRAINTS = [
            "Angle",
            "PlaneCoincident",
            "AxialAlignment",
            "PlaneAlignment"
            ]
        DISTANCE_CONSTRAINTS = [
            "PointDistance",
            "PointsDistance"
            ]
        if constraint.ConstraintType in ANGLE_CONSTRAINTS:
            return "Angle"
        elif constraint.ConstraintType in DISTANCE_CONSTRAINTS:
            return "Distance"
        else:
            return "Length"
...
```

This method checks if the type of the given constraint can be found in one of the lists, and returns which kind of dimension has to be controlled.

It is assumed that in the kinematic document the driver is marked correctly and working if edited manually. In this case there is no need to filter out geometric constraints such as Colinear or PointsCoincidence (but here would be the place to do so\...)

##### Window properties 

The window size is defined by its minimum and maximum dimensions. Using the same values results in a fixed size.

The title shows the driver name and whether its an angle, a distance, or a length. Finally the window is told to stay on top of all windows.


```python
...
        # the window has 640 x 480 pixels and is centered by default
        #- set window dimensions
        self.setMaximumWidth(400)
        self.setMaximumHeight(200)
        self.setMinimumWidth(400)
        self.setMinimumHeight(200)
        self.setWindowTitle(self.actuator.Label + ": " + self.driver_type)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        # now make the window visible
...
```


{{Top}}

#### Setting more parameters 

The next step is to extract the current value of the driver and set the default start and end values depending on the driver type.

A distance cannot be negative and exactly zero puzzles the solver and so the start value is set to 0.001. Angles accept negative values and get symmetric values. (If lengths accept negative values has to be proven finally\...)

The unit suffix must be kept for returning the value to the constraint property in the end. Distances and lengths need values with units.

Dealing with units and displaying values as strings in several widgets requires to convert numbers into strings and back again quite often.

To complete the parameters we set a default number of steps that should be computed when the motion is automated and if the {{Incode|self.sequence}} toggle is set to {{Incode|True}}, a picture will be taken with each step of the motion.


```python
...
        self.steps_value = 10
        self.sequence = False
        if self.driver_type == "Angle":
            self.current_value = self.actuator.Angle
            self.start_value = (self.current_value - 15)
            self.end_value = (self.current_value + 15)
            self.unit_suffix = (" °")
        elif self.driver_type == "Distance":
            self.current_value = float(str(self.actuator.Distance)[:-3])
            self.start_value = 0.001 # Distance must not be <= 0
            self.end_value = (self.current_value + 10)
            self.unit_suffix = (" mm")
        else:
            self.current_value = float(str(self.actuator.Offset)[:-3])
            self.start_value = (self.current_value - 10)
            self.end_value = (self.current_value + 10)
            self.unit_suffix = (" mm")
...
```


{{Top}}

#### Labels

Now three labels are added to display the start, end, and current value.

First the class {{Incode|QLabel}} must be imported i.e. the import list has to be extended like this:


```python
from PySide2.QtWidgets import (QDialog, QLabel)
```

Back in the {{Incode|initUI()}} method we insert:


```python
...
        # create some labels
        self.label_start = QLabel("", self)
        self.label_start.setFont("osifont") # set to a non-proportional font
        self.label_start.setText(str(round(self.start_value, 1)) + self.unit_suffix)
        self.label_start.setGeometry(QtCore.QRect(30, 15, 60, 25))

        self.label_end = QLabel("", self)
        self.label_end.setFont("osifont")
        self.label_end.setText(str(round(self.end_value, 1)) + self.unit_suffix)
        self.label_end.setGeometry(QtCore.QRect(320, 15, 60, 25))

        self.label_current = QLabel("", self)
        self.label_current.setFont("osifont")
        self.label_current.setText("Current value: " + str(round(self.current_value, 1)) + self.unit_suffix)
        self.label_current.setGeometry(QtCore.QRect(130, 15, 150, 25))
...
```

The placement is done with the inherited {{Incode|setGeometry()}} method. In this case the description of a rectangle is used (X position, Y position, width, height).

The first and third lines could be combined, but it is not recommended for clarity reasons:


```python
self.label_end = QLabel((str(round(self.end_value, 1)) + self.unit_suffix), self)
```

Running the macro with a kinematic assembly document would create a dialog window like this:

<img alt="A dialog window displaying start value, current Value, and end value" src=images/Tutorial_KinCon-02.png  style="width:300px;"> 
*The dialog window displaying the constraint label and driver type in the title, and the start value, current value and end value on the first line in the main area*


<div class="mw-collapsible mw-collapsed">

**And the macro so far\...**


<div class="mw-collapsible-content">


```python
#! python
# -*- coding: utf-8 -*-
# (c) 2021 Your name LGPL

# imports and constants
from PySide2.QtWidgets import (QDialog, QLabel)

class ControlPanel(QDialog):
    """
    docstring for ControlPanel.
    """
    def __init__(self, document, actuator):
        super(ControlPanel, self).__init__()
        self.initUI(document, actuator)

    def initUI(self, document, actuator):
        # Setting up class parameters
        self.actuator = document.getObject(actuator)
        self.driver_type = self.getDriverType(self.actuator)
        self.steps_value = 10
        self.sequence = False
        if self.driver_type == "Angle":
            self.current_value = self.actuator.Angle
            self.start_value = (self.current_value - 15)
            self.end_value = (self.current_value + 15)
            self.unit_suffix = (" °")
        elif self.driver_type == "Distance":
            self.current_value = float(str(self.actuator.Distance)[:-3])
            self.start_value = 0.001 # Distance must not be <= 0
            self.end_value = (self.current_value + 10)
            self.unit_suffix = (" mm")
        else:
            self.current_value = float(str(self.actuator.Offset)[:-3])
            self.start_value = (self.current_value - 10)
            self.end_value = (self.current_value + 10)
            self.unit_suffix = (" mm")

        # the window has 640 x 480 pixels and is centered by default
        #- set window dimensions
        self.setMaximumWidth(400)
        self.setMaximumHeight(200)
        self.setMinimumWidth(400)
        self.setMinimumHeight(200)
        self.setWindowTitle(self.actuator.Label + ": " + self.driver_type)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        # create some labels
        self.label_start = QLabel("", self)
        self.label_start.setFont("osifont") # set to a non-proportional font
        self.label_start.setText(str(round(self.start_value, 1)) + self.unit_suffix)
        self.label_start.setGeometry(QtCore.QRect(30, 15, 60, 25))

        self.label_end = QLabel("", self)
        self.label_end.setFont("osifont")
        self.label_end.setText(str(round(self.end_value, 1)) + self.unit_suffix)
        self.label_end.setGeometry(QtCore.QRect(320, 15, 60, 25))

        self.label_current = QLabel("", self)
        self.label_current.setFont("osifont")
        self.label_current.setText("Current value: " + str(round(self.current_value, 1)) + self.unit_suffix)
        self.label_current.setGeometry(QtCore.QRect(130, 15, 150, 25))

        # now make the window visible
        self.show()

    def getDriverType(self, constraint):
        ANGLE_CONSTRAINTS = [
            "Angle",
            "PlaneCoincident",
            "AxialAlignment",
            "PlaneAlignment"
            ]
        DISTANCE_CONSTRAINTS = [
            "PointDistance",
            "PointsDistance"
            ]
        if constraint.ConstraintType in ANGLE_CONSTRAINTS:
            return "Angle"
        elif constraint.ConstraintType in DISTANCE_CONSTRAINTS:
            return "Distance"
        else:
            return "Length"

# End of ControlPanel()
# Main section below:

def findTheDrivingConstraints(document_object):
    # search through the Objects and find the driving constraint
    driver_list = []
    for each in document_object.Objects:
        if each.Label.endswith("Driver"):
            driving_constraint = each.Name
            driver_list.append(driving_constraint)
    return driver_list

def main():
    kin_doc = App.ActiveDocument # Kinematic Document
    drivers = findTheDrivingConstraints(kin_doc)
    if len(drivers) < 1:
        print("No driver found!")
    else:
        panel_list = []
        for each_driver in drivers:
            panel = ControlPanel(kin_doc, each_driver)
            panel_list.append(panel)
        panel.exec_()

if __name__ == "__main__":
    # This will be true only if the file is "executed"
    # but not if imported as a module
    main()
```


</div>


</div>


{{Top}}

#### Slider

To change the current value to any number between start and end value a slider widget would fit.

First the class {{Incode|QSlider}} must be imported i.e. the import list has to be extended like this:


```python
from PySide2.QtWidgets import (QDialog, QLabel, QSlider)
```

Back in the {{Incode|initUI()}} method and right after the labels section we insert:


```python
...
        # Horizontal slider
        self.actuator_slider = QSlider(self)                             # create horizontalSlider
        self.actuator_slider.setOrientation(QtCore.Qt.Horizontal)        # orientation horizontal
        self.actuator_slider.setGeometry(QtCore.QRect(30, 50, 330, 25))  # position coordinates
        self.actuator_slider.setObjectName("horizontalSlider")           # object name
        self.actuator_slider.setInvertedAppearance(False)                # default: right to left
        self.actuator_slider.setRange(0, 100)                            # default: (0, 99)
        self.actuator_slider.setValue(self.current_value / self.stepRatio())
        self.actuator_slider.valueChanged.connect(self.onActuatorSlider)
...
```

The slider button is placed with the {{Incode|setValue()}} method. Its value has to be calculated from the current value and a step ratio. The ratio has to be calculated whenever a start or end value is changed and so we insert another method after the {{Incode|getDriverType()}} method.

To work with a ratio instead of altering the slider\'s min and max values has the advantage of a finer resolution for small values.


```python
...
    def stepRatio(self):
        ratio = (self.end_value - self.start_value) / 100
        return ratio
...
```

And after this one comes another method defining what to do when the slider position or the slider value changes. The {{Incode|onActuatorSlider()}} method is called by the {{Incode|connect()}} method which also hands over the slider value as an argument.

It recalculates the current value from the slider position, rewrites the text of the label {{Incode|self.label_current}} and changes the constraint property according to the driver type.

Running the command {{Incode|"asm3CmdQuickSolve"}} starts the solver to rearrange the assembly parts with the altered value.


```python
...
    def onActuatorSlider(self, slider_value):
        self.current_value = slider_value * self.stepRatio() + self.start_value
        if self.driver_type == "Angle":
            self.actuator.Angle = self.current_value
        elif self.driver_type == "Distance":
            self.actuator.Distance = self.current_value
        else:
            self.actuator.Offset = self.current_value
        self.label_current.setText("Current value: " + str(round(self.current_value, 1)) + self.unit_suffix)
        Gui.runCommand("asm3CmdQuickSolve", 0)
...
```

The dialog window with the slider should look like this and is ready to control a motion:

<img alt="Two dialog windows with a slider" src=images/Tutorial_KinCon-03.png  style="width:300px;"> 
*Dialog windows with the added slider, one for an Angle driver and one for a Distance driver*

We can start a dialog window for any opened document, they won\'t interfere with each other. {{Top}}

#### Text entry fields 

To set the start and end value we use a line edit widget.

First the class {{Incode|QLineEdit}} must be imported i.e. the import list has to be extended like this:


```python
from PySide2.QtWidgets import (QDialog, QLabel, QSlider, QLineEdit)
```

Back in the {{Incode|initUI()}} method and between the labels and the slider sections we insert:


```python
...
        # text input field - Start value
        self.entry_start = QLineEdit(self)
        self.entry_start.setText(str(round(self.start_value, 1)))
        self.entry_start.setGeometry(QtCore.QRect(30, 80, 50, 25))
        self.entry_start.textChanged[str].connect(self.onEntryStart)

        # text input field - End value
        self.entry_end = QLineEdit(self)
        self.entry_end.setText(str(round(self.end_value, 1)))
        self.entry_end.setGeometry(QtCore.QRect(320, 80, 50, 25))
        self.entry_end.textChanged[str].connect(self.onEntryEnd)
...
```

The entry fields display the default start and end values. They are not complete until we add the methods to deal with altered entries. This will be done by the methods {{Incode|self.onEntryStart()}} and {{Incode|self.onEntryEnd()}} that are inserted between the {{Incode|self.stepRatio()}} and the {{Incode|self.onActuatorSlider()}} methods.


```python
...
    def onEntryStart(self, new_start):
        self.start_value = float(new_start)
        self.label_start.setText(str(round(self.start_value, 1)) + self.unit_suffix)
        # Update the slider
        slider_value = ((self.current_value - self.start_value) / self.stepRatio())
        self.actuator_slider.setValue(slider_value)

    def onEntryEnd(self, new_end):
        self.end_value = float(new_end)
        self.label_end.setText(str(round(self.end_value, 1)) + self.unit_suffix)
        # Update the slider
        slider_value = ((self.current_value - self.start_value) / self.stepRatio())
        self.actuator_slider.setValue(slider_value)
...
```

Both convert the received string value to a floating point number and change either {{Incode|self.start_value}} or {{Incode|self.end_value}} and the corresponding label accordingly. After that the slider value is updated.

The dialog window with text entry fields should look like this and is ready to change the range of a motion:

<img alt="Two dialog windows with line edit fields" src=images/Tutorial_KinCon-04.png  style="width:300px;"> 
*Dialog windows with line edit fields, again for an angle and a distance driver*


<div class="mw-collapsible mw-collapsed">

**And the macro so far\...**


<div class="mw-collapsible-content">


```python
#! python
# -*- coding: utf-8 -*-
# (c) 2021 Your name LGPL

# imports and constants
from PySide2.QtWidgets import (QDialog, QLabel, QSlider, QLineEdit)

class ControlPanel(QDialog):
    """
    docstring for ControlPanel.
    """
    def __init__(self, document, actuator):
        super(ControlPanel, self).__init__()
        self.initUI(document, actuator)

    def initUI(self, document, actuator):
        # Setting up class parameters
        self.actuator = document.getObject(actuator)
        self.driver_type = self.getDriverType(self.actuator)
        self.steps_value = 10
        self.sequence = False
        if self.driver_type == "Angle":
            self.current_value = self.actuator.Angle
            self.start_value = (self.current_value - 15)
            self.end_value = (self.current_value + 15)
            self.unit_suffix = (" °")
        elif self.driver_type == "Distance":
            self.current_value = float(str(self.actuator.Distance)[:-3])
            self.start_value = 0.001 # Distance must not be <= 0
            self.end_value = (self.current_value + 10)
            self.unit_suffix = (" mm")
        else:
            self.current_value = float(str(self.actuator.Offset)[:-3])
            self.start_value = (self.current_value - 10)
            self.end_value = (self.current_value + 10)
            self.unit_suffix = (" mm")

        # the window has 640 x 480 pixels and is centered by default
        #- set window dimensions
        self.setMaximumWidth(400)
        self.setMaximumHeight(200)
        self.setMinimumWidth(400)
        self.setMinimumHeight(200)
        self.setWindowTitle(self.actuator.Label + ": " + self.driver_type)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        # create some labels
        self.label_start = QLabel("", self)
        self.label_start.setFont("osifont") # set to a non-proportional font
        self.label_start.setText(str(round(self.start_value, 1)) + self.unit_suffix)
        self.label_start.setGeometry(QtCore.QRect(30, 15, 60, 25))

        self.label_end = QLabel("", self)
        self.label_end.setFont("osifont")
        self.label_end.setText(str(round(self.end_value, 1)) + self.unit_suffix)
        self.label_end.setGeometry(QtCore.QRect(320, 15, 60, 25))

        self.label_current = QLabel("", self)
        self.label_current.setFont("osifont")
        self.label_current.setText("Current value: " + str(round(self.current_value, 1)) + self.unit_suffix)
        self.label_current.setGeometry(QtCore.QRect(130, 15, 150, 25))

        # create some input elements

        # text input field - Start value
        self.entry_start = QLineEdit(self)
        self.entry_start.setText(str(round(self.start_value, 1)))
        self.entry_start.setGeometry(QtCore.QRect(30, 80, 50, 25))
        self.entry_start.textChanged[str].connect(self.onEntryStart)

        # text input field - End value
        self.entry_end = QLineEdit(self)
        self.entry_end.setText(str(round(self.end_value, 1)))
        self.entry_end.setGeometry(QtCore.QRect(320, 80, 50, 25))
        self.entry_end.textChanged[str].connect(self.onEntryEnd)

        # Horizontal slider
        self.actuator_slider = QSlider(self)                             # create horizontalSlider
        self.actuator_slider.setOrientation(QtCore.Qt.Horizontal)        # orientation horizontal
        self.actuator_slider.setGeometry(QtCore.QRect(30, 50, 330, 25))  # position coordinates
        self.actuator_slider.setObjectName("horizontalSlider")           # object name
        self.actuator_slider.setInvertedAppearance(False)                # default: right to left
        self.actuator_slider.setRange(0, 100)                            # default: (0, 99)
        self.actuator_slider.setValue(self.current_value / self.stepRatio())
        self.actuator_slider.valueChanged.connect(self.onActuatorSlider)

        # now make the window visible
        self.show()

    def getDriverType(self, constraint):
        ANGLE_CONSTRAINTS = [
            "Angle",
            "PlaneCoincident",
            "AxialAlignment",
            "PlaneAlignment"
            ]
        DISTANCE_CONSTRAINTS = [
            "PointDistance",
            "PointsDistance"
            ]
        if constraint.ConstraintType in ANGLE_CONSTRAINTS:
            return "Angle"
        elif constraint.ConstraintType in DISTANCE_CONSTRAINTS:
            return "Distance"
        else:
            return "Length"

    def stepRatio(self):
        ratio = (self.end_value - self.start_value) / 100
        return ratio

    def onEntryStart(self, new_start):
        self.start_value = float(new_start)
        self.label_start.setText(str(round(self.start_value, 1)) + self.unit_suffix)
        # Update the slider
        slider_value = ((self.current_value - self.start_value) / self.stepRatio())
        self.actuator_slider.setValue(slider_value)

    def onEntryEnd(self, new_end):
        self.end_value = float(new_end)
        self.label_end.setText(str(round(self.end_value, 1)) + self.unit_suffix)
        # Update the slider
        slider_value = ((self.current_value - self.start_value) / self.stepRatio())
        self.actuator_slider.setValue(slider_value)

    def onActuatorSlider(self, slider_value):
        self.current_value = slider_value * self.stepRatio() + self.start_value
        if self.driver_type == "Angle":
            self.actuator.Angle = self.current_value
        elif self.driver_type == "Distance":
            self.actuator.Distance = self.current_value
        else:
            self.actuator.Offset = self.current_value
        self.label_current.setText("Current value: " + str(round(self.current_value, 1)) + self.unit_suffix)
        Gui.runCommand("asm3CmdQuickSolve", 0)
        print(slider_value, self.current_value)

# End of ControlPanel()
# Main section below:

def findTheDrivingConstraints(document_object):
    # search through the Objects and find the driving constraint
    driver_list = []
    for each in document_object.Objects:
        if each.Label.endswith("Driver"):
            driving_constraint = each.Name
            driver_list.append(driving_constraint)
    return driver_list

def main():
    kin_doc = App.ActiveDocument # Kinematic Document
    drivers = findTheDrivingConstraints(kin_doc)
    if len(drivers) < 1:
        print("No driver found!")
    else:
        panel_list = []
        for each_driver in drivers:
            panel = ControlPanel(kin_doc, each_driver)
            panel_list.append(panel)
        panel.exec_()

if __name__ == "__main__":
    # This will be true only if the file is "executed"
    # but not if imported as a module
    main()
```


</div>


</div>


{{Top}}

### Motion

To get the assembly in motion we need:

-   Buttons to trigger motion in the desired direction.
-   An input field to alter the number of steps for faster or smoother motions.
-   A check box to indicate if we want to shoot a sequence of images.

#### Forward and Backward buttons 

To move the assembly parts automatically we need two buttons to trigger the motions, one towards the start position and one towards the end position. These two and a close button will use a {{Incode|QPushButton}} widget.

Small assemblies compute a bit too fast and show jumps instead of a smooth motion. To slow it down we use the {{Incode|sleep()}} method of the {{Incode|time}} module which has to be imported first.

Another import and another widget:


```python
import time
from PySide2.QtWidgets import (QDialog, QLabel, QSlider, QLineEdit, QPushButton)
```

Back in the {{Incode|initUI()}} method we insert the buttons after the slider section:


```python
...
        # forward button
        self.forward_button = QPushButton(">->", self)
        self.forward_button.setGeometry(QtCore.QRect(240, 80, 50, 25))
        self.forward_button.setAutoDefault(False)
        self.forward_button.clicked.connect(self.onForward)
        # backward button
        self.backward_button = QPushButton("<-<", self)
        self.backward_button.setGeometry(QtCore.QRect(100, 80, 50, 25))
        self.backward_button.setAutoDefault(False)
        self.backward_button.clicked.connect(self.onBackward)
        # close button
        self.close_button = QPushButton("Close window", self)
        self.close_button.setGeometry(QtCore.QRect(120, 160, 130, 25))
        self.close_button.setAutoDefault(False)
        self.close_button.clicked.connect(self.onClose)
...
```

The methods dealing with pressed buttons are {{Incode|self.onForward()}}, {{Incode|self.onBackward()}}, and {{Incode|self.onClose()}}. They are inserted after the {{Incode|onActuatorSlider()}} method.


```python
...
    def onForward(self):
        steps_left = self.steps_value
        print(self.steps_value)
        step = ((self.end_value - self.current_value) / steps_left)
        while steps_left > 0:
            self.current_value += step
            slider_value = ((self.current_value - self.start_value) / self.stepRatio())
            self.actuator_slider.setValue(slider_value)
            time.sleep(0.2)
            steps_left -= 1
        self.actuator_slider.setValue(100)

    def onBackward(self):
        steps_left = self.steps_value
        step = ((self.current_value - self.start_value) / steps_left)
        while steps_left > 0:
            self.current_value -= step
            slider_value = ((self.current_value - self.start_value) / self.stepRatio())
            self.actuator_slider.setValue(slider_value)
            time.sleep(0.2)
            steps_left -= 1
        self.actuator_slider.setValue(0)

    def onClose(self):
        self.result = "Closed"
        self.close()
...
```

The method {{Incode|self.onClose()}} invokes the inherited method {{Incode|self.close()}} which just closes the dialog window and thereby ends the macro.

Both {{Incode|self.onForward()}} and {{Incode|self.onBackward()}} count the steps that are left to go to reach the wanted position and calculate the length of a step according to the number of steps. For now we go with the default number of 10 steps.

Each round on the while loop increases/decreases the current value and updates the slider values which triggers {{Incode|onActuatorSlider()}} in the background (see [Slider paragraph](#Slider.md)). After a pause to let the computer provide another updated 3D view, counting down the steps left to go finishes the loop.

With no steps left the slider is set to the first/last slider position, just in case if a rounding error had occurred.

The dialog window with buttons should look like this and can now move the assembly by 10 steps towards the wanted start/end position:

<img alt="Dialog window with buttons" src=images/Tutorial_KinCon-05.png  style="width:300px;"> 
*Dialog window with buttons*


<div class="mw-collapsible mw-collapsed">

**And the macro so far\...**


<div class="mw-collapsible-content">


```python
#! python
# -*- coding: utf-8 -*-
# (c) 2021 Your name LGPL

# imports and constants
import time
from PySide2.QtWidgets import (QDialog, QLabel, QSlider, QLineEdit, QPushButton)

class ControlPanel(QDialog):
    """
    docstring for ControlPanel.
    """
    def __init__(self, document, actuator):
        super(ControlPanel, self).__init__()
        self.initUI(document, actuator)

    def initUI(self, document, actuator):
        # Setting up class parameters
        self.actuator = document.getObject(actuator)
        self.driver_type = self.getDriverType(self.actuator)
        self.steps_value = 10
        self.sequence = False
        if self.driver_type == "Angle":
            self.current_value = self.actuator.Angle
            self.start_value = (self.current_value - 15)
            self.end_value = (self.current_value + 15)
            self.unit_suffix = (" °")
        elif self.driver_type == "Distance":
            self.current_value = float(str(self.actuator.Distance)[:-3])
            self.start_value = 0.001 # Distance must not be <= 0
            self.end_value = (self.current_value + 10)
            self.unit_suffix = (" mm")
        else:
            self.current_value = float(str(self.actuator.Offset)[:-3])
            self.start_value = (self.current_value - 10)
            self.end_value = (self.current_value + 10)
            self.unit_suffix = (" mm")

        # the window has 640 x 480 pixels and is centered by default
        #- set window dimensions
        self.setMaximumWidth(400)
        self.setMaximumHeight(200)
        self.setMinimumWidth(400)
        self.setMinimumHeight(200)
        self.setWindowTitle(self.actuator.Label + ": " + self.driver_type)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        # create some labels
        self.label_start = QLabel("", self)
        self.label_start.setFont("osifont") # set to a non-proportional font
        self.label_start.setText(str(round(self.start_value, 1)) + self.unit_suffix)
        self.label_start.setGeometry(QtCore.QRect(30, 15, 60, 25))

        self.label_end = QLabel("", self)
        self.label_end.setFont("osifont")
        self.label_end.setText(str(round(self.end_value, 1)) + self.unit_suffix)
        self.label_end.setGeometry(QtCore.QRect(320, 15, 60, 25))

        self.label_current = QLabel("", self)
        self.label_current.setFont("osifont")
        self.label_current.setText("Current value: " + str(round(self.current_value, 1)) + self.unit_suffix)
        self.label_current.setGeometry(QtCore.QRect(130, 15, 150, 25))

        # create some input elements

        # text input field - Start value
        self.entry_start = QLineEdit(self)
        self.entry_start.setText(str(round(self.start_value, 1)))
        self.entry_start.setGeometry(QtCore.QRect(30, 80, 50, 25))
        self.entry_start.textChanged[str].connect(self.onEntryStart)

        # text input field - End value
        self.entry_end = QLineEdit(self)
        self.entry_end.setText(str(round(self.end_value, 1)))
        self.entry_end.setGeometry(QtCore.QRect(320, 80, 50, 25))
        self.entry_end.textChanged[str].connect(self.onEntryEnd)

        # Horizontal slider
        self.actuator_slider = QSlider(self)                             # create horizontalSlider
        self.actuator_slider.setOrientation(QtCore.Qt.Horizontal)        # orientation horizontal
        self.actuator_slider.setGeometry(QtCore.QRect(30, 50, 330, 25))  # position coordinates
        self.actuator_slider.setObjectName("horizontalSlider")           # object name
        self.actuator_slider.setInvertedAppearance(False)                # default: right to left
        self.actuator_slider.setRange(0, 100)                            # default: (0, 99)
        self.actuator_slider.setValue(self.current_value / self.stepRatio())
        self.actuator_slider.valueChanged.connect(self.onActuatorSlider)

        # forward button
        self.forward_button = QPushButton(">->", self)
        self.forward_button.setGeometry(QtCore.QRect(240, 80, 50, 25))
        self.forward_button.setAutoDefault(False)
        self.forward_button.clicked.connect(self.onForward)
        # backward button
        self.backward_button = QPushButton("<-<", self)
        self.backward_button.setGeometry(QtCore.QRect(100, 80, 50, 25))
        self.backward_button.setAutoDefault(False)
        self.backward_button.clicked.connect(self.onBackward)
        # close button
        self.close_button = QPushButton("Close window", self)
        self.close_button.setGeometry(QtCore.QRect(120, 160, 130, 25))
        self.close_button.setAutoDefault(False)
        self.close_button.clicked.connect(self.onClose)

        # now make the window visible
        self.show()

    def getDriverType(self, constraint):
        ANGLE_CONSTRAINTS = [
            "Angle",
            "PlaneCoincident",
            "AxialAlignment",
            "PlaneAlignment"
            ]
        DISTANCE_CONSTRAINTS = [
            "PointDistance",
            "PointsDistance"
            ]
        if constraint.ConstraintType in ANGLE_CONSTRAINTS:
            return "Angle"
        elif constraint.ConstraintType in DISTANCE_CONSTRAINTS:
            return "Distance"
        else:
            return "Length"

    def stepRatio(self):
        ratio = (self.end_value - self.start_value) / 100
        return ratio

    def onEntryStart(self, new_start):
        self.start_value = float(new_start)
        self.label_start.setText(str(round(self.start_value, 1)) + self.unit_suffix)
        # Update the slider
        slider_value = ((self.current_value - self.start_value) / self.stepRatio())
        self.actuator_slider.setValue(slider_value)

    def onEntryEnd(self, new_end):
        self.end_value = float(new_end)
        self.label_end.setText(str(round(self.end_value, 1)) + self.unit_suffix)
        # Update the slider
        slider_value = ((self.current_value - self.start_value) / self.stepRatio())
        self.actuator_slider.setValue(slider_value)

    def onActuatorSlider(self, slider_value):
        self.current_value = slider_value * self.stepRatio() + self.start_value
        if self.driver_type == "Angle":
            self.actuator.Angle = self.current_value
        elif self.driver_type == "Distance":
            self.actuator.Distance = self.current_value
        else:
            self.actuator.Offset = self.current_value
        self.label_current.setText("Current value: " + str(round(self.current_value, 1)) + self.unit_suffix)
        FreeCADGui.updateGui() # screen update between steps
        Gui.runCommand("asm3CmdQuickSolve", 0)

    def onForward(self):
        steps_left = self.steps_value
        print(self.steps_value)
        step = ((self.end_value - self.current_value) / steps_left)
        while steps_left > 0:
            self.current_value += step
            slider_value = ((self.current_value - self.start_value) / self.stepRatio())
            self.actuator_slider.setValue(slider_value)
            time.sleep(0.2)
            steps_left -= 1
        self.actuator_slider.setValue(100)

    def onBackward(self):
        steps_left = self.steps_value
        step = ((self.current_value - self.start_value) / steps_left)
        while steps_left > 0:
            self.current_value -= step
            slider_value = ((self.current_value - self.start_value) / self.stepRatio())
            self.actuator_slider.setValue(slider_value)
            time.sleep(0.2)
            steps_left -= 1
        self.actuator_slider.setValue(0)

    def onClose(self):
        self.result = "Closed"
        self.close()

# End of ControlPanel()
# Main section below:

def findTheDrivingConstraints(document_object):
    # search through the Objects and find the driving constraint
    driver_list = []
    for each in document_object.Objects:
        if each.Label.endswith("Driver"):
            driving_constraint = each.Name
            driver_list.append(driving_constraint)
    return driver_list

def main():
    kin_doc = App.ActiveDocument # Kinematic Document
    drivers = findTheDrivingConstraints(kin_doc)
    if len(drivers) < 1:
        print("No driver found!")
    else:
        panel_list = []
        for each_driver in drivers:
            panel = ControlPanel(kin_doc, each_driver)
            panel_list.append(panel)
        panel.exec_()

if __name__ == "__main__":
    # This will be true only if the file is "executed"
    # but not if imported as a module
    main()
```


</div>


</div>


{{Top}}

#### Number of steps 

The default setting is to get a quick impression if the assembly is moving as expected without wasting too much computing time.

If the parts jump rather than move smoothly, or if drivers based on angles tend to cause trouble when the difference between two angles is too large, then both can be fixed by increasing the number of steps.

And so another line edit widget is used to alter the number steps (placed after the existing line edit widgets):


```python
...
        # text input field - number of steps
        self.entry_steps = QLineEdit(self)
        self.entry_steps.setText(str(int(self.steps_value)))
        self.entry_steps.setGeometry(QtCore.QRect(180, 80, 50, 25))
        self.entry_steps.textChanged[str].connect(self.onEntrySteps)
...
```

The related method {{Incode|self.onEntrySteps()}} just fills the parameter {{Incode|self.step_value}} with the entered value. It is inserted after the {{Incode|onEntryEnd()}} method.


```python
...
    def onEntrySteps(self, new_steps):
        self.steps_value = int(new_steps)
...
```

The dialog window able to change the number of steps should look like this:

<img alt="Dialog window with another text entry field" src=images/Tutorial_KinCon-06.png  style="width:300px;"> 
*Dialog window with another text entry field* {{Top}}

#### Image sequence 

When the motion of our assembly meets our expectations, we can take a picture of each step. The resulting sequence of images can be used to create a short gif animation.

To implement this functionality we need a {{Incode|QCheckBox}} widget, and a directory to store the images.

One more import and widget:


```python
import time
from PySide2.QtWidgets import (QDialog, QLabel, QSlider, QLineEdit, QPushButton, QCheckBox)
```

Back in the {{Incode|initUI()}} method we insert the check box after the slider section:


```python
...
        # output check box
        self.output_check = QCheckBox(self)
        self.output_check.setGeometry(QtCore.QRect(40, 120, 300, 25))
        self.output_check.setChecked(False)
        self.output_check.setText("Check to record an image sequence")
        self.output_check.setObjectName("checkBoxOutput")
        self.output_check.clicked.connect(self.onOutputClicked)
...
```

The method {{Incode|onOutputClicked()}} synchronises the parameter {{Incode|self.sequence}} and the display of the check mark.


```python
...
    def onOutputClicked(self):
        if self.sequence == True:
            self.sequence = False
            self.output_check.setChecked(False)
        else:
            self.sequence = True
            self.output_check.setChecked(True)
...
```

To define the output parameters we use the method {{Incode|output()}}:


```python
...
    def output(self, counter):
        if (self.sequence == True):
            image_path = ".../FreeCAD/ScreenShots/Sequence"
            file_tag = ".png"
            height = 640
            width = 480
            background = "Transparent"
            # dealing with leading zeros
            if (counter > 999) or (counter < 0):
                print("Out of Range")
            elif (counter < 10):
                number = "00" + str(counter)
            elif (counter < 100):
                number = "0" + str(counter)
            else:
                number = str(counter)
            # Screen shot
            Gui.activeDocument().activeView().saveImage(image_path + number + file_tag, height, width, background)
...
```

First the image path has to be adapted to your OS; the last part is the image name without current number and file tag. This must be done manually for now.

Then follow file tag to finish the image name, image height and width, and how the background should be filled ({{Incode|"Current"}} (3D view background), {{Incode|"White"}}, {{Incode|"Black"}}, or {{Incode|"Transparent"}}).

To always have a 3 digit number leading zeros have to be prefixed to the counter parameter.

Finally the scripted version of the command <img alt="" src=images/Std_ViewScreenShot.svg  style="width:24px;"> [Std ViewScreenShot](Std_ViewScreenShot.md) is used to take a picture based on the mentioned parameters.

Still no pictures taken!?! No problem, as this method doesn\'t get called yet, and so we need to insert a call in the while loop of {{Incode|onForward()}} and {{Incode|onBackward()}}. Right after {{Incode|time.sleep(0.2)}} we insert this line:


```python
...
            self.output(steps_left)
...
```

Now the macro should be ready to control an assembly and to take pictures for an animated gif.

The final version of the dialog window:

<img alt="Dialog window finished" src=images/Tutorial_KinCon-07.png  style="width:300px;"> 
*Dialog windows finished*


<div class="mw-collapsible mw-collapsed">

**And finally the whole macro**


<div class="mw-collapsible-content">

**Don\'t forget to set the path in the output() method!**


```python
#! python
# -*- coding: utf-8 -*-
# (c) 2021 Your name LGPL

# imports and constants
import time
from PySide2.QtWidgets import (QDialog, QLabel, QSlider, QLineEdit, QPushButton, QCheckBox)

class ControlPanel(QDialog):
    """
    docstring for ControlPanel.
    """
    def __init__(self, document, actuator):
        super(ControlPanel, self).__init__()
        self.initUI(document, actuator)

    def initUI(self, document, actuator):
        # Setting up class parameters
        self.actuator = document.getObject(actuator)
        self.driver_type = self.getDriverType(self.actuator)
        self.steps_value = 10
        self.sequence = False
        if self.driver_type == "Angle":
            self.current_value = self.actuator.Angle
            self.start_value = (self.current_value - 15)
            self.end_value = (self.current_value + 15)
            self.unit_suffix = (" °")
        elif self.driver_type == "Distance":
            self.current_value = float(str(self.actuator.Distance)[:-3])
            self.start_value = 0.001 # Distance must not be <= 0
            self.end_value = (self.current_value + 10)
            self.unit_suffix = (" mm")
        else:
            self.current_value = float(str(self.actuator.Offset)[:-3])
            self.start_value = (self.current_value - 10)
            self.end_value = (self.current_value + 10)
            self.unit_suffix = (" mm")

        # the window has 640 x 480 pixels and is centered by default
        #- set window dimensions
        self.setMaximumWidth(400)
        self.setMaximumHeight(200)
        self.setMinimumWidth(400)
        self.setMinimumHeight(200)
        self.setWindowTitle(self.actuator.Label + ": " + self.driver_type)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        # create some labels
        self.label_start = QLabel("", self)
        self.label_start.setFont("osifont") # set to a non-proportional font
        self.label_start.setText(str(round(self.start_value, 1)) + self.unit_suffix)
        self.label_start.setGeometry(QtCore.QRect(30, 15, 60, 25))

        self.label_end = QLabel("", self)
        self.label_end.setFont("osifont")
        self.label_end.setText(str(round(self.end_value, 1)) + self.unit_suffix)
        self.label_end.setGeometry(QtCore.QRect(320, 15, 60, 25))

        self.label_current = QLabel("", self)
        self.label_current.setFont("osifont")
        self.label_current.setText("Current value: " + str(round(self.current_value, 1)) + self.unit_suffix)
        self.label_current.setGeometry(QtCore.QRect(130, 15, 150, 25))

        # create some input elements

        # text input field - Start value
        self.entry_start = QLineEdit(self)
        self.entry_start.setText(str(round(self.start_value, 1)))
        self.entry_start.setGeometry(QtCore.QRect(30, 80, 50, 25))
        self.entry_start.textChanged[str].connect(self.onEntryStart)

        # text input field - End value
        self.entry_end = QLineEdit(self)
        self.entry_end.setText(str(round(self.end_value, 1)))
        self.entry_end.setGeometry(QtCore.QRect(320, 80, 50, 25))
        self.entry_end.textChanged[str].connect(self.onEntryEnd)

        # text input field - number of steps
        self.entry_steps = QLineEdit(self)
        self.entry_steps.setText(str(int(self.steps_value)))
        self.entry_steps.setGeometry(QtCore.QRect(180, 80, 50, 25))
        self.entry_steps.textChanged[str].connect(self.onEntrySteps)

        # Horizontal slider
        self.actuator_slider = QSlider(self)                             # create horizontalSlider
        self.actuator_slider.setOrientation(QtCore.Qt.Horizontal)        # orientation horizontal
        self.actuator_slider.setGeometry(QtCore.QRect(30, 50, 330, 25))  # position coordinates
        self.actuator_slider.setObjectName("horizontalSlider")           # object name
        self.actuator_slider.setInvertedAppearance(False)                # default: right to left
        self.actuator_slider.setRange(0, 100)                            # default: (0, 99)
        self.actuator_slider.setValue(self.current_value / self.stepRatio())
        self.actuator_slider.valueChanged.connect(self.onActuatorSlider)

        # output check box
        self.output_check = QCheckBox(self)
        self.output_check.setGeometry(QtCore.QRect(40, 120, 300, 25))
        self.output_check.setChecked(False)
        self.output_check.setText("Check to record an image sequence")
        self.output_check.setObjectName("checkBoxOutput")
        self.output_check.clicked.connect(self.onOutputClicked)

        # forward button
        self.forward_button = QPushButton(">->", self)
        self.forward_button.setGeometry(QtCore.QRect(240, 80, 50, 25))
        self.forward_button.setAutoDefault(False)
        self.forward_button.clicked.connect(self.onForward)
        # backward button
        self.backward_button = QPushButton("<-<", self)
        self.backward_button.setGeometry(QtCore.QRect(100, 80, 50, 25))
        self.backward_button.setAutoDefault(False)
        self.backward_button.clicked.connect(self.onBackward)
        # close button
        self.close_button = QPushButton("Close window", self)
        self.close_button.setGeometry(QtCore.QRect(120, 160, 130, 25))
        self.close_button.setAutoDefault(False)
        self.close_button.clicked.connect(self.onClose)

        # now make the window visible
        self.show()

    def getDriverType(self, constraint):
        ANGLE_CONSTRAINTS = [
            "Angle",
            "PlaneCoincident",
            "AxialAlignment",
            "PlaneAlignment"
            ]
        DISTANCE_CONSTRAINTS = [
            "PointDistance",
            "PointsDistance"
            ]
        if constraint.ConstraintType in ANGLE_CONSTRAINTS:
            return "Angle"
        elif constraint.ConstraintType in DISTANCE_CONSTRAINTS:
            return "Distance"
        else:
            return "Length"

    def stepRatio(self):
        ratio = (self.end_value - self.start_value) / 100
        return ratio

    def onEntryStart(self, new_start):
        self.start_value = float(new_start)
        self.label_start.setText(str(round(self.start_value, 1)) + self.unit_suffix)
        # Update the slider
        slider_value = ((self.current_value - self.start_value) / self.stepRatio())
        self.actuator_slider.setValue(slider_value)

    def onEntryEnd(self, new_end):
        self.end_value = float(new_end)
        self.label_end.setText(str(round(self.end_value, 1)) + self.unit_suffix)
        # Update the slider
        slider_value = ((self.current_value - self.start_value) / self.stepRatio())
        self.actuator_slider.setValue(slider_value)

    def onEntrySteps(self, new_steps):
        self.steps_value = int(new_steps)

    def onActuatorSlider(self, slider_value):
        self.current_value = slider_value * self.stepRatio() + self.start_value
        if self.driver_type == "Angle":
            self.actuator.Angle = self.current_value
        elif self.driver_type == "Distance":
            self.actuator.Distance = self.current_value
        else:
            self.actuator.Offset = self.current_value
        self.label_current.setText("Current value: " + str(round(self.current_value, 1)) + self.unit_suffix)
        FreeCADGui.updateGui() # screen update between steps
        Gui.runCommand("asm3CmdQuickSolve", 0)

    def onForward(self):
        steps_left = self.steps_value
        print(self.steps_value)
        step = ((self.end_value - self.current_value) / steps_left)
        while steps_left > 0:
            self.current_value += step
            slider_value = ((self.current_value - self.start_value) / self.stepRatio())
            self.actuator_slider.setValue(slider_value)
            time.sleep(0.2)
            self.output(steps_left)
            steps_left -= 1
        self.actuator_slider.setValue(100)

    def onBackward(self):
        steps_left = self.steps_value
        step = ((self.current_value - self.start_value) / steps_left)
        while steps_left > 0:
            self.current_value -= step
            slider_value = ((self.current_value - self.start_value) / self.stepRatio())
            self.actuator_slider.setValue(slider_value)
            time.sleep(0.2)
            self.output(steps_left)
            steps_left -= 1
        self.actuator_slider.setValue(0)

    def onClose(self):
        self.result = "Closed"
        self.close()

    def onOutputClicked(self):
        if self.sequence == True:
            self.sequence = False
            self.output_check.setChecked(False)
        else:
            self.sequence = True
            self.output_check.setChecked(True)

    def output(self, counter):
        if (self.sequence == True):
            image_path = ".../FreeCAD/ScreenShots/Sequence"
            file_tag = ".png"
            height = 640
            width = 480
            background = "Transparent"
            # dealing with leading zeros
            if (counter > 999) or (counter < 0):
                print("Out of Range")
            elif (counter < 10):
                number = "00" + str(counter)
            elif (counter < 100):
                number = "0" + str(counter)
            else:
                number = str(counter)
            # Screen shot
            Gui.activeDocument().activeView().saveImage(image_path + number + file_tag, height, width, background)

# End of ControlPanel()
# Main section below:

def findTheDrivingConstraints(document_object):
    # search through the Objects and find the driving constraint
    driver_list = []
    for each in document_object.Objects:
        if each.Label.endswith("Driver"):
            driving_constraint = each.Name
            driver_list.append(driving_constraint)
    return driver_list

def main():
    kin_doc = App.ActiveDocument # Kinematic Document
    drivers = findTheDrivingConstraints(kin_doc)
    if len(drivers) < 1:
        print("No driver found!")
    else:
        panel_list = []
        for each_driver in drivers:
            panel = ControlPanel(kin_doc, each_driver)
            panel_list.append(panel)
        panel.exec_()

if __name__ == "__main__":
    # This will be true only if the file is "executed"
    # but not if imported as a module
    main()
```


</div>


</div>


{{Top}}

## Some imperfections 

-   The order of the image sequence is reversed as we use the variable steps_left which is counted down.
-   The image directory and the image name are hard-coded.
-   Multiple Controllers are not synchronised.



---
![](images/Button_right.svg) [documentation index](../README.md) > Tutorial KinematicController/en
