import sqlite3

conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
        CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
        )
''')

# List all videos
def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

# Add video
def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

# Update video
def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    conn.commit()

# Delete video
def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()

# Main menu
def main():
    while True:
        print('\nYoutube manager app with DB')
        print('1. List all videos')
        print('2. Add video')
        print('3. Update video')
        print('4. Delete video')
        print('5. Exit app')
        
        choice = input('Enter your choice: ')
        
        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input('Enter the video name: ')
            time = input('Enter the time: ')
            add_video(name, time)
        elif choice == '3':
            video_id = int(input('Enter the Video ID to update: '))
            name = input('Enter the new video name: ')
            time = input('Enter the new time: ')
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = int(input('Enter the Video ID to delete:  '))
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print('Invalid choice')
    conn.close()

if __name__ == '__main__':
    main()
