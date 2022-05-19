## dash-prefix

Plotly/[Dash] utility library that allows component IDs to use prefixed
namespaces. This greatly reduces Dash component ID conflicts. A component ID
is only defined once when the component is created. It is then used by
reference in associated Dash callbacks:

    pip install dash-prefix

**prefix()** Returns a lambda that will prefix all component IDs with the given prefix. If no
prefix is given one will be assigned.

```
from dash import html, callback
from dash_prefix import prefix

pfx = prefix()

user_name = dbc.Input(id=pfx('user'), placeholder="Enter name")
password = dhc.PasswordInput("Password", name='password', id=pfx('password'), placeholder="Enter password")
btn = html.Button('Enter', id=pfx('enter'), disabled=True)

@callback(btn.output.disabled, user_name.input.value, password.input.value)
def _cb_enter(user_name, password):
    return not db_validate_user(user_name, password)

```

**isTriggered()** Returns true if the given dash component was the reason for the enclosing callback
being triggered

```
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
```
**match()** and **trigger_index()** Are [Pattern-Matching Callback] helpers
```
    Match = match({'type': 'buttons', 'idx': ALL})

    btn1 = html.Button('Button 1', id=Match.idx(1))
    btn2 = html.Button('Button 2', id=Match.idx(2))
    btn2 = html.Button('Button 3', id=Match.idx(3))

    title = html.Div(id='title')

    @callback(title.output.children, Match.input.n_clicks)
    def _update_(button_clicks):
        idx = trigger_index()
        if idx is not None:
            return f"Button {idx} triggered {button_clicks[idx]} times!"
        return NOUPDATE
```
**css_id** All dash components are injected with a `css_id` property. This makes testing
with Dash [Duo] far less taxing.
```
title = html.Div('Title', id='title')

_title = dash_duo.find_element(title.css_id)
```
Can also be used with dictionary IDs
```
Match = match({'type': 'buttons', 'idx': ALL})

btn1 = html.Button('Button 1', id=Match.idx(1))
btn2 = html.Button('Button 2', id=Match.idx(2))
btn3 = html.Button('Button 3', id=Match.idx(3))

_btn3 = dash_duo.find_element(btn3.css_id)
```

#### Build the project

The dash-prefix package is available on [pypi]. If needed, to create a local
tarball, first change the release version in *dash_spa/_version.py*, then:

    rm -rf dist dash_spa.egg-info build

    python setup.py sdist bdist_wheel

The tarball is in *dist/dash_spa-<version>.tar.gz*

To install the tarball in a dash project:

    pip install dash_spa-<version>.tar.gz

#### Testing

Pytest and [Dash Duo](https://dash.plotly.com/testing) are used for testing. To run
these tests both the Chrome browser and Chrome driver must be installed.

To run the tests:

    pytest

#### Publish

    twine upload dist/*

[pypi]: https://pypi.org/project/dash-prefix/
[Dash]: https://dash.plot.ly/introduction
[Duo]: https://dash.plotly.com/testing
[Pattern-Matching Callback]: https://dash.plotly.com/pattern-matching-callbacks

