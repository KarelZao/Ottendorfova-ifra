from typing import Tuple, List
import ast


def zasifruj(zprava, sifrovaci_klic, datum):
    sifrovana_zprava = []
    for char in zprava:
        position = sifrovaci_klic.find(char) + datum
        if position < len(sifrovaci_klic):
            page = position // (26 * 26)
            row = (position % (26 * 26)) // 26
            char_pos = (position % (26 * 26)) % 26
            sifrovana_zprava.append((page, row, char_pos))
    return sifrovana_zprava


def desifruj(sifrovana_zprava, sifrovaci_klic, datum):
    desifrovana_zprava = ""
    for page, row, char_pos in sifrovana_zprava:
        position = page * 26 * 26 + row * 26 + char_pos - datum
        if 0 <= position < len(sifrovaci_klic):
            desifrovana_zprava += sifrovaci_klic[position]
    return desifrovana_zprava

"""
def zasifruj(zprava: str, sifrovaci_klic: str, datum: int) -> List[Tuple[int, int, int]]:
    sifrovana_zprava = []
    for char in zprava:
        position = sifrovaci_klic.find(char) + datum
        if position < len(sifrovaci_klic):
            page = position // (26 * 26)
            row = (position % (26 * 26)) // 26
            char_pos = (position % (26 * 26)) % 26
            sifrovana_zprava.append((page, row, char_pos))
    return sifrovana_zprava


def desifruj(sifrovana_zprava: List[Tuple[int, int, int]], sifrovaci_klic: str, datum: int) -> str:
    desifrovana_zprava = ""
    for page, row, char_pos in sifrovana_zprava:
        position = page * 26 * 26 + row * 26 + char_pos - datum
        if 0 <= position < len(sifrovaci_klic):
            desifrovana_zprava += sifrovaci_klic[position]
    return desifrovana_zprava
"""
def nacti_sifru_ze_souboru():
    with open('sifra.txt', 'r') as soubor:
        sifra = soubor.read()
    return ast.literal_eval(sifra)
