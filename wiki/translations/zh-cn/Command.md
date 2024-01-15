# Command/zh-cn
## Introduction





<div class="mw-translate-fuzzy">

一条FreeCAD命令是指：当您按下一个工具栏按钮或输入一个键盘快捷键时所执行的命令。它可能是一个非常简单的动作，如改变3D视图的缩放级别，或旋转视角；也可能是一个打开对话框并等待用户执行特定任务的复杂系统。


</div>


<div class="mw-translate-fuzzy">

每个FreeCAD命令都有自己独一无二的名称，可参见[:Category:Command_Reference](:Category_Command_Reference.md)页面。加载命令的方式很多，如通过工具栏按钮、菜单项，也可以在python脚本或python控制台中执行：


</div>


```python
FreeCADGui.runCommand("my_Command_Name")
```

## Background


<div class="mw-translate-fuzzy">

每个工作台中都定义了多种FreeCAD命令。工作台通常在FreeCAD初始化时添加各自的命令定义，因此FreeCAD一旦开启其命令就存在并可用了，无论对应的工作台是否已被激活。然而在某些情况下，工作台的作者可能会决定并不在FreeCAD开启过程中加载过多内容，而是仅在工作台初始化期间才加载命令定义。此时，只有在工作台被激活后才能使用对应的命令（也就是说，您至少要用工作台选择器来切换至对应工作台一次）。


</div>


<div class="mw-translate-fuzzy">

大多命令都需要与用户进行交互，FreeCAD命令仅存在于GUI模式下，而不存在于控制台模式下。但是，为了方便，大多FreeCAD命令也都有与之对应的python函数(如Part.makeBox 或 Draft.makeLine)，或者执行非常便于从python脚本中复制的代码。


</div>

可以通过C++或Python来定义命令。

## Commands defined in C++ 


<div class="mw-translate-fuzzy">

以下为一个C++的命令定义示例（通常定义于/Mod/ModuleName/Gui/Command.cpp文件中）：


</div>


{{Code|lang=cpp|code=
DEF_STD_CMD_A(StdCmdMyCommand);

StdCmdMyCommand::StdCmdMyCommand()
  : Command("Std_My_Command")
{
    sGroup        = QT_TR_NOOP("File");
    sMenuText     = QT_TR_NOOP("My Command");
    sToolTipText  = QT_TR_NOOP("Runs my command in the active document");
    sWhatsThis    = "Std_MyCommand";
    sStatusTip    = QT_TR_NOOP("Runs my command in the active document");
    sPixmap       = "MyCommand.svg";
    sAccel        = "Ctrl+A";
}

void StdCmdExport::activated(int iMsg)
{
    // place here the code to be executed when the command is ran
}

bool StdCmdMyCommand::isActive(void)
{
    // here you have a chance to return true or false depending if your command must be shown as active or inactive (greyed).
}

// the command must be "registered" in FreeCAD's command system
CommandManager &rcCmdMgr = Application::Instance->commandManager();
rcCmdMgr.addCommand(new StdCmdMyCommand());
}}

## Commands defined in Python 


<div class="mw-translate-fuzzy">

以及用python实现相似的命令（并没有具体规定python文件一定放于何处，只要令每个python工作台都能如预期那样工作即可......）


</div>


```python
from PySide.QtCore import QT_TRANSLATE_NOOP


class MyCommand:
    """Explanation of the command."""

    def __init__(self):
        """Initialize variables for the command that must exist at all times."""
        pass

    def GetResources(self):
        """Return a dictionary with data that will be used by the button or menu item."""
        return {'Pixmap': 'MyCommand.svg',
                'Accel': "Ctrl+A",
                'MenuText': QT_TRANSLATE_NOOP("My_Command", "My Command"),
                'ToolTip': QT_TRANSLATE_NOOP("My_Command", "Runs my command in the active document")}

    def Activated(self):
        """Run the following code when the command is activated (button press)."""
        print("Activated")

    def IsActive(self):
        """Return True when the command should be active or False when it should be disabled (greyed)."""
        return True

# The command must be "registered" with a unique name by calling its class.
FreeCADGui.addCommand('My_Command', MyCommand())
```

## Examples

See [Line drawing function](Line_drawing_function.md).



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > [Glossary](Category_Glossary.md) > Command/zh-cn
