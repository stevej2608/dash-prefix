import dash
from dash import html
from dash_prefix import prefix, isTriggered, copy_factory
from dash_prefix.dash_prefix import NOUPDATE

# Test that copy_factory() correctly maps the id of an
# embedded component to the enclosing container

def test_browser_interaction(dash_duo):

    def jumbotron_header(title, text, id):
        btn = html.Button("Click for more information", id=id)
        container = html.Header([
            html.H1(title, className='display-4 text-center'),
            html.P(text),
            btn
        ], className='jumbotron my-4')

        copy_factory(btn, container)

        return container

    app = dash.Dash(__name__)

    header = jumbotron_header('Welcome to Dash', "copy test", id="header")
    title = html.H1('Title', id='title')

    @app.callback(title.output.children, header.input.n_clicks)
    def _update(clicks):
        if isTriggered(header.input.n_clicks):
            return "Information button clicked"
        return NOUPDATE

    app.layout = html.Div([title, header])

    dash_duo.start_server(app)

    dash_duo.wait_for_text_to_equal(title.css_id, 'Title', timeout=4)

    _title = dash_duo.find_element(title.css_id)
    _header = dash_duo.find_element(header.css_id)

    assert _title.text == 'Title'

    _header.click()
    assert _title.text == 'Information button clicked'
