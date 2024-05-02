import os
import argparse


def generate_tree(directory, indent='', count_files=False, count_dirs=False, extension_filter=None, file_search=None, show_size=False):
    """
    Генерация древовидного представления структуры каталога.
    """
    if not os.path.isdir(directory):
        return

    files = sorted(os.listdir(directory))
    dir_count = 0
    file_count = 0
    for i, file in enumerate(files):
        path = os.path.join(directory, file)
        if os.path.isdir(path):
            dir_count += 1
        else:
            file_count += 1
        if extension_filter and os.path.isfile(path):
            if not file.endswith(extension_filter):
                continue
        if file_search and file_search not in file:
            continue
        if i == len(files) - 1:
            print(indent + '└── ' + file)
            if os.path.isdir(path):
                generate_tree(path, indent + '    ', count_files,
                              count_dirs, extension_filter, file_search, show_size)
        else:
            print(indent + '├── ' + file)
            if os.path.isdir(path):
                generate_tree(path, indent + '│   ', count_files,
                              count_dirs, extension_filter, file_search, show_size)
    if count_files and count_dirs:
        print(indent + f"Total: {file_count} files, {dir_count} directories")
    elif count_files:
        print(indent + f"Total: {file_count} files")
    elif count_dirs:
        print(indent + f"Total: {dir_count} directories")
    if show_size:
        print(indent + f"Size: {get_size(directory)}")


def get_size(path):
    """
    Получить размер файла или каталога в байтах.
    """
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        total_size = 0
        for dirpath, _, filenames in os.walk(path):
            for filename in filenames:
                total_size += os.path.getsize(os.path.join(dirpath, filename))
        return total_size


def main():
    parser = argparse.ArgumentParser(
        description="Отображение древовидной структуры каталога.")
    parser.add_argument("directory", nargs='?', default='.',
                        help="Каталог для отображения дерева (по умолчанию: текущий каталог)")
    parser.add_argument("-d", "--depth", type=int,
                        help="Максимальная глубина дерева каталогов для отображения")
    parser.add_argument("-f", "--files", action="store_true",
                        help="Отображать только файлы")
    parser.add_argument("-dirs", "--directories",
                        action="store_true", help="Отображать только каталоги")
    parser.add_argument("-e", "--extension",
                        help="Фильтровать файлы по расширению")
    parser.add_argument("-s", "--search", help="Поиск файла по имени")
    parser.add_argument("-z", "--size", action="store_true",
                        help="Отображать размер файлов и каталогов")
    args = parser.parse_args()

    if args.depth:
        generate_tree(args.directory, count_files=args.files, count_dirs=args.directories,
                      extension_filter=args.extension, file_search=args.search, show_size=args.size)
    else:
        generate_tree(args.directory, count_files=args.files, count_dirs=args.directories,
                      extension_filter=args.extension, file_search=args.search, show_size=args.size)


if __name__ == "__main__":
    main()


# -f или --files: отображает только файлы.
# -dirs или --directories: отображает только каталоги.
# -e или --extension: фильтрует файлы по заданному расширению.
# -s или --search: ищет файл в дереве по имени.
# -z или --size: отображает размер файлов и каталогов.
