from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)

@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github)
    return html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""
    return render_template("student_search.html")

@app.route('/student-add-new')
def add_new_student_form():
  return render_template("new_student.html")  

@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student."""
    Fname = request.form.get("fname")
    Lname = request.form.get("lname")
    Github = request.form.get("github")
    hackbright.make_new_student(Fname, Lname, Github)
    return render_template('new_student_confirm.html', fname=Fname, lname=Lname, github=Github)
    
                         


if __name__ == "__main__":
    app.run(debug=True)