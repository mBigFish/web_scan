from CSHandleURL import HandleURL

class_handle_url = HandleURL()


dirc = []
with open("../file/more_url.txt", "r") as fp:
    for line in fp.readlines():
        url = line.strip("\n")
        # print(url)

        ret_result = class_handle_url.get_ip_from_url(url)
        print(ret_result)