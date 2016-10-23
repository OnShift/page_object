# PageObject
PageObject implementation in Python

# Using the PageObject Pattern

```python
# Example PageObject class
from support.page_object import PageObject

class ExamplePage(PageObject):

    page_url = 'http://pageurl'

    def initialize_page(self):
          # name: can be anything you want
          # id: must match html id on page
          self.table(name = "example", id = "example_id")
```

### Visit a PageObject

```python
@when('I view the example page')
def visit_example(context):
    visit_page(ExamplePage)
```

### Using PageObject Accessor methods

```python
   on_page(ExamplePage).example_element
```

### Available Element Accessors
- Table
-
