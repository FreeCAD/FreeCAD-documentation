# Mouse navigation/de
## Überblick

Die FreeCAD **Mausnavigation** besteht aus den Befehlen zum visuellen Navigieren im 3D-Raum und zur Interaktion mit den angezeigten Objekten. FreeCAD unterstützt mehrere Mausnavigationsstile. Der standardmäßige Navigationsstil wird als [CAD-Navigation](#CAD_navigation.md) bezeichnet und ist sehr einfach und praktisch, jedoch bietet FreeCAD auch alternative Navigationsstile, die nach eigenen Vorlieben ausgewählt werden können. Der ausgewählte Navigationsstil wird in allen Arbeitsbereichen verwendet.

Für mehr Information über das Auswählen von Objekten siehe [Auswahlmethoden](Selection_methods/de.md).

Für mehr Informationen zum Bearbeiten von Objekten siehe [Std Bewegen](Std_TransformManip/de.md).



## Navigationsstil auswählen 

1.  Eine der folgenden Möglichkeiten ausführen:
    -   Die Schaltfläche **[<img src=images/NavigationCAD_dark.svg style="width:16px">** in der [Statusleiste](Status_bar/de.md) drücken.
    -   Ein Rechtsklick auf einen leeren Bereich in der [3D-Ansicht](3D_view/de.md) und **Navigationsstile** im Kontextmenü auswählen.
    -   Den [Voreinstellungseditor](Preferences_Editor/de#Navigation.md) über den Menüeintrag **Bearbeiten → Einstellungen** öffnen und dort **Anzeige → Navigation → 3D-Navigation**
2.  Einen Stil in der Liste auswählen.
3.  Wahlweise den **Orbit-Stil** ändern: Die Schaltfläche **[<img src=images/NavigationCAD_dark.svg style="width:16px">** in der [Statusleiste](Status_bar/de.md) drücken und **Einstellungen → Orbit Stil** auswählen. Siehe [Voreinstellungseditor](Preferences_Editor/de#Navigation.md).
4.  Wahlweise die **Art der Drehung** ändern. Siehe [Voreinstellungseditor](Preferences_Editor/de#Navigation.md).
5.  Wenn der Navigationsstil **CAD** ausgewählt ist: Wahlweise die Einstellung **Animationen** aktivieren. Siehe [Voreinstellungseditor](Preferences_Editor/de#Navigation.md).



## Verfügbare Navigationsstile 

Für alle Navigationsstile gilt: Solange keine Objekte im Sketcher-Bearbeitungsmodus ausgewählt werden, muss immer die **Strg**-Taste (Ctrl-Taste) gedrückt und gehalten werden, um mehrere Objekte auszuwählen.

Die folgenden Tastatur-Optionen stehen allen Stilen zur Verfügung:

-    **Ctrl**\+ {{ASCII|43}} and **Ctrl** + {{ASCII|22}} or **PgUp** and **PgDn** to zoom in and out, respectively.

-   The arrow keys, {{ASCII|17}}{{ASCII|16}}{{ASCII|30}}{{ASCII|31}}, to pan the view left/right and up/down.

-    **Shift**\+ {{ASCII|17}} and **Shift** + {{ASCII|16}} to rotate the view by 90 degrees.



### Blender Navigation 

Der Navigationsstil Blender ist der Software [Blender](https://www.blender.org) nachempfunden.


{{Blender Navigation
|Select_name=Auswählen
|Zoom_name=Zoomen
|Rotate_view_name=Ansicht drehen
|Pan_name=Schwenken

|Shift=**Shift**

|Select_text=Die linke Maustaste über einem Objekt drücken, das ausgewählt werden soll.

|Zoom_text=Das Mausrad zum Anpassen der Darstellungsgröße (Zoom) verwenden.

|Rotate_view_text=Die mittlere Maustaste gedrückt halten und den Mauszeiger bewegen.

|Pan_text=**Shift** und die mittlere Maustaste gedrückt halten und den Mauszeiger bewegen.

Alternativ die linke und rechte Maustaste gedrückt halten und den Mauszeiger bewegen.
}}



### CAD Navigation 

Dies ist der Standard-Navigationsstil. Er ermöglicht dem Benutzer eine einfache Steuerung der Ansicht und erfordert keine Verwendung von Tastaturtasten, außer um Mehrfachauswahlen zu treffen.


{{CAD Navigation
|Select_name=Auswählen
|Zoom_name=Zoomen
|Rotate_view_name=Ansicht drehen<br>Erste Methode
|Rotate_view_alt_name=Ansicht drehen<br>Alternative Methode
|Pan_name=Schwenken

|Ctrl=**Strg**
|Shift=**Shift**

|Select_text=Die linke Maustaste über einem Objekt drücken, das ausgewählt werden soll.

|Zoom_text=Das Mausrad zum Anpassen der Darstellungsgröße (Zoom) verwenden.

Clicking the middle mouse button re-centers the view on the location of the cursor.

|Rotate_view_text=Die mittlere Maustaste gedrückt halten, dann die linke Maustaste drücken und halten, dann den Mauszeiger bewegen.

Werden die Tasten losgelassen, bevor die Mausbewegung gestoppt ist, wird die Drehung der Ansicht fortgesetzt, sofern dies aktiviert ist.

Ein Doppelklick mit der mittleren Maustaste setzt einen neuen Drehmittelpunkt.

|Rotate_view_alt_text=Die mittlere Maustaste gedrückt halten, dann die rechte Maustaste drücken und halten, dann den Mauszeiger bewegen.

Mit dieser Methode kann die mittlere Maustaste losgelassen werden, wenn die rechte Maustaste gedrückt gehalten wird.

Anwender, die die Maus mit der rechten Hand benutzen, finden diese Methode möglicherweise einfacher als die erste Methode.

|Pan_text=Die mittlere Maustaste gedrückt halten und den Mauszeiger bewegen.

|Zoom_mode_text=Zoom mode: hold the **Ctrl** and **Shift** keys, press the right mouse button once, then move the pointer.

|Rotate_view_mode_text=Rotate mode: hold the **Shift** key, press the right mouse button once, then move the pointer.

|Pan_mode_text=Pan mode: hold the **Ctrl** key, press the right mouse button once, then move the pointer.
}}



### Gestennavigation

Dieser Stil wurde für die Nutzung mit Touchscreen und Stift entworfen. Er kann natürlich auch mit einer Maus benutzt werden und wird auch empfohlen, wenn ein Mac mit Trackpad eingesetzt wird.


{{Gesture Navigation
|Select_name=Auswählen
|Zoom_name=Zoomen
|Rotate_view_name=Ansicht drehen
|Pan_name=Schwenken
|Tilt_view_name=Ansicht kippen

|Select_text=Die linke Maustaste über einem Objekt drücken, das ausgewählt werden soll.

|Zoom_text=Das Mausrad zum Anpassen der Darstellungsgröße (Zoom) verwenden.

|Rotate_view_text=Hold the left mouse button, then move the pointer.
In [Sketcher](Sketcher_Workbench.md) and other edit modes, this behavior is disabled. Hold **Alt** when pressing the mouse button to enter rotation mode.

Um den Fokuspunkt der Kamera für die Drehung festzulegen, mit der mittleren Maustaste einen Punkt anklicken. Alternativ kann der Mauszeiger auf einen Punkt gerichtet und **H** auf der Tastatur gedrückt werden.

|Pan_text=Die rechte Maustaste gedrückt halten und den Mauszeiger bewegen.

|Tilt_view_text=Die linke und die rechte Maustaste gedrückt halten, dann den Mauszeiger seitwärts bewegen.

|Select_gesture_text=Tap to select.

|Zoom_gesture_text=Drag two fingers (pinch) closer or farther apart.

|Rotate_view_gesture_text=Mit einem Finger ziehen, um zu rotieren.

Im [Sketcher](Sketcher_Workbench/de.md) die **Alt**-Taste gedrückt halten.

|Pan_gesture_text=Drag with two fingers.

Oder tippen, halten und dann ziehen. Dies simuliert das Schwenken mit der rechten Maustaste.

|Tilt_view_gesture_text=Die imaginäre Linie rotieren, die durch zwei Berührungspunkte gebildet wird.

Diese Methode ist standardmäßig deaktiviert. Zum Aktivieren zu den Voreinstellungen unter **Bearbeiten → Einstellungen → Anzeige → Navigation** wechseln und "Touchscreen-Neige-Geste deaktivieren" deaktivieren.
}}



### Maya-Gestennavigation 

In der Maya-Gestennavigation werden Schwenken, Zoomen und Drehen der Ansicht durch Drücken der **ALT**-Taste zusammen mit einer Maustaste aktiviert. Daher wird eine 3-Tasten-Maus benötigt. Es ist auch möglich, Gesten zu verwenden, da dieser Stil über den Stil [Gestennavigation](#Gestennavigation.md) entwickelt wurde.


{{MayaGesture Navigation
|Select_name=Auswählen
|Zoom_name=Zoomen
|Rotate_view_name=Ansicht drehen
|Pan_name=Schwenken
|Tilt_view_name=Ansicht kippen

|Alt=**Alt**

|Select_text=Die linke Maustaste über einem Objekt drücken, das ausgewählt werden soll.

|Zoom_text=Das Mausrad zum Anpassen der Darstellungsgröße (Zoom) verwenden.

Alternativ **Alt** und die rechte Maustaste gedrückt halten und dann den Mauszeiger bewegen.

|Rotate_view_text=**Alt** und die mittlere Maustaste gedrückt halten und dann den Mauszeiger bewegen.

|Pan_text=**Alt** und die mittlere Maustaste gedrückt halten und dann den Mauszeiger bewegen.

|Tilt_view_text=**Alt**, die linke und die rechte Maustaste gedrückt halten und dann den Mauszeiger seitwärts bewegen.
}}



### OpenCascade - Navigation 

Der Navigationsstil OpenCascade wurde gemäß [OpenCascade](https://www.opencascade.com/) gestaltet.


{{OpenCascade Navigation
|Select_name=Auswählen
|Zoom_name=Zoomen
|Rotate_view_name=Ansicht drehen
|Pan_name=Schwenken

|Ctrl=**Strg**

|Select_text=Die linke Maustaste über einem Objekt drücken, das ausgewählt werden soll.

|Zoom_text=Das Mausrad zum Anpassen der Darstellungsgröße (Zoom) verwenden.

Alternativ **Shift** und die linke Maustaste gedrückt gehalten und dann den Mauszeiger bewegen.

|Rotate_view_text=Die mittlere Maustaste gedrückt halten, dann die rechte Maustaste drücken und halten, dann den Mauszeiger bewegen.

Alternativ **Shift** und die rechte Maustaste gedrückt gehalten und dann den Mauszeiger bewegen.

|Pan_text=Die mittlere Maustaste drücken und den Mauszeiger bewegen. Es kann auch **Strg** gedrückt gehalten werden.
}}



### OpenInventor Navigation 

Die OpenInventor - Navigation (ehemals Inventor) wurde gemäß [Open Inventor](http://en.wikipedia.org/wiki/Open_Inventor) gestaltet. Um Objekte auszuwählen, muss **(Shift)** (Umschalttaste) oder **Strg** gedrückt gehalten werden.

Dieser Stil basiert nicht auf Autodesk Inventor.


{{OpenInventor Navigation
|Select_name=Auswählen
|Zoom_name=Zoomen
|Rotate_view_name=Ansicht drehen
|Pan_name=Schwenken

|Shift=**Shift**

|Select_text=**Shift** gedrückt halten, dann die linke Maustaste über dem Objekt drücken, das ausgewählt werden soll.

Stattdessen **Strg** gedrückt halten, um mehrere Objekte zu markieren.

|Zoom_text=Das Mausrad zum Anpassen der Darstellungsgröße (Zoom) verwenden.

Alternativ die mittlere Maustaste gedrückt halten, dann die linke Maustaste drücken und halten, dann den Mauszeiger bewegen.

|Rotate_view_text=Die linke Maustaste gedrückt halten und den Mauszeiger bewegen.

|Pan_text=Die mittlere Maustaste gedrückt halten und den Mauszeiger bewegen.
}}



### OpenSCAD Navigation 

Die OpenSCAD Navigation wurde gemäß [OpenSCAD](https://openscad.org/) gestaltet.


{{OpenSCAD_Navigation
|Select_name=Auswählen
|Zoom_name=Zoomen
|Rotate_view_name=Ansicht drehen
|Pan_name=Schwenken

|Shift=**Shift**

|Select_text=Die linke Maustaste über einem Objekt drücken, das ausgewählt werden soll.

{{VersionMinus/de|0.21}} **Strg**-Taste (Ctrl) und **Umschalttaste** (Shift) gedrückt halten, wenn die Maustaste gedrückt wird, um ein Objekt im Sketcher-Bearbeitungsmodus zu ziehen.

|Zoom_text=Das Mausrad zum Anpassen der Darstellungsgröße (Zoom) verwenden.

Alternativ die mittlere Maustaste gedrückt halten und den Mauszeiger bewegen.

Alternativ **Umschalttaste** (Shift) und die rechte Maustaste gedrückt halten und den Mauszeiger bewegen.

|Rotate_view_text=Die linke Maustaste gedrückt halten und den Mauszeiger bewegen.

Alternativ und wenn sich eine Skizze im Bearbeitungsmodus befindet: Die mittlere Maustaste gedrückt halten, dann die rechte Maustaste drücken und halten, dann den Mauszeiger bewegen.

|Pan_text=Die rechte Maustaste gedrückt halten und den Mauszeiger bewegen.
}}



### Revit Navigation 

Der Revit Navigationsstil basiert auf [Revit](https://de.wikipedia.org/wiki/Revit).


{{Revit Navigation
|Select_name=Auswählen
|Zoom_name=Zoomen
|Rotate_view_name=Ansicht drehen
|Pan_name=Schwenken

|Shift=**Shift**

|Select_text=Die linke Maustaste über einem Objekt drücken, das ausgewählt werden soll.

|Zoom_text=Das Mausrad zum Anpassen der Darstellungsgröße (Zoom) verwenden.

|Rotate_view_text=**Shift** und die mittlere Maustaste gedrückt halten und den Mauszeiger bewegen.

Alternativ die mittlere Maustaste gedrückt halten, dann die rechte Maustaste drücken und halten, dann den Mauszeiger bewegen.

|Pan_text=Die mittlere Maustaste gedrückt halten und den Mauszeiger bewegen.

Alternativ die linke und rechte Maustaste gedrückt halten und den Mauszeiger bewegen.
}}



### TinkerCAD Navigation 

Der TinkerCAD-Navigationsstil basiert auf [TinkerCAD](https://en.wikipedia.org/wiki/Tinkercad).


{{TinkerCAD Navigation
|Select_name=Auswählen
|Zoom_name=Zoomen
|Rotate_view_name=Ansicht drehen
|Pan_name=Schwenken

|Select_text=Die linke Maustaste über einem Objekt drücken, das ausgewählt werden soll.

|Zoom_text=Das Mausrad zum Anpassen der Darstellungsgröße (Zoom) verwenden.

|Rotate_view_text=Die rechte Maustaste drücken und den Mauszeiger bewegen.

|Pan_text=Die mittlere Maustaste gedrückt halten und den Mauszeiger bewegen.
}}



### Touchpad Navigation 

Für den Navigationsstil Tastfläche (touchpad) erfordern das Schwenken, Zoomen und Drehen der Ansicht das Drücken einer Erweiterungstaste mit dem Touchpad. Dieser Stil kann auch mit einer Maus verwendet werden


{{Touchpad Navigation
|Select_name=Auswählen
|Zoom_name=Zoomen
|Rotate_view_name=Ansicht drehen
|Pan_name=Schwenken

|Ctrl=**Strg**
|Shift=**Shift**
|Alt=**Alt**

|Select_text=Die linke Maustaste über einem Objekt drücken, das ausgewählt werden soll.

|Zoom_text=**Strg** und **Shift** gedrückt gehalten und dann den Mauszeiger bewegen.

|Rotate_view_text=**Alt** gedrückt halten und dann dann den Mauszeiger bewegen.

Alternativ **Shift** und die linke Maustaste gedrückt gehalten und dann den Mauszeiger bewegen.

|Pan_text=**Shift** gedrückt halten und den Mauszeiger bewegen.
}}

## Hardware support 

FreeCAD unterstützt auch einige [3D-Eingabegeräte](3D_input_devices/de.md).



## Empfohlene Navigation unter macOS 

Auf MacBooks mit einer Tastfläche (trackpad) funktioniert die Gesture-Navigation sehr gut, jedoch haben die Gesten eine besondere Bedeutung:

-   Zoom: mit zwei Fingern ziehen.
-   Drehen: mit drei Fingern ziehen.
-   Schwenken: **Strg** drücken und drei Finger verwenden.



---
⏵ [documentation index](../README.md) > Mouse navigation/de
