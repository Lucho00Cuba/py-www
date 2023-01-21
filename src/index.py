from pywebio.output import put_markdown, put_row
from os import environ

# The deployment address of the demos module
# ENDPOINT = 'http://localhost:8080'
ENDPOINT = environ.get('ENDPOINT', 'http://localhost:8080')


index_md = r"""### Data visualization demo
PyWebIO supports for data visualization with the third-party libraries.

 - App `bmi` [**endpoint**]({URL}/apps/bmi)
 - App `chat_room` [**endpoint**]({URL}/apps/chat_room)
 - App `markdown_editor` [**endpoint**]({URL}/apps/markdown)
""".format(URL=ENDPOINT)

def main():
    """PyWebIO Multiple Apps"""
    put_row([
        put_markdown('# PyWebIO Multiple Apps')
    ], size='1fr auto').style('align-items:center')

    put_markdown(index_md)