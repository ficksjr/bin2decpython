def bin2dec():
    resp = 's'
    while resp == 's':
        try:
            ene = int(str(input('Digite um número binário de até 8 dígitos: ')).strip())
            ene = str(ene).strip()
            b = {'0', '1'}
            t = set(str(ene))
            if b == t or t == {'0'} or t == {'1'}:
                num = str(ene[::-1])
                cont = 0
                for i in range(0, len(num)):
                    if num[i] == '1':
                        cont = cont + (2 ** i)
                break
            else:
                print("O número informado não é binário.")
                continue
        except ValueError:
            print("O dado informado não é numeral.")
    print("O número binário transformado para base decimal é " + str(cont))
    resp = input("Deseja fazer outra operação? [s/n]").lower().strip()
    if resp == 's':
        bin2dec()
    else:
        print("Finalizando Programa.")


bin2dec()
