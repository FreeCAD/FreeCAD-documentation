# Macro Editor Assistant/en
{{Macro
|Name=Macro Editor Assistant
|Icon=Editor_Assistant_Icon.svg
|Description=Extend functionality of FreeCAD's integrated Python editor
|Author=TheMarkster
|Version=1.91
|Date=2022-04-19
|FCVersion=Python 3 versions
|Download=[https://wiki.freecadweb.org/File:Editor_Assistant_Icon.svg ToolBar Icon]
|SeeAlso=
|Links=[https://github.com/mwganson/Editor_Assistant Documentation on Github]
}}

## Description

The Editor Assistant extends the capabilities of FreeCAD\'s integrated Python editor. The editor is quite good at what it does, but is somewhat limited in features. This macro attempts to supplement the editor by adding some of these missing features, including: search and replace, bookmarks, help references, snapshots, diffs, find highlighting, snippet text insertion via a templates mechanism, and more.

## Usage

Install and run the macro. A new dialog will appear as a third tab in the Combo view. As a third tab dialog it will not interfere with other task dialogs needing to use the Task tab for their dialogs. (If preferred, you can launch the macro as a dockable floating window by holding the Alt key while executing the macro.)

The macro will feature a list widget showing all the currently open editors. The editor selected will be the current editor to which the macro functions will be applied. When you select an editor from the list widget that editor is given the focus. (But selecting a new editor in the MDI area tab widget does not make it the current editor.) From time to time as new windows are opened and others are closed you will need refresh the list widget by pressing the Refresh button.

Full documentation can be found on GitHub: [Editor Assistant](https://github.com/mwganson/Editor_Assistant).

<img alt="" src=images/Editor_Assistant_scr1.png  style="width:400px;"> 
*Macro Editor Assistant screenshot‎*

## Legend


{{Codeextralink|https://gist.github.com/mwganson/20475dad57d9b659190f082d20e3bde6/raw/36b9e890ef920b5c8b81bde825d4dc48a32e704c/Editor_Assistant.FCMacro|Editor_Assistant.FCMacro}}

ToolBar Icon ![](images/Editor_Assistant_Icon.svg )

## Script

**Macro Editor_Assitant.FCMacro**


{{CodeDownload|https://gist.github.com/mwganson/20475dad57d9b659190f082d20e3bde6|Editor_Assitant.FCMacro}}



---
⏵ [documentation index](../README.md) > Macro Editor Assistant/en
