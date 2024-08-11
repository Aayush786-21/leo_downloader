from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.youtube_downloader
downloads_collection = db.downloads

def save_download_info(video_info):
    downloads_collection.insert_one(video_info)
