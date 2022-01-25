# HiDPI support/it
**
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
**


{{TOCright}}

![Device pixel ratio. 100% = 1, 200% = 2, 150% = 1.5](images/HiDpiDevicePixelRatio.png )

This is a [project](Development_roadmap.md) dedicated to support high-resolution displays in FreeCAD.


<div class="mw-translate-fuzzy">

Il supporto per HiDPI si riferisce al problema della visualizzazione di grafica raster (caratteri, cursori, immagini) ed elementi dell\'interfaccia utente (pulsanti, menu, maniglie) su schermi ad alta risoluzione.


</div>


<div class="mw-translate-fuzzy">

Il problema è dovuto al fatto che la dimensione fisica di un display rimane la stessa mentre la sua risoluzione aumenta.


</div>

To solve the issue, Apple introduced \"HiDPI\", that is scaling all the UI elements according to the font size. Font sizes are specified in points, while their pixel value is calculated using DPI and device pixel ratio which is a scale factor specified by a user in OS settings. At the same time, raster images are rendered at their true pixel size, so individual pixels are less noticeable. It means that raster images are provided at higher resolution to make up for their size on a screen. Vector graphics (UI elements) are rendered accordingly, at higher resolution.

## Piano principale 

### Prima parte 

Obiettivo: assicurarsi di ottenere il massimo dal supporto Qt.


<div class="mw-translate-fuzzy">

-   In corso. Migrare la base utenti su Qt\> 5.6 e impostare AA\_EnableHighDpiScaling su true.
-   Ridimensionare tutti i cursori e le icone (moltiplicandoli per devicePixelRatio) <https://github.com/FreeCAD/FreeCAD/pull/3712>


</div>

### Part two 

Goal: Make sure that the system font is correctly determined.

-   Bundle appropriate QPA theme plugins on all major platforms (AppImage, etc)
-   Find ways to detect that system\'s font is changed
-   Remove the toolbar/icon size setting and make the toolbar size relative to the system font
-   Add an experimental setting \"scale factor\" which will depend on device pixel ratio and/or system font size
-   Rescale the toolbar/icon size according to the new experimental setting
-   Gather user feedback whether we need the customizable toolbar icon size

### Part three 

Goal: Make all UI widgets size relative to the font size

-   In all appropriate places, get system font metrics to determine the size of a widget.
-   In places where real size is referenced, assume font size as a relative measure (72 points = 96 virtual pixels = 1 inch).
-   Choose a reference device relative to which UI could scale up and down.
-   2D coordinates and sizes should assume device-independent pixels.
-   Make sure qreal versions of APIs are used.
-   Turn off AA\_EnableHighDpiScaling

### Part four 

Goal: Support rescaling when the window is moved from one screen to another

-   Detect that device pixel ratio has changed
-   Notify all widgets depending on device pixel ratio or the font size

## Background

### Display resolutions 

<img alt="" src=images/Vector_Video_Standards8.svg  style="width:800px;">

### Device pixel ratio 

It\'s a well-known concept for Web and Android developers. But not so much for desktop developers.

Basically, it\'s the ratio between physical pixels and device-independent pixels.

First things first. UI positioning and size (x, y, width, height) are historically defined in pixels.

But as more variety of displays resolutions become available at many different physical sizes, it\'s become a problem software developers need to be aware of.

FreeCAD development was started in 2002, long before such a problem was even foreseen.

Ok, why not just increase DPI, you ask. Well, the issue is that you still want to benefit from the high-resolution display.

All the raster graphics need to contain more pixels, while vector graphics (fonts and icons) should be of the same physical size as visible on the display.

If you just change DPI, you would scale everything up and down. But in fact, you need all the pixel sizes to remain the same, while resources (images) to be displayed in a higher resolution.

So the concept of \"Device-independent pixels\" was introduced. The idea was that developers could keep not worrying about the physical size of a display and design UIs in virtual pixels.

But the reality is that if you use raster graphics, it becomes pixelized, blurry, or aliased as it is displayed in non-native resolution. So developers now need to provide multiple versions of raster images, for each device pixel ratio. Usually, it\'s whole numbers: 1, 2, 3, 4. But it can also be fractional (125%, 150%, 175% = 1.25, 1.5, 1.75) meaning that there\'s still some scaling involved, but not as apparent.

-   <https://stackoverflow.com/questions/8785643/what-exactly-is-device-pixel-ratio>
-   <https://stackoverflow.com/questions/13911786/what-is-device-pixel-ratio-for>

## Issue testing/demonstration 

### OS X 

1.  Open \"Display\"
2.  Choose \"Scaled\"
3.  Choose \"Larger text\" - this increases device pixel ratio

Video: <https://www.youtube.com/watch?v=4U3eh_fMo4o>

### X Window 

Useful commands:

    ~$ xrdb -query
    *customization: -color
    Xft.dpi:    192
    Xft.antialias:  1
    Xft.hinting:    1
    Xft.hintstyle:  hintslight
    Xft.rgba:   rgb
    Xcursor.size:   128
    Xcursor.theme:  DMZ-White

    ~$ xdpyinfo | grep -B 2 resolution
    screen #0:
      dimensions:    3840x2160 pixels (1016x572 millimeters)
      resolution:    96x96 dots per inch

### Ubuntu (GNOME Shell) 

1.  Open \"Displays\" (Settings \> Devices \> Displays)
2.  Select the highest resolution available
3.  Select scaling higher than 100%

## Issues and solutions 

-   Raster images (cursors, icons)
-   Fonts (defined in pixels rather than points)
-   Cursor hot point
-   Zoom/Rotate origin
-   Snap distance
-   Selection distance (the hot area around selectable objects)

### Font size 

Fonts are usually vector. So they don\'t require a higher resolution version to be able to scale up (in pixels). However, we can\'t just increase every font size and call it a day. People are used to font sizes in relation to how they look on paper. And on paper, it is known that 72pt font takes one inch, and on displays of old days, an inch was equal to 96 pixels at 1:1 zoom level.

So, as display resolutions become higher, displays could fit more text lines of the same size. So naturally, as display physical size remains the same and our eyes don\'t become better at discerning smaller detail, we perceive the same font point size as smaller on higher resolutions.

To overcome this issue, OS implemented what it\'s called DPI scaling (or DPI font settings in the older days) or High-DPI scaling of the recent 4K displays. Users could change the DPI and benefit from much more real estate in terms of pixels while keeping a comfortable to read font size.

### Custom cursor size 

The cursor size is kind of difficult. Qt recommends using a hardcoded image size of 32x32. As of 5.x it doesn\'t provide any functionality to integrate with OS and query the size of the mouse pointer. It\'s a shame since it means you can\'t benefit from accessibility settings, where cursor size can be set to an arbitrarily large value.

So, until Qt provides better guidance on the cursor size, let\'s use an image of 32 \* device pixel ratio.

In OS, for example in GNOME, cursor size appears to be fixed in terms of virtual pixels. That is, it respects the device pixel ratio (keep the same apparent size). But it does increase when you change the display resolution (that is, stays the same in pixels, but increase in apparent size).

For example, here\'s a default setting for virtual pixels in GNOME:

    ~$ gsettings get org.gnome.desktop.interface cursor-size
    64

Taking into account the scale factor, it means the physical pixel size of 128.

Qt doesn\'t provide the functionality to retrieve that value. So we have to either hard code it or provide a user setting to change that.

## Forum threads 

-   [Improve support of high DPI displays](https://forum.freecadweb.org/viewtopic.php?t=34916) - general Qt support
-   [News: Qt 5.14 Is Bringing Significantly Better HiDPI Support](https://forum.freecadweb.org/viewtopic.php?t=39325) - general Qt support
-   [Custom cursors and high dpi (Windows and MacOS testers needed)](https://forum.freecadweb.org/viewtopic.php?&t=48719) - raster cursor image issue
-   [HiDPI Support in Sketcher View](https://forum.freecadweb.org/viewtopic.php?t=34853) - selection distance issue
-   [High DPI Improvements](https://forum.freecadweb.org/viewtopic.php?t=10512) - PR \"High DPI Fixes\" <https://github.com/FreeCAD/FreeCAD/pull/54>, bad quality, 2015
-   [High dpi](https://forum.freecadweb.org/viewtopic.php?t=12123) - experimental build with \"High DPI Improvements\" PR
-   [GUI font size](https://forum.freecadweb.org/viewtopic.php?t=41656) - font size issue and the QT\_SCALE\_FACTOR workaround
-   [BUG? Cropped icons](https://forum.freecadweb.org/viewtopic.php?t=28838) - issues with HiDPI on multiple displays
-   [FreeCAD 0.17 on macOS Update (Qt 5 builds now available)](https://forum.freecadweb.org/viewtopic.php?t=20977) - issues with HiDPI on OS X after upgrade to Qt5
-   [Ticket \#3537 - Draft Edit mode not working on MacOS X (HiDPi issue)](https://forum.freecadweb.org/viewtopic.php?f=3&t=29743) - OS X + HiDPI, Qt5
-   [Menu distorted on MAC external display](https://forum.freecadweb.org/viewtopic.php?t=39975) - OS X + HiDPI, external display
-   [macOS Qt5 plan and status](https://forum.freecadweb.org/viewtopic.php?t=19724&start=60) - OS X dropped support for Qt4, HiDPI issues
-   <https://www.google.com/search?q=freecad+hidpi+site:forum.freecadweb.org>
-   [A suggestion to disable \"dump\" scaling before tackling the font size issues](https://forum.freecadweb.org/viewtopic.php?f=10&t=52307)
-   [Navigation cube scaling](https://forum.freecadweb.org/viewtopic.php?f=3&t=42835)
-   [Navigation cube scaling 2](https://forum.freecadweb.org/viewtopic.php?p=450061#p450061)

## Relevant changes 

-    {{commit|a14b99e77}}
    

-    {{commit|2f2d50535}}
    

-    {{commit|bb6e4e6ad}}
    

-    {{commit|23ecb8eac}}
    

-    {{commit|ca7770b80}}
    

-    {{commit|51fcdd2c0}}
    

-    {{commit|805ccd8deb}}
    

-    {{commit|347156403}}
    

-    {{commit|094dda5900d}}
    

-    {{commit|925cffc1535}}
    

-    {{commit|7dfeb801a}}
    

## Bugtracker Issues 

-   Tickets tagged with [HiDPI](https://tracker.freecadweb.org/search.php?tag_string=HiDPI)

## External references 

-   <https://doc.qt.io/qt-5/highdpi.html>
-   <https://doc.qt.io/qt-5/scalability.html>
-   <https://docs.microsoft.com/en-us/windows/win32/hidpi/high-dpi-desktop-application-development-on-windows>
-   <https://docs.microsoft.com/en-us/windows/win32/w8cookbook/high-dpi-for-desktop-apps-in-windows-8-1?redirectedfrom=MSDN>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Roadmap](Category_Roadmap.md) > HiDPI support/it
