# Translating an external workbench/es
<div class="mw-translate-fuzzy">

En las siguientes notas, `"contexto"` debe ser el mismo nombre de tu complemento o banco de trabajo, por ejemplo, `"MiSuperComplemento"` o `"DraftPlus"`, o el que sea. Este contexto hace que todas esas traducciones de tu código sean reunidas bajo el mismo nombre, para que sean mas fácilmente identificables por los traductores. Esto es, ellos sabrán exactamente a cual complemento o banco de trabajo una cadena de texto pertenece.


</div>

**Note**: Here is an all-in-one script that automates the complete procedure mentioned below (you are still advised to read the procedure to know what the script should do, though): <https://github.com/yorikvanhavre/BIM_Workbench/blob/master/utils/updateTranslations.py>

## Preparando las fuentes 

### General

-   Agregar una carpeta `translations/`. Puedes nombrarlo con algo más, pero esto sera mas sencillo como es el mismo en todo FreeCAD. En esta carpeta, tu colocaras los archivos `.ts` (Los archivos de traducción \"fuente\" ) y los archivos `.qm` (Archivos compilados de traducción).
-   Solo el texto que es mostrado al usuario en la Interface de usuario FreeCAD debera ser traducida. Solo el texto que es mostrado en la consola de python no debe ser traducida.
-   Texto que es impreso con `FreeCAD.Console` es mostrado en \"Vista de reporte\", y por lo tanto de ser traducido. La \"Vista de reporte es diferente a la consola de Python\".


<div class="mw-translate-fuzzy">

### En cada archivo Python .py: 


</div>

-   In every file where you need to translate text, you need a `translate()` function defined. You can use the fully-qualified name from Qt, but it\'s a little cleaner to use:

:   
    
```python
    import FreeCAD
    translate = FreeCAD.Qt.translate
    
```
    

-   All text that must be translated must be passed through the `translate()` function:

:   
    
```python
    print("My text")
    
```
    





:   becomes:





:   
    
```python
    print(translate("context", "My text"))
    
```
    





:   Be aware that `translate()` is not just a normal function: it also serves as a \"tag\" for the `lupdate` text-processing utility, so must be named exactly \"translate\". The `lupdate` program is a simple text processor, it does not execute your code. You must pass string literals directly to the `translate()` function: you cannot pass variables, constants, etc. For example:





:   
    
```python
    # This works:
    FreeCAD.Console.PrintMessage(translate("context", "My text") + "\n")

    # This does not, lupdate only sees the word "a_variable", and doesn't know what that is:
    a_variable = "My text"
    FreeCAD.Console.PrintMessage(translate("context", a_variable ) + "\n")

    # But this works -- a_variable will contain the translated string:
    a_variable = translate("context", "My text")
    FreeCAD.Console.PrintMessage(a_variable  + "\n")
    
```
    





:   This can be used anywhere: in `print()`, in `FreeCAD.Console.PrintMessage()`, in Qt dialogs, etc. The `FreeCAD.Console` functions do not automatically add the newline character (`\n`), so this must be added at the end if desired. This character doesn\'t need translation either, so it can be outside the translating function:





:   
    
```python
    FreeCAD.Console.PrintMessage(translate("context", "My text") + "\n")
    
```
    

-   If you are using `.ui` files made with QtDesigner, nothing special needs to be done with them.
-   When creating new objects, do not translate the object\'s \"Name\". Rather, translate the object\'s \"Label\". The difference is that a \"Name\" is unique; it stays the same throughout the life of the object; on the other hand, a \"Label\" can be changed by the user as desired.
-   When creating properties for your objects, don\'t translate the property name. But place the description inside `QT_TRANSLATE_NOOP`:

:   
    
```python
    obj.addProperty("App::PropertyBool", "MyProperty", "PropertyGroup", QT_TRANSLATE_NOOP("App::Property", "This is what My Property does"))
    
```
    





:   Don\'t use your own `"context"` in this specific case. Keep `"App::Property"`.

-   Do not translate the text of document transactions made with `Document.openTransaction()`

### In InitGui.py 

-   Add the following line near the top of the file:

:   
    
```python
    def QT_TRANSLATE_NOOP(context, text):
        return text
    
```
    





:   The `QT_TRANSLATE_NOOP` macro doesn\'t do anything, but it marks texts to be picked up by the `lupdate` utility later on. We only use it in special cases where FreeCAD itself takes care of everything.

-   To translate menu and toolbar names use the word `"Workbench"` as the context:

:   
    
```python
    self.appendMenu(QT_TRANSLATE_NOOP("Workbench", "My menu"), [list of commands, ...])
    self.appendToolbar(QT_TRANSLATE_NOOP("Workbench", "My toolbar"), [list of commands, ...])
    
```
    

-   Add the path to your `translations/` folder in the Initialized function:

:   
    
```python
    FreeCADGui.addLanguagePath("/path/to/translations")
    
```
    





:   The `InitGui.py` file has no **file** attribute, so it is not easy to find the translations folder\'s relative location. An easy way to work around this is to make it import another file from the same folder, and in that file do:





:   
    
```python
    FreeCADGui.addLanguagePath(os.path.join(os.path.dirname(__file__), "translations"))
    
```
    

### Inside each FreeCAD command class 

-   Add the following line near the top of the file:

:   
    
```python
    def QT_TRANSLATE_NOOP(context, text):
        return text
    
```
    

-   Translate the `'MenuText'` and `'Tooltip'` of the command like this:

:   
    
```python
    def GetResources(self):
        return {'Pixmap'  : "path/to/icon.svg"),
                'MenuText': QT_TRANSLATE_NOOP("CommandName", "My Command"),
                'ToolTip' : QT_TRANSLATE_NOOP("CommandName", "Describes what the command does"),
                'Accel'   : "Shift+A"
        }
    
```
    





:   where `"CommandName"` is the name of the command, defined by:





:   
    
```python
    FreeCADGui.addCommand('CommandName', My_Command_Class())
    
```
    

## Gather all the strings from your module 

-   You will need the `lupdate`, `lconvert`, `lrelease` and `pylupdate` tools installed on your system. In Linux distributions they usually come in packages named `pyside-tools` or `pyside2-tools`. On some systems `lupdate` is named `lupdate4` or `lupdate5` or `lupdate-qt4` or similar. Same for the other tools. You may use the Qt4 or Qt5 version at your choice.
-   If you have `.ui` files, you need to run `lupdate` first:

:   
    
```python
    lupdate *.ui -ts translations/uifiles.ts
    
```
    





:   This is recursive and will find `.ui` files inside your whole directory structure.

-   If you have `.py` files, you need to run `pylupdate` too:

:   
    
```python
    pylupdate *.py -ts translations/pyfiles.ts
    
```
    

-   If you ran both operations, you now need to unify these two files into one:

:   
    
```python
    lconvert -i translations/uifiles.ts translations/pyfiles.ts -o translations/MyModule.ts
    
```
    

-   Check the contents of the three `.ts` files to make sure that they contain the strings, then you can delete both `pyfiles.ts` and `uifiles.ts`.
-   You can do it all in one bash script like this:

:   
    
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

some platforms like Crowdin can integrate with GitHub and do all the process from points 2, 3 and 4 automatically. For that, you can\'t use the FreeCAD Crowdin account; you will need to set up your own account.

## Merge the translations 

Once your `.ts` file has been translated, even if partially, you can download the translations from the site:

-   You will usually download a `.zip` file containing one `.ts` per language
-   Place all the translated `.ts` files, together with your base `.ts` file, in the `translations/` folder

## Compile the translations 

Now run the `lrelease` program on each file that you have:


```python
lrelease "translations/Draft_de.ts"
lrelease "translations/Draft_fr.ts"
lrelease "translations/Draft_pt-BR.ts"
```

You can automate the process:


```python
for f in translations/*_*.ts
do
    lrelease "translations/$f"
done
```

You should find one `.qm` file for each translated `.ts` file. The `.qm` files is what will be used by Qt and FreeCAD at runtime.

That\'s all you need. Note that certain parts of your workbench cannot be translated on-the-fly if you decide to switch languages. If this is the case, you will need to restart FreeCAD for the new language to take effect.

## Testing translations 

1.  Switch FreeCAD to a language you have translated (for example German)
2.  Load translation into FreeCAD, ex. `FreeCADGui.addTranslationPath("/path/to/the/folder/containing/qmfile")`
3.  Test something, for example `FreeCAD.Qt.translate("your context","some string")`

Result: This should give you the German translation. If this works, then the basic setup is OK. Then we can look at something else. For example, command names should always use a special context that is the name of the command as registered to FreeCAD.

### Important notes 

-   Make sure you are using a \*context\* and \*string\* that actually are in the ts/qm file of course.

## Convenience script 

Yorik maintains a convenience script for the BIM workbench, that can gather, upload and download ts files. You can just copy and adapt that script for your workbench:

<https://github.com/yorikvanhavre/BIM_Workbench/blob/master/utils/updateTranslations.py>

## Technical details and advanced usage 

In the above examples there are two separate functions being used: `translate()` and `QT_TRANSLATE_NOOP`. You may also run across `tr()` and `QT_TR_NOOP`, which automatically provide the \"context\" argument based on their calling location. These two pairs of functions are fundamentally different.


`translate()`

and `tr()` accomplish two separate tasks: at runtime they perform the actual translation from the string passed into them to the final translated string. This is true whether they are provided a literal string, or a variable, or a constant: the lookup is dynamic and real-time during the run of the code. However, they provide an additional non-runtime function: they are recognized by the `pylupdate` utility. If (and only if) they contain a string literal, that literal is extracted by the utility. ONLY string literals are extracted by `pylupdate` \-- if a variable is passed it is ignored by the `pylupdate` utility. Qt will attempt to provide a translation at runtime, but this will only work if some other piece of code called one of the translation functions with the literal string that needs to be translated, so that `pylupdate` can extract it. Note that the code with the string literal need not actually ever execute, it must simply exist as a line of code in a file somewhere: `pylupdate` performs no analysis or code execution, it is simply performing a string search and extraction.

In contrast, `QT_TRANSLATE_NOOP` and `QT_TR_NOOP` do nothing at all at runtime: they are literal \"no-ops\", and are completely ignored by running code. Their only use is to mark a literal string for extraction by `pylupdate`: it never makes sense to place a variable within a call to one of these functions, it will have no effect. They are used in circumstances where `translate()` or `tr()` will be called with a variable containing the text to translate. For example, any code that is used to create a Command or a Property will use a NOOP-type function around the command menu text or tooltip, or the property docstring: at runtime when FreeCAD displays these items to the user it calls `translate()`: the literal strings must have been extracted by `pylupdate` at the point of creation, for example:


```python
def GetResources(self):
    return {'Pixmap'  : "path/to/icon.svg",
            'MenuText': QT_TRANSLATE_NOOP("CommandName", "My Command"),
            'ToolTip' : QT_TRANSLATE_NOOP("CommandName", "Describes what the command does"),
            'Accel'   : "Shift+A"
    }
```

In this usage, at runtime the dictionary returned by this function is literally:


```python
{ 
    'Pixmap'  : "path/to/icon.svg",
    'MenuText': "My Command",
    'ToolTip' : "Describes what the command does",
    'Accel'   : "Shift+A"
}
```

There is no reference to any type of translation information. When FreeCAD actually displays this information to the user, the pseudo-code is:


```python
for command in commands:
    resources = command.GetResources()
    menu_text = translate(resources['MenuText'])
```

In this case, `lupdate` cannot extract any string from the call to `translate()` because it refers to a variable. So `lupdate` ignores that call, but at runtime Qt searches for the string that\'s passed to it. As long as someplace in the code there is a call to one of the translation functions with a matching literal string (in this case, in the `GetResources()` function), this translation call will succeed.

To verify that the expected strings are being extracted, you can manually run the `pylupdate` command:


```python
pylupdate myfile.py -ts outfile.ts
```

The file `outfile.ts` will contain the set of strings that are uploaded to CrowdIn for translation.

## Important references 

-   Why and how to translate `openCommand()` functions ([forum thread](https://forum.freecadweb.org/viewtopic.php?f=10&t=55869))

## Related Pages 

-   [External Workbenches](External_Workbenches.md)
-   [Localisation](Localisation.md)
-   For more information make your requests here: [Translating external workbenches](https://forum.freecadweb.org/viewtopic.php?f=10&t=36413).




[<img src="images/Property.png" style="width:16px"> Developer Documentation](Category_Developer_Documentation.md)

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Translating an external workbench/es
