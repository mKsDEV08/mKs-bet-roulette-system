import numpy as np
import os
import PySimpleGUI as sg

layout = [
    [sg.Text("Sistema de Apostas")],
    [sg.Text("Qual seu nome"), sg.InputText(key='-name-')],
    [sg.Text("Qual o Valor da Aposta"), sg.InputText(key='-bet_amount-')],
    [sg.Text("Qual o lado da aposta"), sg.InputText(key='-choice-')],
    [sg.Text('P | Preto (49,5% - 2*)'), sg.Text('V | Vermelho (49,5% - 2*)'), sg.Text('B | Branco (1% - 14*)')],
    [sg.Button("Apostar", key='-bet-')],
    [sg.Text('', key='-result-')]
]

window = sg.Window('Bet System', layout)

while True:
    event, values = window.read()

    roll = np.random.randint(1, 1001)
    folder_path = os.getcwd() + r'\snames'

    i = os.listdir(folder_path)

    name = values['-name-']

    file_name = name + ".txt"

    if event == '-bet-':

        if file_name in i:
            with open(f'snames\{name}.txt', 'r') as file:
                amount = file.read()

            choice = values['-choice-']
            bet_amount = values['-bet_amount-']

            if choice == "P" or "V" or "B":
                if int(amount) >= int(bet_amount):
                    if roll <= 495 and choice == "P":
                        win_add = int(bet_amount) * 2
                        final_amount = win_add + int(amount)
                        window['-result-'].update(f'Você Ganhou! (Seu saldo atual é de R${final_amount})')
                        with open(f'snames\{name}.txt', 'w') as file:
                            file.write(str(final_amount))

                    elif 495 < roll <= 990 and choice == "V":
                        win_add = int(bet_amount) * 2
                        final_amount = win_add + int(amount)
                        window['-result-'].update(f'Você Ganhou! (Seu saldo atual é de R${final_amount})')
                        with open(f'snames\{name}.txt', 'w') as file:
                            file.write(str(final_amount))

                    elif 990 < roll <= 1001 and choice == "B":
                        win_add = int(bet_amount) * 14
                        final_amount = win_add + int(amount)
                        window['-result-'].update(f'Você Ganhou! (Seu saldo atual é de R${final_amount})')
                        with open(f'snames\{name}.txt', 'w') as file:
                            file.write(str(final_amount))

                    else:
                        win_add = int(bet_amount)
                        final_amount = int(amount) - win_add
                        window['-result-'].update(f'Você Perdeu! (Seu saldo atual é de R${final_amount})')
                        with open(f'snames\{name}.txt', 'w') as file:
                            file.write(str(final_amount))

                else:
                    window['-result-'].update('Você não tem saldo suficiente!')

            else:
                window['-result-'].update('Isso não é uma escolha válida!')

        else:
            with open(f'snames\{name}.txt', 'w') as file:
                file.write("1000")

            with open(f'snames\{name}.txt', 'r') as file:
                amount = file.read()

            if choice == "P" or "V" or "B":
                if int(amount) >= int(bet_amount):
                    if roll <= 495 and choice == "P":
                        win_add = int(bet_amount) * 2
                        final_amount = win_add + int(amount)
                        window['-result-'].update(f'Você Ganhou! (Seu saldo atual é de R${final_amount})')
                        with open(f'snames\{name}.txt', 'w') as file:
                            file.write(str(final_amount))

                    elif 495 < roll <= 990 and choice == "V":
                        win_add = int(bet_amount) * 2
                        final_amount = win_add + int(amount)
                        window['-result-'].update(f'Você Ganhou! (Seu saldo atual é de R${final_amount})')
                        with open(f'snames\{name}.txt', 'w') as file:
                            file.write(str(final_amount))

                    elif 990 < roll <= 1001 and choice == "B":
                        win_add = int(bet_amount) * 14
                        final_amount = win_add + int(amount)
                        window['-result-'].update(f'Você Ganhou! (Seu saldo atual é de R${final_amount})')
                        with open(f'snames\{name}.txt', 'w') as file:
                            file.write(str(final_amount))

                    else:
                        win_add = int(bet_amount)
                        final_amount = int(amount) - win_add
                        window['-result-'].update(f'Você Perdeu! (Seu saldo atual é de R${final_amount})')
                        with open(f'snames\{name}.txt', 'w') as file:
                            file.write(str(final_amount))

                else:
                    window['-result-'].update('Você não tem saldo suficiente!')

            else:
                window['-result-'].update('Isso não é uma escolha válida!')

    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break