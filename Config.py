import configparser


class ReadConfig:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")  # 读取配置文件，如果写文件的绝对路径，就可以不用os模块

    def section_config(self, section):
        return self.config.items(section)



    def cs(self):
        a = self.section_config("request")[1][1]

        print(a)

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read("config.ini")  # 读取配置文件，如果写文件的绝对路径，就可以不用os模块
    a = config.has_section("request")
    print(a)
    b = config.getboolean('request', 'ALLOW_REDIRECT')
    print(b)


