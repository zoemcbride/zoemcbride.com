from flask import Flask, render_template, current_app
from utils import calculate_reading_time, count_words 
import json 
import os

app = Flask(__name__, template_folder='templates')

# Use debug = True to automatically reload localhost page when 
# changes are made
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/side_projects.html')
def side_projects():
    return render_template('side_projects.html')

@app.route('/running_analysis_blog.html')
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

@app.route('/restaurant_recommendations.html')
def restaurant_recommendations():
    return render_template('restaurant_recommendations.html')

@app.route('/strava_analysis_howto.html')
def strava_analysis_howto():
    return render_template('strava_analysis_howto.html')

# Construct an absolute path to the data directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_REVIEWS_DATA_FILE = os.path.join(BASE_DIR, 'data', 'book_reviews.json')

with open(BOOK_REVIEWS_DATA_FILE, 'r') as f:
    reviews = json.load(f)

@app.route('/book_reviews.html')
def book_reviews():
    return render_template('book_reviews.html', reviews=reviews)

@app.route('/energy_analysis_blog.html')
def energy_analysis_blog():
    # Specify the path relative to the template folder
    html_file_path = 'templates/energy_analysis_blog.html'  # Adjust the path accordingly

    # open(html_file_path, 'r')
    # Read the content of your running analysis blog post from the HTML file
    with current_app.open_resource(html_file_path, 'r') as blog_file:
        blog_post_content = blog_file.read() # Note that this technically counts all words on the html file, including html coding
    
    # Calculate reading time using the calculate_reading_time function
    reading_time_minutes = calculate_reading_time(blog_post_content)
    
    return render_template('energy_analysis_blog.html', content=blog_post_content, word_count=count_words(blog_post_content), reading_time=reading_time_minutes)


if __name__ == '__main__':
    app.run()