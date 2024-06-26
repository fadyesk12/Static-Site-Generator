from htmlnode import HTMLNode
class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag,None,children,props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag not provided")
        
        if self.children is None:
            raise ValueError("children not provided")
        resultHTML = ""
        for node in self.children:
            resultHTML += node.to_html()
        resultHTML = f"<{self.tag}{self.props_to_html()}>" + resultHTML
        resultHTML += f"</{self.tag}>"
        return resultHTML
    
    def __repr__(self):
        return f"ParentNode({self.tag},children: {self.children},{self.props})"