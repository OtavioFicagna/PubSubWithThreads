Requisitos necessários (A aplicação está homologada para funcionamento na versão 24.04 LTS do sistema operacional Ubuntu. Assim sendo, o funcionamento da aplicação não é garantido fora desse escopo):

1. É recomendada a utilização de ambiente virtual do Python para execução. Para criação de um ambiente virtual pode ser utilizado o seguinte comando:

python3 -m venv env

E para a ativação do ambiente virtual podemos utilizar o comando:

source env/bin/activate

2. Instalar os pacotes do PyQt5 e Qt5:

sudo apt-get update
pip install pyqt5
sudo apt install -y qtcreator qtbase5-dev qt5-qmake cmake
