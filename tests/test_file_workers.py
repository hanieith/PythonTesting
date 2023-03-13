from my_funcs.file_workers import read_from_file
def test_read_from_file():
    with open('tests/test', 'w') as f_o:
        pass
    test_data = ['one\n', 'two\n', 'three']
    with open('tests/test', 'a') as f_o:
        f_o.writelines(test_data)
    assert test_data == read_from_file('tests/test')