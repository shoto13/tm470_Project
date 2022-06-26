from pymongo import MongoClient
client = MongoClient('mongodb+srv://tm470test:dAVg7WKRh01pGudx@tm470project.adfi2.mongodb.net/?retryWrites=true&w=majority')

db = client.tm470Data
u_settings_collection = db.u_settings_collection

# Basic user settings
text_colour_preference = "#C4826E"
background_colour_preference = "#5865F2"
javascript_on_preference = True
page_images_preference = True
show_ads_preference = False

u01_settingsDocument = {
    "text_colour_preference": "#C4826E",
    "background_colour_preference": "#5865F2",
    "javascript_on_preference": True,
    "page_images_preference": True,
    "show_ads_preference": False
}

u_settings_collection.insert_one(u01_settingsDocument)


