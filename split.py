import os.path
from operator import itemgetter, attrgetter
caminho = input("Caminho do arquivo m3u: ")
arquivo = open(caminho,encoding="utf8")
destino = input("Caminho de destino: ")

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
for linha in arquivo:
    foto = linha.split("tvg-logo=")[1].split("group-title=")[0].split("\n")[0]
    grupo = linha.split("group-title=")[1].split(",")[0].split("\n")[0]
    nome = linha.split("group-title=")[1].split(",")[1].split("\n")[0]
    m3u = linha;
    linha = link = arquivo.readline()
    arq.append(arquivoM3u(grupo,nome,link,foto,m3u))

arq = sorted(arq, key=lambda arquivoM3u: arquivoM3u.grupo)

for linha in arq:
    grupo = linha.grupo
    grupo = grupo.replace('|','-').replace("\"",'').replace(':','').replace("?", '')
    fullfilename = os.path.join(destino, grupo)
    if(os.path.exists(fullfilename) == False):
        os.mkdir(fullfilename)
    nome = linha.nome+".m3u";
    nome = nome.replace("/", '-').replace("?", '').replace(":","").replace("*",'')
    criarArq = os.path.join(fullfilename, nome)
    criarArq = open(criarArq, "a",encoding="utf8")
    txt = list()
    txt.append("#EXTM3U")
    txt.append(linha.m3u)
    txt.append(linha.link+"\n")
    criarArq.writelines(txt)
    criarArq.close()
