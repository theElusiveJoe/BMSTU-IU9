import javax.swing.*;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;

public class PictureForm {
    private JPanel mainPanel;
    private JSpinner heightSpinner;
    private CanvasPanel canvasPanel;
    private JSpinner widthSpinner;

    public PictureForm() {
        heightSpinner.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent changeEvent) {
                int height = (int) heightSpinner.getValue();
                canvasPanel.setHeight(height);
            }
        });
        widthSpinner.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent changeEvent) {
                int width = (int) widthSpinner.getValue();
                canvasPanel.setWidth(width);
            }
        });
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Sircle");
        frame.setContentPane(new PictureForm().mainPanel);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
    }

    private void createUIComponents() {
        // TODO: place custom component creation code here
    }
}
