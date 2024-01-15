# Macro Template
{{Macro
    |Name=Macro_Template
    |Description=Minimum required text to publish the FreeCAD Addon.
    |Author=Screeneroner
    |Version=Template
    |Date=2023-09-28
}}

## THE GUIDE 

To make your macro available in the Addon Manager, it must be published in the FreeCAD Repository. There are two ways to do it with and without GitHub. Publishing via GitHub requires its deep knowledge, which most of us haven\'t. So here will be described the easiest way - without GitHub.

Actually the FreeCAD Repository is a wiki web page <https://wiki.freecad.org/Macros_recipes>. Once you (by yourself) add here a link to the properly formatted wiki-page, you macros will be shown in the FreeCAD Addon Manager. To make changes to this repository page and pages with your macros, you should become a wiki-editor. You can\'t register as the editor by yourself. Instead, you should send a private message to \@yorik and/or \@Kunda1 with request containing you login and preferred e-mail (the latest changes in getting wiki editing permissions you may find here <https://forum.freecad.org/viewforum.php?f=21>). Once you get a e-mail with admins response (be patient - it may request several days), follow the link in it activate your new account, then set a permanent password, and confirm your e-mail. Now you can start publishing your macros.

The following codes snippets you should use to create your own macro that will be available in the FreeCAD Addon Manager:

1.  for wiki page about your macro with its code inside
2.  for making your macro visible in the FreeCAD Addon Manager macros list.

## 1. Code for pasting into your wiki page editor 

Type in your web browser address <https://wiki.freecad.org/Macro_My_Macro_Name> (replace the placeholder \'My_Macro_Name\' with your real name). The prefix \"Macro\_\" after the \"wiki.freecad.org/\" is mandatory. If the name is used - you will see its content. In this case, you should choose another macro name. If name is available - you will see an empty page with a link at its end \"create this page\". Click it to create your page and paste into the empty entry field this snippet:

    {{Macro
        |Name=Macro_Template
        |Description=Minimum required text to publish the FreeCAD Addon.
        |Author=Screeneroner
        |Version=Template
        |Date=2023-09-28
    }}
    ==Script==
    {{MacroCode|code=
    &lt;nowiki>
    __Name__    = "Macro_Template"
    __Comment__ = "This page contains the minimum required text to publish the FreeCAD Addon"
    __Author__  = "Screeneroner"
    __Version__ = "Template"
    __Date__    = "2023-08-01"
    __Help__    = "Use this text to start publishing your macro"

    print("Hello World!")
    &lt;/nowiki>
    }}

## 2. Code for pasting into [Addon Macro Repository](https://wiki.freecad.org/index.php?title=Macros_recipes) 

    * <img style="width:16px;" src="images/Applications-python.svg"> [Macro Template](Macro_Template.md): Macro Template for the new macro wiki page.

## Script

This is the real script that just prints text \"Hello World!\" in the FreeCAD console. Once you create the wiki page about your macro and include it in Addon Manager Repository, you may install it and verify that the installed version of \'your\' macro really makes the given printout. If all working fine - you may start replacing dummy print with your real code.


{{MacroCode|code=
__Name__    = "Macro_Template"
__Comment__ = "This page contains the minimum required text to publish the FreeCAD Addon"
__Author__  = "Screeneroner"
__Version__ = "Template"
__Date__    = "2023-08-01"
__Help__    = "Use this text to start publishing your macro"

print("Hello World!")
}}



---
⏵ [documentation index](../README.md) > Macro Template
