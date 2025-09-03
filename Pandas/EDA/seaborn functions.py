
sns.regplot(x = 'header_1',y = 'header_2',data= df)

sns.residplot(data=df,x='header_1', y='header_2')
# Alternatively:
sns.residplot(x=df['header_1'], y=df['header_2'])

sns.kdeplot(X)

sns.distplot(X,hist=False)

