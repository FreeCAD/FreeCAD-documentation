# Command/tr
## Introduction





<div class="mw-translate-fuzzy">

Bir FreeCAD komutu, bir araç çubuğu düğmesine bastığınızda veya bir klavye kısayolu yazdığınızda yürütülen şeydir. 3D görünümün yakınlaştırma düzeyini değiştirmek veya bakış açısını döndürmek gibi çok basit bir işlem olabileceği gibi iletişim kutularını açıp kullanıcının belirli görevleri gerçekleştirmesini bekleyecek karmaşık bir sistem olabilir.


</div>


<div class="mw-translate-fuzzy">

Her FreeCAD komutunun [Komut Referansı](:Category:Command_Reference/tr.md) sayfasında görünen benzersiz bir adı vardır. Komutlar aşağıdakileri çalıştırarak, bir araç çubuğu düğmesi, bir menü öğesi veya bir python betiğinden veya python konsolundan başlatılabilir:


</div>


```python
FreeCADGui.runCommand("my_Command_Name")
```

## Background


<div class="mw-translate-fuzzy">

Tezgah başına FreeCAD komutları tanımlanmıştır. Tezgahlar normalde FreeCAD açılış anında komut tanımlarını ekleyecektir, bu yüzden komut hazır olur ve ilgili tezgahın etkinleştirilip etkinleştirilmediğine bakılmaksızın FreeCAD başlatıldığı anda kullanılabilir. Bununla birlikte, bazı durumlarda tezgah kodlayıcısı, FreeCAD başlatma işlemini çok fazla yüklememeye, komut tanımlarını sadece tezgah girişinde yüklemeye karar vermiş olabilir. Bu gibi durumlarda, komut yalnızca tezgah etkinleştirildikten sonra kullanılabilir (tezgah seçicisiyle en az bir kere ona geçtiniz.)


</div>


<div class="mw-translate-fuzzy">

FreeCAD komutlarının birçoğu kullanıcı etkileşimi gerektirdiğinden, sadece GUI modunda kullanılabilir, konsol modunda kullanılamaz. Bununla birlikte, kolaylık olması açısından, FreeCAD komutlarının çoğu ya karşılık gelen bir python işlevine (Part.makeBox veya Draft.makeLine gibi) sahip olacak veya bir python komut dosyasında çoğaltılması çok kolay olan bir kod yürütecektir.


</div>

Komutlar, C ++ veya Python\'da tanımlanabilir.

## Commands defined in C++ 


<div class="mw-translate-fuzzy">

C ++ komut tanımı örneği (genellikle /Mod/ModuleName/Gui/Command.cpp içinde tanımlanır):


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

ve python\'da benzer bir komut (yapılması gereken yer için kural yoktur, her python tezgahı uygun gördüğü şekilde yapar \...)


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
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > [Glossary](Category_Glossary.md) > Command/tr
