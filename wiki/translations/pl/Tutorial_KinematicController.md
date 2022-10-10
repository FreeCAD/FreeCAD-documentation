---
- TutorialInfo   */pl
   Topic   *Sterownik kinematyczny utworzony w środowisku Python
   Level   *Przydatna jest podstawowa znajomość języka Python
   FCVersion   *0.20 lub nowszy
   Time   *1 godzina
   Author   *[FBXL5](User_FBXL5.md)
---

# Tutorial KinematicController/pl





## Wprowadzenie

Ten poradnik opisuje jak z kilku linijek kodu Python wygenerować prosty kontroler kinematyczny do użycia z zespołami utworzonymi za pomocą środowiska pracy [Złożenie 3](Assembly3_Workbench/pl.md).

Do kodowania można użyć dowolnego edytora tekstu. Mój wybór to Atom, ale wbudowany edytor FreeCAD też działa dobrze.

Poniższe przykłady kodu można skopiować i wkleić do pustego pliku tekstowego, a następnie zapisać pod wybraną nazwą jako plik typu ***.py** lub ***.FCMacro**.

## Sekcje makrodefinicji 

### Podstawowa struktura 


```python
#! python
# -*- coding   * utf-8 -*-
# (c) 2022 Your name LGPL

def main()   *
    pass

if __name__ == "__main__"   *
    # This will be true only if the file is "executed"
    # but not if imported as a module
    main()
```

Podstawowa struktura składa się z funkcji {{Incode|main()}} oraz przełącznika sprawdzającego, czy makro jest używane jako kontener dla klas, metod itp. czy też jest uruchamiane samodzielnie. Tylko druga opcja powoduje uruchomienie funkcji {{Incode|main()}}. Funkcja ta jest na razie pusta.

### Wyznacz więzy prowadzące 

Więzy prowadzące są obiektami w obrębie dokumentu FreeCAD. Należy je oznaczyć, aby można było je odnaleźć.

Dla tego kontrolera przyrostek {{Incode|"Driver"}} musi być dołączony do etykiety wiązania prowadzącego. Może on być oddzielony znakiem {{Incode|"."}} lub {{Incode|"-"}} dla jasności, ponieważ będziemy sprawdzać tylko czy etykieta kończy się {{Incode|"Driver"}}.

Funkcja, która otrzymuje obiekt dokumentu i zwraca listę więzów prowadzących *(nazwy w tym przypadku)* wykona zadanie.


```python
def findTheDrivingConstraints(document_object)   *
    # search through the Objects and find the driving constraint
    driver_list = []
    for each in document_object.Objects   *
        if each.Label.endswith("Driver")   *
            driving_constraint = each.Name
            driver_list.append(driving_constraint)
    return driver_list
```

Funkcja {{Incode|main()}} ładuje aktywny dokument do zmiennej {{Incode|kin_doc}}, a następnie wywołuje funkcję {{Incode|findTheDrivingConstraints()}} i przekazuje jej zawartość {{Incode|kin_doc}}. Zwrócona lista jest ładowana do {{Incode|drivers}}, która następnie jest sprawdzana, czy zawiera przynajmniej jeden element. Jeśli tak jest, lista jest ostatecznie wyświetlona w widoku [Raportu](Report_view/pl.md).


```python
def main()   *
    kin_doc = App.ActiveDocument # Kinematic Document
    drivers = findTheDrivingConstraints(kin_doc)
    if len(drivers) < 1   *
        print("No driver found!")
    else   *
        print(drivers)
```


<div class="mw-collapsible mw-collapsed">

**Dotychczasowe makrodefinicje \...**


<div class="mw-collapsible-content">


```python
#! python
# -*- coding   * utf-8 -*-
# (c) 2021 Your name LGPL

def findTheDrivingConstraints(document_object)   *
    # search through the Objects and find the driving constraint
    driver_list = []
    for each in document_object.Objects   *
        if each.Label.endswith("Driver")   *
            driving_constraint = each.Name
            driver_list.append(driving_constraint)
    return driver_list

def main()   *
    kin_doc = App.ActiveDocument # Kinematic Document
    drivers = findTheDrivingConstraints(kin_doc)
    if len(drivers) < 1   *
        print("No driver found!")
    else   *
        print(drivers)

if __name__ == "__main__"   *
    # This will be true only if the file is "executed"
    # but not if imported as a module
    main()
```


</div>


</div>


{{Top}}

### Panel sterowania 

Panel sterowania jest zbudowany z widżetów Qt, jedno główne okno zawierające kilka widżetów wejścia / wyjścia.

Każdy widżet musi zostać zaimportowany, zanim będzie można go użyć, ale można je zaimportować jako pojedynczy zestaw. Linia importu jest umieszczona w pobliżu górnej części pliku.

#### Okno główne 

W głównym oknie linia importu wygląda tak   *


```python
from PySide2.QtWidgets import (QDialog)
```

Okno główne o nazwie {{Incode|ControlPanel}} to obiekt klasy utworzony z widżetu {{Incode|QDialog}}.

Posiada ona dwie metody init. Metoda {{Incode|__init__()}} inicjalizuje nowy obiekt klasy, obsługuje przychodzące argumenty oraz uruchamia metodę {{Incode|initUI()}}, która zarządza wszystkimi widżetami w obrębie okna głównego.


```python
class ControlPanel(QDialog)   *
    """
    docstring for ControlPanel.
    """
    def __init__(self, document, actuator)   *
        super(ControlPanel, self).__init__()
        self.initUI(document, actuator)

    def initUI(self, document, actuator)   *
        # Setting up class parameters
        # the window has 640 x 480 pixels and is centered by default
        # now make the window visible
        self.show()
```

Aby uruchomić pojedynczy panel sterowania, zostanie utworzona instancja tej klasy o nazwie {{Incode|panel}}, z {{Incode|kin_doc}} *(obiekt dokumentu)* oraz {{Incode|drivers[0]}} *(pierwsze z listy wiązań dotyczących prowadzenia)* przekazanymi do tej instancji. Na koniec metoda {{Incode|exec_()}} klasy otwiera okno dialogowe.


```python
panel = ControlPanel(kin_doc, drivers[0])
panel.exec_()
```

Aby obsłużyć więcej niż jeden sterownik, musimy sprawdzić listę sterowników i utworzyć instancję dla każdej pozycji na liście i przenieść bieżącą pozycję.


```python
panel_list = []
for each_driver in drivers   *
    panel = ControlPanel(kin_doc, each_driver)
    panel_list.append(panel)
panel.exec_()
```

Te linie zastępują polecenie {{Incode|print()}} w gałęzi *else* funkcji {{Incode|main()}}.

Uwaga   * Zebranie {{Incode|panel_list}} pozwala na uruchomienie wszystkich paneli jednocześnie. *(Nie potrafię jeszcze wyjaśnić tego zachowania\...)*

Uruchomienie makra spowoduje wyświetlenie nowego, pustego okna dialogowego czekającego na widżety   *

<img alt="Puste okno dialogowe" src=images/Tutorial_KinCon-01.png  style="width   *300px;">


<div class="mw-collapsible mw-collapsed">

**Dotychczasowe makrodefinicje \...**


<div class="mw-collapsible-content">


```python
#! python
# -*- coding   * utf-8 -*-
# (c) 2021 Your name LGPL

# imports and constants
from PySide2.QtWidgets import (QDialog)

class ControlPanel(QDialog)   *
    """
    docstring for ControlPanel.
    """
    def __init__(self, document, actuator)   *
        super(ControlPanel, self).__init__()
        self.initUI(document, actuator)

    def initUI(self, document, actuator)   *
        # Setting up class parameters
        # the window has 640 x 480 pixels and is centered by default
        # now make the window visible
        self.show()


def findTheDrivingConstraints(document_object)   *
    # search through the Objects and find the driving constraint
    driver_list = []
    for each in document_object.Objects   *
        if each.Label.endswith("Driver")   *
            driving_constraint = each.Name
            driver_list.append(driving_constraint)
    return driver_list

def main()   *
    kin_doc = App.ActiveDocument # Kinematic Document
    drivers = findTheDrivingConstraints(kin_doc)
    if len(drivers) < 1   *
        print("No driver found!")
    else   *
        panel_list = []
        for each_driver in drivers   *
            panel = ControlPanel(kin_doc, each_driver)
            panel_list.append(panel)
        panel.exec_()

if __name__ == "__main__"   *
    # This will be true only if the file is "executed"
    # but not if imported as a module
    main()
```


</div>


</div>


{{Top}}

#### Ustawienie parametrów 

Teraz przyszedł czas na wypełnienie metody {{Incode|initUI()}}   *


```python
...
    def initUI(self, document, actuator)   *
        # Setting up class parameters
        self.actuator = document.getObject(actuator)
        self.driver_type = self.getDriverType(self.actuator)
        # the window has 640 x 480 pixels and is centered by default
        # now make the window visible
        self.show()
...
```


{{Incode|self.actuator}}

reprezentuje wiązanie napędowe, a {{Incode|self.driver_type}} przechowuje słowo kluczowe dla jego typu. To ostatnie jest używane do wyboru odpowiedniej właściwości z każdym wiązaniem.

##### Metoda getDriverType() 

Do późniejszego użycia potrzebujemy typ sterownika *(Kąt, Odległość, Długość)* i dlatego należy zdefiniować metodę {{Incode|getDriverType()}}   *


```python
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
```

This method checks if the type of the given constraint can be found in one of the lists, and returns which kind of dimension has to be controlled.

It is assumed that in the kinematic document the driver is marked correctly and working if edited manually. In this case there is no need to filter out geometric constraints such as Colinear or PointsCoincidence (but here would be the place to do so\...)

##### Ustawienia okna 

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
        self.setWindowTitle(self.actuator.Label + "   * " + self.driver_type)
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
        if self.driver_type == "Angle"   *
            self.current_value = self.actuator.Angle
            self.start_value = (self.current_value - 15)
            self.end_value = (self.current_value + 15)
            self.unit_suffix = (" °")
        elif self.driver_type == "Distance"   *
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
```


{{Top}}

#### Etykiety

Teraz dodano trzy etykiety, które wyświetlają wartość początkową, końcową i bieżącą.

Najpierw należy zaimportować klasę {{Incode|QLabel}}, tzn. rozszerzyć listę importu w sposób następujący   *


```python
from PySide2.QtWidgets import (QDialog, QLabel)
```

Back in the {{Incode|initUI()}} method we insert   *


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
        self.label_current.setText("Current value   * " + str(round(self.current_value, 1)) + self.unit_suffix)
        self.label_current.setGeometry(QtCore.QRect(130, 15, 150, 25))
...
```

The placement is done with the inherited {{Incode|setGeometry()}} method. In this case the description of a rectangle is used (X position, Y position, width, height).

The first and third lines could be combined, but it is not recommended for clarity reasons   *


```python
self.label_end = QLabel((str(round(self.end_value, 1)) + self.unit_suffix), self)
```

Running the macro with a kinematic assembly document would create a dialog window like this   *

<img alt="A dialog window displaying start value, current Value, and end value" src=images/Tutorial_KinCon-02.png  style="width   *300px;"> 
*The dialog window displaying the constraint label and driver type in the title, and the start value, current value and end value on the first line in the main area*


<div class="mw-collapsible mw-collapsed">

**Dotychczasowe makrodefinicje \...**


<div class="mw-collapsible-content">


```python
#! python
# -*- coding   * utf-8 -*-
# (c) 2021 Your name LGPL

# imports and constants
from PySide2.QtWidgets import (QDialog, QLabel)

class ControlPanel(QDialog)   *
    """
    docstring for ControlPanel.
    """
    def __init__(self, document, actuator)   *
        super(ControlPanel, self).__init__()
        self.initUI(document, actuator)

    def initUI(self, document, actuator)   *
        # Setting up class parameters
        self.actuator = document.getObject(actuator)
        self.driver_type = self.getDriverType(self.actuator)
        self.steps_value = 10
        self.sequence = False
        if self.driver_type == "Angle"   *
            self.current_value = self.actuator.Angle
            self.start_value = (self.current_value - 15)
            self.end_value = (self.current_value + 15)
            self.unit_suffix = (" °")
        elif self.driver_type == "Distance"   *
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

def findTheDrivingConstraints(document_object)   *
    # search through the Objects and find the driving constraint
    driver_list = []
    for each in document_object.Objects   *
        if each.Label.endswith("Driver")   *
            driving_constraint = each.Name
            driver_list.append(driving_constraint)
    return driver_list

def main()   *
    kin_doc = App.ActiveDocument # Kinematic Document
    drivers = findTheDrivingConstraints(kin_doc)
    if len(drivers) < 1   *
        print("No driver found!")
    else   *
        panel_list = []
        for each_driver in drivers   *
            panel = ControlPanel(kin_doc, each_driver)
            panel_list.append(panel)
        panel.exec_()

if __name__ == "__main__"   *
    # This will be true only if the file is "executed"
    # but not if imported as a module
    main()
```


</div>


</div>


{{Top}}

#### Slider

Aby zmienić bieżącą wartość na dowolną liczbę między wartością początkową a końcową, przydatny byłby widżet suwaka.

First the class {{Incode|QSlider}} must be imported i.e. the import list has to be extended like this   *


```python
from PySide2.QtWidgets import (QDialog, QLabel, QSlider)
```

Back in the {{Incode|initUI()}} method and right after the labels section we insert   *


```python
...
        # Horizontal slider
        self.actuator_slider = QSlider(self)                             # create horizontalSlider
        self.actuator_slider.setOrientation(QtCore.Qt.Horizontal)        # orientation horizontal
        self.actuator_slider.setGeometry(QtCore.QRect(30, 50, 330, 25))  # position coordinates
        self.actuator_slider.setObjectName("horizontalSlider")           # object name
        self.actuator_slider.setInvertedAppearance(False)                # default   * right to left
        self.actuator_slider.setRange(0, 100)                            # default   * (0, 99)
        self.actuator_slider.setValue(self.current_value / self.stepRatio())
        self.actuator_slider.valueChanged.connect(self.onActuatorSlider)
...
```

The slider button is placed with the {{Incode|setValue()}} method. Its value has to be calculated from the current value and a step ratio. The ratio has to be calculated whenever a start or end value is changed and so we insert another method after the {{Incode|getDriverType()}} method.

To work with a ratio instead of altering the slider\'s min and max values has the advantage of a finer resolution for small values.


```python
...
    def stepRatio(self)   *
        ratio = (self.end_value - self.start_value) / 100
        return ratio
...
```

And after this one comes another method defining what to do when the slider position or the slider value changes. The {{Incode|onActuatorSlider()}} method is called by the {{Incode|connect()}} method which also hands over the slider value as an argument.

It recalculates the current value from the slider position, rewrites the text of the label {{Incode|self.label_current}} and changes the constraint property according to the driver type.

Running the command {{Incode|"asm3CmdQuickSolve"}} starts the solver to rearrange the assembly parts with the altered value.


```python
...
    def onActuatorSlider(self, slider_value)   *
        self.current_value = slider_value * self.stepRatio() + self.start_value
        if self.driver_type == "Angle"   *
            self.actuator.Angle = self.current_value
        elif self.driver_type == "Distance"   *
            self.actuator.Distance = self.current_value
        else   *
            self.actuator.Offset = self.current_value
        self.label_current.setText("Current value   * " + str(round(self.current_value, 1)) + self.unit_suffix)
        Gui.runCommand("asm3CmdQuickSolve", 0)
...
```

The dialog window with the slider should look like this and is ready to control a motion   *

<img alt="Two dialog windows with a slider" src=images/Tutorial_KinCon-03.png  style="width   *300px;"> 
*Dialog windows with the added slider, one for an Angle driver and one for a Distance driver*

We can start a dialog window for any opened document, they won\'t interfere with each other. {{Top}}

#### Text entry fields 

To set the start and end value we use a line edit widget.

First the class {{Incode|QLineEdit}} must be imported i.e. the import list has to be extended like this   *


```python
from PySide2.QtWidgets import (QDialog, QLabel, QSlider, QLineEdit)
```

Back in the {{Incode|initUI()}} method and between the labels and the slider sections we insert   *


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
```

Both convert the received string value to a floating point number and change either {{Incode|self.start_value}} or {{Incode|self.end_value}} and the corresponding label accordingly. After that the slider value is updated.

The dialog window with text entry fields should look like this and is ready to change the range of a motion   *

<img alt="Two dialog windows with line edit fields" src=images/Tutorial_KinCon-04.png  style="width   *300px;"> 
*Dialog windows with line edit fields, again for an angle and a distance driver*


<div class="mw-collapsible mw-collapsed">

**Dotychczasowe makrodefinicje \...**


<div class="mw-collapsible-content">


```python
#! python
# -*- coding   * utf-8 -*-
# (c) 2021 Your name LGPL

# imports and constants
from PySide2.QtWidgets import (QDialog, QLabel, QSlider, QLineEdit)

class ControlPanel(QDialog)   *
    """
    docstring for ControlPanel.
    """
    def __init__(self, document, actuator)   *
        super(ControlPanel, self).__init__()
        self.initUI(document, actuator)

    def initUI(self, document, actuator)   *
        # Setting up class parameters
        self.actuator = document.getObject(actuator)
        self.driver_type = self.getDriverType(self.actuator)
        self.steps_value = 10
        self.sequence = False
        if self.driver_type == "Angle"   *
            self.current_value = self.actuator.Angle
            self.start_value = (self.current_value - 15)
            self.end_value = (self.current_value + 15)
            self.unit_suffix = (" °")
        elif self.driver_type == "Distance"   *
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
        self.actuator_slider.setOrientation(QtCore.Qt.Horizontal)        # orientation horizontal
        self.actuator_slider.setGeometry(QtCore.QRect(30, 50, 330, 25))  # position coordinates
        self.actuator_slider.setObjectName("horizontalSlider")           # object name
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
        if self.driver_type == "Angle"   *
            self.actuator.Angle = self.current_value
        elif self.driver_type == "Distance"   *
            self.actuator.Distance = self.current_value
        else   *
            self.actuator.Offset = self.current_value
        self.label_current.setText("Current value   * " + str(round(self.current_value, 1)) + self.unit_suffix)
        Gui.runCommand("asm3CmdQuickSolve", 0)
        print(slider_value, self.current_value)

# End of ControlPanel()
# Main section below   *

def findTheDrivingConstraints(document_object)   *
    # search through the Objects and find the driving constraint
    driver_list = []
    for each in document_object.Objects   *
        if each.Label.endswith("Driver")   *
            driving_constraint = each.Name
            driver_list.append(driving_constraint)
    return driver_list

def main()   *
    kin_doc = App.ActiveDocument # Kinematic Document
    drivers = findTheDrivingConstraints(kin_doc)
    if len(drivers) < 1   *
        print("No driver found!")
    else   *
        panel_list = []
        for each_driver in drivers   *
            panel = ControlPanel(kin_doc, each_driver)
            panel_list.append(panel)
        panel.exec_()

if __name__ == "__main__"   *
    # This will be true only if the file is "executed"
    # but not if imported as a module
    main()
```


</div>


</div>


{{Top}}

### Motion

To get the assembly in motion we need   *

-   Buttons to trigger motion in the desired direction.
-   An input field to alter the number of steps for faster or smoother motions.
-   A check box to indicate if we want to shoot a sequence of images.

#### Forward and Backward buttons 

To move the assembly parts automatically we need two buttons to trigger the motions, one towards the start position and one towards the end position. These two and a close button will use a {{Incode|QPushButton}} widget.

Small assemblies compute a bit too fast and show jumps instead of a smooth motion. To slow it down we use the {{Incode|sleep()}} method of the {{Incode|time}} module which has to be imported first.

Another import and another widget   *


```python
import time
from PySide2.QtWidgets import (QDialog, QLabel, QSlider, QLineEdit, QPushButton)
```

Back in the {{Incode|initUI()}} method we insert the buttons after the slider section   *


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
```

The method {{Incode|self.onClose()}} invokes the inherited method {{Incode|self.close()}} which just closes the dialog window and thereby ends the macro.

Both {{Incode|self.onForward()}} and {{Incode|self.onBackward()}} count the steps that are left to go to reach the wanted position and calculate the length of a step according to the number of steps. For now we go with the default number of 10 steps.

Each round on the while loop increases/decreases the current value and updates the slider values which triggers {{Incode|onActuatorSlider()}} in the background (see [Slider paragraph](#Slider.md)). After a pause to let the computer provide another updated 3D view, counting down the steps left to go finishes the loop.

With no steps left the slider is set to the first/last slider position, just in case if a rounding error had occurred.

The dialog window with buttons should look like this and can now move the assembly by 10 steps towards the wanted start/end position   *

<img alt="Dialog window with buttons" src=images/Tutorial_KinCon-05.png  style="width   *300px;"> 
*Dialog window with buttons*


<div class="mw-collapsible mw-collapsed">

**And the macro so far\...**


<div class="mw-collapsible-content">


```python
#! python
# -*- coding   * utf-8 -*-
# (c) 2021 Your name LGPL

# imports and constants
import time
from PySide2.QtWidgets import (QDialog, QLabel, QSlider, QLineEdit, QPushButton)

class ControlPanel(QDialog)   *
    """
    docstring for ControlPanel.
    """
    def __init__(self, document, actuator)   *
        super(ControlPanel, self).__init__()
        self.initUI(document, actuator)

    def initUI(self, document, actuator)   *
        # Setting up class parameters
        self.actuator = document.getObject(actuator)
        self.driver_type = self.getDriverType(self.actuator)
        self.steps_value = 10
        self.sequence = False
        if self.driver_type == "Angle"   *
            self.current_value = self.actuator.Angle
            self.start_value = (self.current_value - 15)
            self.end_value = (self.current_value + 15)
            self.unit_suffix = (" °")
        elif self.driver_type == "Distance"   *
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
        self.actuator_slider.setOrientation(QtCore.Qt.Horizontal)        # orientation horizontal
        self.actuator_slider.setGeometry(QtCore.QRect(30, 50, 330, 25))  # position coordinates
        self.actuator_slider.setObjectName("horizontalSlider")           # object name
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
        if self.driver_type == "Angle"   *
            self.actuator.Angle = self.current_value
        elif self.driver_type == "Distance"   *
            self.actuator.Distance = self.current_value
        else   *
            self.actuator.Offset = self.current_value
        self.label_current.setText("Current value   * " + str(round(self.current_value, 1)) + self.unit_suffix)
        FreeCADGui.updateGui() # screen update between steps
        Gui.runCommand("asm3CmdQuickSolve", 0)

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

def findTheDrivingConstraints(document_object)   *
    # search through the Objects and find the driving constraint
    driver_list = []
    for each in document_object.Objects   *
        if each.Label.endswith("Driver")   *
            driving_constraint = each.Name
            driver_list.append(driving_constraint)
    return driver_list

def main()   *
    kin_doc = App.ActiveDocument # Kinematic Document
    drivers = findTheDrivingConstraints(kin_doc)
    if len(drivers) < 1   *
        print("No driver found!")
    else   *
        panel_list = []
        for each_driver in drivers   *
            panel = ControlPanel(kin_doc, each_driver)
            panel_list.append(panel)
        panel.exec_()

if __name__ == "__main__"   *
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

And so another line edit widget is used to alter the number steps (placed after the existing line edit widgets)   *


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
    def onEntrySteps(self, new_steps)   *
        self.steps_value = int(new_steps)
...
```

The dialog window able to change the number of steps should look like this   *

<img alt="Dialog window with another text entry field" src=images/Tutorial_KinCon-06.png  style="width   *300px;"> 
*Dialog window with another text entry field* {{Top}}

#### Sekwencja obrazów 

Gdy ruch wykonywany przez złożenie spełnia nasze oczekiwania, możemy zrobić zdjęcie każdego kroku. Powstała sekwencja zdjęć może posłużyć do stworzenia krótkiej animacji gif.

Do realizacji tej funkcjonalności potrzebujemy widżetu {{Incode|QCheckBox}}, oraz katalogu do przechowywania obrazków.

Jeszcze jeden import i widżet   *


```python
import time
from PySide2.QtWidgets import (QDialog, QLabel, QSlider, QLineEdit, QPushButton, QCheckBox)
```

Wracając do metody {{Incode|initUI()}} wstawiamy pole wyboru po sekcji suwaka   *


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

Metoda {{Incode|onOutputClicked()}} synchronizuje parametr {{Incode|self.sequence}} i wyświetlenie znaku kontrolnego.


```python
...
    def onOutputClicked(self)   *
        if self.sequence == True   *
            self.sequence = False
            self.output_check.setChecked(False)
        else   *
            self.sequence = True
            self.output_check.setChecked(True)
...
```

Do określenia parametrów wyjściowych używamy metody {{Incode|output()}}   *


```python
...
    def output(self, counter)   *
        if (self.sequence == True)   *
            image_path = ".../FreeCAD/ScreenShots/Sequence"
            file_tag = ".png"
            height = 640
            width = 480
            background = "Transparent"
            # dealing with leading zeros
            if (counter > 999) or (counter < 0)   *
                print("Out of Range")
            elif (counter < 10)   *
                number = "00" + str(counter)
            elif (counter < 100)   *
                number = "0" + str(counter)
            else   *
                number = str(counter)
            # Screen shot
            Gui.activeDocument().activeView().saveImage(image_path + number + file_tag, height, width, background)
...
```

Przede wszystkim ścieżka do obrazów musi być dostosowana do Twojego systemu operacyjnego. Ostatnią częścią jest określenie nazwy obrazu bez numeru bieżącego i tagu pliku. Na razie trzeba to zrobić samodzielnie.

Następnie podążaj za tagiem pliku, aby zakończyć nazwę obrazu, nadać wysokość i szerokość obrazu oraz sposób wypełnienia tła ({{Incode|"Bieżące"}} *(tło widoku 3D)*, {{Incode|"Białe"}}, {{ Incode\|\"Czarne\"}} lub {{Incode|"Przezroczyste"}}).

Aby zawsze mieć trzycyfrową liczbę, należy przed parametrem licznika umieścić wiodące zera.

W końcu oskryptowana wersja polecenia <img alt="" src=images/Std_ViewScreenShot.svg  style="width   *24px;"> [Zrzut ekranu](Std_ViewScreenShot/pl.md) jest używana do robienia zdjęcia na podstawie wspomnianych parametrów.

Nadal nie zrobiono zdjęć!!! Nie ma problemu, ponieważ ta metoda nie została jeszcze wywołana, a więc musimy wstawić wywołanie w pętli *while* {{Incode|onForward()}} i {{Incode|onBackward()}}. Zaraz po {{Incode|time.sleep(0,2)}} wstawiamy tę linię   *


```python
...
            self.output(steps_left)
...
```

Teraz makrodefinicja powinno być gotowa do sterowania złożeniem oraz do robienia zdjęć do animowanego gifa.

Końcowa wersja okna dialogowego   *

<img alt="Dialog window finished" src=images/Tutorial_KinCon-07.png  style="width   *300px;"> 
*Ukończone okno dialogowe.*


<div class="mw-collapsible mw-collapsed">

**I wreszcie całe makro**


<div class="mw-collapsible-content">

\'\'\'Nie zapomnij ustawić ścieżki w metodzie output()!


```python
#! python
# -*- coding   * utf-8 -*-
# (c) 2021 Your name LGPL

# imports and constants
import time
from PySide2.QtWidgets import (QDialog, QLabel, QSlider, QLineEdit, QPushButton, QCheckBox)

class ControlPanel(QDialog)   *
    """
    docstring for ControlPanel.
    """
    def __init__(self, document, actuator)   *
        super(ControlPanel, self).__init__()
        self.initUI(document, actuator)

    def initUI(self, document, actuator)   *
        # Setting up class parameters
        self.actuator = document.getObject(actuator)
        self.driver_type = self.getDriverType(self.actuator)
        self.steps_value = 10
        self.sequence = False
        if self.driver_type == "Angle"   *
            self.current_value = self.actuator.Angle
            self.start_value = (self.current_value - 15)
            self.end_value = (self.current_value + 15)
            self.unit_suffix = (" °")
        elif self.driver_type == "Distance"   *
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
        self.actuator_slider.setInvertedAppearance(False)                # default   * right to left
        self.actuator_slider.setRange(0, 100)                            # default   * (0, 99)
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

    def onEntrySteps(self, new_steps)   *
        self.steps_value = int(new_steps)

    def onActuatorSlider(self, slider_value)   *
        self.current_value = slider_value * self.stepRatio() + self.start_value
        if self.driver_type == "Angle"   *
            self.actuator.Angle = self.current_value
        elif self.driver_type == "Distance"   *
            self.actuator.Distance = self.current_value
        else   *
            self.actuator.Offset = self.current_value
        self.label_current.setText("Current value   * " + str(round(self.current_value, 1)) + self.unit_suffix)
        FreeCADGui.updateGui() # screen update between steps
        Gui.runCommand("asm3CmdQuickSolve", 0)

    def onForward(self)   *
        steps_left = self.steps_value
        print(self.steps_value)
        step = ((self.end_value - self.current_value) / steps_left)
        while steps_left > 0   *
            self.current_value += step
            slider_value = ((self.current_value - self.start_value) / self.stepRatio())
            self.actuator_slider.setValue(slider_value)
            time.sleep(0.2)
            self.output(steps_left)
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
            self.output(steps_left)
            steps_left -= 1
        self.actuator_slider.setValue(0)

    def onClose(self)   *
        self.result = "Closed"
        self.close()

    def onOutputClicked(self)   *
        if self.sequence == True   *
            self.sequence = False
            self.output_check.setChecked(False)
        else   *
            self.sequence = True
            self.output_check.setChecked(True)

    def output(self, counter)   *
        if (self.sequence == True)   *
            image_path = ".../FreeCAD/ScreenShots/Sequence"
            file_tag = ".png"
            height = 640
            width = 480
            background = "Transparent"
            # dealing with leading zeros
            if (counter > 999) or (counter < 0)   *
                print("Out of Range")
            elif (counter < 10)   *
                number = "00" + str(counter)
            elif (counter < 100)   *
                number = "0" + str(counter)
            else   *
                number = str(counter)
            # Screen shot
            Gui.activeDocument().activeView().saveImage(image_path + number + file_tag, height, width, background)

# End of ControlPanel()
# Main section below   *

def findTheDrivingConstraints(document_object)   *
    # search through the Objects and find the driving constraint
    driver_list = []
    for each in document_object.Objects   *
        if each.Label.endswith("Driver")   *
            driving_constraint = each.Name
            driver_list.append(driving_constraint)
    return driver_list

def main()   *
    kin_doc = App.ActiveDocument # Kinematic Document
    drivers = findTheDrivingConstraints(kin_doc)
    if len(drivers) < 1   *
        print("No driver found!")
    else   *
        panel_list = []
        for each_driver in drivers   *
            panel = ControlPanel(kin_doc, each_driver)
            panel_list.append(panel)
        panel.exec_()

if __name__ == "__main__"   *
    # This will be true only if the file is "executed"
    # but not if imported as a module
    main()
```


</div>


</div>


{{Top}}

## Kilka niedoskonałości 

-   Kolejność sekwencji obrazów jest odwrócona, ponieważ używamy zmiennej steps_left, która jest odliczana.
-   Katalog obrazów i nazwa obrazu są zakodowane na sztywno.
-   Wiele kontrolerów nie jest zsynchronizowanych.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Tutorial KinematicController/pl
