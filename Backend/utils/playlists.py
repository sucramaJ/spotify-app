import spotipy
import dotenv
import os

dotenv.load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

print(CLIENT_SECRET)