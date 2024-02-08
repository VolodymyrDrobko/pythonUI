from page.base.element.web_object import WebObject


class WebInput(WebObject):

    def __init__(self, xpath: str, name: str):
        super().__init__(xpath, name + " input")
