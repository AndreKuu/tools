import os
import threading

def copy_work(file_name, src_dir, target_dir):
    src_path = src_dir + "\\" + file_name
    target_path = target_dir + "\\" + file_name
    if os.path.isdir(src_path):
        try:
            os.mkdir(target_path)
        except:
            print("已经创建好了")
        newlst = os.listdir(src_path)
        for file_name in newlst:
            copy_work(file_name, src_path, target_path)
    else:
        with open(src_path, "rb") as current_file:
            with open(target_path, "wb") as target_file:
                while True:
                    context = current_file.read(1024)
                    if context:
                        target_file.write(context)
                    else:
                        print(src_path, "--------->", target_path)
                        break





if __name__ == "__main__":
    src_dir = "C:\\Users\\user\\Desktop\\面经"
    target_dir = "C:\\Users\\user\\Desktop\\copy2~"
    try:
        os.mkdir(target_dir)
    except:
        print("已经创建好了文件夹")
    lst = os.listdir(src_dir)
    for file_name in lst:
        thread_copy = threading.Thread(copy_work(file_name, src_dir, target_dir))
        thread_copy.start()
