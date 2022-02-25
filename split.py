import os.path
from operator import itemgetter, attrgetter
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter import filedialog

frame = Tk()
frame.withdraw()
caminho = askopenfilename()
arquivo = open(caminho,encoding="utf8")
destino = filedialog.askdirectory()

class arquivoM3u:
    def __init__(self, grupo, nome, link, foto, m3u):
        self.grupo = grupo
        self.nome = nome
        self.link = link
        self.foto = foto
        self.m3u = m3u
    def __repr__(self):
        return repr((self.grupo, self.nome, self.link, self.foto, self.m3u))
    
arq = []
arquivo.readline()
arquivo.readline()
for linha in arquivo:
    foto = linha.split("tvg-logo=")[1].split("group-title=")[0].split("\n")[0]
    grupo = linha.split("group-title=")[1].split(",")[0].split("\n")[0]
    nome = linha.split("group-title=")[1].split(",")[1].split("\n")[0]
    m3u = linha;
    linha = link = arquivo.readline()
    arq.append(arquivoM3u(grupo,nome,link,foto,m3u))

arq = sorted(arq, key=lambda arquivoM3u: arquivoM3u.grupo)
i = 0;
while(i < len(arq)):
    linha = arq[i]
    grupo = linha.grupo
    grupo = grupo.replace('|','-').replace("\"",'').replace(':','').replace("?", '')
    fullfilename = os.path.join(destino, grupo)
    if(os.path.exists(fullfilename) == False):
        print(str(round((i*100)/len(arq),2)) + "% - " + str(i)+" : "+str(len(arq)) + "\n" + fullfilename)
        os.mkdir(fullfilename)
    while(fullfilename[len(fullfilename)-1] == ' '):
        fullfilename = fullfilename[:-1]
    nome = linha.nome+".m3u";
    nome = nome.replace("/", '-').replace("?", '').replace(":","").replace("*",'')
    criarArq = os.path.join(fullfilename, nome)
    criarArq = criarArq.replace("\\","/").replace('"',"").replace('|'," ").replace('  '," ")
    criarArq = open(criarArq, "a",encoding="utf8")
    txt = list()
    txt.append("#EXTM3U")
    txt.append(linha.m3u)
    txt.append(linha.link+"\n")
    criarArq.writelines(txt)
    criarArq.close()
    i = i + 1
print(str(round((i*100)/len(arq),2))+"%\nFim!!")
frame.destroy()
