import os
import json
import random
import tempfile
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)
app.secret_key = 'super_secret_exam_key' # Replace with a real secret key in production

# Load questions
with open('questions.json', 'r') as f:
    QUESTIONS = json.load(f)

# Helper for Leaderboard
LEADERBOARD_FILE = os.path.join(tempfile.gettempdir(), 'leaderboard.json')
def get_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        return []
    with open(LEADERBOARD_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_to_leaderboard(name, branch, score_num, total_num):
    board = get_leaderboard()
    
    # Check if student already exists in the leaderboard
    existing_student = next((item for item in board if item['name'] == name), None)
    
    if existing_student:
        # Update score only if the new score is higher
        if score_num > existing_student['score']:
            existing_student['score'] = score_num
            existing_student['total'] = total_num
            existing_student['branch'] = branch
    else:
        # Add new student
        board.append({
            'name': name,
            'branch': branch,
            'score': score_num,
            'total': total_num
        })
        
    # Sort descending by score
    board.sort(key=lambda x: x['score'], reverse=True)
    
    with open(LEADERBOARD_FILE, 'w') as f:
        json.dump(board, f, indent=4)
    return board

APPS_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbzna3EKmmGhHo6G35EwqGWXi4MEpr1gC_XxYIXanulihZcy4uWbjVct1neSEEr8SL7l6w/exec'

def save_to_google_sheet(first_name, surname, branch, batch, score, warnings_count):
    try:
        data = {
            'first_name': first_name,
            'surname': surname,
            'branch': branch,
            'batch': batch,
            'score': score,
            'warnings_count': warnings_count
        }
        
        # Depending on how the Apps Script is written, it might expect JSON or form data.
        # Most simple doPost(e) scripts expect form data, but let's try JSON first or form data if it fails.
        # Standard approach for Google Apps Script Web App without CORS issues is to post form data or JSON.
        # Sending as JSON payload:
        response = requests.post(APPS_SCRIPT_URL, json=data, verify=False)
        
        # If the Apps Script expects form data (x-www-form-urlencoded), we would use:
        # response = requests.post(APPS_SCRIPT_URL, data=data)
        
        if response.status_code in [200, 201]:
            print("Successfully saved to Google Sheets.")
            return True
        else:
            print(f"Failed to save to Google Sheets. Status code: {response.status_code}, Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"Error saving to Google Sheets webhook: {e}")
        return False

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['first_name'] = request.form.get('first_name')
        session['surname'] = request.form.get('surname')
        session['branch'] = request.form.get('branch')
        session['batch'] = request.form.get('batch')
        session['warnings'] = 0
        return redirect(url_for('exam'))
    return render_template('index.html')

@app.route('/exam', methods=['GET'])
def exam():
    if 'first_name' not in session:
        return redirect(url_for('index'))
    
    # Use all questions
    import copy
    exam_questions = copy.deepcopy(QUESTIONS)
    
    # Shuffle questions
    random.shuffle(exam_questions)
    
    # Shuffle options for each question
    for q in exam_questions:
        random.shuffle(q['options'])
    
    # Time limit: 1 minute per question
    time_limit_minutes = len(exam_questions)
    
    return render_template('exam.html', questions=exam_questions, student_name=f"{session['first_name']} {session['surname']}", time_limit=time_limit_minutes)

@app.route('/record_warning', methods=['POST'])
def record_warning():
    if 'warnings' in session:
        session['warnings'] += 1
        return jsonify({"status": "success", "warnings": session['warnings']})
    return jsonify({"status": "ignored", "message": "Session already cleared"}), 200

@app.route('/submit', methods=['POST'])
def submit():
    if 'first_name' not in session:
        return redirect(url_for('index'))
        
    branch = session.get('branch')
    exam_questions = QUESTIONS
    
    score = 0
    total = len(exam_questions)
    
    breakdown = []
    
    for q in exam_questions:
        ans = request.form.get(f"question_{q['id']}")
        is_correct = False
        
        if ans:
            is_correct = (ans == q['answer'])
            if is_correct:
                score += 1
            else:
                score -= 2
            
        breakdown.append({
            'question': q['question'],
            'user_answer': ans,
            'correct_answer': q['answer'],
            'is_correct': is_correct
        })
            
    # Save to Google Sheets
    save_to_google_sheet(
        session.get('first_name'),
        session.get('surname'),
        branch,
        session.get('batch'),
        f"{score}/{total}",
        session.get('warnings')
    )
    
    # Prepare result data before clearing session
    student_name = f"{session['first_name']} {session['surname']}"
    result_data = {
        'name': student_name,
        'score': score,
        'total': total,
        'warnings': session.get('warnings'),
        'breakdown': breakdown
    }
    
    # Save to local leaderboard and get top 5
    full_leaderboard = save_to_leaderboard(student_name, branch, score, total)
    top_5 = full_leaderboard[:5]
    
    session.clear()
    
    return render_template('result.html', result=result_data, leaderboard=top_5)

if __name__ == '__main__':
    app.run(debug=True)
