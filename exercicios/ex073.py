# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:

#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética. 
#d) Em que posição está o time Goiás.


times = ('América-MG',
'Athletico-PR',
'Atlético-MG',
'Bahia',
'Botafogo',
'Corinthians',
'Coritiba',
'Cruzeiro',
'Cuiabá',
'Flamengo',
'Fluminense',
'Fortaleza',
'Goiás',
'Grêmio',
'Internacional',
'Palmeiras',
'Bragantino',
'Santos',
'São Paulo',
'Vasco da Gama',)

print(f'Os 5 primeiros times do brasileirão são: 1º{times[0]} 2º {times[1]} 3º {times[2]} 4º {times[3]} 5º {times[4]}')
print(f'Os 5 primeiros times do brasileirão são: {times[0:5]}')
print(f'Os 4 Ultimos times do brasileirão são:{times[-4:]}')
print(sorted(times))
print(f'O time do Gioás esta na {times.index("Goiás")}')