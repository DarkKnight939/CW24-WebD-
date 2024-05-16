from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    # Make a GET request to the API endpoint
    api_url = 'https://coding-week-2024-api.onrender.com/api/data'
    response = requests.get(api_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        blogs_data = response.json()

        # Extract data for photo1
        photo1_data = blogs_data[0]
        photo2_data = blogs_data[1]
        photo3_data = blogs_data[2]
        photo4_data = blogs_data[3]
        photo5_data = blogs_data[4]
        photo6_data = blogs_data[5]
        photo7_data = blogs_data[6]
        photo8_data = blogs_data[7]

        # Pass the data to the HTML template
        return render_template('index.html', photo1_image=photo1_data.get('image'), photo1_type=photo1_data.get('type'),
                               photo1_headline=photo1_data.get('headline')[0:40] + "...",photo1_author=photo1_data.get('author'),photo1_date=photo1_data.get('date'),
                               photo2_image=photo2_data.get('image'), photo2_type=photo2_data.get('type'),
                               photo2_headline=photo2_data.get('headline')[0:15] + "...", photo2_author=photo2_data.get('author'),photo2_date=photo2_data.get('date'),
                               photo3_image=photo3_data.get('image'), photo3_type=photo3_data.get('type'),
                               photo3_headline=photo3_data.get('headline')[0:20] + "...", photo3_author=photo3_data.get('author'),photo3_date=photo3_data.get('date'),
                               photo4_image=photo4_data.get('image'), photo4_type=photo4_data.get('type'),
                               photo4_headline=photo4_data.get('headline')[0:20] + "...",photo4_author=photo4_data.get('author'),photo4_date=photo4_data.get('date'),
                               photo5_image=photo5_data.get('image'), photo5_headline=photo5_data.get('headline')[0:20] + "...", photo5_date=photo5_data.get('date'),
                               photo6_image=photo6_data.get('image'), photo6_headline=photo6_data.get('headline')[0:20] + "...", photo6_date=photo6_data.get('date'),
                               photo7_image=photo7_data.get('image'), photo7_headline=photo7_data.get('headline')[0:20] + "...", photo7_date=photo7_data.get('date'),
                               photo8_image=photo8_data.get('image'), photo8_headline=photo8_data.get('headline')[0:20] + "...", photo8_date=photo8_data.get('date'))
    else:
        # Handle the error case
        return "Failed to fetch data from the API"


if __name__ == '__main__':
    app.run(debug=True)
