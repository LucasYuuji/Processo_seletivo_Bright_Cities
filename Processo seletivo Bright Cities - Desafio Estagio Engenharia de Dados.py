#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd


# In[14]:


import pandas as pd

#======================================================CAPITAl========================================================#

natureza = ["HOMICÍDIO DOLOSO (2)", "Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO (3)","HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO OUTROS","TENTATIVA DE HOMICÍDIO","LESÃO CORPORAL SEGUIDA DE MORTE","LESÃO CORPORAL DOLOSA","LESÃO CORPORAL CULPOSA POR ACIDENTE DE TRÂNSITO","LESÃO CORPORAL CULPOSA - OUTRAS","LATROCÍNIO","Nº DE VÍTIMAS EM LATROCÍNIO","TOTAL DE ESTUPRO (4)","ESTUPRO","ESTUPRO DE VULNERÁVEL","TOTAL DE ROUBO - OUTROS (1)","ROUBO - OUTROS","ROUBO DE VEÍCULO","ROUBO A BANCO","ROUBO DE CARGA","FURTO - OUTROS","FURTO DE VEÍCULO"]
ano = [2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021]
regiao = ["Capital","Capital","Capital","Capital","Capital","Capital","Capital","Capital","Capital","Capital","Capital","Capital","Capital","Capital","Capital","Capital","Capital","Capital","Capital","Capital","Capital","Capital","Capital"]
meses_total = [563,603,4,4,387,30,596,17,27765,9841,913,53,56,2339,650,1689,128589,125518,13656,7,3064,187785,34331]

df_capital2021 = pd.DataFrame({"Natureza": natureza, "Ano": ano,"Região": regiao, "Total dos meses": meses_total})

natureza = ["HOMICÍDIO DOLOSO (2)", "Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO (3)","HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO OUTROS","TENTATIVA DE HOMICÍDIO","LESÃO CORPORAL SEGUIDA DE MORTE","LESÃO CORPORAL DOLOSA","LESÃO CORPORAL CULPOSA POR ACIDENTE DE TRÂNSITO","LESÃO CORPORAL CULPOSA - OUTRAS","LATROCÍNIO","Nº DE VÍTIMAS EM LATROCÍNIO","TOTAL DE ESTUPRO (4)","ESTUPRO","ESTUPRO DE VULNERÁVEL","TOTAL DE ROUBO - OUTROS (1)","ROUBO - OUTROS","ROUBO DE VEÍCULO","ROUBO A BANCO","ROUBO DE CARGA","FURTO - OUTROS","FURTO DE VEÍCULO"]
ano = [2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020]
regiao = ["Capital","Capital","Capital","Capital","Capital","Capital","Capital","Capital","Capital","Capital","Capital","Capital","Capital","Capital","Capital","Capital","Capital","Capital","Capital","Capital","Capital","Capital","Capital"]
meses_total = [659,709,7,7,393,22,590,32,25758,9983,996,46,46,2318,604,1714,127513,124552,13965,18,2943,164444,27035]

df_capital2020 = pd.DataFrame({"Natureza": natureza, "Ano": ano,"Região": regiao, "Total dos meses": meses_total})

#======================================================GRANDE SP============================================================#

natureza = ["HOMICÍDIO DOLOSO (2)", "Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO (3)","HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO OUTROS","TENTATIVA DE HOMICÍDIO","LESÃO CORPORAL SEGUIDA DE MORTE","LESÃO CORPORAL DOLOSA","LESÃO CORPORAL CULPOSA POR ACIDENTE DE TRÂNSITO","LESÃO CORPORAL CULPOSA - OUTRAS","LATROCÍNIO","Nº DE VÍTIMAS EM LATROCÍNIO","TOTAL DE ESTUPRO (4)","ESTUPRO","ESTUPRO DE VULNERÁVEL","TOTAL DE ROUBO - OUTROS (1)","ROUBO - OUTROS","ROUBO DE VEÍCULO","ROUBO A BANCO","ROUBO DE CARGA","FURTO - OUTROS","FURTO DE VEÍCULO"]
ano = [2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021]
regiao = ["Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo"]
meses_total = [501,530,1,1,508,45,574,18,20726,8291,572,33,35,2384,477,1907,54475,52478,11041,2,1995,68833,20022]

df_grande_sp2021 = pd.DataFrame({"Natureza": natureza, "Ano": ano,"Região": regiao, "Total dos meses": meses_total})

natureza = ["HOMICÍDIO DOLOSO (2)", "Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO (3)","HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO OUTROS","TENTATIVA DE HOMICÍDIO","LESÃO CORPORAL SEGUIDA DE MORTE","LESÃO CORPORAL DOLOSA","LESÃO CORPORAL CULPOSA POR ACIDENTE DE TRÂNSITO","LESÃO CORPORAL CULPOSA - OUTRAS","LATROCÍNIO","Nº DE VÍTIMAS EM LATROCÍNIO","TOTAL DE ESTUPRO (4)","ESTUPRO","ESTUPRO DE VULNERÁVEL","TOTAL DE ROUBO - OUTROS (1)","ROUBO - OUTROS","ROUBO DE VEÍCULO","ROUBO A BANCO","ROUBO DE CARGA","FURTO - OUTROS","FURTO DE VEÍCULO"]
ano = [2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020]
regiao = ["Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo","Grande São Paulo"]
meses_total = [642,674,6,7,424,45,557,23,19560,7358,538,34,35,2260,510,1750,49756,48109,9872,2,1645,54402,15763]

df_grande_sp2020 = pd.DataFrame({"Natureza": natureza, "Ano": ano,"Região": regiao, "Total dos meses": meses_total})

#======================================================SÃO JOSÉ DOS CAMPOS============================================================#

natureza = ["HOMICÍDIO DOLOSO (2)", "Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO (3)","HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO OUTROS","TENTATIVA DE HOMICÍDIO","LESÃO CORPORAL SEGUIDA DE MORTE","LESÃO CORPORAL DOLOSA","LESÃO CORPORAL CULPOSA POR ACIDENTE DE TRÂNSITO","LESÃO CORPORAL CULPOSA - OUTRAS","LATROCÍNIO","Nº DE VÍTIMAS EM LATROCÍNIO","TOTAL DE ESTUPRO (4)","ESTUPRO","ESTUPRO DE VULNERÁVEL","TOTAL DE ROUBO - OUTROS (1)","ROUBO - OUTROS","ROUBO DE VEÍCULO","ROUBO A BANCO","ROUBO DE CARGA","FURTO - OUTROS","FURTO DE VEÍCULO"]
ano = [2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021]
regiao = ["São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos"]
meses_total = [323,335,0,0,226,11,318,6,6447,2588,126,13,13,677,156,521,5113,4978,889,1,134,20465,2195]

df_sao_jose_campos2021 = pd.DataFrame({"Natureza": natureza, "Ano": ano,"Região": regiao, "Total dos meses": meses_total})

natureza = ["HOMICÍDIO DOLOSO (2)", "Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO (3)","HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO OUTROS","TENTATIVA DE HOMICÍDIO","LESÃO CORPORAL SEGUIDA DE MORTE","LESÃO CORPORAL DOLOSA","LESÃO CORPORAL CULPOSA POR ACIDENTE DE TRÂNSITO","LESÃO CORPORAL CULPOSA - OUTRAS","LATROCÍNIO","Nº DE VÍTIMAS EM LATROCÍNIO","TOTAL DE ESTUPRO (4)","ESTUPRO","ESTUPRO DE VULNERÁVEL","TOTAL DE ROUBO - OUTROS (1)","ROUBO - OUTROS","ROUBO DE VEÍCULO","ROUBO A BANCO","ROUBO DE CARGA","FURTO - OUTROS","FURTO DE VEÍCULO"]
ano = [2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020]
regiao = ["São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos","São José dos Campos"]
meses_total = [326,344,0,0,217,4,369,7,6854,2395,93,8,8,660,157,503,5066,4946,897,3,117,16762,2365]

df_sao_jose_campos2020 = pd.DataFrame({"Natureza": natureza, "Ano": ano,"Região": regiao, "Total dos meses": meses_total})

#======================================================CAMPINAS============================================================#

natureza = ["HOMICÍDIO DOLOSO (2)", "Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO (3)","HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO OUTROS","TENTATIVA DE HOMICÍDIO","LESÃO CORPORAL SEGUIDA DE MORTE","LESÃO CORPORAL DOLOSA","LESÃO CORPORAL CULPOSA POR ACIDENTE DE TRÂNSITO","LESÃO CORPORAL CULPOSA - OUTRAS","LATROCÍNIO","Nº DE VÍTIMAS EM LATROCÍNIO","TOTAL DE ESTUPRO (4)","ESTUPRO","ESTUPRO DE VULNERÁVEL","TOTAL DE ROUBO - OUTROS (1)","ROUBO - OUTROS","ROUBO DE VEÍCULO","ROUBO A BANCO","ROUBO DE CARGA","FURTO - OUTROS","FURTO DE VEÍCULO"]
ano = [2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021]
regiao = ["Campinas","Campinas","Campinas","Campinas","Campinas","Campinas","Campinas","Campinas","Campinas","Campinas","Campinas","Campinas","Campinas","Campinas","Campinas","Campinas","Campinas","Campinas","Campinas","Campinas","Campinas","Campinas","Campinas"]
meses_total = [208,225,1,1,354,8,237,6,9415,5057,95,5,5,932,213,719,9393,8924,3209,2,467,34822,5704]

df_campinas2021 = pd.DataFrame({"Natureza": natureza, "Ano": ano,"Região": regiao, "Total dos meses": meses_total})

natureza = ["HOMICÍDIO DOLOSO (2)", "Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO (3)","HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO OUTROS","TENTATIVA DE HOMICÍDIO","LESÃO CORPORAL SEGUIDA DE MORTE","LESÃO CORPORAL DOLOSA","LESÃO CORPORAL CULPOSA POR ACIDENTE DE TRÂNSITO","LESÃO CORPORAL CULPOSA - OUTRAS","LATROCÍNIO","Nº DE VÍTIMAS EM LATROCÍNIO","TOTAL DE ESTUPRO (4)","ESTUPRO","ESTUPRO DE VULNERÁVEL","TOTAL DE ROUBO - OUTROS (1)","ROUBO - OUTROS","ROUBO DE VEÍCULO","ROUBO A BANCO","ROUBO DE CARGA","FURTO - OUTROS","FURTO DE VEÍCULO"]
ano = [2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020]
regiao = ["Campinas","Campinas","Campinas","Campinas","Campinas","Campinas","Campinas","Campinas","Campinas","Campinas","Campinas","Campinas","Campinas","Campinas","Campinas","Campinas","Campinas","Campinas","Campinas","Campinas","Campinas","Campinas","Campinas"]
meses_total = [228,233,0,0,357,5,218,11,8995,4980,150,26,26,837,228,609,8829,8329,2993,2,498,27082,5427]

df_campinas2020 = pd.DataFrame({"Natureza": natureza, "Ano": ano,"Região": regiao, "Total dos meses": meses_total})



#======================================================RIBEIRÃO PRETO============================================================#

natureza = ["HOMICÍDIO DOLOSO (2)", "Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO (3)","HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO OUTROS","TENTATIVA DE HOMICÍDIO","LESÃO CORPORAL SEGUIDA DE MORTE","LESÃO CORPORAL DOLOSA","LESÃO CORPORAL CULPOSA POR ACIDENTE DE TRÂNSITO","LESÃO CORPORAL CULPOSA - OUTRAS","LATROCÍNIO","Nº DE VÍTIMAS EM LATROCÍNIO","TOTAL DE ESTUPRO (4)","ESTUPRO","ESTUPRO DE VULNERÁVEL","TOTAL DE ROUBO - OUTROS (1)","ROUBO - OUTROS","ROUBO DE VEÍCULO","ROUBO A BANCO","ROUBO DE CARGA","FURTO - OUTROS","FURTO DE VEÍCULO"]
ano = [2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021]
regiao = ["Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto"]
meses_total = [246,252,0,0,381,16,306,9,10549,4304,231,19,19,1038,254,784,5560,5370,999,2,188,34869,4513]

df_ribeirao2021 = pd.DataFrame({"Natureza": natureza, "Ano": ano,"Região": regiao, "Total dos meses": meses_total})

natureza = ["HOMICÍDIO DOLOSO (2)", "Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO (3)","HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO OUTROS","TENTATIVA DE HOMICÍDIO","LESÃO CORPORAL SEGUIDA DE MORTE","LESÃO CORPORAL DOLOSA","LESÃO CORPORAL CULPOSA POR ACIDENTE DE TRÂNSITO","LESÃO CORPORAL CULPOSA - OUTRAS","LATROCÍNIO","Nº DE VÍTIMAS EM LATROCÍNIO","TOTAL DE ESTUPRO (4)","ESTUPRO","ESTUPRO DE VULNERÁVEL","TOTAL DE ROUBO - OUTROS (1)","ROUBO - OUTROS","ROUBO DE VEÍCULO","ROUBO A BANCO","ROUBO DE CARGA","FURTO - OUTROS","FURTO DE VEÍCULO"]
ano = [2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020]
regiao = ["Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto","Ribeirão Preto"]
meses_total = [195,200,1,1,363,10,239,9,9629,4349,250,15,15,813,202,611,4546,4432,888,2,112,28076,3466]

df_ribeirao2020 = pd.DataFrame({"Natureza": natureza, "Ano": ano,"Região": regiao, "Total dos meses": meses_total})

#=========================================================BAURU=================================================================#

natureza = ["HOMICÍDIO DOLOSO (2)", "Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO (3)","HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO OUTROS","TENTATIVA DE HOMICÍDIO","LESÃO CORPORAL SEGUIDA DE MORTE","LESÃO CORPORAL DOLOSA","LESÃO CORPORAL CULPOSA POR ACIDENTE DE TRÂNSITO","LESÃO CORPORAL CULPOSA - OUTRAS","LATROCÍNIO","Nº DE VÍTIMAS EM LATROCÍNIO","TOTAL DE ESTUPRO (4)","ESTUPRO","ESTUPRO DE VULNERÁVEL","TOTAL DE ROUBO - OUTROS (1)","ROUBO - OUTROS","ROUBO DE VEÍCULO","ROUBO A BANCO","ROUBO DE CARGA","FURTO - OUTROS","FURTO DE VEÍCULO"]
ano = [2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021]
regiao = ["Bauru","Bauru","Bauru","Bauru","Bauru","Bauru","Bauru","Bauru","Bauru","Bauru","Bauru","Bauru","Bauru","Bauru","Bauru","Bauru","Bauru","Bauru","Bauru","Bauru","Bauru","Bauru","Bauru"]
meses_total = [108,112,1,1,207,5,183,5,6470,4712,120,7,7,624,129,495,1262,1221,114,0,41,17277,1132]

df_bauru2021 = pd.DataFrame({"Natureza": natureza, "Ano": ano,"Região": regiao, "Total dos meses": meses_total})

natureza = ["HOMICÍDIO DOLOSO (2)", "Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO (3)","HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO OUTROS","TENTATIVA DE HOMICÍDIO","LESÃO CORPORAL SEGUIDA DE MORTE","LESÃO CORPORAL DOLOSA","LESÃO CORPORAL CULPOSA POR ACIDENTE DE TRÂNSITO","LESÃO CORPORAL CULPOSA - OUTRAS","LATROCÍNIO","Nº DE VÍTIMAS EM LATROCÍNIO","TOTAL DE ESTUPRO (4)","ESTUPRO","ESTUPRO DE VULNERÁVEL","TOTAL DE ROUBO - OUTROS (1)","ROUBO - OUTROS","ROUBO DE VEÍCULO","ROUBO A BANCO","ROUBO DE CARGA","FURTO - OUTROS","FURTO DE VEÍCULO"]
ano = [2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020]
regiao = ["Bauru","Bauru","Bauru","Bauru","Bauru","Bauru","Bauru","Bauru","Bauru","Bauru","Bauru","Bauru","Bauru","Bauru","Bauru","Bauru","Bauru","Bauru","Bauru","Bauru","Bauru","Bauru","Bauru"]
meses_total = [117,121,1,1,196,7,205,5,6325,4548,90,9,9,595,134,461,1253,1224,112,1,28,14307,1051]

df_bauru2020 = pd.DataFrame({"Natureza": natureza, "Ano": ano,"Região": regiao, "Total dos meses": meses_total})


#===================================================SÃO JOSÉ DO RIO PRETO============================================================#

natureza = ["HOMICÍDIO DOLOSO (2)", "Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO (3)","HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO OUTROS","TENTATIVA DE HOMICÍDIO","LESÃO CORPORAL SEGUIDA DE MORTE","LESÃO CORPORAL DOLOSA","LESÃO CORPORAL CULPOSA POR ACIDENTE DE TRÂNSITO","LESÃO CORPORAL CULPOSA - OUTRAS","LATROCÍNIO","Nº DE VÍTIMAS EM LATROCÍNIO","TOTAL DE ESTUPRO (4)","ESTUPRO","ESTUPRO DE VULNERÁVEL","TOTAL DE ROUBO - OUTROS (1)","ROUBO - OUTROS","ROUBO DE VEÍCULO","ROUBO A BANCO","ROUBO DE CARGA","FURTO - OUTROS","FURTO DE VEÍCULO"]
ano = [2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021]
regiao = ["São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto"]
meses_total = [86,87,0,0,173,6,169,1,5585,5647,167,3,3,568,114,454,1031,1006,106,1,24,13688,1358]

df_sao_jose_riopreto2021 = pd.DataFrame({"Natureza": natureza, "Ano": ano,"Região": regiao, "Total dos meses": meses_total})

natureza = ["HOMICÍDIO DOLOSO (2)", "Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO (3)","HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO OUTROS","TENTATIVA DE HOMICÍDIO","LESÃO CORPORAL SEGUIDA DE MORTE","LESÃO CORPORAL DOLOSA","LESÃO CORPORAL CULPOSA POR ACIDENTE DE TRÂNSITO","LESÃO CORPORAL CULPOSA - OUTRAS","LATROCÍNIO","Nº DE VÍTIMAS EM LATROCÍNIO","TOTAL DE ESTUPRO (4)","ESTUPRO","ESTUPRO DE VULNERÁVEL","TOTAL DE ROUBO - OUTROS (1)","ROUBO - OUTROS","ROUBO DE VEÍCULO","ROUBO A BANCO","ROUBO DE CARGA","FURTO - OUTROS","FURTO DE VEÍCULO"]
ano = [2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020]
regiao = ["São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto","São José do Rio Preto"]
meses_total = [82,82,0,0,185,7,140,3,5479,4996,179,5,5,553,116,437,981,968,87,0,13,11766,1278]

df_sao_jose_riopreto2020 = pd.DataFrame({"Natureza": natureza, "Ano": ano,"Região": regiao, "Total dos meses": meses_total})

#===========================================================SANTOS================================================================#

natureza = ["HOMICÍDIO DOLOSO (2)", "Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO (3)","HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO OUTROS","TENTATIVA DE HOMICÍDIO","LESÃO CORPORAL SEGUIDA DE MORTE","LESÃO CORPORAL DOLOSA","LESÃO CORPORAL CULPOSA POR ACIDENTE DE TRÂNSITO","LESÃO CORPORAL CULPOSA - OUTRAS","LATROCÍNIO","Nº DE VÍTIMAS EM LATROCÍNIO","TOTAL DE ESTUPRO (4)","ESTUPRO","ESTUPRO DE VULNERÁVEL","TOTAL DE ROUBO - OUTROS (1)","ROUBO - OUTROS","ROUBO DE VEÍCULO","ROUBO A BANCO","ROUBO DE CARGA","FURTO - OUTROS","FURTO DE VEÍCULO"]
ano = [2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021]
regiao = ["Santos","Santos","Santos","Santos","Santos","Santos","Santos","Santos","Santos","Santos","Santos","Santos","Santos","Santos","Santos","Santos","Santos","Santos","Santos","Santos","Santos","Santos","Santos"]
meses_total = [150,153,0,0,233,7,220,3,5397,2793,172,10,11,647,137,510,11146,10862,875,1,283,29216,2744]

df_santos2021 = pd.DataFrame({"Natureza": natureza, "Ano": ano,"Região": regiao, "Total dos meses": meses_total})

natureza = ["HOMICÍDIO DOLOSO (2)", "Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO (3)","HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO OUTROS","TENTATIVA DE HOMICÍDIO","LESÃO CORPORAL SEGUIDA DE MORTE","LESÃO CORPORAL DOLOSA","LESÃO CORPORAL CULPOSA POR ACIDENTE DE TRÂNSITO","LESÃO CORPORAL CULPOSA - OUTRAS","LATROCÍNIO","Nº DE VÍTIMAS EM LATROCÍNIO","TOTAL DE ESTUPRO (4)","ESTUPRO","ESTUPRO DE VULNERÁVEL","TOTAL DE ROUBO - OUTROS (1)","ROUBO - OUTROS","ROUBO DE VEÍCULO","ROUBO A BANCO","ROUBO DE CARGA","FURTO - OUTROS","FURTO DE VEÍCULO"]
ano = [2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020]
regiao = ["Santos","Santos","Santos","Santos","Santos","Santos","Santos","Santos","Santos","Santos","Santos","Santos","Santos","Santos","Santos","Santos","Santos","Santos","Santos","Santos","Santos","Santos","Santos"]
meses_total = [121,128,1,5,228,2,237,11,5588,2402,109,14,16,639,148,491,11845,11584,900,0,261,25464,2174]

df_santos2020 = pd.DataFrame({"Natureza": natureza, "Ano": ano,"Região": regiao, "Total dos meses": meses_total})

#==========================================================SOROCABA==============================================================#

natureza = ["HOMICÍDIO DOLOSO (2)", "Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO (3)","HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO OUTROS","TENTATIVA DE HOMICÍDIO","LESÃO CORPORAL SEGUIDA DE MORTE","LESÃO CORPORAL DOLOSA","LESÃO CORPORAL CULPOSA POR ACIDENTE DE TRÂNSITO","LESÃO CORPORAL CULPOSA - OUTRAS","LATROCÍNIO","Nº DE VÍTIMAS EM LATROCÍNIO","TOTAL DE ESTUPRO (4)","ESTUPRO","ESTUPRO DE VULNERÁVEL","TOTAL DE ROUBO - OUTROS (1)","ROUBO - OUTROS","ROUBO DE VEÍCULO","ROUBO A BANCO","ROUBO DE CARGA","FURTO - OUTROS","FURTO DE VEÍCULO"]
ano = [2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021]
regiao = ["Sorocaba","Sorocaba","Sorocaba","Sorocaba","Sorocaba","Sorocaba","Sorocaba","Sorocaba","Sorocaba","Sorocaba","Sorocaba","Sorocaba","Sorocaba","Sorocaba","Sorocaba","Sorocaba","Sorocaba","Sorocaba","Sorocaba","Sorocaba","Sorocaba","Sorocaba","Sorocaba"]
meses_total = [156,162,2,2,375,7,226,5,7965,3203,82,10,10,1270,247,1023,3037,2919,591,0,118,23211,2495]

df_sorocaba2021 = pd.DataFrame({"Natureza": natureza, "Ano": ano,"Região": regiao, "Total dos meses": meses_total})

natureza = ["HOMICÍDIO DOLOSO (2)", "Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO (3)","HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO OUTROS","TENTATIVA DE HOMICÍDIO","LESÃO CORPORAL SEGUIDA DE MORTE","LESÃO CORPORAL DOLOSA","LESÃO CORPORAL CULPOSA POR ACIDENTE DE TRÂNSITO","LESÃO CORPORAL CULPOSA - OUTRAS","LATROCÍNIO","Nº DE VÍTIMAS EM LATROCÍNIO","TOTAL DE ESTUPRO (4)","ESTUPRO","ESTUPRO DE VULNERÁVEL","TOTAL DE ROUBO - OUTROS (1)","ROUBO - OUTROS","ROUBO DE VEÍCULO","ROUBO A BANCO","ROUBO DE CARGA","FURTO - OUTROS","FURTO DE VEÍCULO"]
ano = [2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020]
regiao = ["Sorocaba","Sorocaba","Sorocaba","Sorocaba","Sorocaba","Sorocaba","Sorocaba","Sorocaba","Sorocaba","Sorocaba","Sorocaba","Sorocaba","Sorocaba","Sorocaba","Sorocaba","Sorocaba","Sorocaba","Sorocaba","Sorocaba","Sorocaba","Sorocaba","Sorocaba","Sorocaba"]
meses_total = [192,203,0,0,361,11,225,8,7849,3247,105,12,13,1192,249,943,3098,3010,658,1,87,17409,2068]

df_sorocaba2020 = pd.DataFrame({"Natureza": natureza, "Ano": ano,"Região": regiao, "Total dos meses": meses_total})


#====================================================PRESIDENTE PRUDENTE============================================================#

natureza = ["HOMICÍDIO DOLOSO (2)", "Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO (3)","HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO OUTROS","TENTATIVA DE HOMICÍDIO","LESÃO CORPORAL SEGUIDA DE MORTE","LESÃO CORPORAL DOLOSA","LESÃO CORPORAL CULPOSA POR ACIDENTE DE TRÂNSITO","LESÃO CORPORAL CULPOSA - OUTRAS","LATROCÍNIO","Nº DE VÍTIMAS EM LATROCÍNIO","TOTAL DE ESTUPRO (4)","ESTUPRO","ESTUPRO DE VULNERÁVEL","TOTAL DE ROUBO - OUTROS (1)","ROUBO - OUTROS","ROUBO DE VEÍCULO","ROUBO A BANCO","ROUBO DE CARGA","FURTO - OUTROS","FURTO DE VEÍCULO"]
ano = [2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021]
regiao = ["Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente"]
meses_total = [60,62,0,0,92,1,90,0,4533,2883,84,3,3,354,80,274,361,341,40,0,20,7687,358]

df_presidente_prudente2021 = pd.DataFrame({"Natureza": natureza, "Ano": ano,"Região": regiao, "Total dos meses": meses_total})

natureza = ["HOMICÍDIO DOLOSO (2)", "Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO (3)","HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO OUTROS","TENTATIVA DE HOMICÍDIO","LESÃO CORPORAL SEGUIDA DE MORTE","LESÃO CORPORAL DOLOSA","LESÃO CORPORAL CULPOSA POR ACIDENTE DE TRÂNSITO","LESÃO CORPORAL CULPOSA - OUTRAS","LATROCÍNIO","Nº DE VÍTIMAS EM LATROCÍNIO","TOTAL DE ESTUPRO (4)","ESTUPRO","ESTUPRO DE VULNERÁVEL","TOTAL DE ROUBO - OUTROS (1)","ROUBO - OUTROS","ROUBO DE VEÍCULO","ROUBO A BANCO","ROUBO DE CARGA","FURTO - OUTROS","FURTO DE VEÍCULO"]
ano = [2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020]
regiao = ["Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente","Presidente Prudente"]
meses_total = [46,48,0,0,84,2,73,1,4593,2683,83,1,1,290,51,239,316,299,25,0,17,6101,316]

df_presidente_prudente2020 = pd.DataFrame({"Natureza": natureza, "Ano": ano,"Região": regiao, "Total dos meses": meses_total})

#======================================================PIRACICABA===============================================================#

natureza = ["HOMICÍDIO DOLOSO (2)", "Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO (3)","HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO OUTROS","TENTATIVA DE HOMICÍDIO","LESÃO CORPORAL SEGUIDA DE MORTE","LESÃO CORPORAL DOLOSA","LESÃO CORPORAL CULPOSA POR ACIDENTE DE TRÂNSITO","LESÃO CORPORAL CULPOSA - OUTRAS","LATROCÍNIO","Nº DE VÍTIMAS EM LATROCÍNIO","TOTAL DE ESTUPRO (4)","ESTUPRO","ESTUPRO DE VULNERÁVEL","TOTAL DE ROUBO - OUTROS (1)","ROUBO - OUTROS","ROUBO DE VEÍCULO","ROUBO A BANCO","ROUBO DE CARGA","FURTO - OUTROS","FURTO DE VEÍCULO"]
ano = [2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021]
regiao = ["Piracicaba","Piracicaba","Piracicaba","Piracicaba","Piracicaba","Piracicaba","Piracicaba","Piracicaba","Piracicaba","Piracicaba","Piracicaba","Piracicaba","Piracicaba","Piracicaba","Piracicaba","Piracicaba","Piracicaba","Piracicaba","Piracicaba","Piracicaba","Piracicaba","Piracicaba","Piracicaba"]
meses_total = [229,240,1,2,312,6,257,4,8812,6840,110,6,6,708,154,554,5114,4927,1485,1,186,24896,4434]

df_piracicaba2021 = pd.DataFrame({"Natureza": natureza, "Ano": ano,"Região": regiao, "Total dos meses": meses_total})

natureza = ["HOMICÍDIO DOLOSO (2)", "Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO (3)","HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO OUTROS","TENTATIVA DE HOMICÍDIO","LESÃO CORPORAL SEGUIDA DE MORTE","LESÃO CORPORAL DOLOSA","LESÃO CORPORAL CULPOSA POR ACIDENTE DE TRÂNSITO","LESÃO CORPORAL CULPOSA - OUTRAS","LATROCÍNIO","Nº DE VÍTIMAS EM LATROCÍNIO","TOTAL DE ESTUPRO (4)","ESTUPRO","ESTUPRO DE VULNERÁVEL","TOTAL DE ROUBO - OUTROS (1)","ROUBO - OUTROS","ROUBO DE VEÍCULO","ROUBO A BANCO","ROUBO DE CARGA","FURTO - OUTROS","FURTO DE VEÍCULO"]
ano = [2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020]
regiao = ["Piracicaba","Piracicaba","Piracicaba","Piracicaba","Piracicaba","Piracicaba","Piracicaba","Piracicaba","Piracicaba","Piracicaba","Piracicaba","Piracicaba","Piracicaba","Piracicaba","Piracicaba","Piracicaba","Piracicaba","Piracicaba","Piracicaba","Piracicaba","Piracicaba","Piracicaba","Piracicaba"]
meses_total = [220,227,2,3,268,16,208,10,8878,6203,95,6,6,648,173,475,5080,4893,1450,0,187,20115,4363]

df_piracicaba2020 = pd.DataFrame({"Natureza": natureza, "Ano": ano,"Região": regiao, "Total dos meses": meses_total})

#=========================================================ARAÇATUBA==============================================================#

natureza = ["HOMICÍDIO DOLOSO (2)", "Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO (3)","HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO OUTROS","TENTATIVA DE HOMICÍDIO","LESÃO CORPORAL SEGUIDA DE MORTE","LESÃO CORPORAL DOLOSA","LESÃO CORPORAL CULPOSA POR ACIDENTE DE TRÂNSITO","LESÃO CORPORAL CULPOSA - OUTRAS","LATROCÍNIO","Nº DE VÍTIMAS EM LATROCÍNIO","TOTAL DE ESTUPRO (4)","ESTUPRO","ESTUPRO DE VULNERÁVEL","TOTAL DE ROUBO - OUTROS (1)","ROUBO - OUTROS","ROUBO DE VEÍCULO","ROUBO A BANCO","ROUBO DE CARGA","FURTO - OUTROS","FURTO DE VEÍCULO"]
ano = [2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021]
regiao = ["Araçatuba","Araçatuba","Araçatuba","Araçatuba","Araçatuba","Araçatuba","Araçatuba","Araçatuba","Araçatuba","Araçatuba","Araçatuba","Araçatuba","Araçatuba","Araçatuba","Araçatuba","Araçatuba","Araçatuba","Araçatuba","Araçatuba","Araçatuba","Araçatuba","Araçatuba","Araçatuba"]
meses_total = [83,86,0,0,68,1,124,2,2527,2397,33,4,5,221,50,171,625,615,36,1,9,7451,384]

df_aracatuba2021 = pd.DataFrame({"Natureza": natureza, "Ano": ano,"Região": regiao, "Total dos meses": meses_total})

natureza = ["HOMICÍDIO DOLOSO (2)", "Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO (3)","HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO OUTROS","TENTATIVA DE HOMICÍDIO","LESÃO CORPORAL SEGUIDA DE MORTE","LESÃO CORPORAL DOLOSA","LESÃO CORPORAL CULPOSA POR ACIDENTE DE TRÂNSITO","LESÃO CORPORAL CULPOSA - OUTRAS","LATROCÍNIO","Nº DE VÍTIMAS EM LATROCÍNIO","TOTAL DE ESTUPRO (4)","ESTUPRO","ESTUPRO DE VULNERÁVEL","TOTAL DE ROUBO - OUTROS (1)","ROUBO - OUTROS","ROUBO DE VEÍCULO","ROUBO A BANCO","ROUBO DE CARGA","FURTO - OUTROS","FURTO DE VEÍCULO"]
ano = [2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020]
regiao = ["Araçatuba","Araçatuba","Araçatuba","Araçatuba","Araçatuba","Araçatuba","Araçatuba","Araçatuba","Araçatuba","Araçatuba","Araçatuba","Araçatuba","Araçatuba","Araçatuba","Araçatuba","Araçatuba","Araçatuba","Araçatuba","Araçatuba","Araçatuba","Araçatuba","Araçatuba","Araçatuba"]
meses_total = [65,69,1,2,91,1,139,2,2513,2342,54,3,3,218,47,171,556,546,44,0,10,6383,418]

df_aracatuba2020 = pd.DataFrame({"Natureza": natureza, "Ano": ano,"Região": regiao, "Total dos meses": meses_total})

#======================================================Junção DataFrames============================================================#

df_capital = pd.merge(df_capital2021, df_capital2020, how = 'outer')
df_grande_sp = pd.merge(df_grande_sp2021, df_grande_sp2020, how = 'outer')
df_sao_jose_campos = pd.merge(df_sao_jose_campos2021, df_sao_jose_campos2020, how = 'outer')
df_campinas = pd.merge(df_campinas2021, df_campinas2020, how = 'outer')
df_ribeirao = pd.merge(df_ribeirao2021, df_ribeirao2020, how = 'outer')
df_bauru = pd.merge(df_bauru2021, df_bauru2020, how = 'outer')
df_sao_jose_riopreto = pd.merge(df_sao_jose_riopreto2021, df_sao_jose_riopreto2020, how = 'outer')
df_santos = pd.merge(df_santos2021, df_santos2020, how = 'outer')
df_sorocaba = pd.merge(df_sorocaba2021, df_sorocaba2020, how = 'outer')
df_presidente_prudente = pd.merge(df_presidente_prudente2021, df_presidente_prudente2020, how = 'outer')
df_piracicaba = pd.merge(df_piracicaba2021, df_piracicaba2020, how = 'outer')
df_aracatuba = pd.merge(df_aracatuba2021, df_aracatuba2020, how = 'outer')


df_part1 = pd.merge(df_capital, df_grande_sp, how = 'outer')
df_part2 = pd.merge(df_sao_jose_campos, df_campinas, how = 'outer')
df_part3 = pd.merge(df_ribeirao, df_bauru, how = 'outer')
df_part4 = pd.merge(df_sao_jose_riopreto, df_santos, how = 'outer')
df_part5 = pd.merge(df_sorocaba, df_presidente_prudente, how = 'outer')
df_part6 = pd.merge(df_piracicaba, df_aracatuba, how = 'outer')



df_part7 = pd.merge(df_part1, df_part2, how = 'outer')
df_part8 = pd.merge(df_part3, df_part4, how = 'outer')
df_part9 = pd.merge(df_part5, df_part6, how = 'outer')

df_part10 = pd.merge(df_part7, df_part8, how = 'outer')
df_completo = pd.merge(df_part9, df_part10, how = 'outer')

df_completo


# In[18]:


#Converter DataFrame para CSV

df_completo.to_csv("Dados_Ocorrencias_Mes")


# In[227]:


#As três regiões com mais homicídios dolosos (2020-2021)

df_completo[df_completo['Natureza']=="HOMICÍDIO DOLOSO (2)"].nlargest(3, 'Total dos meses')


# # Tentativas para finalização do teste

# 

# In[240]:


df = df_completo[(df_completo.Natureza == "HOMICÍDIO DOLOSO (2)") & (df_completo.Região == "Capital") & (df_completo.Ano == 2021)]
df2 = df.assign(d_minus = df['Total dos meses'] - df1['Total dos meses'])
df2


# In[15]:


df = df_completo[(df_completo.Natureza == "HOMICÍDIO DOLOSO (2)") & (df_completo.Região == "Grande São Paulo")]
df["Total dos meses"].sum()


# In[17]:


df2 = df_completo[(df_completo.Natureza == "HOMICÍDIO DOLOSO (2)") & (df_completo.Região == "São José dos Campos")]
df2["Total dos meses"].sum()


# In[16]:


df3 = df_completo[(df_completo.Natureza == "HOMICÍDIO DOLOSO (2)") & (df_completo.Região == "Campinas")]
df3["Total dos meses"].sum()


# In[ ]:




