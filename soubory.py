from typing import List, Tuple
import ast
import PySimpleGUI as sg


def nacti_txt_jako_klic(cesta_k_souboru):
    with open(cesta_k_souboru, 'r', encoding='utf8') as soubor:
        text = soubor.read()
    return text

def uloz_sifru_do_souboru(sifra, cesta_k_souboru='sifra.txt'):
    with open(cesta_k_souboru, 'w', encoding='utf8') as soubor:
        soubor.write(str(sifra))
    sg.popup("Šifra uložena.")


def nacti_sifru_z_souboru(cesta_k_souboru='sifra.txt'):
    with open(cesta_k_souboru, 'r', encoding='utf8') as soubor:
        sifra = ast.literal_eval(soubor.read())
    return sifra

