import yaml
from api_unittest.main import DIR, Environ


class ReadYaml:
    @staticmethod
    def env_yaml():
        with open((DIR + '/env_config' + Environ) + '/config.yml', 'r', encoding='utf-8') as f:
            return yaml.load(f, Loader=yaml.FullLoader)

    @staticmethod
    def api_yaml(group_name):
        """
        接口数据驱动的读取方式
        :param group_name:如果配置存储没有嵌套目录结构，只需要传递包名，比方说api_yml('notes'),
                          如果有嵌套的目录结构，传参如：api_yaml('note/notesvrSetNotegroup')
        :return:
        """
        with open((DIR + r"/date/") + group_name + '/api_date.yml', "r", encoding='utf-8') as f:
            # 调用load方法加载文件流
            return yaml.load(f, Loader=yaml.FullLoader)

    @staticmethod
    def common_yaml(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return yaml.load(f, Loader=yaml.FullLoader)


if __name__ == '__main__':
    rY = ReadYaml()
    api_data = rY.api_yaml('note_groups/notesvrSetNotegroup')
    print(api_data)
