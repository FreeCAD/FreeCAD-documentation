# Mouse navigation/de
{{TOCright}}

## Overview


<div class="mw-translate-fuzzy">

## Überblick

Die FreeCAD **Mausnavigation** besteht aus den verwendeten Befehlen zur visuellen Navigation im 3D Raum und zur Interaktion mit den angezeigten Objekten. FreeCAD unterstützt mehrere Mausmodell Navigationsstile. Der standardmäßige Navigationsstil wird als \"CAD Navigation\" bezeichnet und ist sehr einfach und praktisch, jedoch bietet FreeCAD auch alternative Navigationsstile, die du nach deinen Vorlieben auswählen kannst.


</div>

## Navigation


<div class="mw-translate-fuzzy">

## Navigation 

Die für die Objekthandhabung verwendeten Mausgesten variieren je nach ausgewähltem Navigationsstil; der aktuell ausgewählte Stil wird für alle Arbeitsbereiche verwendet.


</div>

Es gibt zwei Möglichkeiten, um den Navigationsstil zu ändern:

-   Im [Voreinstellungseditor](Preferences_Editor/de#Navigation.md); Menü {{MenuCommand/de|Bearbeiten → Einstellungen → Anzeige → Navigation → 3D Navigation}}.
-   Durch Rechtsklick in den leeren Bereich in der 3D Ansicht, dann Auswahl von {{MenuCommand/de|Navigationsstile}} im Kontextmenü.

### CAD navigation 


<div class="mw-translate-fuzzy">

### CAD Navigation 

Dies ist der Standard Navigationsstil. Er ermöglicht dem Benutzer eine einfache Steuerung der Ansicht und erfordert keine Verwendung von Tastaturtasten, außer um Mehrfachauswahlen zu treffen.


</div>


{{CAD Navigation
|Select_name=Auswählen
|Pan_name=Schwenken
|Zoom_name=Zoom
|Rotate_view_name=Ansicht drehen<br>Erste Methode
|Rotate_view_alt_name=Ansicht drehen<br>Ersatz Methode
|Ctrl=**Strg**
|Shift=**Shift**
|Select_text=Drücke die linke Maustaste über einem Objekt das du auswählen möchtest.

Niederhalten **Strg** ermöglicht die Auswahl mehrerer Objekte.
|Pan_text=Halte die mittlere Maustaste gedrückt und bewege den Mauszeiger.
|Pan_mode_text=Pan Modus: Halte die **Strg** Taste gedrückt, drücke einmal die rechte Maustaste und bewege dann den Mauszeiger.  {{Version/de|0.17}}
|Zoom_text=Verwende das Mausrad, um ein- und auszuzoomen.

Die mittleren Maustaste klicken zentriert die Ansicht wieder auf die Position des Cursors.
|Zoom_mode_text=Zoom Modus: Halte die **Strg** und **Shift** Tasten, drücke einmal die rechte Maustaste und bewege dann den Zeiger. {{Version/de|0.17}}
|Rotate_view_text=Halte die mittlere Maustaste, dann drücke und halte die linke Maustaste, dann bewege den Mauszeiger.

Die Cursorposition beim Drücken der mittleren Maustaste bestimmt den Drehmittelpunkt. Die Drehung funktioniert wie das Drehen einer Kugel, die sich um ihr Zentrum dreht. Wenn die Tasten losgelassen werden, bevor du die Mausbewegung stoppst, wird die Ansicht [Std DemoModus](spinning/de.md) fortgesetzt, sofern dies aktiviert ist.

Ein Doppelklick mit der mittleren Maustaste setzt einen neuen Drehmittelpunkt.
|Rotate_view_mode_text=Dreh-Modus: Halte die Taste **Shift** gedrückt, drücke einmal die rechte Maustaste und bewege den Mauszeiger. {{Version/de|0.17}}
|Rotate_view_alt_text=Halte die mittlere Maustaste gedrückt, dann drücke und halte die rechte Maustaste und bewege den Mauszeiger.

Mit dieser Methode kann die mittlere Maustaste losgelassen werden, nachdem die rechte Maustaste gedrückt gehalten wird.

Anwender, die die Maus mit der rechten Hand benutzen, finden diese Methode möglicherweise einfacher als die erste Methode.
}}

### OpenInventor navigation 


<div class="mw-translate-fuzzy">

### OpenInventor Navigation 

Die OpenInventor Navigation (ehemals Inventor) wurde nach dem Vorbild von [Open Inventor](http://en.wikipedia.org/wiki/Open_Inventor) gestaltet. Um Objekte auszuwählen, muss du die **Strg** Taste gedrückt halten.


</div>

Dieser Modus basiert nicht auf Autodesk Inventor.


{{OpenInventor Navigation
|Select_name=Auswählen
|Pan_name=Schwenken
|Zoom_name=Zoom
|Rotate_view_name=Ansicht drehen
|Ctrl=**Strg**
|Select_text=Halte die Taste **Strg** gedrückt und drücke dann die linke Maustaste über einem Objekt, das ausgewählt werden soll.
|Pan_text=Halte die mittlere Maustaste gedrückt und bewege den Mauszeiger.
|Zoom_text=Verwende das Mausrad, um ein- und auszuzoomen.

Alternativ halte die mittlere Maustaste, dann drücke und halte die linke Maustaste, dann bewege den Mauszeiger. 
|Rotate_view_text=Halte die linke Maustaste, dann bewege den Mauszeiger.
}}


<div class="mw-translate-fuzzy">

### Blender Navigation 


</div>

Der Blender Navigationsstil wurde nach [Blender](https://www.blender.org) gestaltet. Zuvor gab es kein reines Schwenken mit der Maus; es erforderte immer die **Shift** Taste gedrückt zu halten. Dies änderte sich 2016, jetzt kannst du zum Schwenken sowohl die linke als auch die rechte Maustaste gedrückt halten. {{Blender Navigation
|Select_name=Auswählen
|Pan_name=Schwenken
|Zoom_name=Zoom
|Rotate_view_name=Ansicht drehen
|Shift=**Shift**
|Select_text=Drücke die linke Maustaste über einem Objekt, das ausgewählt werden soll.
|Pan_text=Halte **Shift** und die mittlere Maustaste gedrückt und bewege dann den Mauszeiger.

Alternativ kann auch die linke und rechte Maustaste gedrückt gehalten und der Mauszeiger bewegt werden.
|Zoom_text=Verwende das Mausrad, um ein- und auszuzoomen.
|Rotate_view_text=Halte die mittlere Maustaste gedrückt und bewege den Mauszeiger.
}}


<div class="mw-translate-fuzzy">

### Touchpad Navigation 


</div>

In der Touchpad-Navigation erfordern das Schwenken, Zoomen und Drehen der Ansicht eine Modifizierungstaste zusammen mit dem Touchpad. {{Touchpad Navigation
|Select_name=Auswählen
|Pan_name=Schwenken
|Zoom_name=Zoom
|Rotate_view_name=Ansicht drehen
|Shift=**Shift**
|Ctrl=**Strg**
|Alt=**Alt**
|PageUp=**PageUp**
|PageDown=**PageDown**
|Select_text=Drücke die linke Maustaste über einem Objekt, das ausgewählt werden soll.
|Pan_text=Halte **Shift**, und bewege dann den Mauszeiger.
|Zoom_text=Verwende **PageUp** und **PageDown** um hinein- und herauszuzoomen.
|Zoom_alt_text=Alternativ kann **Shift** und **Strg** gedrückt gehalten und dann der Mauszeiger bewegt werden.
|Rotate_view_text=Halte **Alt** gedrückt und bewege dann den Mauszeiger.
|Rotate_view_alt_text=Alternativ kann **Shift** und die linke Taste gedrückt gehalten und dann der Mauszeiger bewegt werden.
}}


<div class="mw-translate-fuzzy">

### Gestennavigation


</div>

Dieser Stil wurde in der Version 0.16 eingeführt und ist auf die Verwendung mit Touchscreen und Stift zugeschnitten, er kann auch mit einer Maus verwendet werden und wird für die Verwendung empfohlen, wenn ein Mac mit einem Trackpad benutzt wird. {{Gesture Navigation
|Select_name=Auswählen
|Pan_name=Schwenken
|Zoom_name=Zoom
|Rotate_view_name=Ansicht drehen
|Tilt_view_name=Ansicht kippen
|Select_text=Über einem Objekt, das ausgewählt werden soll, die linke Maustaste drücken.
|Select_gesture_text=Zum Auswählen tippen.
|Pan_text=Die rechte Maustaste halten und den Mauszeiger bewegen.
|Pan_gesture_text=Mit zwei Fingern ziehen.

Oder tippen, halten und dann ziehen. Dies simuliert das Schwenken mit der rechten Maustaste.
|Zoom_text=Mit dem Mausrad hinein- und hinauszoomen.
|Zoom_gesture_text=Zwei Finger (Kneifen) näher oder weiter auseinanderziehen.
|Rotate_view_text=Die rechte Maustaste halten und den Mauszeiger bewegen.
Im [Skizzierer](Sketcher_Workbench/de.md) und in anderen Bearbeitungsmodi ist dieses Verhalten nicht gegeben. Für den Rotationsmodus die **Alt**-Taste halten, wenn eine Maustaste gedrückt wird.

Um den Fokuspunkt der Kamera für die Rotation festzulegen, klicken Sie mit der mittleren Maustaste auf einen Punkt. Alternativ können Sie den Cursor auf einen Punkt richten und **H** auf der Tastatur drücken.
|Rotate_view_gesture_text=Mit einem Finger ziehen, um zu rotieren.

Im [Skizzierer](Sketcher_Workbench/de.md) die **Alt**-Taste halten.
|Tilt_view_text=Die linke und rechte Maustaste halten und den Mauszeiger seitwärts bewegen. 
|Tilt_view_gesture_text=Die imaginäre Linie rotieren, die durch zwei Berührungspunkte gebildet wird.

In der Version 0.18 ist diese Methode per Voreinstellung deaktiviert. Im **Bearbeiten → Einstellungen → Anzeige**, das Häckchen bei "Deaktiviere die Touchscreen Neige Geste" entfernen, um sie zu aktivieren.
}}


<div class="mw-translate-fuzzy">

### Maya-Gestennavigation 


</div>

In der Maya-Gestennavigation werden Schwenken, Zoomen und Drehen durch Drücken der **ALT**- und einer Maustaste aktiviert. Daher wird eine 3-Tasten-Maus benötigt. Es ist auch möglich, Gesten zu verwenden, da dieser Modus über den [Gestennavigationsmodus](#Gestennavigation.md) entwickelt wurde. {{MayaGesture Navigation
|Select_name=Auswählen
|Pan_name=Schwenken
|Zoom_name=Zoom
|Rotate_view_name=Ansicht drehen
|Alt=**Alt**
|Select_text=Drücke die linke Maustaste über einem Objekt, das du auswählen möchtest.
|Pan_text=Halte **Alt** und die mittlere Maustaste, dann bewege den Zeiger.
|Zoom_text=Halte **Alt** und die rechte Maustaste gedrückt, und bewege dann den Zeiger.

Oder mit dem Mausrad hinein- oder hinauszoomen.
|Rotate_view_text=Die **Alt**-Taste und die linke Maustaste halten und den Mauszeiger bewegen.
}}


<div class="mw-translate-fuzzy">

### Revit Navigation 


</div>

Dieser Stil wurde in Version 0.18 eingeführt.


{{Revit Navigation
|Select_name=Auswählen
|Pan_name=Schwenken
|Zoom_name=Zoom
|Rotate_view_name=Ansicht drehen
|Shift=**Shift**
|Select_text=Mit dem Mauszeiger über einem Objekt die linke Maustaste drücken, um das Objekt auszuwählen.
|Pan_text=Die mittlere Maustaste drücken und den Mauszeiger bewegen.

Oder die linke und rechte Maustaste halten und den Mauszeiger bewegen.

|Zoom_text=Mit dem Mausrad hinein- und hinauszoomen.
|Rotate_view_text=Die **Shift**- und die mittlere Maustaste drücken und den Mauszeiger bewegen.

Oder die mittlere und die rechte Maustaste drücken und den Mauszeiger bewegen.
}}


<div class="mw-translate-fuzzy">

### OpenCascade


</div>

Dieser Stil wurde in Version 0.18 eingeführt.


{{OpenCascade Navigation
|Select_name=Auswählen
|Pan_name=Schwenken
|Zoom_name=Zoom
|Rotate_view_name=Ansicht drehen
|Ctrl=**Strg**
|Select_text=Mit dem Mauszeiger über einem Objekt die linke Maustaste drücken, um das Objekt auszuwählen.
|Pan_text=Die mittlere Maustaste drücken und den Mauszeiger bewegen.
|Zoom_text=Mit dem Mausrad hinein- und hinauszoomen.

Oder die **Strg**-Taste und die linke Maustaste halten und den Mauszeiger bewegen.
|Rotate_view_text=Die **Strg**- und die rechte Maustaste drücken und den Mauszeiger bewegen.
}}

## Objekte anwählen 

### Simple selection 


<div class="mw-translate-fuzzy">

### Einfache Auswahl 

Objekte können mit einem Linksklick auf das Objekt in der [3D Ansicht](3D_view/de.md) oder durch die Auswahl in der [Baumansicht](tree_view/de.md) gewählt werden.


</div>

### Preselection


<div class="mw-translate-fuzzy">

### Vorauswahl

Es gibt auch einen sogenannten \"Vorauswahl\"mechanismus, der Objekte hervorhebt und Informationen anzeigt bevor sie ausgewählt werden, wenn mit der Maus über das Objekt gefahren wird. Falls dieses Verhalten nicht gewünscht ist oder der Rechner langsam ist, können dies in den Einstellungen abgeschaltet werden.


</div>

## Manipulating objects 


<div class="mw-translate-fuzzy">

## Objekte Manipulieren 

FreeCAD bietet [*manipulators*](Manipulator/de.md), die benutzt werden können, um ein Objekt, oder aber seine Optische Erscheinung zu verändern. Ein einfaches Beispiel ist die Schnittebene- ;engl.


</div>

## Hardware support 


<div class="mw-translate-fuzzy">

FreeCAD unterstützt auch einige [3D Eingabegeräte](3D_input_devices/de.md).


</div>


<div class="mw-translate-fuzzy">

## Mac OS X Probleme 


</div>


<div class="mw-translate-fuzzy">

Vor kurzem erhielten wir Berichte von Mac Anwendern [im Forum](http://forum.freecadweb.org/viewtopic.php?f=3&t=3592&start=0), dass diese Maustaste und Tastenkombination nicht wie erwartet funktionieren. Leider besitzt keiner der Entwickler einen Mac, ebenso wenig wie die anderen regelmäßigen Mitwirkenden. Wir benötigen Eure Hilfe, um festzustellen, welche Maustasten und Tastenkombinationen funktionieren, damit wir dieses Wiki aktualisieren können.


</div>

## Developing a custom navigation 

The tutorial [Adding a new mouse navigation option to FreeCAD](Adding_a_new_mouse_navigation_option_to_FreeCAD.md) orients developers who want to develop a custom mouse navigation option. Familiarity with the C++ syntax is required.

---
[documentation index](../README.md) > Mouse navigation/de
