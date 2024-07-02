import unittest
from block_markdown import *

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks1(self):
        test_case = ""
        result = markdown_to_blocks(
            "     This is **bolded** paragraph\n\n       This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line\n\n     * This is a list\n* with items"
        )
        self.assertEqual(
            ["This is **bolded** paragraph",
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items"], result)

    def test_block_to_block_type1(self):
        test_case = "## a3"
        test_case_type = "heading"
        self.assertEqual(test_case_type,block_to_block_type(test_case))
    def test_block_to_block_type2(self):
        test_case = "```a3```"
        test_case_type = "code"
        self.assertEqual(test_case_type,block_to_block_type(test_case))
    def test_block_to_block_type3(self):
        test_case = "> a3\n> a3"
        test_case_type = "quote"
        self.assertEqual(test_case_type,block_to_block_type(test_case))
    
    def test_block_to_block_type4(self):
        test_case = "* a3\n- a3"
        test_case_type = "unordered_list"
        self.assertEqual(test_case_type,block_to_block_type(test_case))
    
    def test_block_to_block_type5(self):
        test_case = "1. a3\n2. a3"
        test_case_type = "ordered_list"
        self.assertEqual(test_case_type,block_to_block_type(test_case))
    def test_block_to_block_type6(self):
        test_case = "1. a3\n- a3"
        test_case_type = "paragraph"
        self.assertEqual(test_case_type,block_to_block_type(test_case))
    
    def test_block_to_html_p(self):
        test_case = "a3a3"
        test_case_type = block_to_block_type(test_case)
        print(block_to_HTML(test_case,test_case_type))
        # self.assertEqual("<p>a3a3</p>", block_to_HTML(test_case,test_case_type))
    
    def test_block_to_html_q(self):
        test_case = "> a3a3\n> *a3*"
        test_case_type = block_to_block_type(test_case)
        print(block_to_HTML(test_case,test_case_type))
        # self.assertEqual("<blockquote>a3a3\na3</blockquote>", block_to_HTML(test_case,test_case_type))
    
    def test_block_to_html_h(self):
        test_case = "### a3a3\n# a3"
        test_case_type = block_to_block_type(test_case)
        print(block_to_HTML(test_case,test_case_type))
        # self.assertEqual("<h3>a3a3\na3</h3>", block_to_HTML(test_case,test_case_type))
    
    def test_block_to_html_c(self):
        test_case = "```a3a3\na3```"
        test_case_type = block_to_block_type(test_case)
        print(block_to_HTML(test_case,test_case_type))
        # self.assertEqual("<pre><code>a3a3\na3</code></pre>", block_to_HTML(test_case,test_case_type))

    def test_block_to_html_ul(self):
        test_case = "* a3\n- a3a3"
        test_case_type = block_to_block_type(test_case)
        print(block_to_HTML(test_case,test_case_type))
        # self.assertEqual("<ul><li>a3</li><li>a3a3</li></ul>", block_to_HTML(test_case,test_case_type))
    
    def test_block_to_html_ol(self):
        test_case = "1. a3\n2. a3"
        test_case_type = block_to_block_type(test_case)
        print(block_to_HTML(test_case,test_case_type))
        # self.assertEqual("<ol><li>a3</li><li>a3</li></ol>", block_to_HTML(test_case,test_case_type))
    