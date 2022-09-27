import requests
# pretty print is used to print the output in the console in an easy to read format
from pprint import pprint
import json
import pandas as pd


# function to use requests.post to make an API call to the subgraph url
# def run_query(q):

#     # endpoint where you are making the request
#     request = requests.post('https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2'
#                             '',
#                             json={'query': query})
#     if request.status_code == 200:
#         return request.json()
#     else:
#         raise Exception('Query failed. return code is {}.      {}'.format(request.status_code, query))


# The Graph query - Query Uniswap for a list of the top 10 pairs where the reserve is > 1000000 USD and the volume is >50000 USD
query = """

{
  pairs(first: 10, where: {reserveUSD_gt: "1000000", volumeUSD_gt: "50000"}, orderBy: reserveUSD, orderDirection: desc) {
    id
    token0 {
      id
      symbol
    }
    token1 {
      id
      symbol
    }
    reserveUSD
    volumeUSD
  }
}
"""

request = requests.post('https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2'
                            '',
                            json={'query': query})
json_data = json.loads(request.text)

# convert json into a dataframe
df = pd.DataFrame(json_data['data']['pairs'])

# check result
print(df)

# writing data to csv
df.iloc[:,0:4].to_csv("fetchedData.csv", index=False)

# # print the results
# print('Print Result - {}'.format(result))
# print('#############')
# # pretty print the results
# pprint(result)