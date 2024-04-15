from flask import Flask, render_template
app = Flask(__name__)


quiz_data = {
    1: {
        'title': 'Geography',
        'questions': [
            {'question_text': 'What is the capital of France?', 'options': ['Berlin', 'London', 'Paris', 'Madrid'], 'correct_option': 2},
            {'question_text': 'What is the capital of Turkey?', 'options': ['Sofia', 'Istanbul', 'Ankara', 'Damascus'], 'correct_option': 0},
            {'question_text': 'What is the capital of Nigeria?', 'options': ['Umuahia', 'Abuja', 'Yola', 'Makurdi'], 'correct_option': 1},
        ]
    }
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/quizzes')
def quizzes():
    return render_template('quizzes.html', quizzes=quiz_data)


if __name__ == '__main__':
    app.run(debug=True)
