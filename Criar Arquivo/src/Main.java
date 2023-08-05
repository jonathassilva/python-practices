import java.io.*;
import java.io.BufferedReader;
import java.util.ArrayList;
public class Main {
    public static void main(String[] args) throws IOException {
        FileReader path = new FileReader("usuarios.txt");
        BufferedReader br = new BufferedReader(path);
        int numerodeusuarios = 0;
        double espacoutilizado = 0;
        ArrayList<String> usuarios = new ArrayList<>();
        ArrayList<String> Nomes = new ArrayList<>();
        ArrayList<Double> MB = new ArrayList<>();
        ArrayList<String> porcentagem = new ArrayList<>();
        ArrayList<String> MBString = new ArrayList<>();
        String line = br.readLine();

        while (line != null) {
            usuarios.add(line);
            numerodeusuarios++;
            line = br.readLine();
        }
        for (String nome: usuarios){
            Nomes.add(nome.substring(0,15));
            String nbytes = (nome.substring(16)).trim();
            double mb = Double.parseDouble(nbytes);
            mb = mb / (1024 * 1024);
            MB.add(mb);
        }
        for(Double mbytes: MB){
            espacoutilizado += mbytes;
        }

        Double espacomedio = espacoutilizado/numerodeusuarios;

        for(Double mbytes: MB){
            double porcent = (mbytes/espacoutilizado)*100;
            String Porcentagem = String.format("%.2f", porcent);
            if(Porcentagem.length() == 4){
                String espacos = "   ";
                Porcentagem = espacos.concat(Porcentagem);
                Porcentagem = Porcentagem.concat("%");
                porcentagem.add(Porcentagem);
            }
            else if(Porcentagem.length() == 5){
                String espacos = "  ";
                Porcentagem = espacos.concat(Porcentagem);
                Porcentagem = Porcentagem.concat("%");
                porcentagem.add(Porcentagem);
            }
            else if(Porcentagem.length() == 6){
                String espacos = " ";
                Porcentagem = espacos.concat(Porcentagem);
                Porcentagem = Porcentagem.concat("%");
                porcentagem.add(Porcentagem);
            }
            else{
                Porcentagem = Porcentagem.concat("%");
                porcentagem.add(Porcentagem);
            }


            String MbytesString = String.format("%.2f", mbytes);
            if(MbytesString.length() == 4){
                String espacos = "   ";
                MbytesString = espacos.concat(MbytesString);
                MbytesString = MbytesString.concat(" MB");
                MBString.add(MbytesString);
            }
            else if(MbytesString.length() == 5){
                String espacos = "  ";
                MbytesString = espacos.concat(MbytesString);
                MbytesString = MbytesString.concat(" MB");
                MBString.add(MbytesString);
            }
            else if(MbytesString.length() == 6){
                String espacos = " ";
                MbytesString = espacos.concat(MbytesString);
                MbytesString = MbytesString.concat(" MB");
                MBString.add(MbytesString);
            }
            else {
                MbytesString = MbytesString.concat(" MB");
                MBString.add(MbytesString);
            }
        }

        String ESPACOUTILIZADO = String.format("%.2f", espacoutilizado);
        String ESPACOMEDIO = String.format("%.2f", espacomedio);
        ESPACOUTILIZADO = ESPACOUTILIZADO.concat(" MB");
        ESPACOMEDIO = ESPACOMEDIO.concat(" MB");

        try {
            FileWriter relatorio = new FileWriter("relatorio.txt");
            PrintWriter escreverrelatorio = new PrintWriter(relatorio);
            escreverrelatorio.println("ACME Inc.               Uso do espaço em disco pelos usuários");
            escreverrelatorio.println("------------------------------------------------------------------------");
            escreverrelatorio.println("Nr.  Usuário        Espaço utilizado     % do uso");
            escreverrelatorio.println("");

            for(int i = 0; i < numerodeusuarios; i++) {
                escreverrelatorio.print(i + 1);
                escreverrelatorio.print("    ");
                escreverrelatorio.print(Nomes.get(i));
                escreverrelatorio.print(MBString.get(i));
                escreverrelatorio.print("           ");
                escreverrelatorio.println(porcentagem.get(i));
            }
            escreverrelatorio.println("");
            escreverrelatorio.println("Espaço total ocupado: " + ESPACOUTILIZADO);
            escreverrelatorio.println("Espaço total ocupado: " + ESPACOMEDIO);
            escreverrelatorio.close();
        }
        catch (IOException e){
            System.out.println(e.getMessage());
        }

    }
}
