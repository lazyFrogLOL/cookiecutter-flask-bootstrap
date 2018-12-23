import os


def remove_unnecessary_files():
    if '{{cookiecutter.better_dev_experience}}' == 'no':
        os.remove('.coveragerc')
    if '{{cookiecutter.deploy_to_heroku}}' == 'no':
        os.remove('Procfile')
        os.remove('app.json')


if __name__ == '__main__':
    remove_unnecessary_files()
