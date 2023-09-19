from flask import Flask, render_template, current_app
from utils import calculate_reading_time, count_words  

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
    # Specify the path relative to the template folder
    html_file_path = 'templates/running_analysis_blog.html'  # Adjust the path accordingly

    # open(html_file_path, 'r')
    # Read the content of your running analysis blog post from the HTML file
    with current_app.open_resource(html_file_path, 'r') as blog_file:
        blog_post_content = blog_file.read() # Note that this technically counts all words on the html file, including html coding
    
    # Calculate reading time using the calculate_reading_time function
    reading_time_minutes = calculate_reading_time(blog_post_content)
    
    return render_template('running_analysis_blog.html', content=blog_post_content, word_count=count_words(blog_post_content), reading_time=reading_time_minutes)




if __name__ == '__main__':
    app.run()