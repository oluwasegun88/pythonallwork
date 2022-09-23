# with open('temp_file.txt', mode='w', encoding='utf-8') as file_object:
    #print(file_object.tell())
    #file_object.write("Life is good with Banke\n")
    # file_object.seek(10)
    # print(file_object.tell())
    #file_object.write("Life is good with Banke\n")
    #file_object.writelines(['Life\n', 'is\n', 'bad\n', 'with\n', 'Judas\n'])

# with open('temp_file.txt', 'r', encoding='utf-8') as file:
#     # print(file.readline())
#     # print(file.read())
#     for idx, line in enumerate(file.readlines(), start=1):
#         print(f"{idx}.{line.upper()}")


from pathlib import Path

# path = Path("./folder/sub-folder/text.txt")
#
# print(path.resolve())
#
# path.parent.mkdir(parents=True,exist_ok=True)
#
#
# path.touch(exist_ok=True)
#
# with path.open(mode='a') as f:
#     f.write("Hello")


file_path = Path.home() / "temperatures.txt"
with file_path.open(mode="r", encoding = "utf-8") as f:
    file.write(str(temperature_readings[0]))
    for temp in temperature_readings[1:]:
        file.write(f",{temp}")

#print(path.exists())