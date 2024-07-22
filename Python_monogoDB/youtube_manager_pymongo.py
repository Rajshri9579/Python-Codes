from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://youtubepy:youtubepy@cluster0.7ki5yn4.mongodb.net/")
print(client)
# Not a good idea to include id and password in code files
# tlsAlowInvalidCertificates=True --> Not a good way to handle ssl

db = client["ytmanager"]
video_collection = db["videos"]

print(video_collection)

def list_all_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']} and Time: {video['time']}")

def add_new_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def update_video(video_id, new_name, new_time):
    video_collection.update_one(
        {'_id': ObjectId(video_id)},
        {'$set': {"name": new_name}}   
    )

def delete_video(video_id):
    video_collection.delete_one({'_id': ObjectId(video_id)})
    
def main():
    #videos = []
    while True:
        print("\n Youtube Manager App")
        print("1. List all videos")
        print("2. Add a new videos")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit App")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_all_videos()
        elif choice =='2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_new_video(name, time)
        elif choice =='3':
            video_id = input("Enter the video id to be updated: ")
            new_name = input("Enter the the updated video name: ")
            new_time = input("Enter the updated video time: ")
            update_video(video_id, new_name, new_time)
        elif choice == '4':
            video_id = input("Enter the video id to be deleted: ")
            delete_video(video_id)
        elif choice == '5':
            print("Time to exit the app....")
            break
        else:
            print("Invalid input... :(")

if __name__ == "__main__":
    main()