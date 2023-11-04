import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "25435105")

API_HASH = os.environ.get("API_HASH", "011126265844f2d7cc7dc1a024f6bc78")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6431397060:AAGPfvfeIh_3d8bUstZbAPVj9jrgTe2xUMo") 

FORCE_SUB = os.environ.get("FORCE_SUB", "hdlinks4uu") 

DB_NAME = os.environ.get("DB_NAME","cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://BIGBOSS:BIGBOSS@cluster0.ii3gmvr.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "100"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/2acf37dd041dc8cae6fc2.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6459102722').split()]

PORT = os.environ.get("PORT", "8080")
