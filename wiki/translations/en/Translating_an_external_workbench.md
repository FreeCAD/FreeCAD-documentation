# Translating an external workbench/en



In the following notes, `"context"` should be your addon\'s or workbench\'s name, for example, `"MySuperAddon"` or `"DraftPlus"`, or whatever. This context makes it so that all translation of your code will be gathered under the same name, to be more easily identified by translators. That is, they will know exactly to which addon or workbench a particular string belongs.

**Note**: Here is an all-in-one script that automates the complete procedure mentioned below (you are still advised to read the procedure to know what the script should do, though): <https://github.com/yorikvanhavre/BIM_Workbench/blob/master/utils/updateTranslations.py>

## Preparing the sources 

### General

-   Add a `translations/` folder. You can name it to something else, but this will be easier as it is the same throughout FreeCAD. In this folder, you will place the `.ts` files (the \"source\" translation files) and `.qm` files (compiled translation files).
-   Only the text that is shown to the user in the FreeCAD UI should be translated. Text that is only shown in the Python console should not be translated.
-   Text that prints to the `FreeCAD.Console` is shown in the \"Report view\", and therefore should be translated. The \"Report view\" is different from the Python console.

### In every Python .py file 

-   In every file where you need to translate text, you need a `translate()` function defined. An easy way is to use the one from the [Draft Workbench](Draft_Workbench.md):


```python
from DraftTools import translate
```

From FreeCAD 0.19, the FreeCAD module also defines a translate() function, it\'s best to use that one: 
```python
from FreeCAD.Qt import translate
```

-   All text that must be translated must be passed through the `translate()` function.


```python
print("My text")
```

becomes 
```python
print(translate("context", "My text"))
```

This can be used anywhere: in `print()`, in `FreeCAD.Console.PrintMessage()`, in Qt dialogs, etc. The `FreeCAD.Console` functions do not automatically add the newline character (`\n`), so this must be added at the end if desired. This character doesn\'t need translation either, so it can be outside the translating function: 
```python
FreeCAD.Console.PrintMessage(translate("context", "My text") + "\n")
```

-   If you are using `.ui` files made with QtDesigner, nothing special needs to be done with them.
-   When creating new objects, do not translate the object\'s \"Name\". Rather, translate object\'s \"Label\". The difference is that a \"Name\" is unique; it stays the same throughout the life of the object; on the other hand, a \"Label\" can be changed by the user as desired.
-   When creating properties for your objects, don't translate the property name. But place the description inside `QT_TRANSLATE_NOOP`:


```python
obj.addProperty("App::PropertyBool", "MyProperty", "PropertyGroup", QT_TRANSLATE_NOOP("App::Property", "This is what My Property does"))
```

Don\'t use your own `"context"` in this specific case. Keep `"App::Property"`.

-   Do not translate the text of document transactions made with `Document.openTransaction()`

### In InitGui.py 

-   Add the following line, close to the top of the file:


```python
def QT_TRANSLATE_NOOP(scope, text):
    return text
```

-   To translate menu names:


```python
self.appendMenu(QT_TRANSLATE_NOOP("context", "My menu"), [list of commands, ...])
```

-   The `QT_TRANSLATE_NOOP` macro doesn't do anything, but it marks texts to be picked up by the `lupdate` utility later on. Since it doesn\'t actually do anything, we only use it in special cases where FreeCAD itself takes care of everything.
-   Add the path to your `translations/` folder in the Initialized function:


```python
FreeCADGui.addLanguagePath("/path/to/translations")
```

The `InitGui.py` file has no **file** attribute, so it is not easy to find the translations folder's relative location. An easy way to work around this is to make it import another file from the same folder, and in that file, do 
```python
FreeCADGui.addLanguagePath(os.path.join(os.path.dirname(__file__), "translations"))
```

### Inside each FreeCAD command class 

-   Add the following line, close to the top of the file:


```python
def QT_TRANSLATE_NOOP(context, text):
    return text
```

-   Translate the `'MenuText'` and `'Tooltip'` of the command like this:


```python
def GetResources(self):
    return {'Pixmap'  : "path/to/icon.svg"),
            'MenuText': QT_TRANSLATE_NOOP("CommandName", "My Command"),
            'ToolTip' : QT_TRANSLATE_NOOP("CommandName", "Describes what the command does"),
            'Accel'   : "Shift+A"
    }
```

where `"CommandName"` is the name of the command, defined by 
```python
FreeCADGui.addCommand('CommandName', My_Command_Class())
```

## Gather all the strings from your module 

-   You will need the `lupdate`, `lconvert`, `lrelease` and `pylupdate` tools installed on your system. In Linux distributions they usually come in packages named `pyside-tools` or `pyside2-tools`. On some systems `lupdate` is named `lupdate4` or `lupdate5` or `lupdate-qt4` or similar. Same for the other tools. You may use the Qt4 or Qt5 version at your choice.
-   If you have `.ui` files, you need to run `lupdate` first:


```python
lupdate *.ui -ts translations/uifiles.ts
```

This is recursive and will find `.ui` files inside all your directory structure

-   If you have `.py` files, you need to run `pylupdate` too:


```python
pylupdate *.py -ts translations/pyfiles.ts
```

-   If you ran both operations, you now need to unify these two files into one:


```python
lconvert -i translations/uifiles.ts translations/pyfiles.ts -o translations/MyModule.ts
```

-   Check the contents of the three `.ts` files to make sure that they contain the strings, then you can delete both `pyfiles.ts` and `uifiles.ts`.
-   You can do it all in one bash script like this:


```python
#!/bin/sh
lupdate *.ui -ts translations/uifiles.ts
pylupdate *.py -ts translations/pyfiles.ts
lconvert -i translations/uifiles.ts translations/pyfiles.ts -o translations/MyModule.ts
rm translations/pyfiles.ts
rm translations/uifiles.ts
```

## Send the .ts file to a translation platform 

It is time to have your `.ts` file translated. You can choose to set up an account on a public translation platform such as [Crowdin](https://crowdin.com/) or [Transifex](https://www.transifex.com/), or you can benefit from our existing [FreeCAD-addons account at Crowdin](https://crowdin.com/project/freecad-addons), which has many users already, and therefore more chance to have your file translated quickly and by people who know FreeCAD.

If you wish to host your file on the FreeCAD Crowdin account, get in touch with [Yorik](https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=68) on the [FreeCAD forum](https://forum.freecadweb.org/).


**Note:**

some platforms like Crowdin can integrate with GitHub and do all the process from points 2, 3 and 4 automatically. For that, you can't use the FreeCAD Crowdin account; you will need to set up your own account.

## Merge the translations 

Once your `.ts` file has been translated, even if partially, you can download the translations from the site:

-   You will usually download a `.zip` file containing one `.ts` per language
-   Place all the translated `.ts` files, together with your base `.ts` file, in the `translations/` folder

## Compile the translations 

Now run the `lrelease` program on each file that you have. 
```python
lrelease "translations/Draft_de.ts"
lrelease "translations/Draft_fr.ts"
lrelease "translations/Draft_pt-BR.ts"
```

You can automate the process 
```python
for f in translations/*_*.ts
do
    lrelease "translations/$f"
done
```

You should find one `.qm` file for each translated `.ts` file. The `.qm` files is what will be used by Qt and FreeCAD at runtime.

That\'s all you need. Note that certain parts of your workbench cannot be translated on-the-fly if you decide to switch languages. If this is the case, you will need to restart FreeCAD for the new language to take effect.

## Testing translations 

1.  Switch FreeCAD to a language you have translated (ex. German)
2.  Load translation into FreeCAD, ex. `FreeCADGui.addTranslationPath("/path/to/the/folder/containing/qmfile")`
3.  Test something, ex. `FreeCAD.Qt.translate("your context","some string")`

Result: This should give you the German translation. If this works ok, then the basic setup is OK. Then we can look at something else. For ex, command names should always use a special context that is the name of the command as registered to FreeCAD.

### Important notes 

-   Make sure you are using a \*context\* and \*string\* that actually are in the ts/qm file of course.

## Important references 

-   Why and how to translate `openCommand()` functions ([forum thread](https://forum.freecadweb.org/viewtopic.php?f=10&t=55869))

## Related Pages 

-   [External Workbenches](External_Workbenches.md)
-   [Localisation](Localisation.md)
-   For more informations make your requests here [Translating external workbenches](https://forum.freecadweb.org/viewtopic.php?f=10&t=36413)


 

[Category:Developer Documentation](Category:Developer_Documentation.md)
