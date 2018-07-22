# 爬取klc首页 项目数据 Ywx

import urllib
import ssl
import csv
from urllib import request
from bs4 import BeautifulSoup


class GetBorrowInfo:
    def __init__(self, url):
        self.url = url
        self.html = ''
        self.borrow_data = []
        self.path = './klc_data.csv'

    """请求页面"""
    def get_html(self):
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        context = ssl._create_unverified_context()
        request = urllib.request.Request(self.url, headers=header)
        response = urllib.request.urlopen(request, context=context)
        self.html = response.read().decode('UTF-8')

    """解析并获取数据"""
    def get_data(self):
        soup = BeautifulSoup(self.html, 'html.parser')

        """获取项目个数"""
        borrow = soup.find_all('div', 'klc-invest-item')

        """获取项目编号"""
        borrow_nid = []
        for borrow_link in borrow:
            a = borrow_link.find_all('a')
            href = a[0]['href']
            borrow_nid.append(str(href[-11:]))

        """获取项目名称"""
        borrow_name = []
        borrow_name_div = soup.find_all('div', 'project-title')

        for name in borrow_name_div:
            borrow_name.append(name.text.replace(' ', ''))

        """获取项目历史收益率"""
        borrow_apr = []
        history_apr = soup.find_all('div', 'year-money')
        for his_apr in history_apr:
            apr = his_apr.find_all('p')
            apr = apr[1]
            borrow_apr.append(apr)

        """获取项目期限 项目金额"""
        borrow_period = []
        borrow_account = []
        project_info = soup.find_all('div', 'project-day')
        for pro in project_info:
            pro_data = pro.find_all('span')
            period = pro_data[0]
            account = pro_data[2]
            borrow_period.append(period)
            borrow_account.append(account)

        """获取项目投资金额及其占比"""
        borrow_tender = []
        borrow_now = []
        for tender_info in borrow:
            tender = tender_info.find_all('span')
            borrow_tender.append(tender[4])
            borrow_now.append(tender[5])

        """获取项目投资状态"""
        borrow_status = []
        borrow_status_div = soup.find_all('div', 'buy-button')
        for status in borrow_status_div:
            borrow_status.append(status.text.replace(' ', ''))

        """项目数据信息"""
        index = 0
        for name_txt in borrow_name:
            data = [
                borrow_nid[index],                            # 项目编号
                name_txt,                           # 项目名称
                borrow_apr[index].text.replace(' ', ''),      # 项目历史收益率
                borrow_period[index].text.replace(' ', ''),   # 项目期限
                borrow_account[index].text.replace(' ', ''),  # 项目金额
                borrow_tender[index].text.replace(' ', ''),   # 项目投资金额
                borrow_now[index].text.replace(' ', ''),      # 项目投资进度
                borrow_status[index]                          # 项目投资状态
            ]
            self.borrow_data.append(data)
            index += 1

    """写入文件"""
    def create_file(self, header=['项目编号', '项目名称', '历史收益率', '项目期限', '项目规模', '投资/总额', '投资进度', '投资状态']):

        with open(self.path, 'w', newline='', encoding='utf-8-sig') as file:
            write_file = csv.writer(file, 'excel')
            if header is not None:
                write_file.writerow(header)
            for row_data in self.borrow_data:
                write_file.writerow(row_data)
            print("数据写入文件成功！" + self.path)


url = 'https://www.58klc.com/'
borrow = GetBorrowInfo(url)
borrow.get_html()
borrow.get_data()
borrow.create_file()
