def test_reality():
    import Reality
    assert Reality.__version__, 'Fail'

    assert Reality.widgets, 'Fail'
    assert Reality.interface.Interface, 'Fail'
    assert Reality.WidgetComposer, 'Fail'
    assert Reality.WidgetHandler, 'Fail'
