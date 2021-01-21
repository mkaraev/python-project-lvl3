import logging


def save(path, content):
    write_mode = 'wb' if isinstance(content, bytes) else 'w'
    with open(path, write_mode) as file:
        file.write(content)
        logging.info(f'Saved file {path}')
