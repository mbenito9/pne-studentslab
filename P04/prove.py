from pathlib import Path
def get_file(base):
    folder = "html/info/"
    filename = folder + base + ".html"
    read = Path(filename).read_text()
    return read

print(get_file("A"))