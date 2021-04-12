import javax.swing.*;
import java.awt.*;

public class CanvasPanel extends JPanel {
    private int height, width;

    public void setHeight(int h) {
        height = h;
        repaint();
    }

    public void setWidth(int w) {
        width = w;
        repaint();
    }

    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.setColor(Color.orange);
        g.drawLine(350, 700, 350, 700 - height);
        if (height > 50) {
            g.setColor(Color.orange.darker().darker());
            g.drawLine(350, 700, 350, 650);
        }
        g.setColor(Color.green.darker());
        int f1 = 1, f2 = 1, ft, top = 700 - height;
        while (true) {
            top += f1;
            ft = f1;
            f1 += f2;
            f2 = ft;
            if (top > 650) {
                break;
            }
        }
        float tgg = width / 2;
        tgg /= (height - 700 + top);
        if (tgg > 0 && tgg < 1) {
            System.out.println(tgg);
            f1 = 1;
            f2 = 1;
            top = 700-height;
            while (true) {
                top += f1;
                ft = f1;
                f1 += f2;
                f2 = ft;
                System.out.println(top);
                if (top < 650) {
                    g.drawLine(350, top, (int) (350 + (-700 + height + top) * tgg), 700 - height);
                    g.drawLine(350, top, (int) (350 - (-700 + height + top) * tgg), 700 - height);
                } else {
                    break;
                }
            }
        }
    }
}
