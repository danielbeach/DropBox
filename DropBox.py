#import SDK
import dropbox
import logging

logger = logging.getLogger('myapp')
hdlr = logging.FileHandler('C:\\YOUR_PATH\\FacebookPythonLog.txt')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.INFO)

# Get your app key and secret from the Dropbox developer website
app_key = 'your_key'
app_secret = 'your_secret'

#start OAuth flow
#The OAuth flow has two parts:
#Ask the user to authorize linking your app to their Dropbox account.
#Once authorized, exchange the received authorization code for an access token, which will be used for calling the Core API.

#get authorization url from SDK
access_token = 'your_token'

client = dropbox.client.DropboxClient(access_token)

f = open('//YOUR_FILE_LOCATION/FacebookFeed.tsv', 'rb')
response = client.put_file('YOUR_DROPBOX_FOLDER/ProductFeed.tsv', f, 'True')
logger.info(response)

