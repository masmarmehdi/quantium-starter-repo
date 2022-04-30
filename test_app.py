from dash.testing.application_runners import import_app


def test_header_visual_region_picker(dash_duo):
    app = import_app(app_file='app.py')
    dash_duo.start_server(app)

    dash_duo.wait_for_element("h1")

    dash_duo.wait_for_element_by_id("region-radio")

    dash_duo.wait_for_element_by_id("show-figure")
