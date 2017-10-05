import os
import glob


def sing(f_name, l_name, father, data, level, n_code, mobile, phone, address, sex, c_f, m_b):
    os.mkdir("students/%s" % (n_code))  # ejad
    os.chdir("students/%s" % (n_code))  # go to
    print (os.getcwd())  # show address
    with open("f_name.txt", "w") as file:
        file.write(f_name)

    with open("l_name.txt", "w") as file:
        file.write(l_name)

    with open("father.txt", "w") as file:
        file.write(father)

    with open("data.txt", "w") as file:
        file.write(data)

    with open("level.txt", "w") as file:
        file.write(level)

    with open("n_code.txt", "w") as file:
        file.write(n_code)

    with open("mobile.txt", "w") as file:
        file.write(mobile)

    with open("phone.txt", "w") as file:
        file.write(phone)

    with open("address.txt", "w") as file:
        file.write(address)

    with open("sex.txt", "w") as file:
        file.write(sex)

    with open("c_f.txt", "w") as file:
        file.write(c_f)

    with open("m_b.txt", "w") as file:
        file.write(m_b)


def search(n_code):
    lisr_result = []
    x = str(n_code)
    os.chdir("/home/alidehghan/shookooh/V0.0.3/students")
    for file in glob.glob(x):

        if file != x:
            return False

        if file == x:
            try:
                lisr_result.append("OK")
                os.chdir("/home/alidehghan/shookooh/V0.0.3/students/%s" % (x))
                with open("f_name.txt", "r") as file:
                    lisr_result.append(file.read())

                with open("l_name.txt", "r") as file:
                    lisr_result.append(file.read())

                with open("father.txt", "r") as file:
                    lisr_result.append(file.read())

                with open("data.txt", "r") as file:
                    lisr_result.append(file.read())

                with open("level.txt", "r") as file:
                    lisr_result.append(file.read())

                with open("n_code.txt", "r") as file:
                    lisr_result.append(file.read())

                with open("mobile.txt", "r") as file:
                    lisr_result.append(file.read())

                with open("phone.txt", "r") as file:
                    lisr_result.append(file.read())

                with open("address.txt", "r") as file:
                    lisr_result.append(file.read())

                with open("sex.txt", "r") as file:
                    lisr_result.append(file.read())

                with open("c_f.txt", "r") as file:
                    lisr_result.append(file.read())

                with open("m_b.txt", "r") as file:
                    lisr_result.append(file.read())
                os.chdir("..")
                return lisr_result
            except:
                lisr_result.append("NO")
                return lisr_result
