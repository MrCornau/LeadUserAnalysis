
#%%
NewNew = df
identifyer = []
for idx, row in df.iterrows():
    identifyer.append(idx)

print(len(identifyer))
# NewNew.head()

# %%
NewNew['identifyer'] = identifyer
NewNew.head()

#%%
NewNew.to_csv('ReditCore_ID.csv')
# %%