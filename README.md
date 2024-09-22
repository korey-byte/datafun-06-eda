# datafun-06-eda
CC6.1: Start a New Project (w/Local Project Virtual Env)
Core Competency: Start a new Project & Create and Manage a Local Project Virtual Environment

Create and Activate Project Virtual Environment

python3 -m venv .venv source .venv\bin\Activate

Install Dependencies

py -m pip install -r "requirements.txt"

Freeze Requirements

py -m pip freeze > requirements.txt

Git Add / Commit / Push

git add . 
git commit -m "add .gitignore, commands to README.md" 
git push -u origin main