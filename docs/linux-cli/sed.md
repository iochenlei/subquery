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
