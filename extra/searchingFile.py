import os

# def find_files(filename, search_path):
#    result = []

# # Wlaking top-down from the root
#    for root, dir, files in os.walk(search_path):
#       if filename in files:
#          result.append(os.path.join(root, filename))
#    return result

# print(find_files("c 27.pdf","E:"))

isFound = False
listing1 = os.walk("C:/")
listing2 = os.walk("D:/")
listing3 = os.walk("E:/")
listing4 = os.walk("F:/")
search = input("Enter file name:")

if isFound == False:
    print("Searching in D: drive")
    for root, dir, files in listing2:
        if search in files:
            print(os.path.join(root,search))
            os.startfile(os.path.join(root,search))
            isFound = True
    if isFound == False:
        print(search + " not found in D drive")

if isFound == False:
    print("Searching in E: drive")
    for root, dir, files in listing3:
        if search in files:
            print(os.path.join(root,search))
            os.startfile(os.path.join(root,search))
            isFound = True
    if isFound == False:
        print(search + " not found in D drive")

if isFound == False:
    print("Searching in F: drive")
    for root, dir, files in listing4:
        if search in files:
            print(os.path.join(root,search))
            os.startfile(os.path.join(root,search))
            isFound = True
    if isFound == False:
        print(search + " not found in D drive")

if not isFound:
    print("Searching in C: drive")
    for root, dir, files in listing1:
        if search in files:
            print(os.path.join(root,search))
            os.startfile(os.path.join(root,search))
            isFound = True
    if isFound == False:
        print(search + " not found in D drive")