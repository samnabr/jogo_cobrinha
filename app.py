from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Estado inicial do jogo
game_state = {
    'score': 0,
    'level': 1,
    'game_over': False,
    'speed': 5
}

# Objetivos de pontos por nível
level_goals = {1: 5, 2: 10, 3: 15, 4: 20, 5: 25}
# Velocidades por nível (FPS)
level_speeds = {1: 5, 2: 8, 3: 12, 4: 16, 5: 20}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game_state', methods=['GET'])
def get_game_state():
    return jsonify(game_state)

@app.route('/update_state', methods=['POST'])
def update_state():
    global game_state
    data = request.json
    game_state['score'] = data['score']
    
    # Verifica se atingiu o objetivo do nível
    current_level = game_state['level']
    if current_level <= 5 and game_state['score'] >= level_goals[current_level]:
        if current_level < 5:
            game_state['level'] += 1
            game_state['speed'] = level_speeds[game_state['level']]
            game_state['score'] = 0
        else:
            game_state['game_over'] = True
    
    return jsonify(game_state)

@app.route('/reset', methods=['POST'])
def reset():
    global game_state
    game_state = {
        'score': 0,
        'level': 1,
        'game_over': False,
        'speed': 5
    }
    return jsonify(game_state)

if __name__ == '__main__':
    app.run(debug=True)