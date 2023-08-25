# hogwarts-sorting-hat-spotify

The application retrieves a user's Spotify data after they input their credentials, and then employs a sorting algorithm to categorize them into a Hogwarts house based on their music taste. This algorithm considers the distinct traits associated with each Harry Potter house as well as the user's top genres, artists, and tracks to determine which house the user belongs to. This is a full-stack application that uses Django for the backend and React for the frontend.

# Setup Instructions

### Create a Spotify Developer Account:
If you don't already have one, sign up for a Spotify Developer Account at the Spotify Developer Dashboard: https://developer.spotify.com/dashboard/

### Create a New App:
Once logged in to the Spotify Developer Dashboard, create a new application by clicking on the "Create an App" button. Provide the required details for your app.

### Retrieve Client ID and Client Secret:
After creating the app, you'll be given a Client ID and Client Secret. These are crucial for authenticating your application with the Spotify API. 

In the sorting_hat/credentials.py file, replace the Client ID and Client Secret placeholders with your own.

### Configure Redirect URI:
Configure the Redirect URI in your Spotify app settings to http://127.0.0.1:8000. This is the URL where the user will be redirected after they grant access to your app.

### Start Web Server

To start the web server you need to run the following sequence of commands.

First cd into your desired tutorial folder (replace x with tutorial number).
```bash 
cd "Tutorial x"
```
Next run the django web server.
```bash
python manage.py runserver
```

