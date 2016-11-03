from hamcrest import assert_that, equal_to


@when(u'I get the image element')
def step_impl(context):
    context.element = context.page.image_id_element()


@when(u'I get the image element by "{how}"')
def step_impl(context, how):
    method = 'image_{0}_element'.format(how)
    context.element = getattr(context.page, method)()


@then(u'the image should be "{expected_pixels}" pixels wide')
def step_impl(context, expected_pixels):
    assert_that(context.element.width, equal_to(expected_pixels))


@then(u'the image should be "{expected_pixels}" pixels tall')
def step_impl(context, expected_pixels):
    assert_that(context.element.height, equal_to(expected_pixels))
