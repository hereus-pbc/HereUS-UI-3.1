import requests
import secrets
import json
from bevyframe import Frame, Request, Response, Page, redirect, Widget

app = Frame(
    package='net.hereus.ui.demo',
    developer='islekcaganmert@hereus.net',
    administrator=True,
    secret=secrets.token_hex(secrets.randbits(8)),
    style=json.load(open('./HereUS-UI-3.1.json', 'rb')),
    icon='https://www.hereus.net/favicon.png',
    keywords=['Test']
)


@app.route('/')
def index() -> Response:
    return redirect('/blue')


@app.route('/<color>')
def index(request: Request, color) -> Page:
    return Page(
        title='HereUS UI Demo',
        selector=f'body_{color}',
        childs=[
            Widget(
                'nav',
                selector='Navbar',
                childs=[]
            ),
            Widget(
                'nav',
                selector='Topbar',
                childs=[]
            ),
        ] + [
            Widget(
                'div',
                style={
                    'margin': '100px'
                },
                childs=[
                    Widget('p', childs=[i])
                    for i in [
                        Widget('div', selector='the_box', style={'width': '400px'}, childs=[
                            Widget('p', innertext='.the_box'),
                            Widget('input', selector='textbox', value='.textbox')
                        ]),
                        Widget('button', selector='button', innertext='.button'),
                        Widget('button', selector='button small', innertext='.button.small'),
                        Widget('button', selector='button mini', innertext='.button.mini'),
                        Widget('input', selector='textbox grey', value='.textbox.grey')
                    ]
                ]
            )
        ]
    )


app.run('0.0.0.0', 80, True)
