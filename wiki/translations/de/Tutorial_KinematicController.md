---
 TutorialInfo:
   Topic: Kinematisteuerung erstellt mit Python
   Level: Pythongrundkentnisse sind hilfreich
   FCVersion: 0.20 und später
   Time: 1 Stunde
   Author: User:FBXL5
---

# Tutorial KinematicController/de







## Einleitung

Diese Anleitung beschreibt, wie man eine einfache Kinematiksteuerung aus ein paar Zeilen Python-Kode erstellt, die mit Baugruppen des Arbeitsbereiches [Assembly3](Assembly3_Workbench.md) verwendet werden kann.

Jeder Texteditor kann zum Erstellen von Kode genutzt werden. Mein Favorit ist Atom, aber FreeCADs eingebauter Editor funktioniert auch bestens.

Die folgenden Kode-Beispiele können kopiert, in eine leere Textdatei eingefügt und dann unter einem selbstgewählten Namen als ***.py** oder \****.FCMacro** abgespeichert werden.



## Makroabschnitte



### Grundstruktur


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

Die Grundstruktur besteht aus einer Hauptfunktion {{Incode|main()}} und einer Weiche, an der überprüft wird, ob das Makro als Behälter für Klassen, Methoden usw. verwendet wird oder ob es eigenständig läuft. Nur die zweite Möglichkeit startet die Hauptfunktion {{Incode|main()}}. Noch ist diese Funktion leer.



### Randbedingungen zum Antreiben finden 

Die Randbedingungen zum Antreiben (Antriebe) sind Objekte in einem FreeCAD-Dokument. Sie müssen markiert sein, um gefunden zu werden.

Für diese Steuerung muss das Suffix {{Incode|"Driver"}} an das Label eines Antriebs angehängt werden. Es kann zur Verdeutlichung mit einem {{Incode|"."}} oder {{Incode|"-"}} abgetrennt werden, da nur geprüft wird ob das Label auf {{Incode|"Driver"}} endet.

Eine Funktion, der das Dokumentobjekt übergeben wird und die eine Liste von Antrieben zurück gibt, wird diese Arbeit erledigen.


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

Die Hauptfunktion {{Incode|main()}} lädt das aktive Dokument in die Variable {{Incode|kin_doc}} und ruft im Anschluss die Funktion {{Incode|findTheDrivingConstraints()}} (Antriebs-Randbedingungen finden) auf und übergibt den Inhalt von {{Incode|kin_doc}}. Die zurückgegebene Liste wird in die Variable {{Incode|drivers}} abgelegt, die dann überprüft wird, ob sie wenigstens ein Element enthält. Wenn das der Fall ist, wird die Liste im [Ausgabefenster](Report_view.md) angezeigt.


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

**Das Makro bis hierhin\...**


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



### Steuerungsfenster

Das Steuerungsfenster ist aus Qt-Widgets (**wi**ndow ga**dgets** \~ Fenstergelöt) aufgebaut, einem Hauptfenster und einigen Ein- und Ausgabe-Widgets.

Alle Widgets müssen importiert werden, bevor sie verwendet werden können, aber sie können als ein kompletter Satz importiert werden.



#### Hauptfenster

Für das Hauptfenster sieht die Import-Zeile so aus:


```python
from PySide2.QtWidgets import (QDialog)
```

Das Hauptfenster, {{Incode|ControlPanel}} genannt, ist ein Klassenobjekt, das eine Instanz des {{Incode|QDialog}}-Widgets ist.

Es enthält zwei init-Methoden. {{Incode|__init__()}} initialisiert das neue Klassenobjekt, verarbeitet eingehende Variablen und startet {{Incode|initUI()}}, die alle Widgets innerhalb des Hauptfensters verwaltet.


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

Um ein einzelnes Steuerungsfenster zu starten, wird eine Instanz dieser Klasse namens {{Incode|panel}} erstellt, mit {{Incode|kin_doc}} (dem Dokumentobjekt) und {{Incode|drivers[0]}} (dem ersten Element auf der Liste der Antriebe), die an diese Instanz übergeben wurden. Schließlich öffnet die Methode {{Incode|exec_()}} der Klasse das Dialogfenster.


```python
panel = ControlPanel(kin_doc, drivers[0])
panel.exec_()
```

Um mehr als eine Antrieb zu verwenden, muss die Liste der Antriebe durchgesehen werden und für jedes Element der Liste eine Instanz erstellt werden, der das jeweilige Element übergeben wird.


```python
panel_list = []
for each_driver in drivers:
    panel = ControlPanel(kin_doc, each_driver)
    panel_list.append(panel)
panel.exec_()
```

Diese Zeilen ersetzen den Ausgabebefehl {{Incode|print()}} im else-Abschnitt der Hauptfunktion {{Incode|main()}}.

Hinweis: Das Zusammenstellen einer {{Incode|panel_list}} (Fensterliste) erlaubt es alle Fenster auf einmal zu starten. (Ich kann dieses Verhalten bisher nicht erklären\...)

Lässt man das Makro laufen, erstellt es ein sauberes, leeres Dialogfenster, das auf Widgets wartet.

<img alt="Ein leeres Dialogfenster" src=images/Tutorial_KinCon-01.png  style="width:300px;">


<div class="mw-collapsible mw-collapsed">

**Das Makro bis hierhin\...**


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



#### Parameter setzen 

Nun ist es Zeit die Methode {{Incode|initUI()}} zu befüllen:


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

repräsentiert den Antrieb und {{Incode|self.driver_type}} Speichert ein Schlüsselwort für die Art des Antriebs. Letztere sorgt dafür, dass jeder Randbedingung die richtige Eigenschaft zugeordnet wird.



##### Methode getDriverType() 

Für spätere Verwendung muss die Art des Antriebs ermittelt werden, Winkel, Abstand oder Länge (Angle, Distance, Length), daher muss eine Methode namens {{Incode|getDriverType()}} (Finde den Antriebstyp) definiert werden.


```python
...
    def getDriverType(self, constraint):
        ANGLE_CONSTRAINTS = [
            "PlaneCoincident",
            "AxialAlignment",
            "PlaneAlignment"
            ] # Angel constraints that use negative values, too
        ANGLE_DEG_CONSTRAINTS = [
            "Angle",
            ] # Angel constraints that use positive values only
        DISTANCE_CONSTRAINTS = [
            "PointDistance",
            "PointsDistance"
            ] # Lenght constraints that use positive values only
        if constraint.ConstraintType in ANGLE_CONSTRAINTS:
            return "Angle"
        elif constraint.ConstraintType in ANGLE_DEG_CONSTRAINTS:
            return "AnglePos"
        elif constraint.ConstraintType in DISTANCE_CONSTRAINTS:
            return "Distance"
        else:
            return "Length"
...
```

Diese Methode überprüft, ob die Art der gegebenen Randbedingung in einer der Listen zu finden ist, und gibt zurück, welche Art Maß zu steuern ist

Es wird angenommen, dass der Antrieb im Kinematikdokument korrekt markiert wurde und funktioniert, wenn er von Hand geändert wird. In diesem Falle ist es nicht nötig geometrische Randbedingungen wie Colinear oder PointsCoincidence herauszufiltern (aber hier wäre die Stelle es zu tun\...)



##### Fenstereigenschaften

Die Fenstergröße wird über seine Größt- und Kleinstmaße festgelegt. Verwendet man jeweils dieselben Werte, wird eine konstante Größe festgelegt

Im Titel findet sich der Name des Antriebs und ob es sich um einen Winkel, einen Abstand oder eine Länge handelt. Schließlich wird das Fenster angewiesen über allen anderen Fenstern (sichtbar) zu bleiben.


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



#### Weitere Parameter setzen 

Im nächsten Schritt wird der Wert des Antriebs ausgelesen und die Start- und Endwerte abhängig von der Antriebsart gesetzt.

Ein Abstand kann nicht negativ sein und exakt null verwirrt den Gleichungslöser, daher wird der Startwert auf 0,001 gesetzt. Winkel akzeptieren negative Werte und erhalten symmetrische Werte. (Ob Längen negative Werte akzeptieren, muss noch abschließend festgestellt werden\...)

Die Einheiten müssen gespeichert werden, bis die Werte am Ende an die Eigenschaften der Randbedingungen zurückgegeben werden. Abstände und Längen benötigen Werte mit Einheiten.

Der Umgang mit Einheiten und die Darstellung der Werte als Zeichenketten in einigen Widgets erfordert es häufig Zahlen in Zeichenketten und wieder zurück zu verwandeln.

Um die Parameter zu vervollständigen, wird ein Wert für die Anzahl von Schritten vorgegeben, die berechnet werden solle, wenn die Bewegung automatisch erfolgt; und wenn der Umschalter {{Incode|self.sequence}} auf {{Incode|True}} gesetzt ist, wird bei jedem Schritt der Bewegung ein Bild aufgenommen.


```python
...
        self.steps_value = 10
        self.sequence = False
        if self.driver_type == "Angle":
            self.current_value = self.actuator.Angle
            self.start_value = (self.current_value - 15)
            self.end_value = (self.current_value + 15)
            self.unit_suffix = (" °")
        elif self.driver_type == "AnglePos":
            self.current_value = float(str(self.actuator.Angle)[:-4])
            self.start_value = 0.001 # Angle must not be <= 0 and >=180
            self.end_value = 179.999
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



#### Label

Nun werden drei Label(-Widgets) hizugefügt, um Start-, End-, sowie den aktuellen Wert anzuzeigen

Zuerst muss die Klasse {{Incode|QLabel}} importiert werden, d. h. die Import-Liste muss, wie hier gezeigt wird, ergänzt werden:


```python
from PySide2.QtWidgets import (QDialog, QLabel)
```

Zurück in der Methode {{Incode|initUI()}} fügt man folgendes ein:


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

Die Platzierung erfolgt mit der ererbten Methode {{Incode|setGeometry()}}. In diesem Falle wird die Beschreibung eines Rechtecks verwendet (X-Position, Y-Position, Breite, Höhe)

Die ersten und dritten Zeilen könnten zusammengefasst werden, wird aber aus Gründen der Übersichtlichkeit nicht empfohlen.


```python
self.label_end = QLabel((str(round(self.end_value, 1)) + self.unit_suffix), self)
```

Startet man das Makro aus einem Kinematikdokument heraus, erhält man ein Dialogfenster wie dieses:

<img alt="Ein Dialogfenster, das den Startwert, den aktuellen Wert und den Endwert anzeigt" src=images/Tutorial_KinCon-02.png  style="width:300px;"> 
*Das Dialogfenster zeigt in der Titelleiste das Label der Randbedingung und die Art des Antriebs an, sowie den Startwert, den aktuellen Wert und den Endwert in der ersten Zeile des Hauptbereiches*


<div class="mw-collapsible mw-collapsed">

**Das Makro bis hierhin\...**


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
        elif self.driver_type == "AnglePos":
            self.current_value = float(str(self.actuator.Angle)[:-4])
            self.start_value = 0.001 # Angle must not be <= 0 and >=180
            self.end_value = 179.999
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
            "PlaneCoincident",
            "AxialAlignment",
            "PlaneAlignment"
            ] # Angel constraints that use negative values, too
        ANGLE_DEG_CONSTRAINTS = [
            "Angle",
            ] # Angel constraints that use positive values only
        DISTANCE_CONSTRAINTS = [
            "PointDistance",
            "PointsDistance"
            ]
        if constraint.ConstraintType in ANGLE_CONSTRAINTS:
            return "Angle"
        elif constraint.ConstraintType in ANGLE_DEG_CONSTRAINTS:
            return "AnglePos"
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



#### Schieberegler

Um den aktuellen Wert auf jede mögliche Zahl zwischen Start- und Endwert einzustellen, würde ein Schieberegler passen.

Zuerst muss die Klasse {{Incode|QSlider}} importiert werden, d. h. die Import-Liste muss, wie hier gezeigt wird, ergänzt werden:


```python
from PySide2.QtWidgets import (QDialog, QLabel, QSlider)
```

Zurück in der Methode {{Incode|initUI()}} fügt man folgendes direkt nach dem Labels-Abschnitt ein:


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

Der Schieberknopf wird mit der Methode {{Incode|setValue()}} platziert. Sein Wert muss aus dem aktuellen Wert und dem Schrittverhältnis berechnet werden. Das Schrittverhältnis muss immer berechnet werden, wenn sich der Start- oder Endwert ändert, daher wird eine weitere Methode hinter der Methode {{Incode|getDriverType()}} eingefügt.

Ein Verhältnis zu verwenden anstatt die Kleinst- und Größtwerte des Schiebereglers zu verändern, hat den Vorteil einer feineren Auflösung für kleinere Werte.


```python
...
    def stepRatio(self):
        ratio = (self.end_value - self.start_value) / 100
        return ratio
...
```

Und nach diesem kommt eine weitere Methode, die festlegt, was zu tun ist, wenn sich die Position des Schiebers bzw. der Wert des Schiebereglers ändert. Die Methode {{Incode|onActuatorSlider()}} wird von der Methode {{Incode|connect()}} aufgerufen, die auch den Wert des Schhiebereglers als Variable übergibt.

Sie berechnet den aktuellen Wert erneut aus der Schieberposition, überschreibt den Text des Labels {{Incode|self.label_current}} und ändert die Eigenschaft der Randbedingung unter Beachtung der Art des Antriebs.

Wird der Befehl {{Incode|"asm3CmdQuickSolve"}} gestartet, beginnt der Gleichnungslöser die Bestandteile der Baugruppe dem geänderten Wert entsprechend neu anzuordnen.


```python
...
    def onActuatorSlider(self, slider_value):
        self.current_value = slider_value * self.stepRatio() + self.start_value
        if self.driver_type == "Angle":
            self.actuator.Angle = self.current_value
        elif self.driver_type == "AnglePos":
            self.actuator.Angle = self.current_value
        elif self.driver_type == "Distance":
            self.actuator.Distance = self.current_value
        else:
            self.actuator.Offset = self.current_value
        self.label_current.setText("Current value: " + str(round(self.current_value, 1)) + self.unit_suffix)
        Gui.runCommand("asm3CmdQuickSolve", 0)
...
```

Das Dialogfenster mit dem Schieberegler sollte so aussehen und ist jetzt bereit eine Bewegung zu steuern.

<img alt="Zwei Dialogfenster mit Schieberegler" src=images/Tutorial_KinCon-03.png  style="width:300px;"> 
*Dialogfenster mit dem hinzugefügten Schieberegler, eins für einen Winkelantrieb (Drehantrieb) und eins für einen (Abstands-/) Linearantrieb*

Es kann ein Dialogfenster für jedes geöffnete Dokument gestartet werden; sie beeinflussen sich nicht gegenseitig. 

#### Texteingabefelder

Um Start- und Endwerte zu ändern kann man ein Line-Edit-Widget verwenden.

Zuerst muss die Klasse {{Incode|QLineEdit}} importiert werden, d. h. die Import-Liste muss, wie hier gezeigt wird, ergänzt werden:


```python
from PySide2.QtWidgets import (QDialog, QLabel, QSlider, QLineEdit)
```

Zurück in der Methode {{Incode|initUI()}} fügt man folgendes zwischen Labels- und Slider-Abschnitt ein:


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

Die Eingabefelder zeigen die voreingestellten Start- und Endwerte an. Sie sind aber erst komplett, wenn auch Methoden hinzugefügt werden, die die geänderten Werte verarbeiten. Das erledigen die Methoden {{Incode|self.onEntryStart()}} und {{Incode|self.onEntryEnd()}}, die zwischen den Methoden {{Incode|self.stepRatio()}} und {{Incode|self.onActuatorSlider()}} eingefügt werden.


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

Beide wandeln die erhaltene Zeichenkette in eine Fließkommazahl und ändern den Startwert {{Incode|self.start_value}} bzw. Endwert {{Incode|self.end_value}} und das dazugehörige Label. Danach wird der Schieber aktualisiert.

Das Dialogfenster mit den Texteingabefeldern sollte so aussehen und ist jetzt bereit den Bereich einer Bewegung zu ändern:

<img alt="Zwei Dialogfenster mit Texteingabefeldern" src=images/Tutorial_KinCon-04.png  style="width:300px;"> 
*Dialogfenster mit Texteingabefeldern, nochmals für Drehantrieb und Linearantrieb*


<div class="mw-collapsible mw-collapsed">

**Das Makro bis hierhin\...**


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
        elif self.driver_type == "AnglePos":
            self.current_value = float(str(self.actuator.Angle)[:-4])
            self.start_value = 0.001 # Angle must not be <= 0 and >=180
            self.end_value = 179.999
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
            "PlaneCoincident",
            "AxialAlignment",
            "PlaneAlignment"
            ] # Angel constraints that use negative values, too
        ANGLE_DEG_CONSTRAINTS = [
            "Angle",
            ] # Angel constraints that use positive values only
        DISTANCE_CONSTRAINTS = [
            "PointDistance",
            "PointsDistance"
            ] # Lenght constraints that use positive values only
        if constraint.ConstraintType in ANGLE_CONSTRAINTS:
            return "Angle"
        elif constraint.ConstraintType in ANGLE_DEG_CONSTRAINTS:
            return "AnglePos"
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
        elif self.driver_type == "AnglePos":
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



### Bewegung

um einen Zusammenbau in Bewegung zu setzen benötigt man:

-   Schaltflächen, die eine Bewegung in die gewünschte Richtung auslösen.
-   Ein Eingabefeld, um die Anzahl der schritte zu verändern, für schnellere oder fließendere Bewegungen.
-   Ein Optionsfeld (Checkbox), um das Erstellen einer Bildfolge zu aktivieren.



#### Vorwärts- und Rückwärts-Schaltflächen 

Damit sich die Bauteile automatisch bewegen, werden zwei Schaltflächen benötigt, die die Bewegungen auslösen, eine in Richtung der Startposition und eine in Richtung der Endposition. Diese beiden und eine zum Schließen verwenden das Widget {{Incode|QPushButton}}.

Kleinere Baugruppen werde etwas zu schnell berechnet und zeigen eher Sprünge anstatt einer fließenden Bewegung. Um sie zu verlangsamen wird die Methode {{Incode|sleep()}} des Moduls {{Incode|time}} verwendet, das zuerst importiert werden muss.

Ein weiterer Import und ein weiteres Widget:


```python
import time
from PySide2.QtWidgets import (QDialog, QLabel, QSlider, QLineEdit, QPushButton)
```

Zurück in der Methode {{Incode|initUI()}} fügt man folgendes nach dem Slider-Abschnitt ein:


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

Die Methoden, die gedrückte Schaltflächen bearbeiten sind {{Incode|self.onForward()}}, {{Incode|self.onBackward()}}, und {{Incode|self.onClose()}}. Sie werden nach der Methode {{Incode|onActuatorSlider()}} eingefügt.


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

Die Methode {{Incode|self.onClose()}} ruft die ererbte Methode {{Incode|self.close()}} auf, die nur das Dialogfenster schließt und damit das Makro beendet.

Beide Methoden {{Incode|self.onForward()}} und {{Incode|self.onBackward()}} zählen die verbleibenden Schritte, die noch zu gehen sind, bis man die gewünschte Position erreicht und berechnen die Schrittlänge entsprechend der Anzahl der Schritte. Zu diesem Zeitpunkt wird die voreingestellte Anzahl von zehn Schritten beibehalten.

Jede Runde in der While-Schleife erhöht/verringert den aktuellen Wert und aktualisiert den Schieber, wodurch im Hintergrund {{Incode|onActuatorSlider()}} ausgelöst wird (siehe Absatz [Schieberegler](#Schieberegler.md)).

Wenn keine Schritte mehr übrig sind, wird der Schieber auf die erste bzw. letzte Position gesetzt, nur für den Fall, dass Rundungsfehler aufgetreten sind.

Das Dialogfenster mit den Schalflächen sollte so aussehen und kann jetzt einen Zusammenbau mit 10 Schritten auf die gewünschte Position bewegen:

<img alt="Dialogfenster mit Schaltflächen" src=images/Tutorial_KinCon-05.png  style="width:300px;"> 
*Dialogfenster mit Schaltflächen*


<div class="mw-collapsible mw-collapsed">

**Das Makro bis hierhin\...**


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
        elif self.driver_type == "AnglePos":
            self.current_value = float(str(self.actuator.Angle)[:-4])
            self.start_value = 0.001 # Angle must not be <= 0 and >=180
            self.end_value = 179.999
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
            "PlaneCoincident",
            "AxialAlignment",
            "PlaneAlignment"
            ] # Angel constraints that use negative values, too
        ANGLE_DEG_CONSTRAINTS = [
            "Angle",
            ] # Angel constraints that use positive values only
        DISTANCE_CONSTRAINTS = [
            "PointDistance",
            "PointsDistance"
            ] # Lenght constraints that use positive values only
        if constraint.ConstraintType in ANGLE_CONSTRAINTS:
            return "Angle"
        elif constraint.ConstraintType in ANGLE_DEG_CONSTRAINTS:
            return "AnglePos"
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
        elif self.driver_type == "AnglePos":
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



#### Anzahl der Schritte 

Die Voreinstellung ist so gewählt, dass man einen schnellen Eindruck erhält, ob sich der Zusammenbau wie erwartet bewegt, ohne zu viel Rechenzeit zu verbrauchen.

Wenn die Bauteile eher springen als sich fließend zu bewegen, oder wenn winkelbasierte Antriebe Problemen bereiten, wenn der Unterschied zwischen zwei Winkeln zu groß ist, dann kann beides durch das Erhöhen der Anzahl der Schritte behoben werden.

Und ein weiteres Line-Edit-Widget wird verwendet, um die Anzahl der Schritte zu ändern (eingesetzt hinter den schon vorhandenen Line-Edit-Widgets):


```python
...
        # text input field - number of steps
        self.entry_steps = QLineEdit(self)
        self.entry_steps.setText(str(int(self.steps_value)))
        self.entry_steps.setGeometry(QtCore.QRect(180, 80, 50, 25))
        self.entry_steps.textChanged[str].connect(self.onEntrySteps)
...
```

Die zugehörige Methode {{Incode|self.onEntrySteps()}} füllt nur den Parameter {{Incode|self.step_value}} mit dem eingegebenen Wert. Sie wird nach der Methode {{Incode|onEntryEnd()}} eingefügt.


```python
...
    def onEntrySteps(self, new_steps):
        self.steps_value = int(new_steps)
...
```

Das Dialogfenster, das in der Lage ist, die Anzahl der Schritte zu ändern sollte so aussehen:

<img alt="Dialogfenster mit einem weiteren Texteingabefeld" src=images/Tutorial_KinCon-06.png  style="width:300px;"> 

#### Bildfolge

Sobald die Bewegung der Bauteile den Erwartungen entspricht, kann bei jedem Schritt ein Bild aufgenommen werden. Aus der entstandenen Bildfolge kann eine kurze GIF-Animation erstellt werden.

Um diese Funktionalität einzubauen, wird das Widget {{Incode|QCheckBox}} und ein Verzeichnis zum Speichern der Bilder gebraucht.

Ein weiterer Import und ein weiteres Widget:


```python
import time
from PySide2.QtWidgets import (QDialog, QLabel, QSlider, QLineEdit, QPushButton, QCheckBox)
```

Zurück in der Methode {{Incode|initUI()}} fügt man folgendes nach dem Slider-Abschnitt ein:


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

Die Methode {{Incode|onOutputClicked()}} synchronisiert den Parameter {{Incode|self.sequence}} und die Anzeige des Aktivierungshäkchens.


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

Um die Ausgabeparameter festzulegen wird die Methode {{Incode|output()}} verwendet:


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

Zuerst muss der Pfad zu den Bilddateien an das eigene Betriebssystem angepasst werden; der letzte Teil des Bildnamens bleibt ohne Zählnummer und Dateianhang. Dies muss zur Zeit von Hand gemacht werden.

Dann folgt der Dateianhang, um den Bildnamen abzuschließen, Bildhöhe und -Breite sowie eine Angabe, wie der Bildhintergrund gefüllt werden soll ({{Incode|"Current"}} (aktueller Hintergrund der 3D-Ansicht), {{Incode|"White"}} (weiß), {{Incode|"Black"}} (schwarz), oder {{Incode|"Transparent"}}).

Damit immer eine dreistellige Zahl verwendet wird, müssen führende Nullen vor der Zählvariable eingefügt werden.

Am Ende wird die Skriptvariante des Befehls <img alt="" src=images/Std_ViewScreenShot.svg  style="width:24px;"> [Std AnsichtAufnehmen](Std_ViewScreenShot/de.md) verwendet, um mit Hilfe der genannten Parameter ein Bild aufzunehmen.

Es werden noch keine Bilder aufgenommen!?! Kein Problem, da diese Methode noch nicht aufgerufen wird, und daher muss noch ein Aufruf in die While-Schleife von {{Incode|onForward()}} und {{Incode|onBackward()}} eingefügt werden. Direkt nach {{Incode|time.sleep(0.2)}} wird diese Zeile eingefügt:


```python
...
            self.output(steps_left)
...
```

Jetzt sollte das Makro bereit sein, einen (kinematischen) Zusammenbau zu steuern und Bilder für ein animiertes GIF-Billd aufzunehmen.

Die endgültige Version des Dialogfensters:

<img alt="Fertiges Dialogfenster" src=images/Tutorial_KinCon-07.png  style="width:300px;"> 
*Fertiges Dialogfenster*


<div class="mw-collapsible mw-collapsed">

**Und schließlich das ganze Makro**


<div class="mw-collapsible-content">

**Nicht vergessen den Pfad in der Ausgabemethode output() anzugeben!**


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
        elif self.driver_type == "AnglePos":
            self.current_value = float(str(self.actuator.Angle)[:-4])
            self.start_value = 0.001 # Angle must not be <= 0 and >=180
            self.end_value = 179.999
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
            "PlaneCoincident",
            "AxialAlignment",
            "PlaneAlignment"
            ] # Angel constraints that use negative values, too
        ANGLE_DEG_CONSTRAINTS = [
            "Angle",
            ] # Angel constraints that use positive values only
        DISTANCE_CONSTRAINTS = [
            "PointDistance",
            "PointsDistance"
            ] # Lenght constraints that use positive values only
        if constraint.ConstraintType in ANGLE_CONSTRAINTS:
            return "Angle"
        elif constraint.ConstraintType in ANGLE_DEG_CONSTRAINTS:
            return "AnglePos"
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
        elif self.driver_type == "AnglePos":
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



## Ein paar Schwachstellen 

-   Die Numerierung der Bildfolge ist umgekehrt, da die Variable steps_left (verbleibende Schritte) heruntergezählt wird.
-   Das Bildverzeichnis und der Name des Bildes sind im Makro hinterlegt (hard-coded).
-   Mehrfach geöffnete Steuerungsfenster sind nicht synchronisiert.



---
⏵ [documentation index](../README.md) > Tutorial KinematicController/de
