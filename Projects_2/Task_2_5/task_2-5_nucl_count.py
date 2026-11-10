dna = input("input DNA sequence ").upper()

a_amount = dna.count('A')  
t_amount = dna.count('T')
g_amount = dna.count('G')
c_amount = dna.count('C')

sequence_length = len(dna)

a_rate = a_amount*100 / sequence_length
t_rate = t_amount*100 / sequence_length
g_rate = g_amount*100 / sequence_length
c_rate = c_amount*100 / sequence_length

print(f"DNA sequence analysis:\tA amount:  {a_amount}\tT amount:  {t_amount}\tG amount:  {g_amount}\tC amount:  {c_amount}\t\tA rate:  {a_rate}%\tT rate:   {t_rate}%\tG rate:   {g_rate}%\tC rate:   {c_rate}%")