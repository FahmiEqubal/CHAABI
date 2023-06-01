# Q2. Dictionary, what?
# Write a program that returns the file type from a file name. The type of the file is determined
# from the extension. Initially, a list of values of the form "extension,type"(e.g. xls,spreadsheet;
# png,image) will be input.
# The program takes input in the following form:
# 1. Input extension and type values in the form of a string having the following format:
# a. "extension1,type1;extension2,type2;extension3,type3"
# b. E.g. If we needed to input xls → spreadsheet, xlsx → spreadsheet, jpg → image
# our string would be something like: "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
# 2. Input a list of filename.extension. E.g. an input list could be something like ["abc.html",
# "xyz.xls", "text.csv", "123"]
# The program should return a dict of filename: type pairs
# E.g.
# f("xls,spreadsheet;xlsx,spreadsheet;jpg,image", ["abc.jpg",
# "xyz.xls", "text.csv", "123"]) should return
# {
# "abc.jpg": "image",
# "xyz.xls": "spreadsheet",
# "Text.csv": "unknown",
# "123": "unknown"
# }

def get_file_types(extension_type_string, filenames):
    extension_type_list = extension_type_string.split(";")
    extension_type_map = {}
    
    for ext_type in extension_type_list:
        extension, file_type = ext_type.split(",")
        extension_type_map[extension] = file_type
    
    result = {}
    
    for filename in filenames:
        file_parts = filename.split(".")
        if len(file_parts) > 1:
            extension = file_parts[-1]
            if extension in extension_type_map:
                result[filename] = extension_type_map[extension]
            else:
                result[filename] = "unknown"
        else:
            result[filename] = "unknown"
    
    return result

# Example usage
extension_type_string = "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
filenames = ["abc.jpg", "xyz.xls", "text.csv", "123"]

file_types = get_file_types(extension_type_string, filenames)
print(file_types)
