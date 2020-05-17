import dash

app = dash.Dash()
# To avoid displaying the alert raised by the callbacks and unfound ids.
app.config.suppress_callback_exceptions = True
