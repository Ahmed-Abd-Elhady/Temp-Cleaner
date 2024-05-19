from colorama import Fore
import pyfiglet,os,time,sys,getpass,shutil,subprocess
#FUNCTIONS s

def delete(path_folder):    
    try:
        for file in os.listdir(path_folder):
            try: 
                shutil.rmtree(os.path.join(path_folder, file))
                print(Fore.GREEN + f"File {file} Cleaned ! File Type 'DIR' ")
            except:
                try:
                    os.remove(path_folder+ "/" +file)
                except:
                    print(Fore.RED + f"This File Used By Another Process [ {file} ]")
                print(Fore.GREEN + "File " + Fore.BLUE+ f"[ {file} ] " + Fore.GREEN+" Cleaned ! Type 'File'")
    except Exception as e:
        print("This File Does not exsis or premssion denind Or CANNOT BE DELETED")
        print(f"Erorr info {e}")
        time.sleep(2)


while True:
    os.system('cls')
    print(Fore.BLUE + pyfiglet.figlet_format("V$C By | @ZERO", font="small"))
    print(Fore.GREEN + "1-Clean All Temp Files\n")
    print(Fore.RED + "2-Exit\n")
    try :
        user_input = int(input(Fore.CYAN+ "Choose : "))
    except:
        print("???")
        time.sleep(2)
        continue
    if user_input == 1:
        os.system("cls")
        print(Fore.GREEN + "Clean Temp Files......\n")
        delete('C:/Windows/Temp')
        delete(f'C:/Users/{getpass.getuser()}/AppData/Local/Temp')
        delete('C:/Windows/Prefetch')
        try:
            subprocess.run(["cleanmgr", "/sagerun:1"], check=True)
            print( Fore.BLUE + "Disk Cleanup completed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")
            time.sleep(5)
        continue

        

            