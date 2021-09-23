# Introduction to Python/ja



{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

これは、Pythonをはじめる人のために作られた短いチュートリアルです。 [Python](http://en.wikipedia.org/wiki/Python_%28programming_language%29)はオープンソース、マルチプラットフォームの[プログラミング言語](http://en.wikipedia.org/wiki/Programming_language)です。 Pythonは他の一般的なプログラミング言語と違い、あなたのようなはじめてのユーザーにとって非常に使いやすくするいくつかの機能を持っています。


</div>


<div class="mw-translate-fuzzy">

-   人間が読みやすいように特別に設計されたので、それを学習し理解することは非常に容易であるされています。
-   C言語のようなコンパイル言語とは異なり、実行する前にコンパイルを必要とせずにコードを解釈します。あなたがそうしたい場合は、記述したコードはすぐに1行ずつ実行することができます。これは、ステップごとに実行されるので、簡単に学習でき、あなたのコード内のエラーを検出することが極めて容易になります。
-   スクリプト言語として他のプログラムに埋め込むことができます。 FreeCADは、埋め込まれたPythonインタプリタを持っているので、FreeCADの部品を操作する例えばジオメトリを作成することをFreeCADのPythonコードで書くことができます。これは非常に強力でプログラマが用意した\"球体作成\"のボタンをクリックするかわりに自由にかつ簡単に作成した独自のツールであなたが望む正確なジオメトリを作成することができます。
-   それは拡張可能であり、新しいPythonのモジュールをプラグインとして簡単にインストールし機能を拡張することができます。例えば、jpg画像の読み書き、Twitterとの通信、使用しているオペレーティングシステムによって実行されるタスクのスケジュール等のモジュールがあります。


</div>


<div class="mw-translate-fuzzy">

まずは、実際に使ってみましょう！次は非常に簡単な紹介であることに注意してください。これは完全はチュートリアルではありません。しかし、私の希望は、後にFreeCADのメカニズムをより深く探求するための十分な基礎を得ることです。


</div>

## インタプリタ


<div class="mw-translate-fuzzy">

通常、コンピュータプログラムを書くとき、単にテキストエディタを使用するかほとんど場合は、特別なプログラミング環境のテキストエディタと周辺のツールを利用して プログラムを書き、それをコンパイルして実行します。ほとんどの場合、記述中に誤りがあるとあなたのプログラムは動作しません。そして、何が悪かったのかを伝えるエラーメッセージが表示されます。あなたはテキストエディタに戻って、間違いを修正し、再度実行するということをプログラムが正常に動作するまで繰り返します。


</div>


<div class="mw-translate-fuzzy">

Pythonにおけるプロセスは、Pythonインタプリタの内部で透過的に実行できます。Pythonインタプリタは、Pythonウィンドウのコマンドプロンプトを使って簡単にPythonコードを入力することができます。お使いのコンピュータにPythonをインストールする場合は、（WindowsもしくはMacの場合は[PythonのWebサイト](http://www.python.org)からダウンロードしてください。GNU/Linuxの場合はパッケージリポジトリからインストールしてください）スタートメニューにPythonインタプリタが入ります。しかし、FreeCADは、ウィンドウ下部にPythonインタプリタが入っています。


</div>

![](images/FreeCAD_Python_console.png )


<div class="mw-translate-fuzzy">

![](images/Screenshot_pythoninterpreter.jpg )


</div>


<div class="mw-translate-fuzzy">

（表示されない場合は、View → Views → Python consoleをクリックしてください。）


</div>


<div class="mw-translate-fuzzy">

インタプリタは、Pythonのバージョンを表示し、そしてコマンドプロンプトとなる\>\>\>のシンボルを表示します。ここへPythonコードを入力します。インタプリタでコードを書くことは簡単です：1行は1命令です。あなたがEnterを押すと、入力したコードが実行されます。（瞬時にコンパイルされます）例えば、これを書いてください。


</div>


```python
print("hello")
```


<div class="mw-translate-fuzzy">

print は言うまでもなく画面に何かを表示することを意味する特別なPythonのキーワードです。Enterキーを押すと、操作が実行され、\"hello\"というメッセージが表示されます。エラーにしたい場合は、次の例を書いてください：

print hello


</div>


```python
print(hello)
```


<div class="mw-translate-fuzzy">

Pythonは\"hello\"が何かを知らないということを教えてくれる。 「\"」はその中身が文字列であることを指します。それはプログラミング用語において、ひとつのテキスト文字列ｆであることを示します。「\"」がない場合、printコマンドは、helloがテキストの一部ではなく特別なPythonのキーワードだと思います。重要なことは、あなたがすぐにエラーになった通知を受けとれることです。上矢印を押して、（FreeCADのインタプリタの場合はCtrl + 上矢印）、あなたが書いた最後のコマンドに戻って、それを修正することができます。


</div>


<div class="mw-translate-fuzzy">

Pythonインタプリタにもヘルプ機能があります。次の命令を試してください：


</div>


```python
help("print")
```


<div class="mw-translate-fuzzy">

あなたは、printコマンドが実行できるすべての完全な説明を得ることができます。


</div>


<div class="mw-translate-fuzzy">

今、私たちはインタプリタを使いこなせます。本気になって使いはじめましょう。


</div>

[top](#top.md)

## 変数


<div class="mw-translate-fuzzy">

もちろん、\"hello\"を表示することが注目すべき点ではありません。より注目すべき点は、あなたが気づかなかったことをPythonが解釈して表示していることです。 これが変数の概念です。変数は単に名前をつけて値を格納しているのです。例えば次のように入力します。


</div>


```python
a = "hello"
print(a)
```


<div class="mw-translate-fuzzy">

何がおこったのか解説すると、\"hello\"という文字列をaという名前をつけて格納しました。この時点でaは未知の名前ではありません！printコマンドなどで、どこでも使用することができます。スペースや句切り点を使用しないというような簡単なルールに守っていれば任意の名前を使用できます。この例は、非常によく使います。


</div>


```python
hello = "my own version of hello"
print(hello)
```


<div class="mw-translate-fuzzy">

見ましたか？helloはもう未定義の言葉ではありません。不運にもPythonで予約されているキーワードを選んだ場合はどうなりますか？\"print\"という名前で文字列を格納したいとしましょう：


</div>


```python
myVariable = "hello"
print(myVariable)
myVariable = "good bye"
print(myVariable)
```


<div class="mw-translate-fuzzy">

myVariableの値を変更しました。また、変数をコピーすることができます：


</div>


```python
var1 = "hello"
var2 = var1
print(var2)
```


<div class="mw-translate-fuzzy">

あなたの使う変数に適切な名前を付けることが重要であることに注意してください。なぜなら、長いプログラムを書こうとしたときに\"a\"という名前の変数が何のためにあるのか覚えられないと思います。しかし、あなたが例のようにmyWelcomeMessageという変数の名前を使用した場合、あなたはその変数を見たり使ったりするときに簡単に思い出すことができます。


</div>

Case is very important, `myVariable` is not the same as `myvariable`. If you were to enter `print(myvariable)` it would come back with an error as not defined.

[top](#top.md)

## 数値


<div class="mw-translate-fuzzy">

もちろん、あなたがプログラムを作る上で文字列だけでなくすべての種類のデータ、特に数値を使うことを知っている必要があります。重要なことの一つにPythonでどのような種類のデータを使うことができるか知っておく必要があります。print helloの例題から　printコマンドで\"hello\"という文字列を表示できることがわかりました。それは\"を使用すると、printコマンドにおいてその後に続くのが文字列であることがわかりました。


</div>


<div class="mw-translate-fuzzy">

特別なPythonのキーワードを入力することにより、いつでも変数のデータ型が何なのか確認することができます:


</div>


```python
myVar = "hello"
type(myVar)
```


<div class="mw-translate-fuzzy">

これはmyVarの中身が\'str\'、つまりPython用語における文字列であることがわかります。また、他の基本的なデータ型には、整数型や浮動小数点数型などがあります:


</div>


```python
firstNumber = 10
secondNumber = 20
print(firstNumber + secondNumber)
type(firstNumber)
```


<div class="mw-translate-fuzzy">

これは、今までよりはるかに興味深いですが、それはないですか？今、私たちは、すでに強力な電卓を持っています！それが機能していることをよく見てください。Pythonは10と20が整数であることを認識しています。だからそれらは \"int\"型として格納されており、Pythonは整数として扱うことができます。この結果を見てください:


</div>


```python
firstNumber = "10"
secondNumber = "20"
print(firstNumber + secondNumber)
```


<div class="mw-translate-fuzzy">

見ましたか？これはPythonは2つの変数が数字ではなく単なる文字列として認識していることを意味しています。Pythonは、2つの文字列を合わせて一つにすることができますが、2つの合計を求めようとはしません。しかし、我々は、整数型のことも話題にしていました。浮動小数点型もあります。これらの違いは浮動小数点の数値は小数部を有することができ、整数の数値は、小数部を持っていないということです:


</div>


```python
var1 = 13
var2 = 15.65
print("var1 is of type ", type(var1))
print("var2 is of type ", type(var2))
```


<div class="mw-translate-fuzzy">

int型と浮動小数点型は問題なく一緒に混合することができます:


</div>


```python
total = var1 + var2
print(total)
print(type(total))
```


<div class="mw-translate-fuzzy">

いいですか？もちろん合計は小数になります。 Pythonは自動的に結果が浮動小数点型であると判断しました。この例のように、いくつかのケースではPythonは自動的に何型かをを判断します。他のケースではそれはしていません。たとえば、次のように:


</div>


```python
varA = "hello 123"
varB = 456
print(varA + varB)
```


<div class="mw-translate-fuzzy">

これは、エラーになります。varAは文字列であり、varBのデータ型は整数型で、Pythonは何をすればいいのかわかりません。しかし、型の変換をPythonに強制することもできます:


</div>


```python
varA = "hello"
varB = 123
print(varA + str(varB))
```


<div class="mw-translate-fuzzy">

これで、両方が文字列となり実行できます！表示する時にvarBが\"文字列\"となっていますが、私たちはvarB自体を変更していないことに注意してください。varBを常に文字列にしたい場合は、次のようにします:


</div>


```python
varB = str(varB)
```


<div class="mw-translate-fuzzy">

また、場合によって整数型や浮動小数点型に変換するためにint()やfloat()を使用することができます:


</div>


```python
varA = "123"
print(int(varA))
print(float(varA))
```


<div class="mw-translate-fuzzy">

このセクションでprintコマンドをいくつかの方法で使用したことに気づいている必要があります。変数の値、合計、コンマで区切られたいくつかの事項、そしてtype()のようなPythonコマンドの結果を出力しています。これらの2つのコマンドを実行してみてはどうでしょうか:


</div>


```python
type(varA)
print(type(varA))
```


<div class="mw-translate-fuzzy">

まったく同じ結果になります。それはインタプリタであり、すべてのものが画面上に自動的に表示されているからです。インタプリタの外で複雑なプログラムを書いて実行させようと思うと、自動的にすべてが画面上に表示されないので、printコマンドを使用する必要があります。しかし、今からここではそれは使わないでおきましょう。それよりはやいからです。だから簡単に書くことができます:


</div>


```python
myVar = "hello friends"
myVar
```

[top](#top.md)

## リスト


<div class="mw-translate-fuzzy">

もう一つの興味深いデータ型がリストである。リストは、単にデータの配列です。\"\"を使用して、テキスト文字列を定義するのと同じ方法で、\[\]を使用してリストを定義します。

myList = [1,2,3]
type(myList)
myOtherList = ["Bart", "Frank", "Bob"]
myMixedList = ["hello", 345, 34.567]


</div>


```python
myList = [1, 2, 3]
type(myList)
myOtherList = ["Bart", "Frank", "Bob"]
myMixedList = ["hello", 345, 34.567]
```


<div class="mw-translate-fuzzy">

それが任意の型のデータで作成できることがわかります。変数も一緒にグループ化することができますので、リストは非常に便利です。その後、グループに対して様々な処理を行うことができます　次の例はグループ内のデータの数をカウントします：

len(myOtherList)


</div>


```python
len(myOtherList)
```


<div class="mw-translate-fuzzy">

またはリストの中から1つのアイテムを取得します：

myName = myOtherList[0]
myFriendsName = myOtherList[1]


</div>


```python
myName = myOtherList[0]
myFriendsName = myOtherList[1]
```


<div class="mw-translate-fuzzy">

あなたはlen()コマンドの結果からアイテムの合計数がわかり、0から始まるリストの\"位置\"がわかります。リスト内の最初のアイテムが常に0の位置にあるので、myOtherListで、\"Bob\"は2番目の位置になります。[ここ](http://diveintopython.org/native_data_types/lists.html)を読むことによってアイテムの並び替えや削除、追加など様々な操作をおこなうことができます。


</div>


<div class="mw-translate-fuzzy">

とても面白くて興味深い事:テキストの文字列は文字のリストに非常に似ています！これをやってみてください：

myvar = "hello"
len(myvar)
myvar[2]


</div>


```python
myvar = "hello"
len(myvar)
myvar[2]
```


<div class="mw-translate-fuzzy">

通常、あなたがリストに対して実行できるすべての操作を文字列に対して行うことができます。実際にはリストも文字列も配列です。


</div>


<div class="mw-translate-fuzzy">

文字列、整数、浮動小数点数とリストの他には、[辞書](http://www.diveintopython.org/getting_to_know_python/dictionaries.html)にのっているような組み込みのデータ型だけではなく、[クラス](http://www.freenetpages.co.uk/hp/alan.gauld/tutclass.htm)を使用して独自のデータ型を作成することもできます。


</div>

[top](#top.md)

## インデント


<div class="mw-translate-fuzzy">

リストの一つのとても洗練された使用方法は、アイテムを参照して各要素で何らかの処理をすることです。例えばこれを見てください：

alldaltons = ["Joe", "William", "Jack", "Averell"]
for dalton in alldaltons:
   print dalton + " Dalton"


</div>


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
for dalton in alldaltons:
    print(dalton + " Dalton")
```


<div class="mw-translate-fuzzy">

リストを使って（再びプログラミング専門用語！）\"for \... in \...\"コマンドと各要素で何らかの処理を行いました。特殊な構文に注意してください。forコマンドは、:で完了するとこその次のコマンドを1ブロックのコマンドとします。コマンドラインに:を入力すると\...コマンドプロンプトに変わります。これは:が行の終わりであることを示し次に入力される行が1ブロックであるとPythonは解釈します。


</div>


<div class="mw-translate-fuzzy">

Pythonはどのようにしてfor\...in構文の中で実行する命令文がどれぐらいあるのかを判断するのでしょうか？そのために、Pythonはインデントを使用しています。つまり、あなたの次の命令がすぐに実行されません。あなたは空白、連続した空白、またはタブ、連続したタブを使って記述します。他のプログラミング言語では、括弧で括るなどPythonとは違う方法を使っています。 あなたは**同じ**インデントを使用して次の命令を記述している限り、それらはfor-inのブロックの一部とみなされます。あなたは2つのスペースを使用して記述した後、次の行を4つにするとエラーが発生します。 作業が終わったら、インデントせずに別の行を書き込むか、または単にEnterを押せばfor-inのブロックから戻ってくることができます。


</div>


<div class="mw-translate-fuzzy">

インデントは幅の大きなインデントを（例えば幅が大きいのでスペースの代わりにタブを使用する）使う場合、大きなプログラムを書くときにどのような処理を実行しているかを明確にすることができるのでとてもクールです。for-in以外にもコードをインデントでブロックにする多くのコマンドがあります。


</div>


<div class="mw-translate-fuzzy">

for-inコマンドは命令を繰り返し実行するようなものにも使用することができます。例えばrange()コマンドと組み合わせることができます。

serie = range(1,11)
total = 0
print "sum"
for number in serie:
   print number
   total = total + number
print "----"
print total


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

If you have been running the code examples in an interpreter by copy-pasting, you will find the previous block of text will throw an error. Instead, copy to the end of the indented block, i.e. the end of the line `total <nowiki>=</nowiki> total + number` and then paste in the interpreter. In the interpreter press **Enter** until the three dot prompt disappears and the code runs. Then copy the final two lines followed by another **Enter**. The final answer should appear.


<div class="mw-translate-fuzzy">

range()コマンドは、（あなたが開始番号を指定しない場合）0から始まる特性を持っており、最後の数は、指定した終了番号より1つ少なくなることに注意してください。それはもちろん、他のPythonコマンドでも同じです。例えば、次のように:

alldaltons = ["Joe", "William", "Jack", "Averell"]
total = len(alldaltons)
for n in range(total):
   print alldaltons[n]

インデントされたブロックのもう一つの興味深い使用方法はifコマンドを使用することです。特定の条件が満たされる場合に限り、ブロックのコードを実行します。例えば:

alldaltons = ["Joe", "William", "Jack", "Averell"]
if "Joe" in alldaltons:
   print "We found that Dalton!!!"

もちろん、これは常に最初のセンテンスを表示します。しかし、2行目を次のように書き換えると:

if "Lucky" in alldaltons:

何も表示されません。else:ステートメントを指定することができます。

alldaltons = ["Joe", "William", "Jack", "Averell"]
if "Lucky" in alldaltons:
   print "We found that Dalton!!!"
else:
   print "Such Dalton doesn't exist!"


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

より複雑なもの：

alldaltons = ["Joe", "William", "Jack", "Averell"]
for n in range(4):
   print alldaltons[n], " is Dalton number ", n


</div>


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

[top](#top.md)

## 関数


<div class="mw-translate-fuzzy">

標準のPythonコマンドは、多くはありません [standard Python commands](http://docs.python.org/reference/lexical_analysis.html#identifiers).。現在のバージョンのPythonには約30の標準コマンドがあり、すでにそれらのいくつかを知っています。しかし、独自のコマンドを考案できることを想像してみてください。さて、私たちは独自のコマンドを作ることができ、それは非常に簡単です。実際、多くの追加モジュールはあなたがコマンドを追加するだけでPythonに追加インストールされます。 Pythonでカスタムコマンドは関数と呼ばれ、このように構成されています。

def printsqm(myValue):

  print str(myValue)+" square meters"

printsqm(45)


</div>


```python
def printsqm(myValue):
    print(str(myValue) + " square meters")

printsqm(45)
```


<div class="mw-translate-fuzzy">

極めてシンプルです。def()コマンドは、新しい関数を定義しています。あなたはそれに名前を付け、括弧内には、我々は関数の中で使おうとしている引数を定義します。引数は、関数に渡されるデータです。例えば、len()コマンドを見てみましょう。len()を単独で記述する場合、Pythonは引数を必要と教えてくれます。つまり、あなたは、len()を使って何かをしたいですよね？そして、例えば、あなたはlen(myList)と記述して、myListの長さを取得するとします。そしてmyListは、len()関数に渡す引数です。 len()関数は、渡された引数を使ってどのような処理を実行するのか定義されています。ここで行ったのと同じ処理です。


</div>


<div class="mw-translate-fuzzy">

\"myValue\"の名前は何でもかまいません、それは関数の内部でのみ使用されます。 あなたが変更できるのは名前だけですが、関数が要求するする引数の数にあわせて指定します。例えば、次の場合:

printsqm(45,34)


</div>


```python
printsqm(45, 34)
```


<div class="mw-translate-fuzzy">

エラーが発生します。この関数はただ1つの引数を受け取るようにプログラムされていますが、2つの引数、45および34を受け渡しました。その代わりにこのようなことができます:

def sum(val1,val2):

  total = val1 + val2
  return total

sum(45,34) myTotal = sum(45,34)


</div>


```python
def sum(val1, val2):
    total = val1 + val2
    return total

myTotal = sum(45, 34)
```


<div class="mw-translate-fuzzy">

2つの引数を受け取り合計して、その値を返す関数を作りました。値を返すことは非常に便利です。なぜならmyTotal変数に格納するなど、関数の実行結果を使って何かを行うことができます。もちろん、インタプリタであり、すべてのものを表示されるので、次を実行してください:

sum(45,34)


</div>

[top](#top.md)

## モジュール


<div class="mw-translate-fuzzy">

今、Python使いこなすためには、最後に1つ必要なことがあります。それはどのようにファイルやモジュールを操作するかです。


</div>


<div class="mw-translate-fuzzy">

これまで、インタプリタで1行ずつPythonの命令を書いてきましたね？もしいくつかの行をまとめて書くことができ、それらを一度にすべて実行できたらどうですか？それはもっと複雑なことをするためには手軽な手段です。さらに私たちの作ったものを保存することができます。まあ、それも非常に簡単です。単にテキストエディタ（Windowsのメモ帳など）を開き、インタプリタでプログラムを記述するのと同様にPythonのプログラムをすべて書き、その後、.pyの拡張子でこのファイルをどこかに保存します。それだけです、あなたは完全なPythonプログラムを作ることができました。もちろん、メモ帳よりも便利なエディタがありますが、それはPythonプログラムは、テキストファイル以外の何者でもないことを示しているだけです。


</div>


<div class="mw-translate-fuzzy">

Pythonでプログラムを実行する方法は何百もあります。Windowsでは、単にファイルを右クリックしPythonでそれを開いて実行します。しかし、Pythonインタプリタから直接プログラムを実行することもできます。直接実行するには、Pythonインタプリタが実行しようとする.pyプログラムの保存場所を知っている必要があります。

FreeCADでの最も簡単な方法は、FreeCADのbinフォルダまたはModフォルダのようにFreeCADのPythonインタプリタにデフォルトで設定されている場所にプログラムを配置することです。次のようなファイルを作成します:

    def sum(a,b):
        return a + b

    print "test.py succesfully loaded"


</div>


```python
def sum(a,b):
    return a + b

print("myTest.py succesfully loaded")
```


<div class="mw-translate-fuzzy">

そして作成したファイルをFreeCADの/binディレクトリにtest.pyとして保存します。さて、FreeCADを起動しましょう、そしてインタプリタウィンドウへ次のように入力します。

import test


</div>


```python
import myTest
```


<div class="mw-translate-fuzzy">

.pyの拡張子を除いたものです。これは単にインタプリタで1行ずつ書いて実行したかのように、ファイルの内容を実行します。sum関数が作成され、メッセージが出力されます。1つの大きな違いがあります：importコマンドは、ファイルに書かれたプログラムを実行するだけでなく今までのプログラム同様内部の関数を読み込むのでインタプリタで利用できるようになります。関数を含むファイルは、モジュールと呼ばれます。


</div>


<div class="mw-translate-fuzzy">

通常、インタプリタでsum()関数を記述し、実行するとき単に次のように入力します:

sum(14,45)


</div>


```python
sum(14, 45)
```


<div class="mw-translate-fuzzy">

これは以前行ったとおりです。我々はsum()関数を含むモジュールをインポートすると、構文が少し異なっています。次のように入力します:

test.sum(14,45)


</div>


```python
myTest.sum(14, 45)
```


<div class="mw-translate-fuzzy">

つまり、モジュールは\"container\"として読み込まれ、そのすべての関数は内部にあります。多くのモジュールをインポートし、すべての関数をうまく整理しておくことができるので、これは非常に有用です。したがって、基本的に、something.somethingElseのようにドットで区切ることによって、somethingElse関数がsomethingモジュールの内部にあることを意味しています。


</div>


<div class="mw-translate-fuzzy">

また、testの部分を記述せずにsum()関数のように、メインのインタプリタ空間に直接関数を読み込むことができます:

from test import *
sum(12,54)


</div>


```python
from myTest import *
sum(12, 54)
```


<div class="mw-translate-fuzzy">

基本的に、すべてのモジュールはそのように動作します。モジュールをインポートしてから、module.function(引数)のようにその関数を使用することができます。ほとんどすべてのモジュールが関数を定義し、新しいデータ型とクラスをインタプリタ、モジュール内でモジュールをインポートすることもできるのでPythonモジュールで使えるようになります。


</div>


<div class="mw-translate-fuzzy">

最後にもう一つ、非常に有用なものがあります。どのようなモジュールがありその内部にはどのような関数があってどのように使う（つまり必要とする引数の種類）かわかりますか？ Pythonがhelp()関数を持っていることをすでに知っています。次の操作をしてみましょう:

help()
modules


</div>


```python
help("modules")
```


<div class="mw-translate-fuzzy">

すべての利用可能なモジュールのリストが表示されます。対話式ヘルプから抜け出すには、qを入力し、それらのいずれかをインポートすることができます。dir()コマンドを使用してそのコンテンツを見ることができます。

import math
dir(math)


</div>


```python
import math
dir(math)
```


<div class="mw-translate-fuzzy">

mathモジュールに含まれるすべての関数と同様、\_\_doc\_\_, \_\_file\_\_, \_\_name\_\_といった奇妙な名前が表示されます。\_\_doc\_\_ はドキュメントの文字列を表し、非常に便利です。（既存の）モジュールに含まれるすべての関数は使用方法に関する説明を\_\_doc\_\_に持っています。例えばmathモジュールにはsin関数含まれていることがわかります。それの使用方法が知りたいですか？

print math.sin.__doc__


</div>


```python
print(math.sin.__doc__)
```

It may not be evident, but on either side of `doc` are two underscore characters.


<div class="mw-translate-fuzzy">

最後に少し使いやすい方法は:新しいモジュールをプログラミングするとき、時々プログラムのテストを行いたいです。一度、Pythonインタプリタでモジュールを小さく区切って新しいコードをテストするためにプログラムを記述します。

import myModule
myModule.myTestFunction()


</div>


```python
import importlib
importlib.reload(myTest)
```

There is however an alternative:


```python
exec(open("C:/PathToMyMacro/myMacro.FCMacro").read())
```

[top](#top.md)

## FreeCADではじめる


<div class="mw-translate-fuzzy">

Pythonのプログラムを作るためのアイデアが理解できた思います。そして、FreeCADがどのようなモジュールを提供しているか探し始めることができます。 FreeCADのPython関数は、すべてが異なるモジュールに整理されています。FreeCADを起動したときにそれらのいくつかはすでにロード（インポート）されます。だから、使うだけです。

dir()


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

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)
