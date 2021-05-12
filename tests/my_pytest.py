import pytest
from application.ya_uploader import YaUploader


class TestYaUploader:

    uploader = YaUploader('your_token')
    test_cases = [('test_dir_1', 201), ('test_dir_1', 409), ('test_dir_2', 201)]

    @pytest.mark.parametrize('dir_name, expected_res', test_cases)
    def test_create_dir(self, dir_name, expected_res):
        assert self.uploader.create_dir(dir_name) == expected_res, 'Error'
