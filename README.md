Snake Game - Minecraft Style
Welcome to the Snake Game in Minecraft style! This is a simple and fun game designed for kids (like my 6-year-old niece), with a theme inspired by the pixelated world of Minecraft. The game was developed using Python with Flask for the backend and p5.js for the frontend, running in a browser.
Description
In this game, you control a snake that moves on a grid, eating fruits (Golden Apples) to grow and earn points. The game has 5 levels, each featuring a different Minecraft biome (Plains, Forest, Desert, Mountains, and Nether). The speed increases with each level, starting at 0.5 and going up to 2.0. There are challenges like Creepers (enemies) and interactive blocks (Ores and Quartz) that give extra points.
Features

Themed Levels: 5 Minecraft biomes that change with each level.
Progressive Speed: Starts at 0.5 and increases to 2.0.
Enemies: Creepers appear starting from Level 2 and cause a game over if you collide with them.
Interactive Blocks: Ores and Quartz (Levels 4 and 5) give +2 extra points when collected.
Kid-Friendly Design: Colorful visuals and simple controls (arrow keys) for children.
External Legend: Game items (Golden Apple, Creeper, Ore, Quartz) are explained in a legend outside the game frame.

Technologies Used

Backend: Python 3 with Flask
Frontend: HTML, JavaScript with p5.js
Styling: Basic CSS

Prerequisites

Python 3.x installed
Modern browser (Chrome, Firefox, etc.)
Internet connection (to load the p5.js library via CDN)

Installation

Clone the repository to your machine:
git clone <REPOSITORY_URL>
cd snake_game


Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install the dependencies:
pip install flask


Verify the file structure:
snake_game/
├── app.py
├── templates/
│   └── index.html
├── README.md



How to Run

Start the Flask server:
python app.py

The server will start at http://127.0.0.1:5000. If port 5000 is in use, edit app.py to use another port (e.g., app.run(debug=True, port=5001)).

Open your browser and go to:
http://127.0.0.1:5000


Play using the arrow keys (up, down, left, right) to move the snake.


How to Play

Objective: Eat Golden Apples (red) to earn points and progress through the levels.
Levels: Each level has a Minecraft biome and a point goal (5, 10, 15, 20, 25). Reach the goal to advance to the next level.
Challenges:
Starting from Level 2, Creepers (black) appear and move slowly. Colliding with them causes a game over.
In Levels 4 and 5, collect Ores and Quartz for +2 extra points.


Game Over: Colliding with the edges, your own tail, or a Creeper restarts the level.
Controls: Use the arrow keys to move the snake.

Project Structure

app.py: Flask backend that manages the game state (score, level, speed).
templates/index.html: Frontend with HTML, CSS, and JavaScript (p5.js) to render the game in the browser.

Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a branch for your feature (git checkout -b feature/new-feature).
Commit your changes (git commit -m 'Add new feature').
Push to the remote repository (git push origin feature/new-feature).
Open a Pull Request.

Common Issues and Solutions

Game doesn't load in the browser:
Ensure Flask is running (python app.py).
Verify the file structure (index.html must be in templates/).
Open the browser console (F12 > Console) and check for errors.


Error "Address already in use":
Port 5000 is occupied. Change the port in app.py (e.g., app.run(debug=True, port=5001)).


p5.js doesn't load:
Ensure you're connected to the internet, as p5.js is loaded via CDN.



Credits

Developed by Sam_Ara for a personal project.
Inspired by the classic Snake game and Minecraft's visual style.

License
This project is licensed under the MIT License.





PORTUGUÊS - BRASIL
Jogo da Cobrinha - Estilo Minecraft
Bem-vindo ao Jogo da Cobrinha no estilo Minecraft! Este é um jogo simples e divertido, projetado para crianças (como minha sobrinha de 6 anos), com um tema inspirado no universo pixelado do Minecraft. O jogo foi desenvolvido usando Python com Flask para o backend e p5.js para o frontend, rodando em um navegador.
Descrição
Neste jogo, você controla uma cobrinha que se move em uma grade, comendo frutas (Maçãs Douradas) para crescer e ganhar pontos. O jogo tem 5 fases, cada uma com um bioma diferente do Minecraft (Planície, Floresta, Deserto, Montanha e Nether). A velocidade aumenta a cada fase, começando em 0.5 e indo até 2.0. Há desafios como Creepers (inimigos) e blocos interativos (Minérios e Quartzo) que dão pontos extras.
Características

Fases Temáticas: 5 biomas do Minecraft que mudam a cada fase.
Velocidade Progressiva: Começa em 0.5 e aumenta até 2.0.
Inimigos: Creepers aparecem a partir da Fase 2 e causam game over se colidirem com a cobrinha.
Blocos Interativos: Minérios e Quartzo (Fases 4 e 5) dão +2 pontos ao serem coletados.
Design Amigável: Visual colorido e controles simples (setas do teclado) para crianças.
Legenda Externa: Itens do jogo (Maçã Dourada, Creeper, Minério, Quartzo) são explicados em uma legenda fora do quadro de jogo.

Tecnologias Utilizadas

Backend: Python 3 com Flask
Frontend: HTML, JavaScript com p5.js
Estilização: CSS básico

Pré-requisitos

Python 3.x instalado
Navegador moderno (Chrome, Firefox, etc.)
Conexão com a internet (para carregar a biblioteca p5.js via CDN)

Instalação

Clone o repositório para sua máquina:
git clone <URL_DO_REPOSITORIO>
cd jogo_cobrinha


Crie um ambiente virtual (opcional, mas recomendado):
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate


Instale as dependências:
pip install flask


Verifique a estrutura de arquivos:
jogo_cobrinha/
├── app.py
├── templates/
│   └── index.html
├── README.md



Como Executar

Inicie o servidor Flask:
python app.py

O servidor será iniciado em http://127.0.0.1:5000. Se a porta 5000 estiver em uso, edite o app.py para usar outra porta (ex.: app.run(debug=True, port=5001)).

Abra o navegador e acesse:
http://127.0.0.1:5000


Jogue usando as setas do teclado (cima, baixo, esquerda, direita) para mover a cobrinha.


Como Jogar

Objetivo: Coma Maçãs Douradas (vermelhas) para ganhar pontos e avançar pelas fases.
Fases: Cada fase tem um bioma do Minecraft e um objetivo de pontos (5, 10, 15, 20, 25). Ao atingir o objetivo, você avança para a próxima fase.
Desafios:
A partir da Fase 2, Creepers (pretos) aparecem e se movem lentamente. Colidir com eles causa game over.
Nas Fases 4 e 5, colete Minérios e Quartzo para +2 pontos extras.


Game Over: Colidir com as bordas, com a própria cauda ou com um Creeper reinicia a fase.
Controles: Use as setas do teclado para mover a cobrinha.

Estrutura do Projeto

app.py: Backend Flask que gerencia o estado do jogo (pontuação, fase, velocidade).
templates/index.html: Frontend com HTML, CSS e JavaScript (p5.js) para renderizar o jogo no navegador.

Contribuição
Contribuições são bem-vindas! Para contribuir:

Faça um fork do repositório.
Crie uma branch para sua feature (git checkout -b feature/nova-feature).
Faça commit das suas alterações (git commit -m 'Adiciona nova feature').
Envie para o repositório remoto (git push origin feature/nova-feature).
Abra um Pull Request.

Problemas Comuns e Soluções

Jogo não carrega no navegador:
Verifique se o Flask está rodando (python app.py).
Confirme a estrutura de arquivos (index.html deve estar em templates/).
Abra o console do navegador (F12 > Console) e verifique erros.


Erro "Address already in use":
A porta 5000 está ocupada. Mude a porta no app.py (ex.: app.run(debug=True, port=5001)).


p5.js não carrega:
Certifique-se de estar conectado à internet, pois o p5.js é carregado via CDN.



Créditos

Desenvolvido por Sam_Ara para um projeto pessoal.
Inspirado no clássico jogo da cobrinha e no estilo visual do Minecraft.

Licença
Este projeto está licenciado sob a MIT License.
