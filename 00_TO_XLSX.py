import os, pandas as pd, time

start_t = time.time()

df = pd.DataFrame(columns=["Book Name", "Data"])

bList = [x for x in os.listdir() if x.endswith('.txt')]

for bName in bList:
  with open(f'{bName}', 'r', encoding='utf8') as book :
    btxt = [line.replace('\n', ' ') for line in book]

  t = str()
  for line in btxt:
    for x in line:
      if (2431 < ord(x) < 2559) or ord(x) == 32:
        if (not 2533 < ord(x) < 2544) and (not ord(x) == 2551):
          t = t + x
          # print(x, end='')
  t_final = t.replace('    ', ' ').replace('   ', ' ').replace('  ', ' ')

  tmpDF = pd.DataFrame([[bName[:-4], t_final]], columns=["Book Name", "Data"])
  df = pd.concat([df,tmpDF])
  # print(df)



df.to_excel("output.xlsx", encoding="utf8", index=False)  

end_t = time.time()

print("\n\n\tTime Taken = " + str(end_t - start_t) + " secounds\n")
