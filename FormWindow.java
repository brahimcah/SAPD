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
        setLayout(new FlowLayout());

        add(new JLabel("Email 1:"));
        email1Field = new JTextField(20);
        add(email1Field);

        add(new JLabel("Email 2:"));
        email2Field = new JTextField(20);
        add(email2Field);

        add(new JLabel("CODIGO CENTRO (EX: GE0000):"));
        codigoField = new JTextField(20);
        add(codigoField);

        add(new JLabel("Cells:"));
        cellsField = new JTextArea(10, 40);
        add(new JScrollPane(cellsField));

        JButton generateCsvButton = new JButton("Generate CSV");
        generateCsvButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                try {
                    generateCsv();
                } catch (IOException ex) {
                    ex.printStackTrace();
                }
            }
        });
        add(generateCsvButton);

        add(new JLabel("Versión: 1.0.1 - 30/03/2023"));
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
        System.out.println("CSV file generated.");
        compra();
    }

    private void compra() throws IOException {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("ddMMyyyyHHmmss");
        String format = LocalDateTime.now().format(formatter);

        String zipFilePath = "C:/permdev/" + format + ".zip";
        try (ZipOutputStream zos = new ZipOutputStream(new FileOutputStream(zipFilePath))) {
            addToZipFile("auto.txt", zos);
            addToZipFile("mail.txt", zos);
            addToZipFile("permisos.csv", zos);
        }

        String mailsend = readFile("mail.txt");
        String mailtoUrl = "mailto:" + mailsend + "?&subject=CSV-ZIP PERMISOS DEV"
                + "&body=Buenos días,%0A te adjunto los datos del programa: %0A %0A Un Saludo.zip";
        openUrl(mailtoUrl);
        openUrl("file:///C:/permdev");
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
                e.printStackTrace();
            }
        } else {
            System.out.println("Desktop not supported");
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            FormWindow formWindow = new FormWindow();
            formWindow.setVisible(true);
        });
    }
}
