def get_formatted_name(first,last,middle=""):#加上一個不定變數
    if middle:
        fullname=f"{first} {middle} {last}"
    else:
        fullname=f"{first} {last}"
    return fullname.title()