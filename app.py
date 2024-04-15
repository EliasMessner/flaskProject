from flask import Flask, render_template, redirect, url_for, session, request

app = Flask(__name__)
app.secret_key = 'your_secret_key'


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
def home():
    return render_template('index.html')


@app.route('/quizzes')
def quizzes():
    return render_template('quizzes.html', quizzes=quiz_data)


@app.route('/quiz/<int:quiz_id>', methods=['GET', 'POST'])
def take_quiz(quiz_id):
    if request.method == 'POST':
        # Handle quiz submission
        session['user_answers'] = request.form
        return redirect(url_for('quiz_result', quiz_id=quiz_id))
    else:
        return render_template('quiz.html', quiz=quiz_data.get(quiz_id), quiz_id=quiz_id, enumerate=enumerate)


@app.route('/quiz/<int:quiz_id>/result')
def quiz_result(quiz_id):
    user_answers = {int(key): int(value) for key, value in session.get('user_answers', {}).items()}
    quiz = quiz_data.get(quiz_id)
    score = calculate_score(quiz['questions'], user_answers)
    return render_template('result.html', score=score)


def calculate_score(questions, user_answers):
    correct_answers = 0
    for question_index, question in enumerate(questions):
        if question_index in user_answers and user_answers[question_index] == question['correct_option']:
            correct_answers += 1
    return correct_answers


if __name__ == '__main__':
    app.run(debug=True)
