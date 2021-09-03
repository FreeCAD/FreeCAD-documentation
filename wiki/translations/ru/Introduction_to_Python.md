


{{TOCright}}

## Введение

Это небольшой учебник, созданный для новичков в [Python](http://ru.wikipedia.org/wiki/Python). Python - это язык с открытым исходным кодом, многоплатформенный [язык програмирования](http://ru.wikipedia.org/wiki/%D0%92%D1%8B%D1%81%D0%BE%D0%BA%D0%BE%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D0%B5%D0%B2%D1%8B%D0%B9_%D1%8F%D0%B7%D1%8B%D0%BA_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F). Он имеет некоторые функции, которые отличают его от других языков программирования и легко доступны для новых пользователей:

-   Он был разработан специально для легкого чтения людьми, и поэтому его очень легко узнать и понять.
-   Он интерпретируется, то есть ваша программа не нуждается в компиляции до ее выполнения. Код Python может быть немедленно выполнен, даже строчка за строчкой, если хотите.
-   Он может быть встроен в другие программы, которые будут использоваться в качестве языка сценариев. FreeCAD имеет встроенный интерпретатор Python. Вы можете написать код Python для манипулирования частями FreeCAD. Это чрезвычайно мощно, Вы можете создавать собственный инструмент.
-   Он расширяемый, вы можете легко подключить новые модули к вашей установке Python и расширить его функциональность. Например, есть модули, которые позволяют Python читать и писать изображения, общаться с Твиттером, планировать задачи, которые будут выполняться вашей операционной системой, и т. Д.

Нижеследующее является базовым введением и ни в коем случае не полным учебником. Но есть надежда, что это даст хорошую стартовую точку для более глубокого изучения FreeCad и его механизмов. Мы настоятельно рекомендуем вам вводить фрагменты кода ниже в интерпретатор Python.

## Интерпретатор

Usually when writing computer programs, you open a text editor or your special programming environment (which is basically a text editor with some additional tools), write your program, then compile and execute. Often one or more errors were made during entry, so your program won\'t work. You may even get an error message telling you what went wrong. Then you go back to your text editor, correct the mistakes, run again, repeating until your program works as intended.

In Python that whole process can be done transparently inside the Python interpreter. The interpreter is a Python window with a command prompt, where you can simply type Python code. If you have installed Python on your computer (download it from the [Python website](https://www.python.org/) if you are on Windows or Mac, install it from your package repository if you are on GNU/Linux), you will have a Python interpreter in your start menu. But, as already mentioned, FreeCAD also has a built-in Python interpreter: the [Python console](Python_console.md).

![](images/FreeCAD_Python_console.png ) *The FreeCAD Python console*

If you don\'t see it, click on **View → Panels → Python console**. The Python console can be resized and also undocked.

The interpreter shows the Python version, then a `>>>` symbol which is the command prompt. Writing code in the interpreter is simple: one line is one instruction. When you press **Enter**, your line of code will be executed (after being instantly and invisibly compiled). For example, try writing this:


```python
print("hello")
```


`print()`

is a Python command that, obviously, prints something on the screen. When you press **Enter**, the operation is executed, and the message `"hello"` is printed. If you make an error, for example let\'s write:


```python
print(hello)
```

Python will immediately tell you so. In this case Python doesn\'t know what `hello` is. The `" "` characters specify that the content is a string, programming jargon for a piece of text. Without these the `print()` command doesn\'t recognize `hello`. By pressing the up arrow you can go back to the last line of code and correct it.

The Python interpreter also has a built-in help system. Let\'s say we don\'t understand what went wrong with `print(hello)` and we want specific information about the command:


```python
help("print")
```

You\'ll get a long and complete description of everything the `print()` command can do.

Now that you understand the Python interpreter, we can continue with the more serious stuff.

[наверх](#top.md)

## Переменные

Very often in programming you need to store a value under a name. That\'s where variables come in. For example, type this:


```python
a = "hello"
print(a)
```

You probably understand what happened here, we saved the string `"hello"` under the name `a`. Now that `a` is known we can use it anywhere, for example in the `print()` command. We can use any name we want, we just need to follow some simple rules, such as not using spaces or punctuation and not using Python keywords. For example, we can write:


```python
hello = "my own version of hello"
print(hello)
```

Now `hello` is not an undefined any more. Variables can be modified at any time, that\'s why they are called variables, their content can vary. For example:


```python
myVariable = "hello"
print(myVariable)
myVariable = "good bye"
print(myVariable)
```

We changed the value of `myVariable`. We can also copy variables:


```python
var1 = "hello"
var2 = var1
print(var2)
```

It is advisable to give meaningful names to your variables. After a while you won\'t remember what your variable named `a` represents. But if you named it, for example, `myWelcomeMessage` you\'ll easily remember its purpose. Plus your code is a step closer to being self-documenting.

Case is very important, `myVariable` is not the same as `myvariable`. If you were to enter `print(myvariable)` it would come back with an error as not defined.

[наверх](#top.md)

## Числа

Of course Python programs can deal with all kinds of data, not just text strings. One thing is important, Python must know what kind of data it is dealing with. We saw in our print hello example, that the `print()` command recognized our `"hello"` string. By using `" "` characters, we specified that what follows is a text string.

We can always check the data type of a variable with the `type()` command:


```python
myVar = "hello"
type(myVar)
```

It will tell us the content of `myVar` is a `'str'`, which is short for string. We also have other basic data types such as integer and float numbers:


```python
firstNumber = 10
secondNumber = 20
print(firstNumber + secondNumber)
type(firstNumber)
```

Python knows that 10 and 20 are integer numbers, so they are stored as `'int'`, and Python can do with them everything it can do with integers. Look at the results of this:


```python
firstNumber = "10"
secondNumber = "20"
print(firstNumber + secondNumber)
```

Here we forced Python to consider that our two variables are not numbers but pieces of text. Python can add two pieces of text together, although in that case, of course, it won\'t perform any arithmetic. But we were talking about integer numbers. There are also float numbers. The difference is float numbers can have a decimal part and integer numbers do not:


```python
var1 = 13
var2 = 15.65
print("var1 is of type ", type(var1))
print("var2 is of type ", type(var2))
```

Integers and floats can be mixed together without problems:


```python
total = var1 + var2
print(total)
print(type(total))
```

Because `var2` is a float Python automatically decides that the result must also be a float. But there are cases where Python does not knows what type to use. For example:


```python
varA = "hello 123"
varB = 456
print(varA + varB)
```

This results in an error, `varA` is a string and `varB` is an integer, and Python doesn\'t know what to do. However, we can force Python to convert between types:


```python
varA = "hello"
varB = 123
print(varA + str(varB))
```

Now that both variables are strings the operation works. Note that we \"stringified\" `varB` at the time of printing, but we didn\'t change `varB` itself. If we wanted to turn `varB` permanently into a string, we would need to do this:


```python
varB = str(varB)
```

We can also use `int()` and `float()` to convert to integer and float if we want:


```python
varA = "123"
print(int(varA))
print(float(varA))
```

You must have noticed that we have used the `print()` command in several ways. We printed variables, sums, several things separated by commas, and even the result of another Python command. Maybe you also saw that these two commands:


```python
type(varA)
print(type(varA))
```

have the same result. This is because we are in the interpreter, and everything is automatically printed. When we write more complex programs that run outside the interpreter, they won\'t print automatically, so we\'ll need to use the `print()` command. With that in mind let\'s stop using it here. From now on we will simply write:


```python
myVar = "hello friends"
myVar
```

[наверх](#top.md)

## Списки

Another useful data type is a list. A list is a collection of other data. To define a list we use `[ ]`:


```python
myList = [1, 2, 3]
type(myList)
myOtherList = ["Bart", "Frank", "Bob"]
myMixedList = ["hello", 345, 34.567]
```

As you can see a list can contain any type of data. You can do many things with a list. For example, count its items:


```python
len(myOtherList)
```

Or retrieve one item:


```python
myName = myOtherList[0]
myFriendsName = myOtherList[1]
```

While the `len()` command returns the total number of items in a list, the first item in a list is always at position `0`, so in our `myOtherList` `"Bob"` will be at position `2`. We can do much more with lists such as sorting items and removing or adding items.

Interestingly a text string is very similar to a list of characters in Python. Try doing this:


```python
myvar = "hello"
len(myvar)
myvar[2]
```

Usually what you can do with lists can also be done with strings. In fact both lists and strings are sequences.

Apart from strings, integers, floats and lists, there are more built-in data types, such as dictionaries, and you can even create your own data types with classes.

[наверх](#top.md)

## Indentation

One important use of lists is the ability to \"browse\" through them and do something with each item. For example look at this:


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
for dalton in alldaltons:
    print(dalton + " Dalton")
```

We iterated (programming jargon) through our list with the `for in` command and did something with each of the items. Note the special syntax: the `for` command terminates with `:` indicating the following will be a block of one of more commands. In the interpreter, immediately after you enter the command line ending with `:`, the command prompt will change to `...` which means Python knows that there is more to come.

How will Python know how many of the next lines will need to be executed inside the `for in` operation? For that, Python relies on indentation. The next lines must begin with a blank space, or several blank spaces, or a tab, or several tabs. And as long as the indentation stays the same the lines will be considered part of the `for in` block. If you begin one line with 2 spaces and the next one with 4, there will be an error. When you have finished, just write another line without indentation, or press **Enter** to come back from the `for in` block

Indentation also aids in program readability. If you use large indentations (for example use tabs instead of spaces) when you write a big program, you\'ll have a clear view of what is executed inside what. We\'ll see that other commands use indented blocks of code as well.

The `for in` command can be used for many things that must be done more than once. It can, for example, be combined with the `range()` command:


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

If you have been running the code examples in an interpreter by copy-pasting, you will find the previous block of text will throw an error. Instead, copy to the end of the indented block, i.e. the end of the line `total <nowiki>=</nowiki> total + number` and then paste in the interpreter. In the interpreter press **Enter** until the three dot prompt disappears and the code runs. Then copy the final two lines followed by another **Enter**. The final answer should appear.

If you type into the interpreter `help(range)` you will see:


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

Another `range()` example:


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
for n in range(4):
    print(alldaltons[n], " is Dalton number ", n)
```

The `range()` command also has that strange particularity that it begins with `0` (if you don\'t specify the starting number) and that its last number will be one less than the ending number you specify. That is, of course, so it works well with other Python commands. For example:


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
total = len(alldaltons)
for n in range(total):
    print(alldaltons[n])
```

Another interesting use of indented blocks is with the `if` command. This command executes a code block only if a certain condition is met, for example:


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
if "Joe" in alldaltons:
    print("We found that Dalton!!!")
```

Of course this will always print the sentence, but try replacing the second line with:


```python
if "Lucky" in alldaltons:
```

Then nothing is printed. We can also specify an `else` statement:


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
if "Lucky" in alldaltons:
    print("We found that Dalton!!!")
else:
    print("Such Dalton doesn't exist!")
```

[наверх](#top.md)

## Функции

There are very few [standard Python commands](https://docs.python.org/3/reference/lexical_analysis.html#identifiers) and we already know several of them. But you can create your own commands. In fact, most of the additional modules that you can plug into your Python installation do just that, they add commands that you can use. A custom command in Python is called a function and is made like this:


```python
def printsqm(myValue):
    print(str(myValue) + " square meters")

printsqm(45)
```

The `def()` command defines a new function, you give it a name, and inside the parenthesis you define the arguments that the function will use. Arguments are data that will be passed to the function. For example, look at the `len()` command. If you just write `len()`, Python will tell you it needs an argument. Which is obvious: you want to know the length of something. If you write `len(myList)` then `myList` is the argument that you pass to the `len()` function. And the `len()` function is defined in such a way that it knows what to do with this argument. We have done the same thing with our `printsqm` function.

The `myValue` name can be anything, and it will only be used inside the function. It is just a name you give to the argument so you can do something with it. By defining arguments you also to tell the function how many to expect. For example, if you do this:


```python
printsqm(45, 34)
```

there will be an error. Our function was programmed to receive just one argument, but it received two, `45` and `34`. Let\'s try another example:


```python
def sum(val1, val2):
    total = val1 + val2
    return total

myTotal = sum(45, 34)
```

Here we made a function that receives two arguments, sums them, and returns that value. Returning something is very useful, because we can do something with the result, such as store it in the `myTotal` variable.

[наверх](#top.md)

## Модули

Now that you have a good idea of how Python works, you will need to know one more thing: How to work with files and modules.

Until now, we have written Python instructions line by line in the interpreter. This method is obviously not suitable for larger programs. Normally the code for Python programs is stored in files with the {{FileName|.py}} extension. Which are just plain text files and any text editor (Linux gedit, emacs, vi or even Windows Notepad) can be used to create and edit them.

There are several of ways to execute a Python program. In Windows, simply right-click your file, open it with Python, and execute it. But you can also execute it from the Python interpreter itself. For this, the interpreter must know where your program is. In FreeCAD the easiest way is to place your program in a folder that FreeCAD\'s Python interpreter knows by default, such as FreeCAD\'s user {{FileName|Mod}} folder:

-   On Linux it is usually {{FileName|/home/<username>/.FreeCAD/Mod/}}.
-   On Windows it is {{FileName|%APPDATA%\FreeCAD\Mod\}}, which is usually {{FileName|C:\Users\<username>\Appdata\Roaming\FreeCAD\Mod\}}.
-   On Mac OSX it is usually {{FileName|/Users/<username>/Library/Preferences/FreeCAD/Mod/}}.

Let\'s add a subfolder there called {{FileName|scripts}} and then write a file like this:


```python
def sum(a,b):
    return a + b

print("myTest.py succesfully loaded")
```

Save the file as {{FileName|myTest.py}} in the {{FileName|scripts}} folder, and in the interpreter window write:


```python
import myTest
```

without the {{FileName|.py}} extension. This will execute the contents of the file, line by line, just as if we had written it in the interpreter. The sum function will be created, and the message will be printed. Files containing functions, like ours, are called modules.

When we write a `sum()` function in the interpreter, we execute it like this:


```python
sum(14, 45)
```

But when we import a module containing a `sum()` function the syntax is a bit different:


```python
myTest.sum(14, 45)
```

That is, the module is imported as a \"container\", and all its functions are inside that container. This is very useful, because we can import a lot of modules, and keep everything well organized. Basically when you see `something.somethingElse`, with a dot in between, then this means `somethingElse` is inside `something`.

We can also import our sum() function directly into the main interpreter space:


```python
from myTest import *
sum(12, 54)
```

Almost all modules do that: they define functions, new data types and classes that you can use in the interpreter or in your own Python modules, because nothing prevents you from importing other modules inside your module!

How do we know what modules we have, what functions are inside and how to use them (that is, what kind of arguments they need)? We have already seen that Python has a `help()` function. Doing:


```python
help("modules")
```

will give us a list of all available modules. We can import any of them and browse their content with the `dir()` command:


```python
import math
dir(math)
```

We\'ll see all the functions contained in the `math` module, as well as strange stuff named `__doc__`, `__file__`, `__name__`. Every function in a well made module has a `__doc__` that explains how to use it. For example, we see that there is a `sin()` function inside the math module. Want to know how to use it? 
```python
print(math.sin.__doc__)
```

It may not be evident, but on either side of `doc` are two underscore characters.

And finally one last tip: When working on new or existing code, it is better to not use the FreeCAD macro file extension, {{FileName|.FCMacro}}, but instead use the standard {{FileName|.py}} extension. This is because Python doesn\'t recognize the {{FileName|.FCMacro}} extension. If you use {{FileName|.py}} your code can be easily loaded with `import`, as we have already seen, and also reloaded with `importlib.reload()`:


```python
import importlib
importlib.reload(myTest)
```

There is however an alternative:


```python
exec(open("C:/PathToMyMacro/myMacro.FCMacro").read())
```

[наверх](#top.md)

## Starting with FreeCAD 

Hopefully you now have a good idea of how Python works, and you can start exploring what FreeCAD has to offer. FreeCAD\'s Python functions are all well organized in different modules. Some of them are already loaded (imported) when you start FreeCAD. Just try:


```python
dir()
```

[наверх](#top.md)

## Примечания

-   FreeCAD was originally designed to work with Python 2. Since Python 2 reached the end of its life in 2020, future development of FreeCAD will be done exclusively with Python 3, and backwards compatibility will not be supported.
-   Much more information about Python can be found in the [official Python tutorial](https://docs.python.org/3/tutorial/index.html) and the [official Python reference](https://docs.python.org/3/reference/).

[наверх](#top.md)


{{Powerdocnavi

}} 

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Python Code{{\#translation:}}](Category:Python_Code.md)
