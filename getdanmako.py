'''
Author: Komoriii
email: c2VuZXZhbkBmb3htYWlsLmNvbQ==
'''
import requests
from bs4 import BeautifulSoup


# bilibili danmaku api "https://comment.bilibili.com/xxxxxxxx.xml"
DANMAKU_API = "https://comment.bilibili.com/{0}.xml"
UA_list = []
cids = {}
danmaku_list = []
random.seed()

class Danmaku_pool():
    def __init__(self):
        self.pool = []
    
    def append_dm(self, dm_list):
        self.pool.append(dm_list)

    def print(self):
        print(self.pool)
    
    def save_to_txt(self, filename):
        f = open(filename, 'w', encoding='utf-8')
        for i in self.pool:
            for line in i:
                # change to utf encoding, otherwise this cause an error
                f.writelines(line)
        f.close()

# read all of the User-Agents
def read_lines(filename):
    list_temp = []
    f = open(filename, 'r')
    for line in f:
        list_temp.append(line)
    return list_temp

def get_danmaku1v(cid):
    r = requests.get(DANMAKU_API.format(cid))
    raw_file = r.content
    danmaku_1v = []
    formated_file = BeautifulSoup(raw_file, "lxml")
    for dm in formated_file.find_all('d'):
        danmaku_1v.append(dm.get_text())
    return danmaku_1v


def main():
    danmaku_pool = Danmaku_pool()
    cids = set(read_lines('cids.txt'))
    for c in cids:
        danmaku_pool.append_dm(get_danmaku1v(c))
    danmaku_pool.save_to_txt('data/danmaku_sv.txt')

if __name__ == '__main__':
    main()