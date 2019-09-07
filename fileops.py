import glob
import os


def search(root_path, file_format="*.jpg"):
    """
    搜索指定目录及其递归子目录下指定模式的文件,利用了glob.glob的功能
    :param root_path:
    :param file_format:匹配模式
    :return:
    """
    all_path = [os.path.join(x[0], y)
                for x in os.walk(root_path)
                for y in x[1]]
    all_path = [glob.glob(os.path.join(dirx, file_format)) for dirx in all_path]
    all_matched_files = [f for f in all_path if f]
    result = []
    for item in all_matched_files:
        for item_inner in item:
            result.append(item_inner)
    print(result)
    return result


if __name__ == "__main__":
    search("G:/", "*.mp4")
