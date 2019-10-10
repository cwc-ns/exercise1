from flask import Flask, render_template

app = Flask(__name__, 
            static_url_path='', 
            static_folder='./static',
            template_folder='./templates')

@app.route("/")
def index():
    course = 'CN1 Lab Work'
    year = 2019
    instructions = {}
    instructions["title"] = "Instructions:"
    instructions["message"] = "The lab works are designed to get familier with few virtualization\
                            technologies. You will need to complete all the exercises to pass the course."
    return render_template('index.html', course=course, year=year, instructions=instructions)

    
if __name__ == "__main__":
    app.run()