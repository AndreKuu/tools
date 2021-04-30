import os
import multiprocessing


def copy_work(file_name, source_dir, dest_dir):
    # 1. 拼接源文件和目标文件的路径
    source_path = '\\'.join((source_dir, file_name))
    dest_path = '\\'.join((dest_dir, file_name))
    if not os.path.isdir(source_path):
        print(source_path, "------->", dest_path)
        # 2. 打开源文件、创建目标文件
        with open(source_path, "rb") as source_file:
            with open(dest_path, "wb") as dest_file:
                while True:
                    # 循环读取数据
                    file_data = source_file.read(1024)
                    if file_data:
                        # 循环写入到目标文件
                        dest_file.write(file_data)
                    else:
                        break
    else:
        lst = os.listdir(source_path)
        try:
            os.mkdir(dest_path)
        except:
            print("文件夹已经创建")
        for file_name_ in lst:
            copy_work(file_name_, source_path, dest_path)


if __name__ == "__main__":
    # 1、定义源文件夹所在路径和目标文件夹所在路径
    # 源文件夹
    source_dir = "C:\\Users\\user\\Desktop\\面经"
    # 复制到目的地文件夹
    dest_dir = "C:\\Users\\user\\Desktop\\copy~"

    # 2、创建目标文件夹目录
    try:
        os.mkdir(dest_dir)
    except:
        print("目标文件夹已经创建")

    # 3、列表得到所有源文件中的文件
    file_list = os.listdir(source_dir)
    print(file_list)

    # 4、for 循环一次拷贝每个文件
    for file_name in file_list:
        sub_process = multiprocessing.Process(target=copy_work, args=(file_name, source_dir, dest_dir))
        sub_process.start()
