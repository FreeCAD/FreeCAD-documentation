# Mouse navigation/de
{{TOCright}}

## Überblick

Die FreeCAD **Mausnavigation** besteht aus den verwendeten Befehlen zur visuellen Navigation im 3D Raum und zur Interaktion mit den angezeigten Objekten. FreeCAD unterstützt mehrere Mausnavigationsstile. Der standardmäßige Navigationsstil wird als [CAD Navigation](#CAD_navigation.md) bezeichnet und ist sehr einfach und praktisch, jedoch bietet FreeCAD auch alternative Navigationsstile, die du nach deinen Vorlieben auswählen kannst. Der ausgewählte Navigationsstil wird in allen Arbeitsbereichen verwendet.

Für mehr Information über das Auswählen von Objekten siehe [Auswahlmethoden](Selection_methods/de.md).

Für mehr Informationen zum Bearbeiten von Objekten siehe [Std Transformieren](Std_TransformManip/de.md).

## Navigationsstil auswählen 

1.  Führe eine von folgenden Aktionen aus
    -   Drücke die **<img src=images/NavigationCAD.svg style="width:16px">** Schaltfläche in der [Status bar](Status_bar/de.md).
    -   Rechtsklick auf einen lehren Bereich in der [3D Ansicht](3D_view/de.md), wähle anschließend **Navigation styles** im Kontextmenü.
    -   Benutzen den [Voreinstellungseditor](Preferences_Editor/de#Navigation.md). Wähle dafür im Menü **Edit → Preferences** und dann **Display → Navigation → 3D Navigation**.
2.  Wähle einen Stil von der List.
3.  Ändere optional den **Orbit style**: drücke die **<img src=images/NavigationCAD.svg style="width:16px">** Schaltfläche in der [Status bar](Status_bar/de.md) und Wähle **Settings → Orbit style**. Siehe [Voreinstellungseditor](Preferences_Editor/de#Navigation.md).
4.  Verändere optional den **Rotation mode**. Siehe [Voreinstellungseditor](Preferences_Editor/de#Navigation.md).
5.  Fals der **CAD** Navigationsstil ausgewählt ist: Ändere optional die **Enable animation** Einstellung. Siehe [Voreinstellungseditor](Preferences_Editor/de#Navigation.md).

## Verfügbare Navigationsstile 

### Blender Navigation 

Der Blender Navigationsstil ist der Software [Blender](https://www.blender.org) nachempfunden.


{{Blender Navigation
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

### CAD Navigation 

Dies ist der Standard Navigationsstil. Er ermöglicht dem Benutzer eine einfache Steuerung der Ansicht und erfordert keine Verwendung von Tastaturtasten, außer um Mehrfachauswahlen zu treffen.


{{CAD Navigation
|Select_name=Auswählen
|Pan_name=Schwenken
|Zoom_name=Zoom
|Rotate_view_name=Ansicht drehen<br>Erste Methode
|Rotate_view_alt_name=Ansicht drehen<br>Ersatz Methode
|Ctrl=**Strg**
|Shift=**Shift**
|Select_text=Drücke die linke Maustaste über einem Objekt das du auswählen möchtest.

Niederhalten von **Strg** ermöglicht die Auswahl mehrerer Objekte.
|Pan_text=Halte die mittlere Maustaste gedrückt und bewege den Mauszeiger.
|Pan_mode_text=Pan Modus: Halte die **Strg** Taste gedrückt, drücke einmal die rechte Maustaste und bewege dann den Mauszeiger.
|Zoom_text=Verwende das Mausrad, um ein- und auszuzoomen.

Ein Klick auf die mittlere Maustaste zentriert die Sicht wieder auf die Position der Cursors.
|Zoom_mode_text=Zoom Modus: Halte die **Strg** und **Shift** Tasten gedrückt, drücke einmal die rechte Maustaste und bewege dann den Zeiger.
|Rotate_view_text=Halte die mittlere Maustaste gedrückt, dann drücke und halte die linke Maustaste, dann bewege den Mauszeiger.

<div class="mw-translate-fuzzy">
Die Cursorposition beim Drücken der mittleren Maustaste bestimmt den Drehmittelpunkt. Die Drehung funktioniert wie das Drehen einer Kugel, die sich um ihr Zentrum dreht. Wenn die Tasten losgelassen werden, bevor du die Mausbewegung stoppst, wird die Ansicht [Std DemoModus](spinning/de.md) fortgesetzt, sofern dies aktiviert ist.
</div>

<div class="mw-translate-fuzzy">
Ein Doppelklick mit der mittleren Maustaste setzt einen neuen Drehmittelpunkt.
|Rotate_view_mode_text=Dreh-Modus: Halte die Taste **Shift** gedrückt, drücke einmal die rechte Maustaste und bewege den Mauszeiger. {{Version/de|0.17}}
|Rotate_view_alt_text=Halte die mittlere Maustaste gedrückt, dann drücke und halte die rechte Maustaste und bewege den Mauszeiger.
</div>

Mit dieser Methode kann die mittlere Maustaste losgelassen werden, nachdem die rechte Maustaste gedrückt gehalten wird.

Anwender, die die Maus mit der rechten Hand benutzen, finden diese Methode möglicherweise einfacher als die erste Methode.
}}

### Gestennavigation

Dieser Stil wurde für die Nutzung mit Touchscreen und Stift entworfen. Er kann natürlich auch mit einer Maus benutzt werden und ist auch für die Verwendung eines Mac mit Trackpad empfohlen.


{{Gesture Navigation
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

### Maya-Gestennavigation 

In der Maya-Gestennavigation werden Schwenken, Zoomen und Drehen durch Drücken der **ALT**- und einer Maustaste aktiviert. Daher wird eine 3-Tasten-Maus benötigt. Es ist auch möglich, Gesten zu verwenden, da dieser Modus über den [Gestennavigationsmodus](#Gestennavigation.md) entwickelt wurde.


{{MayaGesture Navigation
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

### OpenCascade


</div>

The OpenCascade navigation style was modeled after [OpenCascade](https://www.opencascade.com/).


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

### OpenInventor Navigation 

Die OpenInventor Navigation (ehemals Inventor) wurde nach dem Vorbild von [Open Inventor](http://en.wikipedia.org/wiki/Open_Inventor) gestaltet. Um Objekte auszuwählen, muss du die **Strg** Taste gedrückt halten.

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

### OpenSCAD navigation 

The OpenSCAD navigation style was modeled after [OpenSCAD](https://openscad.org/).


<small>(v0.20)</small> 


{{OpenSCAD_Navigation
|Select_name=Select
|Pan_name=Pan
|Zoom_name=Zoom
|Rotate_view_name=Rotate view
|Shift=**Shift**
|Select_text=Press the left mouse button over an object you want to select.
|Pan_text=Hold the right mouse button, then move the pointer.
|Zoom_text=Hold the middle mouse button, then move the pointer.
Alternatively, hold **Shift** and the right mouse button, then move the pointer.
|Rotate_view_text=Hold the left mouse button, then move the pointer.
}}

### Revit Navigation 

Der Revit Navigationsstil basiert auf [Revit](https://de.wikipedia.org/wiki/Revit).


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

### TinkerCAD Navigation 

Der TinkerCAD Navigationsstil basiert auf [TinkerCAD](https://en.wikipedia.org/wiki/Tinkercad).


<small>(v0.20)</small> 


{{TinkerCAD Navigation
|Select_name=Select
|Pan_name=Pan
|Zoom_name=Zoom
|Rotate_view_name=Rotate view
|Select_text=Press the left mouse button over an object you want to select.
|Pan_text=Hold the middle mouse button, then move the pointer.
|Zoom_text=Use the mouse wheel to zoom in and out.
|Rotate_view_text=Press the right mouse button, then move the pointer.
}}

### Touchpad Navigation 

In Touchpad Navigation, panning, zooming, and rotating the view require a modifier key together with the touchpad.


<div class="mw-translate-fuzzy">

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


</div>

## Hardware support 

FreeCAD unterstützt auch einige [3D Eingabegeräte](3D_input_devices/de.md).


<div class="mw-translate-fuzzy">

## Mac OS X Probleme 


</div>


<div class="mw-translate-fuzzy">

Vor kurzem erhielten wir Berichte von Mac Anwendern [im Forum](http://forum.freecadweb.org/viewtopic.php?f=3&t=3592&start=0), dass diese Maustaste und Tastenkombination nicht wie erwartet funktionieren. Leider besitzt keiner der Entwickler einen Mac, ebenso wenig wie die anderen regelmäßigen Mitwirkenden. Wir benötigen Eure Hilfe, um festzustellen, welche Maustasten und Tastenkombinationen funktionieren, damit wir dieses Wiki aktualisieren können.


</div>

## Einen eigenen Navigationsstil entwickeln 

The tutorial [Adding a new mouse navigation option to FreeCAD](Adding_a_new_mouse_navigation_option_to_FreeCAD.md) orients developers who want to develop a custom mouse navigation option. Familiarity with the C++ syntax is required.

---
[documentation index](../README.md) > Mouse navigation/de
