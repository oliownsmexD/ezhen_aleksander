while True:

    file_path = input("������ ���� �� �����: ")




    with open(file_path, 'r') as file:

        lines = file.readlines()

        total_lines = len(lines)

        empty_lines = 0

        lines_with_z = 0

        total_z_count = 0

        lines_with_and = 0




        for line in lines:

            line = line.strip()

            if not line:

                empty_lines += 1

            else:

                if 'z' in line.lower():

                    lines_with_z += 1

                    total_z_count += line.lower().count('z')




                if 'and' in line.lower():

                    lines_with_and += 1




        print("ʳ������ �����: ", total_lines)

        print("ʳ������ ������� �����: ", empty_lines)

        print("ʳ������ ����� � ������ 'z': ", lines_with_z)

        print("ʳ������ ���� 'z' � ����: ", total_z_count)

        print("ʳ������ ����� � ������ ������� 'and': ", lines_with_and)




    another_file = input("������ ������������� �� ���� ����? (���/ͳ): ")

    if another_file.lower() != '���':

        break