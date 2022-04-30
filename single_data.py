import pandas as pd

# Firstly Let's merge all csvs data that we have using concat function in pandas
print('Merging all csvs data into one...')
df = pd.concat(
    map(pd.read_csv,
        ['data/daily_sales_data_0.csv', 'data/daily_sales_data_1.csv', 'data/daily_sales_data_2.csv']),
    ignore_index=True
)
# Initializing an empty list for sales
sales = []
print('Removing any product which is not pink morsel...')
# Removing any row that its product is not pink morsel
for i in range(len(df['product'])):
    if df['product'][i] != 'pink morsel':
        df.drop(i, inplace=True)
print('Products rows successfully removed.')
# Resetting index, so we can iterate again for our second loop (l:20)
df = df.reset_index()
# Dropping the old index
df = df.drop(['index'], axis=1)
# Iterating through every row price and multiply it by quantity, then adding it to the new list called sales
for j in range(len(df)):
    sales.append(int(float(df['price'][j].replace('$', '')) * df['quantity'][j]))

# Dropping useless columns
df = df.drop(['price', 'quantity', 'product'], axis=1)

# Adding a new column called sales
df2 = df.assign(sales=sales)

# Saving result into a new csv file
last_df = pd.DataFrame(df2)
last_df.to_csv('data/clean_daily_sales_data.csv', index=False)  # Removing index by using index=False
print('Data has been successfully cleaned and saved into data\'s folder!')
