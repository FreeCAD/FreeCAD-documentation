# Addon/it
## Introduzione

In FreeCAD e in questa documentazione, un addon è un componente che non fa parte dell\'installazione di base di FreeCAD, ma che può essere aggiunto al sistema con determinati metodi.



## I diversi tipi 

Esistono tre tipi di componenti aggiuntivi:

-   Le [Macro](Macros/it.md): brevi frammenti di codice [Python](Python/it.md) che forniscono un nuovo strumento o funzionalità in un singolo file che termina con `.FCMacro`.
-   Gli [Ambienti](External_workbenches/it.md): raccolte di file Python che forniscono [comandi GUI](Gui_Command/it.md) (strumenti) correlati, centrati su un argomento particolare, ad esempio strumenti per progettare cabine o strumenti per lavorare con l\'architettura o strumenti per progettare barche, ecc. Questi ambienti di lavoro di solito definiscono nuove barre degli strumenti in cui sono posizionati i pulsanti dei [comandi](Gui_Command/it.md).
-   [Pacchetti Preferenze](Preference_Packs/it.md): raccolte distribuibili di preferenze utente. {{Version/it|0.20}}



## Installazione

Il modo consigliato per installare i componenti aggiuntivi è con l\'<img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr/it.md).

Ma per le macro e gli ambienti di lavoro è anche possibile l\'installazione manuale:

-   [Come installare le macro](How_to_install_macros/it.md)
-   [Installare ambienti aggiuntivi](Installing_more_workbenches/it.md)



## Informazioni per gli sviluppatori 

Se avete sviluppato un workbench o una macro e volete vederlo incluso in Addon manager, leggete come farlo nelle pagine del repository ([FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons/) e [FreeCAD-macros](https://github.com/FreeCAD/FreeCAD-macros/)). Se aggiungete la vostra macro a [Raccolta di macro](Macros_recipes.md), non dovete fare nient\'altro, essa verrà automaticamente selezionata da Addon manager.

Vedere anche:

-   [Distribuzione di un workbench Python](Workbench_creation/it#Distribuzione.md)
-   [Distribuzione di un workbench C++](Workbench_creation/it#Distribuzione_2.md)



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > Addon/it
