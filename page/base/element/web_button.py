from page.base.element.web_object import WebObject


class WebButton(WebObject):

    def __init__(self, xpath: str, name: str):
        super().__init__(xpath, name + " button")
