---
- GuiCommand:
   Name:Std WhatsThis
   MenuLocation:Help → What's This?
   Workbenches:All
   Shortcut:**Shift**+**F1**
   SeeAlso:[Std OnlineHelp](Std_OnlineHelp.md)
---

## Description

The **Std WhatsThis** command opens the help documentation for a specified command.

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Std_WhatsThis.svg" width=16px> [Std WhatsThis](Std_WhatsThis.md)** button.
    -   Select the {{MenuCommand|Help → <img src="images/Std_WhatsThis.svg" width=16px> What's This?}} option from the menu.
    -   Use the keyboard shortcut: **Shift**+**F1**.
2.  Click on a toolbar button or on a menu option.
3.  The help documentation for the selected command opens in a new window.

## Notes

-   Some commands are not documented, in that case the offline help will open on a blank page and report that the page could not be found.
-   The documentation is based on Qt compiled HTML pages. For it to launch Qt Assistant must be installed.
-   On Debian/Ubuntu and possibly other Linux systems, the offline documentation may need to be installed separately. The package is named {{FileName|freecad-doc}}, or {{FileName|freecad-daily-doc}} (for the freecad-daily PPA). See [Installing Helpfile](Installing_Helpfile.md).

Read this post to understand how the commands must be named in the code to match the help pages in the wiki.

-   [Bunch of TechDraw pages don\'t have the correct name](https://forum.freecadweb.org/viewtopic.php?t=27265)





{{Std Base navi

}}  
