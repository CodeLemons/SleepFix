import multiprocessing
import audioplayer

class Player:
    def __init__(self):
        pass

    @staticmethod
    def start_sound(song):
        audioplayer.AudioPlayer(song).play(block=False)

if __name__ == "__main__":
    song_list = ["lofi.mp3", "rain.mp3", "bells.mp3"]
    process_dict = {}
    while True:
        user_input = input("Enter> p- to play, s- to stop, q - to quit: ")
        if user_input == "p":
            ask_user = input("Choose song: ")
            p = Player()
            process = multiprocessing.Process(target=p.start_sound(f"Music/{ask_user}.mp3"))
            process_dict[ask_user] = process
            process.start()
        elif user_input == "s":
            u_input = input("Which process you want to stop?(?type 'all' to delete all): ")
            if u_input == "all":
                for process in process_dict.values():
                    print(type(process))
                    process.terminate()
            else:
                if u_input in process_dict.keys():
                    process_dict[u_input.lower().strip()].terminate()
                else:
                    print("Process does not exist!")
                

        elif user_input == "q":
            for process in process_dict.values():
                print(type(process))
                process.terminate()
            quit()
