import requests
from bs4 import BeautifulSoup

server=input("enter server: ")
nick=input("enter nickname: ")

def getStats(nickName):

    url=requests.get("http://"+server+".op.gg/summoner/userName="+nick)
    soup=BeautifulSoup(url.text,"html.parser")

    gameStats=soup.findAll("div",{"class":"GameItemWrap"})

    gameTypes=[]
    gameLengths=[]
    gameResults=[]
    champions=[]
    kdas=[]
    csscore=[]

    for i in gameStats:
        type=i.find("div",{"class":"GameType"}).text
        type=type.replace("\n","").replace("\t","")
        if len(type)<len("Flex 5:5 Rank"):
            type+=" "*(len("Flex 5:5 Rank")-len(type))
        gameTypes.append(type)

        length=i.find("div",{"class":"GameLength"}).text
        gameLengths.append(length)

        result=i.find("div",{"class":"GameResult"}).text
        result=result.replace("\n","").replace("\t","")
        gameResults.append(result)

        champion=i.find("div",{"class":"ChampionImage"}).a.img["alt"]
        champions.append(champion)


        kill=i.find("span",{"class":"Kill"}).text
        death=i.find("span",{"class":"Death"}).text
        assist=i.find("span",{"class":"Assist"}).text
        kda=kill+"/"+death+"/"+assist
        kdas.append(kda)

        cs=i.find("div",{"class":"CS"}).span
        csscore.append(cs.text.split(" ")[0])
    return gameTypes,gameLengths,gameResults,champions,kdas,csscore

def printStats(data):
    for i in range(len(data[0])):
        toPrint=""
        for j in range(len(data)):
            toPrint+="    "+data[j][i].ljust(10)
        print(toPrint)

printStats(getStats(nick))
