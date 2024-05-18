from tkinter import simpledialog
from AVLTree import AVLTree
import tkinter as tk
from tkinter import ttk

class AVLTreeVisualizer(tk.Tk):
    def __init__(self, avl_tree):
        super().__init__()
        self.title("AVL Tree Visualizer")
        self.geometry("800x600")
        self.avl_tree = avl_tree
        self.canvas = tk.Canvas(self, width=800, height=600, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.bind("<Return>", self.insert_node)
        self.bind("<Delete>", self.delete_node)
        self.node_positions = {}
        self.node_radius = 20
        self.node_gap_x = 50
        self.node_gap_y = 50

        self.draw_tree()

    def draw_tree(self):
        self.canvas.delete("all")
        if self.avl_tree.root:
            self._draw_node(self.avl_tree.root, 400, 50, 200)

    def _draw_node(self, node, x, y, x_offset):
        if node:
            self.canvas.create_oval(x - self.node_radius, y - self.node_radius,
                                    x + self.node_radius, y + self.node_radius, fill="lightblue")
            self.canvas.create_text(x, y, text=str(node.element))
            balance_factor = self.avl_tree.balanceFactor(node)
            self.canvas.create_text(x, y + 25, text=f"BF: {balance_factor}")
            if node.left:
                self.canvas.create_line(x, y + self.node_radius, x - x_offset, y + self.node_gap_y - self.node_radius)
                self._draw_node(node.left, x - x_offset, y + self.node_gap_y, x_offset // 2)
            if node.right:
                self.canvas.create_line(x, y + self.node_radius, x + x_offset, y + self.node_gap_y - self.node_radius)
                self._draw_node(node.right, x + x_offset, y + self.node_gap_y, x_offset // 2)

    def insert_node(self, event):
        value = simpledialog.askstring("Input", "Enter a value to insert:")
        if value:
            self.avl_tree.insert(value)
            self.draw_tree()

    def delete_node(self, event):
        value = simpledialog.askstring("Input", "Enter a value to delete:")
        if value:
            self.avl_tree.delete(value)
            self.draw_tree()

if __name__ == "__main__":
    avl_tree = AVLTree()
    #avl_tree.insert(50)
    #avl_tree.insert(30)
    #avl_tree.insert(70)
    #avl_tree.insert(20)
    #avl_tree.insert(40)
    #avl_tree.insert(60)
    #avl_tree.insert(80)
    
    avl_tree.insert(50)
    avl_tree.insert(30)
    avl_tree.insert(70)
    avl_tree.insert(20)
    avl_tree.insert(40)
    avl_tree.insert(35)
    
    app = AVLTreeVisualizer(avl_tree)
    app.mainloop()