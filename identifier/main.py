from app.identifier import Identifier


app = Identifier()
identifier = 'cont'

if (app.validate_identifier(identifier)):
    print('Identificador válido')
else:
    print('Identificador inválido')
