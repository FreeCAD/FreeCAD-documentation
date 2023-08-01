# Mouse navigation/de
{{TOCright}}



## Überblick

Die FreeCAD **Mausnavigation** besteht aus den verwendeten Befehlen zur visuellen Navigation im 3D Raum und zur Interaktion mit den angezeigten Objekten. FreeCAD unterstützt mehrere Mausnavigationsstile. Der standardmäßige Navigationsstil wird als [CAD Navigation](#CAD_navigation.md) bezeichnet und ist sehr einfach und praktisch, jedoch bietet FreeCAD auch alternative Navigationsstile, die du nach deinen Vorlieben auswählen kannst. Der ausgewählte Navigationsstil wird in allen Arbeitsbereichen verwendet.

Für mehr Information über das Auswählen von Objekten siehe [Auswahlmethoden](Selection_methods/de.md).

Für mehr Informationen zum Bearbeiten von Objekten siehe [Std Transformieren](Std_TransformManip/de.md).



## Navigationsstil auswählen 

1.  Führe eine von folgenden Aktionen aus:
    -   Drücke die **[<img src=images/NavigationCAD_dark.svg style="width:16px">**-Schaltfläche in der [Statusleiste](Status_bar/de.md).
    -   Rechtsklick auf einen leeren Bereich in der [3D Ansicht](3D_view/de.md) und wähle anschließend **Navigationsstile** im Kontextmenü.
    -   Wähle aus dem Menü den [Voreinstellungseditor](Preferences_Editor/de#Navigation.md) und dort **Bearbeiten → Einstellungen** und dann aus **Anzeige → Navigation → 3D Navigation** einen Stil aus der Liste.
2.  Ändere gegebenenfalls den **Orbit Stil**: drücke die **[<img src=images/NavigationCAD_dark.svg style="width:16px">**-Schaltfläche in der [Statusleiste](Status_bar/de.md) und wähle **Einstellungen → Orbit Stil**. Siehe [Voreinstellungseditor](Preferences_Editor/de#Navigation.md).
3.  Verändere gegebenenfalls die **Art der Drehung**. Siehe [Voreinstellungseditor](Preferences_Editor/de#Navigation.md).
4.  Falls der **CAD** Navigationsstil ausgewählt ist: ändere gegebenenfalls die **Animation zulassen**-Einstellung. Siehe [Voreinstellungseditor](Preferences_Editor/de#Navigation.md).



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

**Strg** gedrückt halten, um die Auswahl mehrerer Objekte zu ermöglichen.
|Pan_text=Halte die mittlere Maustaste gedrückt und bewege den Mauszeiger.
|Pan_mode_text=Pan Modus: **Strg** gedrückt halten und einmal die rechte Maustaste drücken und dann den Mauszeiger bewegen.
|Zoom_text=Verwende das Mausrad, um herein- und hinausaus zu zoomen.

Ein Klick auf die mittlere Maustaste zentriert die Sicht wieder auf die Position der Cursors.
|Zoom_mode_text=Zoom Modus: Halte die **Strg** und **Shift** Tasten gedrückt, drücke einmal die rechte Maustaste und bewege dann den Zeiger.
|Rotate_view_text=Halte die mittlere Maustaste gedrückt, dann drücke und halte die linke Maustaste, dann bewege den Mauszeiger.

Werden die Tasten losgelassen, bevor die Mausbewegung gestoppt ist, wird die Drehung der Ansicht fortgesetzt, sofern dies aktiviert ist.

Ein Doppelklick mit der mittleren Maustaste setzt einen neuen Drehmittelpunkt.
|Rotate_view_mode_text=Dreh-Modus: **Shift** gedrückt halten, einmal die rechte Maustaste drücken und den Mauszeiger bewegen.
|Rotate_view_alt_text=Die mittlere Maustaste gedrückt halten, die rechte Maustaste drücken und halten und dann bewege den Mauszeiger.

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

In der Maya-Gestennavigation werden Schwenken, Zoomen und Drehen der Ansicht durch Drücken der **ALT**- zusammen mit einer Maustaste aktiviert. Daher wird eine 3-Tasten-Maus benötigt. Es ist auch möglich, Gesten zu verwenden, da dieser Modus über den [Gestennavigationsmodus](#Gestennavigation.md) entwickelt wurde.


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



### OpenCascade - Navigation 

Der OpenCascade - Navigationsstil wurde gemäß [OpenCascade](https://www.opencascade.com/) gestaltet.


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

Die OpenInventor - Navigation (ehemals Inventor) wurde gemäß [Open Inventor](http://en.wikipedia.org/wiki/Open_Inventor) gestaltet. Um Objekte auszuwählen, muss **Hochstellen (Shift)** oder **strg** gedrückt gehalten werden.

Dieser Modus basiert nicht auf Autodesk Inventor.


{{OpenInventor Navigation
|Select_name=Auswählen
|Pan_name=Schwenken
|Zoom_name=Zoom
|Rotate_view_name=Ansicht drehen
|Hochsetzen (Shift)=**Shift**
|Select_text=**Shift** gedrückt halten und dann die linke Maustaste drücken und über das Objekt fahren, das ausgewählt werden soll.

Statt dessen **Strg** gedrückt halten, um mehrere Objekte zu markieren.
|Pan_text=Die mittlere Maustaste gedrückt halten und den Mauszeiger bewegen.
|Zoom_text=Mit der mittleren Maustaste hinein- und herauszoomen.

Alternativ halte die mittlere Maustaste, dann drücke und halte die linke Maustaste, dann bewege den Mauszeiger. 
|Rotate_view_text=Halte die linke Maustaste, dann bewege den Mauszeiger.
}}



### OpenSCAD Navigation 

Die OpenSCAD Navigation wurde gemäß [OpenSCAD](https://openscad.org/) gestaltet.


<small>(v0.20)</small> 


{{OpenSCAD_Navigation
|Select_name=Auswählen
|Pan_name=Schwenken
|Zoom_name=Zoom
|Rotate_view_name=Ansicht drehen
|Shift=**Shift**
|Select_text=Die linke Maustaste drücken und über das Objekt fahren, das markiert werden soll.
|Pan_text=Die rechte Maustaste drücken und den Mauszeiger bewegen.
|Zoom_text=Die mittlere Maustaste drücken und den Mauszeiger bewegen.
Alternativ **Hochstellen (Shift)** und die rechte Maustaste halten und den Mauszeiger bewegen.
|Rotate_view_text=Die linke Maustaste drücken und den Mauszeiger bewegen.
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
|Select_name=Auswählen
|Pan_name=Schwenken
|Zoom_name=Zoom
|Rotate_view_name=Ansicht drehen
|Select_text=Die linke Maustaste drücken und über das Objekt fahren, das ausgewählt werden soll.
|Pan_text=Die mittlere Maustaste halten und den Mauszeiger bewegen.
|Zoom_text=Mit dem Mausrad hinein- und herauszoomen.
|Rotate_view_text=Die rechte Maustaste drücken und den Mauszeiger bewegen.
}}



### Touchpad Navigation 

Bei der Navigation mit einer Tastfläche (touchpad) erfordert das Schwenken, Zoomen und Drehen der Ansicht das Drücken einer zusätzlichen Erweiterungstaste.


{{Touchpad Navigation
|Select_name=Auswählen
|Pan_name=Schwenken
|Zoom_name=Zoom
|Rotate_view_name=Ansicht drehen
|Ctrl=**Strg**
|Shift=**Shift**
|Alt=**Alt**
|PageUp=**PageUp**
|PageDown=**PageDown**
|Select_text=Die linke Maustaste drücken und über ein Objekt fahren, das ausgewählt werden soll.
|Pan_text=Halte **Shift**, und dann den Mauszeiger bewegen.
|Zoom_text=Verwende **PageUp** und **PageDown**, um hinein- und heraus zu zoomen.
|Zoom_alt_text=Alternativ kann **Strg** und **Shift** gedrückt gehalten und dann der Mauszeiger bewegt werden.
|Rotate_view_text=**Alt** gedrückt halten und dann dann den Mauszeiger bewegen.
|Rotate_view_alt_text=Alternativ kann **Shift** und die linke Taste gedrückt gehalten und dann der Mauszeiger bewegt werden.
}}

## Hardware support 

FreeCAD unterstützt auch einige [3D Eingabegeräte](3D_input_devices/de.md).



## Empfohlene Navigation unter macOS 

Auf MacBooks mit einer Tastfläche (trackpad) funktioniert die Gesture Navigation sehr gut, jedoch haben die Gesten eine besondere Bedeutung:

-   Zoom: mit zwei Fingern ziehen.
-   Drehen: mit drei Fingern ziehen.
-   Schwenken: **strg** drücken und drei Finger verwenden.



## Einen eigenen Navigationsstil entwickeln 

Die Beschreibung [Adding a new mouse navigation option to FreeCAD](Adding_a_new_mouse_navigation_option_to_FreeCAD.md) zeigt Entwicklern, die eine Möglichkeit zur Erstellung benutzereigener Mausnavigationen entwickeln wollen, einen Weg dazu. Kenntnisse zur C++ - Entwicklung sind hierzu erforderlich.



---
![](images/Button_right.svg) [documentation index](../README.md) > Mouse navigation/de
