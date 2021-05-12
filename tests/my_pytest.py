from application.ya_uploader import YaUploader


uploader = YaUploader('Your TOKEN')


class TestYaUploader:

    def setup_class(self):
        print('method setup_class')

    def setup(self):
        print('method setup')

    def test_create_dir(self):
        print('test_create_dir')
        expected_res = 'Папка создана на яндекс диске!'
        assert uploader.create_dir('test_dir') == expected_res

    def test_failed_to_create_dir(self):
        print('test_failed_to_create_dir')
        expected_res = 'Папка с таким именем уже есть!'
        assert uploader.create_dir('test_dir') == expected_res

    def teardown(self):
        print('method teardown')

    def teardown_class(self):
        print('method teardown_class')
