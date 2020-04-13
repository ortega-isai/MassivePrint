import os

# os.startfile(r"toPrint", "print")

DIRECTORY = r"toPrint"

for root, dirs, files in os.walk(DIRECTORY):
    for file in files:
        if file.endswith(".xml"):
            relativeFile = os.path.join(root, file)
            pre, ext = os.path.splitext(relativeFile)
            os.rename(relativeFile, pre + '.txt')


for root, dirs, files in os.walk(DIRECTORY):
    for file in files:
        if file.endswith(".txt"):
            relativeFile2 = os.path.join(root, file)
            os.startfile(relativeFile2, "print")
            print(" Se envio a imprimier archivo -> {}".format(relativeFile2))