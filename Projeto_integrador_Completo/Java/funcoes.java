import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.*;
import java.lang.Thread;
import java.util.Scanner;

public class funcoes {
    Scanner sc = new Scanner(System.in);
    public void ler(String arquivo, String nome_arquivo) throws InterruptedException {
        String arquivo_csv = arquivo + nome_arquivo;
        System.out.println(arquivo_csv);
        String linha = "";
        String separar_csv = "; ";

        try (BufferedReader br = new BufferedReader(new FileReader(arquivo_csv))) {
            while ((linha = br.readLine()) != null) {
                String[] data = linha.split(separar_csv);
                for (String value : data) {
                    System.out.print(value + " ");
                }
                System.out.println();
            }
        } catch (IOException e) {
            print_robo("Não foi possível ler o arquivo "+ arquivo_csv);
            enter();
        }
    }

    public void print_robo(String msg) throws InterruptedException {
        for(int i = 0; i < msg.length(); i++){
             char letra = msg.charAt(i);
            System.out.print(letra);
            Thread.sleep(125);
        }
    }

    public void enter(){
        System.out.println();
    }

    public String tratar_arquivo(String arquivo){
        String novo_arquivo = arquivo.replaceAll("\\\\", "//") + "//";
        return novo_arquivo;
    }

    public String continuar() throws InterruptedException {
        String escolha = "false";
        print_robo("Para continuar, digite ['S']");
        String op = sc.next();
        if(op.equalsIgnoreCase("s")) {
           escolha = "true";
        }
        return escolha;
    }
}

