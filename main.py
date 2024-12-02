import sys
import os
from functools import partial
from utils import generate_blog, write_to_docx
from multiprocessing import Pool


def process_blog(title: str, folder_name: str):
    print(f'Generating blog for: "{title}"')
    blog = generate_blog(title)

    base_path = f"./{folder_name}/{title}/"
    blog_path = f"{base_path}/Blog/"
    images_path = f"{base_path}/Images/"

    os.mkdir(base_path)
    os.mkdir(blog_path)
    os.mkdir(images_path)

    output_path = f"{blog_path}/{title}.docx"

    if blog:
        write_to_docx(blog, output_path)
        return True, title

    return False, title


if __name__ == "__main__":
    folder_name = sys.argv[1]

    with open(f"./{folder_name}/blogs.txt", "r") as blog_titles:
        titles = [title.strip() for title in blog_titles.readlines()]

    with Pool(processes=90) as pool:
        results = pool.map(partial(process_blog, folder_name=folder_name), titles)
