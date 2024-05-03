
#perguntar quem é o pagador e o recebedor ou encerrar

# Perguntar ao usuário qual o tipo de pagamento se pix ou se em boleto
# Se boleto, só permitir um pagamento
# e trazer mensagem de sucesso e que em 24h estará depositado na conta favorecida e mais uma liberação de pagamento


# Se pix, perguntar se vai querer recorrência de pagamentos
# Verificar valor inicial e final


conta_pagador= 150000
conta_recebedor= -45000

tipoOperador = input('Qual o tipo de acesso? Pagador ou recebedor? ')

while tipoOperador.lower() == 'pagador' or tipoOperador.lower() == 'recebedor':

    if tipoOperador.lower() == 'pagador':
        
        tipoPgto= input('Qual será o tipo de pagamento?(boleto ou pix)  ')

        if tipoPgto.lower() == 'pix':
            qtdPgto= int(input('Quantos pagamentos serão realizados? '))
            valor = float(input('Qual o valor que será pago nas transações? Em R$.  '))
            if qtdPgto > 1:
                for transacao in range(1,qtdPgto+1):
                    print(f'Transferência {tipoPgto.upper()} de nº {transacao}.\n\n')
                    print(f'Você tinha R$ {conta_pagador}.')
                    conta_pagador =  conta_pagador - valor
                    conta_recebedor = conta_recebedor + valor
                    print(f'Você tem R$ {conta_pagador}.\n')
            else:
                print(f'Transferência {tipoPgto.upper()} de nº {qtdPgto}.')
                print(f'Você tinha R$ {conta_pagador}.')
                conta_pagador = conta_pagador - valor
                conta_recebedor = conta_recebedor + valor
                print(f'Você tem R$ {conta_pagador}.')

        elif tipoPgto.lower() == 'boleto':
            valor = float(input('Qual o valor que será pago na transação? Em R$.  '))
            print(f'Você tinha R$ {conta_pagador}.')
            print(f'Você fez uma transferência de R$ {valor}. A próxima transferência só poderá ser realizada amanhã!')
            conta_pagador = conta_pagador - valor
            print(f'Você tinha R$ {conta_pagador}.')

    else:
        print(f'Você tem R$ {conta_recebedor}')

    tipoOperador = input('Você é recebedor ou pagador? ')