# Addon/it
{{TOCright}}

## Introduzione

In FreeCAD e in questa documentazione, un addon è un componente che non fa parte dell\'installazione di base di FreeCAD, ma che può essere aggiunto al sistema con determinati metodi.

## I diversi tipi 


<div class="mw-translate-fuzzy">

Esistono tre tipi di componenti aggiuntivi   *

-   Le [Macro](Macros/it.md)   * brevi frammenti di codice [Python](Python/it.md) che forniscono un nuovo strumento o funzionalità in un singolo file che termina con `.FCMacro`.
-   I Moduli   * un singolo file sorgente Python o una raccolta di file Python che estende il software in qualche modo. I moduli non definiscono necessariamente un \"ambiente di lavoro\" grafico ma possono fornire una funzione di supporto, ad esempio una libreria che esegue la conversione di formati o un codice che modifica l\'[interfaccia](interface/it.md) grafica.
-   Gli [Ambienti](External_workbenches/it.md)   * raccolte di file Python che forniscono [comandi GUI](Gui_Command/it.md) (strumenti) correlati, centrati su un argomento particolare, ad esempio strumenti per progettare cabine o strumenti per lavorare con l\'architettura o strumenti per progettare barche, ecc. Questi ambienti di lavoro di solito definiscono nuove barre degli strumenti in cui sono posizionati i pulsanti dei [comandi](Gui_Command/it.md).


</div>

## Installazione


<div class="mw-translate-fuzzy">

A partire da FreeCAD 0.17, il modo consigliato per installare i componenti aggiuntivi è tramite <img alt="" src=images/Std_AddonMgr.svg  style="width   *24px;"> [Addon Manager](Std_AddonMgr/it.md).


</div>


<div class="mw-translate-fuzzy">

L\'installazione manuale è ancora possibile.

-   [Come installare le macro](How_to_install_macros/it.md)
-   [Installare ambienti aggiuntivi](Installing_more_workbenches/it.md)


</div>

## Information for developers 

If you have developed a macro or workbench, and want to see it included in the Addon manager, read how to do so on the repository pages   * ([FreeCAD-addons](https   *//github.com/FreeCAD/FreeCAD-addons/) and [FreeCAD-macros](https   *//github.com/FreeCAD/FreeCAD-macros/)). If you add your macro to the [Macros recipes](Macros_recipes.md) page, there is nothing else to do, it will automatically be picked up by the Addon manager.

### Python workbenches 

For Python workbenches, you don\'t need any specific approval to have your workbench added to the Addon Manager. In addition, because your Addon is outside the FreeCAD source code, you can choose the license you want. If you request for your workbench to be added to the Addon Manager\'s default list (we will not add any new workbench without a request from its authors), either by asking so on the forum or by opening an issue on the [FreeCAD-addons](https   *//github.com/FreeCAD/FreeCAD-addons/) repository, your code will stay on your own git repository, we will just add it as a submodule to the [FreeCAD-addons](https   *//github.com/FreeCAD/FreeCAD-addons/) repository. Of course, before adding your workbench, we will take a look at it and make sure there is nothing potentially problematic with it. For more details about structuring your Addon, including information about metadata used by the Addon Manager, see [Workbench creation](Workbench_creation.md).

### C++ workbenches 

If you develop a workbench in C++, it cannot be run directly by users and must be compiled first. You then have two options, either you provide precompiled versions of your workbench yourself, for the different operating systems, or you should request to have your code merged into the FreeCAD source code. For that, you should use the LGPL license (or a fully compatible license like MIT or BSD), and you must present your new tools to the community in the [FreeCAD forum](https   *//forum.freecadweb.org) for review. Once your code has been tested and approved, you should fork the FreeCAD repository, if not done yet, create a new branch, push your code to it, and open a pull request so that your branch is merged into the main repository.




[Category   *Addons](Category_Addons.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > Addon/it
