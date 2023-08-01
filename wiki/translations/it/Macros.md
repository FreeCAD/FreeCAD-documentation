# Macros/it
## Introduzione

Le macro sono un modo pratico per riprodurre delle azioni complesse in FreeCAd. È sufficiente registrare le azioni così come vengono eseguite, quindi salvare queste azioni con un nome, per poterle ripetere quando si vuole. Dato che le macro sono in realtà un elenco di comandi [Python](Python/it.md), è anche possibile modificarle e creare degli script molto complessi.

Sebbene gli script Python abbiano normalmente l\'estensione `.py`, le macro di FreeCAD dovrebbero avere l\'estensione `.FCMacro`. Una raccolta di macro scritte da utenti esperti si trova nella pagina [raccolta di macro](macros_recipes/it.md).

Vedere l\'[Hub degli utenti esperti](Power_users_hub/it.md) per saperne di più sul linguaggio di programmazione [Python](Python/it.md) e sulla scrittura di macro. In particolare, si dovrebbe iniziare con queste pagine:

-   [Introduzione a Python](Introduction_to_Python/it.md)
-   [Guida agli Script Python](Python_scripting_tutorial/it.md)
-   [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

## Come funzionano 

Abilitare l\'output della console nel menu **Modifica → Preferenze → Generale → Macro → Mostra lo script dei comandi nella console Python**. Si noterà che in FreeCAD, ogni azione eseguita, come premere un pulsante, genera un comando Python. Questi comandi possono essere registrati in una macro. Lo strumento principale per creare macro è la barra degli strumenti delle macro: ![](images/Macros_toolbar.jpg ). Su di esso ci sono 4 pulsanti: Registra una macro, interrompi la registrazione, modifica e riproduci la macro corrente.

È molto semplice da usare: premere il pulsante di registrazione, dare un nome alla macro, quindi eseguire alcune azioni. Al termine, fare clic sul pulsante Interrompi registrazione, e le azioni compiute vengono salvate. Ora è possibile accedere alla finestra di dialogo delle macro utilizzando il pulsante Modifica,

![](images/Macros_it.png ) 
*Finestra di dialogo Macro, che elenca le macro disponibili nel sistema*

Quì è possibile gestire le macro, eliminarle, duplicarle, installarle, modificarle o crearne di nuove partendo da zero. Quando si modifica una macro, essa viene aperta in una finestra dell\'editor in cui è possibile apportare le proprie modifiche al codice. È possibile installare delle nuove macro utilizzando il pulsante {{button|Addons ...}}, che collega al [Addon Manager](Std_AddonMgr/it.md).

## Esempio

Premere il pulsante di registrazione, fornire un nome, ad esempio, \"cilindro 10x10\", poi, nell\'[Ambiente Parte](Part_Workbench/it.md), creare un cilindro con raggio = 10 e altezza = 10. Quindi, premere il pulsante \"Interrompi registrazione\". Nella finestra di dialogo Modifica macro, è possibile vedere il codice python che è stato registrato, e, volendo, apportarvi delle modifiche. Per eseguire la macro, è sufficiente premere sul pulsante Esegui della barra degli strumenti, mentre la macro è nell\'editor. La macro viene sempre salvata su disco, in modo che tutte le modifiche apportate, o ogni nuova macro creata, sono sempre disponibili al successivo avvio di FreeCAD.

## Personalizzazione

Naturalmente non è pratico dover caricare una macro nell\'editor per poterla utilizzare. FreeCAD fornisce modi migliori per usarle, come ad esempio l\'assegnazione ad essa di una scorciatoia da tastiera o l\'inserimento di una voce nel menu. Dopo aver creato la macro, tutto questo può essere fatto tramite il menu **Strumenti → Personalizza**.

![](images/Macros_config_it.png )

In questo modo si può trasformare la macro in un vero strumento, proprio come qualsiasi strumento standard di FreeCAD. Questo, aggiunto alla potenza dello scripting Python all\'interno di FreeCAD, rende possibile aggiungere facilmente i propri strumenti all\'interfaccia.

Vedi [Personalizza le barre degli strumenti](Customize_Toolbars/it.md) per una descrizione più dettagliata.

## Creare delle macro senza registrarle 

Puoi anche copiare/incollare direttamente il codice Python in una macro, senza registrare l\'azione della GUI. Basta creare una nuova macro, modificarla e incollare il codice. È quindi possibile salvare la macro nello stesso modo in cui si salva un documento di FreeCAD. La prossima volta che avvierai FreeCAD, la macro apparirà sotto la voce \"Macro\...\" del menu Macro.

Vedere [Come installare le macro](How_to_install_macros/it.md) per una descrizione più dettagliata.

## Repositorio di macro 

Ci sono due posti principali per le macro. Il primo è il repository di macro ufficiale sottoposto a revisione paritaria su [GitHub](https://github.com/FreeCAD/FreeCAD-macros). La seconda è la pagina [Raccolta di macro](Macros_recipes/it.md) da cui puoi scegliere alcune utili macro da aggiungere alla tua installazione di FreeCAD. Le macro di entrambi i repository possono essere installate tramite [Addon Manager](Std_AddonMgr/it.md) direttamente da FreeCAD.

## Informazioni aggiuntive 

-   [Eseguire automaticamente una macro all\'avvio](Macro_at_Startup/it.md)
-   [Installazione di più Ambienti di lavoro](Installing_more_workbenches/it.md)

## Tutorial

È possibile installare manualmente le estensioni, tuttavia è molto più semplice utilizzare semplicemente l\'[Addon Manager](Std_AddonMgr/it.md).

-   [Come installare le macro](How_to_install_macros/it.md)
-   [Come installare Ambienti di lavoro aggiuntivi](How_to_install_additional_workbenches/it.md)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > [Macros](Category_Macros.md) > Macros/it
