from bs4 import BeautifulSoup
import requests
from csv import writer
import pandas as pd 
from matplotlib import pyplot as plt 
import numpy as np 
user_num = input('Input how many users: ')
nnn = int(user_num)
aaa = []
i=0
user_id = print('Input user ids:')
while i < nnn :
    user_name = input()
    aaa.append(user_name)
    i+=1 
ddate = input('Input a date(dd/mm/yyyy) : ')
#aaa = ['soyeb_p_jim', 'TSN121', 'Ahasanul_Kabir_Rifat', 'sajin10', 'DiptoArchyes07', 'Zarif_Mustafa', 'Himel_Roy', 'Waseem_Mustak', 'RayhanSefat1332', 'dibbyo_roy', 'TheSurfer']
with open('scores.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['User','Date', 'Score', 'Solved']
    thewriter.writerow(header)
    for user in aaa:
        uurl = f"https://codeforces.com/submissions/{user}"
        html_text = requests.get(uurl).text
        soup = BeautifulSoup(html_text, 'lxml')
        page_num = soup.find_all('span', class_='page-index')[-1].text
        pagenum = int(page_num)
        score = 0
        solved_prob = 0
        page = 1
        ctt = 0
        cttt=0
        while page < pagenum and cttt==0:
            url = f"https://codeforces.com/submissions/{user}/page/{page}"
            resporse = requests.get(url).text
            sou = BeautifulSoup(resporse, 'lxml')
            for tr in sou.find_all('tr')[1:50]:
                tds = tr.find_all('td')
                date = ''
                final_date=''
                if tds[1].text.strip().split()[0][:3] == 'Jan':
                    date = tds[1].text.strip().split()[0][4:6] + '/' +'01' + tds[1].text.strip().split()[0][6:]
                elif tds[1].text.strip().split()[0][:3] == 'Feb':
                    date = tds[1].text.strip().split()[0][4:6] + '/' +'02' + tds[1].text.strip().split()[0][6:]
                elif tds[1].text.strip().split()[0][:3] == 'Mar':
                    date = tds[1].text.strip().split()[0][4:6] + '/' +'03' + tds[1].text.strip().split()[0][6:]
                elif tds[1].text.strip().split()[0][:3] == 'Apr':
                    date = tds[1].text.strip().split()[0][4:6] + '/' +'04' + tds[1].text.strip().split()[0][6:]
                elif tds[1].text.strip().split()[0][:3] == 'May':
                    date = tds[1].text.strip().split()[0][4:6] + '/' +'05' + tds[1].text.strip().split()[0][6:]
                elif tds[1].text.strip().split()[0][:3] == 'Jun':
                    date = tds[1].text.strip().split()[0][4:6] + '/' +'06' + tds[1].text.strip().split()[0][6:]
                elif tds[1].text.strip().split()[0][:3] == 'Jul':
                    date = tds[1].text.strip().split()[0][4:6] + '/' +'07' + tds[1].text.strip().split()[0][6:]
                elif tds[1].text.strip().split()[0][:3] == 'Aug':
                    date = tds[1].text.strip().split()[0][4:6] + '/' +'08' + tds[1].text.strip().split()[0][6:]
                elif tds[1].text.strip().split()[0][:3] == 'Sep':
                    date = tds[1].text.strip().split()[0][4:6] + '/' +'09' + tds[1].text.strip().split()[0][6:]
                elif tds[1].text.strip().split()[0][:3] == 'Oct':
                    date = tds[1].text.strip().split()[0][4:6] + '/' +'10' + tds[1].text.strip().split()[0][6:]
                elif tds[1].text.strip().split()[0][:3] == 'Nov':
                    date = tds[1].text.strip().split()[0][4:6] + '/' +'11' + tds[1].text.strip().split()[0][6:]
                elif tds[1].text.strip().split()[0][:3] == 'Dec':
                    date = tds[1].text.strip().split()[0][4:6] + '/' +'12' + tds[1].text.strip().split()[0][6:]
                time = int(tds[1].text.strip().split()[1][:2])+3
                if time>=24:
                    kk = int(date[:2])+1
                    if len(str(kk))==1:
                        pk = '0' + str(kk)
                    else:
                        pk = str(kk)
                    if date[3:5]=='01' and kk>31:
                        final_date = pk + '/02' + date[5:]
                    elif date[3:5]=='02' and kk>28:
                        final_date = pk + '/03'+date[5:]
                    elif date[3:5]=='03' and kk>31:
                        final_date = pk + '/04'+date[5:]
                    elif date[3:5]=='04' and kk>30:
                        final_date = pk + '/05'+date[5:]
                    elif date[3:5]=='05' and kk>31:
                        final_date = pk + '/06'+date[5:]
                    elif date[3:5]=='06' and kk>30:
                        final_date = pk + '/07'+date[5:]
                    elif date[3:5]=='07' and kk>31:
                        final_date = pk + '/08'+date[5:]
                    elif date[3:5]=='08' and kk>31:
                        final_date = pk + '/09'+date[5:]
                    elif date[3:5]=='09' and kk>30:
                        final_date = pk + '/10'+date[5:]
                    elif date[3:5]=='10' and kk>31:
                        final_date = pk + '/11'+date[5:]
                    elif date[3:5]=='11' and kk>30:
                        final_date = pk + '/12'+date[5:]
                    elif date[3:5]=='12' and kk>31:
                        final_date = pk + '/01/'+str(int(date[6:10])+1)
                    else:
                        final_date = pk + date[2:]
                else:
                    final_date = date
                if final_date==ddate and len(tds[5].text)==11:
                    solved_prob += 1
                    prob = tds[3].a['href']
                    prob_url = f"https://codeforces.com{prob}"
                    prob_res = requests.get(prob_url).text
                    prob_soup = BeautifulSoup(prob_res, 'lxml')
                    difficulty = prob_soup.find('span', title='Difficulty')
                    if difficulty is None:
                        score +=0
                    else:
                        dif = int(difficulty.text.strip()[1:])
                        if dif==800:
                            score += 0.25
                        else:
                            score += (dif-800)/100
                    ctt+=1
                if ctt>0 and final_date!=ddate:
                    cttt=1
                    break
            page = page+1
        amm = [user, ddate, score, solved_prob]
        print(amm)
        thewriter.writerow(amm)
score_data = pd.read_csv('scores.csv')
x_index = np.arange(len(score_data.User))
w = 0.2
plt.bar(x_index -w , score_data.Score, width=2*w)
plt.bar(x_index +w , score_data.Solved, width=2*w)
plt.xticks(ticks=x_index, labels=score_data.User)
plt.legend(['Score','Solved'])
tt = f'Date: {ddate}'
plt.title(tt)
plt.show()