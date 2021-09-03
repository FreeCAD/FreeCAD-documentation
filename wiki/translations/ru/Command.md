

## Вступление


{{TOCright}}

Под [Командой](Command/ru.md) подразумевается выполнение некоторых действий (кода), в следствии нажатия какой-либо кнопку на панели инструментов или при наборе определённых комбинаций клавиш на клавиатуре. Это может быть как очень простое действие, как например изменение уровня масштабирования [трёхмерного вида](3D_view/ru.md) или поворот точки обзора, так и комплексное решение которое запустит диалоговые окна и будет ожидать, когда пользователь выполнит определенные действия.


<div class="mw-translate-fuzzy">

Каждая команда FreeCAD имеет уникальное имя, которое внесено в список [:Category:Command\_Reference/ru](:Category:Command_Reference/ru.md). Команды могут запускаться с помощью кнопки на панели инструментов или из списка меню, а так же из [python](python/ru.md) скрипта или [консоли Python](Python_console/ru.md), по средством выполнения следующей комманды:


</div>


```python
FreeCADGui.runCommand("my_Command_Name")
```

## Основы

Команды FreeCAD определяются отдельно для каждого верстака. Верстаки обычно добавляют свои определения команд во время запуска FreeCAD, поэтому команда существует и доступна сразу после запуска FreeCAD, независимо от того, был ли активирован соответствующий верстак или нет. Однако в некоторых случаях автор рабочей среды, возможно, решил не перегружать/нагружать процесс запуска FreeCAD и поэтому загрузил определения команд только при запуске рабочей среды. В этих случаях команда будет доступна только после активации рабочего стола (если вы переключились на него по крайней мере один раз с помощью переключателя верстака).

Поскольку большинство из них требуют взаимодействия с пользователем, команды FreeCAD доступны только в режиме графического интерфейса, а не в режиме консоли. Однако для удобства большинство команд FreeCAD либо будут иметь соответствующую функцию python (например, `Part.makeBox` или `Draft.makeLine`), либо будут выполнять код, который очень легко воспроизвести в скрипте python и/или [макросе](macros/ru.md).

Команды могут быть назначены как на языке C++, так и посредством Python.

## Назначение команд в C++ {#назначение_команд_в_c}

Пример назначения команды на языке C++, назначение производится по следующей структре {{FileName|Mod/ModuleName/Gui/Command.cpp}}.


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

## Назначение команд в Python {#назначение_команд_в_python}

Пример назначения команды на языке Python. Данный код может быть размещен в папке по адрессу вроде этого: {{FileName|Mod/ModuleName/tools/commands.py}}. 
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

    def isActive(self):
        """Return True when the command should be active or False when it should be disabled (greyed)."""
        return True

# The command must be "registered" with a unique name by calling its class.
FreeCADGui.addCommand('My_Command', MyCommand())
```

## Примеры

Смотрите [функцию рисования линии](Line_drawing_function/ru.md).


{{Powerdocnavi

}}

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Python Code{{\#translation:}}](Category:Python_Code.md) [Category:Glossary{{\#translation:}}](Category:Glossary.md)
