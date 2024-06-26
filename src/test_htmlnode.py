import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "text")
        node2 = HTMLNode("p", "text")
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = HTMLNode("p", "text")
        node2 = HTMLNode("a", "text")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = HTMLNode("p", "a3", ["3a","a3"],{"3a":"a3"})
        self.assertEqual(
            "HTMLNode(p, a3,children: [\'3a\', \'a3\'], {\'3a\': \'a3\'})", repr(node)
        )
    
    def test_propstohtml(self):
        node = HTMLNode("This is a text node", "text", [],{"3a":"a3"})
        self.assertEqual(
            " 3a=\"a3\"", node.props_to_html()
        )

if __name__ == "__main__":
    unittest.main()