## 1. 使用sed替换字符串

### 1.1 简单字符串替换

假设存在一个文件`old.txt`，它的内容如下：

```text
me
good
night
yes
```

下面来看一下如何使用`sed`命令把单词`night`替换为`day`。

很简单，我们在终端中运行下面的命令即可实现：

```text
sed s/night/day/ < old.txt > new.txt
```

最后我们运行`cat new.txt`命令来查看一下`new.txt`文件中的内容：

```text
me
good
day
yes
```

可见单词`night`已经被替换为`day`。

### 1.2 替换所有匹配的字符串

假设我们有一个文件`a.txt`，其内容如下：

```text
one two three, one two three
four three two one
one hundred
```

现在我们要把该文件小写的单词`one`全部替换为大写的单词`ONE`。

我们在学习过[1.1简单字符串替换](#11)后，可能会写出下面的命令：

```text
sed 's/one/ONE/' < a.txt > b.txt
```

上面这条命令能实现我们的需求吗？我们先来执行该命令，然后查看`b.txt`中的内容：

```text
ONE two three, one two three
four three two ONE
ONE hundred
```

经过观察我们发现并不是所有的`one`都被替换为了`ONE`，在第一行中，只有第一次出现的`one`被替换为了`ONE`，第二次出现的`one`并没有被替换掉，对比如下：

替换之前的第一行：

```text
one two three, one two three
```

替换之后的第一行：

```text
ONE two three, one two three
```

!!! note "上述命令不能完全把one替换为ONE的原因"
    `sed`是以行为单位对文件进行处理的，而且默认只会替换一行中第一个匹配的值。

那么如何实现我们的需求？很简单，我们只要命令进行一点点修改，添加一个标志位`g`表示替换所有匹配的字符串，修改后的命令如下：

```text
sed 's/one/ONE/g' < a.txt > b.txt
```

然后执行命令`cat b.txt`查看结果，可见所有的`one`已被替换为`ONE`：

```text
ONE two three, ONE two three
four three two ONE
ONE hundred
```
