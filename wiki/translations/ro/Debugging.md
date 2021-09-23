# Debugging/ro



<div class="mw-translate-fuzzy">





</div>


{{TOCright}}


<div class="mw-translate-fuzzy">

## Testează mai întâi 

Înainte de a trece prin durerea de a depana utilizați [Test framework](Testing/ro.md) pentru a verifica dacă testele standard funcționează corect. Dacă acestea nu se execută complet, este posibil să fie o instalare defectuoasă.


</div>

Before you go through the pain of debugging use the [Test framework](Testing.md) to check if the standard tests work properly. If they do not run complete there is possibly a broken installation.


<div class="mw-translate-fuzzy">

## Linie de Commandă 

Depanarea *debugging* în FreeCAD este susținută de câteva mecanisme interne. Versiunea liniei de comandă a FreeCAD oferă câteva opțiuni pentru suportul de depanare.


</div>

The *debugging* of FreeCAD is supported by a few internal mechanisms. The command line version of FreeCAD provides some options for debugging support.


<div class="mw-translate-fuzzy">

Acestea sunt opțiunile recunoscute curent în FreeCAD 0.15:


</div>


<div class="mw-translate-fuzzy">

Generic options:

 -v [ --version ]      Prints version string
 -h [ --help ]         Prints help message
 -c [ --console ]      Starts in console mode
 --response-file arg   Can be specified with '@name', too


</div>


<div class="mw-translate-fuzzy">

Configuration:

 -l [ --write-log ]       Writes a log file to:
                          $HOME/.FreeCAD/FreeCAD.log
 --log-file arg           Unlike to --write-log this allows to log to an 
                          arbitrary file
 -u [ --user-cfg ] arg    User config file to load/save user settings
 -s [ --system-cfg ] arg  System config file to load/save system settings
 -t [ --run-test ] arg    Test level
 -M [ --module-path ] arg Additional module paths
 -P [ --python-path ] arg Additional python paths


</div>


<div class="mw-translate-fuzzy">

## Generarea unei Backtrace 

Dacă rulați o versiune experimentală de FreeCAD care este încă în curs de dezvoltare, aceasta poate \"îngheța\". Vă puteți ajuta să rezolvați astfel de probleme furnizând dezvoltatorilor o \"backtrace\". Pentru a face acest lucru, trebuie să executați o \"Debug build\" a software-ului. \"Debug build\" este un parametru care este setat în timpul compilării, deci va trebui fie să compilați FreeCAD dvs înșivă, fie să obțineți o versiune \"debug\" precompilată.


</div>

If you are running a version of FreeCAD from the bleeding edge of the development curve, it may \"crash\". You can help solve such problems by providing the developers with a \"backtrace\". To do this, you need to be running a \"debug build\" of the software. \"Debug build\" is a parameter that is set at compile time, so you\'ll either need to compile FreeCAD yourself, or obtain a pre-compiled \"debug\" version.

### For Linux 


<div class="toccolours mw-collapsible mw-collapsed" style="width:800px;">

Linux Debugging →


<div class="mw-collapsible-content">

Prerequisites:


<div class="mw-translate-fuzzy">

-   varianta software de package gdb instalat
-   o depanare a variantei compilate a FreeCAD (în acest moment disponibilă prin [building from source](CompileOnUnix#For_a_Debug_build.md))
-   un model FreeCAD care a cauzat crash-ul


</div>

Pași: Introduceți următoarelor în fereastra terminalului dvs:

Find FreeCAD binary on your system:


```python
$ whereis freecad
freecad: /usr/local/freecad <--- for example

$ cd /usr/local/freecad/bin
$ gdb FreeCAD
```

GNUdebugger will output some initializing information. The (gdb) shows GNUDebugger is running in the terminal, now input:


```python
(gdb) handle SIG33 noprint nostop
(gdb) run
```

FreeCAD va porni. Efectuați pașii care determină ca FreeCAD să se prăbușească sau să înghețe, apoi introduceți în fereastra terminalului:


```python
(gdb) bt
```

Aceasta va genera o listă lungă a exact ceea ce a făcut programul atunci când sa prăbușit sau a înghețat. Includeți acest lucru cu raportul problemei dvs.


```python
(gdb) bt full
```

Print the values of the local variables also. This can be combined with a number to limit the number of frames shown.


</div>


</div>


<div class="mw-translate-fuzzy">

### For MacOSX 


</div>


<div class="toccolours mw-collapsible mw-collapsed" style="width:800px;">


<div class="mw-translate-fuzzy">

MacOSX Debugging →


</div>


<div class="mw-collapsible-content">

Prerequisites:

-   software package lldb installed
-   a debug build of FreeCAD
-   a FreeCAD model that causes a crash

Steps: Enter the following in your terminal window:


```python
$ cd FreeCAD/bin
$ lldb FreeCAD
```

LLDB will output some initializing information. The (lldb) shows the debugger is running in the terminal, now input:


```python
(lldb) run
```

FreeCAD va porni. Efectuați pașii care determină ca FreeCAD să se prăbușească sau să înghețe, apoi introduceți în fereastra terminalului:


```python
(lldb) bt
```

Aceasta va genera o listă lungă a exact ceea ce a făcut programul atunci când sa prăbușit sau a înghețat. Includeți acest lucru cu raportul problemei dvs.


</div>


</div>

## List Libraries Loaded by FreeCAD 

(Applicable to Linux and macOS)

Sometimes it\'s helpful to understand what libraries FreeCAD is loading, specifically if there are multiple libraries being loaded of the same name but different versions (version collision). In order to see which libraries are loaded by FreeCAD when it crashes you should open a terminal and run it in the debugger. In a second terminal window, find out the process id of FreeCAD:


`ps -A &#124; grep FreeCAD`

Use the returned id and pass it to `lsof`:


` lsof -p process_id`

This prints a long list of loaded resources. So for example, if trying to ascertain if more than one Coin3d library versions is loaded, scroll through the list or search directly for Coin in the output:


`lsof -p process_id &#124; grep Coin`


<div class="mw-translate-fuzzy">

## Python Debugging 

Pentru o abordare mai modernă a depanării Python, cel puțin în Windows, a se vedea asta

-   [Debugging macros with VS 2017](https://forum.freecadweb.org/viewtopic.php?f=22&t=28901)
-   [Python workbenches debugging](https://forum.freecadweb.org/viewtopic.php?f=10&t=35383)


</div>

For a more modern approach to debugging Python, see these posts:

-   [Debugging macros with VS 2017](https://forum.freecadweb.org/viewtopic.php?f=22&t=28901)
-   [Python workbenches debugging](https://forum.freecadweb.org/viewtopic.php?f=10&t=35383)
-   [python3.dll, Qt5Windgets.dll, Qt5Gui.dll and Qt5Core.dll not found](https://forum.freecadweb.org/viewtopic.php?f=4&t=40251)

### winpdb


<div class="toccolours mw-collapsible mw-collapsed" style="width:800px;">

winpdb Debugging →


<div class="mw-collapsible-content">

Here is an example of using *Winpdb* inside FreeCAD:


<div class="mw-translate-fuzzy">

Avem nevoie de depanatorul Python: \'\' Winpdb \'\'. Dacă nu aveți instalat, instalați-l sub Ubuntu / Debian cu:


</div>


```python
sudo apt-get install winpdb
```

Acum permiteți configurarea programului de depanare.


<div class="mw-translate-fuzzy">

1.  Start *Winpdb*.
2.  Set the debugger password to \"test\": Go to menu *File*-\>\'\'Password\" and set the password.


</div>


<div class="mw-translate-fuzzy">

Acum vom rula pas cu pas un script de testare Python în FreeCAD.


</div>

1.  Rulați winpdb și definiți password (e.g. test)
2.  Creați un fișier Python cu acest conținut


```python
import rpdb2
rpdb2.start_embedded_debugger("test")
import FreeCAD
import Part
import Draft
print "hello"
print "hello"
import Draft
points=[FreeCAD.Vector(-3.0,-1.0,0.0),FreeCAD.Vector(-2.0,0.0,0.0)]
Draft.makeWire(points,closed=False,face=False,support=None)
```

1.  Dați Start la FreeCAD și încărcați fișierul de mai sus în FreeCAD
2.  Apăsați F6 ptru al-l executa
3.  Acum FreeCAD se va bloca (nu va răspunde) deoarece debuggerul Python este în așteptare
4.  Comutați pe Windpdb GUI și click on \"Attach\". După câteva secunde un articol \"\" apare acolo unde ați făcut dublu clic
5.  Acum Scriptul aflat în execuție curentă apare în Winpdb.
6.  Definiți o pauză la ultima linie și apăsați F5
7.  Acum apăsați F7 pentru a intra în codul Python al Draft.makeWire


</div>


</div>

### Visual Studio Code (VS Code) 


<div class="toccolours mw-collapsible mw-collapsed" style="width:800px;">

VS Code Debugging →


<div class="mw-collapsible-content">

Prerequisites:

-   ptvsd package need to be installed


```python
pip install ptvsd
```

[pypi page](https://pypi.org/project/ptvsd/)

[Visual Studio Code documentation for remote debugging](https://code.visualstudio.com/docs/python/debugging#_remote-debugging)

Steps:

-   Add following code at the beginning of your script


```python
import ptvsd
print("Waiting for debugger attach")
# 5678 is the default attach port in the VS Code debug configurations
ptvsd.enable_attach(address=('localhost', 5678), redirect_output=True)
ptvsd.wait_for_attach()
```

-   Add a debug configuration in Visual Studio Code **Debug → Add Configurations…**. It should looks like this :




        "configurations": [
            {
                "name": "Python: Attacher",
                "type": "python",
                "request": "attach",
                "port": 5678,
                "host": "localhost",
                "pathMappings": [
                    {
                        "localRoot": "${workspaceFolder}",
                        "remoteRoot": "."
                    }
                ]
            },

-   In VS Code add a breakpoint anywhere you want.
-   Launch the script in FreeCAD. FreeCAD freeze waiting for attachment.
-   In VS Code start debugging using created configuration. You should see variables in debugger area.
-   When setting breakpoints, VS Code will complain about not finding the .py file opened in the VS Code editor.
    -   Change \"remoteRoot\": \".\" to \"remoteRoot\": \"\"
    -   For example, if the Python file resides in */home/FC\_myscripts/myscript.py*
    -   Change to: \"remoteRoot\": \"/home/FC\_myscripts\"
-   If your macro can\'t find ptvsd despite having installed it somewhere precede \'import ptvsd\' with


```python
from sys import path
sys.path.append('/path/to/site-packages')
```

where the path is to the directory where ptvsd got installed

-   On the left bottom edge of VSCode you can choose the Python executable - it\'s best to make this the version packaged with FreeCAD.

In the Mac package it is /Applications/FreeCAD.App/Contents/Resources/bin/python

You can locate it on your system by typing 
```python
import sys
print(sys.executable)
``` into FreeCAD\'s Python console.


</div>


</div>

## Debugging OpenCasCade 

For developers needing to dig deeper in to the OpenCasCade kernel, user \@abdullah has created a [thread](https://forum.freecadweb.org/viewtopic.php?f=10&t=47017) orientation discussing how to do so.


<div class="mw-translate-fuzzy">





</div>


{{Powerdocnavi

}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)
