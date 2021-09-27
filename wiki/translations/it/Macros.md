# Macros/it
{{TOCright}}

## Introduzione

Le macro sono un modo pratico per riprodurre delle azioni complesse in FreeCAd. È sufficiente registrare le azioni così come vengono eseguite, quindi salvare queste azioni con un nome, per poterle ripetere quando si vuole. Dato che le macro sono in realtà un elenco di comandi [Python](Python/it.md), è anche possibile modificarle e creare degli script molto complessi.

Sebbene gli script Python abbiano normalmente l\'estensione `.py`, le macro di FreeCAD dovrebbero avere l\'estensione `.FCMacro`. Una raccolta di macro scritte da utenti esperti si trova nella pagina [raccolta di macro](macros_recipes/it.md).

Vedere l\'[Hub degli utenti esperti](Power_users_hub/it.md) per saperne di più sul linguaggio di programmazione [Python](Python/it.md) e sulla scrittura di macro. In particolare, si dovrebbe iniziare con queste pagine:

-   [Introduzione a Python](Introduction_to_Python/it.md)
-   [Guida agli Script Python](Python_scripting_tutorial/it.md)
-   [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)


<div class="mw-translate-fuzzy">

## Come funzionano 

Quando dal menu **Modifica → Preferenze → Generale → Macro → Mostra comandi script nella console python**, si attiva l\'output nella console si vede che ogni azione che si compie, come ad esempio la pressione di un pulsante, invia un comando Python. Questi comandi sono ciò che è possibile registrare in una macro. Lo strumento principale per creare una macro è la barra degli strumenti macro: ![](images/_Macros_toolbar.jpg ). Su di essa si trovano 4 tasti: Registrare, Interrompere la registrazione, Modificare e Riprodurre la macro corrente.


</div>

Enable the console output in the menu **Edit → Preferences → General → Macro → Show scripts commands in python console**. You will see that in FreeCAD, every action you do, such as pressing a button, outputs a Python command. Those commands are what can be recorded in a macro. The main tool for making macros is the macros toolbar: ![](images/Macros_toolbar.jpg ). On it you have 4 buttons: Record, stop recording, edit and play the current macro.

È molto semplice da usare: premere il pulsante di registrazione, dare un nome alla macro, quindi eseguire alcune azioni. Al termine, fare clic sul pulsante Interrompi registrazione, e le azioni compiute vengono salvate. Ora è possibile accedere alla finestra di dialogo delle macro utilizzando il pulsante Modifica,

![](images/Macros.png ) *Finestra di dialogo Macro, che elenca le macro disponibili nel sistema*

Quì è possibile gestire le macro, eliminarle, duplicarle, installarle, modificarle o crearne di nuove partendo da zero. Quando si modifica una macro, essa viene aperta in una finestra dell\'editor in cui è possibile apportare le proprie modifiche al codice. È possibile installare delle nuove macro utilizzando il pulsante {{button|Addons ...}}, che collega al [Addon Manager](AddonManager/it.md).


<div class="mw-translate-fuzzy">

## Esempio

Premere il pulsante di registrazione, fornire un nome, ad esempio, \"cilindro 10x10\", poi, nell\'[Ambiente Parte](Part_Workbench/it.md), creare un cilindro con raggio = 10 e altezza = 10. Quindi, premere il pulsante \"Interrompi registrazione\". Nella finestra di dialogo Modifica macro, è possibile vedere il codice python che è stato registrato, e, volendo, apportarvi delle modifiche. Per eseguire la macro, è sufficiente premere sul pulsante Esegui della barra degli strumenti, mentre la macro è nell\'editor. La macro viene sempre salvata su disco, in modo che tutte le modifiche apportate, o ogni nuova macro creata, sono sempre disponibili al successivo avvio di FreeCAD.


</div>

Press the record button, give a name, let\'s say \"cylinder 10x10\", then, in the [Part Workbench](Part_Workbench.md), create a cylinder with radius = 10 and height = 10. Then, press the \"stop recording\" button. In the edit macros dialog, you can see the python code that has been recorded, and, if you want, make alterations to it. To execute your macro, simply press the execute button on the toolbar while your macro is in the editor. You macro is always saved to disk, so any change you make, or any new macro you create, will always be available next time you start FreeCAD.


<div class="mw-translate-fuzzy">

## Personalizzazione

Naturalmente non è pratico dover caricare una macro nell\'editor per poterla utilizzare. FreeCAD fornisce modi migliori per usarle, come ad esempio l\'assegnazione ad essa di una scorciatoia da tastiera o l\'inserimento di una voce nel menu. Dopo aver creato la macro, tutto questo può essere fatto tramite il menu **Strumenti → Personalizza**.


</div>

Of course it is not practical to load a macro in the editor in order to use it. FreeCAD provides much better ways to use your macro, such as assigning a keyboard shortcut to it or putting an entry in the menu. Once your macro is created, all this can be done via the **Tools → Customize** menu.

![](images/Macros_config.jpg )


<div class="mw-translate-fuzzy">

[Personalizzare la barra degli strumenti.](Customize_Toolbars/it.md) In questo modo si può trasformare la macro in un vero e proprio strumento, proprio come qualsiasi strumento standard di FreeCAD. Questo, sommato alla potenza degli script Python all\'interno di FreeCAD, permette di aggiungere facilmente all\'interfaccia dei propri strumenti. Per maggiori informazioni sugli script [Python](Python/it.md), continuare la lettura alle pagine del [Centro utenti esperti](Power_users_hub/it.md) o degli [Script](Scripting/it.md)


</div>

See [Customize Toolbars](Customize_Toolbars.md) for a more detailed description.


<div class="mw-translate-fuzzy">

## Creare delle macro senza registrarle 

[Come installare le macro](How_to_install_macros/it.md). È anche possibile inserire direttamente con copia/incolla del codice python in un macro, senza registrare le azioni della GUI (dell\'interfaccia grafica). È sufficiente creare una nuova macro, modificarla, e incollare il codice. È quindi possibile salvare la macro nello stesso modo in cui si salva un documento di FreeCAD. Al prossima avvio di FreeCAD, la macro viene visualizzata in \"Macro installate\" nel menu Macro.


</div>

You can also directly copy/paste python code into a macro, without recording GUI action. Simply create a new macro, edit it, and paste your code. You can then save your macro the same way as you save a FreeCAD document. Next time you start FreeCAD, the macro will appear under the \"Installed Macros\" item of the Macro menu.

See [How to install macros](How_to_install_macros.md) for a more detailed description.


<div class="mw-translate-fuzzy">

## Repositorio di macro 

Visitare la pagina degli [esempi di macro](Macros_recipes/it.md) per trovare alcune utili macro da aggiungere alla propria installazione di FreeCAD.


</div>

There are two main places for macros. The first one is the official peer-reviewed macro repository on _ page from which you can pick some useful macros to add to your FreeCAD installation. Macros from both repositories can be installed via the [Addon Manager](Std_AddonMgr.md) directly from FreeCAD.


<div class="mw-translate-fuzzy">

## Link

[Installare ulteriori ambienti](Installing_more_workbenches/it.md)


</div>

-   [Automatically run macro at startup](Macro_at_Startup.md)
-   [Installing more workbenches](Installing_more_workbenches.md)


<div class="mw-translate-fuzzy">

## Tutorial

[Come installare ambienti di lavoro aggiuntivi](How_to_install_additional_workbenches/it.md).


</div>

You can manually install extensions, however, it is much simpler to just use the [Addon Manager](Std_AddonMgr.md).

-   [How to install macros](How_to_install_macros.md)
-   [How to install additional workbenches](How_to_install_additional_workbenches.md)


{{Powerdocnavi

}} 

_ _ _

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Macros/it
