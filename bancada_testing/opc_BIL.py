import OpenOPC
from time import sleep

import pywintypes
pywintypes.datetime = pywintypes.TimeType


opc = OpenOPC.client()

opc.connect('OPC.SimaticHMI.CoRtHmiRTm')

while 1:
    pt = opc.read(('Peças_Erradas_Total'))
    print('\nAtenção! O numero de pecas erradas total: '+str(pt[0]))
    ans = input('Deseja alterar esse valor? \nDigite:\n- S para sim\n- N para nao\n- Q para sair\n')
    if ans == 'S':
        val = input('Insira o novo valor:\n')
        opc.write(('Peças_Erradas_Total',val))
    sleep(1)
    if ans == 'N':
        pass
    if ans == 'Q':
        break

sleep(1)

opc.close()
