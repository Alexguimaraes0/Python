#elif   
name = input('Qual é o seu nome? ')

if name == 'Alex':
    print('Que nome bonito!')
elif name == 'Maria' or name == 'Pedro' or name == 'carlos':
    print('Seu nome é bem popular no brasil.')
elif name in ('Ana Claudia Jéssica Julia'):
    print('Que belo nome feminino!')

print('Tenha um bom dia {}!'.format(name))