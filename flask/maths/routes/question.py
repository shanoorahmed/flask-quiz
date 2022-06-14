from flask import Blueprint, render_template, redirect, url_for, flash, request
from maths.extensions import db
from flask_login import login_required, current_user
from maths.models import Question
from maths.timings import start, end
from datetime import datetime

question = Blueprint('question', __name__)

@question.route('/questions', methods=['GET', 'POST'])
@login_required
def questions():
    # if datetime.now() < start:
    #     flash("Event not started!", category="danger")
    #     return redirect(url_for('main.index'))

    # elif datetime.now() > end:
    #     current_user.attempt_no = 1
    #     current_user.question_no = 1
    #     current_user.bid_value = 0
    #     db.session.commit()
    #     flash("Event Finished", category = "danger")
    #     return redirect(url_for('main.thankyou'))
    
    # else:
        if request.method == 'POST':
            if request.form['submit_button'] == "skip_this_question":
                current_user.question_no = current_user.question_no+1
                current_user.score = current_user.score-current_user.bid_value
                current_user.attempt_no = 1
                current_user.bid_value = 0
                db.session.commit()
                if current_user.question_no == 21:
                    return redirect(url_for('main.thankyou'))
                return redirect(url_for('question.questionBid'))

            elif request.form['submit_button'] == "answer_this_question":
                answer=request.form['answer']
                shuffled_qno=int(request.form['shuffled_question_no'])

                questions = Question.query.all()
                easyList = [
                    current_user.first_question, 
                    current_user.second_question, 
                    current_user.third_question, 
                    current_user.fourth_question,
                    current_user.fifth_question,
                    current_user.sixth_question,
                    current_user.seventh_question,
                    current_user.eighth_question,
                    current_user.ninth_question,
                    current_user.tenth_question
                ]
                midList = [
                    current_user.eleventh_question,
                    current_user.twelfth_question,
                    current_user.thirteenth_question,
                    current_user.fourteenth_question,
                    current_user.fifteenth_question,
                    current_user.sixteenth_question
                ]
                hardList = [
                    current_user.seventeenth_question,
                    current_user.eighteenth_question,
                    current_user.nineteenth_question,
                    current_user.twentieth_question
                ]

                context = {
                    'questions' : questions,
                    'easyList' : easyList,
                    'midList' : midList,
                    'hardList' : hardList
                }

                # nowtime = end - datetime.now()
                # nowtime = str(nowtime)
                # hours = nowtime[0:1]
                # min = nowtime[2:4]
                # sec = nowtime[5:7] 
                # total = int(hours)*3600 + int(min)*60 + int(sec)

                for question in questions:
                    if question.question_number == shuffled_qno:
                        correct_ans = question.answer

                if answer==correct_ans:
                    current_user.question_no = current_user.question_no+1
                    current_user.score = current_user.score+2*current_user.bid_value
                    current_user.attempt_no = 1
                    current_user.bid_value = 0
                    current_user.last_answered = datetime.now()
                    db.session.commit()
                    flash("Correct!", category="success")
                    if current_user.question_no == 21:
                        return redirect(url_for('main.thankyou'))
                    return redirect(url_for('question.questionBid'))
                else:
                    current_user.attempt_no = current_user.attempt_no+1
                    if current_user.attempt_no < 4:
                        current_user.score = current_user.score-5
                        db.session.commit()
                        flash("Wrong!", category="danger")
                        # return render_template('questions.html', shuffled_qno = shuffled_qno, **context, total = total)
                        return render_template('questions.html', shuffled_qno = shuffled_qno, **context)
                    if current_user.attempt_no == 4:
                        current_user.attempt_no = 1
                        current_user.question_no = current_user.question_no+1
                        current_user.score = current_user.score-current_user.bid_value
                        current_user.bid_value = 0
                        db.session.commit()
                    flash("Wrong!", category="danger")
                    if current_user.question_no == 21:
                        return redirect(url_for('main.thankyou'))
                    return redirect(url_for('question.questionBid'))

        return render_template('questions.html')

@question.route('/question_bid', methods=['GET', 'POST'])
@login_required
def questionBid():
    # if datetime.now() < start:
    #     flash("Event not started!", category="danger")
    #     return redirect(url_for('main.index'))

    # elif datetime.now() > end:
    #     current_user.attempt_no = 1
    #     current_user.question_no = 1
    #     current_user.bid_value = 0
    #     db.session.commit()
    #     flash("Event Finished", category = "danger")
    #     return redirect(url_for('main.thankyou'))
    
    # else:
    questions = Question.query.all()
    easyList = [
        current_user.first_question, 
        current_user.second_question, 
        current_user.third_question, 
        current_user.fourth_question,
        current_user.fifth_question,
        current_user.sixth_question,
        current_user.seventh_question,
        current_user.eighth_question,
        current_user.ninth_question,
        current_user.tenth_question
    ]
    midList = [
        current_user.eleventh_question,
        current_user.twelfth_question,
        current_user.thirteenth_question,
        current_user.fourteenth_question,
        current_user.fifteenth_question,
        current_user.sixteenth_question
    ]
    hardList = [
        current_user.seventeenth_question,
        current_user.eighteenth_question,
        current_user.nineteenth_question,
        current_user.twentieth_question
    ]
    context = {
        'questions' : questions,
        'easyList' : easyList,
        'midList' : midList,
        'hardList' : hardList
    }
    # nowtime = end - datetime.now()
    # nowtime = str(nowtime)
    # hours = nowtime[0:1]
    # min = nowtime[2:4]
    # sec = nowtime[5:7]
    # total = int(hours)*3600 + int(min)*60 + int(sec)
    if request.method == 'POST':
        if request.form['submit_button'] == "bid_entered":
            bid_value = int(request.form['bid'])
            if current_user.question_no<=10:
                if bid_value<5 or bid_value>25:
                    flash("Enter a valid bid!", category="danger")
                    return redirect(url_for('question.questionBid'))
                else:
                    current_user.bid_value = bid_value
                    db.session.commit()
                    shuffled_qno = int(request.form['shuffled_question_no'])
                    # return render_template('questions.html', shuffled_qno = shuffled_qno, **context, total = total)
                    return render_template('questions.html', shuffled_qno = shuffled_qno, **context)
            elif current_user.question_no>=11 and current_user.question_no<=16:
                if bid_value<20 or bid_value>50:
                    flash("Enter a valid bid!", category="danger")
                    return redirect(url_for('question.questionBid'))
                else:
                    current_user.bid_value = bid_value
                    db.session.commit()
                    shuffled_qno = int(request.form['shuffled_question_no'])
                    # return render_template('questions.html', shuffled_qno = shuffled_qno, **context, total = total)
                    return render_template('questions.html', shuffled_qno = shuffled_qno, **context)
            elif current_user.question_no>=17 and current_user.question_no<=20:
                if bid_value<40 or bid_value>100:
                    flash("Enter a valid bid!", category="danger")
                    return redirect(url_for('question.questionBid'))
                else:
                    current_user.bid_value = bid_value
                    db.session.commit()
                    shuffled_qno = int(request.form['shuffled_question_no'])
                    # return render_template('questions.html', shuffled_qno = shuffled_qno, **context, total = total)
                    return render_template('questions.html', shuffled_qno = shuffled_qno, **context)
        elif request.form['submit_button'] == "skip_bid":
            current_user.question_no = current_user.question_no+1
            current_user.attempt_no = 1
            db.session.commit()
            if current_user.question_no == 21:
                return redirect(url_for('main.thankyou'))
            return redirect(url_for('question.questionBid'))
        elif request.form['submit_button'] == "go_back_to_question":
            shuffled_qno = int(request.form['shuffled_question_no'])
            # return render_template('questions.html', shuffled_qno = shuffled_qno, **context, total = total)
            return render_template('questions.html', shuffled_qno = shuffled_qno, **context)
    # return render_template('question_bid.html', **context, total = total)
    return render_template('question_bid.html', **context)

# @question.route('/addquestions', methods=['GET', 'POST'])
# @login_required
# def addquestion():
#     if request.method == 'POST':
#         questionnumber = request.form['questionnumber']
#         topic = request.form['topic']
#         image = request.form['image']
#         question = request.form['question']
#         answer = request.form['answer']

#         qno = Question.query.filter_by(question_number = questionnumber).first()

#         if qno:
#             flash("Question already exists!", category="danger")
#             return redirect(url_for('question.addquestion'))

#         question = Question(
#             question_number = questionnumber,
#             question_topic = topic,
#             question_img = image,
#             question = question,
#             answer = answer
#         )
#         db.session.add(question)
#         db.session.commit()
#         flash("Question Added!", category="success")
#         return redirect(url_for('question.addquestion'))

#     return render_template('addquestions.html')