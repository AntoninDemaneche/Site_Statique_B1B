import markdown2
import os
import re
import argparse


# Variable permettant l'executions de la fonctions via cmd
parser = argparse.ArgumentParser(description = "Transforme un fichier Markdown en un fichier Html")
parser.add_argument("-i", "--input", help = "Donner le fichier Markdown à convertir")
parser.add_argument("-o", "--output", help = "Donner le fichier qui sera transformer en fichier HTML")
args = parser.parse_args()

# Variable contenant les fichiers Md et Html
fichier_md = args.input
fichier_html = args.output

# Template de la page HTML
head = "<!doctype html>\n\t<html lang='fr'>\n<head>\n\t<meta charset='utf-8'>\n\t<title>Dab</title>\n</head>\n<body>"
footer = "</body>\n</html>"

# Pour géré les liens
link_patterns=[(re.compile(r'((([A-Za-z]{3,9}:(?:\/\/)?)(?:[\-;:&=\+\$,\w]+@)?[A-Za-z0-9\.\-]+(:[0-9]+)?|(?:www\.|[\-;:&=\+\$,\w]+@)[A-Za-z0-9\.\-]+)((?:\/[\+~%\/\.\w\-_]*)?\??(?:[\-\+=&;%@\.\w_]*)#?(?:[\.\!\/\\\w]*))?)'),r'\1')]

# Variable permettant la conversion 
input_file = open(fichier_md, "r")
conv = markdown2.markdown(input_file.read(), extras=["link-patterns"] ,link_patterns=link_patterns)


#Fonctions permettant de mettre en place le fichier HTML et de mettre la conversion du fichier MD dans le fichier HTML
def convert(fichier_md, fichier_html): 
    if '.conv' in fichier_html:
             html_file = open(fichier_html, 'w')
    if '.conv' not in fichier_html:
            html_file = open(f'{fichier_html}', 'w')
    html_file.write(head)
    html_file.write(conv)
    html_file.write(footer)
    print('Félicitations la mainoeuvres à réussit !')
   

# Appel de la fonction de conversion
f = open(fichier_md, 'a')
convert(fichier_md, fichier_html)