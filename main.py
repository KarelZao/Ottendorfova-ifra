import PySimpleGUI as sg
from sifrovani import zasifruj, desifruj, nacti_sifru_ze_souboru
from soubory import nacti_txt_jako_klic, uloz_sifru_do_souboru
import ast


def vycisti_formular(okno, hodnoty):
    for key in hodnoty:
        okno[key]('')
    return None


def main():
    klic = nacti_txt_jako_klic('klic.txt')
    sg.theme('DarkTeal9')
    layout = [
        [sg.Radio('Šifrovat', "RADIO1", default=True, key='plus', enable_events=True), sg.Radio('Dešifrovat', "RADIO1", key='minus', enable_events=True)],
        [sg.Text('Datum:', size=(15, 1)), sg.InputText(key='datum')],
        [sg.Text('Zpráva:', size=(15, 1)), sg.InputText(key='text')],
        [sg.Text('Zašifrovaná zpráva:', size=(15, 1)),
         sg.InputText(key='encrypted', disabled=False, text_color='black')],
        [sg.Text('Dešifrovaná zpráva:', size=(15, 1)),
         sg.InputText(key='decrypted', disabled=False, text_color='black')],
        [sg.Submit('Potvrdit'), sg.Button('Uložit šifru'), sg.Button('Načíst šifru')],
        [sg.Button('Vyčistit'), sg.Exit('Konec')]
    ]

    window = sg.Window('Ottendorfiva šifra', layout)

    while True:
        event, values = window.read()
        if event == 'Vyčistit':
            vycisti_formular(window, values)

        if event == 'Potvrdit':
            if values['datum'].isdigit():
                date = int(values['datum'])
                msg = values['text']
                if values['plus']:
                    encrypted_msg = zasifruj(msg, klic, date)
                    window['encrypted'].update(str(encrypted_msg))
                if values['minus']:
                    encrypted_msg = ast.literal_eval(window['encrypted'].get())
                    if isinstance(encrypted_msg, list):
                        decrypted_msg = desifruj(encrypted_msg, klic, date)
                        window['decrypted'].update(decrypted_msg)
                    else:
                        sg.popup('Chybí zašifrovaná zpráva!')
            else:
                sg.popup('Datum musí být číslo!')

        if event == 'Uložit šifru':
            encrypted_msg = ast.literal_eval(window['encrypted'].get())
            if isinstance(encrypted_msg, list):
                uloz_sifru_do_souboru(encrypted_msg)
            else:
                sg.popup('Chybí zašifrovaná zpráva!')

        if event == 'Načíst šifru':
            encrypted_msg = nacti_sifru_ze_souboru()
            window['encrypted'].update(str(encrypted_msg))

        if event == sg.WIN_CLOSED or event == 'Konec':
            break

    window.close()


if __name__ == "__main__":
    main()
