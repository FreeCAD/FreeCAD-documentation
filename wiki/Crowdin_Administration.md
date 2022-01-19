# Crowdin Administration
## Roles

-   Translator
    -   Ability to suggest and vote on translations in a language.
    -   Ask for more context; ask for clarity; report mistakes in the string to be translated; dispute a current translation entry etc\...

-   Proofreader
    -   Manages the translations that translators suggest and/or vote on. The proofreader then accepts/reject the translation.
    -   An extra step is needed to also give the final approval of the the translation string. Because \'Approving\' a translation requires reading it again and check-marking it, it provides a type of \'Quality Assurance\' layer. Once a translation is approved it will mark the string green and will add more progress to the green status bar of the language that is getting translated. The green progress bar can indicate the \'health\' of the language being translated. It also allows an extra flexibility to the developers to merge translations that have only been approved.
    -   Address the questions of translators within the Crowdin interface. For example, if more context is needed; or there\'s an error in the string that is to be translated, or a translation that was accepted or approved is disputed etc\...
    -   Report to devs any relevant issues that require changes to the source code etc..

## Filtering strings 

 <img alt="" src=images/Crowdin_Filter_Strings.png  style="width:500px;"> 

Filtering strings is a useful feature for proofreaders and managers. It give the person ability to effectively sort through many translation strings to for example show only strings that have been marked as \'missing more contextual information\' or \'incorrect source string\'. This service that the translators are doing for FreeCAD provides an extra layer of QA testing. Many typos, grammar issues, and even bugs can be exposed via checking translation strings. And so users mark these said problematic strings for us to respond to and eventually \'Resolve\'.

## Keyboard shortcuts 

 <img alt="" src=images/Crowdin_keyboard_shortcuts.png  style="width:300px;"> 

Using keyboard shortcuts is a major time-saving and efficiency tip. It is worth learning if you\'re a translator, proofreader, or manager. It is possible to see the list of keyboard shortcuts by pressing on the keyboard icon in the top right-hand portion of the Crowdin user interface.

**Important Note:** Please be mindful not to introduce mistakes in to translation strings produced by rogue keypresses that were meant to be a keyboard shortcut.

**Frequently used shortcuts:**

-   Copy source translation: **Alt**+**C**
-   Save translation: **Ctrl**+**Enter**
-   Approve translation: **Alt**+**L** (relevant for proofreaders)

## Fix translation issues 

If you notice a string in the FreeCAD UI that is not translated do the following:

1.  If you are not sure to which workbench the string belongs, first locate it in the FreeCAD source code. On Linux you can use {{Incode|grep -r "English text" *}}.
2.  For example, if the string is {{Incode|"Solver Calculix Standard"}} you will find this file: {{FileName|src/Mod/Fem/femcommands/commands.py}}, and you will know that the string belongs to the FEM workbench.
3.  Now search for this string on Crowdin. If your language is French visit <https://crowdin.com/project/freecad/fr>, go to the FEM workbench, and check if is there and translated.
4.  There two possibilities:
    1.  The string is not on Crowdin because it has not been picked up by the script that gathers strings from the FreeCAD source code and packs them into {{FileName|.ts}} files. There can be two reasons for this:
        -   The string is not properly handled by {{Incode|translate()}} code (or {{Incode|QT_TRANSLATE_NOOP()}} code for special cases like command names), that means there is a problem that must be solved in the source code.
        -   Everything seems normal, but the gathering script has a problem with that specific string, which can happen as it has many bugs.
    2.  The string is on Crowdin. There are several possibilities then:
        -   It might be that the latest Crowdin strings have not yet been merged. You can check if that\'s the case by searching for the string (see above), and check if it appears in the translated {{FileName|.ts}} files. In our example {{Incode|"Solver Calculix Standard"}} would then be found in {{FileName|src/Mod/Fem/Gui/Resources/translations/Fem_fr.ts}}. This indicates that the translated string is in the FreeCAD source and everything should be fine in the next build.
        -   If the string is still missing in the next build, the problem is more complex and we\'ll need to do some debugging:
            1.  Check in the source file if the original string is handled by {{Incode|translate()}} or {{Incode|QT_TRANSLATE_NOOP()}}.
            2.  Verify that the context matches what is on Crowdin.
            3.  In case of {{Incode|QT_TRANSLATE_NOOP()}}, there are several particular cases. For commands, the context must be the exact command name, the same as used in {{Incode|FreeCADGui.runCommand()}}. For properties it must be {{Incode|"App::Property"}}. For the names of menus and toolbars it must be {{Incode|"Workbench"}}.

## Links

-   [Localisation](Localisation.md)
-   [Crowdin Scripts](Crowdin_Scripts.md)
-   [Release process](Release_process.md)

 

[<img src="images/Property.png" style="width:16px"> Administration](Category_Administration.md)

---
[documentation index](../README.md) > [Administration](Category_Administration.md) > Crowdin Administration
