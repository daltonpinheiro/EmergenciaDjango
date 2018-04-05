# EmergenciaDjango
Sistema para realização de fichas de triagem de pacientes no setor de emergência médica em django.
Este sistema cria uma ficha que se acomoda perfeitamente a uma folha A4:
1)  O paciente chega ao hospital e realiza a triagem da qual é atribuida a este uma classificação de risco;
2)  Ao clicar em registrar o sistema imprime a ficha e registra o evento em um banco de dados SQLITE;
3)  O admin pode verificar o andamento do processo no modo administrativo;
4)  O sistema gera uma interface gráfica com os gráficos em tempo real.
## Instalação
1)	Instalar python na máquina, no Linux criar um virtualenv com a versão de python 3.6.4;
2)	Instalar a versão mais recente do Django 2.0.1 (pip install django);
3)	Baixe o repositório em uma pasta;
4)  Descompacte o arquivo, entre na pasta e digite "pip install -r requirements.txt" para instalar os pacotes adicionais que sistema vai usar.

## Testando
Entre na pasta que baixou e digite “python manage.py runserver”

**Modo operador**

Login:operador

Senha:operador

**Modo admin**

Login:admin

Senha:manchester

Desenvolvedores: Dalton/Suzete EBSERH
