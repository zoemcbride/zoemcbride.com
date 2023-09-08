from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

# Use debug = True to automatically reload localhost page when 
# changes are made
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/side_projects')
def side_projects():
    return render_template('side_projects.html')

@app.route('/running_analysis_blog')
def running_analysis_blog():
    return render_template('running_analysis_blog.html')

if __name__ == '__main__':
    app.run()