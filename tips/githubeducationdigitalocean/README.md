# 利用Github Education 优惠来购买VPS搭建SSR科学上网
[本文已同步至Github](https://github.com/coderchaser/LearningPython/blob/master/tips/githubeducationdigitalocean)
## Preliminary requirements
* Github Education认证
* Paypal账号或者可以进行外币交易的信用卡
* Digitalocean 或者Vultr 邀请注册
	* 我的digitalocean邀请链接：[Digitalocean](https://m.do.co/c/9f3a141bb280),点击链接进行注册，你我账户上都会被赠送10$，类似于支付宝互相扫红包。
	* 我的vultr邀请链接：[Vultr](https://www.vultr.com/?ref=7307591),点击链接进行注册，你我账户上都会被赠送10$，类似于支付宝互相扫红包。PS:使用vultr购买VPS不会有下文介绍的Github Education优惠，我就不多说，都差不多。
* Droplet或Instance创建
* Putty、Xshell或者其他SSH登陆工具
* Shadowsocks配置

### Github Education认证
Github作为世界上最大的分布式代码托管网站，对于我们学生来讲真是送出了天大的优惠。它有一个Education Community用于传授学生们编程知识。这个项目有一个student developer pack（学生开发者大礼包）,里面很多东西用于软件开发。其中一个优惠是digitalocean 50$的兑换码。50$是什么概念？折合人民币将近323元！上面最便宜的VPS只需5$一个月，这意味着你可以至少免费用10个月VPS。可能我说了这么多很多同学还不了解什么是VPS。下面来介绍：
> VPS，Virtual private server，虚拟专用服务器，是指通过虚拟化技术在独立服务器中运行的专用服务器。每个使用VPS技术的虚拟独立服务器拥有各自独立的公网IP地址、操作系统、硬盘空间、内存空间、CPU资源等，还可以进行安装程序、重启服务器等操作，与运行一台独立服务器完全相同。

这里很明显了，凭咱们自己的财力肯定搭不了服务器，只能租用别人的服务器，而digitalocean和vultr都是VPS提供商，他们提供不同配置的VPS供人们租用来建网站、计算大型项目，以及我们最重要的目的：科学上网。国内也有VPS，像阿里云，对学生也有优惠，不过对科学上网不怎么支持。
回到正题：**如何申请github education pack呢？**

1. 去[学校电子邮局](http://newmail.shu.edu.cn/)申请带edu后缀的邮箱。点击右上角邮箱申请即可。（非上大的同学可以去自己学校电子邮局申请）。
2. 注册github账号，并把刚才注册的学校邮箱添加到github邮箱列表中。
3. 点击[Github Education](https://education.github.com/),点击`Get the Pack`按钮，获取礼包。照着流程走就行了。
4. 认证学生身份一般需要一段时间，成功之后，你可以在pack列表里找到如下图所示的digitalocean兑换码（马赛克部分）。![Your Code](https://github.com/coderchaser/LearningPython/blob/master/tips/githubeducationdigitalocean/digitalocean.png)。
5. 按照我的邀请链接注册并验证支付能力后即可兑换50$。

### Paypal账号或者可以进行外币交易的信用卡
因为digitalocean在里进行注册时会进行邮箱和支付能力双重认证，所以你要么在注册后添加信用卡要么使用paypal充值5美元。这之后才能享受邀请码链接注册优惠。我没有信用卡，Paypal里面可以添加工商银行的借记卡，我就利用这种方式充值了5美元（貌似农业银行的不行）。Paypal注册我就不赘述了。如果你和我一样，最后digitalocean账户上有多少余额呢？一共是：

**5（自己充值的）+10（邀请链接注册赠送）+50（Github赠送=65$** 

这是最划算的考量（*勤俭持家*）了！
### Droplet或Instance创建
现在账户上有了65$，瞬间感觉土豪了呢！！那就新建一个droplet吧。至于为什么叫droplet？因为网站叫Digitalocean啊！妙不妙！
创建Droplet就按照GIF所示。
![create_droplet.gif](https://github.com/coderchaser/LearningPython/blob/master/tips/githubeducationdigitalocean/droplet_creation.gif)

1. 选择Create->Droplets
2. 选择系统为Centos,版本6.9X64，当然你可以选用别的系统，只要你会用。不要选Windows，我不会配置这个。
3. Size选择最便宜的，个人够用了。
4. 服务器所在区域我选的是美国，你懂的。
5. 我勾选了允许IPV6访问，可能我以后会建自己的网站吧。看你自己情况。
6. 选择数量，我只需要一个就够了。然后设置主机名称。
7. 点击创建按钮，稍等一会问就会完成，服务器的地址、密码会发送至你的注册邮箱里，稍后我们会用到。

至此服务器创建完成，接下来我们来搭建SSR进行科学上网。
### Putty、Xshell或者其他SSH登陆工具
Putty是一款小巧的SSH远程登陆软件，我们用它来登陆刚才创建好的服务器。Putty下载链接：链接：https://pan.baidu.com/s/1eTFqxk2 密码：3zqz。
打开Putty后我们在红框处输入邮箱中收到的droplet IP地址。
![putty.png](https://github.com/coderchaser/LearningPython/blob/master/tips/githubeducationdigitalocean/putty.png)

端口不改，默认22。之后会出现窗口，第一行：
`login as:`，我们输入root，接着会让你输入密码，我们复制邮箱邮件收到的密码粘贴到putty中（粘贴直接右键即可）。粘贴后你不会看到任何效果，因为Linux哲学就是`没有回应就是最好的回应`，直接回车就好。初次登陆，digitalocean会要求你更改密码，重新设置密码就行。至此，我们成功地远程登陆了我们租用的服务器。
### Shadowsocks配置
>Shadowsocks----A secure socks5 proxy,designed to protect your Internet traffic.

本来Shadowsocks是一款代理软件，但是被天朝的大神们魔改之后，变成了一款fanqiang软件。Shadowsocks配置过程非常繁琐，对于我这种小白（没错，我其实也是小白）来说实在是太麻烦了，不过我follow的一位大神已经帮我们做好了[配置教程](http://miaomiaoai.cn/?p=1011)。按照这篇一键教程，大大精简了配置过程。大家在设置的过程中可以自己去决定shadowsocks的服务端配置，比如加密算法，混淆协议等，我现在用的是下面的规则，感觉有点慢，不过够我用了，之后我会研究一下shadowsocks，改善配置。谁知道规则怎么设置，请指教一下我，我的邮箱：codechaser@163.com。有谁对配置过程不清楚的也可以和我练习。
![shadowsocks.png](https://github.com/coderchaser/LearningPython/blob/master/tips/githubeducationdigitalocean/shadowcoks.PNG)

刚才是服务端的配置，现在我们在自己的PC上使用shadowsocks。它有不同版本，我用的是[ShadowsocksR-dotnet4.0](https://pan.baidu.com/s/1dP7UIq)。这是免安装版本。我们进去后选择`添加`来添加服务器。服务器IP是我们创建的droplet地址，端口的话如果你是按照上面那位大神教程做而且没有修改默认是2333，最后加密、协议、混淆按你配置的选。这个弄好之后，我们右键右下角的小飞机图标，选择启用系统代理，系统代理模式选择PAC模式，这样访问国内的网站不会走代理。PAC文件更新有多种途径，大家可以自己去baidu/google，我之后也会再对此进行介绍。
这个设置好之后，你就可以穿越高墙，直达世界了。***但是，高墙之外的不一定全是好的，甚至充斥着很多邪教、反动势力的言论，这时候如何做全在你自己。有民族自信心、有明辨是非的能力、有对美好明天的向往，相信大家都能查阅资料，投入到科研、进步的征途中。***
最后，认识我的可以来
>.---/../.-/-../../-./--./-..-/../.-/---/--.-/..-/-..../..../.-/---/.-../---/..-/....-/-----/-....

寝室找我，或者与我联系：codechaser@163.com。

----
一键更换Centos内核以安装锐速：

`wget --no-check-certificate https://blog.asuhu.com/sh/ruisu.sh bash ruisu.sh`

一键shadowsocks配置脚本：

`wget -N --no-check-certificate https://raw.githubusercontent.com/ToyoDAdoubi/doubi/master/ssr.sh && chmod +x ssr.sh && bash ssr.sh
`
