from langchain_google_genai import GoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
import os

# # Retrieve the Google API key from the environment variables
google_api_key = "AIzaSyAEeJbTi4icM4tF-ik0n5-x6GLMn9QVl9k"

llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=google_api_key, temperature=1.0)
# Define your prompts
# prompts = ['is it working']

# # Generate responses using the model
# llm_result = llm._generate(prompts)

# # Print the generated text
# print(llm_result.generations[0][0].text)



db_user = "ww"
db_password = "123"
db_host = "localhost"
db_name = "atliq_tshirts"
db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",sample_rows_in_table_info=3)

# print(db.table_info)

db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)
qns1 = db_chain.invoke("""SELECT sum(a.total_amount * ((100-COALESCE(discounts.pct_discount,0))/100)) as total_revenue from
(select sum(price*stock_quantity) as total_amount, t_shirt_id from t_shirts where brand = 'Nike' and size="L"
group by t_shirt_id) a left join discounts on a.t_shirt_id = discounts.t_shirt_id
 """)

#


