import re

def update_index():
    with open('templates/index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_style = """    <style>
        :root {
            --yellow: #FCC206;
            --gray-dark: #374151;
            --gray-light: #F9FAFB;
            --gray-border: #E5E7EB;
            --white: #FFFFFF;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Inter', sans-serif; }

        body {
            background: var(--gray-light);
            color: var(--gray-dark);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            position: relative;
        }

        .bg-animation {
            position: absolute; top: 0; left: 0; right: 0; bottom: 0;
            background: radial-gradient(ellipse at 50% 0%, #ffffff 0%, #f3f4f6 50%, #e5e7eb 100%);
            z-index: 0;
        }
        .bg-animation::before {
            content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
            background: 
                radial-gradient(circle at 20% 50%, rgba(252, 194, 6, 0.15) 0%, transparent 50%),
                radial-gradient(circle at 80% 50%, rgba(55, 65, 81, 0.08) 0%, transparent 50%);
            animation: gradientShift 15s ease infinite;
        }
        .bg-animation::after {
            content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
            background-image: 
                linear-gradient(rgba(55, 65, 81, 0.05) 1px, transparent 1px),
                linear-gradient(90deg, rgba(55, 65, 81, 0.05) 1px, transparent 1px);
            background-size: 50px 50px;
        }
        @keyframes gradientShift { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.1); } }

        .container {
            position: relative; z-index: 2; width: 100%; max-width: 500px; padding: 20px;
            animation: fadeInUp 0.8s ease-out forwards;
        }
        @keyframes fadeInUp { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: translateY(0); } }

        .card { 
            background: var(--white);
            border: 1px solid var(--gray-border);
            border-radius: 16px; 
            padding: 2.5rem;
            box-shadow: 0 20px 40px rgba(0,0,0,0.08);
            transition: all 0.3s ease;
        }
        
        .logo-box {
            background: var(--gray-dark);
            padding: 1.5rem;
            border-radius: 12px;
            text-align: center;
            margin-bottom: 2rem;
            box-shadow: inset 0 0 20px rgba(0,0,0,0.2);
        }
        .logo-box img { max-height: 45px; }

        .form-label {
            display: block; margin-bottom: 0.5rem; font-size: 0.85rem;
            color: var(--gray-dark); font-weight: 600; text-transform: uppercase; letter-spacing: 1px;
        }
        .form-control, .form-select {
            width: 100%; padding: 1rem; margin-bottom: 1.5rem;
            background: #F3F4F6; border: 1px solid var(--gray-border);
            border-radius: 8px; color: var(--gray-dark);
            font-family: inherit; font-size: 1rem; transition: all 0.3s;
        }
        .form-control:focus, .form-select:focus {
            outline: none; border-color: var(--yellow); background: var(--white);
            box-shadow: 0 0 0 4px rgba(252, 194, 6, 0.15); transform: translateY(-2px);
        }

        .radio-group { display: flex; gap: 1rem; margin-bottom: 2rem; }
        .radio-label {
            flex: 1; display: flex; align-items: center; justify-content: center; gap: 0.5rem;
            cursor: pointer; padding: 1rem; background: #F3F4F6;
            border: 1px solid var(--gray-border); border-radius: 8px; transition: all 0.3s; font-weight: 500;
        }
        .radio-label:hover { background: var(--white); border-color: var(--yellow); }
        .radio-label input:checked + span { color: var(--gray-dark); font-weight: 700; }
        .radio-label input { accent-color: var(--yellow); width: 1.2rem; height: 1.2rem; }
        .radio-label:has(input:checked) { background: #FFF9E6; border-color: var(--yellow); }

        .btn-primary {
            width: 100%; padding: 1.2rem; border: none; border-radius: 50px;
            background: var(--yellow); color: var(--gray-dark); font-weight: 800; font-size: 1.1rem;
            cursor: pointer; transition: all 0.3s;
            box-shadow: 0 10px 20px rgba(252, 194, 6, 0.3); letter-spacing: 0.5px;
        }
        .btn-primary:hover {
            transform: translateY(-4px); box-shadow: 0 15px 30px rgba(252, 194, 6, 0.4);
            background: #FFD000;
        }
    </style>"""
    
    content = re.sub(r'<style>.*?</style>', new_style, content, flags=re.DOTALL)
    
    new_header = """<div class="logo-box">
                <img src="{{ url_for('static', filename='DoxPro_logo_white.png') }}" alt="DoxPro Logo">
            </div>"""
    content = re.sub(r'<h2 class="title">.*?</h2>', new_header, content)
    
    with open('templates/index.html', 'w', encoding='utf-8') as f:
        f.write(content)


def update_exam():
    with open('templates/exam.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_style = """    <style>
        :root {
            --yellow: #FCC206;
            --gray-dark: #374151;
            --gray-light: #F9FAFB;
            --gray-border: #E5E7EB;
            --white: #FFFFFF;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Inter', sans-serif; }

        body {
            background: var(--gray-light);
            color: var(--gray-dark);
            min-height: 100vh;
            position: relative;
        }

        .bg-animation {
            position: fixed; top: 0; left: 0; right: 0; bottom: 0;
            background: radial-gradient(ellipse at 50% 0%, #ffffff 0%, #f3f4f6 50%, #e5e7eb 100%);
            z-index: -1;
        }
        .bg-animation::before {
            content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
            background: 
                radial-gradient(circle at 20% 50%, rgba(252, 194, 6, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 80% 50%, rgba(55, 65, 81, 0.05) 0%, transparent 50%);
            animation: gradientShift 20s ease infinite;
        }
        .bg-animation::after {
            content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
            background-image: 
                linear-gradient(rgba(55, 65, 81, 0.05) 1px, transparent 1px),
                linear-gradient(90deg, rgba(55, 65, 81, 0.05) 1px, transparent 1px);
            background-size: 50px 50px;
        }
        @keyframes gradientShift { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.1); } }

        .container {
            width: 100%; max-width: 800px; margin: 0 auto;
            padding: 6rem 1rem 4rem;
        }

        .header {
            position: fixed; top: 0; left: 0; right: 0; height: 80px;
            background: var(--gray-dark);
            border-bottom: 4px solid var(--yellow);
            display: flex; justify-content: center; align-items: center; z-index: 1000;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        }
        .header-content {
            width: 100%; max-width: 800px; display: flex; justify-content: space-between; align-items: center; padding: 0 1rem;
        }
        .header h2 {
            margin: 0; color: var(--white); font-weight: 800; font-size: 1.5rem; letter-spacing: -0.5px;
        }
        .header h2 span { color: var(--yellow); }
        .header-logo { display: flex; align-items: center; gap: 12px; }
        .header-logo img { max-height: 40px; }

        .badge {
            background: rgba(255, 255, 255, 0.1); border: 1px solid rgba(255, 255, 255, 0.2);
            color: var(--white); padding: 0.5rem 1.2rem; border-radius: 50px; font-size: 0.9rem; font-weight: 600;
        }
        
        .timer-badge {
            background: rgba(220, 53, 69, 0.1); border: 1px solid rgba(220, 53, 69, 0.5);
            color: #dc3545; padding: 0.5rem 1.2rem; border-radius: 50px; font-size: 1.1rem;
            font-weight: 800; font-variant-numeric: tabular-nums; background: #fff; box-shadow: 0 0 10px rgba(220,53,69,0.2);
        }
        .timer-badge.safe {
            background: #fff; border-color: rgba(40, 167, 69, 0.5); color: #28a745;
            box-shadow: 0 0 10px rgba(40,167,69,0.2);
        }

        .alert {
            display: none; background: #FEF2F2; border: 1px solid #F87171; color: #DC2626;
            padding: 1.5rem; border-radius: 12px; margin-bottom: 2rem;
            animation: slideDown 0.5s ease-out forwards;
        }
        @keyframes slideDown { from { transform: translateY(-20px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }

        .question-card { 
            background: var(--white); border: 1px solid var(--gray-border);
            border-radius: 16px; padding: 2.5rem; margin-bottom: 2rem;
            opacity: 0; transform: translateY(30px); animation: fadeInUp 0.6s ease-out forwards;
            box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        }
        @keyframes fadeInUp { to { opacity: 1; transform: translateY(0); } }

        .question-card h5 {
            margin-top: 0; margin-bottom: 2rem; font-size: 1.25rem; font-weight: 600; line-height: 1.6; color: var(--gray-dark);
        }

        .options-grid { display: grid; grid-template-columns: 1fr; gap: 1rem; }
        @media (min-width: 600px) { .options-grid { grid-template-columns: 1fr 1fr; } }

        .option-label {
            position: relative; display: flex; align-items: center; padding: 1.2rem;
            background: #F9FAFB; border: 1px solid var(--gray-border); border-radius: 12px;
            cursor: pointer; transition: all 0.3s; font-weight: 500; color: var(--gray-dark);
        }
        .option-label:hover {
            background: #FFFFFF; border-color: var(--yellow); transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(252, 194, 6, 0.1);
        }
        .option-label input[type="radio"] { position: absolute; opacity: 0; cursor: pointer; }

        .option-label input[type="radio"]:checked + .option-text { font-weight: 700; color: var(--gray-dark); }
        .option-label:has(input[type="radio"]:checked) {
            background: #FFF9E6; border-color: var(--yellow);
            box-shadow: 0 0 0 2px var(--yellow);
        }

        .btn-success {
            width: 100%; padding: 1.2rem; border: none; border-radius: 50px;
            background: var(--yellow); color: var(--gray-dark); font-weight: 800; font-size: 1.2rem;
            cursor: pointer; transition: all 0.3s; box-shadow: 0 10px 20px rgba(252, 194, 6, 0.3);
            margin-top: 1rem; letter-spacing: 0.5px;
        }
        .btn-success:hover {
            transform: translateY(-4px); box-shadow: 0 15px 30px rgba(252, 194, 6, 0.4); background: #FFD000;
        }
    </style>"""
    
    content = re.sub(r'<style>.*?</style>', new_style, content, flags=re.DOTALL)
    
    new_header = """<div class="header">
        <div class="header-content">
            <div class="header-logo">
                <img src="{{ url_for('static', filename='DoxPro_logo_white.png') }}" alt="DoxPro Logo">
                <h2>DoxPro <span>Portal</span></h2>
            </div>
            <div style="display: flex; gap: 1rem; align-items: center;">"""
    
    content = re.sub(r'<div class="header">\s*<div class="header-content">\s*<h2>.*?</h2>\s*<div style="display: flex; gap: 1rem; align-items: center;">', new_header, content, flags=re.DOTALL)
    
    with open('templates/exam.html', 'w', encoding='utf-8') as f:
        f.write(content)


def update_result():
    with open('templates/result.html', 'r', encoding='utf-8') as f:
        content = f.read()
        
    new_style = """    <style>
        :root {
            --yellow: #FCC206;
            --gray-dark: #374151;
            --gray-light: #F9FAFB;
            --gray-border: #E5E7EB;
            --white: #FFFFFF;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Inter', sans-serif; }

        body {
            background: var(--gray-light);
            color: var(--gray-dark);
            min-height: 100vh;
            display: flex;
            align-items: flex-start;
            justify-content: center;
            padding: 4rem 1rem;
        }

        .bg-animation {
            position: fixed; top: 0; left: 0; right: 0; bottom: 0;
            background: radial-gradient(ellipse at 50% 0%, #ffffff 0%, #f3f4f6 50%, #e5e7eb 100%);
            z-index: -1;
        }
        .bg-animation::before {
            content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
            background: 
                radial-gradient(circle at 30% 60%, rgba(252, 194, 6, 0.1) 0%, transparent 40%),
                radial-gradient(circle at 70% 40%, rgba(55, 65, 81, 0.05) 0%, transparent 40%);
            animation: gradientShift 20s ease infinite alternate;
        }
        @keyframes gradientShift { 0% { transform: scale(1); } 100% { transform: scale(1.1); } }

        .container {
            width: 100%; max-width: 800px; display: flex; flex-direction: column; gap: 2rem;
            z-index: 1;
        }

        .card { 
            background: var(--white);
            border: 1px solid var(--gray-border);
            border-radius: 16px; 
            padding: 3rem 2rem;
            box-shadow: 0 20px 40px rgba(0,0,0,0.08);
            text-align: center;
            animation: fadeInUp 0.8s ease-out forwards;
        }
        @keyframes fadeInUp { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: translateY(0); } }

        .logo-box {
            background: var(--gray-dark);
            padding: 1.5rem;
            border-radius: 12px;
            display: inline-block;
            margin-bottom: 2rem;
            box-shadow: inset 0 0 20px rgba(0,0,0,0.2);
        }
        .logo-box img { max-height: 50px; }

        .title {
            font-weight: 800; margin-bottom: 1rem; color: var(--gray-dark);
            font-size: 1.5rem; text-transform: uppercase; letter-spacing: 2px;
        }

        .student-name {
            font-size: 1.2rem; color: #4B5563; margin-bottom: 1rem; font-weight: 600;
        }

        .score-display {
            font-size: 5rem; font-weight: 900; color: var(--yellow); margin: 1.5rem 0;
            text-shadow: 0 4px 15px rgba(252, 194, 6, 0.3);
            animation: popIn 1s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
            opacity: 0; transform: scale(0.5);
        }
        @keyframes popIn { to { opacity: 1; transform: scale(1); } }

        .alert-warning {
            background: #FEF2F2; border: 1px solid #F87171; color: #DC2626;
            padding: 1rem; border-radius: 8px; margin: 1.5rem auto; max-width: 400px; font-weight: 600;
        }

        .btn-outline {
            display: inline-block; padding: 1rem 2.5rem; border: 2px solid var(--yellow);
            border-radius: 50px; background: var(--white); color: var(--gray-dark);
            font-weight: 700; text-decoration: none; transition: all 0.3s;
            margin-top: 1rem; text-transform: uppercase; letter-spacing: 1px;
        }
        .btn-outline:hover {
            background: var(--yellow); color: var(--gray-dark);
            transform: translateY(-2px); box-shadow: 0 10px 20px rgba(252, 194, 6, 0.2);
        }
        
        .leaderboard-card { text-align: left; padding: 2rem; animation-delay: 0.3s; }
        .leaderboard-title {
            color: var(--gray-dark); text-align: center; font-weight: 800;
            font-size: 1.5rem; margin-bottom: 2rem;
        }
        
        .leaderboard-list { list-style: none; display: flex; flex-direction: column; gap: 1rem; }
        
        .leaderboard-item {
            display: flex; align-items: center; padding: 1.2rem;
            background: #F9FAFB; border: 1px solid var(--gray-border); border-radius: 12px;
            transition: all 0.3s; opacity: 0; transform: translateX(-20px);
            animation: slideInRight 0.5s ease-out forwards;
        }
        @keyframes slideInRight { to { opacity: 1; transform: translateX(0); } }
        .leaderboard-item:hover { background: #FFFFFF; transform: translateX(5px); box-shadow: 0 4px 12px rgba(0,0,0,0.05); }

        .rank { font-weight: 800; font-size: 1.2rem; color: #9CA3AF; width: 40px; }
        
        .leaderboard-item:nth-child(1) .rank { color: #F59E0B; }
        .leaderboard-item:nth-child(2) .rank { color: #9CA3AF; }
        .leaderboard-item:nth-child(3) .rank { color: #B45309; }

        .student-info { flex-grow: 1; }
        .student-name-lb { font-weight: 600; font-size: 1.1rem; color: var(--gray-dark); display: block; }
        .student-branch {
            font-size: 0.85rem; color: #6B7280; text-transform: uppercase; letter-spacing: 1px; margin-top: 0.2rem;
        }
        .student-score {
            font-weight: 800; color: var(--gray-dark); font-size: 1.3rem;
            background: #FFF9E6; border: 1px solid rgba(252,194,6,0.3); padding: 0.5rem 1rem; border-radius: 8px;
        }
        
        .highlight-student {
            background: #FFF9E6 !important; border-color: var(--yellow);
            box-shadow: 0 0 0 2px var(--yellow);
        }
    </style>"""
    
    content = re.sub(r'<style>.*?</style>', new_style, content, flags=re.DOTALL)
    
    new_header = """<div class="logo-box">
                <img src="{{ url_for('static', filename='DoxPro_logo_white.png') }}" alt="DoxPro Logo">
            </div>
            <h2 class="title">Exam Results</h2>"""
    content = re.sub(r'<h2 class="title">Exam Results</h2>', new_header, content)
    
    content = re.sub(r'<span class="student-name">{{ entry\.name }}', r'<span class="student-name-lb">{{ entry.name }}', content)
    
    with open('templates/result.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    update_index()
    update_exam()
    update_result()
    print("UI updated successfully")
