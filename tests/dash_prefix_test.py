import dash
from dash import html, dcc
from dash_prefix import prefix, isTriggered
from dash_prefix.dash_prefix import NOUPDATE

def test_component_prefix():
    pfx = prefix()

    name = dcc.Input('Entry name', id=pfx('name'))
    div = html.H2('Hello World', id=pfx('div'))

    assert name.id == 'i1_name'
    assert div.id == 'i1_div'

    prefixes = [prefix()('div') for i in range(256)]
    assert prefixes[254] == 'i100_div'

def test_module_component_prefix():
    pfx = prefix('test')

    name = dcc.Input('Entry name', id=pfx('name'))
    div = html.H2('Hello World', id=pfx('div'))

    assert name.id == 'test_name'
    assert div.id == 'test_div'

# https://dash.plotly.com/testing

def test_bsly001_falsy_child(dash_duo):

    app = dash.Dash(__name__)

    wrapper = html.Div(id="nully-wrapper", children=0)
    app.layout = wrapper

    dash_duo.start_server(app)

    dash_duo.wait_for_text_to_equal(wrapper.css_id, "0", timeout=4)

    assert dash_duo.find_element(wrapper.css_id).text == "0"

    assert dash_duo.get_logs() == [], "browser console should contain no error"

    dash_duo.percy_snapshot("bsly001-layout")


def test_browser_interaction(dash_duo):

    app = dash.Dash(__name__)

    btn1 = html.Button("Button 1", id='btn1')
    btn2 = html.Button("Button 2", id='btn3')
    title = html.H1('Title', id='title')

    @app.callback(title.output.children, btn1.input.n_clicks,  btn2.input.n_clicks)
    def _update(btn1_clicks, btn2_clicks):
        if isTriggered(btn1.input.n_clicks):
            return "Button1 Clicked"
        if isTriggered(btn2.input.n_clicks):
            return "Button2 Clicked"
        return NOUPDATE

    app.layout = html.Div([title, btn1, btn2])

    dash_duo.start_server(app)

    dash_duo.wait_for_text_to_equal(title.css_id, 'Title', timeout=4)

    _title = dash_duo.find_element(title.css_id)
    _btn1 = dash_duo.find_element(btn1.css_id)
    _btn2 = dash_duo.find_element(btn2.css_id)

    assert _title.text == 'Title'

    _btn1.click()
    assert _title.text == 'Button1 Clicked'

    _btn2.click()
    assert _title.text == 'Button2 Clicked'

