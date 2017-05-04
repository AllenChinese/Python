# 下载当当网指定页面的书名  
import urllib.request  
import gzip  
import re  
import time  
      
      
# 获取网页源码  
def get_html(url, timeout=10):  
    req = urllib.request.Request(url, headers=headers)  
    response = urllib.request.urlopen(req)  
    data = response.read()  
    # print('解压前大小：%.2f kb' % (len(data) / 1024)) # 默认单位是bytes字节  
    if response.info().get('Content-Encoding') == 'gzip':  
        data = gzip.decompress(data)  
    # print('解压后大小：%.2f kb' % (len(data) / 1024))  
    return data.decode('gbk')  
      
# 获取最大页数  
def get_max_page(html):  
    pages = max_page_re.findall(html)  
    pages = [int(x) for x in pages]  
    return max(pages)  
      
      
# 把书名列表保存到文件  
def save(names):  
    with open(savefile, 'a') as f:  
        f.write("\n".join(names).strip(" ")+"\n")  
      
# 秒-->时分秒  
def trans_time(sec):  
    hour = int(sec / 3600)  
    sec = sec % 3600  
    minute = int(sec / 60)  
    sec = sec % 60  
    return "%s小时 %s分 %s秒" % (hour, minute, sec)  
      
      
if __name__ == "__main__":      
    headers = {  
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",  
        "Accept-Encoding": "gzip, deflate, sdch",  # 要求服务器进行gzip压缩  
        "Upgrade-Insecure-Requests": "1",  
        "User-Agent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36"  
    }  
    url_pattern = r'http://promo.dangdang.com/subject.php?pm_id=1501519&tag_id=&sort=price_asc&province_id=137&p={0}'      
    savefile = r'F:\booknames.txt'  # 保存到此文件  
    book_name_re = re.compile(r'<p\sclass="pic">[^>]*?title="(.*?)"')  # 解析书名  
    max_page_re = re.compile(r'p=(\d+)"\s+class="page_num\s+ajax"') # 散析最大网页数  
      
    start = time.time()  
    i = 0  
    count = 0  
    while True:       
        i += 1     
        url = url_pattern.format(i)  
        html = get_html(url)  
        names = book_name_re.findall(html)  
        count += len(names)  
        max_page = get_max_page(html)          
        save(names)  
        print("已爬 %s 页，抓取 %s 个书名，一共 %s 页" % (i, count, max_page))  
        if i > max_page:  
            break  
    used_time = trans_time(time.time() - start)  
    print('抓取完成！\n耗时 %s\n请查看 %s' % (used_time, savefile))  