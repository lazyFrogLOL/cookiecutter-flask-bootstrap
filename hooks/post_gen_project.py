import os


def remove_unnecessary_files():
    better_dev_experience = '{{better_dev_experience}}'
    if better_dev_experience == 'no':
        os.remove('.coveragerc')


if __name__ == '__main__':
    remove_unnecessary_files()
