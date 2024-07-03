from textnode import TextNode
import shutil
import os
from block_markdown import markdown_to_HTML 

def copydir(srcdir, destdir):
    if not (os.path.exists(srcdir)):
        raise ValueError("Source path doesn't exist.")
    shutil.rmtree(destdir)
    os.mkdir(destdir)
    fileList = os.listdir(path=srcdir)
    for file in fileList:
        filepath = os.path.join(srcdir,file)
        if os.path.isfile(filepath):
            shutil.copy(filepath,destdir)
        else:
            if not (os.path.exists(destdir + f"{file}/")):
                os.mkdir(destdir + f"{file}/")
            copydir(filepath,destdir+f"{file}/")

def extract_title(markdown):
    lines = markdown.split("\n")
    title = lines[0].strip("# ")
    return title

def generate_page(from_path, template_path, dest_path):
    if len(from_path) == 0 or len(template_path) == 0 or dest_path == 0:
        return
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    mdFile = open(from_path, mode = 'r')
    tempFile = open(template_path, mode = 'r')
    markdown = mdFile.read()
    template = tempFile.read()
    title = extract_title(markdown)
    HTMLContent = markdown_to_HTML(markdown).to_html()
    newHTML = template.replace("{{ Title }}", title)
    newHTML = newHTML.replace("{{ Content }}", HTMLContent)
    if not (os.path.exists(os.path.dirname(dest_path))):
        os.makedirs(os.path.dirname(dest_path))
    resultFile = open(dest_path, mode = 'a')
    resultFile.write(newHTML)
    
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not (os.path.exists(dir_path_content) or os.path.exists(template_path)):
        raise ValueError("Path doesn't exist")
    fileList = os.listdir(path=dir_path_content)
    for file in fileList:
        filepath = os.path.join(dir_path_content,file)
        if os.path.isfile(filepath):
            print(filepath)
            generate_page(filepath,template_path,dest_dir_path + file.rstrip(".md") + ".html")
        else:
            if not (os.path.exists(dest_dir_path + f"{file}/")):
                os.mkdir(dest_dir_path + f"{file}/")
            generate_pages_recursive(filepath, template_path, dest_dir_path + f"{file}/")

def main():
    # tnode = TextNode('This is a text node', 'bold', 'https://www.boot.dev')
    # print(tnode)
    srcdir = "./static/"
    destdir = "./public/"
    copydir(srcdir,destdir)
    # from_path = "content/index.md"
    template_path = "template.html"
    # dest_path = "public/index.html"
    # generate_page(from_path,template_path,dest_path)
    dir_path_content = "content/"
    dest_dir_path = "public/"
    generate_pages_recursive(dir_path_content,template_path,dest_dir_path)

main()