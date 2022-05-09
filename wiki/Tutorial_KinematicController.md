---
- TutorialInfo   *   Topic   *Kinematic controller created with Python
   Level   *Basic skills of Python are helpful
   FCVersion   *0.20. and later
   Time   *(I don't know yet)
   Author   *[FBXL5](User_FBXL5.md)
---

# Tutorial KinematicController


{{Work_in_progress}}

 



## Introduction

This tutorial describes how to generate a simple kinematic controller to use with assemblies created with the Assembly3 workbench out of some lines of Python code.

Any text editor can be used to code. My choice is Atom, but FreeCAD\'s built-in editor works well, too.

The following code examples can be copied and pasted into an empty text file and then saved under a name of your choice as a \*.py or \*.FCMacro file.

## Macro sections 

### Basic structure of a simple Python macro 

 {{Code| |code=
#! python
# -*- coding   * utf-8 -*-
# (c) 2022 Your name LGPL
def main()   *
    pass
if __name__ == '__main__'   *
    # This will be true only if the file is "executed"
    # but not if imported as module
    main()
}}

It consist of a main() routine (function) and a switch checking if the macro is used as a container for classes, methods etc. or if it is run on its own. Only the second option will start the main() routine.

The routine is empty yet and awaits content.

### Find driving constraints 

The driving constraints are objects within a FreeCAD document. They need to be marked so that they can be found.

For this controller the suffix **Driver** has to be attached to the label of a driving constraint. It may be separated by a \".\" or \"-\" for clarity, but this tool will only search for the last 6 characters of the label.

A routine receiving a document name ad returns a list of driving constraints (the names in this case) will do the job.

 {{Code| |code=
def findTheDrivingConstraints(document_name)   *
    # search through the Objects and find the driving constraint
    driver_list = []
    for each in document_name.Objects   *
        if each.Label[-6   *] == 'Driver'    *
            driving_constraint = each.Name
            driver_list.append(driving_constraint)
    return driver_list
}}

The main() routine loads the name of the active document into the variable **kin\_doc** and then calls the function **findTheDrivingConstraints()** and hands over the content of kin\_doc. The returned list is loaded into drivers which is then checked to contain exactly one item. If that is the case it is finally printed to the report view to check the result.

 {{Code| |code=
def main()   *
    kin_doc = App.ActiveDocument # Kinematic Document
    drivers = findTheDrivingConstraints(kin_doc)
    if len(drivers) < 1   *
        print("No driver found!")
    elif len(drivers) > 1   *
        print("Not supported yet!")
    else   *
        print(drivers)
}}


<div class="mw-collapsible mw-collapsed">

**The macro so far\...**


<div class="mw-collapsible-content">

 {{Code| |code=
#! python
# -*- coding   * utf-8 -*-
# (c) 2021 Your name LGPL
def findTheDrivingConstraints(document_name)   *
    # search through the Objects and find the driving constraint
    driver_list = []
    for each in document_name.Objects   *
        if each.Label[-6   *] == 'Driver'    *
            driving_constraint = each.Name
            driver_list.append(driving_constraint)
    return driver_list

def main()   *
    kin_doc = App.ActiveDocument # Kinematic Document
    drivers = findTheDrivingConstraints(kin_doc)
    if len(drivers) < 1   *
        print("No driver found!")
    elif len(drivers) > 1   *
        print("Not supported yet!")
    else   *
        print(drivers)
if __name__ == '__main__'   *
    # This will be true only if the file is "executed"
    # but not if imported as module
    main()
}}


</div>


</div>

[Back to the top](#top.md)

### Control panel 

The control panel is built from Qt widgets, one main window containing several input/output widgets.

Each widget has to be imported before it can be used, but they can be imported as a single set. And the import line is placed close to the top of the script.

#### Main window 

For the main window an import line looks like this   *

 {{Code| |code=
from PySide2.QtWidgets import (QDialog)
}}

The main window called ControlPanel is a class object instantiated from the QDialog widget.

It has two init methods. **\_\_init\_\_** initialises the new class object, handles incoming arguments, and starts **initUI** which manages all widgets within the main window.

 {{Code| |code=
class ControlPanel(QDialog)   *
    """
    docstring for ControlPanel.
    """
    def __init__(self, Document, actuator_list)   *
        super(ControlPanel, self).__init__()
        self.initUI(Document, actuator_list)

    def initUI(self, Document, actuator_list)   *
        # Setting up class parameters
        # the window has 640 x 480 pixels and is centered by default
        # now make the window visible
        self.show()
}}

To launch the control panel an instance of the new class called **form** will be created with the **document name** and the **list of driving constraints** transferred to this instance. Finally the **exec\_()** method of the class opens the dialog window.

 {{Code| |code=
form = ControlPanel(kin_doc, drivers)
form.exec_()
}}

Both lines replace the print command in the else branch of the main section.

Running the macro will display a clean empty dialog window waiting for widgets   *

<img alt="An empty dialog window" src=images/Tutorial_KinCon-01.png  style="width   *300px;">


<div class="mw-collapsible mw-collapsed">

**And the macro so far\...**


<div class="mw-collapsible-content">

 {{Code| |code=
#! python
# -*- coding   * utf-8 -*-
# (c) 2021 Your name LGPL

# imports and constants
from PySide2.QtWidgets import (QDialog)

class ControlPanel(QDialog)   *
    """
    docstring for ControlPanel.
    """
    def __init__(self, Document, actuator_list)   *
        super(ControlPanel, self).__init__()
        self.initUI(Document, actuator_list)

    def initUI(self, Document, actuator_list)   *
        # Setting up class parameters
        # the window has 640 x 480 pixels and is centered by default
        # now make the window visible
        self.show()


def findTheDrivingConstraints(document_name)   *
    # search through the Objects and find the driving constraint
    driver_list = []
    for each in document_name.Objects   *
        if each.Label[-6   *] == 'Driver'    *
            driving_constraint = each.Name
            driver_list.append(driving_constraint)
    return driver_list

def main()   *
    kin_doc = App.ActiveDocument # Kinematic Document
    drivers = findTheDrivingConstraints(kin_doc)
    if len(drivers) < 1   *
        print("No driver found!")
    elif len(drivers) > 1   *
        print("Not supported yet!")
    else   *
        form = ControlPanel(kin_doc, drivers)
        form.exec_()
if __name__ == '__main__'   *
    # This will be true only if the file is "executed"
    # but not if imported as module
    main()
}}


</div>


</div>

[Back to the top](#top.md)

#### Setting parameters 

Now it is time to fill the **initUI()** section   *

 {{Code| |code=
...
    def initUI(self, Document, actuator_list)   *
        # Setting up class parameters
        self.document = Document
        self.actuators = actuator_list
        self.actuator = self.document.getObject(self.actuators[0])
        self.driver_type = self.getDriverType(self.actuator)
        # the window has 640 x 480 pixels and is centered by default
        # now make the window visible
        self.show()
...
}}

The actuator to be used is the first item in the actuators list. (The list contains one single item now, but if the controller can handle more than one driving constraint in the future, it will hold more items.)

##### Method getDriverType() 

For later use we need the driver type (Angle, Distance, Length) and so a method **getDriverType()** has to be defined   *

 {{Code| |code=
...
    def getDriverType(self, constraint)   *
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
        if constraint.ConstraintType in ANGLE_CONSTRAINTS   *
            return "Angle"
        elif constraint.ConstraintType in DISTANCE_CONSTRAINTS   *
            return "Distance"
        else   *
            return "Length"
...
}}

This method checks if the type of the given constraint can be found in one of the lists to return which kind of dimension has to be controlled.

It is assumed that in the kinematic document the driver is marked correctly and working if edited manually. In this case there is no need to filter out geometric constraints such as Colinear or PointsCoincidence (but here would be the place to do so\...)

##### Window properties 

The window size is defined by its minimum and maximum dimensions. Same values mean a fixed size.

The titel shows the driver name and whether its an angle, a distance, or a length. Finally the window is told to stay on top of all windows.

 {{Code| |code=
...
        # the window has 640 x 480 pixels and is centered by default
        #- set window dimensions
        self.setMaximumWidth(400)
        self.setMaximumHeight(200)
        self.setMinimumWidth(400)
        self.setMinimumHeight(200)
        self.setWindowTitle(self.actuator.Label + "   * " + self.driver_type)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        # now make the window visible
...
}}

[Back to the top](#top.md)

#### Setting more parameters 

Next step is to extract the current value of the driver and set default start and end values depending on the driver type.

A distance cannot be negative and exactly zero puzzles the solver and so the start value is set to 0.001. Angles accept negative values and get symmetric values. (If lengths accept negative values has to be proven finally\...)

The unit suffix must be kept for returning the value to the constraint property in the end. Distances and lengths need values with units.

Dealing with units and displaying values as strings in several widgets requires to convert numbers into strings and back again quite often.

To complete the parameters we set a default number of steps that should be computed when the motion is automated and if the sequence toggle is set to TRUE, a picture will be taken with each step of the motion.

 {{Code| |code=
...
        self.steps_value = 10
        self.sequence = False
        if self.driver_type == "Angle"    *
            self.current_value = self.actuator.Angle
            self.start_value = (self.current_value - 15)
            self.end_value = (self.current_value + 15)
            self.unit_suffix = (" °")
        elif self.driver_type == "Distance"    *
            self.current_value = float(str(self.actuator.Distance)[   *-3])
            self.start_value = 0.001 # Distance must not be <= 0
            self.end_value = (self.current_value + 10)
            self.unit_suffix = (" mm")
        else   *
            self.current_value = float(str(self.actuator.Offset)[   *-3])
            self.start_value = (self.current_value - 10)
            self.end_value = (self.current_value + 10)
            self.unit_suffix = (" mm")
...
}}

[Back to the top](#top.md)

#### Labels

Now three labels are added to display the start, end, and current value.

First the class **QLabel** must be imported i.e. the import list has to be extended like this   *

 {{Code| |code=
from PySide2.QtWidgets import (QDialog, QLabel)
}}

Back in the **initUI()** section we insert   *

 {{Code| |code=
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
        self.label_current.setText("Current value   * " + str(round(self.current_value, 1)) + self.unit_suffix)
        self.label_current.setGeometry(QtCore.QRect(130, 15, 150, 25))
...
}}

The placement is done with the inherited setGeometry() method. In this case the description of a rectangle is used (X position, Y position, width, height).

The first and third lines could be combined, but it is not recommended for clarity reasons   *

self.label_end = QLabel((str(round(self.end_value, 1)) + self.unit_suffix), self)

Running the macro with a kinematic assembly document would create a dialog window like this   *

<img alt="A dialog window displaying start value, current Value, and end value" src=images/Tutorial_KinCon-02.png  style="width   *300px;"> 
*The dialog window displaying constraint label and driver type in the header and start value, current Value, and end value on the first line in the main area*


<div class="mw-collapsible mw-collapsed">

**And the macro so far\...**


<div class="mw-collapsible-content">

 {{Code| |code=
#! python
# -*- coding   * utf-8 -*-
# (c) 2021 Your name LGPL

# imports and constants
from PySide2.QtWidgets import (QDialog, QLabel)

class ControlPanel(QDialog)   *
    """
    docstring for ControlPanel.
    """
    def __init__(self, Document, actuator_list)   *
        super(ControlPanel, self).__init__()
        self.initUI(Document, actuator_list)

    def initUI(self, Document, actuator_list)   *
        # Setting up class parameters
        self.document = Document
        self.actuators = actuator_list
        self.actuator = self.document.getObject(self.actuators[0])
        self.driver_type = self.getDriverType(self.actuator)
        self.steps_value = 10
        self.sequence = False
        if self.driver_type == "Angle"    *
            self.current_value = self.actuator.Angle
            self.start_value = (self.current_value - 15)
            self.end_value = (self.current_value + 15)
            self.unit_suffix = (" °")
        elif self.driver_type == "Distance"    *
            self.current_value = float(str(self.actuator.Distance)[   *-3])
            self.start_value = 0.001 # Distance must not be <= 0
            self.end_value = (self.current_value + 10)
            self.unit_suffix = (" mm")
        else   *
            self.current_value = float(str(self.actuator.Offset)[   *-3])
            self.start_value = (self.current_value - 10)
            self.end_value = (self.current_value + 10)
            self.unit_suffix = (" mm")

        # the window has 640 x 480 pixels and is centered by default
        #- set window dimensions
        self.setMaximumWidth(400)
        self.setMaximumHeight(200)
        self.setMinimumWidth(400)
        self.setMinimumHeight(200)
        self.setWindowTitle(self.actuator.Label + "   * " + self.driver_type)
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
        self.label_current.setText("Current value   * " + str(round(self.current_value, 1)) + self.unit_suffix)
        self.label_current.setGeometry(QtCore.QRect(130, 15, 150, 25))

        # now make the window visible
        self.show()

    def getDriverType(self, constraint)   *
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
        if constraint.ConstraintType in ANGLE_CONSTRAINTS   *
            return "Angle"
        elif constraint.ConstraintType in DISTANCE_CONSTRAINTS   *
            return "Distance"
        else   *
            return "Length"

# End of ControlPanel()
# Main section below   *

def findTheDrivingConstraints(document_name)   *
    # search through the Objects and find the driving constraint
    driver_list = []
    for each in document_name.Objects   *
        if each.Label[-6   *] == 'Driver'    *
            driving_constraint = each.Name
            driver_list.append(driving_constraint)
    return driver_list

def main()   *
    kin_doc = App.ActiveDocument # Kinematic Document
    drivers = findTheDrivingConstraints(kin_doc)
    if len(drivers) < 1   *
        print("No driver found!")
    elif len(drivers) > 1   *
        print("Not supported yet!")
    else   *
        form = ControlPanel(kin_doc, drivers)
        form.exec_()
        print(drivers)
if __name__ == '__main__'   *
    # This will be true only if the file is "executed"
    # but not if imported as module
    main()
}}


</div>


</div>

[Back to the top](#top.md)

#### Slider

To change the current value to any number between start and end value a slider widget would fit.

First the class **QSlider** must be imported i.e. the import list has to be extended like this   *

 {{Code| |code=
from PySide2.QtWidgets import (QDialog, QLabel, QSlider)
}}

Back in the **initUI()** section and right after the labels section we insert   *

 {{Code| |code=
...
        # Horizontal slider
        self.actuator_slider = QSlider(self)                             # create horizontalSlider
        self.actuator_slider.setOrientation(QtCore.Qt.Horizontal)        # orientation Horizontal
        self.actuator_slider.setGeometry(QtCore.QRect(30, 50, 330, 25))  # position coordinates
        self.actuator_slider.setObjectName("horizontalSlider")           # object Name
        self.actuator_slider.setInvertedAppearance(False)                # default   * right to left
        self.actuator_slider.setRange(0, 100)                            # default   * (0, 99)
        self.actuator_slider.setValue(self.current_value / self.stepRatio())
        self.actuator_slider.valueChanged.connect(self.onActuatorSlider)
...
}}

The slider button is placed with the setValue() method. Its value has to be calculated from the current value and a step ratio. The ratio has to be calculated whenever a start or end value is changed and so we insert another method after the getDriverType() method.

To work with a ratio instead of altering the slider\'s min and max values has the advantage of a finer resolution for small values.

 {{Code| |code=
...
    def stepRatio(self)   *
        ratio = (self.end_value - self.start_value) / 100
        return ratio
...
}}

And after this one comes another method defining what to do when the slider position or the slider value changes. The onActuatorSlider() method is called by the connect() method which also hands over the slider value as an argument.

It recalculates the current value from the slider position, rewrites the text of the label **self.label\_current** and changes the constraint property according to the driver type.

Running the command **asm3CmdQuickSolve** starts the solver to rearrange the assembly parts with the altered value.

 {{Code| |code=
...
    def onActuatorSlider(self, slider_value)   *
        self.current_value = slider_value * self.stepRatio() + self.start_value
        if self.driver_type == "Angle"    *
            self.actuator.Angle = self.current_value
        elif self.driver_type == "Distance"    *
            self.actuator.Distance = self.current_value
        else   *
            self.actuator.Offset = self.current_value
        self.label_current.setText("Current value   * " + str(round(self.current_value, 1)) + self.unit_suffix)
        Gui.runCommand('asm3CmdQuickSolve',0)
...
}}

The dialog window with the slider should look like this and is ready to control a motion   *

<img alt="Two dialog windows with a slider" src=images/Tutorial_KinCon-03.png  style="width   *300px;"> 
*Dialog windows with the added slider, one for an angle driver and one for a Distance driver*

We can start a dialog window for any opened document, they won\'t interfere with each other.

[Back to the top](#top.md)

#### Text entry fields 

To set the start and end value we use a line edit widget.

First the class **QLineEdit** must be imported i.e. the import list has to be extended like this   *

 {{Code| |code=
from PySide2.QtWidgets import (QDialog, QLabel, QSlider, QLineEdit)
}}

Back in the **initUI()** section and between the labels and the slider sections we insert   *

 {{Code| |code=
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
}}

The entry fields display the default start and end values. They are not complete until we add the methods to deal with altered entries. This will be done by the methods self.onEntryStart() and self.onEntry() that are inserted between the self.stepRatio() and the self.onActuatorSlider() section.

 {{Code| |code=
...
    def onEntryStart(self, new_start)   *
        self.start_value = float(new_start)
        self.label_start.setText(str(round(self.start_value, 1)) + self.unit_suffix)
        # Update the slider
        slider_value = ((self.current_value - self.start_value) / self.stepRatio())
        self.actuator_slider.setValue(slider_value)

    def onEntryEnd(self, new_end)   *
        self.end_value = float(new_end)
        self.label_end.setText(str(round(self.end_value, 1)) + self.unit_suffix)
        # Update the slider
        slider_value = ((self.current_value - self.start_value) / self.stepRatio())
        self.actuator_slider.setValue(slider_value)
...
}}

Both convert the received string value to a floating point number and change self.start\_value/self.end\_value and the corresponding label accordingly. After that the slider value is updated.

The dialog window with text entry fields should look like this and is ready to change the range of a motion   *

<img alt="Two dialog windows with line edit fields" src=images/Tutorial_KinCon-04.png  style="width   *300px;"> 
*Dialog windows with line edit fields, again for an angle and a distance driver*


<div class="mw-collapsible mw-collapsed">

**And the macro so far\...**


<div class="mw-collapsible-content">

 {{Code| |code=
#! python
# -*- coding   * utf-8 -*-
# (c) 2021 Your name LGPL

# imports and constants
from PySide2.QtWidgets import (QDialog, QLabel, QSlider, QLineEdit)

class ControlPanel(QDialog)   *
    """
    docstring for ControlPanel.
    """
    def __init__(self, Document, actuator_list)   *
        super(ControlPanel, self).__init__()
        self.initUI(Document, actuator_list)

    def initUI(self, Document, actuator_list)   *
        # Setting up class parameters
        self.document = Document
        self.actuators = actuator_list
        self.actuator = self.document.getObject(self.actuators[0])
        self.driver_type = self.getDriverType(self.actuator)
        self.steps_value = 10
        self.sequence = False
        if self.driver_type == "Angle"    *
            self.current_value = self.actuator.Angle
            self.start_value = (self.current_value - 15)
            self.end_value = (self.current_value + 15)
            self.unit_suffix = (" °")
        elif self.driver_type == "Distance"    *
            self.current_value = float(str(self.actuator.Distance)[   *-3])
            self.start_value = 0.001 # Distance must not be <= 0
            self.end_value = (self.current_value + 10)
            self.unit_suffix = (" mm")
        else   *
            self.current_value = float(str(self.actuator.Offset)[   *-3])
            self.start_value = (self.current_value - 10)
            self.end_value = (self.current_value + 10)
            self.unit_suffix = (" mm")

        # the window has 640 x 480 pixels and is centered by default
        #- set window dimensions
        self.setMaximumWidth(400)
        self.setMaximumHeight(200)
        self.setMinimumWidth(400)
        self.setMinimumHeight(200)
        self.setWindowTitle(self.actuator.Label + "   * " + self.driver_type)
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
        self.label_current.setText("Current value   * " + str(round(self.current_value, 1)) + self.unit_suffix)
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
        self.actuator_slider.setOrientation(QtCore.Qt.Horizontal)        # orientation Horizontal
        self.actuator_slider.setGeometry(QtCore.QRect(30, 50, 330, 25))  # position coordinates
        self.actuator_slider.setObjectName("horizontalSlider")           # object Name
        self.actuator_slider.setInvertedAppearance(False)                # default   * right to left
        self.actuator_slider.setRange(0, 100)                            # default   * (0, 99)
        self.actuator_slider.setValue(self.current_value / self.stepRatio())
        self.actuator_slider.valueChanged.connect(self.onActuatorSlider)

        # now make the window visible
        self.show()

    def getDriverType(self, constraint)   *
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
        if constraint.ConstraintType in ANGLE_CONSTRAINTS   *
            return "Angle"
        elif constraint.ConstraintType in DISTANCE_CONSTRAINTS   *
            return "Distance"
        else   *
            return "Length"

    def stepRatio(self)   *
        ratio = (self.end_value - self.start_value) / 100
        return ratio

    def onEntryStart(self, new_start)   *
        self.start_value = float(new_start)
        self.label_start.setText(str(round(self.start_value, 1)) + self.unit_suffix)
        # Update the slider
        slider_value = ((self.current_value - self.start_value) / self.stepRatio())
        self.actuator_slider.setValue(slider_value)

    def onEntryEnd(self, new_end)   *
        self.end_value = float(new_end)
        self.label_end.setText(str(round(self.end_value, 1)) + self.unit_suffix)
        # Update the slider
        slider_value = ((self.current_value - self.start_value) / self.stepRatio())
        self.actuator_slider.setValue(slider_value)

    def onActuatorSlider(self, slider_value)   *
        self.current_value = slider_value * self.stepRatio() + self.start_value
        if self.driver_type == "Angle"    *
            self.actuator.Angle = self.current_value
        elif self.driver_type == "Distance"    *
            self.actuator.Distance = self.current_value
        else   *
            self.actuator.Offset = self.current_value
        self.label_current.setText("Current value   * " + str(round(self.current_value, 1)) + self.unit_suffix)
        Gui.runCommand('asm3CmdQuickSolve',0)
        print(slider_value, self.current_value)

# End of ControlPanel()
# Main section below   *

def findTheDrivingConstraints(document_name)   *
    # search through the Objects and find the driving constraint
    driver_list = []
    for each in document_name.Objects   *
        if each.Label[-6   *] == 'Driver'    *
            driving_constraint = each.Name
            driver_list.append(driving_constraint)
    return driver_list

def main()   *
    kin_doc = App.ActiveDocument # Kinematic Document
    drivers = findTheDrivingConstraints(kin_doc)
    if len(drivers) < 1   *
        print("No driver found!")
    elif len(drivers) > 1   *
        print("Not supported yet!")
    else   *
        form = ControlPanel(kin_doc, drivers)
        form.exec_()
        print(drivers)

if __name__ == '__main__'   *
    # This will be true only if the file is "executed"
    # but not if imported as module
    main()
}}


</div>


</div>

[Back to the top](#top.md)

### Motion

To get the assembly in motion we need   *

-   Buttons to trigger motion in the desired direction.
-   An input field to alter the number of steps for faster or smoother motions.
-   A check box to indicate if we want to shoot a sequence of images.

#### Forward and Backward buttons 

To move the assembly parts automatically we need two buttons to trigger the motions, one towards the start position and one towards the end position. These two and a close button are using a **QPushButton** widget.

Small assemblies compute a bit too fast and show jumps instead of a smooth motion. To slow it down we use the sleep() method of the time module which has to be imported first.

Another import and another widget   *

 {{Code| |code=
import time
from PySide2.QtWidgets import (QDialog, QLabel, QSlider, QLineEdit, QPushButton)
}}

Back in the **initUI()** section we insert the buttons after the slider section   *

 {{Code| |code=
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
}}

The methods dealing with pressed buttons are self.onForward(), self.onBackward(), and self.onClose(). They are inserted after the onActuatorSlider() section.

 {{Code| |code=
...
    def onForward(self)   *
        steps_left = self.steps_value
        print(self.steps_value)
        step = ((self.end_value - self.current_value) / steps_left)
        while steps_left > 0   *
            self.current_value += step
            slider_value = ((self.current_value - self.start_value) / self.stepRatio())
            self.actuator_slider.setValue(slider_value)
            time.sleep(0.2)
            steps_left -= 1
        self.actuator_slider.setValue(100)

    def onBackward(self)   *
        steps_left = self.steps_value
        step = ((self.current_value - self.start_value) / steps_left)
        while steps_left > 0   *
            self.current_value -= step
            slider_value = ((self.current_value - self.start_value) / self.stepRatio())
            self.actuator_slider.setValue(slider_value)
            time.sleep(0.2)
            steps_left -= 1
        self.actuator_slider.setValue(0)

    def onClose(self)   *
        self.result = "Closed"
        self.close()
...
}}

The method self.onClose() invokes the inherited method self.close() which just closes the dialog window and so ends the macro.

Both self.onForward() and self.onBackward() count the steps that are left to go to reach the wanted position and calculate the length of a step according to the number of steps. For now we go with the default number of 10 steps.

Each round on the while loop increases/decreases the current value and updates the slider values which triggers onActuatorSlider() in the background (see [Slider section](#Slider.md)). After a pause to let the computer provide another updated 3D view counting down the steps left to go finishes the loop.

With no steps left the slider is set to the first/last slider position, just in case if a rounding error had occurred.

The dialog window with buttons should look like this and can now move the assembly by 10 steps towards the wanted start/end position   *

<img alt="Two dialog windows with buttons" src=images/Tutorial_KinCon-05.png  style="width   *300px;"> 
*Dialog windows with buttons*


<div class="mw-collapsible mw-collapsed">

**And the macro so far\...**


<div class="mw-collapsible-content">

 {{Code| |code=
#! python
# -*- coding   * utf-8 -*-
# (c) 2021 Your name LGPL

# imports and constants
import time    # built-in modules
from PySide2.QtWidgets import (QDialog, QLabel, QSlider, QLineEdit, QPushButton)

class ControlPanel(QDialog)   *
    """
    docstring for ControlPanel.
    """
    def __init__(self, Document, actuator_list)   *
        super(ControlPanel, self).__init__()
        self.initUI(Document, actuator_list)

    def initUI(self, Document, actuator_list)   *
        # Setting up class parameters
        self.document = Document
        self.actuators = actuator_list
        self.actuator = self.document.getObject(self.actuators[0])
        self.driver_type = self.getDriverType(self.actuator)
        self.steps_value = 10
        self.sequence = False
        if self.driver_type == "Angle"    *
            self.current_value = self.actuator.Angle
            self.start_value = (self.current_value - 15)
            self.end_value = (self.current_value + 15)
            self.unit_suffix = (" °")
        elif self.driver_type == "Distance"    *
            self.current_value = float(str(self.actuator.Distance)[   *-3])
            self.start_value = 0.001 # Distance must not be <= 0
            self.end_value = (self.current_value + 10)
            self.unit_suffix = (" mm")
        else   *
            self.current_value = float(str(self.actuator.Offset)[   *-3])
            self.start_value = (self.current_value - 10)
            self.end_value = (self.current_value + 10)
            self.unit_suffix = (" mm")

        # the window has 640 x 480 pixels and is centered by default
        #- set window dimensions
        self.setMaximumWidth(400)
        self.setMaximumHeight(200)
        self.setMinimumWidth(400)
        self.setMinimumHeight(200)
        self.setWindowTitle(self.actuator.Label + "   * " + self.driver_type)
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
        self.label_current.setText("Current value   * " + str(round(self.current_value, 1)) + self.unit_suffix)
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
        self.actuator_slider.setOrientation(QtCore.Qt.Horizontal)        # orientation Horizontal
        self.actuator_slider.setGeometry(QtCore.QRect(30, 50, 330, 25))  # position coordinates
        self.actuator_slider.setObjectName("horizontalSlider")           # object Name
        self.actuator_slider.setInvertedAppearance(False)                # default   * right to left
        self.actuator_slider.setRange(0, 100)                            # default   * (0, 99)
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

    def getDriverType(self, constraint)   *
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
        if constraint.ConstraintType in ANGLE_CONSTRAINTS   *
            return "Angle"
        elif constraint.ConstraintType in DISTANCE_CONSTRAINTS   *
            return "Distance"
        else   *
            return "Length"

    def stepRatio(self)   *
        ratio = (self.end_value - self.start_value) / 100
        return ratio

    def onEntryStart(self, new_start)   *
        self.start_value = float(new_start)
        self.label_start.setText(str(round(self.start_value, 1)) + self.unit_suffix)
        # Update the slider
        slider_value = ((self.current_value - self.start_value) / self.stepRatio())
        self.actuator_slider.setValue(slider_value)

    def onEntryEnd(self, new_end)   *
        self.end_value = float(new_end)
        self.label_end.setText(str(round(self.end_value, 1)) + self.unit_suffix)
        # Update the slider
        slider_value = ((self.current_value - self.start_value) / self.stepRatio())
        self.actuator_slider.setValue(slider_value)

    def onActuatorSlider(self, slider_value)   *
        self.current_value = slider_value * self.stepRatio() + self.start_value
        if self.driver_type == "Angle"    *
            self.actuator.Angle = self.current_value
        elif self.driver_type == "Distance"    *
            self.actuator.Distance = self.current_value
        else   *
            self.actuator.Offset = self.current_value
        self.label_current.setText("Current value   * " + str(round(self.current_value, 1)) + self.unit_suffix)
        FreeCADGui.updateGui() # screen update between steps
        Gui.runCommand('asm3CmdQuickSolve',0)

    def onForward(self)   *
        steps_left = self.steps_value
        print(self.steps_value)
        step = ((self.end_value - self.current_value) / steps_left)
        while steps_left > 0   *
            self.current_value += step
            slider_value = ((self.current_value - self.start_value) / self.stepRatio())
            self.actuator_slider.setValue(slider_value)
            time.sleep(0.2)
            steps_left -= 1
        self.actuator_slider.setValue(100)

    def onBackward(self)   *
        steps_left = self.steps_value
        step = ((self.current_value - self.start_value) / steps_left)
        while steps_left > 0   *
            self.current_value -= step
            slider_value = ((self.current_value - self.start_value) / self.stepRatio())
            self.actuator_slider.setValue(slider_value)
            time.sleep(0.2)
            steps_left -= 1
        self.actuator_slider.setValue(0)

    def onClose(self)   *
        self.result = "Closed"
        self.close()

# End of ControlPanel()
# Main section below   *

def findTheDrivingConstraints(document_name)   *
    # search through the Objects and find the driving constraint
    driver_list = []
    for each in document_name.Objects   *
        if each.Label[-6   *] == 'Driver'    *
            driving_constraint = each.Name
            driver_list.append(driving_constraint)
    return driver_list

def main()   *
    kin_doc = App.ActiveDocument # Kinematic Document
    drivers = findTheDrivingConstraints(kin_doc)
    if len(drivers) < 1   *
        print("No driver found!")
    elif len(drivers) > 1   *
        print("Not supported yet!")
    else   *
        form = ControlPanel(kin_doc, drivers)
        form.exec_()
        print(drivers)

if __name__ == '__main__'   *
    # This will be true only if the file is "executed"
    # but not if imported as module
    main()
}}


</div>


</div>

[Back to the top](#top.md)

to be continued...



---
![](images/Right_arrow.png) [documentation index](../README.md) > Tutorial KinematicController
