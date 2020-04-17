#/usr/bin/python

import sys
from datetime import date
import os

from pathlib import Path


#define o diretorio padrao de trabalho.
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#verificar se foi informado o nome do arquivo atraves do parametro
if(len(sys.argv)==1):
    print("Por-favor, informe o nome do arquivo a ser convertido")
    print("Exemplo:")
    print("$python "+__file__+" <nome_pasta>/<nome_arquivo>")
    exit(0)

#define as pastas de trabalho (Origem e destino)
hoje = str(date.today())

cam_arquivo=str(sys.argv[1]).replace(" ","\ ")
caminho_origem = ''.join(cam_arquivo.split(os.sep)[:-1])
arquivo_pdf = cam_arquivo.split(os.sep)[-1]
caminho_destino = dname+os.sep+hoje+os.sep+arquivo_pdf.replace(".pdf","")


# Recebe como parametro nome do cam_arquivo pdf a ser gerado.
# Exemplo $gera_slides  nome.pdf
print ("Convertendo "+ (cam_arquivo) +" em "+hoje+"_"+(cam_arquivo)+"_web")

# Chama a pdftoppm
# Convert cada página em um cam_arquivo diferente!
#   $mkdir images
#   $pdftoppm -jpeg -r 200 exemplo.pdf images/pg


#os.mkdir(hoje)
Path(hoje).mkdir(parents=True, exist_ok=True)
Path(caminho_destino).mkdir(parents=True, exist_ok=True)
print("Gerando a versão mobile")#+os.system(cmd))
cmd = "pdftoppm -jpeg -r 70  "+ (cam_arquivo) +" "+caminho_destino+os.sep+"p_mobi" #print(cmd)
#print("Destino"+caminho_destino)
#print("CMD")
#print(cmd)
res =os.system(cmd)
print("Imagens geradas com sucesso.")
#print("Gerando a versão webdesktop")#+os.system(cmd))
#cmd = "pdftoppm -jpeg -r 300  "+ (cam_arquivo) +" "+hoje+os.sep+cam_arquivo+"_mobi"
#print(cmd)
#print(os.system(cmd))


    #versao mobi com 100px slides.
    #versao web com 300px slides.


    #calcula quantos sliedes

#folders = cam_arquivo.split(os.sep)[:-1]
#dir = os.sep.join(folders) # obtenho o caminho sem o nome do cam_arquivo
#print(cam_arquivo)
#print("DIR"+dir)

print("caminho_destino")
print(caminho_destino)
lista = [name for name in os.listdir(caminho_destino) if name.endswith("jpg") ]
numero_slides = (len(lista))
lista.sort()
#print(lista)

# Adiciona um arquivo html header.
import io

head_f = io.open("gerador_pdf_webslides"+os.sep+"head.html", mode="r", encoding="utf-8")
footer_f = io.open("gerador_pdf_webslides"+os.sep+"footer.html", mode="r", encoding="utf-8")

cam_arquivo=cam_arquivo.replace("\\ ","_").replace(".pdf","")
print("Gerando o arquivo:"+cam_arquivo)
out = io.open( caminho_destino+os.sep+"index_mobi.html", mode="w", encoding="utf-8")
slides=[]

for i in lista:
    slides.append("\n\t\t\t\t<section data-background-transition=\"slide\" data-background=\""+str(i)+"\">  </section>\n")

html = head_f.read()+''.join(slides) +footer_f.read()
out.write(html)


# Gera o HTML final.