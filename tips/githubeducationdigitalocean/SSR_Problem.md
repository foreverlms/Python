## 使用SSR被谷歌识别为机器人而限制访问google scholar
确保你的VPS允许了ipv6访问，找到google scholar的ipv6地址（[google scholar host查询](https://raw.githubusercontent.com/lennylxx/ipv6-hosts/master/hosts)） ，在你的VPS的`/etc/hosts`上添加下列：
```
#add these below to the end of your /etc/host
## Scholar 学术搜索
2404:6800:4008:c06::be scholar.google.com
2404:6800:4008:c06::be scholar.google.com.hk
2404:6800:4008:c06::be scholar.google.com.tw
2401:3800:4001:10::101f scholar.google.cn #www.google.cn
```
PS:以上地址会变动，请已上面网址里的host为准。

## PAC txt 
[pac.txt](https://raw.githubusercontent.com/coderchaser/LearningPython/master/tips/githubeducationdigitalocean/pac.txt)
