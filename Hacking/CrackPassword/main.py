import hashlib
import time


def get_dictionary_users_passwords(file):
    with open(file) as f:
        raw_lines = f.readlines()
    lines = [x.strip() for x in raw_lines]
    users = [line.split(":")[0] for line in lines]
    raw_hashed_passwords = [line.split(":")[1] for line in lines]
    return dict(zip(users, raw_hashed_passwords))


def get_user_by_hashed_password(hashed_password):
    return list(users_passwords.keys())[list(users_passwords.values()).index('$1$' + hashed_password)]


def get_hashed_passwords_from_shadow_file(file):
    with open(file) as f:
        raw_lines = f.readlines()
    lines = [x.strip() for x in raw_lines]
    raw_hashed_passwords = [line.split(":")[1] for line in lines]
    filtered_raw_hashed_passwords = [x for x in raw_hashed_passwords if x not in undefined_passwords_values]
    return [line[3:] for line in filtered_raw_hashed_passwords]


def get_dictionary_passwords_from_file(file):
    with open(dic_filename) as f:
        raw_lines = f.readlines()
        return [x.strip() for x in raw_lines]


def md5_encrypt(string):
    return hashlib.md5(string.encode()).hexdigest()


def decrypt_md5_hashed_passwords_with_dictionary_passwords(hashed_passwords, dictionary_passwords, users_passwords):
    start = time.time()
    users_discovered_passwords = {}
    for dictionary_password in dictionary_passwords:
        hashed_dictionary_password = md5_encrypt(dictionary_password)
        for hashed_password in hashed_passwords:
            if hashed_password == hashed_dictionary_password:
                end = time.time()
                users_discovered_passwords[get_user_by_hashed_password(hashed_password)] = {dictionary_password: end - start}
    return users_discovered_passwords


def store_list_to_text(list):
    with open('your_file.txt', 'w') as f:
        for x, y in list.items():
            f.write(str(x) + " : " + str(y) + "\n")


if __name__ == '__main__':

    shadow_filename = 'shadow_test'
    dic_filename = 'dico_mini_fr'
    undefined_passwords_values = ['!', '*']

    users_passwords = get_dictionary_users_passwords(shadow_filename)
    hashed_passwords = get_hashed_passwords_from_shadow_file(shadow_filename)
    dictionary_passwords = get_dictionary_passwords_from_file(dic_filename)
    discovered_passwords = decrypt_md5_hashed_passwords_with_dictionary_passwords(hashed_passwords,
                                                                                  dictionary_passwords, users_passwords)
    store_list_to_text(discovered_passwords)

    for password, time in discovered_passwords.items():
        print('{} : {}'.format(password, time))
