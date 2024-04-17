from flask import Flask, render_template, redirect, url_for, session, request

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # we need to define this once here, so we can access the sessions variable everywhere


quiz_data = {
    1: {
        'title': 'Geography',
        'questions': [
            {'question_text': 'What is the capital of France?', 'options': ['Berlin', 'London', 'Paris', 'Madrid'], 'correct_option': 2},
            {'question_text': 'What is the capital of Turkey?', 'options': ['Sofia', 'Istanbul', 'Ankara', 'Damascus'], 'correct_option': 2},
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
    if request.method == 'GET':
        return render_template('quiz.html', quiz=quiz_data[quiz_id], quiz_id=quiz_id, enumerate=enumerate)
    else:
        # Handle quiz submission
        session['user_answers'] = request.form
        return redirect(url_for('quiz_result', quiz_id=quiz_id))


@app.route('/quiz/<int:quiz_id>/result')
def quiz_result(quiz_id):
    user_answers = {int(key): int(value) for key, value in session['user_answers'].items()}  # convert all keys and values from string to int
    quiz = quiz_data[quiz_id]
    correct_answers, total_answers = calculate_score(quiz['questions'], user_answers)
    return render_template('result.html', correct=correct_answers, total=total_answers)


def calculate_score(questions, user_answers):
    correct_answers = 0
    for question_index, question in enumerate(questions):
        if question_index in user_answers.keys() and user_answers[question_index] == question['correct_option']:  # the condition 'question_index in user_answers.keys()' ensures that we don't get an error if the user skipped a question
            correct_answers += 1
    return correct_answers, len(questions)


if __name__ == '__main__':
    app.run(debug=True)
