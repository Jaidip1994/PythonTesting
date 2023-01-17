def test_write_ten_lines(write_file):
    print("\nWrite ten lines")
    num_lines_before = sum(1 for line in open(write_file.name))

    for i in range(10):
        write_file.write("X Y Z %d\n" % (i + 1))

    write_file.flush()
    num_lines_after = sum(1 for line in open(write_file.name))
    assert (num_lines_after - num_lines_before) == 9


def test_file_size_on_write(readonly_file):
    print("\n Reading one line")

    field_count = len(readonly_file.readline().split())
    assert field_count == 11
