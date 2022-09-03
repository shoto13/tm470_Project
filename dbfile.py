from pymongo import MongoClient
client = MongoClient('mongodb+srv://tm470test:dAVg7WKRh01pGudx@tm470project.adfi2.mongodb.net/?retryWrites=true&w=majority')

# START UP MONGO DB CONNECTION
db = client.tm470Data
u_settings_collection = db.u_settings_collection

# # Basic user settings
# username = "test_user"
# text_colour_preference = "#C4826E"
# background_colour_preference = "#5865F2"
# javascript_on = True
# images_on = True
# ads_on = True
#
# u01_settingsDocument = {
#     "username": "test_user",
#     "profile_name": "default profile",
#     "text_colour_preference": "#C4826E",
#     "background_colour_preference": "#5865F2",
#     "javascript_on": True,
#     "images_on": False,
#     "ads_on": False
# }
#
# u_settings_collection.insert_one(u01_settingsDocument)
