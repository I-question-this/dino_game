from dino.blocks.basic import BasicBlock

class InvisibleBlock(BasicBlock):
    def __init__(self, left, top, width, height):
        super().__init__(left, top, width, height)
        self.image.set_alpha(0)
        
