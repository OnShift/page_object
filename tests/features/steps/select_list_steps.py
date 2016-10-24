from hamcrest import assert_that, equal_to


@when(u'I select "{option}" from the select list')
def step_impl(context, option):
    context.page.set_sel_list_id(option)


@when(u'I search for the select list by "{how}"')
def step_impl(context, how):
    context.how = how


@then(u'the current item should be "{option_text}"')
def step_impl(context, option_text):
    assert_that(context.page.get_sel_list_id(), equal_to(option_text))


@then(u'I should be able to select "{option_text}"')
def step_impl(context, option_text):
    getattr(context.page, 'set_sel_list_{0}'.format(context.how))(option_text)


@then(u'the text for the selected item should be "{option_text}"')
def step_impl(context, option_text):
    get_method = 'get_sel_list_{0}'.format(context.how)
    selected_text = getattr(context.page, get_method)()
    assert_that(selected_text, equal_to(option_text))


@then(u'the value for the option should be "{option_value}"')
def step_impl(context, option_value):
    method = 'sel_list_{0}_element'.format(context.how)
    select_list = getattr(context.page, method)()
    assert_that(select_list.value(), equal_to(option_value))


@then(u'option "{index}" should contain "{option_text}"')
def step_impl(context, index, option_text):
    options = context.page.sel_list_id_element().options_text()
    assert_that(options[int(index)-1], equal_to(option_text))


@then(u'each option should contain "{text}"')
def step_impl(context, text):
    options = context.page.sel_list_id_element().options_text()
    assert_that(all(text in option for option in options))
