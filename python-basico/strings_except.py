"""
Strings e Excecoes
"""

texto_string = "tratando string"

print len(texto_string)

#string com multiplas linhas
multi_line = """primeira linha
segunda linha
terceira linha"""

print multi_line

try:
    print 0/0
except ZeroDivisionError:
    print 'erro ao  dividir por zero'

