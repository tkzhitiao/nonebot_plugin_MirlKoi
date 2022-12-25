import asyncio
import requests
from nonebot.adapters.onebot.v11.message import Message  # 用来发cq码
from nonebot.plugin import on_command

quanbu = 'https://iw233.cn/api.php?sort=random'  # 随机壁纸
quanbuwusetu = 'https://iw233.cn/api.php?sort=iw233'  # 无色图随机壁纸
bizhituijian = 'https://iw233.cn/api.php?sort=top'  # 壁纸推荐
yingfa = 'https://iw233.cn/api.php?sort=yin'  # 银发
shouer = 'https://iw233.cn/api.php?sort=cat'  # 兽耳
xingkong = 'https://iw233.cn/api.php?sort=xing'  # 星空
shupingbizhi = 'https://iw233.cn/api.php?sort=mp'  # 竖屏壁纸
hengping = 'https://iw233.cn/api.php?sort=pc'  # 横屏壁纸

random = on_command('全部随机', priority=50)
iw233 = on_command('随机', priority=50)
top = on_command('推荐', priority=50)
yin = on_command('银发', priority=50)
cat = on_command('兽耳', priority=50)
xing = on_command('星空', priority=50)
mp = on_command('竖屏', priority=50)
pc = on_command('横屏', priority=50)

i = []  # 用来记录触发次数
i2 = []  # 用来记录过快请求的次数


def get(x):
    if len(i) == 0:  # 限制访问频率防止IP被锁
        r = requests.get(x, allow_redirects=False)  # 获取跳转图片前响应头的Location的值也就是图片地址
        i.append(1)  # 记录访问次数
        if r.status_code == 302:  # 判断响应码是否正常
            url = r.headers['Location']  # 图片地址
            return f'[CQ:image,file={url}]'  # 发送图片
        else:
            return '获取图片出错'
    else:
        i2.append(1)  # 记录过快访问次数
        return '请求过快请间隔1秒'


@random.handle()
async def _():
    if len(i2) == 0:  # 判断是否是过快的访问
        await random.send(Message(get(quanbu)))
        # 发送get返回的字符串
        await asyncio.sleep(1)
        if len(i) != 0:
            i.remove(1)  # 清除请求次数
        # 限制频率
    else:
        await asyncio.sleep(1)
        i2.clear()  # 清除过快请求次数


@iw233.handle()
async def _():
    if len(i2) == 0:
        await iw233.send(Message(get(quanbuwusetu)))
        # 发送get返回的字符串
        await asyncio.sleep(1)
        if len(i) != 0:
            i.remove(1)
        # 限制频率
    else:
        await asyncio.sleep(1)
        i2.clear()


@top.handle()
async def _():
    if len(i2) == 0:
        await top.send(Message(get(bizhituijian)))
        # 发送get返回的字符串
        await asyncio.sleep(1)
        if len(i) != 0:
            i.remove(1)
        # 限制频率
    else:
        await asyncio.sleep(1)
        i2.clear()


@yin.handle()
async def _():
    if len(i2) == 0:
        await yin.send(Message(get(yingfa)))
        # 发送get返回的字符串
        await asyncio.sleep(1)
        if len(i) != 0:
            i.remove(1)
        # 限制频率
    else:
        await asyncio.sleep(1)
        i2.clear()


@cat.handle()
async def _():
    if len(i2) == 0:
        await cat.send(Message(get(shouer)))
        # 发送get返回的字符串
        await asyncio.sleep(1)
        if len(i) != 0:
            i.remove(1)
        # 限制频率
    else:
        await asyncio.sleep(1)
        i2.clear()


@xing.handle()
async def _():
    if len(i2) == 0:
        await xing.send(Message(get(xingkong)))
        # 发送get返回的字符串
        await asyncio.sleep(1)
        if len(i) != 0:
            i.remove(1)
        # 限制频率
    else:
        await asyncio.sleep(1)
        i2.clear()


@mp.handle()
async def _():
    if len(i2) == 0:
        await mp.send(Message(get(shupingbizhi)))
        # 发送get返回的字符串
        await asyncio.sleep(1)
        if len(i) != 0:
            i.remove(1)
        # 限制频率
    else:
        await asyncio.sleep(1)
        i2.clear()


@pc.handle()
async def _():
    if len(i2) == 0:
        await pc.send(Message(get(hengping)))
        # 发送get返回的字符串
        await asyncio.sleep(1)
        if len(i) != 0:
            i.remove(1)
        # 限制频率
    else:
        await asyncio.sleep(1)
        i2.clear()
