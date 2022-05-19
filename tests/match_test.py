import dash
from dash import html, ALL, callback
from dash_prefix import prefix, trigger_index, match
from dash_prefix.dash_prefix import NOUPDATE

def test_match(dash_duo):

    app = dash.Dash(__name__)

    Match = match({'type': 'buttons', 'idx': ALL})

    btn1 = html.Button('Button 1', id=Match.idx(1))
    btn2 = html.Button('Button 2', id=Match.idx(2))
    btn3 = html.Button('Button 3', id=Match.idx(3))

    title = html.Div('Title', id='title')

    @callback(title.output.children, Match.input.n_clicks)
    def _update_(button_clicks):
        idx = trigger_index()
        if idx is not None:
            return f"Button {idx + 1} triggered {button_clicks[idx]} times!"
        return NOUPDATE

    app.layout = html.Div([title, btn1, btn2, btn3])

    dash_duo.start_server(app)

    dash_duo.wait_for_text_to_equal(title.css_id, 'Title', timeout=4)

    _title = dash_duo.find_element(title.css_id)
    _btn1 = dash_duo.find_element(btn1.css_id)
    _btn2 = dash_duo.find_element(btn2.css_id)
    _btn3 = dash_duo.find_element(btn3.css_id)

    assert _title.text == 'Title'

    _btn1.click()
    assert _title.text == "Button 1 triggered 1 times!"

    _btn2.click()
    assert _title.text == "Button 2 triggered 1 times!"

    _btn3.click()
    assert _title.text == "Button 3 triggered 1 times!"

    _btn1.click()
    assert _title.text == "Button 1 triggered 2 times!"

    _btn2.click()
    assert _title.text == "Button 2 triggered 2 times!"

    _btn3.click()
    assert _title.text == "Button 3 triggered 2 times!"