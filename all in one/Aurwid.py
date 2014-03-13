import urwid
from urwid import *
class AGridFlow(urwid.GridFlow):
    def generate_display_widget(self, size):
        """
        Actually generate display widget (ignoring cache)
        """
        (maxcol,) = size
        d = Divider()
        if len(self.cells) == 0: # how dull
            return d

        if self.v_sep > 1:
            # increase size of divider
            d.top = self.v_sep-1

        # cells per row
        bpr = (maxcol+self.h_sep) // (self.cell_width+self.h_sep)

        if bpr == 0: # too narrow, pile them on top of eachother
            l = [self.cells[0]]
            f = 0
            for b in self.cells[1:]:
                if b is self.focus_cell:
                    f = len(l)
                if self.v_sep:
                    l.append(d)
                l.append(b)
            return Pile(l, f)
        
        if bpr >= len(self.cells): # all fit on one row
            k = len(self.cells)
            f = self.cells.index(self.focus_cell)
            cols = AColumns(self.cells, self.h_sep, f)
            rwidth = (self.cell_width+self.h_sep)*k - self.h_sep
            row = Padding(cols, self.align, rwidth)
            return row

        
        out = []
        s = 0
        f = 0
        while s < len(self.cells):
            if out and self.v_sep:
                out.append(d)
            k = min( len(self.cells), s+bpr )
            cells = self.cells[s:k]
            if self.focus_cell in cells:
                f = len(out)
                fcol = cells.index(self.focus_cell)
                cols = AColumns(cells, self.h_sep, fcol)
            else:
                cols = AColumns(cells, self.h_sep)
            rwidth = (self.cell_width+self.h_sep)*(k-s)-self.h_sep
            row = Padding(cols, self.align, rwidth)
            out.append(row)
            s += bpr
        return Pile(out, f)    

class AColumns(urwid.Columns):
    def render(self, size, focus=False):
        """Render columns and return canvas.

        size -- (maxcol,) if self.widget_list contains flow widgets or
            (maxcol, maxrow) if it contains box widgets.
        """
        widths = self.column_widths(size, focus)
        if not widths:
            return SolidCanvas(" ", size[0], (size[1:]+(1,))[0])
        
        box_maxrow = None
        if len(size)==1 and self.box_columns:
            box_maxrow = 1
            # two-pass mode to determine maxrow for box columns
            for i in range(len(widths)):
                if i in self.box_columns:
                    continue
                mc = widths[i]
                w = self.widget_list[i]
                rows = w.rows( (mc,), 
                    focus = focus)#ARGON and self.focus_col == i )
                box_maxrow = max(box_maxrow, rows)
        
        l = []
        for i in range(len(widths)):
            mc = widths[i]

            # if the widget has a width of 0, hide it
            if mc <= 0:
                continue

            w = self.widget_list[i]
            if box_maxrow and i in self.box_columns:
                sub_size = (mc, box_maxrow)
            else:
                sub_size = (mc,) + size[1:]
            
            canv = w.render(sub_size, 
                focus = focus )#ARGON and self.focus_col == i)

            if i < len(widths)-1:
                mc += self.dividechars
            l.append((canv, i, True,mc))#ARGON self.focus_col == i, mc))
                
        canv = CanvasJoin(l)
        if canv.cols() < size[0]:
            canv.pad_trim_left_right(0, size[0]-canv.cols())
        return canv
