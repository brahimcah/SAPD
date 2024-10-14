import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.*;
import java.nio.file.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.zip.*;
import java.awt.Desktop;
import java.net.URI;
import java.net.URISyntaxException;

public class FormWindow extends JFrame {

    private JTextField email1Field;
    private JTextField email2Field;
    private JTextField codigoField;
    private JTextArea cellsField;

    public FormWindow() {
        setTitle("Formulario");
        setSize(500, 500);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Usar BoxLayout para organizar los componentes verticalmente
        setLayout(new BoxLayout(getContentPane(), BoxLayout.Y_AXIS));
        add(Box.createRigidArea(new Dimension(0, 10))); // Espacio en blanco

        add(createLabelAndField("Email 1:", email1Field = new JTextField(20)));
        add(Box.createRigidArea(new Dimension(0, 10))); // Espacio en blanco
        add(createLabelAndField("Email 2:", email2Field = new JTextField(20)));
        add(Box.createRigidArea(new Dimension(0, 10))); // Espacio en blanco
        add(createLabelAndField("CODIGO CENTRO (EX: GE0000):", codigoField = new JTextField(20)));
        add(Box.createRigidArea(new Dimension(0, 10))); // Espacio en blanco

        add(createLabel("Cells:"));
        cellsField = new JTextArea(10, 40);
        add(new JScrollPane(cellsField));
        add(Box.createRigidArea(new Dimension(0, 10))); // Espacio en blanco

        JButton generateCsvButton = new JButton("Generate CSV");
        generateCsvButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                try {
                    generateCsv();
                } catch (IOException ex) {
                    showError("Error generando el archivo CSV: " + ex.getMessage());
                }
            }
        });
        add(generateCsvButton);
        add(Box.createRigidArea(new Dimension(0, 10))); // Espacio en blanco

        add(createLabel("Versión: 1.0.1 - 30/03/2023"));
    }

    private JPanel createLabelAndField(String labelText, JTextField textField) {
        JPanel panel = new JPanel();
        panel.setLayout(new FlowLayout(FlowLayout.LEFT));
        panel.add(new JLabel(labelText));
        panel.add(textField);
        return panel;
    }

    private JLabel createLabel(String text) {
        return new JLabel(text);
    }

    private void generateCsv() throws IOException {
        String email1 = email1Field.getText();
        String email2 = email2Field.getText();
        String codigo = codigoField.getText();
        String cells = cellsField.getText();

        // Guardar email en mail.txt
        String mailsTotal = email2.isEmpty() ? email1 : email1 + ";" + email2;
        writeToFile("mail.txt", mailsTotal);

        // Guardar código en auto.txt
        writeToFile("auto.txt", codigo);

        // Crear CSV
        try (BufferedWriter writer = Files.newBufferedWriter(Paths.get("permisos.csv"))) {
            for (String row : cells.split("\n")) {
                writer.write(row.replace("\t", ","));
                writer.newLine();
            }
        }
        System.out.println("Archivo CSV generado.");
        compra();
    }

    private void compra() {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("ddMMyyyyHHmmss");
        String format = LocalDateTime.now().format(formatter);
        String zipFilePath = "C:/permdev/" + format + ".zip";

        try (ZipOutputStream zos = new ZipOutputStream(new FileOutputStream(zipFilePath))) {
            addToZipFile("auto.txt", zos);
            addToZipFile("mail.txt", zos);
            addToZipFile("permisos.csv", zos);
        } catch (IOException e) {
            showError("Error creando el archivo ZIP: " + e.getMessage());
            return; // Salir si hay un error
        }

        try {
            String mailsend = readFile("mail.txt");
            String mailtoUrl = "mailto:" + mailsend + "?&subject=CSV-ZIP PERMISOS DEV"
                    + "&body=Buenos días,%0A te adjunto los datos del programa: %0A %0A Un Saludo.zip";
            openUrl(mailtoUrl);
            openUrl("file:///C:/permdev");
        } catch (IOException e) {
            showError("Error leyendo el archivo de correos: " + e.getMessage());
        }
    }

    private void writeToFile(String fileName, String content) throws IOException {
        try (BufferedWriter writer = Files.newBufferedWriter(Paths.get(fileName))) {
            writer.write(content);
        }
    }

    private String readFile(String fileName) throws IOException {
        return new String(Files.readAllBytes(Paths.get(fileName)));
    }

    private void addToZipFile(String fileName, ZipOutputStream zos) throws IOException {
        try (FileInputStream fis = new FileInputStream(fileName)) {
            ZipEntry zipEntry = new ZipEntry(fileName);
            zos.putNextEntry(zipEntry);

            byte[] bytes = new byte[1024];
            int length;
            while ((length = fis.read(bytes)) >= 0) {
                zos.write(bytes, 0, length);
            }
            zos.closeEntry();
        }
    }

    private void openUrl(String url) {
        if (Desktop.isDesktopSupported()) {
            try {
                Desktop.getDesktop().browse(new URI(url));
            } catch (IOException | URISyntaxException e) {
                showError("Error abriendo la URL: " + e.getMessage());
            }
        } else {
            showError("La funcionalidad de escritorio no es soportada.");
        }
    }

    private void showError(String message) {
        JOptionPane.showMessageDialog(this, message, "Error", JOptionPane.ERROR_MESSAGE);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            FormWindow formWindow = new FormWindow();
            formWindow.setVisible(true);
        });
    }
}
