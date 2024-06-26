import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode(tag="p", value="text")
        node2 = LeafNode(tag="p", value="text")
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = LeafNode(tag="p", value="text")
        node2 = LeafNode(tag="a", value="text")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = LeafNode(tag="p", value="a3",props={"3a":"a3"})
        self.assertEqual(
            "LeafNode(p,a3,{\'3a\': \'a3\'})", repr(node)
        )
    
    def test_tohtml(self):
        node = LeafNode(None,value="This is a text node", props={"3a":"a3"})
        self.assertEqual("This is a text node",node.to_html())

    def test_tohtml2(self):
        node = LeafNode(tag="a", value="This is a text node", props={"3a":"a3"})
        self.assertEqual("<a 3a=\"a3\">This is a text node</a>",node.to_html())

    def test_propstohtml(self):
        node = LeafNode(None,value="This is a text node", props={"3a":"a3"})
        self.assertEqual(
            " 3a=\"a3\"", node.props_to_html()
        )

if __name__ == "__main__":
    unittest.main()