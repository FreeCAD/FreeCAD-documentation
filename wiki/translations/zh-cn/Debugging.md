# Debugging/zh-cn
{{TOCright}}


<div class="mw-translate-fuzzy">

## 测试第一

在你经历痛苦的调试过程之前请使用 [测试框架](Testing.md) 来检查标准测试是否正常工作。如果它们未运行完成, 则可能是安装中断。


</div>

Before you go through the pain of debugging use the [Test framework](Testing.md) to check if the standard tests work properly. If they do not run complete there is possibly a broken installation.


<div class="mw-translate-fuzzy">

## 命令行

FreeCAD 的 \"调试\" 是由一些内部机制支持的。FreeCAD 的命令行版本提供了一些用于调试支持的选项。


</div>

The *debugging* of FreeCAD is supported by a few internal mechanisms. The command line version of FreeCAD provides some options for debugging support.


<div class="mw-translate-fuzzy">

以下是 FreeCAD 0.15 中能识别的选项:


</div>


<div class="mw-translate-fuzzy">

一般性选项:

 -v [ --version ]      打印版本字符串
 -h [ --help ]         打印帮助信息
 -c [ --console ]      以控制台模式启动
 --response-file arg   也能使用 '@name' 指定


</div>


<div class="mw-translate-fuzzy">

配置:

 -l [ --write-log ]       输出 log 文件到:
                          $HOME/.FreeCAD/FreeCAD.log
 --log-file arg           不像 --write-log，这个命令允许记录到任意文件
 -u [ --user-cfg ] arg    用于加载/保存用户设置的用户配置文件
 -s [ --system-cfg ] arg  用于加载/保存系统设置的用户配置文件
 -t [ --run-test ] arg    测试等级
 -M [ --module-path ] arg 额外的模块路径
 -P [ --python-path ] arg 额外的python路径


</div>


<div class="mw-translate-fuzzy">

## 生成回溯

如果你运行 FreeCAD 开发中的出血边缘(bleeding edge)版本, 则可能会发生 \"崩溃 \"。 您可以通过向开发人员提供 \"回溯 \" 来帮助解决此类问题。 为此, 您需要运行软件的 \"调试版本 \"。 \"调试生成 \" 是在编译时设置的参数, 因此您需要自己编译 FreeCAD, 或者获取编译 \"调试 \" 版本。


</div>

If you are running a version of FreeCAD from the bleeding edge of the development curve, it may \"crash\". You can help solve such problems by providing the developers with a \"backtrace\". To do this, you need to be running a \"debug build\" of the software. \"Debug build\" is a parameter that is set at compile time, so you\'ll either need to compile FreeCAD yourself, or obtain a pre-compiled \"debug\" version.


<div class="mw-translate-fuzzy">

### 对于 Linux 


<div class="toccolours mw-collapsible mw-collapsed" style="width:800px;">

Linux 调试 \-\-\--\>


<div class="mw-collapsible-content">

必要条件:


</div>


<div class="toccolours mw-collapsible mw-collapsed" style="width:800px;">

Linux Debugging →


<div class="mw-collapsible-content">

Prerequisites:


<div class="mw-translate-fuzzy">

-   安装的 gdb 软件包
-   FreeCAD 的调试版本 (此时仅可通过 [从源代码构建](CompileOnUnix#For_a_Debug_build.md))
-   导致崩溃的 FreeCAD 模式


</div>

步骤: 在终端窗口中输入以下内容:

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


<div class="mw-translate-fuzzy">

FreeCAD 现在就要启动。执行导致 FreeCAD 崩溃或冻结的步骤, 然后在终端窗口中输入:

    (gdb) bt

这将生成一个冗长的列表, 确切地列出程序在崩溃或冻结时正在执行的工作。将此内容包括在问题报告中。


</div>


</div>


</div>


```python
(gdb) bt
```

This will generate a lengthy listing of exactly what the program was doing when it crashed or froze. Include this with your problem report.


```python
(gdb) bt full
```

Print the values of the local variables also. This can be combined with a number to limit the number of frames shown.


</div>


</div>


<div class="mw-translate-fuzzy">

### 对于 MacOSX 


<div class="toccolours mw-collapsible mw-collapsed" style="width:800px;">

MacOSX 调试 \-\-\--\>


<div class="mw-collapsible-content">

必要条件:


</div>


<div class="toccolours mw-collapsible mw-collapsed" style="width:800px;">

macOS Debugging →


<div class="mw-collapsible-content">

Prerequisites:

-   安装好的软件包 lldb
-   FreeCAD 的调试版本
-   一个导致崩溃的 FreeCAD 模式

步骤: 在终端窗口中输入以下内容:


```python
$ cd FreeCAD/bin
$ lldb FreeCAD
```

LLDB will output some initializing information. The (lldb) shows the debugger is running in the terminal, now input:


```python
(lldb) run
```


<div class="mw-translate-fuzzy">

FreeCAD 现在就要启动。执行导致 FreeCAD 崩溃或冻结的步骤, 然后在终端窗口中输入:

    (lldb) bt

这将生成一个冗长的列表, 确切地列出程序在崩溃或冻结时正在执行的工作。将此内容包括在问题报告中。


</div>


</div>


</div>


```python
(lldb) bt
```

This will generate a lengthy listing of exactly what the program was doing when it crashed or froze. Include this with your problem report.


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

## Python 调试 

这里是一个在 FreeCAD 中使用 winpdb 的例子:


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

We need the Python debugger: *Winpdb*. If you do not have it installed, on Ubuntu/Debian install it with:


```python
sudo apt-get install winpdb
```

Now lets setup the debugger.

1.  Start *Winpdb*.
2.  Set the debugger password to \"test\": Go to menu *File* → \'\'Password\" and set the password.

Now we will run a test Python script in FreeCAD step by step.

1.  运行 winpdb 并且设置密码 (例如：测试)
2.  使用以下内容创建一个 Python 文件


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


<div class="mw-translate-fuzzy">

1.  开始 FreeCAD 并将上述文件加载到 FreeCAD
2.  按 F6 执行
3.  现在 FreeCAD 将变得没有响应, 因为 Python 调试器正在等待
4.  切换到 Windpdb GUI, 然后单击 \"附加 \"。几秒钟后, 将出现一个项目 \" \", 您必须双击
5.  现在, 当前执行的脚本出现在 Winpdb 中。
6.  在最后一行设置断点并按 F5
7.  现在按 F7 键跟踪 Python 代码 Draft.makeWire


</div>


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

---
[documentation index](../README.md) > [Developer Documentation](Category:Developer Documentation.md) > Debugging/zh-cn
