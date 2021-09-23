# Macros/sv
{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

Makron är ett smidigt sätt att skapa komplexa aktioner i FreeCAD. Du behöver bara spela in aktioner samtidigt som du gör dem, och sedan spara det under ett namn, och senare spela upp det när du vill. Eftersom makron i realiteten är en lista av python kommandon, så kan du även redigera det, och skapa mycket komplexa skript.


</div>

While Python scripts normally have the `.py` extension, FreeCAD macros should have the `.FCMacro` extension. A collection of macros written by experienced users is found in the [macros recipes](Macros_recipes.md) page.

See the [Power users hub](Power_users_hub.md) to learn more about the [Python](Python.md) programming language, and about writing macros. In particular, you should start with these pages:

-   [Introduction to Python](Introduction_to_Python.md)
-   [Python scripting tutorial](Python_scripting_tutorial.md)
-   [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md)


<div class="mw-translate-fuzzy">

### Hur det fungerar 

Om du aktiverar konsolutmatning(Meny Redigera -\> Alternativ -\> Allmänt -\> Makro -\> Visa skriptkommandon i python konsolen), så kommer du se att varje aktion du gör i FreeCAD, , som att klicka på en knapp, genererar ett python kommando. Dessa kommandon är vad som kan spelas in i ett makro. Huvudverktyget för att göra makron är makroverktygslådan: ![](images/Macros_toolbar.jpg ). På den finns det 4 knappar: Spela in, stoppa inspelning, redigera och spela upp det nuvarande makrot.


</div>

Enable the console output in the menu **Edit → Preferences → General → Macro → Show scripts commands in python console**. You will see that in FreeCAD, every action you do, such as pressing a button, outputs a Python command. Those commands are what can be recorded in a macro. The main tool for making macros is the macros toolbar: ![](images/Macros_toolbar.jpg ). On it you have 4 buttons: Record, stop recording, edit and play the current macro.


<div class="mw-translate-fuzzy">

Det är mycket enkelt att använda: Klicka på inspelningsknappen, du kommer att efterfrågas om ett namn till ditt makro, utför sedan några aktioner. När du är klar, Klick på stoppa inspelning knappen, och dina aktioner kommer att spaaras. Du kan nu komma åt makrodialogen med redigeraknappen:


</div>


<div class="mw-translate-fuzzy">

![](images/Macros.jpg )


</div>


<div class="mw-translate-fuzzy">

Där kan du hantera dina makron, radera, redigera eller skapa nya från scratch. Om du redigerar ett makro, så kommer det att öppnas i ett redigeringsfönster där du kan förändra dess kod.


</div>


<div class="mw-translate-fuzzy">

### Exempel

Klicka på inspelningsknappen, ge den ett namn, låt oss säga \"cylinder 10x10\", skapa skapa sedan med [Del arbetsbänken](Part_Workbench/sv.md) en cylinder med radien= 10 och höjden = 10. Klicka sedan på \"stoppa inspelning\" knappen. I redigera makro dialogen, så kan du se den python kod som har spelats in, och om du vill, göra ändringar på den. För att köra ditt makro, klicka på uppspelningsknappen i verktygslåden medan ditt makro är i redigeraren. Ditt makro sparas alltid till disk, så alla ändringar du gör, eller alla nya makron du skapar, kommer alltid att finnas tillgängliga nästa gång som du startar FreeCAD.


</div>

Press the record button, give a name, let\'s say \"cylinder 10x10\", then, in the [Part Workbench](Part_Workbench.md), create a cylinder with radius = 10 and height = 10. Then, press the \"stop recording\" button. In the edit macros dialog, you can see the python code that has been recorded, and, if you want, make alterations to it. To execute your macro, simply press the execute button on the toolbar while your macro is in the editor. You macro is always saved to disk, so any change you make, or any new macro you create, will always be available next time you start FreeCAD.


<div class="mw-translate-fuzzy">

### Anpassning

Det är förstås inte så praktiskt att behöva ladda ett makro i redigeraren för att kunna använda det. FreeCAD erbjuder många bättre sätt att använda ditt makro, som att tilldela en tangentbordsgenväg till den eller lägga till en punkt i menyn. När ditt makro är sparat, så kan allt detta göras via Verktyg -\> Anpassa menyn:


</div>

Of course it is not practical to load a macro in the editor in order to use it. FreeCAD provides much better ways to use your macro, such as assigning a keyboard shortcut to it or putting an entry in the menu. Once your macro is created, all this can be done via the **Tools → Customize** menu.

![](images/Macros_config.jpg )


<div class="mw-translate-fuzzy">

Pä detta sätt så kan du göra ditt makro till ett riktigt verktyg, precis som ett standardverktyg i FreeCAD . Detta, i tilläg till kraften hos pythonskripten i FreeCAD, gör det möjligt att lätt lägga till dina egna verktyg till gränssnittet. Läs vidare på [Skript](Scripting/sv.md) sidan om du vill veta mer om python skript\...


</div>

See [Customize Toolbars](Customize_Toolbars.md) for a more detailed description.


<div class="mw-translate-fuzzy">

### Skapa makron utan inspelning 

Du kan också direkt kopiera/klistra in python kod till ett makro, utan att behöva spela in aktioner i gränssnittet. Skapa bara ett nytt makro, redigera det, och klistra in din kod. Ditt makro sparas automatiskt när du stänger makroredigerings fönstret.


</div>

You can also directly copy/paste python code into a macro, without recording GUI action. Simply create a new macro, edit it, and paste your code. You can then save your macro the same way as you save a FreeCAD document. Next time you start FreeCAD, the macro will appear under the \"Installed Macros\" item of the Macro menu.

See [How to install macros](How_to_install_macros.md) for a more detailed description.


<div class="mw-translate-fuzzy">

### Makroförråd

Besök [Makrorecept](Macros_recipes/sv.md) sidan för att hämta några användbara makron att lägga till din FreeCAD installation.


</div>

There are two main places for macros. The first one is the official peer-reviewed macro repository on [GitHub](https://github.com/FreeCAD/FreeCAD-macros). The second one is the [Macros recipes](Macros_recipes.md) page from which you can pick some useful macros to add to your FreeCAD installation. Macros from both repositories can be installed via the [Addon Manager](Std_AddonMgr.md) directly from FreeCAD.

## Additional information 

-   [Automatically run macro at startup](Macro_at_Startup.md)
-   [Installing more workbenches](Installing_more_workbenches.md)

## Tutorials

You can manually install extensions, however, it is much simpler to just use the [Addon Manager](Std_AddonMgr.md).

-   [How to install macros](How_to_install_macros.md)
-   [How to install additional workbenches](How_to_install_additional_workbenches.md)


{{Powerdocnavi

}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md) [Category:Macros](Category:Macros.md)

---
[documentation index](../README.md) > [Developer Documentation](Category:Developer Documentation.md) > Macros/sv
