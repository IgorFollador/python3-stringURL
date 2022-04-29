endereco = "Avenida Adão Welker 81, Centro, Barão de Cotegipe, RS, 99740-000"

import re # Regular Expression --RegEx

# 5 dígitos + hífen(opcional) + 3 dígitos
padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
busca = padrao.search(endereco) # Match
if busca:
    cep = busca.group()
    print(cep)