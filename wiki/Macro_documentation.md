# Macro documentation
## Description

All macros should be properly documented in the same way [Gui Commands](Gui_Command.md) are documented. They should have an individual wiki page, and should be listed in one of the categories in [Macros recipes](Macros_recipes.md).

The [Macros recipes](Macros_recipes.md) page has a good selection of macros created by experienced users, and many of them can be directly installed from the [Addon Manager](Std_AddonMgr.md).

See [GuiCommand model](GuiCommand_model.md) and macro pages like [Macro Loft](Macro_Loft.md) and [Macro Site From Contours](Macro_Site_From_Contours.md) to see how macros should be documented. At least two sections should be included, a **Description** section with general usage information, and a **Script** section to hold the actual macro code. Other sections may be included as needed to explain with more detail the usage of the macro.

If a macro provides a well defined functionality, and is well documented, it could be included eventually as part of a new or an existing [workbench](Workbenches.md).

## New macro page 

Create a new page for the macro starting with the word `Macro_`, for example, `Macro_Excellent_Modification`. The link can be used without underscores as `<nowiki>[Macro Excellent Modification](Macro_Excellent_Modification.md)</nowiki>`, which results in [Macro Excellent Modification](Macro_Excellent_Modification.md); the spaces are automatically converted to underscores.

In the new page you should use _ at the top, with a minimum of information: 

{{Macro
|Name=Macro Excellent Modification
|Description=This macro does excellent things on existing shapes
|Author=your username
|Date=2018-11-30
}}



You can add a custom icon if it doesn\'t have the same name as the macro; you can also add other fields of information. 

{{Macro
|Name=Macro Excellent Modification
|Icon=Macro_custom_icon.svg
|Description=This macro does excellent things on existing shapes
|Author=your username
|Date=2018-11-30
|Version=3.14516
|SeeAlso=[[Macro Regular Modification]]
}}



When translating the page, use a localized template. You need to specify the name with the two letter language code (

{{Macro/fr
|Name=Macro Excellent Modification translated
|Icon=Macro_Excellent_Modification.svg
|Description=(Translated description)
|Author=your username
|Date=2018-11-30
}}



or use the `Translate` field



{{Macro/fr
|Name=Macro Excellent Modification
|Translate=Macro Excellent Modification translated
|Description=(Translated description)
|Author=your username
|Date=2018-11-30
}}
-   Use _ to upload the custom icon in [SVG](SVG.md) or PNG formats. It should have the same name as the macro.
-   Otherwise it will default to Icon=Text-x-python.svg <img alt="" src=images/Text-x-python.svg  style="width:32px;">.
-   For the macro used in the Python console by FreeCAD use Icon=Text_console_python.png <img alt="" src=images/Text_console_python.png  style="width:32px;">.
-   For the example video macro use this skeleton of the icon <img alt="" src=images/Text_Video_Movie.png  style="width:32px;"> and fill the screen for obtain ex: <img alt="" src=images/Macro_crank_simul.png  style="width:32px;"> and save the new icon with the same name of your macro.

_ will put the information on using and installing the macros in every page.

 <img alt="" src=images/Macro_Recipes_MacroHowToInstall.png  style="width:200px;">  
*[customize toolbars](How_to_install_macros]]_and_[[Customize_Toolbars.md) links in the infobox in each macro page*

### Adding the macro documentation 

-   Just like a [Gui Command](Gui_Command.md), explain what the macro does, its inputs, outputs, options, and limitations, if any.
-   Include a personalized icon in [SVG](SVG.md) or PNG format for your macro so that other users can include it in a custom toolbar.
-   Add one or more images to clarify the usage of your tool.
-   If the macro performs a complex task, consider adding an animated GIF to showcase its capabilities. The GIF image should have a maximum size of 500 x 500 pixels; if the GIF is bigger, the animation may not work. Do not resize the GIF as the wiki will not play resized GIFs.
-   Mention related macros and workbenches that complement the function of this tool.
-   Mention the version of FreeCAD used to create the macro. This information can be gathered from **Help → About FreeCAD → Copy to clipboard**.

:   When this information is pasted, it looks like this

 
```python
OS: Ubuntu 18.04.1 LTS
Word size of OS: 64-bit
Word size of FreeCAD: 64-bit
Version: 0.18.15302 (Git)
Build type: Release
Branch: master
Hash: 2e03d2f298677b8212c22cbbc3cb20b7c80eabb5
Python version: 2.7.15rc1
Qt version: 4.8.7
Coin version: 4.0.0a
OCC version: 7.3.0
Locale: English/UnitedStates (en_US)
```

Consider adding this information in a comment block inside the code of the macro.

### Adding the macro code 

Inside the **Script** section, use _ to place the code of the macro in the page. This will create a block of text that uses monospace font, which will preserve the whitespace that is essential for [Python](Python.md).

If the block of code contains the characters {{ }} (double closing brace and opening brace) or {{!}} (vertical bar), the <nowiki> ... </nowiki> tags can be added explicitly to allow displaying these special symbols.

This _ essentially generates a block of HTML tags <pre> ... </pre>, so these can be used directly instead of using the template. The [Addon Manager](Std_AddonMgr.md) will search for the biggest such block and use it for the body of the macro.



{{MacroCode|code=

«Your code should be here»

}}



Or if it includes the vertical bar 

{{MacroCode|code=
<nowiki>

«Your code should be here»

</nowiki>
}}



Or 

<pre>

«Your code should be here»

</pre>



Add header information before your actual code. 

{{MacroCode|code=
__Title__="Title_Of_macro"
__Author__ = "User_Name"
__Version__ = "00.11"
__Date__    = "2015-07-25"
__Comment__ = "This is the comment of the macro"
__Web__ = "http://forum.freecadweb.org/viewtopic.php?f=3&t=7384"
__Wiki__ = "http://www.freecadweb.org/wiki/index.php?title=Macro_Title_Of_macro"
__Icon__  = "/usr/lib/freecad/Mod/plugins/icons/Title_Of_macro"
__IconW__  = "C:/Documents and Settings/YourUserName/Application Data/FreeCAD"
__Help__ = "start the macro and follow the instructions"
__Status__ = "stable"
__Requires__ = "freecad 0.14.3706"
__Communication__ = "http://www.freecadweb.org/wiki/index.php?title=User:User_Name" 

«Your code should be here»
}}



Starting with FreeCAD 0.17, this information is used by the [Addon Manager](Std_AddonMgr.md), which downloads the macro from the [FreeCAD-macros](https://github.com/FreeCAD/FreeCAD-macros) repository.

### Adding macro code outside of the wiki 

If your macro is too big that it exceeds 64 KB, it won\'t be able to be hosted on the wiki. In this case, use _ with a link to the raw web address of the code.

For example: 

{{Codeextralink|https://gist.githubusercontent.com/mario52a/8d40ab6c018c2bde678f/raw/e16ad9ea7b38c0c47e42aa3019be01dd1267a620/FCInfo_en_Ver_1-20_Docked.FCMacro}}



It will be displayed as:  

This template must be placed at the beginning of the macro page, in the **Description** section. It must be the first block of code in the page so that the _ for an example of the usage.


{{ColoredParagraph|'''PS:''' In case upgrade in GitHub the path of the RAW code is modified not forgotten modify the link in the Codeextralink template.}}

## Adding the new macro to the wiki repository 

Use _ to include a line in the appropriate category in [Macros recipes](Macros_recipes.md); create a new category if needed.

 
```python
<nowiki>
* {{MacroLink|Macro_Excellent_Modification|Macro Excellent Modification```: the macro described in a short sentence.
</nowiki>
}}

-   The first argument is the name of the macro page in the wiki.
-   The second argument is the displayed text, which may be different from the page name. This will create a link to the first argument, showing the second argument as the text.
-   A short description of the macro comes after the colon.

You can also use the optional parameter  
```python
<nowiki>
* {{MacroLink|Icon=Macro_Excellent_Modification.svg|Macro_Excellent_Modification|Macro Excellent Modification```: the macro described in a short sentence.
</nowiki>
}}

To localize this template, use the appropriate language link in the first argument.  
```python
<nowiki>
* {{MacroLink|Macro_Excellent_Modification/fr|Macro Excellent Modification```: (translated description)
</nowiki>
}}

## Adding the new macro to the central repository 

To make a macro installable from the [Addon Manager](Std_AddonMgr.md) it should be included in the central [FreeCAD-macros](https://github.com/FreeCAD/FreeCAD-macros) repository.

In order to include the macro there, first it must be reviewed by the FreeCAD community in the [Python scripting and macros](https://forum.freecadweb.org/viewforum.php?f=22) subforum. Once this is done, the FreeCAD-macros repository should be forked, the new macro should be included in a branch, and then the branch should be pushed and merged into the upstream repository.



_ _

---
[documentation index](../README.md) > [Macros](Category_Macros.md) > Macro documentation
