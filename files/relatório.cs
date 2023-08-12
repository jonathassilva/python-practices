using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;

class Program
{
    static void Main()
    {
        List<User> users = ReadUsersFromFile("usuarios.txt");
        CalculateSpaceAndPercentage(users);

        using (StreamWriter writer = new StreamWriter("relatorio.txt"))
        {
            writer.WriteLine("ACME Inc.               Uso do espaço em disco pelos usuários");
            writer.WriteLine("------------------------------------------------------------------------");
            writer.WriteLine("Nr.  Usuário        Espaço utilizado     % do uso");
            
            int count = 1;
            foreach (User user in users)
            {
                writer.WriteLine($"{count,-4}  {user.Name,-15} {user.UsedSpace,-20} {user.PercentageOfUsage,-10}");
                count++;
            }
            
            double totalSpace = users.Sum(u => u.UsedSpace);
            double averageSpace = totalSpace / users.Count;

            writer.WriteLine($"\nEspaço total ocupado: {ConvertToMegabytes(totalSpace):F2} MB");
            writer.WriteLine($"Espaço médio ocupado: {ConvertToMegabytes(averageSpace):F2} MB");
        }
        
        Console.WriteLine("Relatório gerado com sucesso!");
    }

    static List<User> ReadUsersFromFile(string fileName)
    {
        List<User> users = new List<User>();
        string[] lines = File.ReadAllLines(fileName);

        foreach (string line in lines)
        {
            string name = line.Substring(0, 15).Trim();
            long usedSpace = long.Parse(line.Substring(15).Trim());
            users.Add(new User { Name = name, UsedSpace = usedSpace });
        }

        return users;
    }

    static void CalculateSpaceAndPercentage(List<User> users)
    {
        long totalSpace = users.Sum(u => u.UsedSpace);
        
        foreach (User user in users)
        {
            user.UsedSpace = ConvertToMegabytes(user.UsedSpace);
            user.PercentageOfUsage = ((double)user.UsedSpace / totalSpace) * 100;
        }
    }

    static double ConvertToMegabytes(long bytes)
    {
        return (double)bytes / (1024 * 1024);
    }
}

class User
{
    public string Name { get; set; }
    public double UsedSpace { get; set; }
    public double PercentageOfUsage { get; set; }
}
