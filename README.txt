Bibliotecas instalar:
pip install requests
pip install pandas
pip install openpyxl
pip install colorama



# Se refere ao Evento 270 – HORAS NORMAIS NA RESCISÃO - FORMULA PADRÃO
# Esse evento substitui o evento 1 – HORAS NORMAIS no processamento de rescisão.
# Desta forma no codigo_evento_copiado informe o código do evento antigo no banco do cliente que seria o 1
# E no campo codigo_novo_evento informe o código do novo evento a ser criado


# Se refere ao Evento 274 – 13º SALÁRIO INTEGRAL NA RESCISÃO - FORMULA PADRÃO
# Esse evento substitui o evento 25 – 13º SALÁRIO INTEGRAL no processamento de rescisão.
# Desta forma no codigo_evento_copiado informe o código do evento antigo no banco do cliente que seria o 25
# E no campo codigo_novo_evento informe o código do novo evento a ser criado


# Se refere ao Evento 275 – MÉDIA HORAS 13º SALÁRIO NA RESCISÃO
# Esse evento substitui o evento 28 – MÉDIA HORAS 13º SALÁRIO  no processamento de rescisão.
# Desta forma no codigo_evento_copiado informe o código do evento antigo no banco do cliente que seria o 28
# E no campo codigo_novo_evento informe o código do novo evento a ser criado


# Se refere ao Evento 276 – MÉDIA VALOR 13º SALÁRIO NA RESCISÃO
# Esse evento substitui o evento 29 – MÉDIA VALOR 13 SALÁRIO  no processamento de rescisão.
# Desta forma no codigo_evento_copiado informe o código do evento antigo no banco do cliente que seria o 29
# E no campo codigo_novo_evento informe o código do novo evento a ser criado


# Se refere ao Evento 277 – VANTAGENS 13º SALÁRIO NA RESCISÃO
# Esse evento substitui o evento 30 – VANTAGENS 13º SALÁRIO  no processamento de rescisão.
# Desta forma no codigo_evento_copiado informe o código do evento antigo no banco do cliente que seria o 30
# E no campo codigo_novo_evento informe o código do novo evento a ser criado


# Se refere ao Evento 278 – MÉDIA PERCENTUAL 13º SALÁRIO NA RESCISÃO
# Esse evento substitui o evento 233 – MÉDIA PERCENTUAL 13º SALÁRIO  no processamento de rescisão.
# Desta forma no codigo_evento_copiado informe o código do evento antigo no banco do cliente que seria o 233
# E no campo codigo_novo_evento informe o código do novo evento a ser criado


# Se refere ao Evento 279 – ADIANTAMENTO 13º SALÁRIO NA RESCISÃO
# Esse evento substitui o evento 43 – ADIANTAMENTO 13º SALÁRIO  no processamento de rescisão.
# Desta forma no codigo_evento_copiado informe o código do evento antigo no banco do cliente que seria o 43
# E no campo codigo_novo_evento informe o código do novo evento a ser criado

# ----------------------------------------------------------
Novos:
271 – 13º SALÁRIO INTEGRAL – APOSENTADO (copiar de 25 - 13º SALÁRIO INTEGRAL)
272 – 13º SALÁRIO ADIANTADO – APOSENTADO (copiar de 26 - 13º SALÁRIO ADIANTADO)
273 – ADIANTAMENTO 13º SALÁRIO – APOSENTADO (copiar de 43 - ADIANTAMENTO 13º SALÁRIO)
Naturezas de rubricas e incidências iguais aos eventos a serem copiados.

300 - 13º SALÁRIO INTEGRAL AUXILIO MATERNIDADE (copiar de 25 - 13º SALÁRIO INTEGRAL)
301 - MÉDIA HORAS 13º SALÁRIO AUXILIO MATERNIDADE (copiar de 28 - MÉDIA HORAS 13º SALÁRIO)
302 - MÉDIA VALOR 13º SALÁRIO AUXILIO MATERNIDADE (copiar de 29 - MÉDIA VALOR 13º SALÁRIO)
303 - VANTAGENS 13º SALÁRIO AUXILIO MATERNIDADE (copiar de 30 - VANTAGENS 13º SALÁRIO)
304 - MÉDIA PERCENTUAL 13º SALÁRIO AUXILIO MATERNIDADE (copiar de 233 - MÉDIA PERCENTUAL 13º SALÁRIO)
Naturezas de rubricas 4051 - Salário maternidade 13º salário, e incidências para
Previdência social 22, IRRF 12, FGTS 12, o restante 00.
Processamento guia Geral: Calcular em 13º integral e rescisões.
