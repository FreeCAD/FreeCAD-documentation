# Introduction to Python/zh-cn
{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

本简短教程可供Python新手参阅。[Python](http://en.wikipedia.org/wiki/Python_%28programming_language%29)是一种开源、支持多平台的 [编程语言](http://en.wikipedia.org/wiki/Programming_language)。Python有几种不同于其他常见语言的特性，使之与众不同，而且还易于对此毫无经验的人使用：


</div>


<div class="mw-translate-fuzzy">

-   Python被设计为一种易于常人阅读的语言，因此方便学习且代码容易理解。
-   Python是一种解释型语言，也就是它并非C那样的编译型语言，在程序运行前无需进行编译。您所编写的代码将如您所愿即刻逐行执行。由于代码可放慢脚步逐行执行，因此更便于学习与查找代码中错误。
-   可将Python嵌入其他程序用作脚本语言。FreeCAD中配有一个内嵌的Python解释器；您可以在FreeCAD中编写Python代码来控制FreeCAD的各种组件，比如用来创建一个几何图形等等。这是一种极其强大的工具，程序员可通过它编写代码，以此取代仅能点击标有\"创建球体\"按钮的机械式操作；您可以借此自由方便地构建自己的工具，创建精准的几何图形，但程序员可能无法预览待创建的图形。
-   Python具有可扩展性，您可以轻松地为它接入新的模块来拓展其功能。例如，您可以借助特定模块使Python可以读写jpg图片、与twitter进行交互，甚至调度任务在操作系统上的执行，等等。


</div>


<div class="mw-translate-fuzzy">

我们墙裂鼓励您亲自将代码输入至Python解释器。经过我们的激烈讨论，认为重点在于令代码跑起来，并显示出结果。不运行代码根本不会理解Python。因此，快动手吧！以下是相关简介，而并非完整的教程。但是我们希望这能为您深入理解FreeCAD中的内部机制而提供相关的基础知识。


</div>

## 解释器


<div class="mw-translate-fuzzy">

用户在写程序时通常会打开文本编辑器或特定的编程环境(一般是配有其他辅助工具的文本编辑器)，借此编写代码、编译并执行。当代码中存在一个或多个错误时，程序往往就跑不起来了。这时，您可以根据报错信息定位错误的根源。再返回编辑器，纠正错误，再次运行，如此往复直到程序可按预期执行为止。


</div>


<div class="mw-translate-fuzzy">

在整个处理流程中，Python解释器的内部工作原理对用户而言都是透明的。所谓的解释器是一种附有命令提示符的Python窗口，在此，您可以方便地输入Python代码。如果您在自己的计算机上安装了Python(如果系统为Windows或Mac，从[Python website](http://www.python.org)下载；如果系统是GNU/Linux，则借助软件包资料库（package repository）进行安装), 您可从开始菜单中开启Python解释器。但是，FreeCAD中的下方窗口中也集成了Python解释器：


</div>

![](images/FreeCAD_Python_console.png ) *The FreeCAD Python console*


<div class="mw-translate-fuzzy">

(如果没有找到，请依次点选View \--\> Panels \--\> Python console。)


</div>


<div class="mw-translate-fuzzy">

解释器中显示着Python的版本，a \>\>\>即为命令提示符，您可以在此输入Python代码。在解释器中编写代码很简单：一行对应一个指令。在按下回车键时，将执行本行代码(此前将自动在背后进行代码编译)。例如，请尝试编写下列代码：


</div>


```python
print("hello")
```


<div class="mw-translate-fuzzy">

print是一种特殊的Python关键字，顾名思义，它负责在屏幕上打印内容。当您按下回车键时，将处理所输入的代码，最后打印\"hello\"这条消息。如果您得到了一个错误信息，例如，让我们来这样写：


</div>


```python
print(hello)
```


<div class="mw-translate-fuzzy">

Python将告知我们，它不知道hello是神马。利用\"符号可方便地指定字符串内的多个字符，用编程术语来讲，即一段文本。若不使用\"符号，则print命令将认为hello并非一段文本，而是一个特殊的Python关键字。而重点在于，您会立即得到一个因此而产生的错误消息。通过按"up"键(或者在FreeCAD解释器中按CTRL+up)，您将返回上一条编写的命令，并对此进行修正。


</div>


<div class="mw-translate-fuzzy">

Python解释器中还设有一个内建的帮助系统。尝试输入：


</div>


```python
help("print")
```


<div class="mw-translate-fuzzy">

您将得到一条既长又完整的print命令功能的描述。


</div>


<div class="mw-translate-fuzzy">

现在让我们来全面了解一下Python解释器，先从最关键的部分入手吧！


</div>

[top](#top.md)

## 变量


<div class="mw-translate-fuzzy">

实话实说，打印\"hello\"字符串没什么意思。更有趣的是打印我们没有提前得知的内容，或令Python来为我们求出所需的内容。这便是引入变量这一概念的原因。简而言之，变量即为：存有特定值的名称。例如，输入下列内容：


</div>


```python
a = "hello"
print(a)
```


<div class="mw-translate-fuzzy">

我猜您已经知道这段代码的背后究竟发生了什么，我们将\"hello\"存在了\"a\"名下。现在，\"a\"在Python环境中已经不再是一个未知的名称了！我们可以在各处运用它，例如，将其用于上述打印命令中。我们几乎可以使用能想到的任意名称，仅需遵循一些简单的规则即可，比如名称中不能夹带空格与特定的标点符号。例如，我们可以这样写：


</div>


```python
hello = "my own version of hello"
print(hello)
```


<div class="mw-translate-fuzzy">

看到了吗？现在的hello是一个有定义的单词。但是，当我们无意中选取了Python中已经存在的名称作为变量名时会发生什么呢？这里，我们选取\"print\"作为变量名来保存字符串：


</div>


```python
myVariable = "hello"
print(myVariable)
myVariable = "good bye"
print(myVariable)
```


<div class="mw-translate-fuzzy">

我们可以改变myVariable的值。也可以复制变量：


</div>


```python
var1 = "hello"
var2 = var1
print(var2)
```


<div class="mw-translate-fuzzy">

请注意，关键的是要给变量起个有意义的名称。这是因为，经过一段时间后您可以会忘记变量\"a\"表示的是什么。例如，将某个变量命名myWelcomeMessage后，您可以轻松回忆起设立此变量的目的。这样便可以使您的代码直观地表达出自身的意义。


</div>


<div class="mw-translate-fuzzy">

字母的大小写也非常重要。myVariable与myvariable是两个截然不同的变量，区别就在于其中字母**v**的大小写上。如果您输入*print myvariable*，系统就会返回一个"未定义"错误。


</div>

[top](#top.md)

## 数字


<div class="mw-translate-fuzzy">

当然，您一定知道编程的过程中要处理各种数据，不仅仅是前面提到的字符串，还有数字等等。有一点十分重要，Python必须知道它要处理的数据类型。在我们此前示范的打印hello的示例中，print命令知道我们提供的\"hello\"是个字符串。这是因为我们利用了引号\"通知了print命令，它接下来要处理的是个文本字符串。


</div>


<div class="mw-translate-fuzzy">

我们可以通过Python中的关键字type来检测一个变量的数据类型：


</div>


```python
myVar = "hello"
type(myVar)
```


<div class="mw-translate-fuzzy">

在这里，它将告诉我们，变量myVar中的内容是一个\'str\'，也就是Python术语中字符串的简写。我们也可以使用Python提供的其他类型数据，如整数与浮点数：


</div>


```python
firstNumber = 10
secondNumber = 20
print(firstNumber + secondNumber)
type(firstNumber)
```


<div class="mw-translate-fuzzy">

这就更有趣了，不是吗？这就是说，我们现在拥有了一个强大的计算器了！来看看她是怎么跑起来的。Python知道10与20窦唯整数。所以他们在内部被存为\"int\"，这样Python就可以把它们看作是整数并加以处理。再来看看下面的计算结果：


</div>


```python
firstNumber = "10"
secondNumber = "20"
print(firstNumber + secondNumber)
```


<div class="mw-translate-fuzzy">

看到了吗？在此，我们强制Python把这两个变量看作是文本而非数字。Python可以把两条文本合二为一，但是却不会计算两者之和。只不过我们现在要讨论的其实是整数。Python还支持浮点数。整数与浮点数的区别在于前者没有小数部分，而浮点数却有：


</div>


```python
var1 = 13
var2 = 15.65
print("var1 is of type ", type(var1))
print("var2 is of type ", type(var2))
```


<div class="mw-translate-fuzzy">

可以肆无忌惮地进行整数与浮点数的混合运算：


</div>


```python
total = var1 + var2
print(total)
print(type(total))
```


<div class="mw-translate-fuzzy">

当然，最后的计算结果依旧存在小数部分，细不细？在此，Python会自动将结果记作一个浮点数。包括上述情况在内的若干情景中，Python会自动推测到底使用哪种类型。但在另外一些场景中却不是这样，例如：


</div>


```python
varA = "hello 123"
varB = 456
print(varA + varB)
```


<div class="mw-translate-fuzzy">

执行上述命令后，我们将得到一个错误信息。varA是一个字符串，而varB则是一个整数，Python不知道该如何处理了。但是，我们可以强制Python将数据的类型互相转化：


</div>


```python
varA = "hello"
varB = 123
print(varA + str(varB))
```


<div class="mw-translate-fuzzy">

两个变量现在都是字符串，可以顺利执行后续操作了！请注意，变量varB的"字符串化"仅发生在打印过程中，但是其自身并没有发生任何改变。如果希望将varB永久转换为字符串，我们需要这样做：


</div>


```python
varB = str(varB)
```


<div class="mw-translate-fuzzy">

我们也可以通过int()与float()将数据转换为整数与浮点数类型：


</div>


```python
varA = "123"
print(int(varA))
print(float(varA))
```


<div class="mw-translate-fuzzy">

您一定注意到了，我们在本部分中用打印命令显示了几种不同的数据。我们以逗号作为分隔符打印了变量、所求之和以及其他内容，甚至还打印了像type()这样的命令所返回的结果。您可能会发现，若执行下列两种命令：


</div>


```python
type(varA)
print(type(varA))
```


<div class="mw-translate-fuzzy">

将得到同样的结果。这是因为我们的执行环境处于解释器中，每个结果都会被自动打印出来。而当我们编写了更为复杂的程序，却在解释器外执行时，便不会自动打印任何内容了，这就要靠自己加入print命令。自此，为了让进度加快，我们就不再使用print命令了。这样，就可以将代码简单地写作：


</div>


```python
myVar = "hello friends"
myVar
```

[top](#top.md)

## 列表


<div class="mw-translate-fuzzy">

另一种有趣的数据类型为列表（list），它是一种简单的其他类型的数据集合。与定义字符串使用\" \"相仿，我们用\[ \]来定义列表：


</div>


```python
myList = [1, 2, 3]
type(myList)
myOtherList = ["Bart", "Frank", "Bob"]
myMixedList = ["hello", 345, 34.567]
```


<div class="mw-translate-fuzzy">

不难看出，列表可容纳其他类型的数据。列表的用处体现在可以把多个变量"打包"在一起。您可以对列表里面的东东执行任意类型的操作，比如统计其中元素的数量：


</div>


```python
len(myOtherList)
```


<div class="mw-translate-fuzzy">

或者取出列表中的任意一项：


</div>


```python
myName = myOtherList[0]
myFriendsName = myOtherList[1]
```


<div class="mw-translate-fuzzy">

可以看到，len()命令返回的是列表中元素的总数，且它们在列表中的"位置"是以0开始计算的。列表中第一项的位置总为0，因此，在myOtherList列表中，\"Bob\"位居第2。我们可以对列表进行更多的操作，例如对元素进行排序、增减其中的元素，这可以参考[这里（已废？）](http://www.diveintopython.net/native_data_types/lists.html)。


</div>


<div class="mw-translate-fuzzy">

其实这里有个有趣的事情：文本字符串与字符构成的列表极其相似！试着这样做一下：


</div>


```python
myvar = "hello"
len(myvar)
myvar[2]
```


<div class="mw-translate-fuzzy">

一般而言，您对字符串所执行的操作也同样可以应用于列表上。事实上，列表与字符串都是顺序结构。


</div>


<div class="mw-translate-fuzzy">

除了字符串、整数、浮点数与列表之外，Python中还有更多其他的内建数据类型，例如[dictionaries](http://www.diveintopython.net/native_data_types/index.html#d0e5174)，或者，您甚至可以通过[类](http://www.freenetpages.co.uk/hp/alan.gauld/tutclass.htm)创建自己的数据类型。


</div>

[top](#top.md)

## 缩进


<div class="mw-translate-fuzzy">

列表的一种极其酷炫用法是遍历每一项，并对其依次进行处理。例如，来看下面这个示例：


</div>


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
for dalton in alldaltons:
    print(dalton + " Dalton")
```


<div class="mw-translate-fuzzy">

我们利用\"for \... in \...\"命令迭代（iterate，编程术语）列表中的每一项，并针对每项执行特定操作。注意到这特殊的语法：**for**命令以**:**作为结尾，表示下面为单个或多个命令所构成的执行块。 在解释器中，在输入以:结尾的命令行后，命令提示符将变为\...这意味着Python知道(:)行后必有更多的输入内容。


</div>


<div class="mw-translate-fuzzy">

那末，Python是如何知道for\...in语句中还有多少行命令要执行呢？这是因为Python采用了缩进策略。即，在for\...in语句后，您是不会直接输入下一行内容的。而是要以一个(多个)空格符，或一个（多个）tab符作为开头。其他编程语言则采用其他方式，如将所有内容都置于括号内等等。 只要您按上述**同样的**缩进编写后续代码，Python就会认为它们都是for-in块的组成部分。如果代码块中第一行以2个空格作为缩进，而下一行以4个空格作为缩进，便会产生一个错误。 如果代码块中的内容编写结束，只需令下一行无缩进，或简单地按下回车键退出for-in块即可。


</div>


<div class="mw-translate-fuzzy">

缩进策略这么吊炸天，究其原因是为了程序的可读性。如果用了较大的索引(比如用tab取代空格，因为tab比空格占用空间更大), 在编写规模很大的程序时，其逻辑看起来就会清晰不少。我们随后会看到，for-in以外的不少命令也可以附有缩进代码块。


</div>


<div class="mw-translate-fuzzy">

for-in命令可用于将某些操作执行多次的情况。例如，它可以搭配range()命令使用：


</div>


```python
serie = range(1, 11)
total = 0
print("sum")
for number in serie:
    print(number)
    total = total + number
print("----")
print(total)
```


<div class="mw-translate-fuzzy">

（如果您通过复制、粘贴的方式在解释器中运行上述代码示例，会发现其中的文本块抛出了一个错误。在这种情况下，我们可以从头一直复制到缩进块的结尾，即*total = total + number*行的结尾，并将其粘贴至解释器中。这时在解释器中（连续）输入，直到解释器不再显示三个点的符号，并执行上述代码。接着再将最后两行代码复制到解释器中以上换行符后。现在，解释器应该能显示出程序的输出结果。）


</div>


<div class="mw-translate-fuzzy">

如果您在解释器宏输入**help(range)**，将会看到： 
```python
range(...)
    range(stop) -> list of integers
    range(start, stop[, step]) -> list of integers
``` 方括号表示可选参数。不难看出，range()的所有参数都为整数。在以下示例中，我们将通过int()把所有range()的参数都强制转换为整数。


</div>


```python
range(...)
    range(stop) -> list of integers
    range(start, stop[, step]) -> list of integers
```

Here the square brackets denote an optional parameter. However all are expected to be integers. Below we will force the step parameter to be an integer using `int()`:


```python
number = 1000
for i in range(0, 180 * number, int(0.5 * number)):
    print(float(i) / number)
```


<div class="mw-translate-fuzzy">

或用range()实现更为复杂的逻辑：


</div>


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
for n in range(4):
    print(alldaltons[n], " is Dalton number ", n)
```


<div class="mw-translate-fuzzy">

可以发现，range()命令也有一些奇怪的特殊性，即它以0开始计数（在没有指定起始编号的情况下），且最后的编号要比您所指定的值小1。当然，这样也可以令它与其他Python命令配合得很顺利。例如：


</div>


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
total = len(alldaltons)
for n in range(total):
    print(alldaltons[n])
```


<div class="mw-translate-fuzzy">

缩进搭配if命令也是另一种有趣的用法。如果满足了特定条件，则执行对应的if代码块，例如：


</div>


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
if "Joe" in alldaltons:
    print("We found that Dalton!!!")
```


<div class="mw-translate-fuzzy">

当然啦，根据上述条件则一定会打印第一条语句，但是现在来以下列代码加以取代：


</div>


```python
if "Lucky" in alldaltons:
```


<div class="mw-translate-fuzzy">

这样就不会打印任何内容了。我们也可以使用一个else:语句（字符串有问题？(Dalton-\>Lucky?)）：


</div>


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
if "Lucky" in alldaltons:
    print("We found that Dalton!!!")
else:
    print("Such Dalton doesn't exist!")
```

[top](#top.md)

## 函数


<div class="mw-translate-fuzzy">

这里列出了 [Python的标准命令](http://docs.python.org/reference/lexical_analysis.html#identifiers)。在Python的最新版本中，大约存在30条命令，我们刚刚尝试了其中的一部分。但是，您是否曾想过"发明"自己的命令？答案是：是的，我们可以，而且还相当简单。事实上，向Python添加其他的模块做的就是这件事：这些模块向Python增添了可供您使用的命令。自定义命令在Python中被称为函数，实现方法如下：


</div>


```python
def printsqm(myValue):
    print(str(myValue) + " square meters")

printsqm(45)
```


<div class="mw-translate-fuzzy">

看吧，很简单：利用def()命令即可定义一个新的函数。您可以为它起名，在括号里定义其参数，在函数中处理这些参数。参数即将传入函数中的数据。例如，现在来考察len()命令。如果仅写len()，则Python将提示您需要为之提供一个参数。即，您需要用len()来做些什么，对吧？比如说，您可以用len(myList)来获取myList的长度。此时，myList便是您传入len()函数的参数。len()函数的定义便是如此，使之知道如何处理传入的参数。而我们刚刚做的也正是如此。


</div>


<div class="mw-translate-fuzzy">

\"myValue\"可以为任意有效名称，仅用于定义它的目标函数之中。它只是您为参数起的名字，同时还负责告知函数所需的参数数量。例如，您可以试着这样写：


</div>


```python
printsqm(45, 34)
```


<div class="mw-translate-fuzzy">

这将导致一个错误。原因是此函数实际仅接收一个参数，但是却为它输入了两个参数：45与34。我们可以编写下列函数：


</div>


```python
def sum(val1, val2):
    total = val1 + val2
    return total

myTotal = sum(45, 34)
```


<div class="mw-translate-fuzzy">

在这段代码中，我们令函数接收两个参数，求其和，并返回其值。函数返回的数据很有用，因为我们可以继续对其结果进行处理，例如，这里将函数返回的结果存于myTotal变量之中。当然，由于我们身处解释器之中，所有内容都可打印出来，于是就可以这样做：


</div>

[top](#top.md)

## 模块


<div class="mw-translate-fuzzy">

现在我们已对Python的工作方式的些许认识，这里来讨论最后一样东西：如何运用文件及模块。


</div>


<div class="mw-translate-fuzzy">

到目前为止，我们一直在解释器中逐行地编写Python指令。我们是否可以将多行代码集合在一起，并一次性执行完毕呢？这可是编写更复杂逻辑的基础啊。而且，我们还可以借此保存自己的工作进度。是的，方法当然有，而且还相当简单。只需打开文本编辑器(如windows的记事本，Linux下的gedit、emacs或vi)，并像在解释器里那样，在其中借助缩进等编写Python代码。再将数据存作以.py为拓展名的文件。这样，您就可以一次性编写完整的Python程序了。当然，还有比notepad更优秀的编辑器，它会以Python程序模式助你编写代码，而不仅仅是将其看作一个文本文件。


</div>


<div class="mw-translate-fuzzy">

有n种方式可以使Python执行上述程序。在windows中，只需对文件按下右键，以Python打开，再执行即可。此外，您可以用Python解释器来执行代码文件。对此，解释器可以识别出.py程序。在FreeCAD中，最简单的方式是将文件放置在FreeCAD中Python解释器可识别的默认位置处，例如FreeCAD的bin文件夹，或任意Mod文件夹下。(在Linux中，所用的文件夹可能为/home//.FreeCAD/Mod，我们可在此添加一个名为scripts的子文件来存放代码文本文件。) 假设我们在文件中写入下列代码：


</div>


```python
def sum(a,b):
    return a + b

print("myTest.py succesfully loaded")
```


<div class="mw-translate-fuzzy">

并将其保存为FreeCAD/bin（或Linux中/home//.FreeCAD/Mod/scripts）下的myTest.py文件。此时，我们开启FreeCAD，并在解释器窗口中输入：


</div>


```python
import myTest
```


<div class="mw-translate-fuzzy">

请注意，并无.py扩展名。这将像在解释器中所做的那样，逐行执行文件中的代码。执行过程中将创建sum函数，并打印代码中的对应信息。 这里有一个较大的不同点：import命令不仅执行文件中的程序，还会加载其中的函数，因此就可以在解释器中使用这些函数。而包含函数的文件则被称作模块。


</div>


<div class="mw-translate-fuzzy">

如果在解释器中编写sum()函数，可以这样方便地执行：


</div>


```python
sum(14, 45)
```


<div class="mw-translate-fuzzy">

这就是我们此前的做法。当我们导入包含sum()函数的模块时，语法则稍有不同：


</div>


```python
myTest.sum(14, 45)
```


<div class="mw-translate-fuzzy">

即，可将导入的模块看作是个"容器"，其中所存均为其函数。这个设计极其有用，因为我们可以导入大量模块，并令所有的代码都有一定的组织结构。因此，基本上来讲，到处您都可看到 **something.somethingElse**的形式，以点作为隔断，表示**somethingElse**位于**something**中。


</div>


<div class="mw-translate-fuzzy">

我们可以在主解释器空间中导入自己编写的sum()函数，就像这样：


</div>


```python
from myTest import *
sum(12, 54)
```


<div class="mw-translate-fuzzy">

基本上，所有模块的形式都是如此。导入一个模块，使用其中的函数：module.function(argument)。大多数的模块是这样编写的：由于您可以在自己的模块中导入其他模块，因此可以在模块中定义您要在解释器或自己的Python模块中使用的函数、新数据类型与类。


</div>


<div class="mw-translate-fuzzy">

这里要提及最后一样极有用的东东。我们如何得知有哪些模块可用？模块里有哪些函数？而这些函数如何使用（即，这些函数使用哪些参数）？我们此前曾使用过Python的help()函数。现在输入：


</div>


```python
help("modules")
```


<div class="mw-translate-fuzzy">

这将为我们列举出所有可用的模块。随后，我们可以按q来退出当前的交互帮助系统，并按需导入这些模块。甚至可以用dir()命令来浏览模块中的内容


</div>


```python
import math
dir(math)
```


<div class="mw-translate-fuzzy">

此时，我们将看到math模块中的所有函数，以及一些陌生的名字：\_\_doc\_\_, \_\_file\_\_, \_\_name\_\_。其中，\_\_doc\_\_用处很大，它是描述性的文档文本。（质量高的）模块中的每个函数都有对应的\_\_doc\_\_，用来解释它们的用法。例如，我们可以从math模块中看到有个sin函数。想知道怎样使用吗？


</div>


```python
print(math.sin.__doc__)
```


<div class="mw-translate-fuzzy">

（可能不太明显，但是doc左右两端各有两条下划线。）


</div>


<div class="mw-translate-fuzzy">

最后再来点儿饭后甜点吧：当使用一个新的模块或已存在的模块时，最好以py作为文件扩展名，例如：myModule.FCMacro =\> myModule.py。我们通常会希望测试这些模块，遂以上述方式来加载它。


</div>


```python
import importlib
importlib.reload(myTest)
```


<div class="mw-translate-fuzzy">

然而，这里还有两种方式来打开其他扩展名的模块：在宏中使用Python的exec或execfile函数。


</div>


```python
exec(open("C:/PathToMyMacro/myMacro.FCMacro").read())
```

[top](#top.md)

## 在FreeCAD中使用Python


<div class="mw-translate-fuzzy">

好的，我认为您现在已经了解了Python工作的基本原理，并可以开始查看FreeCAD为您提供了哪些相应设施。FreeCAD的Python函数都很妙地组织在不同的模块中。其中的一部分已经在FreeCAD开启时得到加载（导入）。因此，只需执行


</div>


```python
dir()
```

[top](#top.md)

## Notes

-   FreeCAD was originally designed to work with Python 2. Since Python 2 reached the end of its life in 2020, future development of FreeCAD will be done exclusively with Python 3, and backwards compatibility will not be supported.
-   Much more information about Python can be found in the [official Python tutorial](https://docs.python.org/3/tutorial/index.html) and the [official Python reference](https://docs.python.org/3/reference/).

[top](#top.md)


{{Powerdocnavi

}} 

_ _

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Introduction to Python/zh-cn
