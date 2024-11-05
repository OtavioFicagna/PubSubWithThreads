
# Sistema PubSub utilizando socket e threads

## Requisitos Necessários
> **Obs:** A aplicação está homologada para funcionamento na versão 24.04 LTS do sistema operacional Ubuntu. Assim sendo, o funcionamento da aplicação não é garantido fora desse escopo.

### Ambiente Virtual
1. É recomendada a utilização de um ambiente virtual do Python para execução. Para criação de um ambiente virtual, utilize o comando:
   ```bash
   python3 -m venv env
   ```
2. Para ativar o ambiente virtual, utilize o comando:
   ```bash
   source env/bin/activate
   ```

### Instalação dos Pacotes PyQt5 e Qt5
1. Atualize o gerenciador de pacotes:
   ```bash
   sudo apt-get update
   ```
2. Instale o PyQt5:
   ```bash
   pip install pyqt5
   ```
3. Instale os pacotes do Qt5:
   ```bash
   sudo apt install -y qtcreator qtbase5-dev qt5-qmake cmake
   ```

## Execução

### Passos para Execução
1. Clone este repositório do GitHub.
2. Verifique os requisitos necessários contidos neste README.
3. A única ordem obrigatória para execução é iniciar o **difusor** antes do **consumidor**.
4. A ordem recomendada é:
   - Difusor ➔ Consumidor (realizar as inscrições) ➔ Gerador  
   Dessa forma, nenhuma informação é perdida.
5. Os arquivos a seguir contêm os parâmetros relacionados a portas e IP utilizados durante a execução (por padrão, configurados como `localhost`):
   - `difusor/difusor.py`
   - `gerador/gerador.py`
   - `consumidor/main.py`
6. No arquivo `gerador/gerador.py`, é possível configurar as variáveis:
   - `T_MIN` e `T_MAX`: tempo mínimo e máximo que a thread geradora dorme após gerar a informação.
   - `V_MIN` e `V_MAX`: valor máximo e mínimo que a thread geradora gera.
7. Podem ser instanciados quantos consumidores forem necessários.

### Execução do Difusor
1. Com o repositório clonado, entre no diretório `difusor`.
2. Execute o comando:
   ```bash
   python3 difusor.py
   ```

### Execução do Consumidor
1. Com o repositório clonado, entre no diretório `consumidor`.
2. Execute o comando:
   ```bash
   python3 main.py
   ```
3. Na interface, inscreva-se nas informações desejadas.

### Execução do Gerador
1. Com o repositório clonado, entre no diretório `gerador`.
2. Execute o comando:
   ```bash
   python3 gerador.py
   ```
3. Digite o número de geradores a serem instanciados.
4. Digite quais tipos de informações (1 a 6) cada gerador irá gerar, separados por espaço.

## Contatos
- Henrique Linck: 179791@upf.br
- Otávio Ficagna: 195749@upf.br
