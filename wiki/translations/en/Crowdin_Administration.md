# Crowdin Administration/en


## Roles

-   Translator
    -   Ability to suggest and vote on translations in a language.
    -   Ask for more context; ask for clarity; report mistakes in the string to be translated; dispute a current translation entry etc\...

-   Proofreader
    -   Manages the translations that translators suggest and/or vote on. The proofreader then accepts/reject the translation.
    -   An extra step is needed to also give the final approval of the the translation string. Because \'Approving\' a translation requires reading it again and check-marking it, it provides a type of \'Quality Assurance\' layer. Once a translation is approved it will mark the string green and will add more progress to the green status bar of the language that is getting translated. The green progress bar can indicate the \'health\' of the language being translated. It also allows an extra flexibility to the developers to merge translations that have only been approved.
    -   Address the questions of translators within the crowdin interface. For example, if more context is needed; or there\'s an error in the string that is to be translated, or a translation that was accepted or approved is disputed etc\...
    -   Report to devs any relevant issues that require changes to the source code etc..

### Filtering Strings 

<img alt="" src=images/Crowdin_Filter_Strings.png  style="width:300px;"> Filtering strings is a useful feature for proofreaders and managers. It give the person ability to effectively sort through many translation strings to for example show only strings that have been marked as \'missing more contextual information\' or \'incorrect source string\'. This service that the translators are doing for FreeCAD provides an extra layer of QA testing. Many typos, grammar issues, and even bugs can be exposed via checking translation strings. And so users mark these said problematic strings for us to respond to and eventually \'Resolve\'.

------------------------------------------------------------------------

### Keyboard Shortcuts 

![](images/Crowdin_keyboard_shortcuts.png ) Using keyboard shortcuts is a major time-saving and efficiency tip. It is worth learning if you\'re a translator, proofreader, or manager. It is possible to see the list of keyboard shortcuts by pressing on the keyboard icon in the top right-hand portion of the Crowdin user interface.

**Important Note:** Please be mindful not to introduce mistakes in to translation strings produced by rogue keypresses that were meant to be a keyboard shortcut.

#### Frequently used shortcuts 

-   Copy source translation: **Alt**+**C**
-   Save translation: **Ctrl**+**Enter**
-   Approve translation: **Alt**+**L** (relevant for proofreaders)

### Relevant Pages 

-   [Localisation](Localisation.md)
-   [Crowdin Scripts](Crowdin_Scripts.md)
-   [Release process](Release_process.md)




[Category:Administration](Category:Administration.md)
