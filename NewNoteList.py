import wx
import wx.lib.agw.customtreectrl as treectrl

class NewNoteList(treectrl.CustomTreeCtrl):
    '''
    重写树, 使其变得更加美观
    '''

    def __init__(self, parent):
        super().__init__(
            parent, wx.ID_ANY, wx.DefaultPosition, wx.Size(300, 700), agwStyle=treectrl.TR_HAS_BUTTONS|treectrl.TR_FULL_ROW_HIGHLIGHT|treectrl.TR_ELLIPSIZE_LONG_ITEMS|treectrl.TR_TOOLTIP_ON_LONG_ITEMS
            |treectrl.TR_HAS_VARIABLE_ROW_HEIGHT)
        panel_font = self.GetFont()
        panel_font.SetPointSize(panel_font.GetPointSize() + 1)
        self.SetFont(panel_font)
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.EnableSelectionGradient(False)
        self.SetSpacing(20)
        self.SetIndent(10)

    def ergodic(self):
        #遍历树
        result = []
        treeRoot = self.GetRootItem()
       

        def recursivelyGetTreeItem(tree, leval):
            ''' 递归遍历TreeCtrl的所有孩子 '''
            (item, cookie) = self.GetFirstChild(tree)
            while item:
                ItemStr = (item, self.GetItemText(item), leval)
                result.append(ItemStr)
                if self.GetChildrenCount(item) > 0:
                    leval += 1
                    recursivelyGetTreeItem(item, leval)
                    leval -= 1
                (item, cookie) = self.GetNextChild(tree, cookie)
                print((item, cookie))

        leval = 0  #递归的子树层次
        recursivelyGetTreeItem(treeRoot, leval)
        print(result)
        return result
    

    def ergodic_item(self, tree):
        #遍历某个树的所有孩子
        try:
            result = []
            (item, cookie) = self.GetFirstChild(tree)
            while item:
                result.append((item, self.GetItemText(item)))
                if self.GetChildrenCount(item) > 0:
                    result.extend(self.ergodic_item(item))
                (item, cookie) = self.GetNextChild(tree, cookie)
            return result
        except:
            return False
        
        
