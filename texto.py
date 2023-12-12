from time import sleep

def dormir():
    sleep(0.5)

if __name__ == "__main__":
    
    cursor_vermelho = '\x1b[31m'
    cursor_acima = '\033[1A'
    limpar_linha = '\x1b[2k'
    
    print(cursor_vermelho + "Vermelho")
    dormir()
    print('\x1b[34mAzul')
    dormir()
    print('\x1b[32mVerde')
    dormir()
    print((cursor_acima + limpar_linha) * 3, end='')