"""
classes
XMLObject
 - GetRoot

Tag
 - SetName
 - NewTag
 - AddAttribute
 - Print
"""


class XMLObject:

    def __init__(self, root_tag_name):
        self.root = Element(root_tag_name)
        return

    def get_root(self):
        return self.root

    def display(self):
        self.root.display()


class Element:

    def __init__(self, name_to_use, string_value=None):
        self.name = name_to_use
        self.child_tags = []
        self.attributes = {}
        self.string_value = string_value
        return

    def set_name(self, name):
        self.name = name
        return

    def add_element(self, name, string_value=None):
        new_tag = Element(name, string_value)
        self.child_tags.append(new_tag)
        return new_tag

    def add_attribute(self, key, value):
        self.attributes[key] = value
        return

    def display(self, depth=0):
        opening_tag = self.get_opening_tag(depth)

        if not self.child_tags:
            closing_tag = self.get_closing_tag(0)
            print("%s%s%s" % (opening_tag, self.string_value, closing_tag))
        else:
            print(opening_tag)
            for child_tag in self.child_tags:
                child_tag.display(depth=depth+1)
            closing_tag = self.get_closing_tag(depth)
            print(closing_tag)
        return

    def get_opening_tag(self, depth=0):
        attributes_string = self.get_attributes_string()
        return "%s<%s%s>" % ("\t" * depth, self.name, attributes_string)

    def get_closing_tag(self, depth=0):
        return "%s</%s>" % ("\t" * depth, self.name)

    def get_attributes_string(self):
        attributes_string = ""
        for key, value in self.attributes.items():
            current_attribute_string = " %s=\"%s\"" % (key, value)
            attributes_string += current_attribute_string
        return attributes_string


def main():
    x = XMLObject("test")
    root = x.get_root()
    root.set_name("people")

    # First Person
    person = root.add_element("Person")  # using 'add_element' instead of 'NewTag'
    person.add_attribute("id", "2323")
    person.add_attribute("DOB", "1/1/1901")
    fname = person.add_element("FirstName", "John")  # person is a tag
    lname = person.add_element("LastName", "Smith")
    address = person.add_element("address")
    street = address.add_element("street", "123 NW 45th street")
    apartment = street.add_element("apartment", "20")
    address.add_element("city", "Gaithersburg")
    address.add_element("zip", "21234")
    address.add_element("state", "MD")

    person = root.add_element("Person")  # using 'add_element' instead of 'NewTag'
    person.add_attribute("id", "2323")
    person.add_attribute("DOB", "1/1/1901")
    fname = person.add_element("FirstName", "John")  # person is a tag
    lname = person.add_element("LastName", "Smith")
    address = person.add_element("address")
    street = address.add_element("street", "123 NW 45th street")
    street.add_attribute("apartment", "20")
    address.add_element("city", "Gaithersburg")
    address.add_element("zip", "21234")
    address.add_element("state", "MD")


    x.display()



if __name__ == '__main__':
    main()
