# Crowdin Administration/it



## Roles

-   Translator
    -   Ability to suggest and vote on translations in a language.
    -   Ask for more context; ask for clarity; report mistakes in the string to be translated; dispute a current translation entry etc\...

-   Proofreader
    -   Manages the translations that translators suggest and/or vote on. The proofreader then accepts/reject the translation.
    -   An extra step is needed to also give the final approval of the the translation string. Because \'Approving\' a translation requires reading it again and check-marking it, it provides a type of \'Quality Assurance\' layer. Once a translation is approved it will mark the string green and will add more progress to the green status bar of the language that is getting translated. The green progress bar can indicate the \'health\' of the language being translated. It also allows an extra flexibility to the developers to merge translations that have only been approved.
    -   Address the questions of translators within the crowdin interface. For example, if more context is needed; or there\'s an error in the string that is to be translated, or a translation that was accepted or approved is disputed etc\...
    -   Report to devs any relevant issues that require changes to the source code etc..

### Filtraggio delle stringhe 

<img alt="" src=images/Crowdin_Filter_Strings.png  style="width:300px;"> Il filtraggio delle stringhe è una funzione utile per revisori e manager. Permette di ordinare in modo efficace molte stringhe di traduzione, per esempio mostra solo le stringhe che sono state contrassegnate come \'mancanti di informazioni più contestuali\' o \'stringa sorgente errata\'. Questo servizio che i traduttori stanno facendo per FreeCAD fornisce un ulteriore livello di test di garanzia della qualità. Molti errori di battitura, problemi di grammatica e persino bug possono essere scoperti controllando le stringhe di traduzione. Gli utenti contrassegnano queste stringhe problematiche in modo che possiamo rispondere e alla fine risolverle.

------------------------------------------------------------------------

### Tasti di scelta rapida 

![](images/Crowdin_keyboard_shortcuts.png ) L\'utilizzo delle scorciatoie da tastiera è un trucco importante per risparmiare tempo ed essere più efficienti. Se siete un traduttore, un correttore di bozze o un manager vale la pena impararlo. È possibile visualizzare l\'elenco delle scorciatoie da tastiera premendo sull\'icona della tastiera nella parte in alto a destra dell\'interfaccia utente di Crowdin.

**Nota importante:** fare attenzione a non introdurre errori nelle stringhe di traduzione generate da pressioni di tasti inaffidabili che avrebbero dovuto essere una scorciatoia da tastiera.

#### Frequently used shortcuts 

-   Copy source translation: **Alt**+**C**
-   Save translation: **Ctrl**+**Enter**
-   Approve translation: **Alt**+**L** (relevant for proofreaders)

### Pagine pertinenti 

-   [Localizzazione](Localisation/it.md)
-   [Crowdin Scripts](Crowdin_Scripts/it.md)
-   [Release process](Release_process/it.md)




[Category:Administration](Category:Administration.md)
