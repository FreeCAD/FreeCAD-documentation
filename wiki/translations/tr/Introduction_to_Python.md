


{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

Bu Python\'a yeni başlayanlar için kısa bir rehberdir. [Python](http://en.wikipedia.org/wiki/Python_%28programming_language%29), açık kaynaklı, çoklu bir platformdur [programlama dili](http://en.wikipedia.org/wiki/Programming_language). Python, onu diğer yaygın programlama dillerinden çok farklı kılan ve sizin gibi yeni kullanıcıların erişebildiği birçok özelliğe sahiptir:


</div>


<div class="mw-translate-fuzzy">

-   Özellikle insanlar tarafından okunması kolay olacak şekilde tasarlandı ve bu yüzden öğrenmesi ve anlaması çok kolay.
-   Yorumlanır, yani C gibi derlenmiş dillerden farklı olarak, programınızın yürütülmeden önce derlenmesi gerekmez. İsterseniz yazdığınız kod, satır satır hemen çalıştırılabilir. Yavaş yavaş adım adım ilerleyebildiğiniz için, kodunuzdaki hataları öğrenmek ve hataları bulmak son derece kolaydır.
-   Kodlama dili olarak kullanılmak üzere diğer programlara gömülebilir. FreeCAD\'in yerleşik bir Python yorumlayıcısı vardır; Python kodunu FreeCAD\'e yazabilir, örneğin FreeCAD\'in parçalarını değiştirebilir, örneğin geometri oluşturmak için. Bu, bazı programcıların kodladığı \"küre yarat\" etiketli bir düğmeyi tıklamak yerine, son derece güçlüdür; Programcının öngöremeyeceği şekilde veya istediğiniz şekilde tam olarak istediğiniz geometriyi oluşturarak kendi aracınızı kolayca oluşturma özgürlüğüne sahipsiniz.
-   Genişletilebilirdir, Python kurulumunuzdaki yeni modülleri kolayca takabilir ve işlevselliğini artırabilirsiniz. Örneğin, Python\'un jpg görüntüleri okuyup yazmasına, twitter ile iletişim kurmasına, işletim sisteminiz tarafından gerçekleştirilecek görevleri zamanlamasına, vb. İzin veren modüllere sahipsiniz.


</div>


<div class="mw-translate-fuzzy">

Aşağıdaki kod parçacıklarını bir Python yorumlayıcısına girmenizi kesinlikle öneririz. Tartışmalarımızın çoğu için önemli olan, pasajın çalıştırılmasından sonraki satırdır, ortaya çıkar. Kodu çalıştırmamak yumruk çizgisi olmadan tümüyle oluşturulur. Öyleyse eller! Aşağıdakiler çok basit bir giriştir ve hiçbir şekilde tam bir eğitim değildir. Ancak bizim umudumuz, bunun FreeCAD mekanizmalarını daha derinlemesine keşfetmek için yeterli temelleri sağlayacağıdır.


</div>

## Yorumlayıcı


<div class="mw-translate-fuzzy">

Genellikle, bilgisayar programları yazarken, sadece bir metin editörünü veya özel programlama ortamınızı (genellikle birkaç ek araç içeren bir metin editörüdür) açarsınız, programınızı yazıp derler ve çalıştırırsınız. Genellikle, kod yazma sırasında bir veya daha fazla hata yapıldı ise programınız çalışmayacaktır. Neyin yanlış gittiğini söyleyen bir hata mesajı bile alabilirsiniz. Ardından metin editörünüze döner, hataları düzeltir, tekrar çalıştırırsınız, programınız istenen şekilde çalışıncaya kadar tekrarlarsınız.


</div>


<div class="mw-translate-fuzzy">

Python\'daki bu işlem Python yorumlayıcısının içinde şeffaf bir şekilde yapılabilir. Yorumlayıcı, yalnızca Python kodunu yazabileceğiniz bir komut istemi içeren bir Python penceresidir. Bilgisayarınıza Python yüklerseniz (Windows veya Mac'te iseniz [Python web sitesinden indirin](http://www.python.org), eğer Windows veya Mac'te iseniz, GNU / Linux'taysanız paket deponuzdan yükleyin) Başlat menünüzde bir Python yorumlayıcısı var. Ancak FreeCAD\'in alt penceresinde bir Python yorumlayıcısı da vardır:


</div>

![](images/FreeCAD_Python_console.png )


<div class="mw-translate-fuzzy">

![](images/Screenshot_pythoninterpreter.jpg )


</div>


<div class="mw-translate-fuzzy">

(Eğer bulamadıysanız, Görünüm -\> Paneller -\> Python konsolu\'nu tıklayın.)


</div>


<div class="mw-translate-fuzzy">

Yorumlayıcı, Python versiyonunu ve ardından Python kodunu girdiğiniz komut istemi olan \>\>\> sembolünü gösterir. Yorumlayıcıya kod yazmak basittir: bir satır bir talimattır. Enter tuşuna bastığınızda, kod satırınız yürütülür (hemen ve görünmez bir şekilde derlendikten sonra). Örneğin, şunu yazmayı deneyin:


</div>


```python
print("hello")
```


<div class="mw-translate-fuzzy">

print, açıkça ekranda bir şey yazdırmak için kullanılan özel bir Python anahtar kelimesidir. Enter tuşuna bastığınızda, işlem yürütülür ve \"merhaba\" mesajı yazdırılır. Bir hata yaparsanız, örneğin yazalım:


</div>


```python
print(hello)
```


<div class="mw-translate-fuzzy">

Python bize merhaba\'yı bilmediğini söyleyecek. \"Karakterler içeriğin sadece bir jargon, bir metin parçası olan bir dize olduğunu belirtir. \" Olmadan, baskı komutu merhaba bir metin parçası değil, özel bir Python anahtar sözcüğüdür. Önemli olan, hemen bir hata yaptığınız konusunda bilgilendirilmenizdir. Yukarı okuna basarak (veya FreeCAD yorumlayıcısında, CTRL yukarı okunda) yazdığınız son komuta geri dönebilir ve düzeltebilirsiniz.


</div>


<div class="mw-translate-fuzzy">

Python yorumlayıcı ayrıca dahili bir yardım sistemine sahiptir. Yazmayı deneyin:


</div>


```python
help("print")
```


<div class="mw-translate-fuzzy">

Print komutunun yapabileceği her şeyin uzun ve eksiksiz bir açıklamasını alırsınız.


</div>


<div class="mw-translate-fuzzy">

Artık yorumlayıcıya hükmettiğimize göre, ciddi şeylerle başlayabiliriz.


</div>

[top](#top.md)

## Değişkenler


<div class="mw-translate-fuzzy">

Tabii ki, \"merhaba\" yazdırmak çok ilginç değil. Daha ilginç olanı, daha önce bilmediğiniz şeyler basmak ya da Python\'un sizin için bulmasına izin vermek. Değişken kavramının devreye girdiği yer burasıdır. Bir değişken, yalnızca bir ad altında sakladığınız bir değerdir. Örneğin, şunu yazın:


</div>


```python
a = "hello"
print(a)
```


<div class="mw-translate-fuzzy">

Sanırım ne olduğunu anladınız, biz \"merhaba\" dizesini \"a\" adı altında \"kaydettik\". Şimdi, \"a\" artık bilinmeyen bir isim değil! Herhangi bir yerde, örneğin baskı komutunda kullanabiliriz. İstediğimiz herhangi bir ismi kullanabiliriz, sadece boşluk veya noktalama işareti kullanmama gibi basit kurallara uyun. Örneğin, şunu yazabiliriz:


</div>


```python
hello = "my own version of hello"
print(hello)
```


<div class="mw-translate-fuzzy">

Gördünüz mü? şimdi merhaba artık tanımsız bir kelime değil. Ya, kötü şansla, Python\'da zaten var olan bir ismi seçersek? Dizimizi \"print\" adı altında saklamak istediğimizi varsayalım:


</div>


```python
myVariable = "hello"
print(myVariable)
myVariable = "good bye"
print(myVariable)
```


<div class="mw-translate-fuzzy">

MyVariable\'ın değerini değiştirdik. Ayrıca değişkenleri de kopyalayabiliriz:


</div>


```python
var1 = "hello"
var2 = var1
print(var2)
```


<div class="mw-translate-fuzzy">

Değişkenlerinize anlamlı adlar vermenin önemli olduğunu unutmayın. Bir süre sonra \"a\" isimli değişkeninizin neyi temsil ettiğini hatırlamayacaksınız. Fakat eğer ismini verdiyseniz, örneğin myWelcomeMessage, amacını kolayca hatırlarsınız. Ayrıca, kodunuz kendi kendini belgelemeye bir adım daha yakın.


</div>


<div class="mw-translate-fuzzy">

Harf boyutu çok önemli. myVariable, myvariable ile aynı değildir; büyük / küçük harf farkı **v**. *print myvariable* yazarsanız, tanımlanmayan bir hatayla geri dönecektir.


</div>

[top](#top.md)

## Sayılar


<div class="mw-translate-fuzzy">

Elbette, programlamanın yalnızca metin dizeleri için değil, her türlü verinin ve özellikle sayıların işlenmesinde yararlı olduğunu bilmelisiniz. Bir şey önemlidir, Python ne tür verilerle uğraştığını bilmelidir. Merhaba örneğimizde, print komutunun \"merhaba\" dizgimizi tanıdığını gördük. Bunun nedeni, \" kullanarak, özellikle baskı komutunun bundan sonra gelenlerin bir metin dizesi olduğunu söylemiş olmamızdır.


</div>


<div class="mw-translate-fuzzy">

Özel bir Python anahtar kelime türüyle bir değişkenin veri türünü her zaman kontrol edebiliriz:


</div>


```python
myVar = "hello"
type(myVar)
```


<div class="mw-translate-fuzzy">

Bize myVar\'ın içeriğinin Pyrhon jargonundaki string için kısa olan str olduğunu söyleyecektir. Tam sayı ve değişken sayılar gibi diğer temel veri türlerimiz de vardır


</div>


```python
firstNumber = 10
secondNumber = 20
print(firstNumber + secondNumber)
type(firstNumber)
```


<div class="mw-translate-fuzzy">

Bu çok daha ilginç, değil mi? Şimdi güçlü bir hesap makinemiz var! Ne kadar iyi çalıştığına bakın, Python 10 ve 20\'nin tam sayı olduğunu biliyor. Böylece \"int\" olarak depolanırlar ve Python onlarla tamsayılarla yapabileceği her şeyi yapabilir. Bunun sonuçlarına bakın:


</div>


```python
firstNumber = "10"
secondNumber = "20"
print(firstNumber + secondNumber)
```


<div class="mw-translate-fuzzy">

Gördünüz mü? Python\'u iki değişkenimizin sayı değil, sadece metin parçaları olduğunu düşünmeye zorladık. Python iki parçayı bir araya getirebilir, ancak toplamı bulmaya çalışmaz. Fakat biz tamsayılardan bahsediyorduk. Kayan noktalı sayılar da vardır. Fark, tam sayıların ondalık bölüm içermemesi, kayan noktalı sayıların ise ondalık bölüm içermesidir:


</div>


```python
var1 = 13
var2 = 15.65
print("var1 is of type ", type(var1))
print("var2 is of type ", type(var2))
```


<div class="mw-translate-fuzzy">

Int ve Floats birlikte sorunsuzca karıştırılabilir:


</div>


```python
total = var1 + var2
print(total)
print(type(total))
```


<div class="mw-translate-fuzzy">

Elbette hepsi ondalık sayıdır, değil mi? Sonra Python otomatik olarak sonucun bir kayan noktalı sayı olduğuna karar verdi. Bunun gibi bazı durumlarda, Python hangi tipin kullanılacağına otomatik olarak karar verir. Diğer durumlarda değil. Örneğin:


</div>


```python
varA = "hello 123"
varB = 456
print(varA + varB)
```


<div class="mw-translate-fuzzy">

Bu bize bir hata verecektir, varA bir dizedir ve varB bir int\'dir ve Python ne yapacağını bilemez. Ancak, Python\'u türler arasında dönüştürmeye zorlayabiliriz:


</div>


```python
varA = "hello"
varB = 123
print(varA + str(varB))
```


<div class="mw-translate-fuzzy">

Şimdi her ikisi de dizgedir, işlem çalışır! Baskı sırasında varB\'yi \"dizeledik\", ancak varB\'nin kendisini değiştirmediğimizi unutmayın. VarB\'yi kalıcı olarak bir dizgeye çevirmek isteseydik, bunu yapmamız gerekirdi:


</div>


```python
varB = str(varB)
```


<div class="mw-translate-fuzzy">

İsterseniz int () ve float () işlevini int\'ye dönüştürmek için int () ve float () işlevini de kullanabiliriz:


</div>


```python
varA = "123"
print(int(varA))
print(float(varA))
```


<div class="mw-translate-fuzzy">

Bu bölümde print komutunu birkaç şekilde kullandığımızı fark etmiş olmalısınız. Değişkenleri, toplamları, virgülle ayrılmış birçok şeyi ve hatta type () gibi diğer Python komutlarının sonuçlarını bastık. Şu iki emri yerine getirdiğini de farkettiniz,


</div>


```python
type(varA)
print(type(varA))
```


<div class="mw-translate-fuzzy">

tam olarak aynı sonucu verir. Çünkü biz yorumlayıcıdayız ve her şey otomatik olarak basılıyor. Yorumlayıcı dışında çalışan daha karmaşık programlar yazdığımızda, otomatik olarak yazdırılmazlar, bu yüzden print komutunu kullanmamız gerekir. Şu andan itibaren, burada kullanmayı bırakalım, daha hızlı olacak. Böylece basitçe şunu yazabiliriz:


</div>


```python
myVar = "hello friends"
myVar
```

[top](#top.md)

## Listeler


<div class="mw-translate-fuzzy">

Bir başka ilginç veri tipi de bir liste. Bir liste sadece başka bir veri topluluğudur. \"\" Kullanarak bir metin dizesini tanımladığımız şekilde, \[\] kullanarak bir liste tanımlarız:


</div>


```python
myList = [1, 2, 3]
type(myList)
myOtherList = ["Bart", "Frank", "Bob"]
myMixedList = ["hello", 345, 34.567]
```


<div class="mw-translate-fuzzy">

Herhangi bir tür veri içerebileceğini görüyorsunuz. Listeler çok faydalıdır çünkü değişkenleri birlikte gruplayabilirsiniz. Daha sonra o gruptaki her türlü şeyi yapabilirsiniz; örneğin, onları sayarak:


</div>


```python
len(myOtherList)
```


<div class="mw-translate-fuzzy">

veya listedeki bir öğeyi almak:


</div>


```python
myName = myOtherList[0]
myFriendsName = myOtherList[1]
```


<div class="mw-translate-fuzzy">

en () komutu bir listedeki toplam öğe sayısını döndürürken, listedeki \"konumları\" 0 ile başlar. Listedeki ilk öğe her zaman 0 konumunda, yani myOtherList \"Bob\" da 2. konumda olacaksınız. Listelerle çok daha fazlasını yapabiliriz, içerikleri sıralama, öğeleri kaldırma veya ekleme gibi [1](http://www.diveintopython.net/native_data_types/lists.html) adresini okuyabilirsiniz.


</div>


<div class="mw-translate-fuzzy">

Komik ve ilginç bir şey: bir metin dizesi karakter listesine çok benzer! Bunu yapmayı deneyin:


</div>


```python
myvar = "hello"
len(myvar)
myvar[2]
```


<div class="mw-translate-fuzzy">

Genellikle, listelerde yapabileceğinizi dizelerle de yapabilirsiniz. Aslında hem listeler hem de diziler dizilerdir.


</div>


<div class="mw-translate-fuzzy">

Dizeler, ints, floats ve listeler dışında, [sözlükleri](http://www.diveintopython.net/native_data_types/index.html#d0e5174) gibi daha yerleşik veri türleri vardır veya kendi veri türlerinizi bile oluşturabilirsiniz [sınıfları](http://www.freenetpages.co.uk/hp/alan.gauld/tutclass.htm) ile.


</div>

[top](#top.md)

## Girinti


<div class="mw-translate-fuzzy">

Listelerin büyük ve harika bir kullanımı da, içinde gezinmek ve her öğeyle bir şeyler yapmaktır. Örneğin şuna bakın:


</div>


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
for dalton in alldaltons:
    print(dalton + " Dalton")
```


<div class="mw-translate-fuzzy">

Listemiz boyunca \"for \... in \...\" komutunu kullanarak yineledik (programlama jargonu) ve her bir öğe için bir şeyler yaptık. Özel sözdizimine dikkat edin: \'\' \'için\' \'\' komutu \'\' \':\' \'ile sonlanır ve aşağıdakilerin birden fazla komuttan birinin bir bloğu olacağını belirtir. Tercümanda, biten komut satırına girdikten hemen sonra: komut istemi \... olarak değişecektir, bu da Python\'un iki nokta üst üste (:) son satırın gerçekleştiğini ve daha fazlasının geldiğini bildiği anlamına gelir.


</div>


<div class="mw-translate-fuzzy">

Python, for \... operasyonunun içinde bir sonraki satırın kaç tanesinde yürütüleceğini nasıl bilecek? Bunun için Python girintiyi kullanır. Yani, bir sonraki satırınız hemen başlamayacak. Onlara bir boşlukla ya da birkaç boşlukla ya da bir sekmeyle ya da birkaç sekmeyle başlayacaksınız. Diğer programlama dilleri, her şeyi parantez içine koymak vb. Gibi diğer yöntemleri kullanır. Sonraki satırlarınızı \'\' \'aynı\' \'\' girintiyle yazdığınız sürece for-in bloğunun bir parçası olarak kabul edilirler. Bir satıra 2 boşlukla, bir başkasını da 4 ile başlarsanız, bir hata olacaktır. İşiniz bittiğinde, girintisiz başka bir satır yazın veya for-in bloğundan geri dönmek için Enter tuşuna basın


</div>


<div class="mw-translate-fuzzy">

Girinti kullanışlıdır, çünkü programın okunabilirliğine yardımcı olur. Büyük girintiler kullanırsanız (örneğin, boşluklar yerine sekmeler kullanın), büyük bir program yazdığınızda neyin içinde yürütüldüğünün net bir görüntüsünü görürsünüz. For-in dışındaki komutların da girilen kod bloklarını içerebileceğini göreceğiz.


</div>


<div class="mw-translate-fuzzy">

For-in komutları, bir defadan fazla yapılması gereken birçok şey için kullanılabilir. Örneğin, range () komutuyla birleştirilebilir:


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

(Kod örneklerini Kopyalama ve Yapıştırma yoluyla bir yorumlayıcı da çalıştırıyorsanız, önceki metin bloğunun bir hata vereceğini göreceksiniz. Bunun yerine, girintili bloğun sonuna, yani satırın sonuna \'\' toplamı kopyalayın = toplam sayı \'\' ve ardından yorumlayıcıya yapıştırın. Yorumlayıcı da üç nokta istemi kaybolup kod çalıştırılana kadar bir  basın. Sonra son iki satırı yorumlayıcıya kopyalayın, ardından bir veya daha fazla  cevap görünmelidir.)


</div>


<div class="mw-translate-fuzzy">

Eğer yorumlayıcıya **help(range)** yazarsanız şunu görürsünüz: 
```python
range(...)
    range(stop) -> list of integers
    range(start, stop[, step]) -> list of integers
``` Burada köşeli parantez isteğe bağlı bir parametreyi gösterir. Ancak hepsinin tamsayı olması bekleniyor. Aşağıda, range parametrelerini int () kullanarak bir tam sayı olmaya zorlayacağız.


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

Veya bunun gibi daha karmaşık şeyler:


</div>


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
for n in range(4):
    print(alldaltons[n], " is Dalton number ", n)
```


<div class="mw-translate-fuzzy">

Range () komutunun ayrıca, 0 ile başlayan (başlangıç numarasını belirtmezseniz) ve son numarasının belirttiğiniz bitiş numarasından daha az olacağını tuhaf bir özelliğe sahip olduğunu görürsünüz. Bu elbette diğer Python komutları ile iyi çalışır. Örneğin:


</div>


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
total = len(alldaltons)
for n in range(total):
    print(alldaltons[n])
```


<div class="mw-translate-fuzzy">

Girintili blokların bir başka ilginç kullanımı if komutudur. Bir kod bloğunu yalnızca belirli bir koşul karşılandığında çalıştırırsa, örneğin:


</div>


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
if "Joe" in alldaltons:
    print("We found that Dalton!!!")
```


<div class="mw-translate-fuzzy">

Elbette bu her zaman ilk cümleyi yazdıracak, ancak ikinci satırı değiştirmeyi deneyin:


</div>


```python
if "Lucky" in alldaltons:
```


<div class="mw-translate-fuzzy">

Sonra hiçbir şey basılmaz. Ayrıca başka bir ifade de belirtebiliriz: ifadesi:


</div>


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
if "Lucky" in alldaltons:
    print("We found that Dalton!!!")
else:
    print("Such Dalton doesn't exist!")
```

[top](#top.md)

## Fonksiyonlar


<div class="mw-translate-fuzzy">

Çok az [standart Python komutları](http://docs.python.org/reference/lexical_analysis.html#identifiers) vardır. Python\'un şu anki versiyonunda, yaklaşık 30 tane var ve biz zaten birkaç tanesini biliyoruz. Ama kendi komutlarımızı icat edip edemeyeceğimizi hayal edin? Yapabiliriz ve bu son derece kolay. Aslında, Python kurulumunuza ekleyebileceğiniz çoğu ek modül tam da bunu yapar, kullanabileceğiniz komutları ekler. Python\'daki özel bir komut fonksiyon olarak adlandırılır ve şöyle yapılır:


</div>


```python
def printsqm(myValue):
    print(str(myValue) + " square meters")

printsqm(45)
```


<div class="mw-translate-fuzzy">

Son derece basit: def () komutu yeni bir fonksiyon tanımlar. Ona bir isim verin ve parantez içinde fonksiyonumuzda kullanacağımız argümanları tanımlayın. Bağımsız değişkenler, işleve iletilecek verilerdir. Örneğin, len () komutuna bakın. Sadece len () yazarsanız, Python size bir argüman gerektirdiğini söyleyecektir. Yani, len () bir şey istiyorum, değil mi? Sonra, örneğin, len (myList) yazacak ve myList\'in uzunluğunu alacaksınız. MyList, len () fonksiyonuna ilettiğiniz bir argümandır. Len () işlevi, kendisine geçenlerle ne yapılacağını bildiği şekilde tanımlanır. Burada yaptığımız gibi.


</div>


<div class="mw-translate-fuzzy">

\"MyValue\" adı herhangi bir şey olabilir ve yalnızca işlev içinde kullanılacaktır. Bu sadece argümana verdiğiniz bir isimdir, onunla bir şeyler yapabilirsiniz, ancak fonksiyona kaç tane argüman bekleneceğini de söyler. Örneğin, bunu yaparsanız:


</div>


```python
printsqm(45, 34)
```


<div class="mw-translate-fuzzy">

Bir hata olacak. Fonksiyonumuz sadece bir argüman alacak şekilde programlandı, fakat iki, 45 ve 34 aldı. Bunun yerine şöyle bir şey yapabiliriz:


</div>


```python
def sum(val1, val2):
    total = val1 + val2
    return total

myTotal = sum(45, 34)
```


<div class="mw-translate-fuzzy">

İki argüman alan, toplayan ve bu değeri veren bir fonksiyon yaptık. Bir şeyi döndürmek çok yararlıdır, çünkü sonucunu myTotal değişkeninde saklamak gibi bir şey yapabiliriz. Elbette, biz tercüman olduğumuz ve her şey basıldığı için:


</div>

[top](#top.md)

## Modüller


<div class="mw-translate-fuzzy">

Şimdi Python\'un nasıl çalıştığı hakkında iyi bir fikrimiz olduğuna göre, son bir şeye ihtiyacımız var: Dosya ve modüllerle nasıl çalışılır


</div>


<div class="mw-translate-fuzzy">

Şimdiye kadar, Python komutlarını yorumlayıcıya satır satır yazdık, değil mi? Birlikte birkaç satır yazabilseydik ve hepsini bir kerede yürütebilseydik? Kesinlikle daha karmaşık şeyler yapmak için çok zor olurdu. Ve biz de işimizi kurtarabiliriz. Bu da son derece kolaydır. Basitçe bir metin editörü (Windows not defteri, Linux gedit, emacs veya vi gibi) açın ve tüm Python kodlarınızı, yorumlayıcıya girdiğiniz şekilde, girintilerle vb. Yazın. Ardından, bu dosyayı bir yere kaydedin. , tercihen bir .py uzatma ile. İşte bu, tam bir Python programınız var. Tabii ki, not defterinden çok daha iyi editörler var, ama sadece size bir Python programının bir metin dosyasından başka bir şey olmadığını göstermektir.


</div>


<div class="mw-translate-fuzzy">

Python\'un bu programı yürütmesini sağlamak için yüzlerce yol vardır. Pencerelerde, dosyayı sağ tıklayın, Python ile açın ve çalıştırın. Ancak Python tercümandan da çalıştırabilirsiniz. Bunun için tercümanın .py programınızın nerede olduğunu bilmesi gerekir. FreeCAD\'de en kolay yol, programınızı FreeCAD\'in Python yorumlayıcısının FreeCAD\'in bin klasörü veya Mod klasörlerinden herhangi biri gibi varsayılan olarak bildiği bir yere yerleştirmektir. (Linux\'ta muhtemelen / home /  /.FreeCAD/Mod dizininiz var, hadi metin dosyasını koyacağımız komut dosyalarına bir alt dizin ekleyelim.) Bunun gibi bir dosya yazdığımızı varsayalım:


</div>


```python
def sum(a,b):
    return a + b

print("myTest.py succesfully loaded")
```


<div class="mw-translate-fuzzy">

ve bunu FreeCAD/bin dizinine myTest.py olarak kaydedelim (veya Linux\'ta /home/ /.FreeCAD/Mod/scripts.) Şimdi FreeCAD\'i başlatalım ve yorumlayıcı penceresinde şunu yazın:


</div>


```python
import myTest
```


<div class="mw-translate-fuzzy">

.py uzantısı olmadan. Bu, tıpkı yorumlayıcıya yazdığımız gibi, dosyanın içeriğini satır satır yürütür. Toplam işlevi oluşturulacak ve mesaj yazdırılacaktır. Büyük bir fark var: import komutu sadece dosyalarımızda yazılan programları yürütmek için değil, aynı zamanda içindeki fonksiyonları yüklemek için de yapılır, böylece yorumlayıcı da kullanılabilir hale gelirler. Bizimki gibi fonksiyonlar içeren dosyalara modüller denir.


</div>


<div class="mw-translate-fuzzy">

Normal olarak, yorumlayıcıya bir sum () işlevi yazdığımızda, onu sadece şöyle uygularız:


</div>


```python
sum(14, 45)
```


<div class="mw-translate-fuzzy">

Daha önce yaptığımız gibi. Sum () fonksiyonumuzu içeren bir modülü içe aktardığımızda, sözdizimi biraz farklıdır. Şöyle yaparız:


</div>


```python
myTest.sum(14, 45)
```


<div class="mw-translate-fuzzy">

Yani, modül bir \"konteyner\" olarak içe aktarılır ve tüm fonksiyonları içeridedir. Bu son derece kullanışlıdır, çünkü birçok modülü içe aktarabilir ve her şeyi iyi organize edebiliriz. Yani, temelde, her yerde **something.somethingElse**\', arada bir nokta varken, bu **somethingElse** **something** içindedir demektir.


</div>


<div class="mw-translate-fuzzy">

Sum() fonksiyonumuzu doğrudan ana yorumlayıcı alanına da aktarabiliriz, şöyle:


</div>


```python
from myTest import *
sum(12, 54)
```


<div class="mw-translate-fuzzy">

Temel olarak tüm modüller böyle davranır. Bir modülü içe aktarırsanız, işlevlerini kullanabilirsiniz: module.function (argument). Neredeyse tüm modüller bunu yapar: yorumlayıcı da veya kendi Python modüllerinde kullanabileceğiniz işlevleri, yeni veri türlerini ve sınıflarını tanımlar, çünkü hiçbir şey sizin modülünüzün içine diğer modülleri içe aktarmanızı engellemez!


</div>


<div class="mw-translate-fuzzy">

Son derece yararlı bir şey. Hangi modüllere sahip olduğumuzu, hangi fonksiyonların içinde olduğunu ve nasıl kullanılacağını (yani, ne tür argümanlara ihtiyaç duyduklarını) nasıl biliyoruz? Python\'un bir help () işlevi olduğunu zaten gördük. Şunu yapın:


</div>


```python
help("modules")
```


<div class="mw-translate-fuzzy">

Mevcut tüm modüllerin bir listesini verir. Şimdi etkileşimli yardımdan çıkmak ve bunlardan herhangi birini almak için q yazabiliriz. Hatta dir () komutuyla içeriğine göz atabiliriz.


</div>


```python
import math
dir(math)
```


<div class="mw-translate-fuzzy">

Matematik modülünde yer alan tüm fonksiyonları ve ayrıca \_\_doc\_\_, \_\_dosya\_\_, \_\_name\_\_ adında garip şeyleri göreceğiz. \_\_Doc\_\_ son derece kullanışlıdır, bir belge metnidir. (İyi yapılmış) modüllerin her işlevi, nasıl kullanılacağını açıklayan bir \_\_doc \_\_ işlevine sahiptir. Örneğin, matematik modülünün yanında bir sin işlevi olduğunu görüyoruz. Nasıl kullanılacağını bilmek ister misiniz?


</div>


```python
print(math.sin.__doc__)
```


<div class="mw-translate-fuzzy">

(Açık olmayabilir, ancak dokümanın her iki tarafında iki alt çizgi karakter vardır.)


</div>


<div class="mw-translate-fuzzy">

Ve son olarak son bir küçük tüyo: Yeni veya mevcut bir modül üzerinde çalışırken, dosya uzantısını py gibi bir ile değiştirmek en iyisidir: myModule.FCMacro =\> myModule.py. Sık sık test etmek istiyoruz, böylece yukarıdaki gibi yükleyeceğiz.


</div>


```python
import importlib
importlib.reload(myTest)
```


<div class="mw-translate-fuzzy">

Bununla birlikte, iki alternatif vardır: Bir makroda Python\'un exec veya execfile işlevlerini kullanın.


</div>


```python
exec(open("C:/PathToMyMacro/myMacro.FCMacro").read())
```

[top](#top.md)

## FreeCAD ile Başlamak 


<div class="mw-translate-fuzzy">

Şimdi Python\'un nasıl çalıştığı hakkında iyi bir fikriniz olduğunu ve FreeCAD\'in neler sunabileceğini keşfetmeye başlayabileceğinizi düşünüyorum. FreeCAD\'in Python fonksiyonları farklı modüllerde iyi düzenlenmiştir. FreeCAD\'i başlattığınızda bazıları zaten yüklendi (içe aktarıldı). Yani, sadece yap


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

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Python Code{{\#translation:}}](Category:Python_Code.md)
