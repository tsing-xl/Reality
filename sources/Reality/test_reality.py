import Reality

interface = Reality.Interface()

test_button = Reality.widgets.Button(interface = interface)
test_label = Reality.widgets.Label(interface = interface)
test_cover = Reality.widgets.Cover(interface = interface, is_main_cover = True)
test_checkbox = Reality.widgets.CheckBox(interface = interface)

Reality.consoleLogout(log_String = 'Hello, reality!')