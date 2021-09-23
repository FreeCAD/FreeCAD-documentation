# Themes
{{TOCright}}

## Description

**Note:** the term \'stylesheet\' is interchangeable with the term \'theme\'

FreeCAD supports complete theming of its interface via the Qt Style Sheet `.qss` format. The [qss format](https://doc.qt.io/qt-5/stylesheet-syntax.html) is **very** similar to [Cascading Style Sheets (css) format](https://en.wikipedia.org/wiki/CSS) used in web pages. It basically adds methods (in a separate .qss file) to reference the different widgets and elements of the Qt interface (as one would an .html file). You can change the default theme (which simply takes the style defined by your desktop system) by selecting a different **style sheet** in the [FreeCAD preferences](Preferences_Editor#General.md).

## Customization

As mentioned above, one can tweak or even create their own own theme to suit their personal needs and taste.

### Location

Default themes that come bundled in to the FreeCAD source code live in [`src/Gui/Stylesheets`](https://github.com/FreeCAD/FreeCAD/tree/master/src/Gui/Stylesheets)

If one chooses to tweak a preexisting theme or create their own, all that needs to be done is to either copy the preexisting theme or create a new theme and place in a specific local folder for it to be found by FreeCAD:

-    {{FileName|%APPDATA%/FreeCAD/Gui/Stylesheets}}(on Windows). The {{FileName|%APPDATA%}} folder can be retrieved by entering {{Incode|App.getUserAppDataDir()}} in the [Python console](Python_console.md).

-    {{FileName|$HOME/.FreeCAD/Gui/Stylesheets}}(on Linux).

-    {{FileName|$HOME/Library/Preferences/FreeCAD/Gui/Stylesheets}}(on macOS).

### Syntax

-   Toolbars are called `QToolBar`
-   Tools are called `QToolButton`

## Related

-   ModernUI theme by hakanseven12 [ModernUI Workbench](ModernUI_Workbench.md)
-   ProDark theme by turn211 <https://github.com/turn211/ProDark-FreeCAD-theme>
-   VerticalUI theme by studio petrikas
-   FreeCAD [Interface Customization](Interface_Customization.md)

 {{Interface navi}} 

[Category:Developer Documentation](Category:Developer_Documentation.md)

---
[documentation index](../README.md) > [Developer Documentation](Category:Developer Documentation.md) > Themes
