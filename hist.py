import pandas as pd
df = pd.read_csv("cc_18.csv",
                 names=["direction", "src", "dest"],low_memory=False)
df.drop(columns=['direction'])
print df

df =(df["src"].map(str) +"_"+ df["dest"].map(str)).value_counts()
print df
print df.value_counts()


