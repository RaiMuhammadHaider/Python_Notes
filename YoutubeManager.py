import json # learn about json

def load_data():
    try:
        with open('youtube.txt' , 'r') as file :
            return json.load(file) # it wil go to file and load the data and also convert the data into json
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt' , 'w') as file:
        json.dump(videos , file) # what to store and where to store

def  list_all_videos(videos):
    print('\n')
    print('*' * 70)
    for index , video in  enumerate(videos , start=1): #enumerate basically provide indexing we cal also start indexing from a certain piint
        print(f"{index}. {video['name']} Duration : {video['time']}")
    print('\n')
    print('*' * 70)


def add_videos(videos):
    name = input('Enter video name: ')
    time = input('Enter video time: ')
    videos.append({'name' : name , 'time' : time})
    save_data_helper(videos)

def update_videos(videos):
    list_all_videos(videos)
    index = int(input('Enter the video number to delete: '))
    if 1 <= index <= len(videos):
        name = input('Enter the name of the video: ')
        time = input('Enter the Duration of the video: ')
        videos[index-1] = {'name': name , 'time':time}
        save_data_helper(videos)
    else:
        print('Invalid index selected')
    

def delete_videos(videos):
    list_all_videos(videos)
    index = int(input('Enter the video number to be deleted'))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print('Invalid video index selected')



def main():
    videos = load_data()
    while True:
        print('\n Youtube Manager | choose an option')
        print('1. List all Youtube videos')
        print('2. add a Youtube video')
        print('3. Update a Youtube video')
        print('4. Delete a Youtube video')
        print('5. Exit the app')
        chose = input('Enter Your choice: ')
        print(videos)

        match chose:
            case  '1':
                list_all_videos(videos)
            case '2':
                add_videos(videos)
            case '3':
                update_videos(videos)
            case '4':
                delete_videos(videos)
            case '5':
                break
            case _:
                print('Invalid Choice')

if __name__ == '__main__':
    main()