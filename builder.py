import json

with open('./Palette.json', 'rb') as f:
    palette = json.load(f)

style = {}
dark_style = {}


def do_import() -> None:
    style.update({'@imports': [
        "https://fonts.googleapis.com/css2?family=Noto+Emoji:wght@700&display=swap",
        "https://fonts.googleapis.com/css2?family=Inter&display=swap",
        "https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@24,300,0,0",
        "https://fonts.googleapis.com/css2?family=Croissant+One&family=Parisienne&display=swap",
        "https://fonts.googleapis.com/css2?family=Catamaran:wght@100..900&family=Moirai+One&display=swap",
        "https://fonts.googleapis.com/css2?family=Work+Sans:ital,wght@0,100..900;1,100..900&display=swap",
        "https://www.nerdfonts.com/assets/css/webfont.css"
    ]})


def touches() -> None:
    style.update({'.data': {
        "visibility": "hidden",
        "height": "0px",
        "width": "0px",
        "font-size": "0px"
    }})
    style.update({'p:hover': {"border": "none"}})
    style.update({".caution::after": {
        "content": "var(--caution-content)",
        "font-weight": "500",
        "font-size": "15px",
        "margin-left": "-30px",
        "background-color": "#FF0000",
        "z-index": "9999",
        "position": "relative",
        "padding-left": "4px",
        "padding-right": "4px",
        "border-radius": "10px",
        "margin-top": "-50px"
    }})
    style.update({".textbox:focus": {
        "outline": "none"
    }})
    style.update({".button:focus": {
        "box-shadow": "inset 0 0 100px 100px #FFFFFF60",
        "outline": "none"
    }})
    style.update({".button:hover": {
        "box-shadow": "inset 0 0 100px 100px #FFFFFF60",
        "outline": "none"
    }})
    style.update({"a": {
        "color": "inherit",
        "text-decoration": "inherit"
    }})
    style.update({"::-webkit-scrollbar": {
        "width": "0px"
    }})
    style.update({".feed": {
        "padding-right": "100px",
        "padding-left": "100px"
    }})
    style.update({".centerfeed": {
        "padding-right": "350px",
        "padding-left": "100px"
    }})
    style.update({".rightbar": {
        "position": "fixed",
        "top": "40px",
        "bottom": "0px",
        "right": "0px",
        "z-index": "1000",
        "display": "block",
        "padding": "20px",
        "padding-left": "0px",
        "overflow-x": "hidden",
        "overflow-y": "auto",
        "border-right": "none"
    }})
    style.update({"#page-wrap": {
        "width": "1300px",
        "margin": "0 auto"
    }})
    style.update({"textarea": {
        "margin": "3px"
    }})
    style.update({"textarea:focus": {
        "outline": "none"
    }})


def body() -> None:
    style.update({"body": {
        "padding-top": "0px",
        "font-family": [
            "Catamaran",
            "Noto Emoji",
            "sans-serif"
        ],
        "overflow-x": "hidden",
        "scroll-behavior": "smooth",
        "background-color": palette['Blank']['Light']['Background'],
        "accent-color": palette['Blank']['Light']['AccentColor']
    }})
    dark_style.update({"body": {
        "color": "#FFFFFF",
        "background-color": palette['Blank']['Dark']['Background'],
        "accent-color": palette['Blank']['Dark']['AccentColor']
    }})
    for i in palette:
        style.update({f'.body_{i.lower()}': {
            'background-color': palette[i]['Light']['Background'],
            'accent-color': palette[i]['Light']['AccentColor']
        }})
        dark_style.update({f'.body_{i.lower()}': {
            'background-color': palette[i]['Dark']['Background'],
            'accent-color': palette[i]['Dark']['AccentColor']
        }})


def the_box() -> None:
    style.update({".the_box": {
        "background-color": palette['Blank']['Light']['WidgetColor'],
        "border": "1px solid #808080A0",
        "border-radius": "10px",
        "padding": "20px",
        "padding-top": "0px",
        "padding-bottom": "10px"
    }})
    dark_style.update({".the_box": {"background-color": palette['Blank']['Dark']['WidgetColor']}})
    for i in palette:
        style.update({f'.body_{i.lower()} .the_box': {
            'background-color': palette[i]['Light']['WidgetColor']
        }})
        dark_style.update({f'.body_{i.lower()} .the_box': {
            'background-color': palette[i]['Dark']['WidgetColor']
        }})


def button() -> None:
    style.update({".button": {
        "border-radius": "15px",
        "border": "none",
        "background-color": palette['Blank']['Light']['AccentColor'],
        "color": "#FFFFFF",
        "width": "400px",
        "height": "50px",
        "font-size": "20px",
        "cursor": "pointer"
    }})
    style.update({".button.small": {
        "border-radius": "15px",
        "width": "150px",
        "height": "50px",
        "font-size": "15px"
    }})
    style.update({".button.mini": {
        "border-radius": "15px",
        "width": "100px",
        "height": "30px",
        "font-size": "15px"
    }})
    for i in palette:
        style.update({f'.body_{i.lower()} .button': {
            'background-color': palette[i]['Light']['AccentColor']
        }})


def textbox() -> None:
    style.update({".textbox": {
        "border-radius": "5px",
        "border": "none",
        "border-bottom": "1px solid #808080A0",
        "background-color": palette['Blank']['Light']['SubWidgetColor'],
        "color": "#000000",
        "width": "380px",
        "max-width": "380px",
        "height": "50px",
        "font-size": "20px",
        "padding-left": "10px",
        "padding-right": "10px"
    }})
    dark_style.update({".textbox": {
        "background-color": palette['Blank']['Dark']['SubWidgetColor'],
        "color": "#FFFFFF",
    }})
    style.update({".textbox.grey": {
        "background-color": palette['Blank']['Light']['WidgetColor']
    }})
    dark_style.update({".textbox.grey": {
        "background-color": palette['Blank']['Dark']['WidgetColor'],
        "color": "#FFFFFF",
    }})
    for i in palette:
        style.update({f'.body_{i.lower()} .textbox': {
            'background-color': palette[i]['Light']['SubWidgetColor']
        }})
        style.update({f'.body_{i.lower()} .textbox.grey': {
            'background-color': palette[i]['Light']['WidgetColor']
        }})
        dark_style.update({f'.body_{i.lower()} .textbox': {
            'background-color': palette[i]['Dark']['SubWidgetColor']
        }})
        dark_style.update({f'.body_{i.lower()} .textbox.grey': {
            'background-color': palette[i]['Dark']['WidgetColor']
        }})


def app_icon() -> None:
    style.update({".app_icon": {
        "padding": "20px",
        "border-radius": "20px",
        "background-color": palette['Blank']['Light']['AccentColor'],
        "width": "40px",
        "height": "40px"
    }})
    style.update({".app_icon span": {
        "color": "#FFFFFFD0",
        "font-size": "40px"
    }})
    style.update({".app_icon img": {
        "height": "40px",
        "width": "40px",
        "filter": "opacity(0.85)"
    }})


def auto_color() -> None:
    for a in ['background', 'asset']:
        for b in palette:
            style.update({f'.body_{b.lower()} .autocolor.{a}': (
                {'background-color': palette[b]['Light']['AccentColor']}
                if a == 'background' else
                {'color': palette[b]['Light']['AccentColor']}
            )})


def navbar() -> None:
    style.update({"nav.Navbar": {
        "position": "fixed",
        "height": "100%",
        "top": "20px",
        "bottom": "20px",
        "left": "10px",
        "width": "60px",
        "overflow": "hidden",
        "z-index": "9999",
        "padding-right": "5px",
        "border-radius": "10px"
    }})
    style.update({"nav.Topbar": {
        "position": "fixed",
        "top": "20px",
        "bottom": "0px",
        "left": "0px",
        "right": "0px",
        "height": "75px",
        "overflow": "hidden",
        "z-index": "9999",
        "padding-right": "5px",
        "border-radius": "10px",
        "margin-top": "-10px"
    }})
    style.update({"nav.Navbar a.active button span font": {
        "color": "#FFFFFF"
    }})
    style.update({"nav.Navbar a.titleicon": {
        "float": "left",
        "text-align": "center",
        "text-decoration": "none",
        "padding-left": "10px",
        "filter": "drop-shadow(1px 1px 1px #0084FF)"
    }})
    style.update({"nav.Navbar a": {
        "float": "right",
        "text-align": "center",
        "text-decoration": "none",
        "font-size": "17px",
        "color": "#FFFFFF",
        "align-items": "left"
    }})
    style.update({"nav.Navbar a.active button": {
        "background-color": palette['Blank']['Light']['AccentColor'],
        "border-radius": "15px",
        "color": "#FFFFFF",
        "border": "none",
        "padding": "14px 16px",
        "align-items": "left",
        "cursor": "pointer"
    }})
    style.update({"nav.Navbar a.inactive button": {
        "background-color": "#00000000",
        "border-radius": "15px",
        "color": "#000000",
        "border": "none",
        "padding": "14px 16px",
        "align-items": "left",
        "cursor": "pointer"
    }})
    style.update({"nav.Topbar a.inactive button": {
        "background-color": "#00000000",
        "border-radius": "15px",
        "color": "#000000",
        "border": "none",
        "padding": "14px 16px",
        "align-items": "left",
        "cursor": "pointer",
        "float": "right",
        "filter": "drop-shadow(1px 1px 1px #808080A0)"
    }})
    for i in palette:
        style.update({f" .body_{i} nav.Navbar a.active button": {
            "background-color": palette[i]['Light']['AccentColor']
        }})


do_import()
touches()
body()
the_box()
button()
textbox()
app_icon()
auto_color()
navbar()
style.update({'@media (prefers-color-scheme: dark)': dark_style})


def get(r) -> dict:
    return style


with open('./HereUS-UI-3.1.json', 'w', encoding='UTF-8') as f:
    json.dump(style, f)
